# Empresa

> Memória central do negócio. O Claude lê esse arquivo antes de cada resposta.
> Você pode editar a qualquer momento.

**Nome:** Rafael (marca pessoal — ainda sem nome de marca, sem logo)
**Negócio:** Tráfego pago — afiliado (agora) e produto próprio (futuro)
**O que faz:** Quer rodar tráfego pago promovendo produtos como afiliado e, mais pra frente, um produto próprio. Está começando — se considera leigo em tráfego pago.
**Perfil:** Solopreneur
**Atende clientes:** Não. Vende pra público final via plataformas de afiliado.
**Equipe:** Sozinho, por enquanto
**Ferramentas:** Hotmart e Kiwify (contas de afiliado). Canais desejados: Google Ads, Facebook e Instagram (Meta Ads) e TikTok Ads — tudo de tráfego pago.
**Principais entregas:** Campanhas de tráfego pago pra ofertas de afiliado

## Contexto adicional

- Ainda não tem produto próprio, marca, logo nem identidade visual.
- Projeto atual: construir um **sistema de agente de IA** (conjunto de skills, possivelmente com interface em HTML/CSS/JS) que faça o trabalho de um gestor de tráfego / afiliado experiente:
  - **Buscar ofertas** (ex: "busca oferta de emagrecimento na Hotmart") ou **analisar oferta enviada** por ele
  - **Validar oferta**: se está vendendo, se já está validada no mercado, nota em % de quão boa é a oferta pra ele
  - **Buscar low tickets** e produtos que estão vendendo
  - **Espião de criativos**: analisar criativos de outros na Biblioteca de Anúncios do Meta etc. e **modelar** (adaptar a estrutura, não copiar); também criar criativos próprios
  - Funil, palavras-chave, estrutura de campanha
  - **Analisar métricas e erros**: quando pausar, quando vai dar prejuízo, conversão
- Limitação conhecida: Hotmart/Kiwify não mostram vendas públicas — validação precisa cruzar sinais indiretos (temperatura/ranking do marketplace, volume e tempo de anúncios ativos na Biblioteca de Anúncios, Google Trends, comissão).
- **Não construir o sistema sem ele pedir.** Antes, conversar mais e entender os detalhes — ele quer aprender e definir junto.
- **Já construído (out/2026):** robô espião (`sistema/espiao/`), validador de ofertas com nota em % (`sistema/validador/` + skill `validar-oferta`), `anti-bloqueio` (Meta, Google, TikTok + regras do produtor), `conselho` (Sobral, Hormozi, Brunson, Schwartz/Halbert, Ladeira) e 7 agentes em `.claude/agents/` (minerador, estrategista, copywriter, gestor, auditor-meta, auditor-google, auditor-tiktok).
