---
name: radar
description: Radar do Rafael — mostra os NICHOS em alta agora (com mais pesquisa ou mais ofertas rodando nesta semana) — saúde, emagrecimento, beleza, vícios, relacionamento, dinheiro etc. Antes de rodar pergunta só "Google ou Meta Ads?". Entrega só o top 5. Use quando o Rafael disser "roda o radar", "radar", "o que está em alta", "quais nichos estão em alta", "o que o povo está pesquisando", "qual nicho está bombando", ou /radar.
---

# /radar — Os nichos em alta agora

## O que o Rafael quer (ele já explicou várias vezes — seguir à risca)

- **Nicho = categoria grande**: saúde, emagrecimento, beleza, vícios, relacionamento, dinheiro,
  educação... Produto não é nicho ("cartilha do ENEM" é produto do nicho educação)
- **Em alta = com mais pesquisa / mais ofertas AGORA** (esta semana). Não é "o que mais cresceu"
- Mostrar **só o top 5**. Nada de listão, nada de explicação longa
- É pra infoproduto. Loja/marketplace não conta. Não filtrar por risco de bloqueio

## 1. Perguntar (sempre, e só isso)

**"Google ou Meta Ads?"** — nunca perguntar quais nichos.

## 2. Rodar

```bash
PYTHONIOENCODING=utf-8 python sistema/radar/radar.py --google   # nichos com mais pesquisa esta semana
PYTHONIOENCODING=utf-8 python sistema/radar/radar.py --meta     # nichos com mais ofertas rodando agora
```

Prioridade baixa e navegador invisível: não trava o PC. Precisa do `pytrends`.
Os nichos e as buscas que medem cada um ficam em `NICHOS`, no topo de `sistema/radar/radar.py`.
Se o Rafael citar um nicho que não está lá, adicionar.

## 3. Entregar (curto)

Ler `saidas/radar/radar-google-<data>.md` ou `radar-meta-<data>.md` e responder só com:

| # | Nicho | Pesquisa (ou ofertas rodando) | O que mais buscam |
|---|---|---|---|

E 1 linha: o nicho nº 1. Mais nada, a não ser que ele peça.
Se o outro lado (Google/Meta) tiver rodado nos últimos dias, cruzar em 1 linha: nicho no top dos dois = o melhor.
