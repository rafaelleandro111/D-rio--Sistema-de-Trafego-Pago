# Nome de criativo

**Criativo** = cada anúncio (vídeo ou imagem). O nome dele é o que liga o vídeo ao resultado:
é por ele que você descobre, no Gerenciador de Anúncios, qual peça vendeu e qual não vendeu.
Vale pra todo produto e todo tipo de venda.

## A fórmula

```
[OFERTA]_Pack[N]_[FORMATO]_[NUM]          criativo sem troca de preço
[OFERTA]_Pack[N]_[FORMATO]_[NUM]_V[n]     mesmo criativo, versão de preço n
```

Exemplo, pra uma oferta de código `RPC`:

```
RPC_Pack1_VID_001
RPC_Pack1_VID_002_V1      ← R$7
RPC_Pack1_VID_002_V2      ← R$9
RPC_Pack1_VID_002_V3      ← R$10
RPC_Pack1_IMG_003
RPC_Pack2_VID_016         ← o Pack1 terminou no 015; o Pack2 continua dali
```

| Campo | Regra | Exemplo |
|---|---|---|
| `OFERTA` | código da oferta, **3 letras maiúsculas** (ver abaixo como escolher) | `RPC` |
| `Pack[N]` | a palavra `Pack` + o número do pack, sem zero à esquerda e sem espaço | `Pack1`, `Pack12` |
| `FORMATO` | `VID` (vídeo) ou `IMG` (imagem estática) | `VID` |
| `NUM` | **3 casas**, com zero à esquerda | `001`, `016`, `120` |
| `V[n]` | **só quando há troca de preço**: a versão de preço do mesmo criativo, a partir de `V1` | `_V1`, `_V2` |

Separador é sempre `_`. Nada de espaço, acento, emoji ou texto livre no nome.

## Como escolher o código da oferta (3 letras)

Faz uma vez, no primeiro pack, e nunca mais muda.

1. **Pegue as iniciais das palavras principais do nome do produto**, ignorando "de", "da", "do",
   "e", "o", "a". Ex.: "Receitas Práticas em Casa" → `RPC`. "Método Planilha Zero" → `MPZ`.
2. **Nome de uma ou duas palavras:** use as 3 primeiras consoantes fortes. Ex.: "Destrava" → `DST`.
3. **Um código por oferta, não por produto.** Se o mesmo conteúdo for vendido em duas ofertas
   diferentes (ex.: um a R$ 7 com página própria e outro dentro de um combo), cada oferta ganha
   o seu código — a métrica de uma não pode misturar com a da outra.
4. **Sem acento, só letras maiúsculas**, e diferente de qualquer código que você já usou.

Anote o código em `infoproduto/criativos/nomenclatura.md` (ver o fim deste arquivo).

## As regras que seguram a leitura de resultado

1. **O nome é idêntico em todo lugar:** o nome do arquivo do vídeo, o nome do anúncio no
   Gerenciador e o título da peça no pack. Quem sobe o anúncio copia o nome do arquivo, sem
   reescrever.
2. **`NUM` é sequencial da oferta e nunca recomeça entre packs.** Se o Pack1 terminou no `015`, o
   Pack2 começa no `016`. Um mesmo número existe uma vez só na história da oferta — é o que impede
   dois criativos diferentes de dividirem nome (e resultado). A contagem é uma só pra `VID` e `IMG`.
3. **Troca de preço = mesmo número, sufixo de versão.** O roteiro gravado em 7/9/10 reais é UM
   criativo em três versões: `RPC_Pack3_VID_030_V1`, `_030_V2`, `_030_V3`. O pack registra qual
   versão é qual preço (ex.: `V1` = R$7 · `V2` = R$9 · `V3` = R$10) — o nome não carrega o preço.
   Criativo sem troca de preço não leva sufixo. Qualquer outra diferença (gancho, corte, cena)
   é criativo novo, com número novo.
4. **O pack é o lote de produção**, não a campanha. Um criativo nasce num pack e carrega esse
   número pra sempre, mesmo que rode em campanhas de outro pack depois.
5. **Nome não muda depois que o anúncio rodou.** Se você usa rastreamento por UTM (a etiqueta no
   link que diz de qual anúncio veio a venda), o `utm_content` costuma puxar o nome do anúncio
   (`{{ad.name}}`): renomear um anúncio no ar parte o resultado dele em dois na data da troca.
   Se precisar renomear histórico, é por plano (abaixo), nunca no improviso.

## Onde cada coisa fica registrada

- **O código da oferta** e o **último `NUM` usado** ficam em `infoproduto/criativos/nomenclatura.md`.
  Antes de nomear um pack novo, leia o último número lá — e atualize ao fechar o pack. Se o
  arquivo não existe, crie com este molde:

  ```markdown
  # Nomenclatura dos criativos

  | Oferta | Código | Produto / página | Último NUM | Atualizado em |
  |---|---|---|---|---|
  | <nome da oferta> | <ABC> | <link da página> | 000 | <AAAA-MM-DD> |

  ## Histórico de packs
  | Pack | Oferta | NUMs | Data |
  |---|---|---|---|
  ```

  Se você já subiu anúncios antes com outro padrão de nome, pergunte ao usuário quantos
  criativos já existem e comece a contagem depois deles — nunca do `001` por conta própria
  quando houver histórico.
- **O que o nome não carrega** (formato do catálogo, ângulo, pessoa, gancho, preço) fica no
  bastidor do pack, numa tabela por criativo. É dali que sai a leitura de resultado por ângulo,
  formato e pessoa.

## Renomear criativos que já existem

Só com plano aprovado, nesta ordem:

1. **Levantar** todos os arquivos (no computador ou no Drive) e os anúncios na conta, com o nome atual.
2. **Montar o de-para** (nome antigo → nome novo) numa planilha ou `.md`, com a data. O nome
   antigo costuma carregar qual gancho e qual copy geraram o vídeo — o de-para é o único lugar
   onde essa informação sobrevive.
3. **Renomear os arquivos primeiro.**
4. **Na Meta, renomear só anúncio que ainda não rodou ou que já foi desligado.** Anúncio ativo
   mantém o nome antigo até sair do ar; o de-para cobre a leitura. Se decidir renomear ativo
   mesmo assim, registre a data: ao comparar períodos, agrupar pelo ID do anúncio, não pelo nome.
