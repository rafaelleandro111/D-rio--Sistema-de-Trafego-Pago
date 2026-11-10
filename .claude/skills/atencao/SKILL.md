---
name: atencao
description: Atenção e clique do Rafael — faz o anúncio parar o dedo, segurar a pessoa e gerar clique (CTR) no nicho da oferta. Antes de rodar - cria e dá nota pra ganchos com base nos anúncios que escalam no nicho. Depois de rodar - lê os números (taxa de gancho, retenção, CTR, conversão) e diz em qual dos 4 degraus o anúncio está falhando e o que trocar. Use quando o Rafael falar em "gancho", "chamar atenção", "CTR baixo", "ninguém clica", "ninguém assiste", "o anúncio não para o dedo", "retenção", "hook", "como prender a pessoa", ou /atencao.
---

# /atencao — Parar o dedo, segurar, fazer clicar

O Rafael é leigo: explicar simples. Números de referência e fontes em
`references/numeros.md`. Antes de tudo, ler `_memoria/aprendizados.md`
(ganchos e formatos que já funcionaram pra ele valem mais que a teoria).

## Os 4 degraus

| Degrau | Métrica | Se falhar, o problema é… | O que trocar |
|---|---|---|---|
| 1. **Parar o dedo** | Taxa de gancho (3 s ÷ impressões) | Os 3 primeiros segundos | Só o começo do vídeo (manter o resto) |
| 2. **Segurar** | Retenção (15 s ou ThruPlay ÷ 3 s) | O meio não cumpre o que o gancho prometeu, ou o ritmo cai | Corpo do vídeo: mais rápido, entregar a promessa logo |
| 3. **Clicar** | CTR (link) | Falta motivo pra clicar: promessa fraca, sem curiosidade, chamada pra ação ruim | Final do vídeo, texto do anúncio, título |
| 4. **Comprar** | Vendas ÷ cliques | Página ou oferta — **não é o anúncio** | Página ponte, ou trocar de oferta (`validar-oferta`) |

Regra de ouro: **arrumar o primeiro degrau que falha**, de cima pra baixo.
Trocar o gancho de um vídeo cujo problema é a página só queima dinheiro.

## Modo 1 — Antes de rodar: criar ganchos

1. **Material do nicho:** ler os anúncios que escalam no espião
   (`marketing/espiao/<palavra>-<data>/anuncios.json`, ordenados por escala;
   olhar as capas em `imagens/`) e a Persona Profunda se existir
   (`infoproduto/alicerce-do-copy/persona-profunda/`). Anotar as **frases
   literais** do público e os ganchos que se repetem nos anúncios mais escalados.
2. **Criar 10 ganchos**, misturando os tipos:

| Tipo | Exemplo (pilates em casa) |
|---|---|
| Situação reconhecível | "Eu também achava que precisava de academia pra ter resultado…" |
| Pergunta sobre o problema (sem acusar a pessoa) | "Por que tanta gente desiste do exercício na segunda semana?" |
| Número concreto | "15 minutos, uma parede, nenhum aparelho." |
| Quebra de crença | "Fazer abdominal todo dia não é o que mais ajuda a barriga." |
| Curiosidade | "O exercício que fisioterapeutas fazem e quase ninguém conhece" |
| Cena estranha / visual inesperado | Primeira imagem: pessoa "andando" na parede |
| POV / identificação | "POV: você tem 20 minutos livres e nenhuma vontade de sair de casa" |
| Notícia / descoberta | "Virou moda no Brasil: o treino na parede" |

3. **Dar nota de 0 a 10** a cada gancho:
   - [ ] Para o dedo em até 3 s (no TikTok, 1–2 s)? Ação/rosto/imagem logo no 1º quadro, sem logo no começo
   - [ ] Usa palavras do nicho (as frases literais do passo 1)?
   - [ ] É específico (número, cena, situação) e não genérico?
   - [ ] Cria vontade de ver o resto (curiosidade ou promessa)?
   - [ ] Combina com a página do produtor (mesma promessa — método Ladeira)?
   - [ ] Parece conteúdo, não propaganda (principalmente TikTok e Reels)?
   - [ ] **Passa no `anti-bloqueio`**? Gancho que ataca a pessoa ("você está gorda?") → nota 0
4. Entregar os **5 melhores** com a nota e o porquê em 1 linha. Pra virar
   roteiro completo: skill `escrever-criativos-low-ticket` ou agente `copywriter`.

**Google Ads:** o "gancho" é o título. Repetir a palavra que a pessoa
pesquisou no 1º título, depois benefício específico, depois prova/garantia.

## Modo 2 — Depois de rodar: diagnosticar

1. Pedir **uma coisa só**: print ou relatório do Gerenciador por anúncio com
   impressões, reproduções de 3 s, ThruPlays (ou 15 s), cliques no link, CTR
   (link), gasto — mais as vendas da Hotmart/Kiwify. Esperar ~1.000
   impressões por anúncio antes de julgar.
2. Calcular as 4 métricas (fórmulas em `references/numeros.md`) e comparar
   com as faixas da plataforma — e com o histórico do Rafael, se houver.
3. Achar **o primeiro degrau fraco** e dizer o que trocar (tabela dos 4 degraus).
4. Se o gancho for o problema: gerar 3 ganchos novos (Modo 1) pra testar
   **no mesmo vídeo**, trocando só os primeiros segundos.

## Entrega

```
Anúncio X — falha no degrau N (nome)
  Gancho: 18% (fraco; bom é 25%+)   Retenção: 9%   CTR: 0,6%   Conversão: —
  O problema: ...
  Trocar: ...
```

Salvar em `saidas/atencao/<oferta>-<data>.md`.

## Aprender

Quando um gancho/formato for bem (gancho ≥ 30% e CTR acima da faixa "bom"),
anotar em `_memoria/aprendizados.md` → "Ângulos e formatos de criativo que
funcionam" (nicho + tipo de gancho + números). Depois de alguns testes, as
faixas de "bom" passam a ser as do Rafael, não as do mercado.
