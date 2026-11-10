---
name: validar-oferta
description: Validador de ofertas do Rafael. Dá uma nota de 0 a 100% pra uma oferta de afiliado (Hotmart, Kiwify etc.) e diz se vale rodar, quanto pode gastar e quando pausar. Funciona por busca de palavra ("acha oferta boa de emagrecimento") ou por link ("valida essa oferta: <link>"). Usa o robô espião na Biblioteca de Anúncios + entra na página de vendas. Use quando o Rafael disser "valida", "validar oferta", "essa oferta é boa?", "acha oferta de X", "busca oferta", "qual produto eu rodo", "nota da oferta", ou /validar-oferta.
---

# /validar-oferta — Validador de ofertas

O Rafael é leigo e tem pouco dinheiro. Explicar simples, curto, sem jargão.
Sempre separar o que é **dado real** (veio do robô/página) do que é **estimativa**.

## Como a nota funciona

| Critério | Peso | De onde vem |
|---|---|---|
| Prova de mercado | 30 | Robô espião — sinais de escala: anúncios ativos (com cópias), anúncios novos nos últimos 15 dias, nº de anunciantes. Tempo no ar NÃO dá ponto, só filtra (7+ dias = passou do teste) |
| Números da Hotmart/Kiwify | 25 | Rafael manda print/dados: temperatura, Blueprint, satisfação |
| Dinheiro | 20 | Comissão (Rafael) + preço (página) |
| Página de vendas | 15 | Robô (plataforma, preço, velocidade) + avaliação do Claude (0-5) |
| Risco de bloqueio | 10 | Nicho (alto/médio/baixo) |

70%+ = boa, vale testar · 50-69% = só testar com pouco · abaixo de 50% = não rodar.
Se faltar algum dado, a nota é calculada com o que tem e marcada **provisória**.

## Modo 1 — Busca por palavra

```bash
PYTHONIOENCODING=utf-8 python sistema/validador/validador.py busca "<palavra>" --max 100 --top 5
```

Demora ~3-5 min. Gera `saidas/ofertas/<palavra>-<data>/` com `ranking.md` e uma
ficha `criterios-<oferta>.json` pra cada uma das 5 ofertas mais fortes.

## Modo 2 — Link de uma oferta

```bash
PYTHONIOENCODING=utf-8 python sistema/validador/validador.py link "<url da página de vendas>" --busca "<nome do produto>"
```

`--busca` é o que o robô procura na Biblioteca de Anúncios — usar o nome do
produto ou a promessa principal (ex: "pilates na parede"). Se o link for da
página do produto na Hotmart/Kiwify, primeiro abrir e achar a página de vendas.

## Depois de rodar (os dois modos)

1. **Ler a página de vendas** (`_pagina.resumo_pagina` na ficha, ou abrir o link)
   e dar `qualidade_pagina_0a5`: promessa clara, prova/depoimento, garantia,
   oferta fácil de entender. Ajustar `risco_nicho` se o automático errou.
2. **Conferir o preço**: `preco` pega o menor valor da página. Se for claramente
   errado (ex: preço de bônus), corrigir pelo `precos_na_pagina`.
3. **Pedir ao Rafael os dados do marketplace** (só ele vê, precisa de login):
   > "Pra nota ficar completa, procura esse produto na vitrine da Hotmart/Kiwify
   > e me manda um print mostrando temperatura, Blueprint, satisfação e comissão."
   Se ele não achar o produto pra se afiliar → avisar: o produto pode ser do
   próprio anunciante (sem programa de afiliado). Aí a oferta serve como
   **referência de mercado**, não pra ele rodar.
4. Preencher na ficha: `temperatura`, `blueprint` (%), `satisfacao` (0-5),
   `comissao` (R$ que ele recebe por venda). Kiwify não mostra temperatura etc.
   → deixar `null`.
5. Calcular:
   ```bash
   PYTHONIOENCODING=utf-8 python sistema/validador/validador.py nota "saidas/ofertas/<pasta>/criterios-<oferta>.json"
   ```

## Entregar ao Rafael

Curto, nessa ordem:
0. **Está escalando agora ou não?** Sempre dizer logo no começo, com os números: anúncios ativos,
   quantos foram lançados nos últimos 15 dias e há quanto tempo o mais antigo está no ar
   (o Rafael pediu — é o sinal que ele mais valoriza)
1. **Nota e veredito** (ex: "72% — boa, vale testar")
2. **Por quê**, em 3 frases simples: o ponto mais forte e o mais fraco
3. **Limite de gasto**: pausar o conjunto que gastar o valor de 1 comissão sem
   venda; teste inteiro no máximo 3 comissões
4. **Cuidado com bloqueio** se o nicho for de risco alto
5. O que falta pra nota ficar completa (se provisória)

No modo busca, mostrar primeiro a tabela do `ranking.md` e perguntar qual
oferta ele quer aprofundar — não pedir print das 5 de uma vez.

## Avisos

- Hotmart/Kiwify não mostram quantas vendas um produto tem. "Prova de mercado"
  é sinal indireto: muita gente colocando dinheiro na oferta agora (muitos
  anúncios ativos, criativos novos subindo, vários anunciantes) = está vendendo.
  Anúncio antigo sozinho não prova nada — pode estar esquecido com verba baixa.
- Usar o robô com moderação (algumas buscas por dia) pra não ser bloqueado.
- Se o robô retornar "Nenhum anúncio encontrado", a página do Facebook pode ter
  mudado → ajustar `JS_CARDS` / `interpretar()` em `sistema/espiao/espiao.py`.
- A escala de temperatura da Hotmart nos critérios (100+ = quente) é uma
  referência inicial — ajustar com o Rafael conforme ele for vendo produtos reais.
