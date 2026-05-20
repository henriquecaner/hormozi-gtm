---
description: Email sequence (cold, warm, nurture, re-engagement). Gera 5-7 emails sequenciais com hook + agitação + proof + CTA, timing entre touches, contextualização por touch. Tunado para B2B brasileiro — voz direta, sem superlativo, com prova específica.
argument-hint: "[--tipo=cold|warm|nurture|re-engagement] [--produto=<slug>] [--ref=<arquivo>]"
---

# /hormozi-gtm:email

Sequência de emails que faz lead frio virar lead quente, ou lead morno virar oportunidade qualificada. Não é blast — é cadência sequenciada onde cada touch tem função.

## Carregamento de persona

Use `hormozi-persona` para orquestrar. Delegate copy específico ao `ad-architect` (que escreve cada email no tom Hormozi 1ª pessoa). Pass final pelo `humanizer` modo **full** (output externo entregue a leads do cliente).

## Skills ativas

- `hook-framework` (subject + opener de cada email)
- `ad-copy-formula` (estrutura do corpo)
- `value-equation` (ancoragem nos benefícios)
- `guarantees` (email de fechamento)
- `humanizer-rules` (modo full)
- `output-conventions`

## Argumentos

| Argumento | Comportamento |
|---|---|
| (vazio) | Modo interativo: pergunta tipo de sequência + produto + ICP no chat |
| `--tipo=cold` | Cold outreach (lead nunca te ouviu falar). 5-7 emails. |
| `--tipo=warm` | Warm (lead engajou — baixou lead magnet, abriu LP). 4-5 emails. |
| `--tipo=nurture` | Nurture educacional (lead na lista há 30+ dias, sem comprar). 5-7 emails. |
| `--tipo=re-engagement` | Re-engage lead inativo (90+ dias sem abrir). 3-4 emails. |
| `--produto=<slug>` | Slug do produto/oferta (lido de gtm-context.md ou input) |
| `--ref=<arquivo>` | Refinar sequência existente (cria v2) |
| `--foco=<X>` | Em modo refinar: foca em parte específica (subject, opener, CTA, sequence flow) |

## Pré-requisitos

1. `gtm-context.md` existe → carrega ICP, oferta, brand voice, audience externa, intensidade do tom
2. Audit recente (≤30 dias)? → carrega como `audit_ref` (soft warning se ausente)
3. Para `--tipo=cold`: idealmente sample list de 5-10 prospects reais (LinkedIn, sites) — alimenta personalização

## Fluxo

### Passo 1: Detecta tipo + valida contexto

Se `--tipo` não foi passado: pergunta.
Se `gtm-context.md` está stale (>30 dias): sugere `/init --refresh`.

### Passo 2: Carrega briefing de oferta

Se houver `audit_ref` válido, lê briefing do `offer-architect`. Senão, lê oferta direto do `gtm-context.md` ou pede 3 inputs mínimos:
- Qual a transformação que a oferta entrega?
- Quem é o ICP?
- Qual a objeção principal que aparece em sales calls?

### Passo 3: Define estrutura por tipo

**Cold (5-7 emails):**
- Email 1: Hook + observação específica do prospect (research). CTA leve (PDF, link, micro-pergunta).
- Email 2 (+3 dias): Proof point específico — case study com nomes + números.
- Email 3 (+5 dias): Reframe da objeção comum ("a maioria pensa que X, mas é Y").
- Email 4 (+7 dias): Conteúdo de valor sem ask (linka conteúdo educacional próprio).
- Email 5 (+14 dias): Última tentativa com escassez genuína (vaga, cohort, prazo real).
- Email 6 (+21 dias, opcional): Breakup email — "fechando o follow-up, mas se mudar de ideia...". Frequentemente o que mais converte.
- Email 7 (+45 dias, opcional): Re-attempt 6 semanas depois — sequence nova, ângulo diferente.

**Warm (4-5 emails):**
- Email 1: Reconhece o engajamento ("vi que baixou X"), aprofunda dor específica.
- Email 2 (+2 dias): Demonstração de como o produto resolve a dor — 1 sentença + 1 case curto.
- Email 3 (+4 dias): Convida pra próxima etapa (demo, call de 15min, trial).
- Email 4 (+7 dias): Reframe + urgência se aplicável.
- Email 5 (+14 dias): Breakup.

**Nurture (5-7 emails, mais espaçados):**
- Email 1 a 5 (1 por semana): Cada um ensina 1 framework / mostra 1 case / responde 1 pergunta. Sem CTA de venda explícito até email 5.
- Email 6 (semana 6): Soft pitch da oferta com contexto do que aprendeu nas semanas anteriores.
- Email 7 (semana 8): Hard ask com escassez genuína.

**Re-engagement (3-4 emails):**
- Email 1: Honesto — "vi que você não abre meus emails há 90 dias. Posso te tirar da lista, ou você quer continuar?". Pergunta direta.
- Email 2 (+5 dias se ele clicou em "continuar"): Reapresentação do que mudou desde a última vez.
- Email 3 (+7 dias): Oferta especial de re-engagement (não desconto genérico — algo verdadeiramente novo).
- Email 4 (+14 dias): Última call.

### Passo 4: Construção dos emails

Delegate ao `ad-architect` com briefing estruturado de cada email (subject, hook, corpo, CTA). Ele devolve a sequência completa.

### Passo 5: Humanizer pass (full)

Pass full obrigatório. Sequence vai pra lead do cliente — voz precisa estar limpa.

### Passo 6: Métricas e teste sugerido

Inclui no output:
- Métrica primária a tracking (reply rate / open rate / click-to-call)
- Sample size mínimo (10-15 contatos por tipo pra ter sinal)
- Critério de iteração (se reply rate < 3%, troca subject; se < 1%, troca hook + opener)

### Passo 7: Salva

`outputs/email/email-{tipo}-{produto_slug}-{YYYYMMDD}-v{n}.md` via template `email-sequence.md`.

### Passo 8: Preview na conversa

```
✅ Salvo em: outputs/email/email-cold-{slug}-20260520-v1.md
📋 Preview:
   • Sequência: cold, 7 emails, span de 45 dias
   • Subject email 1: "{{X}}"
   • CTA primário (cada email): "{{Y}}"
   • Status humanizer: ✓ full pass

👉 Próximos passos:
   1. Testar em 10-15 contatos primeiro
   2. Medir reply rate em 14 dias
   3. Se < 3%, rode /hormozi-gtm:review --ref=outputs/email/...
```

## Critério de pronto

- [ ] Cada email tem subject específico (não genérico)
- [ ] Hook do email 1 passa tweet test (lê isoladamente)
- [ ] Cada email tem 1 CTA único e específico
- [ ] Sequência tem timing definido entre emails
- [ ] Breakup email incluído (se aplicável)
- [ ] Humanizer full aplicado
- [ ] Métrica primária e critério de iteração documentados

## Anti-padrões

- Email "vamos conversar?" sem proposta específica
- Todos os emails terminam em "marque uma call" (cliente sai do ritmo)
- Subject genérico ("Oportunidade") ou clickbait ("Aberto?")
- Copy idêntico em todos os touches (cliente nota)
- Personalização fake ("Olá [nome], adorei seu post sobre [tópico aleatório]")
- Falta de breakup email (deixa lead morno indefinidamente)
- Sequência sem métrica clara de sucesso/iteração
