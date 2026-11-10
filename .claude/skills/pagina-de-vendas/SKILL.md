---
name: pagina-de-vendas
description: 'Transforma uma página de vendas de referência (que o aluno admira) na página de vendas DELE: faz a engenharia reversa da referência (blocos, texto e imagens, papel de cada bloco na venda), cruza com o Alicerce do Copy do aluno e escreve a copy inteira num WIREFRAME HTML, com cada espaço de imagem descrito e a lista do que falta ele providenciar. Uma entrada (o link ou arquivo da referência), uma parada (aprovar o plano), uma entrega (o wireframe). Use SEMPRE que o usuário disser "página de vendas", "monta minha página", "quero uma página igual a essa", "copia a estrutura dessa página", "engenharia reversa", "raio-x da página", "destrincha essa landing", "wireframe", "copy da página", "transforma meu alicerce em página", ou mandar link/print/HTML de página pedindo pra usar como base. Precisa do Alicerce do Copy — sem ele, manda rodar a /alicerce-copy antes. Depois da copy, oferece a /design-paginas pra vestir o wireframe com a marca e ter a página final pronta. NÃO publica página.'
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


# Página de Vendas

## Pra quem é esta skill

Quem usa esta skill **não é copywriter**. Está montando o próprio infoproduto e aprendendo o processo agora. Isso muda duas coisas, e as duas valem pra sessão inteira:

1. **Por dentro, rigor total.** O mapeamento contra as 11 seções da persona profunda, a regra de verbatim, a proibição de dado inventado — tudo continua valendo. A qualidade da página vem daí.
2. **Por fora, zero jargão.** Na conversa, nunca diga "S5", "seção-motor", "VoC", "verbatim", "intensidade × frequência", "mecanismo de copy". Use os nomes em português da tabela abaixo. Os códigos (S1–S11) só aparecem nos arquivos de trabalho (comentários do HTML e raio-X), nunca no chat.

Fale curto, uma coisa por vez, e sempre diga **o que você está fazendo e por quê** em uma frase — ele está aprendendo o método enquanto usa.

### Nomes que o aluno vê

| Código (só nos arquivos) | Como falar com o aluno |
|---|---|
| S1 | quem é o seu cliente (perfil) |
| S2 | o problema de verdade |
| S3 | como o problema aparece no dia a dia |
| S4.1 | o que dói |
| S4.2 | o que ele quer |
| S4.3 | o que ele tem medo que aconteça |
| S5 | o que ele pensa e não fala |
| S6 | o antes e o depois |
| S7 | como ele fala, onde presta atenção e como compra |
| S8 | o culpado (o que ele acha que atrapalha) |
| S9.1 | o que empurra ele pra comprar |
| S9.2 | o que faz ele desconfiar e fugir |
| S10 | as desculpas pra não comprar (objeções) |
| S11 | os tipos de cliente que você tem |
| verbatim | "a frase exata que seu cliente usa" |
| slot de imagem | "espaço de imagem" |
| `.nota` | "o que falta você providenciar" |

---

## O fluxo (o aluno só age em 2 momentos)

```
[aluno] manda a página de referência
   ↓
0. confere o alicerce e o design ──► sem alicerce: PARA
1. lê a referência (texto + imagens)
2. quebra em blocos e entende cada um  → raio-x.md (arquivo de trabalho)
3. monta o plano da página DELE
   ↓
[aluno] aprova o plano  ◄── única parada
   ↓
4. escreve a copy
5. veste no wireframe HTML
6. checa e entrega (abre no navegador)
   ↓
[aluno] quer a página final com a cara da marca?
   ↓ sim
7. roda a /design-paginas no mesmo wireframe → pagina-final.html
```

---

## Passo 0 — Conferir o que já existe

### 0.a — Alicerce (obrigatório)

Procure o alicerce **dentro do projeto do aluno**, nunca no disco inteiro (buscar fora traz o alicerce de outro produto, e trocar de cliente no meio é o pior erro possível aqui). Rode na raiz do Info OS:

```bash
find infoproduto -path "*alicerce-do-copy*" -type f -name "*.md" 2>/dev/null
```

O alicerce mora em `infoproduto/alicerce-do-copy/`, em três pastas: `pesquisa-de-mercado/`, `persona-profunda/` (a persona profunda, a matriz de benefícios e o banco de frases) e `tom-de-voz/`. O `README.md` da raiz resume tudo — leia primeiro. O documento das 11 seções, que o mapeamento dos Passos 2 e 3 usa, é o `persona-profunda-*.md` dentro de `alicerce-do-copy/persona-profunda/` (se houver `-v2`, `-v3`, use a versão mais alta).

Se houver mais de um produto/cliente, pergunte de qual é a página antes de seguir.

**Se não houver alicerce, pare.** Diga, nessas palavras ou parecido:

> "Antes da página, a gente precisa do seu alicerce — é dele que sai tudo que a página vai falar (as dores, as frases que seu cliente usa, as desculpas que ele dá pra não comprar). Sem ele eu escreveria uma página bonita que ninguém se reconhece. Roda o `/alicerce-copy` e volta aqui com a mesma página de referência."

Não ofereça "seguir assim mesmo". Pro aluno do curso, página sem alicerce é página genérica, e ele vai concluir que o método não funciona.

Se achar o banco de frases (`*verbatim*`), use também. Se não achar, puxe as frases das colunas de evidência da própria persona profunda — não precisa parar por isso.

**Tom de voz:** se existir `tom-de-voz/tom-de-voz-*.md`, ele é obrigatório na escrita (Passo 4). Se não existir, siga, mas avise numa linha: "Sem o seu tom de voz a página vai sair na voz do seu cliente, não na sua. Quando tiver, rode `/tom-de-voz` e eu ajusto."

### 0.b — Design (opcional)

Procure a identidade visual da marca do aluno (`marca/DESIGN.md`, criado pela `/identidade-visual`):

```bash
find . -path ./.claude -prune -o -type f \( -iname "DESIGN.md" -o -iname "tokens.json" -o -iname "design-guide.md" \) -print 2>/dev/null
```

Se achar, as cores dele entram no wireframe (Passo 5). Se não achar, siga com a paleta neutra — não é bloqueio: o wireframe é pra revisar a copy, e a identidade entra no design, no Passo 7. Se não houver, avise numa linha que ela é necessária pro Passo 7: `/identidade-visual`.

### 0.c — Onde salvar (uma pasta só)

Tudo desta rodada mora junto:

```
infoproduto/funil/pagina-de-vendas/<nome-curto>/
├── raio-x.md        ← a análise da referência (arquivo de trabalho)
├── imgs/            ← imagens baixadas da referência (de outra pessoa: nunca vão pra página final)
├── pagina.html      ← o wireframe (a entrega desta skill)
├── fotos/           ← as fotos DO ALUNO, com o número do espaço de imagem (foto-01.jpg…) — Passo 7
├── direcao-de-criacao.md ← Passo 7
└── pagina-final.html     ← a página com a cara da marca — Passo 7
```

`<nome-curto>` é o nome do produto em minúsculas com hífen. Se já existir, versione com sufixo (`-v2`), nunca sobrescreva.

Nunca salve em `Downloads`, na área de trabalho, nem fora do Info OS.

---

## Passo 1 — Ler a referência

Diga ao aluno o que está fazendo: *"Vou ler a página inteira — texto e imagens, porque muita coisa importante em página de vendas está escrita dentro da imagem."*

### 1.a — O texto

| O aluno mandou | Como tratar |
|---|---|
| **Link** | `WebFetch` na URL pedindo o texto completo por seção, em ordem, com títulos e botões. Se vier vazio (página feita em JS), peça um print da página inteira ou o arquivo salvo (no navegador: Ctrl/Cmd + S). |
| **Arquivo .html ou pasta** | `python3 .claude/skills/pagina-de-vendas/scripts/extrair_blocos.py <caminho>` |
| **Print ou PDF** | Leia direto. Fundos alternados, colunas e cards marcam onde um bloco termina. |
| **Texto colado** | Títulos e quebras de assunto marcam os blocos. Avise que sem as imagens a análise fica parcial. |

Se o `python3` não existir na máquina (comum no Windows), não trave: diga que falta o Python (a aula de instalação cobre), e siga lendo pelo `WebFetch` ou pelo print.

### 1.b — As imagens (obrigatório com link ou HTML)

```bash
python3 .claude/skills/pagina-de-vendas/scripts/extrair_imagens.py <url> --out <pasta-da-rodada>/imgs
```

Depois **abra cada arquivo com a ferramenta de leitura de imagem**. Baixar não é ler. É dentro das imagens que costumam estar: os balões de pensamento, os prints de depoimento, o título dos entregáveis no mockup, os selos de garantia, o antes e depois. Quem pula isso mapeia a página errada e não percebe, porque o resultado fica coerente do mesmo jeito.

Descreva cada imagem pelo **conteúdo**, nunca pela dimensão: "print de conversa de WhatsApp com aluna agradecendo, sem sobrenome" — não "PNG 697×473". Se o script avisar que não converteu um arquivo e ele não abrir, peça ao aluno um print daquele trecho.

---

## Passo 2 — Quebrar em blocos (o raio-X)

Isso é trabalho interno. Mostre ao aluno só o resumo no Passo 3.

**Bloco é unidade de venda, não de código.** Uma área que tem uma transição *e* três pilares são dois blocos. Duas áreas seguidas que formam um só argumento são um bloco. Nomeie pelo que o bloco **é** ("tabela sintoma × causa"), não pela classe do HTML.

Para cada bloco, registre: **função na venda**, **como ele faz** (formato + movimento), **seção-motor** e no máximo duas de apoio.

- Leia `references/mapa-persona-profunda.md` antes de atribuir — ele tem os sinais de cada seção e as confusões mais comuns.
- `references/arquetipos-de-bloco.md` é atalho de reconhecimento; o texto real da página sempre ganha da tabela.
- **Uma seção-motor, e apoio só quando faz diferença.** O teste: *se essa seção sumisse da persona profunda, o bloco ainda existiria?* Não existiria → motor. Só ficaria mais fraco → apoio. Se quase todo bloco ficou com três seções, você preencheu em vez de decidir.
- Objeção nunca é só "S10": diga a camada (S10.3, confiança no mentor, etc.).
- Bloco que existe só por convenção ou respiro: diga isso, não force mapeamento.
- Registre também o **inventário de imagem** por bloco — é dele que saem os espaços de imagem do wireframe.

Salve em `raio-x.md` usando `assets/template-raiox.md`.

---

## Passo 3 — O plano da página DELE (a única parada)

Agora cruze o raio-X com o alicerce do aluno. **A referência dá a ordem e o formato. O alicerce dá as palavras.**

Regras do plano:

- **A referência define a ordem, não o teto.** Se a persona profunda tem algo dominante (≥30 menções) sem lugar na referência, crie o bloco. Se a referência tem um bloco que a persona profunda do aluno não sustenta, corte — bloco inventado é pior que bloco ausente.
- **Frequência decide o tamanho.** Dominante (≥30) merece bloco próprio ou headline. Secundário (15-29) vira bloco ou parte de um. Terciário (6-14) vira item de lista ou pergunta do FAQ.
- **Quando o documento do aluno e a referência discordam** (preço, garantia, prazo), vale o do aluno — a referência é de outro produto.

Mostre ao aluno em linguagem simples, numa lista curta, assim:

> **O plano da sua página (14 blocos)**
>
> 1. **Abertura** — a pergunta que seu cliente se faz + a promessa. *Vem de: o que ele quer.*
> 2. **O que ele pensa e não fala** — 5 frases exatas que seus clientes usaram. *Vem de: o que ele pensa e não fala.*
> 3. **O culpado** — por que não é culpa dele. *Vem de: o culpado.*
> …
>
> **Mudei da referência:** tirei o bloco de "depoimentos em vídeo" (você ainda não tem) e criei um de "as desculpas pra não comprar", porque é o que mais aparece na sua pesquisa.
>
> Posso escrever assim? Se quiser trocar a ordem, tirar ou incluir algum bloco, é agora.

Espere a resposta. Ajuste o que ele pedir e siga.

---

## Passo 4 — Escrever

Ordem de escrita ≠ ordem da página. Comece pelos blocos que mais dependem da pesquisa (o que ele pensa e não fala, os sintomas, o culpado, as objeções) — eles fixam o vocabulário. **Headline por último**: ela resume o que já ficou escrito.

Quatro regras que não se negociam:

1. **A frase real do cliente ganha da frase bonita.** Se existe uma frase do banco ou da persona profunda que serve, ela entra literal — sem polir, sem corrigir a gramática.
2. **Cada bloco puxa da sua seção.** Escrevendo o bloco do culpado sem ter aberto a S8? Está inventando.
3. **Nada de dado inventado.** Número de alunos, depoimento, credencial, faturamento, preço, tempo de mercado — se não está nos documentos do aluno, vira "o que falta você providenciar" (`.nota`), nunca um número plausível.
4. **Duas vozes, cada uma no seu lugar.** As frases do *cliente* (dor, o que ele pensa, objeções) vêm da pesquisa, literais. O *narrador* da página — quem explica, promete, chama pra compra — é o especialista, e fala como o documento de tom de voz manda: palavras-assinatura, vetos, jeito de abrir e fechar, as frases-lei dele. Palavra que não está em nenhum dos dois provavelmente é sua. Teste: apagando o nome do produto, dá pra saber o nicho *e* quem está falando? Se não dá, está genérico.

Com o tom de voz disponível, passe a página pela régua de 7 notas (§11 do documento de voz) antes do Passo 5. Média abaixo de 7,5 ou algum eixo abaixo de 6: reescreva os blocos do narrador.

**Nunca copie frase da referência.** Da referência vêm só a ordem e o formato.

---

## Passo 5 — Vestir de HTML

Copie `assets/wireframe-base.html` para `<pasta-da-rodada>/pagina.html` e preencha o corpo com os componentes de `references/blocos-html.md`. Não escreva CSS novo.

- **Cores:** se achou o design do aluno no Passo 0.b, troque as variáveis de cor do `:root` pelas dele (cor principal, fundo, texto, destaque). Senão, deixe a neutra.
- **Rastreabilidade:** acima de cada `<section>`, o comentário com seção-motor, apoio e a frase da persona profunda que originou o bloco. No fim do `<body>`, a tabela completa bloco → seção → linha da persona profunda. Não aparece no navegador.
- **Fundos:** normal → `.alt` → normal; transição e reoferta em `.dark`. Nunca dois `.alt` seguidos.
- **Espaços de imagem:** FOTO 01, 02, 03… em sequência na página toda. Cada um com briefing que alguém que nunca leu a copy consegue executar (o que aparece, enquadramento, o que a imagem precisa provar). Use o inventário de imagem do raio-X como ponto de partida.
- **O que falta providenciar:** `.nota` só pro que só o aluno tem — depoimentos, prints, números, preço, link do checkout. Nunca pra fugir de escrever copy difícil.

---

## Passo 6 — Checar e entregar

```bash
python3 .claude/skills/pagina-de-vendas/scripts/checar_wireframe.py <pasta-da-rodada>/pagina.html
```

Corrija tudo que ele apontar. Abra o arquivo no navegador (`open` no Mac, `start` no Windows) e diga ao aluno, curto:

1. **A página em uma frase** e quantos blocos ela tem.
2. **O que falta você providenciar** pra ela ir pro ar — em lista, do mais importante pro menos.
3. **Onde eu tive que decidir sem informação**, se aconteceu.
4. **Como revisar:** "Lê a página inteira no navegador como se fosse seu cliente. Onde você não se reconhecer, me fala o bloco e eu ajusto."

O wireframe é o briefing da página final: a copy está pronta e cada espaço de imagem diz o que produzir.

5. **A oferta do design** — sempre, no fim da entrega:

   > "A copy está pronta. Quer que eu transforme esse wireframe na página final, com as cores, as fontes e o jeito da sua marca, funcionando no computador e no celular? Se sim, me diz quando a copy estiver aprovada e, se já tiver, coloca as suas fotos em `<pasta-da-rodada>/fotos/` com o número de cada espaço de imagem (`foto-01.jpg`, `foto-02.jpg`…)."

   Não emende o design na mesma resposta: primeiro o aluno revisa a copy. Ajuste de copy pedido depois entra no `pagina.html` **antes** do design, nunca direto na página final.

---

## Passo 7 — Design (opcional, com o OK do aluno)

Aluno aprovou a copy e quer a página final → rode a `/design-paginas` apontando pra `<pasta-da-rodada>/pagina.html`. Ela lê o wireframe como fonte do texto, busca a identidade em `marca/DESIGN.md` (sem ela, manda rodar a `/identidade-visual` antes), para uma vez pra ele aprovar o visual e entrega `direcao-de-criacao.md` + `pagina-final.html` na mesma pasta. Ela nunca muda a copy nem sobrescreve o `pagina.html`.

---

## Erros que estragam a página

**Pular as imagens.** A análise fica coerente e errada: você conclui que a referência "não usa o que ele pensa e não fala" quando os balões estão inteiros dentro de um PNG.

**Escrever na sua voz.** O texto fica bom e não soa como ninguém. É o erro mais comum e o mais difícil de ver.

**Preencher o formato sem ter o conteúdo.** Seis balões porque o componente pede seis, com metade inventada. Três verdadeiros valem mais — o componente aceita quatro.

**Copiar a copy da referência junto com a estrutura.** Se uma frase sua é igual à da referência, você copiou o que não devia.

**Espaço de imagem vago.** "Foto do produto" não é briefing.

**Soltar jargão no chat.** Se o aluno ler "S5" ou "seção-motor", você falhou na parte de fora da skill. Traduza sempre.
