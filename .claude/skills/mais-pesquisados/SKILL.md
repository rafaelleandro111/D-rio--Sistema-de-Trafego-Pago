---
name: mais-pesquisados
description: Mostra o que o Brasil mais pesquisa no Google agora, entre os temas que viram infoproduto (oração, Excel, ansiedade, air fryer, maquiagem, crochê, emagrecer...), na mesma régua, com volume e se está subindo ou caindo nas últimas 4 semanas. Use quando o Rafael perguntar "o que está sendo mais pesquisado", "o que o Brasil mais pesquisa", "o que o povo está procurando agora", "mais pesquisados", ou /mais-pesquisados.
---

# /mais-pesquisados — O que o Brasil mais pesquisa agora

Rodar direto, sem perguntar nada:

```bash
PYTHONIOENCODING=utf-8 python sistema/radar/mais_pesquisados.py
```

~1 minuto, prioridade baixa (não trava o PC). Precisa do `pytrends`.
Os temas ficam em `TEMAS`, no topo de `sistema/radar/mais_pesquisados.py` — se o Rafael citar um
tema novo, adicionar. Evitar palavra de duplo sentido (ex: "desenho" pega desenho animado).

## Entregar

Ler `saidas/radar/mais-pesquisados-<data>.md` e mostrar a tabela, do mais pesquisado pro menos:

| Tema | Volume (bolo = 100) | Últimas 4 semanas |
|---|---|---|

- Volume: comparado com "receita de bolo" = 100. 265 = 2,6 vezes mais pesquisado
- Pode agrupar os de volume parecido numa linha só (ex: "Violão, tarot, costura — 80 a 90") pra ficar curto
- Destacar em negrito os 2 ou 3 que valem mais pra infoproduto
- Depois da tabela, no máximo 2 linhas: o que chama atenção. Avisar se algum número parecer inflado
  por duplo sentido

É pra infoproduto. Não filtrar por risco de bloqueio.
