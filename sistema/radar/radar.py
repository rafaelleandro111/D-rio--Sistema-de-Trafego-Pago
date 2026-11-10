"""
Radar — os NICHOS em alta agora.

Em alta = com mais pesquisa / mais ofertas rodando AGORA (esta semana).

  Google  — compara a pesquisa dos últimos 7 dias de cada nicho no Brasil
            (cada nicho é medido pela soma das buscas principais dele).
  Meta    — conta quantos anúncios e anunciantes de infoproduto estão rodando
            agora em cada nicho na Biblioteca de Anúncios (loja fica de fora).

Entrega só o top 5. Roda em prioridade baixa (não trava o PC), navegador invisível.

Uso:
    python sistema/radar/radar.py --google
    python sistema/radar/radar.py --meta

Saída: saidas/radar/radar-google-<data>.md / radar-meta-<data>.md (+ .json)
"""

import argparse
import asyncio
import ctypes
import json
import re
import sys
import time
from datetime import date
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
PASTA = RAIZ / "saidas" / "radar"
sys.path.insert(0, str(RAIZ / "sistema" / "espiao"))
import espiao  # noqa: E402

TOP = 5
REGUA = "receita de bolo"
SIMULTANEOS = 3

# Nicho -> buscas que medem o nicho. A 1ª também é usada no Meta.
NICHOS = {
    "Emagrecimento": ["emagrecer", "dieta", "perder barriga"],
    "Saúde": ["ansiedade", "diabetes", "dor nas costas"],
    "Beleza": ["maquiagem", "skincare", "cabelo"],
    "Vícios": ["parar de fumar", "parar de beber", "vício"],
    "Relacionamento": ["reconquistar", "conquistar", "casamento"],
    "Dinheiro": ["renda extra", "ganhar dinheiro", "investir"],
    "Educação": ["concurso", "enem", "inglês"],
    "Culinária": ["receitas", "air fryer", "confeitaria"],
    "Fitness": ["treino", "pilates", "academia"],
    "Espiritualidade": ["oração", "tarot", "signos"],
    "Maternidade": ["gravidez", "amamentação", "bebê"],
    "Pets": ["cachorro", "gato", "adestramento"],
    "Artesanato": ["crochê", "costura", "bordado"],
    "Desenvolvimento pessoal": ["autoestima", "produtividade", "inteligência emocional"],
}

# O projeto é infoproduto: loja e marketplace não contam
LOJAS = ("shein", "shopee", "magalu", "magazineluiza", "amazon", "mercadolivre", "mercadolibre",
         "aliexpress", "temu", "americanas", "casasbahia", "pontofrio", "carrefour", "netshoes",
         "centauro", "renner", "riachuelo", "cea.com", "havan", "kabum", "submarino", "extra.com",
         "leroymerlin", "tiktok.com/shop", "olx")
INFO = re.compile(r"curso|aula|desafio|e-?book|apostila|m[eé]todo|treinamento|mentoria|pdf|"
                  r"passo a passo|acesso|protocolo|guia|aprenda|forma[cç][aã]o|certificado|"
                  r"m[oó]dulo|programa de|plano alimentar|card[aá]pio|receitas", re.I)


def prioridade_baixa():
    """Windows: BELOW_NORMAL. O navegador aberto depois herda a prioridade."""
    try:
        h = ctypes.windll.kernel32.GetCurrentProcess()
        ctypes.windll.kernel32.SetPriorityClass(h, 0x00004000)
    except Exception:
        pass


def salvar(nome, md, dados):
    PASTA.mkdir(parents=True, exist_ok=True)
    arq = PASTA / f"{nome}-{date.today().isoformat()}.md"
    arq.write_text(md, encoding="utf-8")
    arq.with_suffix(".json").write_text(json.dumps(dados, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Salvo em: {arq}")


# ---------------------------------------------------------------- Google

def google():
    from pytrends.request import TrendReq
    trends = TrendReq(hl="pt-BR", tz=180, timeout=(10, 25))
    termos = [t for ts in NICHOS.values() for t in ts]
    vol = {}
    for i in range(0, len(termos), 4):
        lote = termos[i:i + 4]
        print(f"Google: {', '.join(lote)}")
        for t in range(3):
            try:
                trends.build_payload(lote + [REGUA], geo="BR", timeframe="now 7-d")
                df = trends.interest_over_time()
                base = df[REGUA].mean() or 1
                for k in lote:
                    vol[k] = 100 * df[k].mean() / base
                break
            except Exception as e:
                print(f"  Google recusou ({e.__class__.__name__}), tentando de novo...")
                time.sleep(20 * (t + 1))
        time.sleep(2)

    res = []
    for nicho, ts in NICHOS.items():
        medidos = {t: vol[t] for t in ts if t in vol}
        if not medidos:
            continue
        principal = max(medidos, key=medidos.get)
        res.append({"nicho": nicho, "pesquisa": round(sum(medidos.values())), "mais_buscado": principal})
    res.sort(key=lambda x: -x["pesquisa"])
    return res


def relatorio_google(res):
    L = [f"# Nichos em alta no Google — {date.today().strftime('%d/%m/%Y')}", "",
         "Os nichos com **mais pesquisa no Brasil nesta semana** (receita de bolo = 100).", "",
         "| # | Nicho | Pesquisa | O que mais buscam |", "|---|---|---|---|"]
    for i, x in enumerate(res[:TOP], 1):
        L.append(f"| {i} | **{x['nicho']}** | {x['pesquisa']} | {x['mais_buscado']} |")
    return "\n".join(L)


# ---------------------------------------------------------------- Meta

def infoproduto(a):
    destinos = " ".join([a.get("destino") or ""] + list(a.get("todos_destinos") or [])).lower()
    if any(l in destinos or l in (a["anunciante"] or "").lower() for l in LOJAS):
        return False
    return bool(a["plataforma_afiliado"]) or bool(INFO.search(a.get("texto") or ""))


async def ler(nicho, termo, maximo, vagas):
    async with vagas:
        print(f"Meta: {nicho} ({termo})")
        try:
            return await espiao.coletar(termo, "BR", maximo)
        except Exception as e:
            print(f"  Biblioteca falhou ({termo}): {e.__class__.__name__}")
            return None


def meta(maximo):
    async def tudo():
        vagas = asyncio.Semaphore(SIMULTANEOS)
        pares = [(n, ts[0]) for n, ts in NICHOS.items()]
        res = dict(zip([n for n, _ in pares],
                       await asyncio.gather(*(ler(n, t, maximo, vagas) for n, t in pares))))
        uma = asyncio.Semaphore(1)  # o Facebook às vezes recarrega a página: refaz um por um
        for n in [n for n, x in res.items() if x is None]:
            res[n] = await ler(n, NICHOS[n][0], maximo, uma)
        return res
    cards = asyncio.run(tudo())

    hoje, res = date.today(), []
    for nicho, lista in cards.items():
        if lista is None:
            continue
        ads, vistos = [], set()
        for c in lista:
            a = espiao.interpretar(c, hoje)
            if a and a["id"] not in vistos:
                vistos.add(a["id"])
                if infoproduto(a):
                    ads.append(a)
        res.append({"nicho": nicho, "ofertas": len(ads),
                    "anunciantes": len({a["anunciante"] for a in ads}),
                    "copias": sum(a["variacoes"] for a in ads)})
    res.sort(key=lambda x: (-x["ofertas"], -x["copias"]))
    return res


def relatorio_meta(res):
    L = [f"# Nichos em alta no Meta Ads — {date.today().strftime('%d/%m/%Y')}", "",
         "Os nichos com **mais ofertas de infoproduto rodando agora** (loja fica de fora).", "",
         "| # | Nicho | Anúncios de infoproduto | Anunciantes |", "|---|---|---|---|"]
    for i, x in enumerate(res[:TOP], 1):
        L.append(f"| {i} | **{x['nicho']}** | {x['ofertas']} | {x['anunciantes']} |")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="Radar: nichos em alta agora (Google ou Meta)")
    lado = ap.add_mutually_exclusive_group(required=True)
    lado.add_argument("--google", action="store_true", help="nichos com mais pesquisa agora")
    lado.add_argument("--meta", action="store_true", help="nichos com mais ofertas rodando agora")
    ap.add_argument("--max", type=int, default=60, help="anúncios lidos por nicho no Meta (padrão 60)")
    a = ap.parse_args()
    prioridade_baixa()

    if a.google:
        res = google()
        salvar("radar-google", relatorio_google(res), res)
    else:
        res = meta(a.max)
        salvar("radar-meta", relatorio_meta(res), res)


if __name__ == "__main__":
    main()
