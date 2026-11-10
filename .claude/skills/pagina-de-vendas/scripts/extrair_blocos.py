#!/usr/bin/env python3
"""
Extrai o esqueleto estrutural de páginas de venda em HTML.

Devolve, por arquivo, a lista de blocos na ordem em que aparecem — com o
comentário do bloco (quando existe), a tag/classe do container, headlines,
primeiras linhas de texto, CTAs, contagem de itens de lista, accordions de FAQ
e placeholders de imagem.

O objetivo é remover o ruído (CSS, atributos de estilo, markup repetido) e
deixar só o que importa pra ler a estrutura de persuasão da página.

Uso:
    python3 extrair_blocos.py <arquivo.html>
    python3 extrair_blocos.py <pasta/>
    python3 extrair_blocos.py <a.html> <b.html> --largura 100

Sem dependências externas — só stdlib.
"""

import argparse
import pathlib
import re
import sys
from html.parser import HTMLParser
from html import unescape

# Containers que abrem um bloco novo.
BOUNDARY_TAGS = {"section", "footer", "header", "article", "main"}

# Tags cujo texto interessa capturar.
TEXT_TAGS = {"h1", "h2", "h3", "h4", "p", "li", "summary", "a", "span", "div", "b", "strong"}

# Tags ignoradas por completo (conteúdo e tudo). Só entram aqui tags que TÊM
# fechamento — void tags aqui deixariam o contador de "zona morta" preso pra sempre.
DEAD_TAGS = {"style", "script", "head", "title", "noscript", "svg"}

# Void tags: não abrem nem fecham nada, só são anotadas ou ignoradas.
VOID_TAGS = {"meta", "link", "br", "img", "input", "source", "hr", "col", "embed", "area", "base"}

# Classes que costumam marcar placeholder de imagem em mockup/wireframe.
PLACEHOLDER_HINTS = ("ph", "slot", "placeholder", "img-slot", "foto", "imagem")

# Texto que denuncia um placeholder mesmo sem classe reveladora.
PLACEHOLDER_TEXT = re.compile(
    r"^\s*(FOTO|IMAGEM|IMG|MOCKUP|PRINT|CAPA|V[IÍ]DEO|ANIMA[ÇC][ÃA]O|BANNER|ICONE|[ÍI]CONE)\b",
    re.IGNORECASE,
)

CTA_HINT = re.compile(r"\b(cta|botao|botão|btn|buy|comprar|assinar)\b", re.IGNORECASE)


def squash(text: str) -> str:
    """Colapsa espaços e normaliza quebras vindas de <br> e indentação."""
    text = re.sub(r"\s+", " ", unescape(text)).strip()
    # Ao subir texto de <b>/<span> pro pai a gente insere espaços de segurança;
    # aqui a pontuação volta a encostar na palavra.
    return re.sub(r"\s+([,.;:!?%)\]])", r"\1", text)


def clip(text: str, width: int) -> str:
    text = squash(text)
    return text if len(text) <= width else text[: width - 1].rstrip() + "…"


class Block:
    def __init__(self, comment, tag, classes, line):
        self.comment = comment
        self.tag = tag
        self.classes = classes
        self.line = line
        self.items = []      # (rótulo, texto)
        self.li_count = 0
        self.li_samples = []
        self.details_count = 0

    @property
    def empty(self):
        return not self.items and not self.li_count and not self.details_count


class SkeletonParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks = []
        self.pending_comment = None
        self.dead_depth = 0
        self.capture_stack = []   # (tag, classes, buffer, href)
        self.current = None
        self.seen_h1 = False

    # ---------- infraestrutura ----------

    def _block(self):
        if self.current is None:
            self.current = Block(self.pending_comment, "(sem container)", "", self.getpos()[0])
            self.pending_comment = None
        return self.current

    def _flush_block(self):
        if self.current is not None and not self.current.empty:
            self.blocks.append(self.current)
        self.current = None

    # ---------- callbacks ----------

    def handle_comment(self, data):
        if self.dead_depth:
            return
        text = squash(re.sub(r"[═─=~*#·•]{2,}", "", data))
        # Comentário que carrega copy alternativa inteira não é rótulo de bloco.
        if text and len(text) <= 120:
            self.pending_comment = text
        elif text:
            self._block().items.append(("NOTA", text))

    def handle_starttag(self, tag, attrs):
        if tag in DEAD_TAGS:
            self.dead_depth += 1
            return
        if self.dead_depth:
            return

        if tag in VOID_TAGS:
            self._handle_void(tag, dict(attrs))
            return

        attrd = dict(attrs)
        classes = attrd.get("class", "")

        if tag in BOUNDARY_TAGS:
            self._flush_block()
            self.current = Block(self.pending_comment, tag, classes, self.getpos()[0])
            self.pending_comment = None
            return

        if tag == "details":
            self._block().details_count += 1

        if tag in TEXT_TAGS:
            # [tag, classes, buffer, href, nº de filhos que já viraram item]
            self.capture_stack.append([tag, classes, [], attrd.get("href", ""), 0])

    def handle_startendtag(self, tag, attrs):
        if self.dead_depth:
            return
        if tag in VOID_TAGS:
            self._handle_void(tag, dict(attrs))
            return
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def _handle_void(self, tag, attrd):
        """<br> vira espaço; <img> real vira item; o resto é descartado."""
        if tag == "br":
            if self.capture_stack:
                self.capture_stack[-1][2].append(" ")
            return
        if tag == "img":
            src = attrd.get("src", "")
            alt = attrd.get("alt", "")
            desc = f'{src}{f"  (alt: {alt})" if alt else ""}'
            if desc.strip():
                self._block().items.append(("IMG", desc))

    def handle_endtag(self, tag):
        if tag in DEAD_TAGS:
            self.dead_depth = max(0, self.dead_depth - 1)
            return
        if self.dead_depth:
            return

        if tag in BOUNDARY_TAGS:
            self._flush_block()
            return

        for i in range(len(self.capture_stack) - 1, -1, -1):
            if self.capture_stack[i][0] == tag:
                frame = self.capture_stack.pop(i)
                # Texto de filho sobe pro pai, pra não perder <b> dentro de <p>.
                # Espaço nas duas pontas: no HTML compactado "<b>FOTO 01</b>LOGO"
                # sem isso viraria "FOTO 01LOGO".
                text = squash("".join(frame[2]))
                if self.capture_stack and text:
                    self.capture_stack[-1][2].append(" " + text + " ")
                if self._record(frame[0], frame[1], text, frame[3], frame[4]):
                    for parent in self.capture_stack:
                        parent[4] += 1
                break

    def handle_data(self, data):
        if self.dead_depth or not self.capture_stack:
            return
        self.capture_stack[-1][2].append(data)

    # ---------- classificação ----------

    def _record(self, tag, classes, text, href, child_records):
        """Classifica um elemento fechado. Devolve True se virou item do bloco."""
        if not text:
            return False
        block = self._block()
        cls_tokens = classes.lower().split()

        # Classe reveladora vale sempre. Já o texto ("FOTO 03 — mockup…") só vale
        # em elemento-folha: senão a <div class="wrap"> que ENVOLVE o placeholder
        # herda o texto do filho e o bloco ganha um duplicado inútil.
        is_placeholder = any(h in cls_tokens for h in PLACEHOLDER_HINTS) or (
            child_records == 0 and bool(PLACEHOLDER_TEXT.match(text))
        )

        if tag == "a" and (CTA_HINT.search(classes) or (text.isupper() and len(text) > 8)):
            block.items.append(("CTA", f'"{text}" → {href or "(sem href)"}'))
        elif tag == "h1":
            self.seen_h1 = True
            block.items.append(("H1", text))
        elif tag in ("h2", "h3", "h4"):
            block.items.append((tag.upper(), text))
        elif tag == "summary":
            block.items.append(("FAQ", text))
        elif is_placeholder and tag in ("div", "span", "p"):
            block.items.append(("IMG", text))
        elif tag == "li":
            block.li_count += 1
            if len(block.li_samples) < 2:
                block.li_samples.append(text)
        elif tag == "p":
            block.items.append(("P", text))
        else:
            # span/div/b comuns são ruído estrutural: não viram item.
            return False
        return True


def render(path: pathlib.Path, width: int) -> str:
    raw = path.read_text(encoding="utf-8", errors="replace")
    parser = SkeletonParser()
    parser.feed(raw)
    parser._flush_block()

    lines = []
    header = f"ARQUIVO: {path.name}"
    meta = f"{len(parser.blocks)} blocos · {raw.count(chr(10)) + 1} linhas"
    lines.append("=" * 78)
    lines.append(header)
    lines.append(meta)
    lines.append("=" * 78)

    for n, b in enumerate(parser.blocks, 1):
        lines.append("")
        label = b.comment or "(sem comentário)"
        cls = f".{b.classes.split()[0]}" if b.classes else ""
        lines.append(f"[B{n:02d}]  {label}")
        lines.append(f"       <{b.tag}{cls}>  linha {b.line}")

        for rotulo, texto in b.items:
            lines.append(f"       {rotulo:<4} {clip(texto, width)}")

        if b.li_count:
            amostra = "  ·  ".join(f'"{clip(s, width // 2)}"' for s in b.li_samples)
            lines.append(f"       LI×{b.li_count:<2}  {amostra}")

        if b.details_count:
            lines.append(f"       ACCORDIONS: {b.details_count}")

    lines.append("")
    return "\n".join(lines)


def collect(targets):
    files = []
    for t in targets:
        p = pathlib.Path(t).expanduser()
        if p.is_dir():
            files.extend(sorted(p.glob("*.html")) + sorted(p.glob("*.htm")))
        elif p.exists():
            files.append(p)
        else:
            print(f"[aviso] não encontrei: {p}", file=sys.stderr)
    return files


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("alvos", nargs="+", help="arquivos .html ou pasta contendo eles")
    ap.add_argument("--largura", type=int, default=110, help="corte de cada linha de texto (padrão: 110)")
    args = ap.parse_args()

    files = collect(args.alvos)
    if not files:
        print("Nenhum HTML encontrado.", file=sys.stderr)
        sys.exit(1)

    for f in files:
        print(render(f, args.largura))


if __name__ == "__main__":
    main()
