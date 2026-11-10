# Regras de escrita — a régua de toda fala

Valem pra gancho (a primeira frase do vídeo, os 3 primeiros segundos) e roteiro, em qualquer tipo
de venda. Vieram da prática de escrever anúncio em vídeo e são a régua de qualidade de toda fala.

1. **A linha é uma fala natural completa: 10 a 15 palavras típicas.** Quebra só na mudança de
   ideia. Linhas de até 3 palavras: no máximo ~12% do texto e SÓ como placa ("Por isso…"),
   congelamento ("Simples assim."), confirmação de diálogo ("Não vai.") ou pergunta curta.
   **Nenhuma linha acima de 28 palavras.**
2. **Proibido fragmento-eco** ("Um perfil. Um perfil que…" — a informação entra inteira) e
   **proibido trailer vazio** ("e é aqui que fica interessante…" — a ponte é causal, nunca
   anúncio de importância).
3. **Partitura de locução:** o texto será FALADO. Reticências nas pontes, número como clímax no
   FIM da linha, CAPS cirúrgico em UMA palavra de carga, marcas orais com propósito ("tá?",
   "né?", "Pera…"). Teste final: ler em voz alta — linha que faz tropeçar é reescrita.
4. **Vocabulário do espectador:** as palavras de carga vêm da fala real do público (S7.1 da
   Persona Profunda e o banco de frases, em `infoproduto/alicerce-do-copy/persona-profunda/`) e da
   fala dos anúncios do nicho (`infoproduto/criativos/biblioteca-anuncios/`). Termo que o público não fala → troque
   pelo sinônimo que ele fala. Nome de atração e mecanismo são isentos.
5. **Ignorância presumida:** o espectador não sabe do que você vai falar. O gancho promete sem
   explicar o mecanismo; o nome de atração é dito sem ser definido no gancho; a explicação vive
   no corpo. Vazar a explicação na abertura queima a curiosidade.
6. **O beneficiário é sempre a PESSOA.** O método nunca é o sujeito do benefício. "O curso te
   dá" ✗ → "VOCÊ faz" ✓.
   Sobre **quem fala**: quando é o especialista (você) falando, a fala também segue o seu
   documento de tom de voz, se existir (ver abaixo). Quando o formato põe outra pessoa falando
   (depoimento, UGC em 3ª pessoa, diálogo), aquela personagem fala com as palavras do público.
7. **Trend topic é o que é DITO no gancho**, registrado com as palavras ditas.
8. **Clonagem:** o DISPOSITIVO do concorrente vale (leilão, duelo, série, desafio); a FORMULAÇÃO
   verbatim de abertura de concorrente ativo, nunca.
9. **Números:** dinheiro sempre com unidade de tempo quando for ganho ("por mês"); número quebrado
   > redondo com cara de preço; toda conta feita na frente do espectador tem que fechar na
   calculadora. Preço falado por extenso quando for dito ("sete reais").
10. **Nada inventado sem etiqueta.** Depoimento, print de mensagem, número de alunos, "já me
    falaram pra cobrar 300" — se não é fato confirmado, vai pra nota única `[validar]`. Print
    de mensagem inventado apresentado como real é depoimento fabricado.

## Tom de voz — quando a fala é sua

Se existe `infoproduto/alicerce-do-copy/tom-de-voz/tom-de-voz-*.md` (use a versão mais alta), toda
fala dita pelo especialista passa por ele:
- **Palavras-assinatura (§2.1)** entram; **palavras-veto (§2.5)** não entram nunca.
- Aberturas e fechamentos partem da **biblioteca de frases (§14)**, adaptados.
- Cada roteiro passa pela **régua de 7 notas (§11)**: média ≥ 7,5 e nenhum eixo abaixo de 6.
  Reprovou → reescreve antes de mostrar. A nota vai no bastidor, nunca no pack.

Sem documento de tom de voz, siga só esta régua e registre no cabeçalho do pack
"tom de voz: ainda não extraído (`/tom-de-voz`)".

## Medição em código (obrigatória, peça a peça)

Rode na coluna FALA de cada roteiro antes de mostrar. Nunca estime no olho. O script mede o
pack inteiro de uma vez (Python 3, nada pra instalar), a partir da raiz do Info OS:

```bash
# Mac
python3 .claude/skills/_base-criativos/scripts/medir_falas.py infoproduto/criativos/packs/pack-NN-<produto>.md
# Windows
python .claude/skills/_base-criativos/scripts/medir_falas.py infoproduto/criativos/packs/pack-NN-<produto>.md
```

Pra medir um gancho ou uma fala solta, salve o texto (uma fala por linha) num arquivo e rode
com `--texto <arquivo>`.

**Régua:** mediana 10–15 palavras por linha · micro (até 3 palavras) ≤ ~12%, cada uma justificada
nos 4 usos da regra 1 · zero linhas acima de 28 palavras.

Reprovou → reescrever fundindo ou quebrando e medir de novo.
