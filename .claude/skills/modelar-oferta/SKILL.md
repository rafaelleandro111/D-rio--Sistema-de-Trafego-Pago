---
name: modelar-oferta
description: Modelagem de oferta do Rafael. Pega uma oferta que já está validada e gerando dinheiro (escalando na Biblioteca de Anúncios), faz um raio-x completo (promessa, público, mecanismo, preço, bônus, garantia, funil, página, criativos) e entrega a receita pra ele ganhar em cima — Caminho A (rodar o mesmo produto como afiliado, com anúncios modelados) e/ou Caminho B (criar produto próprio parecido, com outro nome e mecanismo). Use quando o Rafael disser "modela essa oferta", "quero modelar", "faz a minha versão dessa oferta", "raio-x da oferta", "como eu ganho em cima dessa oferta", ou /modelar-oferta.
---

# /modelar-oferta — Modelar oferta validada

O Rafael é leigo: explicar simples. Modelar = pegar o que **já prova que
vende** e fazer a versão dele. Copiar a estrutura, nunca o conteúdo.

## Passo 1 — Achar ou receber a oferta

- **Ele mandou link** → rodar o validador no modo link (ver skill `validar-oferta`).
- **Ele mandou nicho** → rodar o validador no modo busca e pegar a melhor do ranking.
- Ver a **tendência** no acompanhamento diário (skill `acompanhar-ofertas`): só modelar 🚀 ESCALANDO, 📈 SUBINDO ou ➡️ ESTÁVEL. 📉/💀 → não modelar.
- Só modelar oferta com **sinal de escala** (muitos anúncios ativos, criativos
  novos nos últimos 15 dias). Sem sinal → avisar que não está provada e
  perguntar se quer seguir mesmo assim.
- Ler `_memoria/aprendizados.md` antes (nichos e canais que já deram certo/errado pro Rafael).

## Passo 2 — Raio-x da oferta

Fontes: página de vendas (abrir o link com WebFetch, ou `_pagina.resumo_pagina`
na ficha do validador) + anúncios dela em `marketing/espiao/<pasta>/anuncios.json`
(filtrar pelo domínio da oferta; olhar as capas em `imagens/`).

Preencher:

| Item | O que anotar |
|---|---|
| Promessa principal | A grande promessa em 1 frase |
| Público e dor | Quem compra e qual problema quer resolver |
| Mecanismo | O "segredo"/método com nome próprio que explica por que funciona |
| Formato do produto | E-book, aula, planilha, app, acervo… e tamanho |
| Preço | Preço cheio, "de/por", parcelamento |
| Bônus | Lista e o valor que a página dá pra cada um |
| Garantia | Dias e tipo |
| Checkout | Plataforma, order bump, upsell (se der pra ver) |
| Página | Tipo (vendas direta, VSL, nativa/notícia, quiz) e ordem das seções |
| Criativos que escalam | Top 3: gancho, ângulo, formato, duração, nº de cópias |
| Canal | Onde roda (Meta, Google, TikTok) |
| Pontos fracos | O que a oferta faz mal (oportunidade pra versão do Rafael) |

Fechar com a **nota do validador** e a **chance do conselho** (skill `conselho`).

## Passo 2B — Persona Profunda (alimenta as skills de página e criativos)

Salvar em `infoproduto/alicerce-do-copy/persona-profunda/persona-profunda-<oferta>.md`,
com as seções abaixo (as skills `pagina-de-vendas` e `escrever-criativos-low-ticket`
leem esse arquivo; o mapa completo está em
`.claude/skills/pagina-de-vendas/references/mapa-persona-profunda.md`).
Fonte: página de vendas + textos dos anúncios do espião (as **frases reais**
do mercado). Marcar com *(estimado)* o que for dedução e não dado.

S1 Demográfico · S2 Problemas · S3 Sintomas · S4.1 Dores · S4.2 Desejos ·
S4.3 Medos · S5 Conversas internas · S6 Transformação · S7.1 Linguagem (frases
literais dos anúncios/página) · S7.2–S7.5 Atenção, interesses, consumo de
conteúdo, perfil de compra · S8 Inimigos em comum · S9.1 Vieses a explorar ·
S9.2 Gatilhos de rejeição · S10 Objeções · S11 Subpersonas

Curto e direto: 3 a 6 itens por seção.

## Passo 3A — Caminho A: afiliado (mesmo produto)

Só se o produto **aceita afiliado** — pedir ao Rafael pra procurar na
vitrine da Hotmart/Kiwify (o nome do produtor costuma estar na página).

Entregar:
1. Se dá pra se afiliar + comissão (dado do Rafael)
2. **Regras do produtor** a confirmar (skill `anti-bloqueio`, Verificação 3)
3. Os 3 criativos que escalam **modelados**: mesmo gancho, ângulo, ordem,
   formato e duração — reescritos com outras palavras, outra imagem/vídeo.
   Usar o agente `copywriter` (ou a skill `ad-creative`) e passar pelo `anti-bloqueio`.
   Pra um pack maior de roteiros em vídeo (produto low ticket acima de R$ 10):
   skill `escrever-criativos-low-ticket` apontando pra página do produtor
4. Canal e verba de teste (lógica do agente `estrategista`): pausar o
   conjunto que gastar 1 comissão sem venda; teste no máximo 3 comissões
5. Diferencial possível do Rafael: bônus próprio ou página ponte (se o canal pedir)

## Passo 3B — Caminho B: produto próprio (versão do Rafael)

Usar `.claude/skills/conselho/references/ladeira.md` (low ticket) e
`.claude/skills/offers/SKILL.md` (montar oferta).

Entregar a **receita do produto**:
1. **Promessa** — mesma dor e mesmo desejo, com palavras do Rafael
2. **Mecanismo novo** — outro nome e outro ângulo pro "segredo" (nunca o nome do concorrente)
3. **O que o produto precisa ter** — formato, módulos/capítulos, tamanho.
   Corrigir os pontos fracos do original. Conteúdo **criado do zero**
4. **Preço** — na faixa do original (low ticket R$ 27–200); sugerir 2 preços pra testar
5. **Bônus e garantia** — equivalentes, com valor percebido
6. **Order bump** — 1 sugestão barata (20–40% do preço) que complementa
7. **Página de vendas** — skill `pagina-de-vendas` usando a página original
   como **referência** (ela desmonta bloco por bloco e escreve a do Rafael
   no mesmo esqueleto, com a Persona Profunda do Passo 2B). Alternativa
   mais simples: `copy-thief`
8. **Anúncios** — skill `escrever-criativos-low-ticket` (pack de 12 roteiros,
   se o produto custa acima de R$ 10) ou agente `copywriter`; sempre com `anti-bloqueio`
9. **Onde vender** — Hotmart ou Kiwify; e se abre programa de afiliados
10. **Esforço** — quanto tempo/trabalho pra produzir (o Rafael está sozinho)

## Limites (proteger o Rafael)

- **Pode modelar:** promessa, público, estrutura da oferta, faixa de preço,
  tipo de bônus, ordem da página, estrutura dos anúncios.
- **Não copiar:** texto, vídeo, imagem, nome do produto/método, logo, rosto,
  depoimentos ou o conteúdo do produto de outra pessoa. Isso gera denúncia
  de direito autoral, anúncio derrubado e conta bloqueada — e no Caminho B
  pode virar processo.
- Promessas da versão do Rafael passam pelo `anti-bloqueio`. Se a oferta
  original promete algo proibido e está rodando, **não** repetir — ela pode
  cair a qualquer momento.

## Entrega

Salvar em `marketing/modelagem/<oferta>-<data>.md` e responder ao Rafael:

1. Raio-x em tabela (curto)
2. Nota do validador + chance do conselho
3. **Caminho A** (se aceita afiliado) e **Caminho B** — cada um com o
   próximo passo concreto
4. Recomendação: qual caminho começar e por quê (considerar capital baixo,
   tempo e o que está em `_memoria/aprendizados.md`)
