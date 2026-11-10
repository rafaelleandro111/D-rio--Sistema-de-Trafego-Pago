"""
Mais pesquisados — o que o Brasil mais pesquisa no Google agora, entre os
temas que viram infoproduto.

Compara todos os temas de TEMAS na mesma régua ("receita de bolo" = 100,
últimos 3 meses, Brasil) e mostra se cada um subiu ou caiu nas últimas
4 semanas.

Uso:
    python sistema/radar/mais_pesquisados.py

Saída: saidas/radar/mais-pesquisados-<data>.md (+ .json)
"""

import ctypes
import json
import time
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
PASTA = RAIZ / "saidas" / "radar"
REGUA = "receita de bolo"

# Temas que viram infoproduto. Evitar palavra de duplo sentido (ex: "desenho" = desenho animado)
TEMAS = ["oração", "excel", "ansiedade", "air fryer", "maquiagem", "crochê", "emagrecer",
         "violão", "cabelo cacheado", "tarot", "costura", "pilates", "marmita", "sobrancelha",
         "concurso público", "confeitaria", "alfabetização", "atividades para imprimir",
         "unhas de gel", "bolo de pote", "curso de inglês", "renda extra", "treino em casa",
         "parar de fumar", "adestramento"]


def prioridade_baixa():
    try:
        ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x00004000)
    except Exception:
        pass


def tendencia(v):
    if v >= 10:
        return "subindo"
    if v >= 3:
        return "subindo um pouco"
    if v <= -10:
        return "caindo"
    return "estável"


def main():
    from pytrends.request import TrendReq
    prioridade_baixa()
    trends = TrendReq(hl="pt-BR", tz=180, timeout=(10, 25))
    res = {}
    for i in range(0, len(TEMAS), 4):
        lote = TEMAS[i:i + 4]
        print(f"Google: {', '.join(lote)}")
        for t in range(3):
            try:
                trends.build_payload(lote + [REGUA], geo="BR", timeframe="today 3-m")
                df = trends.interest_over_time()
                base = df[REGUA].mean() or 1
                for k in lote:
                    s = df[k]
                    recente, antes = s[-28:].mean(), s[:-28].mean()
                    res[k] = {"volume": round(100 * s.mean() / base),
                              "variacao": round(100 * (recente - antes) / antes) if antes else 0}
                break
            except Exception as e:
                print(f"  Google recusou ({e.__class__.__name__}), tentando de novo...")
                time.sleep(20 * (t + 1))
        time.sleep(2)

    ordem = sorted(res, key=lambda k: -res[k]["volume"])
    L = [f"# O que o Brasil mais pesquisa — {date.today().strftime('%d/%m/%Y')}", "",
         "Temas de infoproduto no Google, mesma régua (receita de bolo = 100), últimos 3 meses.", "",
         "| Tema | Volume (bolo = 100) | Últimas 4 semanas |", "|---|---|---|"]
    for k in ordem:
        v = res[k]
        L.append(f"| {k} | {v['volume']} | {tendencia(v['variacao'])} ({v['variacao']:+d}%) |")
    falhou = [k for k in TEMAS if k not in res]
    if falhou:
        L += ["", f"Sem dado (Google bloqueou): {', '.join(falhou)}"]

    PASTA.mkdir(parents=True, exist_ok=True)
    arq = PASTA / f"mais-pesquisados-{date.today().isoformat()}.md"
    arq.write_text("\n".join(L), encoding="utf-8")
    arq.with_suffix(".json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Salvo em: {arq}")


if __name__ == "__main__":
    main()
