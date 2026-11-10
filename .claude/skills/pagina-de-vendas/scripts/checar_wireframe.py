#!/usr/bin/env python3
"""
Confere um wireframe de copy antes da entrega.

Pega o que costuma quebrar na hora de publicar e o que denuncia trabalho pela
metade: charset faltando, slot de imagem fora de ordem, botão morto, dependência
externa que não vai carregar, colchete deixado no corpo sem nota de produção.

Uso:
    python3 checar_wireframe.py <arquivo.html>

Saída: lista de problemas por gravidade. Código 1 se houver ERRO, 0 se só AVISO.
Sem dependências externas — só stdlib.
"""

import argparse
import pathlib
import re
import sys

ERRO, AVISO, OK = "ERRO ", "AVISO", "  ok "


def checar(html: str) -> list[tuple[str, str]]:
    achados: list[tuple[str, str]] = []

    def erro(msg):
        achados.append((ERRO, msg))

    def aviso(msg):
        achados.append((AVISO, msg))

    # Markup só conta quando é markup de verdade: um "<section>" citado dentro de
    # um comentário explicativo não abre bloco nenhum. Checagens estruturais usam
    # esta versão; as que leem rastreabilidade usam o html cru.
    limpo = re.sub(r"<!--.*?-->", " ", html, flags=re.S)

    # ── charset ────────────────────────────────────────────────────────────
    # Sem isso acento e emoji viram caractere quebrado quando a página sobe.
    if not re.search(r'<meta\s+charset=["\']?utf-8', html, re.I):
        erro('falta <meta charset="UTF-8"> no <head> — acentos e emojis vão quebrar no ar')

    # ── dependências externas ──────────────────────────────────────────────
    # Wireframe precisa abrir offline e sobreviver a CSP restritiva.
    externos = re.findall(r'(?:src|href)=["\'](https?://[^"\']+)["\']', html)
    externos = [u for u in externos if not u.startswith("mailto:")]
    for u in sorted(set(externos)):
        aviso(f"dependência externa: {u} — inline o recurso ou aceite que pode não carregar")

    # ── slots de imagem ────────────────────────────────────────────────────
    nums = [int(n) for n in re.findall(r"<b[^>]*>\s*FOTO\s+(\d+)", html, re.I)]
    if not nums:
        aviso("nenhum slot FOTO NN encontrado — wireframe sem briefing de imagem?")
    else:
        vistos, repetidos = set(), set()
        for n in nums:
            (repetidos if n in vistos else vistos).add(n)
        if repetidos:
            erro(f"slot repetido: FOTO {', '.join(f'{n:02d}' for n in sorted(repetidos))}")
        esperado = list(range(1, max(nums) + 1))
        faltando = sorted(set(esperado) - vistos)
        if faltando:
            erro(f"buraco na numeração: falta FOTO {', '.join(f'{n:02d}' for n in faltando)}")
        if nums != sorted(nums):
            aviso("slots fora de ordem no documento — quem produzir vai se perder")

    # slot sem briefing de verdade. Logo e ícone se explicam em três palavras —
    # a exigência de briefing é para foto, mockup e depoimento.
    simples = re.compile(r"\b(LOGO|LOGOMARCA|[IÍ]CONE|ICON|SELO|BADGE|FAVICON)\b", re.I)
    for corpo in re.findall(r'<div class="slot[^"]*"[^>]*>(.*?)</div>', html, re.S | re.I):
        texto = re.sub(r"<[^>]+>", " ", corpo)
        texto = re.sub(r"\s+", " ", texto).strip()
        if len(texto) < 40 and not simples.search(texto):
            aviso(f'slot com briefing curto demais: "{texto[:60]}" — diga enquadramento, quem aparece e o que prova')

    # ── botões ─────────────────────────────────────────────────────────────
    for m in re.finditer(r'<a[^>]*class=["\'][^"\']*\bcta\b[^"\']*["\'][^>]*>', limpo, re.I):
        tag = m.group(0)
        href = re.search(r'href=["\']([^"\']*)["\']', tag)
        if not href:
            erro("CTA sem href")
        elif href.group(1).strip() in ("#", ""):
            erro('CTA com href="#" — botão morto; use âncora real ou [CHECKOUT] + nota de produção')

    # ── colchetes não resolvidos no corpo visível ──────────────────────────
    # Placeholders dentro de atributo (href="[CHECKOUT]") são o padrão que a
    # skill manda usar — não são pendência de copy, não acusar.
    corpo = re.search(r"<body[^>]*>(.*)</body>", html, re.S | re.I)
    if corpo:
        visivel = re.sub(r"<!--.*?-->", "", corpo.group(1), flags=re.S)
        visivel = re.sub(r'<p[^>]*class=["\'][^"\']*\bnota\b[^"\']*["\'][^>]*>.*?</p>', "", visivel, flags=re.S | re.I)
        visivel = re.sub(r'\w+=["\'][^"\']*["\']', " ", visivel)  # tira atributos
        pendentes = set(re.findall(r"\[([A-ZÀ-Ú][^\]\n]{1,40})\]", visivel))
        for p in sorted(pendentes):
            aviso(f'"[{p}]" ficou no texto visível — resolva ou cubra com uma .nota explicando o que falta')

    # ── HTML quebrado ──────────────────────────────────────────────────────
    # O wireframe existe pra mostrar layout; uma tag aberta destrói justamente isso.
    void = {"br","img","meta","link","input","hr","source","col","area","base","embed","wbr"}
    pilha, desbalanceado = [], False
    for m in re.finditer(r"<(/?)([a-zA-Z][\w-]*)([^>]*?)(/?)>", limpo):
        fecha, tag, attrs, autofecha = m.group(1), m.group(2).lower(), m.group(3), m.group(4)
        if tag in void or autofecha:
            continue
        if not fecha:
            pilha.append(tag)
        else:
            if tag in pilha:
                while pilha and pilha.pop() != tag:
                    desbalanceado = True
            else:
                erro(f"</{tag}> fecha uma tag que não estava aberta")
                desbalanceado = True
    if pilha:
        erro(f"tag(s) sem fechamento: {', '.join(f'<{t}>' for t in pilha[:6])}")
    elif desbalanceado:
        aviso("tags fechadas fora de ordem — confira o aninhamento")

    # ── alternância de fundo ───────────────────────────────────────────────
    fundos = []
    for m in re.finditer(r"<section([^>]*)>", limpo, re.I):
        cls = re.search(r'class=["\']([^"\']*)["\']', m.group(1))
        cls = cls.group(1) if cls else ""
        fundos.append("dark" if "dark" in cls else "alt" if "alt" in cls else "normal")
    for i in range(1, len(fundos)):
        if fundos[i] == "alt" and fundos[i - 1] == "alt":
            aviso(f"blocos {i} e {i+1} são ambos .alt — sem contraste o olho perde o corte entre eles")

    # ── classe usada mas não definida no CSS ───────────────────────────────
    estilo = " ".join(re.findall(r"<style[^>]*>(.*?)</style>", limpo, re.S | re.I))
    definidas = set(re.findall(r"\.([a-zA-Z][\w-]*)", estilo))
    usadas = set()
    for m in re.findall(r'class=["\']([^"\']+)["\']', limpo):
        usadas.update(m.split())
    orfas = sorted(usadas - definidas)
    for c in orfas:
        erro(f'classe ".{c}" usada no corpo mas não existe no CSS — o bloco vai aparecer sem estilo')

    # ── contagem de itens por componente ───────────────────────────────────
    faixas = {
        "balao":    (4, 6, "balões (S5)"),
        "promessa": (4, 4, "promessas numeradas"),
        "pilar":    (3, 3, "pilares do mecanismo"),
        "sintoma":  (4, 6, "cards de sintoma (S3)"),
    }
    for cls, (mini, maxi, nome) in faixas.items():
        n = len(re.findall(rf'class=["\'][^"\']*\b{cls}\b', limpo))
        if n and not (mini <= n <= maxi):
            alvo = f"{mini}" if mini == maxi else f"{mini} a {maxi}"
            aviso(f"{n} {nome} — o formato pede {alvo}; ver references/blocos-html.md")
    faq = len(re.findall(r"<details", limpo, re.I))
    if faq and not (6 <= faq <= 8):
        aviso(f"{faq} perguntas no FAQ — o formato pede 6 a 8")

    # ── .nota usada como copy ──────────────────────────────────────────────
    # Nota é conversa com o cliente. Se não pede nada, provavelmente é copy
    # disfarçada ou desculpa pra não ter escrito o bloco.
    pedido = re.compile(
        # PT
        r"\b(preciso|precisa|confirm|me manda|manda|falta|faltam|definir|decidir|escolher|"
        r"validar|trocar|substituir|checar|conferir|enviar|mandar|"
        # ES — as páginas de cliente LATAM saem em espanhol
        r"necesit|hace falta|hay que|definir|decidir|elegir|validar|reemplazar|"
        # EN
        r"need|missing|confirm|provide)", re.I)
    # Capturar até o fechamento do PRÓPRIO elemento, não até o primeiro "</".
    # Nota que começa com rótulo em negrito ("<b>Falta o número.</b> Preciso de…")
    # era truncada no </b> e o pedido, que vem depois, nunca era visto — todo bloco
    # bem escrito virava aviso.
    notas = re.findall(
        r'<(p|div|span)\b[^>]*class=["\'][^"\']*\bnota\b[^"\']*["\'][^>]*>(.*?)</\1>',
        limpo, re.S | re.I)
    for _tag, corpo_nota in notas:
        texto = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", corpo_nota)).strip()
        if texto and not pedido.search(texto):
            aviso(f'nota de produção sem pedido: "{texto[:70]}" — nota serve pra pedir do cliente, não pra comentar')

    # ── rastreabilidade ────────────────────────────────────────────────────
    blocos = len(re.findall(r"<section", limpo, re.I))
    marcados = len(re.findall(r"motor:\s*S\d", html, re.I))
    if blocos and marcados == 0:
        erro("nenhum bloco tem comentário de rastreabilidade (motor: SX) — sem isso ninguém audita a página depois")
    elif marcados < blocos:
        aviso(f"{blocos - marcados} de {blocos} blocos sem comentário de rastreabilidade")

    # ── notas de produção ──────────────────────────────────────────────────
    notas = len(re.findall(r'class=["\'][^"\']*\bnota\b', limpo, re.I))
    if notas == 0:
        aviso("nenhuma nota de produção — é raro uma página não depender de nada do cliente; confira")

    return achados


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arquivo", help="wireframe .html a conferir")
    args = ap.parse_args()

    p = pathlib.Path(args.arquivo).expanduser()
    if not p.exists():
        print(f"não encontrei: {p}", file=sys.stderr)
        sys.exit(2)

    achados = checar(p.read_text(encoding="utf-8", errors="replace"))

    print(f"\n── {p.name} ──")
    if not achados:
        print(f"{OK} nada a corrigir\n")
        return

    for nivel in (ERRO, AVISO):
        for n, msg in achados:
            if n == nivel:
                print(f"{n} {msg}")

    erros = sum(1 for n, _ in achados if n == ERRO)
    print(f"\n{erros} erro(s), {len(achados) - erros} aviso(s)\n")
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
