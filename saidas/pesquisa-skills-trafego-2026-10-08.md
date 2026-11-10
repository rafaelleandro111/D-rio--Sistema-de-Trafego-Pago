# Pesquisa — skills e ferramentas pro agente de tráfego pago

Data: 08/10/2026. Nada foi instalado ainda.

## Mapa: o que existe pronto x o que vamos construir

| Função | Existe pronto? | Melhor opção encontrada | Custo |
|---|---|---|---|
| Copy, criativo de anúncio, oferta, conversão | Sim | coreyhaines31/marketingskills (skills `ads`, `ad-creative`, `copywriting`, `offers`, `cro`, `marketing-psychology`, `video`, `image`) | Grátis |
| Espião de anúncios (Biblioteca do Meta) | Sim, via robô | Apify (robôs "Facebook Ad Library Scraper") + Apify MCP | ~US$ 0,75–3 por 1.000 anúncios |
| Gerar imagens | Sim | claude-image-gen (Gemini/OpenAI) ou fal-mcp-server | Paga por imagem (API) |
| Editar vídeo | Sim, mas técnico | skill `video-editing` (everything-claude-code) — FFmpeg + Remotion | Grátis (ferramentas), APIs opcionais pagas |
| Conectar Meta Ads (tua conta) | Sim, oficial | Meta Ads MCP oficial (mcp.facebook.com/ads, beta) | Grátis |
| Conectar Google Ads (tua conta) | Sim | MCP oficial do Google (só leitura) ou cohnen/mcp-google-ads | Grátis |
| Hotmart (tua conta: vendas, comissões) | Sim | MCP Hotmart / thaleslaray/hotmart-mcp | Grátis |
| **Validar oferta + nota em %** | **Não existe** | Construir sob medida | — |
| **Alerta de pausa / prejuízo** | **Não existe pronto pra afiliado** | Construir sob medida (pode usar o MCP do Meta/Google como fonte) | — |
| **Modelar criativo do concorrente** | Parcial | Espião (Apify) + `ad-creative` + skill nossa de modelagem | — |

## Observações importantes

- A API oficial gratuita da Biblioteca de Anúncios do Meta só entrega anúncios comerciais veiculados na União Europeia (e anúncios políticos). Pra anúncios do Brasil, o caminho é o robô (Apify) ou olhar manualmente na Biblioteca.
- Hotmart/Kiwify não mostram vendas de produtos de terceiros. A validação vai cruzar: temperatura, Blueprint (>80%), satisfação (>4.0), comissão, volume e tempo de anúncios ativos, Google Trends.
- Skills de terceiros são texto com instruções pro Claude — ler antes de instalar. A maioria é em inglês e voltada a SaaS americano; vão precisar de adaptação pro mercado de afiliado brasileiro.

## Fontes

- https://github.com/coreyhaines31/marketingskills
- https://github.com/OpenClaudia/openclaudia-skills
- https://github.com/zubair-trabzada/ai-marketing-claude
- https://www.markifact.com/meta-ads-library-mcp
- https://apify.com/top_mythos/ad-library-scraper
- https://apify.com/happitap/facebook-ads-scraper
- https://github.com/guinacio/claude-image-gen
- https://github.com/raveenb/fal-mcp-server
- https://awesomeskill.ai/skill/affaan-m-ecc-video-editing
- https://ferrerponseti.com/en/blog/official-meta-ads-mcp-claude/
- https://mcpservers.org/servers/cohnen/mcp-google-ads
- https://github.com/thaleslaray/hotmart-mcp
- https://help.hotmart.com/en/article/48741895558541/mcp-hotmart-como-consultar-dados-e-realizar-aces-na-minha-conta-com-ia
