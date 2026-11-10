---
name: acompanhar-ofertas
description: Acompanhamento diário das ofertas que o Rafael escolher. Um robô roda sozinho todo dia às 11h (Agendador de Tarefas do Windows), confere na Biblioteca de Anúncios só as ofertas da lista dele e mostra a tendência de cada uma — escalando, subindo, estável, caindo ou morrendo. Use quando o Rafael disser "monitora essa oferta", "acompanha esse anúncio", "vigia essa oferta", "como estão as ofertas que estou acompanhando", "quais estão crescendo", "tendência", "tira da lista", ou /acompanhar-ofertas.
---

# /acompanhar-ofertas — Robô que vigia as ofertas escolhidas

O Rafael é leigo: explicar simples. O robô roda **sem o Claude** — o
Windows chama ele todo dia às 11h (tarefa "Robo Ofertas - Acompanhamento
Diario"). Se o PC estiver desligado às 11h, roda quando ligar. Custa zero
token; o Claude só entra pra ler e explicar.

## Regra principal

**Quem escolhe a oferta é o Rafael.** Nunca colocar oferta na lista sem ele
escolher. Máximo **5 ofertas** (mais que isso arrisca bloqueio do Facebook).

## Como uma oferta entra na lista

**Jeito 1 — ele manda o link** (página de vendas ou anúncio da Biblioteca):
1. Se for link da Biblioteca de Anúncios, abrir e pegar o site de destino.
2. Descobrir a **palavra de busca**: o nome do produto ou a promessa que
   aparece no texto dos anúncios (ex: "pilates na parede"). Se não der pra
   saber, perguntar a ele.
3. Adicionar (ver comandos).

**Jeito 2 — ele pede as mais quentes** ("pesquisa as ofertas mais quentes de X"):
1. Rodar o validador no modo busca (skill `validar-oferta`) — ele mostra o
   ranking das 5 mais escaladas agora (anúncios ativos, criativos novos,
   anunciantes, preço, nota).
2. Mostrar o ranking e **perguntar quais ele quer vigiar**.
3. Adicionar só as escolhidas, usando a mesma palavra da busca.

## Comandos

Todos com `PYTHONIOENCODING=utf-8` na frente:

| Pedido | Comando |
|---|---|
| Vigiar oferta | `python sistema/acompanhamento/acompanhar.py adicionar "<link>" --busca "<nome do produto ou promessa>"` (`--pais US` se for de outro país) |
| Parar de vigiar | `... remover "<site>"` |
| Ver a lista | `... lista` |
| Coletar agora (sem esperar as 11h) | `... rodar` (1 vez por dia; repetir não faz nada) |
| Ver tendências | `... relatorio` |

## Como ler a tendência

Precisa de **3 dias** de coleta (antes disso: ⏳ COLETANDO). Ideal: 5 a 7.

| Tendência | Regra | O que fazer |
|---|---|---|
| 🚀 ESCALANDO | anúncios +50% em 3 dias **e** 2+ criativos novos | Melhor momento: validar (`validar-oferta`) e modelar (`modelar-oferta`) |
| 📈 SUBINDO | anúncios +15% ou 3+ criativos novos | Boa candidata, acompanhar mais uns dias |
| ➡️ ESTÁVEL | sem grande mudança | Oferta madura: funciona, mas sem pressa |
| 📉 CAINDO | anúncios −15% | Evitar entrar agora |
| 💀 MORRENDO | sumiu ou caiu 80%+ do pico | Não entrar; sugerir tirar da lista |

"Criativos novos" = anúncios que não existiam nos dias anteriores — sinal
de que estão investindo e testando agora. A contagem soma **todos os
anunciantes** que mandam pro mesmo site (produtor + afiliados).

## Entregar ao Rafael

Rodar `relatorio`, mostrar a tabela e resumir em 1 frase por oferta. Se
alguma estiver 🚀/📈, sugerir o próximo passo (validar ou modelar). Se
estiver 💀, sugerir tirar da lista pra abrir vaga.

Arquivos: `sistema/acompanhamento/historico.json` (fotos diárias),
`log.txt` (cada rodada; olhar se der erro), relatórios em
`saidas/acompanhamento/`. Se o log mostrar 0 anúncios vários dias seguidos
numa oferta que ainda roda, a palavra de busca pode estar ruim — trocar
(remover e adicionar com outra `--busca`). Se der 0 em todas, a página do
Facebook pode ter mudado → ajustar `sistema/espiao/espiao.py`.
