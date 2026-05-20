---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: onboarding-cliente
version: 1
status: draft
created: {{ISO8601}}
client: {{empresa_slug}}
product: {{produto_slug}}
duracao_dias: {{14 | 30 | 60 | 90}}
tipo: {{self-serve | guided | done-with-you | done-for-you}}
ticket_medio_faixa: {{<5k | 5k-30k | >30k | enterprise}}
frameworks:
  - leila-scaling
  - value-equation
humanizer_pass: true
humanizer_mode: lite
parent_version: {{caminho_v_anterior_ou_null}}
---

# Onboarding de Cliente — {{produto_nome}}

## Visão geral

**Duração total:** {{N}} dias
**Tipo:** {{self-serve | guided | done-with-you | done-for-you}}
**Ticket médio:** R$ {{faixa}}
**Time-to-first-value alvo:** {{N}} dias
**Owner principal:** {{cargo}}

---

## Estrutura por marcos

### Marco 0 — Welcome (Dia 0, hora 0)

**Trigger:** assinatura confirmada (contrato / pagamento).

**Touch:**
- Email automático em até 5min
- (R$ 30k+) Mensagem pessoal do founder em 24h

**Conteúdo do welcome email:**
```
Subject: Bem-vindo — próximos 30 dias com {{produto_nome}}

[Nome],

Decisão tomada. Próximas semanas vão definir se foi a certa.
Aqui está o que acontece a partir de agora:

1. [Marco 1] em até 3 dias
2. [Quick win] visível até dia 7
3. [Mid-point] no dia 21
4. [Wrap] no dia 30 com NPS

Próxima ação: [link para agendar kickoff call] — escolha um horário nos próximos 3 dias.

Qualquer dúvida, responda este email. Resposta em até 4h úteis.

[Nome do CS lead]
```

**Métrica:** % que abre + clica o link em 24h. Alvo ≥ 80%.

---

### Marco 1 — Kickoff (Dia 1-3)

**Trigger:** cliente agendou via link do welcome.

**Touch:** call de 45-60min com CS lead + cliente.

**Agenda:**
1. (5min) Recap do que foi vendido. Realinha expectativa.
2. (10min) Cliente conta contexto atual + objetivo principal em 1 frase.
3. (15min) CS lead apresenta plano dos 30 dias com marcos.
4. (15min) Coleta inputs necessários para Marco 2 (quick win).
5. (5min) Próximos passos + agenda Marco 3.

**Output da call:**
- Documento de 1 página com objetivo + plano + responsabilidades + próximos marcos.
- Enviado ao cliente em até 24h pós-call.

**Métrica:** % de calls que aconteceu em < 5 dias da venda. Alvo ≥ 90%.

---

### Marco 2 — Quick win (Dia 7)

**O elemento mais importante de todo o onboarding.**

**Quick win deve ser:**
- Visível (cliente mostra pra chefe/time)
- Atribuível (ficou claro que foi por causa de você)
- Em até 7 dias
- Modesto se necessário (mais importante existir do que ser transformador)

**Exemplos por categoria:**

| Categoria | Quick win típico |
|---|---|
| Consultoria growth | Auditoria de funil com 5 ações imediatas + ranking |
| Consultoria pricing | Recomendação de range + tiering proposto + teste de 14 dias |
| SaaS B2B | Primeiro dashboard configurado com dado real do cliente |
| Cohort educacional | Primeiro framework documentado + aplicado a caso do aluno |
| Done-for-you | Primeira entrega tangível (LP rascunho, copy V1, etc.) |

**Touch:**
- Email com entrega do quick win + 1 frase resumindo valor.
- (R$ 30k+) Loom de 5min do CS apresentando o quick win.

**Métrica:** % de clientes que recebem quick win confirmado em D7. Alvo ≥ 95%.

---

### Marco 3 — Check-in NPS (Dia 14)

**Trigger:** automático D14.

**Touch:**
- Survey curto (3 perguntas)
- (R$ 30k+) Call de 30min se NPS < 8

**Survey:**
1. "Em escala 0-10, qual a chance de recomendar {{produto}} para um colega?"
2. "O que mais te impressionou positivamente nas primeiras 2 semanas?"
3. "O que você mudaria, se algo? (resposta opcional)"

**Métrica:** % que responde survey. Alvo ≥ 70%. NPS médio alvo ≥ 8.

**Trigger de intervenção:** NPS < 7 → call obrigatória do CS lead em 48h.

---

### Marco 4 — Mid-point review (Dia 21)

**Trigger:** D21 automático.

**Touch:** call de 30min com CS lead.

**Agenda:**
1. (5min) Recap do que foi entregue até agora vs o que foi prometido.
2. (10min) Cliente compartilha o que está funcionando + o que não está.
3. (10min) Realinhamento das próximas 4-8 semanas pós-onboarding.
4. (5min) Confirma próximos marcos.

**Output:** documento curto de mid-point com o que foi acordado.

**Métrica:** % de mid-point reviews realizados. Alvo ≥ 90%.

---

### Marco 5 — Wrap-up + NPS formal (Dia 30)

**Trigger:** D30 automático.

**Touch:**
- Email com summary do que foi alcançado nos primeiros 30 dias
- NPS formal (Net Promoter Score + 2 perguntas abertas)
- Transição para fase operacional / continuity

**Conteúdo do wrap-up:**
```
Subject: 30 dias — onde estamos e o que vem agora

[Nome],

30 dias atrás você começou conosco. Aqui está o que rolou:

✅ [Marco 1]: [resultado concreto]
✅ [Marco 2]: [quick win entregue]
✅ [Marco 3]: [progresso em métrica]
✅ [Marco 4]: [next phase alinhada]

NPS rápido: [link]

Próxima fase (dias 31-90):
- [O que continua]
- [Cadência nova de touches]
- [Próximo grande marco]

[Owner] continua como ponto principal de contato.

[Founder ou CS lead]
```

**Métrica:** NPS dia-30 ≥ 8. % que completa todos os 5 marcos ≥ 90%.

---

## Triggers de intervenção

| Threshold | Quem age | Em quanto tempo |
|---|---|---|
| Não respondeu welcome em 48h | CS lead | DM direta em 4h úteis |
| Não compareceu kickoff | CS lead | Reagenda + tira temperatura por SMS/WhatsApp |
| Marco 2 (D7) sem quick win confirmado | CS lead + Founder | Escalation interna em 24h |
| NPS dia-14 < 7 | CS lead + Founder | Call obrigatória em 48h |
| 0 logins (SaaS) em 10 dias | Automated trigger + CS | DM em 24h |
| 2+ tickets em 7 dias | CS sênior assume | Escalation imediata |
| NPS dia-30 < 6 | Founder direto | Call de retention em 72h |

---

## Cadência de touches (overview)

| Dia | Touch | Tipo | Owner |
|---|---|---|---|
| 0 | Welcome email | Automated | Sistema |
| 1-3 | Kickoff call | Call 45min | CS lead |
| 7 | Quick win delivery | Email + (Loom se >R$30k) | CS lead |
| 14 | NPS check-in | Survey | Automated |
| 21 | Mid-point review | Call 30min | CS lead |
| 30 | Wrap-up + NPS formal | Email + Survey | CS lead + Founder |

Para R$ 30k+: adicionar weekly check-in em D7, D14, D21, D28 (4 calls extras).

---

## Métricas de sucesso

| Métrica | Alvo | Por que importa |
|---|---|---|
| % completam marco 5 (D30) | ≥ 90% | Onboarding funcionando |
| NPS dia-14 | ≥ 8 | Cliente vê valor early |
| Time-to-quick-win | ≤ 7 dias | Marco 2 entregue |
| % de touches respondidos | ≥ 70% | Engagement saudável |
| Day-90 retention | ≥ 85% | Correlacionada com onboarding bom |
| Churn em <30 dias | < 5% | Reflexo direto do onboarding |

---

## Owners e cadência interna

- **Owner principal:** {{cargo, 1 pessoa}}
- **Backup:** {{cargo}}
- **Founder envolvido em:** kickoff (≥ R$ 30k) + NPS dia-30 (todos).
- **Squad review:** semanal (5min de "onde estão os clientes em onboarding").
- **Founders review:** mensal (qual a saúde média do onboarding atual).

---

## Anti-padrões a evitar

- Welcome genérico sem expectativa concreta
- Sem kickoff call (cliente fica perdido)
- Quick win frágil (cliente não mostra pra ninguém)
- Touch sem propósito (email só "tá tudo bem?" sem agregar)
- Sem trigger automatizado (cliente em risco passa)
- Onboarding longo demais para ticket pequeno
- Onboarding curto demais para programa longo
- Sem NPS formal (sem como medir saúde)
- Owner diluído (CS, suporte, founder — todos = ninguém)
- Esquecer transição para fase operacional (cliente sente abandono em D31)

---

*Onboarding gerado pelo plugin hormozi-gtm. Persona Alex Hormozi aplicada. Humanizer (modo lite) aplicado.*
