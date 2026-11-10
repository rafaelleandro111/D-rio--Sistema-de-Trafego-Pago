---
name: espiao
description: Espião de anúncios do Rafael. Busca uma palavra-chave na Biblioteca de Anúncios da Meta (Facebook/Instagram, Brasil), coleta os anúncios ativos, ordena pelos mais escalados (mais cópias rodando), marca os que levam pra Hotmart/Kiwify/Eduzz etc. e analisa os padrões que funcionam. Use quando o Rafael disser "espiona", "espião", "busca anúncios de X", "quais anúncios de X estão rodando", "acha anúncio que está dando certo", ou /espiao.
---

# /espiao — Espião de anúncios

O Rafael é leigo: explicar o resultado de forma simples, curta, sem jargão.

## 1. Coletar

Rodar o coletor com a palavra-chave pedida (perguntar se não veio):

```bash
PYTHONIOENCODING=utf-8 python sistema/espiao/espiao.py "<palavra>" --max 100
```

- `--max` padrão 100. Mais anúncios = mais demorado (~1 min a cada 50)
- Saída em `marketing/espiao/<palavra>-<data>/`: `relatorio.html`, `anuncios.csv`, `anuncios.json`, `imagens/`
- Se der "Nenhum anúncio encontrado", a página do Facebook pode ter mudado: avisar o Rafael e ajustar `JS_CARDS` / `interpretar()` no script

## 2. Analisar

Ler `anuncios.json` e, pros ~10 primeiros (mais escalados), olhar as capas em `imagens/`. Analisar:

- **Ganchos:** como os anúncios começam (pergunta, dor, promessa, prova)
- **Dores e promessas** que mais se repetem
- **Formatos:** vídeo / imagem / carrossel
- **Sinais de que dá lucro:** várias cópias rodando (`variacoes`), criativos novos subindo, vários anunciantes na mesma oferta. Tempo no ar sozinho não prova nada; 7+ dias só mostra que passou do teste
- **Oportunidade de afiliado:** anúncios com `plataforma_afiliado` preenchido — listar produto, plataforma e link de destino, e sugerir ao Rafael procurar esse produto na vitrine de afiliados

Lembrar: nicho de saúde/estética/dinheiro tem regras mais rígidas no Facebook — sinalizar promessas que seriam barradas.

## 3. Entregar

Salvar `analise.md` na mesma pasta e responder ao Rafael com:
1. Top 5 anúncios mais escalados (cópias + dias + anunciante + o que faz)
2. 3 padrões que se repetem
3. Produtos de afiliado encontrados (se houver)
4. Um modelo de anúncio pra ele usar como base (sem copiar)
5. Caminho do `relatorio.html` pra ele abrir no navegador

Usar com moderação (algumas buscas por dia), pra não ser bloqueado pelo Facebook.
