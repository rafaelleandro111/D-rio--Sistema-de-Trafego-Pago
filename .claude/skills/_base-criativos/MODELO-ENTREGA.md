# Modelo de entrega — o pack

**Pack** = o lote de criativos que você grava de uma vez (12 roteiros). **O entregável é o `.md`**
em `infoproduto/criativos/packs/pack-NN-<produto>.md`: ele tem o bastidor (etapas 1 a 3 e o portão)
e, embaixo da marca `PACK`, as instruções e os roteiros prontos pra gravar e editar.

**Se você organiza no Google Drive** (ou manda pra um editor), copie só a parte de baixo da marca
`PACK` — as tabelas colam direto num Google Doc. Um jeito que funciona bem é separar em dois
documentos:

1. **`PACK <N> - <OFERTA>`** — pro editor: **mapa do pack no topo** (tabela criativo · gancho escrito
   por extenso · pessoa · ângulo · formato), depois INSTRUÇÕES e as peças completas.
2. **`PACK <N> - ROTEIRO`** — só pra quem grava, sem nada de edição. Por criativo: **PESSOA** (nome +
   quem é) · **OBSERVAÇÕES** (como falar com essa pessoa + quais linhas têm preço pra gravar em N
   valores + o que precisa ter em mãos) · **AÇÕES PRA GRAVAÇÃO** (o que quem grava faz em cena, por
   linha) · **ROTEIRO** (as falas numeradas, preço destacado).

Se o usuário pedir esses dois documentos, gere-os como arquivos `.md` ao lado do pack
(`pack-NN-<produto>-editor.md` e `pack-NN-<produto>-gravacao.md`). Subir pro Drive é com ele.

## Estrutura

```markdown
---
<!-- ======= PACK — daqui pra baixo é o que vai pra gravação e edição ======= -->

# INSTRUÇÕES

**GRAVAÇÃO:** <regra que vale pro pack inteiro — ex.: "Sempre que falarmos o valor, vamos fazer
3 gravações, nos valores de 7 reais – 9 reais – 10 reais. Não precisa gravar o vídeo inteiro,
apenas a frase do valor!">

**EDIÇÃO:** <regra de edição do pack inteiro — ex.: "Sempre que falar o valor, coloca o preço
grande na tela.">

**VISUAL DA MARCA:** <copiado da seção "Anúncios em vídeo" do `marca/DESIGN.md` — ex.: "Texto na
tela em Anton caixa alta, branco, com tarja mostarda (#d4a647) na palavra-chave. Legenda em DM Sans,
branca com sombra. Tela final: fundo #1d4d2e, convite em creme, seta mostarda. Nada de texto nos 14%
de cima nem nos 35% de baixo." Sem DESIGN.md: "Identidade visual ainda não definida.">

<direção de imagem que vale pra todas as peças — ex.: "Mostra o resultado de perto sempre que
der: a tela pronta, o antes e depois, a mão fazendo. Take que faz a pessoa querer ter aquilo.">

---

# <OFERTA>_Pack<N>_VID_<NUM>

**FORMATO**
> <nome do formato, como no catálogo — ex.: Fala e Faz · Tela Dividida · Caixinha>

**OBSERVAÇÕES**
> <o que o editor ou quem grava precisa saber desta peça e que não cabe na tabela — ex.:
> "Colocar uma faixa no topo do vídeo com '7 Reais essa semana' – '9 Reais essa semana' –
> '10 Reais essa semana'">

**ELEMENTOS NECESSÁRIOS**
> - **Preparar/demonstrar:** <o que precisa estar pronto ou em andamento na gravação — o resultado
>   que aparece, a tela aberta, o exercício, o material montado>
> - **Objetos e cenário:** <tudo que não está no seu dia a dia — objeto específico, figurino,
>   locação fora de casa>
> - **Material de apoio:** <print, foto, gravação de tela, trecho das aulas, arte>

| Fala | Tela |
|---|---|
| <1 ideia por linha, exatamente o que é dito> | <o que aparece quando esta fala começa> |
| <…> | |
| <…> | <insert que entra aqui> |
| <CTA> | <tela final> |
```

## Regras do modelo

- **Título da peça = nome do criativo**, no padrão de `NOMENCLATURA.md`:
  `[OFERTA]_Pack[N]_[FORMATO]_[NUM]`. É o mesmo nome do arquivo do vídeo e do anúncio no
  Gerenciador. O `NUM` continua do último usado pela oferta — leia em
  `infoproduto/criativos/nomenclatura.md`; se não estiver lá, pergunte. Nunca comece do `001` por
  conta própria quando já houver criativo dessa oferta.
- **Roteiro com versões de preço** (7/9/10) é um número só, com sufixo de versão. O título leva o
  nome sem sufixo e as OBSERVAÇÕES listam as versões: "Versões: `_V1` = R$7 · `_V2` = R$9 · `_V3` = R$10".
- **ELEMENTOS NECESSÁRIOS:** tudo que precisa existir pra gravar a peça e que **não está no dia a
  dia** de quem grava. Objeto comum da casa não entra; objeto específico entra. Locação fora de
  casa entra sempre. Saia da coluna TELA: cada insert, objeto e resultado citado lá tem que estar
  listado aqui. Take que pode vir de material já gravado (aulas do curso, anúncio antigo) diz isso.
- **Coluna FALA:** uma ideia por linha da tabela. Sem rubrica, sem parêntese de direção dentro da
  fala. A medição (`scripts/medir_falas.py`) roda só nesta coluna.
- **Coluna TELA:** a direção entra **na linha em que ela começa a valer**. Célula vazia = segue o
  plano anterior. Descreva imagem, não intenção ("close da planilha preenchendo sozinha" ✓ ·
  "passar desejo" ✗). Texto que aparece escrito na tela vai entre aspas e em negrito.
- **Layout na coluna TELA** — quando a peça usa material já gravado (aulas do curso, anúncio antigo),
  cada célula começa pela marcação do layout e diz de onde vem o take:
  - **[VOCÊ]** — quem grava, filmado na hora (troque pelo nome de quem grava, se não for você)
  - **[INSERT]** — take de material existente em tela cheia
  - **[DIVIDIDA ↑insert ↓VOCÊ]** — take em cima, quem grava embaixo, mostrando
  - **[DIVIDIDA ↑insert ↓insert]** — dois takes, um em cima e um embaixo
  - fonte do take em itálico: *curso · aula 3 · demonstração*. Take que talvez não exista no
    material vai com `[?]` e entra na nota única.
  Quando o pedido é o mínimo de produção, a regra é: **quem grava só grava a própria fala; tudo
  que é demonstração, técnica e resultado sai do material existente.**
- **Ação contínua** (quem grava fazendo a mesma tarefa a peça inteira) se escreve uma vez, na
  primeira linha, com "vai repetindo o movimento enquanto fala" — não se repete linha a linha.
- **Preço com variação de teste** se escreve `7/9/10 reais` na fala, e a regra de gravação fica
  nas INSTRUÇÕES do pack. Só existe no ultra low ticket: no low ticket e na VSL o anúncio não tem
  preço, então não há regra de gravação de preço nem sufixo `_V`, e a regra de EDIÇÃO proíbe
  produto e preço na tela (ver o SKILL.md de cada uma).
- **Silêncio e pausa** são direção de tela: "Ficar em silêncio 3 segundos, enquanto faz alguma
  coisa com as mãos".
- Nada de nota, fonte ou disclaimer dentro do pack. Tudo isso fica no bastidor.
