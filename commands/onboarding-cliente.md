---
description: Primeiros 30 dias do cliente pós-venda. Cadência de touches estruturada, quick wins early para validar decisão de compra, marcos de valor visível. Reduz churn precoce (< 30 dias) em 40-60% típico. Para consultoria, agência, programa cohort, SaaS B2B mid-market.
argument-hint: "[--produto=<slug>] [--ref=<caminho>] [--duracao=14|30|60] [--no-humanize]"
---

# /hormozi-gtm:onboarding-cliente

Churn em < 30 dias é o mais barato de reverter — só requer estrutura de onboarding. Esta skill gera jornada de primeiros 30 dias com cadência específica, quick wins early para validar decisão de compra, marcos visíveis de progresso.

## Carregamento de persona

Use `hormozi-persona` para orquestrar. Delegate ao `leads-strategist` para encaixar onboarding como engine de retention (não só como UX). Pass final pelo `humanizer` modo **lite** (output é interno para o time operacional).

## Skills ativas

- `leila-scaling` (5 Star Service framework — pilar do onboarding)
- `value-equation` (Time Delay — quanto antes o cliente vê valor, melhor)
- `output-conventions`
- `humanizer-rules` (modo lite)

## Argumentos

| Argumento | Comportamento |
|---|---|
| (vazio) | Modo interativo: pergunta produto + duração + complexidade |
| `--produto=<slug>` | Slug do produto |
| `--ref=<caminho>` | Refinar onboarding existente |
| `--duracao=14\|30\|60` | Janela de onboarding (default 30 dias) |
| `--no-humanize` | Pula humanizer |

## Pré-requisitos

1. `gtm-context.md` existe → carrega ICP, oferta, ticket médio
2. Para SaaS: produto entregue (não é onboarding de produto que não existe)
3. Para consultoria/cohort: contrato assinado / oferta vendida

## Fluxo

### Passo 1: Calibra complexidade do onboarding

Pergunta:
- **Ticket médio:** R$ < 5k? 5k-30k? > 30k?
- **Time-to-first-value esperado:** dias? semanas? meses?
- **Cliente faz sozinho ou com você?:** self-serve, guided, done-with-you, done-for-you?

Determina duração + intensidade:

| Ticket | Time-to-value | Tipo | Duração de onboarding | Touches |
|---|---|---|---|---|
| < R$ 5k | < 7 dias | Self-serve | 14 dias | 5-7 (email, in-app) |
| R$ 5k-30k | 14-30 dias | Guided | 30 dias | 8-12 (email + 1-2 calls) |
| > R$ 30k | 30-90 dias | Done-with-you | 30-60 dias | 12-20 (call semanal + assíncrono) |
| Enterprise | 60-180 dias | Done-for-you | 60-90 dias estruturado | Time dedicado + dashboard de progresso |

### Passo 2: Estrutura por marcos (não por dias)

Onboarding eficaz é por **outcome**, não por timeline. Cada marco entrega um valor concreto.

**Estrutura padrão 30 dias (guided, ticket R$ 5k-30k):**

- **Marco 0 (Dia 0):** Welcome — confirma decisão, define expectativa, agenda kickoff.
- **Marco 1 (Dia 1-3):** Kickoff call — alinhamento de objetivo + primeiros dados/inputs do cliente.
- **Marco 2 (Dia 7):** Primeira entrega visível (quick win) — algo tangível que o cliente possa mostrar para chefe/time.
- **Marco 3 (Dia 14):** Check-in NPS-like + segundo deliverable.
- **Marco 4 (Dia 21):** Mid-point review — alinha próximas 4 semanas, ajusta escopo se necessário.
- **Marco 5 (Dia 30):** Wrap-up do onboarding + transição para fase operacional + NPS formal.

### Passo 3: Touches por marco

Cada marco tem touches específicos:

**Email + In-app (todos os tickets):**
- Welcome (D0)
- Quick win achievement (D7)
- Check-in NPS (D14)
- Mid-point recap (D21)
- 30-day wrap-up (D30)

**Calls (R$ 5k+):**
- Kickoff (D1-3)
- Mid-point review (D21)
- 30-day formal (D30)

**Calls extras (R$ 30k+):**
- Weekly check-in (D7, D14, D21, D28)

### Passo 4: Quick wins early — o load-bearing

O elemento mais importante do onboarding: cliente precisa ver valor concreto antes de D7. Sem quick win, dúvida pós-compra ("será que comprei certo?") vira churn em D60.

Quick win precisa ser:
- **Visível**: cliente pode mostrar pra terceiros (chefe, time).
- **Atribuível**: ficou claro que foi por causa de você.
- **Rápido**: < 7 dias.
- **Modesto se necessário**: não precisa ser transformador. Pode ser "mapeamos seus 3 maiores gargalos com clareza" ou "primeiro relatório de auditoria com 5 ações imediatas".

Para cada produto, identifica qual quick win é entregue no Marco 2 (D7).

### Passo 5: Triggers de intervenção

Define thresholds que disparam ação:

- Cliente não respondeu welcome email em 48h → DM direta do CS lead.
- Cliente não compareceu kickoff call → reagenda + tira temperatura.
- Marco 2 (D7) sem quick win confirmado → escalation interna.
- NPS dia-14 < 7 → call dedicada em 48h com o decisor.
- 0 logins (SaaS) em 10 dias → tem trigger automático.

### Passo 6: Métricas de sucesso do onboarding

- **% que completa marco 5 (D30):** alvo ≥ 90%.
- **NPS dia-14:** alvo ≥ 8.
- **Time-to-quick-win:** alvo ≤ 7 dias.
- **% de touches respondidos:** alvo ≥ 70%.
- **Day-90 retention** (correlacionada): alvo ≥ 85% se onboarding funcionou.

### Passo 7: Humanizer (lite)

### Passo 8: Salva

`outputs/onboarding/onboarding-{produto_slug}-{YYYYMMDD}-v{n}.md` via template `client-onboarding.md`.

### Passo 9: Preview na conversa

```
✅ Salvo em: outputs/onboarding/onboarding-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Duração: {{N}} dias
   • Tipo: {{self-serve | guided | done-with-you | done-for-you}}
   • Marcos definidos: {{N}}
   • Touches totais: {{N}} ({{email + calls + in-app}})
   • Quick win definido para D7: ✓
   • Triggers de intervenção: {{N}}
   • Status humanizer: ✓ lite pass

👉 Próximos passos:
   1. Treinar CS lead nos triggers (role-play 30min)
   2. Configurar emails automatizados no provedor (HubSpot, Active, etc.)
   3. Definir owner único do day-30 NPS
```

## Critério de pronto

- [ ] Duração calibrada por ticket + complexidade
- [ ] Marcos definidos (5 padrão para 30 dias)
- [ ] Quick win específico para D7 identificado
- [ ] Touches por marco com formato (email/call/in-app) definidos
- [ ] Triggers de intervenção com threshold quantitativo
- [ ] Métricas de sucesso + owner único
- [ ] Humanizer lite aplicado

## Anti-padrões

- Onboarding "vou improvisando" sem estrutura (cliente sente)
- Welcome email genérico ("Bem-vindo à família!") em B2B high-ticket
- Quick win frágil (cliente não consegue mostrar pra ninguém)
- Sem trigger de intervenção (cliente em risco passa despercebido)
- Onboarding longo demais (90 dias para ticket de R$ 2k = overkill)
- Onboarding curto demais (7 dias para programa de 6 meses = cliente fica perdido depois)
- Sem owner único (diluído entre 3 pessoas = ninguém responsável)
- Touch sem propósito (email "só pra dizer olá" sem agregar valor)
