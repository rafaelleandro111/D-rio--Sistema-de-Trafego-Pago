#!/usr/bin/env python3
"""Mede as falas de um pack de criativos contra a régua de REGRAS-ESCRITA.md.

Só usa a biblioteca padrão do Python 3. Funciona no Mac e no Windows.

Uso (sempre a partir da raiz do Info OS):
    Mac:     python3 .claude/skills/_base-criativos/scripts/medir_falas.py infoproduto/criativos/packs/pack-01-<produto>.md
    Windows: python  .claude/skills/_base-criativos/scripts/medir_falas.py infoproduto/criativos/packs/pack-01-<produto>.md

    # uma fala solta (um texto com uma fala por linha):
    python3 .claude/skills/_base-criativos/scripts/medir_falas.py --texto rascunho.txt

O que ele faz: acha cada peça do pack (título "# NOME_DO_CRIATIVO"), pega a coluna FALA da
tabela "| Fala | Tela |" daquela peça e mede:
  - linhas: quantas falas
  - mediana: palavras por linha (régua: 10 a 15)
  - micro%: linhas de até 3 palavras (régua: até ~12%, cada uma justificada)
  - longas: linhas acima de 28 palavras (régua: zero)
Mediana fora de 10-15 ou qualquer linha longa = REPROVADA (sai com código 1).
Micro acima de ~12% = "revisar micro": justifique cada uma ou funda com a linha vizinha.
"""
import argparse
import re
import statistics
import sys

MEDIANA_MIN, MEDIANA_MAX = 10, 15
MICRO_MAX_PCT = 12.0
LONGA = 28


def limpar(celula):
    t = celula.strip()
    t = re.sub(r"<br\s*/?>", " ", t)
    t = t.replace("**", "").replace("`", "")
    t = t.strip().strip('"').strip("“”").strip()
    return t


def medir(linhas_brutas):
    linhas = [l.strip() for l in linhas_brutas
              if l.strip() and not l.strip().startswith(("(", "[", "#", "**"))]
    linhas = [limpar(l) for l in linhas]
    linhas = [l for l in linhas if l]
    n = [len(l.split()) for l in linhas]
    micro = [l for l, k in zip(linhas, n) if k <= 3]
    longas = [l for l, k in zip(linhas, n) if k > LONGA]
    mediana = statistics.median(n) if n else 0
    micro_pct = round(100 * len(micro) / max(len(linhas), 1), 1)
    ok = bool(linhas) and MEDIANA_MIN <= mediana <= MEDIANA_MAX and not longas
    status = "REPROVADA" if not ok else ("revisar micro" if micro_pct > MICRO_MAX_PCT else "ok")
    return {"linhas": len(linhas), "mediana": mediana, "micro_pct": micro_pct,
            "micro": micro, "longas": longas, "ok": ok, "status": status}


def pecas_do_pack(texto):
    """Devolve [(nome, [falas])] para cada peça com tabela Fala | Tela."""
    pecas = []
    atual, falas, na_tabela = None, [], False
    for linha in texto.splitlines():
        if re.match(r"^#\s+\S", linha) and not linha.startswith("##"):
            if atual and falas:
                pecas.append((atual, falas))
            atual, falas, na_tabela = linha.lstrip("#").strip(), [], False
            continue
        s = linha.strip()
        if not s.startswith("|"):
            na_tabela = False
            continue
        cols = [c for c in s.strip("|").split("|")]
        primeira = cols[0].strip().lower() if cols else ""
        if primeira in ("fala", "**fala**"):
            na_tabela = True
            continue
        if not na_tabela or re.match(r"^:?-{2,}:?$", cols[0].strip()):
            continue
        falas.append(cols[0])
    if atual and falas:
        pecas.append((atual, falas))
    return pecas


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("arquivo", nargs="?", help="o pack .md")
    ap.add_argument("--texto", help="arquivo de texto com uma fala por linha")
    a = ap.parse_args()

    if a.texto:
        with open(a.texto, encoding="utf-8") as f:
            pecas = [(a.texto, f.read().splitlines())]
    elif a.arquivo:
        with open(a.arquivo, encoding="utf-8") as f:
            pecas = pecas_do_pack(f.read())
    else:
        ap.print_help()
        return 2

    if not pecas:
        print("Nenhuma tabela '| Fala | Tela |' encontrada. Confira o modelo em MODELO-ENTREGA.md.")
        return 2

    reprovou = False
    print("| peça | linhas | mediana | micro% | longas | régua |")
    print("|---|---|---|---|---|---|")
    for nome, falas in pecas:
        r = medir(falas)
        reprovou |= not r["ok"]
        print(f"| {nome} | {r['linhas']} | {r['mediana']} | {r['micro_pct']} | "
              f"{len(r['longas'])} | {r['status']} |")
    for nome, falas in pecas:
        r = medir(falas)
        if r["micro"] or r["longas"]:
            print(f"\n{nome}")
            for l in r["micro"]:
                print(f"  micro (justificar: placa, congelamento, confirmação ou pergunta curta): {l}")
            for l in r["longas"]:
                print(f"  LONGA (quebrar): {l}")
    return 1 if reprovou else 0


if __name__ == "__main__":
    sys.exit(main())
