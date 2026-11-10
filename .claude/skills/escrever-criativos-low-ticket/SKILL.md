---
name: escrever-criativos-low-ticket
description: 'Escreve um pack de 12 anúncios em vídeo (roteiros prontos pra gravar e editar) para produto LOW TICKET, acima de R$ 10, vendido na página (anúncio → página de vendas → checkout) — com uma regra que define a skill — o anúncio NUNCA mostra o produto nem o preço, ele CONVIDA a pessoa a ver um material que você preparou, e o clique leva pra página. Cinco etapas com parada entre cada uma — mercado e formato (anúncios dos concorrentes + catálogo de 50 formatos) → pessoas (Persona Profunda) → 28 ganchos pra você escolher → roteiros → checagem final contra a página — e entrega tudo num arquivo em infoproduto/criativos/packs/. Use SEMPRE que o usuário disser "anúncio", "criativo", "roteiro de anúncio", "gancho", "pack de criativos", "lote de anúncios" pra um produto de R$ 17, 27, 37, 47, 67, 97, "low ticket", "produto de entrada", "tripwire", "anúncio que convida pra ver o material", "anúncio sem mostrar o produto", ou quando o destino do clique for uma página com checkout e o preço for acima de R$ 10. Precisa do Alicerce do Copy (sem ele, manda rodar /alicerce-copy). Até R$ 10 → escrever-criativos-ultra-low-ticket; aula ou VSL gratuita → escrever-criativos-vsl. NÃO sobe campanha.'
---

> **Adaptação pro projeto do Rafael (ler antes de tudo — vale mais que o texto abaixo):**
> - Rafael é afiliado/modelador de ofertas, não aluno de curso. Linguagem simples.
> - **Alicerce / Persona Profunda:** neste projeto quem cria é a skill `modelar-oferta`, em
>   `infoproduto/alicerce-do-copy/persona-profunda/persona-profunda-<oferta>.md`. Se não existir,
>   **não mandar rodar `/alicerce-copy`** (não existe aqui) — mandar rodar `/modelar-oferta` na oferta.
> - **Biblioteca de anúncios / mapa de concorrentes:** usar o nosso espião (`marketing/espiao/<palavra>-<data>/anuncios.json`
>   e as capas em `imagens/`) e o raio-x em `marketing/modelagem/`. Não existe `/biblioteca-anuncios-meta` aqui.
> - **Tom de voz:** `_memoria/preferencias.md` (não existe `tom-de-voz/`). Sem excesso de emoji.
> - **Identidade visual:** `identidade/design-guide.md` (pode estar vazio → paleta neutra).
> - **`/design-paginas` não existe aqui:** entregar o wireframe/página HTML como resultado final.
> - **Antes de entregar** qualquer anúncio ou página: passar pelo `anti-bloqueio` (Meta/Google/TikTok + regras do produtor).
> - Ler `_memoria/aprendizados.md`: ângulos e formatos que já funcionaram pro Rafael têm prioridade.
> - Origem: Info OS (github.com/oheitortoledo/info-os-produto), sem licença declarada — uso pessoal; ver `ORIGEM.md`.


# Escrever criativos — Low Ticket (acima de R$ 10)

**O macro está na base compartilhada.** Leia antes de começar, nesta ordem:

1. `.claude/skills/_base-criativos/PROCESSO.md` — o que conferir antes, as 5 etapas, as paradas, o arquivo do pack
2. `.claude/skills/_base-criativos/REGRAS-ESCRITA.md` — a régua de toda fala, o tom de voz e a medição em código
3. `.claude/skills/_base-criativos/MODELO-ENTREGA.md` — como o pack fica escrito
4. `.claude/skills/_base-criativos/ANGULOS.md` — os 17 ângulos
5. `.claude/skills/_base-criativos/formatos/README.md` — o catálogo (fichas sob demanda)
6. `.claude/skills/_base-criativos/NOMENCLATURA.md` — o nome de cada criativo

Este arquivo só traz **o que é próprio do low ticket**. Onde contradiz a base, vale este.
Todos os caminhos são relativos à raiz do Info OS.

---

## Pra quem é esta skill (vale pra sessão inteira)

Quem usa **não é copywriter nem gestor de tráfego**. É o especialista montando o próprio produto e
aprendendo o método agora. Duas regras:

1. **Por dentro, rigor total.** Os códigos (S4.1, P2, H07, [MÉTODO], [HIPÓTESE]), a régua de
   escrita, a medição em código, a nota única `[validar]` — tudo fica nos arquivos, nada afrouxado.
2. **Por fora, português simples.** No chat, trate por "você", uma coisa por vez, e diga em uma
   frase **o que está fazendo e por quê**. Palavra técnica só com tradução, na primeira vez que
   aparecer:

| Termo (nos arquivos) | Como explicar na primeira vez |
|---|---|
| criativo | cada anúncio (vídeo ou imagem) |
| pack | o lote de 12 anúncios que você grava de uma vez |
| gancho | os 3 primeiros segundos: a frase e a imagem que fazem a pessoa parar de rolar |
| ângulo | a porta de entrada do argumento (um erro, um segredo, uma promessa…) |
| formato | a "embalagem" do vídeo (caixinha de pergunta, tela dividida, fala enquanto faz…) |
| CTA | o pedido de clique no fim ("clica em Saiba Mais") |
| convite | o CTA deste funil: chamar a pessoa pra ver o material que você preparou |
| message match | o anúncio promete exatamente o que a página mostra logo que abre |
| primeira dobra | o que aparece na página antes de rolar |
| portão | a checagem final antes de ir pra gravação |
| UGC | vídeo com cara de gravado por um cliente comum, não por marca |
| CPA | quanto custou, em anúncio, cada venda |
| Persona Profunda | o retrato completo do seu cliente (do seu Alicerce do Copy) |
| subpersona / S11 | os tipos de cliente que você tem |
| verbatim | a frase exata que seu cliente usa |

---

## Status das regras deste funil — leia antes de usar

- **[MÉTODO]** — regra de como o Heitor escreve low ticket: o anúncio convida pra ver o material e
  a página é que vende. Não se negocia dentro desta skill.
- **[HIPÓTESE]** — raciocínio, sem dado medido. Serve pra testar, não pra travar.

**Ainda não há leitura de CPA registrada pra este funil.** Regra marcada [HIPÓTESE] nunca é usada
pra reprovar gancho do usuário. Ao fim de cada pack que rodar, o resultado por criativo volta pro
**Registro de calibração** no fim deste arquivo.

---

## A ideia do funil em uma frase

O anúncio **não vende**: ele entrega um pedaço de valor, abre uma vontade e **convida a pessoa a
ver o material que você preparou**. O material é a página. Quem vende o produto, com nome, entrega
e preço, é a página — nunca o vídeo. [MÉTODO]

Por isso o anúncio de low ticket se parece mais com o de VSL do que com o de ultra low: a diferença
é o destino (página com checkout, não aula) e a forma do convite.

---

## LEI MÁXIMA — todo criativo de low ticket

1. **O produto não aparece.** Nada de nome do produto, capa, mockup, módulos, "curso", "mentoria",
   "método X por R$…", bônus, garantia, "vagas", "comprar". Nem na fala, nem na tela. [MÉTODO]
2. **O preço não aparece.** Nem falado, nem escrito, nem riscado, nem "menos que um café". Preço é
   assunto da página. Por consequência, **não há versões de preço** (`_V1`, `_V2`) neste pack: teste
   de preço, se houver, acontece na página. [MÉTODO]
3. **O CTA é sempre um convite pra ver o material que você preparou**, e nomeia o botão real do
   anúncio. Modelo: "Eu preparei um material mostrando <o que a promessa do gancho entrega>. Clica
   em Saiba Mais pra ver." O que varia entre as peças é a palavra do material (material, página,
   passo a passo, explicação completa) e o que ele mostra — **nunca** vira "clica pra comprar". [MÉTODO]
4. **O convite não mente.** Não chame de "aula grátis", "curso gratuito" ou "presente" o que é uma
   página de vendas. "Preparei um material", "separei tudo numa página", "deixei explicado aqui" é
   verdade; "é de graça" só se a página realmente entrega conteúdo antes de pedir a compra — e aí
   entra na nota única como `[validar]`. Promessa de gratuidade que termina num checkout queima a
   confiança e é motivo comum de reprovação na Meta. [HIPÓTESE]
5. **A primeira dobra da página tem que parecer o material prometido.** A pessoa clicou pra VER
   algo: a página abre continuando o assunto do anúncio (headline que retoma a promessa), não com
   preço e botão de compra. Se a primeira dobra é o bloco de checkout, o convite vira isca e o clique
   morre. [MÉTODO]

Peça que viola qualquer um dos cinco volta antes de chegar ao usuário.

---

## O que muda no processo

### Antes da etapa 1 — conferir e perguntar o que faltar
Primeiro rode a conferência de `PROCESSO.md` (alicerce, página, biblioteca, tom de voz,
nomenclatura). Sem Persona Profunda, **pare** e mande rodar `/alicerce-copy`. Depois pergunte,
numa mensagem só, só o que os arquivos não responderam:

- **Produto e página de destino.** Leia a `pagina.html` da `/pagina-de-vendas`
  (`infoproduto/funil/pagina-de-vendas/<produto>*/pagina.html`) e/ou a URL no ar: a headline, o que
  aparece antes de rolar, onde entra o preço, o rodapé legal. Sem página, não há message match —
  pare e peça (ou sugira `/pagina-de-vendas`). O produto e o preço você lê **pra saber o que a
  página vai vender**, não pra colocar no anúncio.
- **O que é "o material"** na boca do especialista: como ele chama a página quando convida
  ("material", "página", "passo a passo", "vídeo explicando"…). Se a página tem vídeo no topo, o
  convite pode ser "gravei um vídeo explicando"; se não tem, não prometa vídeo.
- **Número do pack e último `NUM` da oferta** — em `infoproduto/criativos/nomenclatura.md`. O pack
  continua a sequência; nunca recomeça do `001`. Primeiro pack e sem arquivo → ajude a escolher o
  código de 3 letras (`NOMENCLATURA.md`) e crie o arquivo.
- **Quem grava e com o quê.** Prefira formatos de dificuldade 1–2 que você grava sozinho.

### Etapa 1 · Mercado e formato — o que olhar a mais
- **O encaixe por funil das fichas.** A linha "Low ticket" das fichas foi escrita pensando em
  anúncio que mostra produto e preço. **Neste funil, use a linha "VSL" como referência principal**
  (é o anúncio que também não mostra produto) e a linha "Low ticket" só como apoio.
- **Descarte na largada** os formatos cuja mecânica é mostrar a oferta: Oferta Direta (F37) e
  qualquer ficha em que o gancho do formato seja preço, produto na mão ou "o que vem no curso".
  Registre na tabela de descartados.
- **Na biblioteca dos concorrentes, separe dois grupos:** quem anuncia mostrando produto e preço, e
  quem anuncia sem mostrar (conteúdo + convite). O segundo grupo é o comparável direto; o primeiro
  serve pra formato e gancho, nunca pra CTA.

### Etapa 2 · Pessoas — o recorte do low ticket
A pessoa deste funil ainda **não está decidindo comprar**: está decidindo se vale a pena parar e
ver mais um material. Pra cada ficha de pessoa, acrescente:
- **O que ela ganha só de ver o material** — a curiosidade ou a dor que o clique resolve já, antes
  de qualquer compra (S4, S5).
- **O "por que não" dela pro clique** — quase sempre cansaço de conteúdo ("mais um guru", "já vi
  isso", "não tenho tempo"). Procure na S10 e no banco de frases. É isso que o gancho desarma —
  não a objeção de preço, que fica pra página.

### Etapa 3 · Ganchos — regras próprias
- **Nenhum gancho abre com produto ou preço** (LEI MÁXIMA). Abra por dor, desejo, curiosidade,
  erro, descoberta — os 17 ângulos estão todos disponíveis.
- **O gancho promete o que o material mostra.** Cada gancho tem que caber numa frase de convite no
  fim ("…preparei um material mostrando isso"). Gancho que promete algo que a página não mostra
  reprova no message match da etapa 5 — confira contra a primeira dobra já aqui. [MÉTODO]

### Etapa 4 · Roteiros — regras próprias
- **Estrutura:** gancho → um pedaço de valor real (um erro, um passo, uma virada de chave, dito
  com o vocabulário da pessoa) → a lacuna (o que falta pra pessoa fazer sozinha) → convite pro
  material. O valor é de verdade: a pessoa tem que sair do vídeo sabendo uma coisa a mais. [MÉTODO]
- **O convite é a última ideia do vídeo**, em uma ou duas linhas, e retoma a promessa do gancho com
  as mesmas palavras. Nada depois dele além da tela final. [MÉTODO]
- **Autoridade sem produto.** Prova de resultado (sua ou de aluno) pode aparecer como história ou
  número — "minha aluna fez X" — desde que não vire vitrine do produto ("no módulo 3 do meu
  curso…"). Número e depoimento seguem a regra 10 da base: não confirmado → `[validar]`.
- **Desqualificador leve é bem-vindo.** Acima de R$ 10, clique errado custa mais que no ultra low:
  uma linha dizendo pra quem o material é ("se você já <faz tal coisa>…") filtra antes da página.
  [HIPÓTESE]
- **Urgência só de conteúdo e só se for verdade** ("vou tirar esse material do ar domingo"). Nunca
  urgência de preço — o preço não existe no anúncio. Prazo não confirmado vai pra nota única.
- **Duração:** alvo de 30 a 60 segundos de fala — tempo pra entregar o pedaço de valor e convidar.
  [HIPÓTESE]
- **A voz é a sua.** Se existe o documento de tom de voz, a fala do especialista usa as suas
  palavras-assinatura, evita as proibidas e passa pela régua de 7 notas (§11) — ver
  `REGRAS-ESCRITA.md`. O convite soa como você chamando um amigo pra ver uma coisa, não como
  anúncio.
- **INSTRUÇÕES do pack:** não há regra de gravação de preço. No lugar, a regra de EDIÇÃO do pack
  proíbe produto na tela: "Nenhuma capa, mockup, preço ou nome do produto aparece no vídeo. A tela
  final é o convite: '<palavra do material>' + seta pro botão."

### Etapa 5 · Portão — itens a mais
- [ ] **Varredura de produto e preço** na parte PACK do arquivo (fala e tela). Rode na raiz do
      Info OS, trocando `<nome do produto>` pelo nome real:
      ```bash
      sed -n '/======= PACK/,$p' infoproduto/criativos/packs/pack-NN-<produto>.md | grep -n -i -E "R\\$|reais|real|preço|valor|desconto|promo|oferta|comprar|compra|checkout|curso|mentoria|módulo|bônus|garantia|vagas|<nome do produto>"
      ```
      Cada ocorrência é lida: se fala de produto, preço ou compra, é violação da LEI MÁXIMA e a peça
      volta. (Palavra solta em outro sentido — "vale a pena", "real" de verdade — passa.)
- [ ] 12/12 peças terminam em convite pro material, nomeando o botão real.
- [ ] Nenhuma peça chama a página de "grátis", "aula gratuita" ou "presente" sem `[validar]` na nota.
- [ ] **Message match com a primeira dobra:** pra cada peça, a promessa do gancho está na headline
      ou subheadline do topo da página, e o topo **não abre com preço nem botão de compra**. Se abre,
      diga em vermelho no topo da nota: **a página precisa abrir como o material que o anúncio
      promete — senão o convite vira isca.**
- [ ] O rodapé da página tem a identificação de quem vende (CNPJ e razão social, ou os dados que a
      sua plataforma de venda exige) e um contato — página sem isso costuma ter anúncio reprovado
      na Meta. Pendência vai pra nota única.
- [ ] Toda peça tem nome no padrão `[OFERTA]_Pack[N]_[FORMATO]_[NUM]`, sem número repetido e
      **sem sufixo de versão** (não há troca de preço no anúncio). Ao fechar, atualizar o último
      `NUM` em `infoproduto/criativos/nomenclatura.md`.
- [ ] 12 roteiros = 4 pessoas × 3, com formato e ângulo distintos dentro de cada pessoa.

---

## Registro de calibração — o seu

Aqui você registra o que aprendeu com os seus packs.

**Como ler o resultado:** depois de 3 a 7 dias no ar, abra o Gerenciador de Anúncios, filtre pelo
pack (o nome de cada anúncio é o nome do criativo) e anote por criativo: gasto, taxa de clique
(CTR), compras e custo por compra (CPA). Neste funil o anúncio e a página trabalham separados:
**CTR alto com CPA ruim** = o convite funciona e a página não converte (mexe na página);
**CTR baixo** = o gancho não para ninguém (mexe no anúncio). Cruze com o bastidor do pack (pessoa
· ângulo · formato · gancho). Uma peça só é sinal fraco; o mesmo padrão em 3+ peças é sinal de
verdade.

**Como registrar:** uma linha por mudança — data · regra · o que mudou (subiu de nível, caiu,
nova) · fonte (qual pack, quais criativos, quantas vendas).

| Data | Regra | O que mudou | Fonte |
|---|---|---|---|
| | | | |
