#!/usr/bin/env python3
"""
Extrai o inventário de imagens de uma página de venda, na ordem do DOM.

Página de venda esconde copy dentro de imagem. Balões de pensamento, print de
depoimento, headline de mockup, selo de garantia — nada disso está no HTML, e
quem lê só o texto mapeia a página errada. Este script resolve o lado mecânico:
descobre quais imagens existem, em que ordem, quais estão quebradas, e baixa
tudo pra você OLHAR uma a uma.

O que ele faz:
  - acha `<img>` (inclusive lazy-load: data-src, data-lazy-src, srcset) e
    `background-image:` em atributo style;
  - preserva a ordem de aparição e agrupa as duplicatas (Elementor duplica cada
    imagem em variante desktop/mobile — vira UMA linha com as duas posições);
  - baixa cada arquivo, mede dimensão real e detecta 404/erro;
  - converte AVIF/WEBP pra PNG via `sips` (macOS) quando disponível, porque
    nem todo leitor de imagem abre esses formatos.

Uso:
    python3 extrair_imagens.py <url> [--out PASTA]
    python3 extrair_imagens.py <arquivo.html> [--base https://dominio.com]
    python3 extrair_imagens.py <url> --no-download    # só o manifesto

Sem dependências externas — só stdlib (+ `sips`, opcional, pra AVIF/WEBP).
"""

import argparse
import pathlib
import re
import shutil
import struct
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from html import unescape

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)

# Ordem importa: o primeiro atributo que trouxer URL real ganha. `src` vem por
# último porque em página com lazy-load ele carrega o placeholder SVG inline.
SRC_ATTRS = ("data-lazy-src", "data-src", "data-original", "data-lazy-srcset", "srcset", "src")

# Imagens que não são conteúdo da página.
RUIDO = re.compile(
    r"(facebook\.com/tr|google-analytics|googletagmanager|/pixel|"
    r"\.gif$|spacer|blank\.png|1x1\.)",
    re.IGNORECASE,
)

CONVERTIVEIS = {".avif", ".webp", ".heic"}

# WordPress serve o mesmo arquivo em vários tamanhos (`foto-1024x576.png`,
# `foto-300x204.png`, `foto-150x150.png`). São a MESMA imagem — agrupar é o que
# separa um inventário de 22 peças de design de uma lista de 53 arquivos.
SUFIXO_TAMANHO = re.compile(r"-(\d{2,4})x(\d{2,4})(?=\.[a-z0-9]+$)", re.IGNORECASE)


def achar_urls(html: str):
    """Devolve [(posicao, url, alt)] na ordem do DOM, sem dedupe."""
    achados = []

    for m in re.finditer(r"<img\b[^>]*>", html, flags=re.IGNORECASE):
        tag = m.group(0)
        url = None
        for attr in SRC_ATTRS:
            v = re.search(rf'{attr}=["\']([^"\']+)["\']', tag, flags=re.IGNORECASE)
            if not v:
                continue
            cand = v.group(1).strip()
            if attr in ("srcset", "data-lazy-srcset"):
                # "a.png 480w, b.png 1024w" — pega a maior declarada (a última).
                cand = cand.split(",")[-1].strip().split(" ")[0]
            if cand.startswith("data:"):
                continue  # placeholder inline de lazy-load
            url = cand
            break
        if not url:
            continue
        alt = re.search(r'alt=["\']([^"\']*)["\']', tag, flags=re.IGNORECASE)
        achados.append((m.start(), unescape(url), unescape(alt.group(1)) if alt else ""))

    # background-image em style inline — muito usado em hero e em bloco de fundo.
    for m in re.finditer(r"background-image\s*:\s*url\(([^)]+)\)", html, flags=re.IGNORECASE):
        url = m.group(1).strip("\"' ")
        if not url.startswith("data:"):
            achados.append((m.start(), unescape(url), "[background-image]"))

    achados.sort(key=lambda x: x[0])
    return achados


def dimensoes(caminho: pathlib.Path):
    """Largura×altura lendo só o cabeçalho. PNG, JPEG e GIF."""
    try:
        with open(caminho, "rb") as f:
            head = f.read(32)
            if head[:8] == b"\x89PNG\r\n\x1a\n":
                w, h = struct.unpack(">II", head[16:24])
                return w, h
            if head[:3] == b"\xff\xd8\xff":
                f.seek(2)
                while True:
                    marker = f.read(2)
                    if len(marker) < 2 or marker[0] != 0xFF:
                        return None
                    if marker[1] in range(0xC0, 0xCF) and marker[1] not in (0xC4, 0xC8, 0xCC):
                        f.read(3)
                        h, w = struct.unpack(">HH", f.read(4))
                        return w, h
                    (size,) = struct.unpack(">H", f.read(2))
                    f.seek(size - 2, 1)
            if head[:6] in (b"GIF87a", b"GIF89a"):
                w, h = struct.unpack("<HH", head[6:10])
                return w, h
    except Exception:
        return None
    return None


def converter(caminho: pathlib.Path):
    """AVIF/WEBP -> PNG via sips. Devolve o novo caminho ou None."""
    if caminho.suffix.lower() not in CONVERTIVEIS or not shutil.which("sips"):
        return None
    destino = caminho.with_suffix(".png")
    r = subprocess.run(
        ["sips", "-s", "format", "png", str(caminho), "--out", str(destino)],
        capture_output=True,
    )
    return destino if r.returncode == 0 and destino.exists() else None


def baixar(url: str, destino: pathlib.Path):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            destino.write_bytes(r.read())
        return 200, None
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:
        return None, str(e)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("alvo", help="URL da página ou caminho de um .html local")
    ap.add_argument("--out", default="imgs", help="pasta de destino (padrão: imgs/)")
    ap.add_argument("--base", default="", help="URL base pra resolver caminho relativo em HTML local")
    ap.add_argument("--no-download", action="store_true", help="só lista, não baixa")
    args = ap.parse_args()

    if args.alvo.startswith("http"):
        req = urllib.request.Request(args.alvo, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode("utf-8", errors="ignore")
        base = args.base or args.alvo
    else:
        html = pathlib.Path(args.alvo).read_text(encoding="utf-8", errors="ignore")
        base = args.base

    achados = achar_urls(html)

    # Dedupe preservando ordem. A chave ignora o sufixo de tamanho do WordPress,
    # então as 4 variantes de `foto-1024x576.png` viram uma linha só — e a URL
    # que fica é a da MAIOR variante vista (mais pixel = mais copy legível).
    ordem, grupos = [], {}
    for pos, url, alt in achados:
        if RUIDO.search(url):
            continue
        full = urllib.parse.urljoin(base, url) if base else url
        nome = urllib.parse.unquote(full.split("/")[-1].split("?")[0])
        m = SUFIXO_TAMANHO.search(nome)
        chave = SUFIXO_TAMANHO.sub("", full)
        area = int(m.group(1)) * int(m.group(2)) if m else 10**9  # sem sufixo = original

        if chave not in grupos:
            ordem.append(chave)
            grupos[chave] = {"url": full, "area": area, "pos": [], "alt": alt, "variantes": 0}
        g = grupos[chave]
        g["pos"].append(pos)
        g["variantes"] += 1
        if area > g["area"]:
            g["url"], g["area"] = full, area
        if alt and not g["alt"]:
            g["alt"] = alt

    print(f"# Inventário de imagem — {args.alvo}")
    print(f"# {len(achados)} tags no DOM · {len(ordem)} imagens distintas "
          f"(variantes de tamanho agrupadas)\n")

    out = pathlib.Path(args.out)
    if not args.no_download:
        out.mkdir(parents=True, exist_ok=True)

    quebradas = []
    for i, chave in enumerate(ordem, 1):
        g = grupos[chave]
        url = g["url"]
        nome = urllib.parse.unquote(url.split("/")[-1].split("?")[0]) or f"img{i}"
        # Quantos LUGARES da página usam a imagem — o que interessa é reuso de
        # bloco (a composição "tudão" que aparece 3×), não variante de tamanho.
        repete = len(set(g["pos"]))
        marca = f" · reaparece em {repete} pontos da página" if repete > 1 else ""
        alt = f" · alt=\"{g['alt']}\"" if g["alt"] else ""

        if args.no_download:
            print(f"{i:02d}. {nome}{marca}{alt}\n    {url}")
            continue

        destino = out / nome
        status, erro = baixar(url, destino)
        if status != 200:
            quebradas.append((nome, status or erro))
            print(f"{i:02d}. 🔴 {nome}{marca} — HTTP {status or erro} · IMAGEM QUEBRADA")
            print(f"    {url}")
            destino.unlink(missing_ok=True)
            continue

        dim = dimensoes(destino)
        dim_txt = f"{dim[0]}×{dim[1]}" if dim else "?"
        kb = destino.stat().st_size // 1024
        linha = f"{i:02d}. {nome}{marca} · {dim_txt} · {kb} KB{alt}"

        convertido = converter(destino)
        if convertido:
            linha += f"\n    ↳ convertido pra {convertido.name} (leia esse)"
        elif destino.suffix.lower() in CONVERTIVEIS:
            linha += ("\n    ⚠️  não deu pra converter (sem `sips`, fora do Mac). "
                      "Tente ler assim mesmo; se não abrir, peça um print desse trecho da página.")
        print(linha)
        print(f"    {destino}")

    if quebradas and not args.no_download:
        print(f"\n## ⚠️  {len(quebradas)} imagem(ns) quebrada(s) — vira BLOQUEIO no raio-X")
        for nome, motivo in quebradas:
            print(f"   - {nome} ({motivo})")

    if not args.no_download:
        print(f"\n## Próximo passo obrigatório")
        print(f"   Leia CADA arquivo de {out}/ com a ferramenta de leitura de imagem.")
        print(f"   Baixar não é ler — a copy da página está dentro desses arquivos.")


if __name__ == "__main__":
    sys.exit(main())
