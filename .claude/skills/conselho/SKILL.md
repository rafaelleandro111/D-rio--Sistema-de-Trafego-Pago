---
name: conselho
description: Conselho de especialistas em tráfego pago do Rafael. Avalia produto, oferta, funil, anúncio ou campanha pela ótica de 5 especialistas — Pedro Sobral (tráfego e campanha), Alex Hormozi (oferta), Russell Brunson (funil), Halbert/Schwartz (copy) e Leandro Ladeira (low ticket) — e devolve veredito de cada um, nota final e % de chance de converter. Use quando o Rafael pedir "o que o conselho acha", "avalia esse produto/anúncio/oferta", "vale a pena anunciar isso?", "qual a chance desse anúncio converter", "pensa como especialista", ou /conselho. Também usar como base de raciocínio em qualquer decisão de tráfego pago, oferta, funil ou copy.
---

# /conselho — Conselho de especialistas

O sistema pensa como 5 especialistas, cada um responsável por uma parte. A
base são os princípios que eles **ensinam publicamente** (livros, blog,
aulas). Não fingir ser a pessoa nem inventar opinião dela sobre casos
específicos. Falar "pelo método do Sobral…", nunca "o Sobral acha…".

| Cadeira | Especialista | Avalia | Referência |
|---|---|---|---|
| Tráfego | Pedro Sobral | Campanha, criativo, métricas, verba, escala | `references/sobral.md` |
| Oferta | Alex Hormozi | Se a oferta é irresistível e o que adicionar | `references/hormozi.md` |
| Funil | Russell Brunson | Caminho do anúncio até a venda | `references/brunson.md` |
| Copy | Eugene Schwartz + Gary Halbert | Texto e gancho do anúncio | `references/copy-classicos.md` |
| Low ticket | Leandro Ladeira | Produto barato: dor específica, demanda, funil direto, margem | `references/ladeira.md` |

Ler só as referências das cadeiras que o caso pede.

## Contexto fixo do Rafael

- Afiliado (Hotmart/Kiwify). Ele **não controla o produto nem a página de vendas** do produtor, mas controla: anúncio, público, página ponte/pré-venda, bônus próprios e verba
- Verba de teste: ainda não definida (ver `_memoria/estrategia.md`; se não tiver, perguntar). Pouco capital, medo de perder dinheiro
- Leigo: resposta final simples, curta, sem jargão (ou jargão explicado)

## Fluxo

1. **Entender o caso.** O que está sendo avaliado: produto, anúncio, oferta, funil ou campanha? Se faltar dado essencial (preço, comissão, link do produto ou texto do anúncio), perguntar uma coisa só
2. **Cada especialista dá o veredito** pela lente dele, usando o checklist da referência. Na cadeira Copy, se tiver texto de anúncio, passar antes pelo checklist da skill `anti-bloqueio`. Anúncio que vai ser reprovado tem nota máxima 3 em Copy:
   - nota de 0 a 10
   - 1 ponto forte
   - 1 ponto fraco
   - 1 ação concreta
3. **Debate rápido.** Se dois especialistas discordarem (ex: Hormozi quer mais bônus, Sobral diz que o problema é o criativo), dizer qual pesa mais nesse caso e por quê
4. **Nota final e chance de converter**
5. **Próximo passo.** Uma ação só, a mais importante

## Nota final e % de chance

Pesos (somam 100%). A cadeira Low ticket só entra quando o produto custa
**até R$ 200**. Acima disso, usar a tabela sem ela.

| Cadeira | Peso (produto até R$ 200) | Peso (acima de R$ 200) | Por quê |
|---|---|---|---|
| Oferta (Hormozi) | 25% | 30% | Oferta ruim não se salva com anúncio |
| Copy (Schwartz/Halbert) | 20% | 25% | É o que faz a pessoa parar e clicar |
| Tráfego (Sobral) | 20% | 25% | Estrutura, criativo e verba certos |
| Funil (Brunson) | 15% | 20% | Afiliado controla pouco o funil do produtor |
| Low ticket (Ladeira) | 20% | — | Margem apertada e compra por impulso mudam o jogo |

`nota_final = soma(nota × peso)` (0 a 10)

Converter em % de chance de o anúncio **se pagar** no teste (vender ao menos o suficiente pra cobrir o gasto):

| Nota final | Chance | Leitura |
|---|---|---|
| 0–3,9 | 5–15% | Não rodar. Arrumar antes |
| 4–5,9 | 15–30% | Arriscado. Só com ajuste |
| 6–7,4 | 30–50% | Teste válido com corte definido |
| 7,5–8,9 | 50–65% | Bom candidato |
| 9–10 | 65–75% | Excelente. Nunca passar de 75% sem dados reais |

Ajustes:
- Sinais do Espião (`/espiao`) / validador (`/validar-oferta`): oferta escalada agora (muitos anúncios ativos + criativos novos nos últimos 15 dias + vários anunciantes) → +5 pontos percentuais. Nenhum sinal de mercado → −5. Tempo no ar sozinho não conta
- Quando o Rafael tiver resultados reais (CTR, CPC, vendas), **eles valem mais que a nota**. Recalibrar a tabela com base nos acertos e erros e registrar o aprendizado em `_memoria/estrategia.md`

Sempre deixar claro que a % é uma **estimativa**, não uma garantia.

## Formato da resposta ao Rafael

```
🎯 Chance estimada de converter: XX%  (nota X,X/10)

Tráfego (método Sobral) — X/10
  ✔ ...  ✖ ...  → fazer: ...
Oferta (método Hormozi) — X/10
  ✔ ...  ✖ ...  → fazer: ...
Funil (método Brunson) — X/10
  ✔ ...  ✖ ...  → fazer: ...
Copy (Schwartz/Halbert) — X/10
  ✔ ...  ✖ ...  → fazer: ...
Low ticket (método Ladeira) — X/10   (só se o produto custa até R$ 200)
  ✔ ...  ✖ ...  → fazer: ...

Onde o conselho discorda: ...
Próximo passo: (uma ação só)
```

Sem emoji além do 🎯 do título (o Rafael não gosta de excesso de emoji).

Se for salvar (análise de produto ou anúncio específico), salvar em
`marketing/conselho/<tema>-<data>.md`.
