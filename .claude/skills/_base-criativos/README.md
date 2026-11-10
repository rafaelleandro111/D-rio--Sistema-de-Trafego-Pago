# Base compartilhada — criativos

Não é uma skill: é o material comum que as skills de escrever criativo (anúncio em vídeo) leem.
Tudo aqui é referenciado a partir da raiz do Info OS, em `.claude/skills/_base-criativos/`.

| Arquivo | O que é |
|---|---|
| `PROCESSO.md` | as 5 etapas (mercado e formato → pessoas → ganchos → roteiros → portão), as paradas e o arquivo do pack |
| `REGRAS-ESCRITA.md` | a régua de toda fala + a medição em código |
| `MODELO-ENTREGA.md` | como o pack fica escrito (o `.md` é a entrega; o Google Drive é opcional) |
| `ANGULOS.md` | os 17 ângulos (portas de entrada do argumento) |
| `NOMENCLATURA.md` | o nome de cada criativo — `[OFERTA]_Pack[N]_[FORMATO]_[NUM]` |
| `formatos/` | catálogo dos 50 formatos (README = índice) |
| `scripts/medir_falas.py` | mede as falas do pack contra a régua (Python 3, sem instalar nada) |

**Onde o trabalho fica salvo** (no projeto do aluno, não aqui):

```
infoproduto/criativos/
├── nomenclatura.md                 código da oferta + último número de criativo usado
├── biblioteca-anuncios/<anunciante>/   anúncios dos concorrentes (skill /biblioteca-anuncios-meta)
└── packs/pack-NN-<produto>.md      um arquivo por pack, que cresce etapa a etapa
```

**Skills que usam esta base** — cada uma só com as regras do seu tipo de venda:

| Skill | Tipo de venda | Status |
|---|---|---|
| `escrever-criativos-ultra-low-ticket` | anúncio → página → checkout, produto até R$ 10 | disponível |
| `escrever-criativos-low-ticket` | anúncio → página → checkout, acima de R$ 10 — o anúncio não mostra produto nem preço, convida pra ver o material | disponível |
| `escrever-criativos-vsl` | anúncio → aula ou vídeo de vendas gratuito — zero produto e preço, CTA pra aula | disponível |
| `escrever-criativos-lancamento` | lançamento | em breve |

Mudou o processo, a régua, o modelo ou um formato → muda aqui, e vale pra todas.
A leitura do mercado vem da skill `/biblioteca-anuncios-meta`; a das pessoas, do Alicerce do Copy
(`/alicerce-copy`).
