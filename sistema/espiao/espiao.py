"""
Espião de anúncios — Biblioteca de Anúncios da Meta (Facebook/Instagram).

Pesquisa uma palavra-chave, coleta os anúncios ativos e ordena pelos mais
escalados: mais cópias do mesmo criativo rodando primeiro. Anúncio com 7+ dias
ainda ativo passou do teste (o que não vende é cortado em poucos dias).

Uso:
    python sistema/espiao/espiao.py "calvície"
    python sistema/espiao/espiao.py "queda de cabelo" --max 150 --pais BR

Saída: marketing/espiao/<palavra>-<data>/
    relatorio.html   -> abre no navegador
    anuncios.csv     -> abre no Excel / Google Planilhas
    anuncios.json    -> dados completos (usado pelo Claude na análise)
    imagens/         -> capa de cada anúncio
"""

import argparse
import asyncio
import csv
import html
import json
import re
import sys
import unicodedata
import urllib.parse
import urllib.request
from datetime import date, timedelta
from pathlib import Path

from playwright.async_api import async_playwright

RAIZ = Path(__file__).resolve().parents[2]

MESES = {"jan": 1, "fev": 2, "mar": 3, "abr": 4, "mai": 5, "jun": 6,
         "jul": 7, "ago": 8, "set": 9, "out": 10, "nov": 11, "dez": 12}

# Domínios que indicam produto de plataforma de afiliado
AFILIADOS = {
    "hotmart": "Hotmart", "hotm.art": "Hotmart",
    "kiwify": "Kiwify",
    "eduzz": "Eduzz",
    "monetizze": "Monetizze",
    "braip": "Braip",
    "perfectpay": "PerfectPay",
    "ticto": "Ticto",
    "greenn": "Greenn",
    "lastlink": "Lastlink",
    "cakto": "Cakto",
}

JS_CARDS = r"""
() => {
  const out = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const idNodes = [];
  while (walker.nextNode()) {
    if (/Identificação da biblioteca:/.test(walker.currentNode.nodeValue))
      idNodes.push(walker.currentNode.parentElement);
  }
  for (const n of idNodes) {
    let el = n, card = null;
    while (el && el !== document.body) {
      const c = (el.innerText.match(/Identificação da biblioteca:/g) || []).length;
      if (c > 1) break;
      card = el; el = el.parentElement;
    }
    if (!card) continue;
    out.push({
      text: card.innerText,
      links: [...card.querySelectorAll('a[href]')].map(a => a.href),
      imgs: [...card.querySelectorAll('img')].map(i => i.src).filter(s => s.includes('fbcdn')),
      posters: [...card.querySelectorAll('video')].map(v => v.poster).filter(Boolean),
    });
  }
  return out;
}
"""


def slug(txt):
    txt = unicodedata.normalize("NFKD", txt).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", txt.lower()).strip("-")


def ler_data(txt):
    m = re.search(r"Veiculação iniciada em (\d{1,2}) de (\w{3})\w* de (\d{4})", txt)
    if not m:
        return None
    return date(int(m.group(3)), MESES.get(m.group(2).lower(), 1), int(m.group(1)))


def destino_real(url):
    if "l.facebook.com/l.php" in url:
        q = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
        return q.get("u", [url])[0]
    return url


def plataforma_afiliado(links):
    for link in links:
        dominio = urllib.parse.urlparse(link).netloc.lower()
        for chave, nome in AFILIADOS.items():
            if chave in dominio:
                return nome
    return ""


def interpretar(card, hoje):
    txt = card["text"]
    m = re.search(r"Identificação da biblioteca:\s*(\d+)", txt)
    if not m:
        return None
    ad_id = m.group(1)
    inicio = ler_data(txt)
    dias = (hoje - inicio).days if inicio else None

    m = re.search(r"(\d+) anúncios usam esse criativo", txt)
    variacoes = int(m.group(1)) if m else 1

    linhas = [l.strip() for l in txt.split("\n") if l.strip() and l.strip() != "​"]
    anunciante, corpo = "", []
    if "Patrocinado" in linhas:
        i = linhas.index("Patrocinado")
        anunciante = linhas[i - 1] if i > 0 else ""
        for l in linhas[i + 1:]:
            if re.match(r"^\d+:\d+ / \d+:\d+$", l):
                break
            corpo.append(l)
    texto = "\n".join(corpo).strip()

    destinos = []
    for l in card["links"]:
        d = destino_real(l)
        if "facebook.com" in urllib.parse.urlparse(d).netloc:
            continue
        if d not in destinos:
            destinos.append(d)

    formato = "vídeo" if re.search(r"\d+:\d+ / \d+:\d+", txt) else "imagem"
    if "Carrossel" in txt or len(card["imgs"]) > 2:
        formato = "carrossel" if formato == "imagem" else formato
    capa = (card["posters"] or card["imgs"] or [""])[0]

    return {
        "id": ad_id,
        "anunciante": anunciante,
        "dias_no_ar": dias,
        "inicio": inicio.isoformat() if inicio else "",
        "variacoes": variacoes,
        "formato": formato,
        "plataforma_afiliado": plataforma_afiliado(destinos),
        "destino": destinos[0] if destinos else "",
        "todos_destinos": destinos,
        "texto": texto,
        "link_biblioteca": f"https://www.facebook.com/ads/library/?id={ad_id}",
        "capa_url": capa,
        "capa_arquivo": "",
    }


async def coletar(palavra, pais, maximo, dias=None):
    url = ("https://www.facebook.com/ads/library/?active_status=active&ad_type=all"
           f"&country={pais}&q={urllib.parse.quote(palavra)}"
           "&search_type=keyword_unordered&media_type=all")
    if dias:
        desde = (date.today() - timedelta(days=dias)).isoformat()
        url += f"&start_date%5Bmin%5D={desde}&start_date%5Bmax%5D="
    async with async_playwright() as p:
        nav = await p.chromium.launch(headless=True)
        pag = await nav.new_page(locale="pt-BR", viewport={"width": 1400, "height": 1000})
        await pag.goto(url, wait_until="domcontentloaded", timeout=60000)
        await pag.wait_for_timeout(7000)

        total = await pag.inner_text("body")
        m = re.search(r"~?([\d.]+) resultados?", total)
        print(f"Resultados na Biblioteca: {m.group(1) if m else '?'}")

        cards, parado = [], 0
        while True:
            cards = await pag.evaluate(JS_CARDS)
            print(f"  coletados: {len(cards)}", end="\r")
            if len(cards) >= maximo:
                break
            antes = len(cards)
            await pag.mouse.wheel(0, 5000)
            await pag.wait_for_timeout(2500)
            if len(await pag.evaluate(JS_CARDS)) == antes:
                parado += 1
                if parado >= 3:
                    break
            else:
                parado = 0
        print()
        await nav.close()
        return cards[:maximo]


def baixar_capas(anuncios, pasta):
    pasta.mkdir(parents=True, exist_ok=True)
    for a in anuncios:
        if not a["capa_url"]:
            continue
        arq = pasta / f"{a['id']}.jpg"
        try:
            urllib.request.urlretrieve(a["capa_url"], arq)
            a["capa_arquivo"] = f"imagens/{arq.name}"
        except Exception:
            pass


def salvar_csv(anuncios, arq):
    campos = ["dias_no_ar", "inicio", "anunciante", "variacoes", "formato",
              "plataforma_afiliado", "destino", "texto", "link_biblioteca"]
    with open(arq, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore", delimiter=";")
        w.writeheader()
        w.writerows(anuncios)


def salvar_html(anuncios, palavra, arq):
    e = html.escape
    cartoes = []
    for i, a in enumerate(anuncios, 1):
        dias = a["dias_no_ar"] if a["dias_no_ar"] is not None else "?"
        afil = (f'<span class="tag afil">{e(a["plataforma_afiliado"])} — dá pra se afiliar?</span>'
                if a["plataforma_afiliado"] else "")
        var = f'<span class="tag">{a["variacoes"]} cópias rodando</span>' if a["variacoes"] > 1 else ""
        img = f'<img src="{e(a["capa_arquivo"])}" loading="lazy" alt="">' if a["capa_arquivo"] else '<div class="semimg">sem imagem</div>'
        dest = (f'<a href="{e(a["destino"])}" target="_blank">{e(urllib.parse.urlparse(a["destino"]).netloc)}</a>'
                if a["destino"] else "sem link")
        cartoes.append(f"""
<article class="card">
  <div class="topo"><span class="pos">#{i}</span><span class="dias">{dias} dias no ar</span></div>
  {img}
  <h3>{e(a["anunciante"]) or "—"}</h3>
  <div class="tags"><span class="tag">{e(a["formato"])}</span>{var}{afil}</div>
  <p class="texto">{e(a["texto"][:600])}{"…" if len(a["texto"]) > 600 else ""}</p>
  <div class="rodape">Destino: {dest} · <a href="{e(a["link_biblioteca"])}" target="_blank">ver na Biblioteca</a></div>
</article>""")

    com_afil = sum(1 for a in anuncios if a["plataforma_afiliado"])
    doc = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Espião — {e(palavra)}</title>
<style>
:root{{--bg:#f6f6f4;--card:#fff;--txt:#1d1d1b;--sub:#6b6b66;--borda:#e4e4df;--dest:#1f6feb;--afil:#0a7a3f;--afilbg:#e3f5ea}}
@media (prefers-color-scheme:dark){{:root{{--bg:#141413;--card:#1e1e1c;--txt:#ececea;--sub:#a3a39d;--borda:#32322f;--dest:#6ea8fe;--afil:#5fd38f;--afilbg:#16301f}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--txt);font:15px/1.5 system-ui,sans-serif;padding:24px 16px}}
header{{max-width:1200px;margin:0 auto 20px}}h1{{margin:0 0 4px;font-size:24px}}header p{{margin:0;color:var(--sub)}}
.grid{{max-width:1200px;margin:0 auto;display:grid;gap:16px;grid-template-columns:repeat(auto-fill,minmax(280px,1fr))}}
.card{{background:var(--card);border:1px solid var(--borda);border-radius:12px;padding:14px;display:flex;flex-direction:column;gap:8px}}
.topo{{display:flex;justify-content:space-between;align-items:center}}.pos{{color:var(--sub);font-weight:600}}
.dias{{background:var(--txt);color:var(--bg);border-radius:999px;padding:2px 10px;font-weight:700;font-size:13px}}
.card img,.semimg{{width:100%;aspect-ratio:1;object-fit:cover;border-radius:8px;background:var(--borda)}}
.semimg{{display:grid;place-items:center;color:var(--sub)}}
h3{{margin:0;font-size:16px}}.tags{{display:flex;flex-wrap:wrap;gap:6px}}
.tag{{font-size:12px;border:1px solid var(--borda);border-radius:999px;padding:1px 8px;color:var(--sub)}}
.tag.afil{{background:var(--afilbg);color:var(--afil);border-color:transparent;font-weight:600}}
.texto{{margin:0;white-space:pre-line;font-size:14px;max-height:220px;overflow:auto}}
.rodape{{font-size:13px;color:var(--sub);margin-top:auto}}a{{color:var(--dest)}}
</style></head><body>
<header><h1>Espião: “{e(palavra)}”</h1>
<p>{len(anuncios)} anúncios ativos no Brasil, do mais escalado pro menos escalado · {com_afil} levam pra plataforma de afiliado · coletado em {date.today().strftime("%d/%m/%Y")}</p></header>
<main class="grid">{"".join(cartoes)}</main></body></html>"""
    arq.write_text(doc, encoding="utf-8")


def ordem_escala(a):
    """Mais cópias primeiro; no empate, quem já passou de 7 dias, e desses o mais novo."""
    dias = a["dias_no_ar"] or 0
    return (-a["variacoes"], 0 if dias >= 7 else 1, dias)


def espionar(palavra, pais="BR", maximo=100, dias=None):
    """Coleta, salva os arquivos e devolve (anuncios, pasta). Usado também pelo validador."""
    hoje = date.today()
    pasta = RAIZ / "marketing" / "espiao" / f"{slug(palavra)}{f'-novos{dias}d' if dias else ''}-{hoje.isoformat()}"
    print(f'Espionando "{palavra}"...')

    cards = asyncio.run(coletar(palavra, pais, maximo, dias))
    anuncios, vistos = [], set()
    for c in cards:
        a = interpretar(c, hoje)
        if a and a["id"] not in vistos:
            vistos.add(a["id"])
            anuncios.append(a)
    if dias:  # só os que começaram a rodar nos últimos N dias
        anuncios = [a for a in anuncios if a["dias_no_ar"] <= dias]
    anuncios.sort(key=ordem_escala)

    if not anuncios:
        return [], pasta

    pasta.mkdir(parents=True, exist_ok=True)
    baixar_capas(anuncios, pasta / "imagens")
    salvar_csv(anuncios, pasta / "anuncios.csv")
    (pasta / "anuncios.json").write_text(json.dumps(anuncios, ensure_ascii=False, indent=1), encoding="utf-8")
    salvar_html(anuncios, palavra, pasta / "relatorio.html")
    return anuncios, pasta


def main():
    ap = argparse.ArgumentParser(description="Espião de anúncios da Biblioteca da Meta")
    ap.add_argument("palavra", help='palavra-chave, ex: "calvície"')
    ap.add_argument("--pais", default="BR")
    ap.add_argument("--max", type=int, default=100, help="máximo de anúncios (padrão 100)")
    ap.add_argument("--dias", type=int, help="só anúncios lançados nos últimos N dias")
    args = ap.parse_args()

    anuncios, pasta = espionar(args.palavra, args.pais, args.max, args.dias)
    if not anuncios:
        print("Nenhum anúncio encontrado. A página pode ter mudado ou o Facebook bloqueou a consulta.")
        sys.exit(1)

    print(f"{len(anuncios)} anúncios salvos em: {pasta}")
    print("Top 5 mais escalados:")
    for a in anuncios[:5]:
        afil = f" [{a['plataforma_afiliado']}]" if a["plataforma_afiliado"] else ""
        print(f"  {a['variacoes']:>3} cópias, {a['dias_no_ar']} dias — {a['anunciante']}{afil}")


if __name__ == "__main__":
    main()
