# Componentes: seção da persona profunda → HTML

Cada seção da persona profunda quer virar um formato específico. Este arquivo tem o snippet pronto de cada um, com a regra de quando usar e quantos itens.

Todos os componentes usam as classes já definidas em `assets/wireframe-base.html` — não escreva CSS novo. Se precisar de um formato que não existe aqui, componha com o que existe antes de inventar.

## Índice
- [Regras que valem para todos](#regras-que-valem-para-todos)
- [Slot de imagem e nota de produção](#slot-de-imagem-e-nota-de-produção)
- [Hero / Gancho](#hero--gancho)
- [S5 → Balões](#s5--balões)
- [S3 → Cards de sintoma](#s3--cards-de-sintoma)
- [S8 → Erros / COMPARATIVO / Tabela de diagnóstico](#s8--erros--comparativo--tabela-de-diagnóstico)
- [S6 → Antes × Depois e Duas escolhas](#s6--antes--depois-e-duas-escolhas)
- [S4.2 → Promessas e cards de benefício](#s42--promessas-e-cards-de-benefício)
- [S2 → Pilares / mecanismo](#s2--pilares--mecanismo)
- [Sistema nomeado do mecanismo (N elementos)](#sistema-nomeado-do-mecanismo-n-elementos)
- [Entregáveis e bônus](#entregáveis-e-bônus)
- [S11 → Para quem é](#s11--para-quem-é)
- [S9.1 → Stack de valor](#s91--stack-de-valor)
- [S7.5 → Caixa de oferta](#s75--caixa-de-oferta)
- [S10 → Prova social, autoridade, garantia, passos, FAQ](#s10--prova-social-autoridade-garantia-passos-faq)
- [S4.3 → Ponte e reoferta](#s43--ponte-e-reoferta)
- [S9.2 → Rodapé e desarmes](#s92--rodapé-e-desarmes)

---

## Regras que valem para todos

**O comentário acima de cada bloco carrega a rastreabilidade.** Formato fixo:

```html
<!-- ══ 04 · COMPARATIVO ══ | motor: S8 (vilão primário, 166 menções, Forte) · suporte: S4.2 | verbatim: "cada vídeo fala uma coisa diferente" (E#12) -->
```

Não aparece no navegador e viaja junto com o arquivo. É o que permite alguém contestar um bloco com precisão seis meses depois.

**Alternância de fundo.** `section` normal → `section.alt` → normal. Blocos de ponte e reoferta usam `section.dark`. Nunca dois `.alt` seguidos: o olho perde o corte entre blocos.

**Numeração de imagem.** Toda imagem é um `.slot` numerado sequencialmente na página inteira — FOTO 01, FOTO 02, FOTO 03. Quem for produzir precisa de uma lista sem buraco e sem número repetido.

---

## Slot de imagem e nota de produção

O slot descreve **o que a imagem precisa mostrar**, não "imagem aqui". Quem produz tem que conseguir executar sem perguntar nada.

```html
<div class="slot mt40" style="min-height:300px">
  <b>FOTO 02</b>ANIMAÇÃO / VÍDEO CURTO — o elemento mais importante da página.<br>
  Tela de celular: [o que entra] → [o que acontece] em segundos.<br>
  Se não tiver vídeo, usar mockup estático.
</div>
```

A nota de produção é para o que **você não pode inventar** e precisa vir do cliente:

```html
<p class="nota mt24">Preciso dos 3 prints reais com nome e cidade. Sem isso este bloco não convence — é o que mais pesa na página.</p>
```

Nunca use `.nota` para copy. Ela é conversa com o cliente, não com o leitor.

---

## Hero / Gancho

Pré-headline em pergunta (a dor verbatim) → H1 com promessa + mecanismo + tempo → selo → imagem → CTA + preço.

```html
<section class="center">
  <div class="wrap">
    <div class="slot" style="min-height:90px;max-width:300px;margin:0 auto 34px"><b>FOTO 01</b>LOGOMARCA — fundo claro</div>
    <h2 style="font-size:clamp(21px,3vw,30px);color:var(--ink-soft)">[pergunta que é a dor dele, verbatim]</h2>
    <h1 class="mt24">[promessa] <span class="hl">[o que muda]</span></h1>
    <p class="lead mt24">[mecanismo em 1 frase] <b>[prazo/velocidade]</b>.</p>
    <div class="mt32"><span class="selo-check">✓ [micro-promessa de primeiro resultado]</span></div>
    <div class="slot mt40" style="min-height:300px"><b>FOTO 02</b>[briefing]</div>
    <div class="mt40"><a class="cta" href="#oferta">[CTA na voz do leitor, 1ª pessoa]</a></div>
    <p class="cta-sub">[preço] · [garantia] · [reversão de risco]</p>
  </div>
</section>
```

O CTA vai em primeira pessoa ("QUERO MEU…"), não no imperativo ("COMPRE AGORA"). É a fala dele, não a sua ordem.

---

## S5 → Balões

Fala interna literal, em itálico, entre aspas. **Grid de 2 colunas, 4 a 6 itens.** Menos que 4 não cria o efeito de reconhecimento; mais que 6 vira lista.

Puxe verbatim do banco. Frase inventada aqui é o erro mais visível de copy sem pesquisa — o leitor sente que não é ele falando.

```html
<h3 class="mt56">[frase que enquadra: "toda vez que aparece um problema, você pensa:"]</h3>
<div class="grid g2 mt24">
  <div class="balao">"[fala interna verbatim]"</div>
  <div class="balao">"[fala interna verbatim]"</div>
</div>
```

---

## S3 → Cards de sintoma

Itens curtos, concretos, observáveis. Sem emoção — a emoção é S4.1 e entra no parágrafo em volta, não no card. 4 a 6 itens.

```html
<div class="grid g2 mt40">
  <div class="sintoma"><span>✕</span> [sintoma que ele vê]</div>
</div>
```

---

## S8 → Erros / COMPARATIVO / Tabela de diagnóstico

Três formatos para o mesmo trabalho: transferir a culpa do leitor para o vilão. Escolha pela natureza do vilão.

**Erros** — quando o vilão é uma prática difundida:

```html
<div class="grid g3 mt40">
  <div class="erro"><span>✕</span> [o que quase todo mundo faz e não funciona]</div>
</div>
<p class="lead mt40 center">[parágrafo que nomeia a causa real e tira a culpa dele]</p>
```

**COMPARATIVO** — quando existe uma alternativa concreta que ele já usa (pesquisar no Google, o método antigo, o concorrente genérico). 5 a 6 linhas de cada lado, **pareadas**: a linha 3 da esquerda responde à linha 3 da direita.

```html
<div class="vs mt40">
  <div class="vs-col vs-a">
    <h3>[o jeito atual]</h3>
    <ul><li><b>✕</b> [custo real]</li></ul>
  </div>
  <div class="vs-mid">VS</div>
  <div class="vs-col vs-b">
    <h3>[o jeito novo]</h3>
    <ul><li><b>✓</b> [o mesmo eixo, resolvido]</li></ul>
  </div>
</div>
```

**Tabela de diagnóstico** — o formato mais forte quando a S3 é rica: cruza o que ele vê, o que ele faz errado e a causa real. 4 linhas.

```html
<div class="diag mt40">
  <div class="diag-row head"><div>O que você vê</div><div>O que quase todo mundo faz</div><div>O que pode ser de verdade</div></div>
  <div class="diag-row"><div class="s">[sintoma S3]</div><div class="e">[erro S8]</div><div class="c">[causa S2]</div></div>
</div>
```

---

## S6 → Antes × Depois e Duas escolhas

Mesmo material, momentos diferentes da página. **Antes × Depois** vai no topo (mostra que a transformação existe). **Duas escolhas** vai depois da oferta (força a decisão) e sempre leva CTA embaixo.

```html
<div class="grid g2 mt40">
  <div class="ad ad-antes"><div class="ad-head">Antes</div><ul class="ad-body"><li>[estado atual]</li></ul></div>
  <div class="ad ad-depois"><div class="ad-head">Depois</div><ul class="ad-body"><li>[mesmo eixo, resolvido]</li></ul></div>
</div>
```

```html
<div class="grid g2 mt40">
  <div class="esc esc-1"><div class="rot">Opção 1</div><h3>[continuar como está]</h3><span class="ic">👉</span><p>[o custo, concreto]</p></div>
  <div class="esc esc-2"><div class="rot">Opção 2</div><h3>[agir]</h3><span class="ic">✅</span><p>[o resultado, concreto]</p></div>
</div>
<h3 class="mt40 center">[frase que fecha a escolha]</h3>
<div class="mt32 center"><a class="cta" href="#oferta">[CTA]</a></div>
```

As linhas das duas colunas são **pareadas pelo mesmo eixo**. Se a esquerda fala de dinheiro e a direita de tempo, o contraste não fecha.

---

## S4.2 → Promessas e cards de benefício

**Promessas**: 4 itens numerados, verbo no infinitivo, grid 2×2. Cada promessa é uma dor invertida — se você não consegue apontar a dor de origem, a promessa é genérica.

```html
<div class="grid g2 mt40">
  <div class="promessa"><div class="n">01</div><h3>[verbo no infinitivo + objeto]</h3><p class="lead" style="font-size:16px">[como, em 1 frase]</p></div>
</div>
```

**Cards de benefício**: 6 itens, grid 3×2, quando os desejos são muitos e paralelos. Se der pra cobrir em 4, prefira promessas — tem mais peso.

```html
<div class="grid g3 mt40">
  <div class="card"><h3>[benefício em 2-3 palavras]</h3><p>[o que ele passa a conseguir, concreto]</p></div>
</div>
```

---

## Sistema nomeado do mecanismo (N elementos)

Quando o mecanismo único do cliente tem um **sistema com nome e N partes** — "os 4 Sinais", "as 3 Chaves", "o Método XYZ em 5 etapas" — isso é o ativo mais forte que o produto tem, e não cabe nos 3 pilares. Dê bloco próprio, com o nome do sistema no H2. Usa `.promessa` para 4 elementos (grid 2×2) ou `.pilar` para 3 e 5+ (grid 3).

```html
<h2 class="center">[Nome do sistema]</h2>
<p class="lead center mt16">[o que o sistema resolve, em 1 frase]</p>
<div class="grid g2 mt40">
  <div class="promessa"><div class="n">SINAL 01</div><h3>[nome do elemento]</h3><p class="lead" style="font-size:16px">[o que ele indica e o que fazer]</p></div>
</div>
```

O rótulo em `.n` acompanha o nome do sistema (SINAL 01, CHAVE 01, ETAPA 01) — é ele que faz o conjunto parecer método e não lista. Não empurre o sistema para dentro de um entregável: ele é o motivo de o produto ser diferente, e escondido ali vira bullet.

---

## S2 → Pilares / mecanismo

3 pilares. Cada um resolve um problema estrutural distinto — se dois pilares resolvem o mesmo, você tem dois pilares a menos do que pensa.

```html
<div class="eyebrow center">Apresentando</div>
<h2 class="mt16 center">[nome do produto]</h2>
<p class="lead mt16 center">[definição em 1 linha]</p>
<div class="grid g3 mt40">
  <div class="pilar"><div class="num">PILAR 01</div><h3>[nome]</h3><p>[o que faz + qual problema mata]</p></div>
</div>
```

---

## Entregáveis e bônus

Zigue-zague: texto e mockup alternando lado. 3 entregáveis, 3 bônus. Alterne `.zig` e `.zig.rev`.

```html
<div class="zig mt40">
  <div class="zig-txt">
    <span class="tag">Entregável 01</span>
    <h3 class="mt16">[nome]</h3>
    <p class="lead mt16">[o que é + a cena de uso concreta, na linguagem da S7.1]</p>
  </div>
  <div class="slot"><b>FOTO 08</b>[briefing]</div>
</div>
```

Bônus usa `<span class="tag bonus">`. Bônus são desejos **secundários** (S4.2 latente + S7.3) — o que ele quer mas não pagaria sozinho para ter. Bônus que resolve a dor principal deveria ser entregável.

---

## S11 → Para quem é

Checklist de 6 linhas + foto da persona ao lado. Cada linha fala com **uma subpersona diferente** — é isso que faz o leitor achar a linha dele.

```html
<div class="wrap grid g2" style="align-items:center;gap:40px">
  <div>
    <h2 style="text-align:left">[Produto] é para você que:</h2>
    <ul class="check mt32"><li><b>✓</b> [situação concreta de uma subpersona]</li></ul>
  </div>
  <div class="slot" style="min-height:420px"><b>FOTO 14</b>FOTO DA PERSONA — [idade, gênero, cenário da S1]. Luz natural, cenário real.</div>
</div>
```

A última linha costuma ser um desarme de S9.2: "não quer virar especialista, só quer [resultado]".

---

## S9.1 → Stack de valor

Ancoragem. Todo item listado precisa **já ter aparecido na página** — item que estreia dentro da tabela de preço não ancora nada, porque o leitor não sabe o que é.

```html
<div class="recap mt40">
  <ul>
    <li><span>[entregável já apresentado]</span><s>R$ [valor]</s></li>
  </ul>
  <div class="total"><div class="rot">Tudo isso deveria custar:</div><div class="val">R$ [soma]</div></div>
</div>
```

Valor cheio de cada item é decisão do cliente, não sua. Coloque a estimativa e uma `.nota` pedindo confirmação.

---

## S7.5 → Caixa de oferta

Na prática o stack e a caixa de preço vivem no **mesmo bloco**, ligados por uma frase-ponte. É a ponte que faz a ancoragem virar oferta — sem ela o leitor vê dois números soltos:

```html
<div class="recap mt40">…</div>

<p class="lead center mt32">[frase-ponte: reancora no custo real que ele já paga hoje.
Ex.: "só em muda reposta no último ano você já gastou mais que isso" — melhor que
"mas hoje sai por", que não ancora em nada]</p>

<div class="grid g2 mt32" style="align-items:center">
  <div class="slot" style="min-height:320px"><b>FOTO NN</b>IMAGEM "TUDÃO" — todos os entregáveis juntos.</div>
  <div class="oferta-box">…</div>
</div>
```

Atenção à classe: a caixa de oferta usa `.eyebrow` para o nome do produto. Páginas antigas usam `.logo`, que **não existe** no CSS da base — se você copiar de uma referência, troque, senão o elemento aparece sem estilo (e o validador acusa).

```html
<div class="oferta-box">
  <div class="eyebrow">[nome do produto]</div>
  <div class="de mt16">de <s>R$ [ancorado]</s> por</div>
  <div class="val">R$ [preço]</div>
  <div class="mes">[recorrência] · [reversão de risco]</div>
  <div class="mt24"><a class="cta" href="[CHECKOUT]" style="width:100%">[CTA]</a></div>
  <div class="selos"><span>🔒 COMPRA SEGURA</span><span>✓ [N] DIAS DE GARANTIA</span><span>🛡 DADOS PROTEGIDOS</span></div>
</div>
```

O `href` do checkout é `[CHECKOUT]` até o cliente mandar o link, e isso vira `.nota`. Nunca deixe `href="#"` silencioso — vira botão morto publicado.

---

## S10 → Prova social, autoridade, garantia, passos, FAQ

Cinco blocos para as sete camadas. Cada um mata uma objeção específica.

**Prova social** (10.4 método, 10.5 autoconfiança) — vai cedo, bloco 02. 3 depoimentos, cada um de uma subpersona diferente.

```html
<div class="grid g3 mt40">
  <div class="slot"><b>FOTO 03</b>DEPOIMENTO 1<br>[o que a imagem mostra] + print.<br>Tarja com nome e cidade.</div>
</div>
<p class="nota mt24">Preciso dos prints reais com nome e cidade.</p>
```

**Autoridade** (10.3) — foto real + bio + **um número**. Sem número, o bloco não sustenta.

**Garantia** (10.1, 10.5) — prazo que a S7.5 diz ser o mínimo que ele exige.

```html
<div class="gar">
  <div class="selo-g">[N]<br>DIAS</div>
  <div><h3>Garantia incondicional de [N] dias</h3><p class="lead mt16">[o que ele pode testar] [como pede o reembolso]. Sem burocracia.</p></div>
</div>
```

**Como recebe** (10.2 tempo, 10.6 prioridade) — 3 passos. Cada passo é uma ação dele, não uma etapa sua: "acesse seu e-mail" e não "enviamos o acesso". O passo 3 é sempre o primeiro uso real do produto, porque é ele que faz a compra parecer curta.

```html
<div class="grid g3 mt40">
  <div class="passo"><div class="n">1</div><h3 style="font-size:19px">[ação dele]</h3><p>[o que acontece]</p></div>
</div>
```

**FAQ** — 6 a 8 accordions, o primeiro `open`. Cada pergunta é uma objeção verbatim da 10.a, não uma pergunta que você inventou.

```html
<details open><summary>[pergunta na voz dele]</summary><p>[resposta direta, sem rodeio]</p></details>
```

**A camada 10.7 (stakeholder)** raramente ganha bloco e quase sempre deveria: é o "vou conversar em casa" que não volta. Se a persona profunda mostra stakeholder relevante, dê a ele o argumento pronto — no FAQ ou num parágrafo do fechamento.

---

## S4.3 → Ponte e reoferta

**Ponte** vem depois da agitação e antes da apresentação do produto. Fundo escuro, custo da inação, depois "mas e se…" e uma pergunta retórica.

```html
<section class="dark center">
  <div class="narrow">
    <div class="slot" style="min-height:100px;max-width:110px;margin:0 auto 26px"><b>FOTO 07</b>ÍCONE DE ALERTA</div>
    <h2>[o que acontece se nada mudar — concreto, temporal]</h2>
    <p class="lead mt32">Mas e se [cenário novo] <b style="color:#fff">[em quanto tempo]</b>?</p>
    <h3 class="mt32">[pergunta retórica que ele responde sozinho]</h3>
  </div>
</section>
```

**Reoferta** repete a caixa de preço em fundo escuro, perto do fim.

---

## S9.2 → Rodapé e desarmes

O rodapé carrega o que evita rejeição e reprovação de anúncio: desvinculação de plataforma, limite do que o produto faz, ressalva de resultado, razão social e CNPJ.

```html
<footer>
  <div class="slot" style="min-height:80px;max-width:260px;margin:0 auto 24px;background:#123725;border-color:#2A5B42"><b>FOTO 17</b>LOGOMARCA — fundo escuro</div>
  <p>Alguma dúvida? Escreva para <a href="mailto:[EMAIL]">[EMAIL]</a></p>
  <p style="max-width:760px;margin:20px auto 0;font-size:12px">
    Este site não é afiliado ao Facebook, ao Instagram ou ao WhatsApp. [limite do que o produto é e não é]. [ressalva de resultado].
  </p>
  <p style="margin-top:18px">[Razão social] · CNPJ [XX] · Termos de uso · Política de privacidade</p>
</footer>
```

Desarmes de S9.2 também entram no corpo: "você não precisa virar especialista", "sem termo técnico", "ninguém julga". Eles não vendem — eles impedem a saída.

**Slot e nota dentro do rodapé.** O rodapé é a única área em fundo escuro fora das seções `.dark`, e os componentes claros não foram feitos pra ele. Um `.slot` ali precisa de override inline (`style="background:#123725;border-color:#2A5B42"`) — vale para qualquer slot que você coloque sobre fundo escuro. Já a `.nota` vermelha fica ilegível sobre escuro: concentre as notas de rodapé (CNPJ, razão social, e-mail de suporte, termos) numa única `.nota` no fim do último `<section>`, antes do `<footer>`.
