---
description: Win/loss interview + churn analysis + retention playbook. Foca em retenção (não aquisição) — onde 80% do plugin atual está focado. Para SaaS B2B com churn > 5%/mês, consultoria com renewal rate < 70%, ou negócio recorrente em platô.
argument-hint: "[--produto=<slug>] [--ref=<caminho>] [--foco=churn|winback|retention] [--no-humanize]"
---

# /hormozi-gtm:churn-prevention

Aquisição cara virou dado (CAC sempre subindo). Retenção é onde fica margem. Esta skill estrutura: por que cliente saiu, o que reverter rápido, o que mudar estruturalmente.

## Carregamento de persona

Use `hormozi-persona` para orquestrar. Delegate ao `money-model-architect` para análise de impacto financeiro (LTV, churn ratio), e ao `offer-architect` se a raiz for problema de oferta original (Probability fraca → cliente desiste cedo). Pass final pelo `humanizer` modo **lite** (output é interno para o time, não pra cliente externo).

## Skills ativas

- `leila-scaling` (5 Star Service framework — operação de retenção)
- `value-equation` (diagnostica se Probability/Effort estavam fracos)
- `money-models` (impacto financeiro do churn)
- `ltv-cac` (matemática de retenção)
- `humanizer-rules` (modo lite)
- `output-conventions`

## Argumentos

| Argumento | Comportamento |
|---|---|
| (vazio) | Modo interativo: pergunta produto + métricas de churn + acesso a clientes que saíram |
| `--produto=<slug>` | Slug do produto |
| `--ref=<caminho>` | Refinar análise existente |
| `--foco=churn` | Análise de churn passado (entender por que clientes saíram) |
| `--foco=winback` | Sequência de winback (recuperar clientes que saíram nos últimos 90 dias) |
| `--foco=retention` | Playbook preventivo (reduzir churn futuro) |
| `--no-humanize` | Pula humanizer |

## Pré-requisitos

1. `gtm-context.md` existe → carrega ICP, oferta, ticket médio
2. Dados de retenção: churn rate atual, % de clientes que saíram nos últimos 6 meses
3. Lista de clientes que saíram (idealmente com motivo declarado)
4. Para `--foco=winback`: lista de contatos ainda válidos dos clientes que saíram

## Fluxo

### Passo 1: Coleta dados de churn

Em modo interativo, pergunta:

1. **Métrica primária:** churn rate mensal atual (ou trimestral)?
2. **Tendência:** subiu/desceu nos últimos 6 meses?
3. **Comparação com cohort:** churn varia muito por época de entrada?
4. **Lifetime médio:** quantos meses cliente fica em média antes de sair?
5. **% de churn por motivo declarado:** preço / produto não entregou / time interno assumiu / mudou de fornecedor / outro?

### Passo 2: Análise por tipo de churn

Identifica padrão dominante:

**Churn precoce (< 30 dias):**
- Raiz: onboarding ruim ou expectativa quebrada na sales call.
- Fix imediato: revisar sales script + primeiros 14 dias do onboarding.

**Churn médio (30-90 dias):**
- Raiz: Value Equation falhou na entrega (Time Delay > prometido, Effort > esperado).
- Fix: rodar `/hormozi-gtm:audit` na oferta original.

**Churn tardio (>90 dias):**
- Raiz: produto entregou inicial mas falhou em sustentar valor (continuity offer fraca).
- Fix: olhar `money-models` skill — Continuity tier precisa repensar.

**Churn voluntário (cliente cancela ativamente):**
- Raiz: alternativa melhor surgiu ou orçamento mudou.
- Fix: positioning + escassez genuína para premium tier.

**Churn passivo (cliente para de usar mas não cancela):**
- Raiz: engagement caiu, valor percebido foi.
- Fix: re-engagement sequence (skill `sales-sequencing`).

### Passo 3: Win/loss interview script

Para `--foco=churn` ou `--foco=winback`:

Gera script de 6-8 perguntas para entrevistar 5-10 clientes que saíram. Pergunta-chave:

> "Olha, sem agenda de venda — só quero entender. Se você pudesse voltar 90 dias antes da decisão de cancelar, o que faria diferente OU o que eu poderia ter feito diferente?"

E mais 5-7 perguntas estruturadas pra extrair:
- Momento exato em que decidiu sair (gatilho).
- O que tentou antes de cancelar.
- O que o competidor/alternativa oferece que você não oferecia.
- O que segue valendo (não joga tudo fora).
- Se voltasse, em quais condições.

### Passo 4: Categorização de motivos

Após 5-10 interviews:

| Motivo | Quantos clientes | % | Raiz no Value Equation |
|---|---|---|---|
| Preço | {{N}} | {{X}}% | Dream Outcome ↓ ou Probability ↓ |
| Não entregou esperado | {{N}} | {{X}}% | Probability ↓ |
| Time interno assumiu | {{N}} | {{X}}% | Effort ↓ (cliente conseguiu reduzir) |
| Mudou de fornecedor | {{N}} | {{X}}% | Saturação de mercado |
| Mudança no business | {{N}} | {{X}}% | Não evitável (não tente) |

### Passo 5: Retention playbook

Para `--foco=retention`, gera playbook em 4 blocos:

**Bloco 1 — Quick wins (0-30 dias):**
3-5 ações concretas a implementar essa semana. Ex:
- Adicionar check-in semanal nos primeiros 30 dias de cliente novo.
- Survey NPS automático no dia 30 + 60 + 90.
- One-Done Guarantee em resposta de cliente (resposta em 4h úteis).

**Bloco 2 — Mudanças estruturais (30-90 dias):**
- Refazer onboarding (skill `leila-scaling` 5 Star Service).
- Refazer continuity offer (skill `money-models`).
- Repensar pricing tier (skill `pricing-playbook`).

**Bloco 3 — Métricas e monitoring (sempre):**
- North star metric de retention (ex: NPS, day-90 product adoption, expansion revenue).
- Threshold de "cliente em risco" (ex: 0 logins em 14 dias).
- Trigger automático de intervenção.

**Bloco 4 — Cultura e operação:**
- 1 pessoa responsável por retention metrics (não diluído).
- Review semanal de churn em squad.
- Pós-mortem de cada cancelamento (mesmo se for inevitável).

### Passo 6: Winback (se `--foco=winback`)

Sequência de 3-4 emails para clientes que saíram nos últimos 90 dias:

**Email 1 (no momento que sai):**
- Honestidade + 1 pergunta direta ("o que eu poderia ter feito diferente?")
- Sem CTA de venda.

**Email 2 (+30 dias):**
- Update do que mudou desde que saiu (novo recurso, novo case, refinement no produto).
- CTA muito leve ("fique de olho").

**Email 3 (+60 dias):**
- Oferta de winback específica (não desconto genérico — algo verdadeiramente novo).
- CTA: pequena conversa de 15min sem pressão.

**Email 4 (+90 dias):**
- Última call. Honesto que vai parar de mandar.
- Porta aberta sempre.

### Passo 7: Impacto financeiro

Delegate ao `money-model-architect`:

```
Cenário atual:
- Churn rate: {{X}}%/mês
- LTV atual: R$ {{X}}
- Quanto cada 1% de redução no churn vale?

Projeção:
- Reduzir churn de {{X}}% para {{Y}}% em 90 dias
- LTV sobe para R$ {{Z}}
- Impacto em ARR/12 meses: R$ {{W}}
```

### Passo 8: Humanizer (lite)

### Passo 9: Salva

`outputs/retention/churn-analysis-{produto_slug}-{YYYYMMDD}-v{n}.md` via template `churn-analysis.md`.

Se `--foco=winback`: também salva `outputs/retention/winback-sequence-{produto_slug}-{YYYYMMDD}-v{n}.md` (estrutura herdada de `email-sequence.md`).

### Passo 10: Preview na conversa

```
✅ Salvo em: outputs/retention/churn-analysis-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Churn atual: {{X}}%/mês
   • Motivo dominante: {{tipo}} ({{N}}% dos casos)
   • Quick wins identificados: {{N}}
   • Impacto financeiro de retention 90d: R$ {{X}}
   • Status humanizer: ✓ lite pass

👉 Próximos passos:
   1. Rodar 5-10 win/loss interviews esta semana (script no output)
   2. Implementar 3 quick wins do Bloco 1 nos próximos 30 dias
   3. Re-medir churn em 90 dias e gerar v2 da análise
```

## Critério de pronto

- [ ] Churn rate medido e contextualizado vs benchmark
- [ ] Motivo dominante identificado (com %)
- [ ] Quick wins concretos (3-5) implementáveis em 30 dias
- [ ] Mudanças estruturais identificadas com framework Hormozi correspondente
- [ ] Impacto financeiro quantificado (R$ por % de churn reduzido)
- [ ] Win/loss interview script (≥ 6 perguntas)
- [ ] Para `--foco=winback`: sequência de 3-4 emails

## Anti-padrões

- "Vamos descontar pra reter" (cliente que sai por valor não volta por preço)
- Ignorar churn passivo (só olha cancelamentos formais)
- Win/loss interview sem perguntar "se voltasse" (perde insight)
- Quick wins genéricos ("melhorar atendimento") — precisa específico
- Mudança estrutural sem owner (nenhuma pessoa responsável = nada muda)
- Esquecer pós-mortem (perde aprendizado de cada caso)
- Winback como spam (mesma sequência pra todos os clientes que saíram)
