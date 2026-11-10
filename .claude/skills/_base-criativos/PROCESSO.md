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

# O processo de escrever criativos — o macro

Vale pra todas as skills de escrita de criativo (ultra low ticket, low ticket e VSL agora;
lançamento em breve). O que muda entre elas é o micro — CTA (o pedido de clique), preço, urgência,
destino — e está no SKILL.md de cada uma.

| Skill | Destino do clique | Produto e preço no anúncio | CTA |
|---|---|---|---|
| ultra low ticket (até R$ 10) | página com checkout | preço em toda peça | "clica em Saiba Mais" pra garantir |
| low ticket (acima de R$ 10) | página com checkout | **nunca** | convite pra ver o material que você preparou |
| VSL | aula ou vídeo gratuito | **nunca** | convite pra assistir a aula gratuita |

**A ordem é fixa, e não se pula etapa:**

```
1 MERCADO E FORMATO  →  2 PESSOAS  →  3 GANCHOS  →  4 ROTEIROS  →  5 PORTÃO
      aprova               aprova        escolhe         revisa        entrega
```

**A forma de todo pack: 12 criativos = 4 pessoas × 3 criativos.**
- **4 pessoas** saem da etapa 2 — nem mais, nem menos.
- **3 criativos por pessoa**, e os 3 de uma mesma pessoa têm **formato diferente e ângulo diferente**
  entre si. Assim, dentro de cada pessoa, o pack testa 3 portas de entrada distintas.
- Entre pessoas, formato e ângulo podem se repetir.
- Versões de preço (`_V1`, `_V2`…) não contam como criativo novo: 12 é o número de roteiros.

**Aos poucos:** cada etapa termina numa parada. Você escreve a etapa no arquivo do pack,
mostra o resumo em chat e **para até o usuário aprovar ou corrigir**. Nunca emende duas
etapas numa resposta. Correção do usuário numa etapa é incorporada no arquivo antes de seguir.

**No chat, português simples.** Os códigos (S4.1, H07, P2, [CPA]) ficam no arquivo. Na conversa,
diga em uma frase o que a etapa faz e por quê, e mostre só o que ele precisa decidir.

---

## Antes da etapa 1 — conferir o que já existe

Rode na raiz do Info OS (só dentro do projeto, nunca no disco inteiro):

```bash
find infoproduto/alicerce-do-copy infoproduto/criativos infoproduto/funil marca -type f -name "*.md" -o -name "pagina.html" 2>/dev/null
```

1. **Alicerce do Copy (obrigatório).** Precisa existir
   `infoproduto/alicerce-do-copy/persona-profunda/persona-profunda-*.md` (a Persona Profunda, com as
   11 seções). **Se não existir, pare** e diga:
   > "Antes dos anúncios, a gente precisa do seu Alicerce do Copy — é dele que saem as pessoas pra
   > quem o anúncio fala, as dores delas e as frases exatas que elas usam. Sem ele eu escreveria
   > anúncio genérico, que ninguém para pra ver. Roda o `/alicerce-copy` e volta aqui."
   Não ofereça "seguir assim mesmo".
2. **Página de destino.** `infoproduto/funil/pagina-de-vendas/<produto>*/pagina.html` (da
   `/pagina-de-vendas`) e/ou a URL da página no ar. É contra ela que o anúncio é conferido (etapa 5).
   Se não houver nenhuma das duas, pare e peça — ou sugira o `/pagina-de-vendas` antes.
3. **Biblioteca de anúncios** (`infoproduto/criativos/biblioteca-anuncios/`) — ver etapa 1.
4. **Tom de voz** (`infoproduto/alicerce-do-copy/tom-de-voz/tom-de-voz-*.md`) — opcional; se
   existir, vale pras falas do especialista (ver `REGRAS-ESCRITA.md`).
5. **Identidade visual** (`marca/DESIGN.md`, seção "Anúncios em vídeo") — recomendada. É dela que
   saem a fonte, a cor e a tarja do texto na tela, a legenda e a tela final, que vão pra regra de
   EDIÇÃO do pack — assim o anúncio e a página parecem da mesma marca. Se não existir, siga e avise
   numa linha: "Sem a sua identidade visual, o editor escolhe fonte e cor do texto na tela. Roda o
   `/identidade-visual` antes de mandar pra edição."
6. **Nomenclatura** (`infoproduto/criativos/nomenclatura.md`) — código da oferta e último número.
   Se não existe, crie seguindo `NOMENCLATURA.md` (e ajude o usuário a escolher o código).

Havendo `-v2`, `-v3` de qualquer documento, use a versão mais alta.

---

## O arquivo do pack — um só, que cresce

Toda a produção de um pack vive num único `.md`. As etapas 1 a 3 ficam no topo, como
**bastidor**; as etapas 4 e 5 formam o **pack** propriamente dito, no modelo de
`MODELO-ENTREGA.md`, embaixo da marca `PACK`. É essa parte de baixo que vai pra gravação e edição.

**Onde salvar:** `infoproduto/criativos/packs/pack-NN-<produto>.md` (ex.: `pack-01-receitas-praticas.md`),
com `NN` = número do pack em 2 casas. Crie a pasta se não existir.
Refazer um pack inteiro = sufixo `-v2`; a versão superada é apagada quando a nova fecha.
**Abrir** o arquivo ao criar e a cada etapa concluída: `open <arquivo>` no Mac, `start "" "<arquivo>"`
no Windows.

Cabeçalho do arquivo:

```markdown
# Pack <NN> · <Produto> · <tipo de venda>
**Destino:** <URL ou caminho da pagina.html> · **Checkout:** <plataforma> · **Preço(s):** <…>
**Oferta:** <código> · **NUMs deste pack:** <primeiro>–<último>
**Status:** etapa <n> de 5 — <aguardando aprovação | aprovada em AAAA-MM-DD>
**Fontes lidas:** <lista dos arquivos, com data>
**Tom de voz:** <arquivo usado | ainda não extraído (`/tom-de-voz`)>
```

---

## Etapa 1 · Mercado e formato

**Pergunta da etapa:** o que o mercado está rodando e quais formatos cabem neste produto
e em quem vai gravar?

**Ler:**
1. **Biblioteca de anúncios** (`infoproduto/criativos/biblioteca-anuncios/`) — o `README.md` (índice)
   e o `dissecacao.md` de cada anunciante: formatos em uso, há quanto tempo cada anúncio está no
   ar, ganchos, preço no anúncio.
   **Se a pasta está vazia ou não existe:** não minere por conta própria. Abra
   `infoproduto/alicerce-do-copy/pesquisa-de-mercado/mapa-concorrentes.md`, escolha 2 ou 3
   concorrentes que anunciam (de preferência os de oferta mais parecida com a do usuário) e diga:
   > "Pra saber o que está funcionando no seu mercado, preciso ver os anúncios dos seus
   > concorrentes. Roda o `/biblioteca-anuncios-meta` com o link da Biblioteca de Anúncios de
   > <concorrente A>, <B> e <C> — os links estão no seu mapa de concorrentes."
   Se o mapa não tiver o link, ensine: abrir a Biblioteca de Anúncios da Meta, buscar o nome da
   página do concorrente e copiar o link da página de resultados.
   Se o usuário quiser seguir sem, declare no arquivo que a leitura de mercado está incompleta.
2. **Os próprios anúncios do usuário**, se ele já anunciou: quais rodaram e o custo por compra
   (CPA) de cada um no Gerenciador. O que já funcionou pra ESTA pessoa gravando pesa mais que
   qualquer concorrente. Se nunca anunciou, registre "sem histórico próprio".
3. **Catálogo de formatos** — `formatos/README.md` e as fichas dos candidatos.
4. **Restrição de produção** — quem grava, com o quê, sozinho ou com ajuda, se tem editor.
   Pergunte se não souber (o `_contexto/` pode responder).

**Escrever no arquivo:**
- **O que o mercado está rodando** — tabela: formato · quantos anunciantes / peças · há quanto tempo
  está no ar a peça mais antiga · preço aparece? · observação. Contagem com denominador. Advertência:
  *repetição mede aposta; tempo no ar é o sinal mais próximo de resultado, e ainda não é prova.*
- **Formatos candidatos** (6 a 10) — tabela: formato (link da ficha) · por que entra (evidência:
  mercado, anúncio próprio, ou lacuna que ninguém ocupa) · dificuldade pra quem grava · risco.
- **Formatos descartados** que pareciam óbvios, com o motivo em uma linha.

**Parada:** "Esses são os formatos candidatos. Tira, põe ou segue?"

---

## Etapa 2 · Pessoas

**Pergunta da etapa:** quem eu quero alcançar com este pack? Cada formato e cada ângulo
conversa com uma pessoa diferente.

**Ler — a Persona Profunda** (`infoproduto/alicerce-do-copy/persona-profunda/`), nesta ordem:
- `persona-profunda-*.md`:
  - **S11 Subpersonas** (os tipos de cliente) — a lista de partida.
  - **S4 Emoções** (dores, desejos, medos) e **S5 Conversas internas** — o que move cada uma.
  - **S10 Objeções** — o que trava o clique e a compra.
  - **S7.1 Linguagem** — as palavras dela. **É daqui que sai o vocabulário dos ganchos.**
  - **S7.2 Tópicos que prendem** — matéria-prima de assunto do momento.
  - **S9.2 Gatilhos de rejeição** — o que não pode aparecer.
- `banco-verbatim-*.md` — o banco de frases do público, por assunto: as falas literais pra cada
  dor, medo, desejo e objeção.
- `matriz-beneficios-*.md` — a matriz da subpersona: a escada feature → funcional → emocional →
  identidade.

**Escrever no arquivo — exatamente 4 fichas de pessoa-alvo** (se a pesquisa sustentar mais, traga
as sobras numa lista curta de "consideradas" e recomende quais 4 ficam):

```markdown
### P1 · <nome curto e fácil de lembrar> (subpersona S11.x)
- **Quem é e em que momento está:** …
- **A dor ou o desejo que faz ela clicar NESTE produto, NESTE preço:** … (fonte: S4.x)
- **A frase dela** (literal, da Persona Profunda ou do banco de frases): "…"
- **A objeção que trava:** … (S10.x) → **o que desarma:** …
- **Nível de consciência:** …
- **Formatos que falam com ela** (da etapa 1): …
- **Ângulos que abrem ela:** …
```

Toda afirmação sobre a pessoa aponta a seção da Persona Profunda. O que não está lá entra como **[?]**.

**Parada:** "Essas são as pessoas do pack. Alguma sobra, falta alguém?"

---

## Etapa 3 · Ganchos

**Gancho** = os 3 primeiros segundos do vídeo: a frase, a imagem e o texto que fazem a pessoa
parar de rolar o feed.

**Pergunta da etapa:** qual é o primeiro contato — os 3 primeiros segundos — pra cada pessoa?

Cruze **pessoa × ângulo × formato**. Ângulos em `ANGULOS.md` (17). Cada gancho é uma
combinação; nenhuma se repete.

**Quantidade:** **7 ganchos por pessoa (28 no total)**, cada pessoa com pelo menos 4 formatos e 5
ângulos diferentes na sua bateria — pra que dê pra escolher 3 com formato e ângulo distintos.

**Cada gancho tem três camadas** — o gancho não é só a frase:
- **Fala** — a primeira frase dita (regras de escrita valem: linha natural, vocabulário da pessoa,
  promete sem explicar).
- **Visual** — o que está na tela no frame 0 (o primeiro quadro do vídeo).
- **Texto na tela** — se houver.

**Escrever no arquivo — tabela agrupada por pessoa:**

| ID | Pessoa | Ângulo | Formato | Fala do gancho | Visual (frame 0) | Texto na tela |
|---|---|---|---|---|---|---|
| H01 | P1 | Curiosidade | Fala e Faz | "…" | … | … |

Depois da tabela, **a recomendação: os 3 de cada pessoa** que você escolheria (formato e ângulo
distintos entre si), com uma linha de porquê cada — evidência do mercado ou da Persona Profunda,
nunca gosto.

**Parada:** "Escolhe 3 ganchos por pessoa — formato e ângulo diferentes entre os 3. Pode marcar os
IDs e mexer em qualquer um."
O usuário pode reescrever o gancho: a versão dele vale, palavra por palavra.

---

## Etapa 4 · Roteiros

Só dos ganchos escolhidos. Cada roteiro no modelo de `MODELO-ENTREGA.md`, seguindo
`REGRAS-ESCRITA.md` e as regras do tipo de venda (SKILL.md da skill em uso).

- O roteiro **começa pelo gancho aprovado, intacto**.
- O **formato** manda na estrutura: siga a "Estrutura típica" e as "Armadilhas" da ficha.
- A **pessoa** manda no corpo: a dor, a objeção e as palavras vêm da ficha dela (etapa 2).
- **A voz:** fala do especialista segue o documento de tom de voz, se existir, e passa pela régua
  de 7 notas (§11) antes de ser mostrada (ver `REGRAS-ESCRITA.md`).
- Cada roteiro registra, no bastidor, de onde veio: `Pessoa · Ângulo · Formato · Gancho Hxx`
  (e a nota da régua de voz, se houver) — nada disso vai pro pack.
- Cada roteiro sai com o bloco **ELEMENTOS NECESSÁRIOS** (ver `MODELO-ENTREGA.md`).
- Rode `scripts/medir_falas.py` no pack antes de mostrar.

Entregue **por pessoa: 3 roteiros de cada vez**, e pare entre as pessoas (4 blocos).

**Parada:** "Roteiros prontos. Revisa e me diz o que muda."

---

## Etapa 5 · Portão

**Portão** = a checagem final antes de o pack ir pra gravação. Nada passa sem ela.

1. **Releia o pack inteiro** contra `REGRAS-ESCRITA.md` e as regras do tipo de venda. Toda violação
   encontrada e corrigida entra numa tabela (peça · violação · regra · correção).
2. **Tabela de medições** — a saída do `scripts/medir_falas.py`: peça · linhas · mediana · micro% · longas.
3. **Message match** (o anúncio promete o que a página entrega logo de cara) — abra a
   `pagina.html` (ou a página no ar) e leia a **primeira dobra**: o que aparece antes de rolar —
   no wireframe da `/pagina-de-vendas`, o bloco Hero (o primeiro `<section>`: headline,
   subheadline, preço, botão). Se houver `<produto>-v2`, `-v3`, leia a versão mais alta. Tabela: peça · o que promete · onde a página paga · está na 1ª dobra? Qualquer
   "não" é defeito: muda a peça ou muda a página.
4. **Lista de produção** — a soma dos ELEMENTOS NECESSÁRIOS de todas as peças, sem repetição,
   agrupada por cenário e por preparo (o que preparar uma vez serve pra quais peças), pra gravar
   o pack num dia só.
5. **Nota única** — todo item inventado ou não confirmado `[validar]`: números, casos, prints de
   mensagem, depoimentos, "preço vai subir". Nunca espalhe aviso pelas peças.
6. **Nomenclatura** — atualize o último `NUM` e o histórico em `infoproduto/criativos/nomenclatura.md`.

O portão fica no bastidor. O pack que vai pra gravação e edição leva só as INSTRUÇÕES e as peças.

**Parada:** "Pack fechado. Está em `infoproduto/criativos/packs/…`. Se você usa o Google Drive, é só
copiar a parte de baixo da marca PACK. Quer que eu separe em dois arquivos, um pra quem grava e
um pro editor?"
