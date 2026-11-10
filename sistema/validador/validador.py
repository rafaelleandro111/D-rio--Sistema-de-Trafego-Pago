"""
Validador de ofertas — dá uma nota de 0 a 100% pra uma oferta de afiliado.

Três comandos:

    # 1. Busca por palavra: espiona a Biblioteca de Anúncios, agrupa os anúncios
    #    por oferta (site de destino), entra nas páginas de vendas das melhores
    #    e monta um ranking.
    python sistema/validador/validador.py busca "emagrecimento" --max 100 --top 5

    # 2. Link: analisa uma oferta específica (página de vendas) e procura
    #    anúncios dela na Biblioteca usando o nome do produto.
    python sistema/validador/validador.py link "https://site.com/oferta" --busca "nome do produto"

    # 3. Nota: calcula a nota final a partir do arquivo de critérios
    #    (os dados da Hotmart/Kiwify entram aqui).
    python sistema/validador/validador.py nota saidas/ofertas/<pasta>/criterios-<oferta>.json

Saída: saidas/ofertas/<palavra>-<data>/
    ranking.md / ranking.json     -> ofertas encontradas, da mais forte pra mais fraca
    criterios-<oferta>.json       -> ficha de cada oferta (completar e rodar "nota")
    nota-<oferta>.md              -> resultado final com a nota
"""

import argparse
import asyncio
import json
import re
import sys
import time
import urllib.parse
from collections import defaultdict
from datetime import date
from pathlib import Path

from playwright.async_api import async_playwright

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "sistema" / "espiao"))
import espiao  # noqa: E402

# Destinos que não são página de vendas (rede social, app, encurtador)
NAO_OFERTA = ("instagram.com", "facebook.com", "fb.me", "wa.me", "whatsapp.com",
              "play.google.com", "apps.apple.com", "itunes.apple.com", "adjust.com",
              "linktr.ee", "youtube.com", "youtu.be", "tiktok.com", "t.me")

CHECKOUTS = {
    "pay.hotmart.com": "Hotmart", "go.hotmart.com": "Hotmart", "hotmart.com": "Hotmart",
    "hotm.art": "Hotmart", "pay.kiwify.com.br": "Kiwify", "kiwify.com.br": "Kiwify",
    "kiwify.app": "Kiwify", "eduzz.com": "Eduzz", "monetizze.com.br": "Monetizze",
    "braip.com": "Braip", "perfectpay.com.br": "PerfectPay", "ticto.app": "Ticto",
    "greenn.com.br": "Greenn", "lastlink.com": "Lastlink", "cakto.com.br": "Cakto",
    "onprofit.com.br": "OnProfit", "payt.com.br": "Payt", "yampi.com.br": "Yampi",
    "pepper.com.br": "Pepper", "doppus.com": "Doppus", "hubla.com": "Hubla",
}

NICHO_RISCO = {
    "alto": ["emagrec", "peso", "gordura", "dieta", "diabet", "pressão", "remédio", "cura",
             "calv", "cabelo", "queda", "menopausa", "ansiedade", "depress", "renda extra",
             "ganhar dinheiro", "dinheiro", "investi", "cripto", "aposta", "trader",
             "sexual", "ereç", "estética", "rugas", "celulite", "saúde", "dor"],
    "medio": ["relacionamento", "conquista", "ex ", "beleza", "pele", "fitness", "treino",
              "academia", "concurso"],
}


# ---------------------------------------------------------------- utilidades

def dominio(url):
    d = urllib.parse.urlparse(url).netloc.lower()
    return d[4:] if d.startswith("www.") else d


def eh_oferta(url):
    d = dominio(url)
    return bool(d) and not any(d == x or d.endswith("." + x) for x in NAO_OFERTA)


def risco_nicho(texto):
    t = texto.lower()
    for nivel in ("alto", "medio"):
        if any(p in t for p in NICHO_RISCO[nivel]):
            return nivel
    return "baixo"


def precos(texto):
    """Preços cheios encontrados na página. "12x de R$ 69,70" vira R$ 836,40."""
    vals = []
    for m in re.finditer(r"(?:(\d{1,2})\s*x\s*(?:de\s*)?)?R\$\s*([\d.]{1,7}(?:,\d{2})?)", texto, re.I):
        try:
            v = float(m.group(2).replace(".", "").replace(",", "."))
        except ValueError:
            continue
        if m.group(1):
            v = round(v * int(m.group(1)), 2)
        if 5 <= v <= 20000:
            vals.append(v)
    return sorted(set(vals))


# ---------------------------------------------------------------- prova de mercado

def agrupar_ofertas(anuncios):
    grupos = defaultdict(list)
    for a in anuncios:
        destino = next((d for d in a.get("todos_destinos") or [a.get("destino", "")] if eh_oferta(d)), "")
        if destino:
            grupos[dominio(destino)].append((a, destino))

    ofertas = []
    for dom, itens in grupos.items():
        ads = [a for a, _ in itens]
        dias = [a["dias_no_ar"] for a in ads if a["dias_no_ar"] is not None]
        ofertas.append({
            "oferta": dom,
            "url": itens[0][1],
            "ativos": sum(a["variacoes"] for a in ads),
            "novos_15d": sum(1 for a in ads if a["dias_no_ar"] is not None and a["dias_no_ar"] <= 15),
            "passaram_teste": sum(1 for a in ads if (a["dias_no_ar"] or 0) >= 7),
            "anunciantes": len({a["anunciante"] for a in ads if a["anunciante"]}),
            "criativos": len(ads),
            "max_dias": max(dias) if dias else 0,
            "exemplo_texto": (ads[0]["texto"] or "")[:300],
            "links_biblioteca": [a["link_biblioteca"] for a in ads[:5]],
        })
    ofertas.sort(key=lambda o: (pontos_mercado(o), o["ativos"]), reverse=True)
    return ofertas


def pontos_mercado(o):
    """0-30. Sinais de escala: gente colocando dinheiro na oferta AGORA.
    Tempo no ar não dá ponto — só serve de filtro (7+ dias = passou do teste)."""
    at = o["ativos"]
    p = 12 if at >= 30 else 9 if at >= 15 else 6 if at >= 5 else 3 if at >= 2 else 1 if at == 1 else 0
    nv = o["novos_15d"]
    p += 10 if nv >= 10 else 7 if nv >= 5 else 4 if nv >= 2 else 2 if nv == 1 else 0
    n = o["anunciantes"]
    p += 8 if n >= 5 else 6 if n >= 3 else 3 if n == 2 else 1 if n == 1 else 0
    if at and not o.get("passaram_teste"):
        p = round(p * 0.7)  # tudo com menos de 7 dias: ainda em teste, sem prova
    return p


# ---------------------------------------------------------------- página de vendas

async def inspecionar_paginas(urls):
    resultado = {}
    async with async_playwright() as p:
        nav = await p.chromium.launch(headless=True)
        for url in urls:
            pag = await nav.new_page(locale="pt-BR")
            info = {"url": url, "carregou": False}
            try:
                t0 = time.time()
                await pag.goto(url, wait_until="domcontentloaded", timeout=30000)
                info["segundos"] = round(time.time() - t0, 1)
                await pag.wait_for_timeout(3000)
                info["carregou"] = True
                info["titulo"] = (await pag.title())[:150]
                links = await pag.evaluate("() => [...document.querySelectorAll('a[href],form[action]')].map(e => e.href || e.action)")
                html = await pag.content()
                texto = await pag.inner_text("body")
                plataforma, checkout = "", ""
                for alvo in links + [html]:
                    for chave, nome in CHECKOUTS.items():
                        if chave in alvo.lower():
                            plataforma = nome
                            if alvo is not html:
                                checkout = alvo
                            break
                    if plataforma:
                        break
                if not plataforma:
                    for alvo in links:
                        d = dominio(alvo)
                        if d.startswith(("pay.", "checkout.", "seguro.")) or "/checkout" in alvo.lower():
                            plataforma, checkout = f"outra ({d})", alvo
                            break
                info.update({
                    "plataforma": plataforma,
                    "checkout": checkout,
                    "precos_na_pagina": precos(texto)[:10],
                    "tem_garantia": bool(re.search(r"garantia", texto, re.I)),
                    "tem_depoimentos": bool(re.search(r"depoimento|resultado de|alunas?|clientes? satisfeit", texto, re.I)),
                    "resumo_pagina": re.sub(r"\s+", " ", texto)[:1500],
                })
            except Exception as e:  # página fora do ar, bloqueio, timeout
                info["erro"] = str(e)[:200]
            finally:
                await pag.close()
            resultado[url] = info
        await nav.close()
    return resultado


def pontos_pagina(info, qualidade=None):
    """0-15. qualidade (0-5) é a avaliação do Claude lendo a página."""
    if not info.get("carregou"):
        return 0
    p = 3 if info.get("plataforma") else 0
    p += 3 if info.get("precos_na_pagina") else 0
    s = info.get("segundos", 99)
    p += 4 if s < 3 else 2 if s < 6 else 0
    if qualidade is not None:
        p += max(0, min(5, qualidade))
    return p


# ---------------------------------------------------------------- nota final

PESOS = {"mercado": 30, "plataforma": 25, "dinheiro": 20, "pagina": 15, "risco": 10}


def calcular_nota(c):
    """c = dicionário de critérios. Campos ausentes (None) ficam de fora e a nota é ajustada."""
    partes, faltando = {}, []
    incompletos = []  # parte calculada só com parte dos dados -> nota provisória

    partes["mercado"] = c.get("pontos_mercado")

    # Hotmart: temperatura, blueprint, satisfação. Kiwify não mostra -> fica de fora.
    temp, blue, sat = c.get("temperatura"), c.get("blueprint"), c.get("satisfacao")
    if temp is None and blue is None and sat is None:
        partes["plataforma"] = None
    else:
        pts, maxp = 0, 0
        if temp is not None:
            pts += 10 if temp >= 100 else 8 if temp >= 70 else 5 if temp >= 40 else 2
            maxp += 10
        if blue is not None:
            pts += 8 if blue >= 80 else 5 if blue >= 60 else 2
            maxp += 8
        if sat is not None:
            pts += 7 if sat >= 4.5 else 5 if sat >= 4.0 else 2 if sat >= 3.5 else 0
            maxp += 7
        partes["plataforma"] = round(pts / maxp * 25, 1)
        # Kiwify nunca mostra esses números: só cobrar quando a plataforma for Hotmart
        if "hotmart" in str(c.get("plataforma") or "").lower():
            incompletos += [n for n, v in (("temperatura", temp), ("blueprint", blue), ("satisfacao", sat)) if v is None]

    com, preco = c.get("comissao"), c.get("preco")
    if com is None and preco is None:
        partes["dinheiro"] = None
    else:
        pts, maxp = 0, 0
        if com is not None:
            pts += 10 if com >= 100 else 8 if com >= 50 else 5 if com >= 25 else 3 if com >= 10 else 1
            maxp += 10
        if preco is not None:  # tráfego frio converte mais fácil em produto barato
            pts += 10 if preco <= 97 else 7 if preco <= 297 else 4 if preco <= 497 else 2
            maxp += 10
        partes["dinheiro"] = round(pts / maxp * 20, 1)
        incompletos += [n for n, v in (("comissao", com), ("preco", preco)) if v is None]

    partes["pagina"] = c.get("pontos_pagina")
    risco = c.get("risco_nicho")
    partes["risco"] = {"baixo": 10, "medio": 6, "alto": 3}.get(risco)

    total, peso_usado = 0, 0
    for k, v in partes.items():
        if v is None:
            faltando.append(k)
        else:
            total += v
            peso_usado += PESOS[k]
    nota = round(total / peso_usado * 100) if peso_usado else 0

    if nota >= 70:
        veredito = "BOA — vale testar"
    elif nota >= 50:
        veredito = "MÉDIA — só testar com pouco dinheiro"
    else:
        veredito = "FRACA — não rodar"

    limite = None
    if com:
        limite = {
            "pausar_conjunto_sem_venda": round(com, 2),
            "teste_total_maximo": round(com * 3, 2),
        }
    faltando += incompletos
    return {"nota": nota, "veredito": veredito, "partes": partes, "faltando": faltando,
            "provisoria": bool(faltando), "limite_gasto": limite}


def reais(v):
    return "R$ " + f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


NOMES = {"mercado": "Prova de mercado", "plataforma": "Números da Hotmart/Kiwify",
         "dinheiro": "Dinheiro (comissão e preço)", "pagina": "Página de vendas",
         "risco": "Risco de bloqueio", "temperatura": "temperatura (Hotmart)",
         "blueprint": "Blueprint (Hotmart)", "satisfacao": "satisfação (Hotmart)",
         "comissao": "comissão", "preco": "preço"}


def nota_md(c, r):
    linhas = [f"# {c.get('oferta', 'Oferta')} — nota {r['nota']}%", "",
              f"**Veredito:** {r['veredito']}" + (" *(nota provisória — faltam dados)*" if r["provisoria"] else ""), "",
              "| Critério | Pontos | Máximo |", "|---|---|---|"]
    for k, v in r["partes"].items():
        linhas.append(f"| {NOMES[k]} | {'falta dado' if v is None else v} | {PESOS[k]} |")
    if r["limite_gasto"]:
        l = r["limite_gasto"]
        linhas += ["", "**Limite de gasto:**",
                   f"- Pausar um conjunto que gastar {reais(l['pausar_conjunto_sem_venda'])} sem nenhuma venda",
                   f"- Gastar no máximo {reais(l['teste_total_maximo'])} no teste inteiro antes de decidir se continua"]
    if r["faltando"]:
        linhas += ["", "**Faltando pra nota completa:** " + ", ".join(NOMES[k] for k in r["faltando"])]
    if c.get("observacoes"):
        linhas += ["", "**Observações:**", c["observacoes"]]
    return "\n".join(linhas) + "\n"


# ---------------------------------------------------------------- comandos

def ficha(o, info, palavra):
    texto_nicho = " ".join([palavra, o.get("exemplo_texto", ""), info.get("titulo", ""), info.get("resumo_pagina", "")[:500]])
    return {
        "oferta": o["oferta"],
        "url": o["url"],
        "plataforma": info.get("plataforma") or None,
        "checkout": info.get("checkout") or None,
        "precos_na_pagina": info.get("precos_na_pagina", []),
        "prova_de_mercado": {k: o[k] for k in ("ativos", "novos_15d", "passaram_teste", "anunciantes", "criativos", "max_dias")},
        "pontos_mercado": pontos_mercado(o),
        "pontos_pagina": pontos_pagina(info),
        "qualidade_pagina_0a5": None,
        "risco_nicho": risco_nicho(texto_nicho),
        "temperatura": None, "blueprint": None, "satisfacao": None,
        "comissao": None,
        "preco": (info.get("precos_na_pagina") or [None])[0],
        "observacoes": "",
        "_pagina": {k: info.get(k) for k in ("titulo", "segundos", "tem_garantia", "tem_depoimentos", "erro", "resumo_pagina")},
        "_links_biblioteca": o.get("links_biblioteca", []),
    }


def salvar_fichas(fichas, pasta):
    pasta.mkdir(parents=True, exist_ok=True)
    for f in fichas:
        arq = pasta / f"criterios-{espiao.slug(f['oferta'])}.json"
        arq.write_text(json.dumps(f, ensure_ascii=False, indent=1), encoding="utf-8")


def cmd_busca(args):
    anuncios, pasta_espiao = espiao.espionar(args.palavra, "BR", args.max)
    if not anuncios:
        print("Nenhum anúncio encontrado. A página do Facebook pode ter mudado ou bloqueou a consulta.")
        sys.exit(1)
    ofertas = agrupar_ofertas(anuncios)
    if not ofertas:
        print("Os anúncios encontrados não levam pra página de vendas (só Instagram/WhatsApp/app).")
        sys.exit(1)

    top = ofertas[:args.top]
    print(f"{len(ofertas)} ofertas diferentes. Abrindo as {len(top)} páginas mais fortes...")
    paginas = asyncio.run(inspecionar_paginas([o["url"] for o in top]))

    pasta = RAIZ / "saidas" / "ofertas" / f"{espiao.slug(args.palavra)}-{date.today().isoformat()}"
    fichas = []
    for o in top:
        f = ficha(o, paginas[o["url"]], args.palavra)
        r = calcular_nota(f)
        f["_nota_previa"] = r["nota"]
        fichas.append(f)
    salvar_fichas(fichas, pasta)

    (pasta / "ranking.json").write_text(json.dumps(ofertas, ensure_ascii=False, indent=1), encoding="utf-8")
    md = [f"# Ofertas encontradas: \"{args.palavra}\"", "",
          f"{len(anuncios)} anúncios analisados · {len(ofertas)} ofertas · espião em `{pasta_espiao.relative_to(RAIZ)}`", "",
          "| # | Oferta | Anúncios ativos | Novos (15 dias) | Anunciantes | Plataforma | Preço | Nota prévia |", "|---|---|---|---|---|---|---|---|"]
    for i, f in enumerate(fichas, 1):
        pm = f["prova_de_mercado"]
        md.append(f"| {i} | {f['oferta']} | {pm['ativos']} | {pm['novos_15d']} | {pm['anunciantes']} | "
                  f"{f['plataforma'] or '?'} | {reais(f['preco']) if f['preco'] else '?'} | {f['_nota_previa']}% |")
    (pasta / "ranking.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print("\n".join(md[4:]))
    print(f"\nSalvo em: {pasta}")


def cmd_link(args):
    url = args.url
    busca = args.busca or dominio(url).split(".")[0]
    anuncios, _ = espiao.espionar(busca, "BR", args.max)
    alvo = dominio(url)
    meus = [a for a in anuncios if any(dominio(d) == alvo for d in a.get("todos_destinos") or [])]
    o = agrupar_ofertas(meus)[0] if meus else {
        "oferta": alvo, "url": url, "ativos": 0, "novos_15d": 0, "passaram_teste": 0,
        "anunciantes": 0, "criativos": 0, "max_dias": 0,
        "exemplo_texto": "", "links_biblioteca": []}
    o["url"] = url
    info = asyncio.run(inspecionar_paginas([url]))[url]

    pasta = RAIZ / "saidas" / "ofertas" / f"{espiao.slug(alvo)}-{date.today().isoformat()}"
    f = ficha(o, info, busca)
    f["_busca_usada"] = busca
    f["_anuncios_da_busca"] = len(anuncios)
    f["_nota_previa"] = calcular_nota(f)["nota"]
    salvar_fichas([f], pasta)
    print(json.dumps({k: v for k, v in f.items() if k != "_pagina"}, ensure_ascii=False, indent=1))
    print(f"\nFicha salva em: {pasta}")


def cmd_nota(args):
    arq = Path(args.arquivo)
    c = json.loads(arq.read_text(encoding="utf-8"))
    pagina_ok = not (c.get("_pagina") or {}).get("erro")
    if c.get("qualidade_pagina_0a5") is not None and pagina_ok:
        c["pontos_pagina"] = min(15, pontos_pagina({"carregou": True, **{
            "plataforma": c.get("plataforma"), "precos_na_pagina": c.get("precos_na_pagina"),
            "segundos": (c.get("_pagina") or {}).get("segundos", 99)}}, c["qualidade_pagina_0a5"]))
    r = calcular_nota(c)
    saida = arq.with_name(arq.name.replace("criterios-", "nota-").replace(".json", ".md"))
    saida.write_text(nota_md(c, r), encoding="utf-8")
    print(json.dumps(r, ensure_ascii=False, indent=1))
    print(f"\nResultado salvo em: {saida}")


def main():
    ap = argparse.ArgumentParser(description="Validador de ofertas de afiliado")
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("busca")
    b.add_argument("palavra")
    b.add_argument("--max", type=int, default=100)
    b.add_argument("--top", type=int, default=5)
    l = sub.add_parser("link")
    l.add_argument("url")
    l.add_argument("--busca", help="nome do produto pra procurar na Biblioteca de Anúncios")
    l.add_argument("--max", type=int, default=100)
    n = sub.add_parser("nota")
    n.add_argument("arquivo")
    args = ap.parse_args()
    {"busca": cmd_busca, "link": cmd_link, "nota": cmd_nota}[args.cmd](args)


if __name__ == "__main__":
    main()
