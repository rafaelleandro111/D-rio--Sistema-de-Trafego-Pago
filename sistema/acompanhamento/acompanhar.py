"""
Acompanhamento diário de OFERTAS escolhidas pelo Rafael — mostra se cada uma
está crescendo ou morrendo.

O Rafael escolhe a oferta (manda o link, ou escolhe do ranking do validador).
Todo dia (Agendador de Tarefas do Windows, 11h) o robô pesquisa na Biblioteca
de Anúncios a palavra de busca de cada oferta e guarda uma "foto" só daquela
oferta (todos os anunciantes que mandam pro mesmo site). A partir de 3 dias,
calcula a tendência.

Uso:
    python sistema/acompanhamento/acompanhar.py adicionar "https://site-da-oferta.com" --busca "pilates na parede"
    python sistema/acompanhamento/acompanhar.py remover "site-da-oferta.com"
    python sistema/acompanhamento/acompanhar.py lista
    python sistema/acompanhamento/acompanhar.py rodar          # coleta do dia (o agendador chama este)
    python sistema/acompanhamento/acompanhar.py relatorio

--busca = o que o robô digita na Biblioteca pra achar os anúncios da oferta:
nome do produto ou a promessa principal (o que aparece no texto dos anúncios).

Arquivos:
    sistema/acompanhamento/lista.json      -> ofertas acompanhadas (máx. 5)
    sistema/acompanhamento/historico.json  -> uma foto por dia, por oferta
    sistema/acompanhamento/log.txt         -> registro de cada rodada automática
    saidas/acompanhamento/relatorio-<data>.md
"""

import argparse
import asyncio
import json
import sys
import traceback
from datetime import date, datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
sys.path.insert(0, str(RAIZ / "sistema" / "espiao"))
sys.path.insert(0, str(RAIZ / "sistema" / "validador"))
import espiao  # noqa: E402
import validador  # noqa: E402

LISTA = AQUI / "lista.json"
HIST = AQUI / "historico.json"
PRECOS = AQUI / "precos.json"
LOG = AQUI / "log.txt"
MAX_OFERTAS = 5  # mais que isso por dia arrisca bloqueio do Facebook

ICONES = {"escalando": "🚀 ESCALANDO", "subindo": "📈 SUBINDO", "estavel": "➡️ ESTÁVEL",
          "caindo": "📉 CAINDO", "morrendo": "💀 MORRENDO", "coletando": "⏳ COLETANDO"}
ORDEM = ["escalando", "subindo", "estavel", "coletando", "caindo", "morrendo"]


def ler(arq, padrao):
    try:
        return json.loads(arq.read_text(encoding="utf-8"))
    except (FileNotFoundError, ValueError):
        return padrao


def salvar(arq, dados):
    arq.write_text(json.dumps(dados, ensure_ascii=False, indent=1), encoding="utf-8")


def log(msg):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M} {msg}\n")


def dominio_de(texto):
    return validador.dominio(texto if "://" in texto else "https://" + texto)


# ---------------------------------------------------------------- lista

def cmd_adicionar(a):
    lista = ler(LISTA, [])
    dom = dominio_de(a.oferta)
    if any(i["oferta"] == dom for i in lista):
        print("Essa oferta já está sendo acompanhada.")
        return
    if len(lista) >= MAX_OFERTAS:
        print(f"Já tem {MAX_OFERTAS} ofertas (limite pra não ser bloqueado). Remova uma antes.")
        return
    url = a.oferta if "://" in a.oferta else "https://" + a.oferta
    lista.append({"oferta": dom, "url": url, "busca": a.busca, "pais": a.pais,
                  "desde": date.today().isoformat()})
    salvar(LISTA, lista)
    print(f'Acompanhando: {dom} (busca "{a.busca}", {a.pais}). Primeira coleta na próxima rodada.')


def cmd_remover(a):
    lista = ler(LISTA, [])
    dom = dominio_de(a.oferta)
    nova = [i for i in lista if i["oferta"] != dom]
    salvar(LISTA, nova)
    print("Removida." if len(nova) < len(lista) else "Não estava na lista.")


def cmd_lista(_):
    lista = ler(LISTA, [])
    if not lista:
        print("Nenhuma oferta sendo acompanhada.")
    for i in lista:
        print(f'- {i["oferta"]}  (busca "{i["busca"]}", {i["pais"]}) desde {i["desde"]}')


# ---------------------------------------------------------------- coleta diária

def coletar_palavra(palavra, pais, maximo=200):
    hoje = date.today()
    cards = asyncio.run(espiao.coletar(palavra, pais, maximo))
    anuncios, vistos = [], set()
    for c in cards:
        ad = espiao.interpretar(c, hoje)
        if ad and ad["id"] not in vistos:
            vistos.add(ad["id"])
            anuncios.append(ad)
    foto = {}
    for o in validador.agrupar_ofertas(anuncios):
        ids = [ad["id"] for ad in anuncios
               if any(validador.dominio(d) == o["oferta"] for d in ad.get("todos_destinos") or [])]
        foto[o["oferta"]] = {"url": o["url"], "ativos": o["ativos"], "criativos": o["criativos"],
                             "anunciantes": o["anunciantes"], "novos_15d": o["novos_15d"], "ids": ids}
    return foto


def cmd_rodar(_):
    lista = ler(LISTA, [])
    if not lista:
        log("lista vazia, nada a fazer")
        print("Nenhuma oferta sendo acompanhada.")
        return
    hist = ler(HIST, {})
    hoje = date.today().isoformat()
    pendentes = [i for i in lista if hoje not in hist.get(i["oferta"], {})]
    if not pendentes:
        print("Tudo já coletado hoje.")
        return
    # uma pesquisa por palavra de busca (várias ofertas podem usar a mesma)
    buscas = {}
    for i in pendentes:
        buscas.setdefault((i["busca"], i["pais"]), []).append(i)
    for (busca, pais), itens in buscas.items():
        try:
            foto = coletar_palavra(busca, pais)
            for i in itens:
                achou = foto.get(i["oferta"])  # None = nenhum anúncio dela hoje
                hist.setdefault(i["oferta"], {})[hoje] = achou
                n = achou["ativos"] if achou else 0
                log(f'OK {i["oferta"]} (busca "{busca}"): {n} anúncios')
                print(f'{i["oferta"]}: {n} anúncios ativos hoje.')
            salvar(HIST, hist)
        except Exception as e:  # um erro numa busca não para as outras
            log(f'ERRO busca "{busca}": {e}\n{traceback.format_exc()}')
            print(f'Busca "{busca}": erro ({e}). Ver log.txt.')


# ---------------------------------------------------------------- tendência

def tendencia(serie):
    """serie = [(data, foto_da_oferta ou None)] em ordem. Devolve (classe, detalhes)."""
    dias = list(serie)
    vistos = [f for _, f in dias if f]
    if len(dias) < 3:
        ult = vistos[-1] if vistos else {}
        return "coletando", {"dias": len(dias), "ativos_hoje": ult.get("ativos", 0),
                             "anunciantes": ult.get("anunciantes", 0)}
    ativos = [f["ativos"] if f else 0 for _, f in dias]
    ultimos = ativos[-3:]
    pico = max(ativos)
    hoje = ativos[-1]

    # criativos novos nos últimos 3 dias (ids que não existiam antes)
    ids_antes = set()
    for _, f in dias[:-3]:
        if f:
            ids_antes.update(f["ids"])
    novos = set()
    for _, f in dias[-3:]:
        if f:
            novos.update(i for i in f["ids"] if i not in ids_antes)
    if len(dias) == 3:  # sem passado pra comparar: conta os que surgiram depois do 1º dia
        primeiro = set(dias[0][1]["ids"]) if dias[0][1] else set()
        novos = {i for _, f in dias[1:] if f for i in f["ids"] if i not in primeiro}

    base = max(ultimos[0], 1)
    variacao = (ultimos[-1] - ultimos[0]) / base
    det = {"dias": len(dias), "ativos_hoje": hoje, "pico": pico,
           "variacao_3d": round(variacao * 100), "criativos_novos_3d": len(novos),
           "anunciantes": vistos[-1]["anunciantes"] if vistos else 0}

    if hoje == 0 or (pico >= 5 and hoje <= pico * 0.2):
        return "morrendo", det
    if variacao >= 0.5 and len(novos) >= 2:
        return "escalando", det
    if variacao >= 0.15 or len(novos) >= 3:
        return "subindo", det
    if variacao <= -0.15:
        return "caindo", det
    return "estavel", det


# ---------------------------------------------------------------- relatório

def cmd_relatorio(_):
    lista = ler(LISTA, [])
    hist = ler(HIST, {})
    precos = ler(PRECOS, {})
    if not lista:
        print("Nenhuma oferta sendo acompanhada.")
        return
    linhas = []
    for item in lista:
        dias = hist.get(item["oferta"], {})
        classe, det = tendencia([(d, dias[d]) for d in sorted(dias)])
        linhas.append({**item, "classe": classe, **det})

    falta = [l for l in linhas if l["oferta"] not in precos]
    if falta:
        print(f"Abrindo {len(falta)} páginas pra pegar o preço...")
        info = asyncio.run(validador.inspecionar_paginas([l["url"] for l in falta]))
        for l in falta:
            i = info[l["url"]]
            precos[l["oferta"]] = {"preco": (i.get("precos_na_pagina") or [None])[0],
                                   "plataforma": i.get("plataforma") or ""}
        salvar(PRECOS, precos)
    for l in linhas:
        p = precos.get(l["oferta"], {})
        l["preco"], l["plataforma"] = p.get("preco"), p.get("plataforma", "")

    linhas.sort(key=lambda l: (ORDEM.index(l["classe"]), -(l.get("ativos_hoje") or 0)))
    md = ["# Ofertas acompanhadas", "", f"Atualizado em {date.today():%d/%m/%Y}", "",
          "| Tendência | Oferta | Anúncios hoje | Variação 3 dias | Criativos novos (3d) | Anunciantes | Preço | Plataforma | Dias | Busca |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for l in linhas:
        var = f"{l['variacao_3d']:+d}%" if "variacao_3d" in l else "—"
        md.append(f"| {ICONES[l['classe']]} | {l['oferta']} | {l.get('ativos_hoje', '—')} | {var} | "
                  f"{l.get('criativos_novos_3d', '—')} | {l.get('anunciantes', '—')} | "
                  f"{validador.reais(l['preco']) if l['preco'] else '?'} | {l['plataforma'] or '?'} | "
                  f"{l['dias']} | {l['busca']} ({l['pais']}) |")
    md += ["", "Tendência só aparece com 3+ dias de coleta. Ideal: 5 a 7 dias pra ter certeza."]

    pasta = RAIZ / "saidas" / "acompanhamento"
    pasta.mkdir(parents=True, exist_ok=True)
    arq = pasta / f"relatorio-{date.today().isoformat()}.md"
    arq.write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))
    print(f"\nSalvo em: {arq}")


def main():
    ap = argparse.ArgumentParser(description="Acompanhamento diário das ofertas escolhidas")
    sub = ap.add_subparsers(dest="cmd", required=True)
    ad = sub.add_parser("adicionar")
    ad.add_argument("oferta", help="link ou site da oferta")
    ad.add_argument("--busca", required=True, help="nome do produto ou promessa (o que aparece nos anúncios)")
    ad.add_argument("--pais", default="BR")
    rm = sub.add_parser("remover")
    rm.add_argument("oferta")
    sub.add_parser("lista")
    sub.add_parser("rodar")
    sub.add_parser("relatorio")
    a = ap.parse_args()
    {"adicionar": cmd_adicionar, "remover": cmd_remover, "lista": cmd_lista,
     "rodar": cmd_rodar, "relatorio": cmd_relatorio}[a.cmd](a)


if __name__ == "__main__":
    main()
