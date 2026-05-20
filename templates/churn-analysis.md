---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: churn-prevention
foco: {{churn | winback | retention}}
version: 1
status: draft
created: {{ISO8601}}
client: {{empresa_slug}}
product: {{produto_slug}}
frameworks:
  - leila-scaling
  - value-equation
  - money-models
  - ltv-cac
humanizer_pass: true
humanizer_mode: lite
parent_version: {{caminho_v_anterior_ou_null}}
---

# Churn Analysis — {{produto_nome}}

## TL;DR

**Churn rate atual:** {{X}}%/mês ({{tendência: subindo/estável/caindo}})
**Motivo dominante:** {{tipo}} ({{N}}% dos casos)
**Impacto financeiro:** R$ {{Y}}/mês em revenue perdido
**Recomendação principal em 1 frase:** {{...}}

---

## 1. Snapshot

| Métrica | Valor atual | Benchmark mercado | Status |
|---|---|---|---|
| Churn mensal | {{X}}% | {{2-5% SaaS, 5-15% consultoria}} | {{✓ / ⚠️ / ❌}} |
| Lifetime médio | {{N}} meses | {{...}} | {{...}} |
| NPS atual | {{X}} | {{30-50 saudável}} | {{...}} |
| Net Revenue Retention | {{X}}% | {{100%+ é alvo}} | {{...}} |
| % churn em <30 dias | {{X}}% | {{<10% saudável}} | {{...}} |

---

## 2. Distribuição por tipo de churn

| Tipo | % do total | Janela típica | Raiz no Value Equation |
|---|---|---|---|
| Precoce (<30d) | {{X}}% | Onboarding | Probability ↓ ou expectativa quebrada |
| Médio (30-90d) | {{X}}% | Entrega | Probability/Time Delay ↓ |
| Tardio (>90d) | {{X}}% | Continuity | Continuity offer fraca |
| Voluntário | {{X}}% | Qualquer | Alternativa surgiu ou budget mudou |
| Passivo | {{X}}% | Qualquer | Engagement caiu |

**Padrão dominante:** {{descrição em 1-2 frases}}

---

## 3. Motivos declarados (após win/loss interviews)

| Motivo | N clientes | % | Categoria raiz | Reversível? |
|---|---|---|---|---|
| Preço | {{N}} | {{X}}% | {{Dream Outcome ↓ / Probability ↓}} | Sim |
| Não entregou esperado | {{N}} | {{X}}% | {{Probability ↓}} | Sim |
| Time interno assumiu | {{N}} | {{X}}% | {{Effort ↓ — cliente conseguiu reduzir}} | Não (sucesso, mas adeus) |
| Mudou de fornecedor | {{N}} | {{X}}% | {{Saturação ou positioning}} | Parcialmente |
| Mudança no business | {{N}} | {{X}}% | {{Não-evitável}} | Não |
| Outro | {{N}} | {{X}}% | {{...}} | {{...}} |

---

## 4. Win/loss interviews — insights

### 5-10 entrevistas qualitativas realizadas

**Quote recorrente:**
> "{{frase que apareceu em ≥3 entrevistas, com aspas exatas}}"

**Padrão emergente:**
{{2-3 frases descrevendo o que múltiplos clientes que saíram disseram em comum.}}

**Surpresas (o que clientes pediram que você não esperava):**
- {{insight 1}}
- {{insight 2}}

**O que continua valendo (não joga fora):**
- {{aspectos da oferta que clientes que saíram ainda elogiam}}

---

## 5. Retention Playbook — 4 blocos

### Bloco 1: Quick wins (0-30 dias)

Implementação imediata. Cada item: descrição + owner + métrica de sucesso.

| Ação | Owner | Métrica de sucesso | Prazo |
|---|---|---|---|
| {{Adicionar check-in semanal nas primeiras 4 semanas de cliente novo}} | {{CS}} | {{NPS dia-30 ≥ 7}} | 2 semanas |
| {{Survey NPS automático em D30/D60/D90}} | {{Ops}} | {{≥ 70% response rate}} | 2 semanas |
| {{One-Done Guarantee em resposta a tickets (4h úteis)}} | {{Suporte}} | {{First response time < 4h}} | 1 semana |
| {{...}} | {{...}} | {{...}} | {{...}} |
| {{...}} | {{...}} | {{...}} | {{...}} |

### Bloco 2: Mudanças estruturais (30-90 dias)

| Mudança | Skill Hormozi correspondente | Owner | Marco principal |
|---|---|---|---|
| {{Refazer onboarding em 4-week structured journey}} | `leila-scaling` (5 Star Service) | {{CS lead}} | Primeiros 5 clientes na nova jornada |
| {{Redesenhar continuity offer}} | `money-models` | {{Founder + Pricing}} | Tier de continuity lançado |
| {{Repensar pricing tier para reduzir comoditização}} | `pricing-playbook` (Lei 4) | {{Founder}} | Novo tiering testado em 10 sales calls |

### Bloco 3: Métricas e monitoring

**North star metric de retention:** {{NPS | day-90 product adoption | expansion revenue | net retention}}

**Alvo (12 meses):** {{X}}

**Threshold de "cliente em risco":**
- {{ex: 0 logins em 14 dias → trigger automático}}
- {{ex: NPS dia-30 < 5 → call de check-in obrigatória em 48h}}
- {{ex: 2 tickets de suporte em 7 dias → escalation pra CS sênior}}

**Trigger de intervenção:**
{{Como o sistema avisa quem é responsável quando threshold bate.}}

### Bloco 4: Cultura e operação

- **Owner do retention metric:** {{1 pessoa, não diluído}}
- **Cadência de review:** semanal (squad), mensal (founders)
- **Pós-mortem obrigatório:** todo cancelamento gera 1 documento curto (15min de escrita) com: motivo, o que aprendemos, o que muda na operação
- **Ritual:** primeira segunda do mês, 30min de retention review

---

## 6. Impacto financeiro projetado

### Cenário atual

```
Churn mensal: {{X}}%
LTV atual: R$ {{Y}}
ARR: R$ {{Z}}
```

### Cenário 90 dias (após implementar Bloco 1 + 2)

```
Churn mensal projetado: {{X - 1 a 2 pontos percentuais}}%
LTV projetado: R$ {{Y + 20-40%}}
ARR adicional capturado em 12 meses: R$ {{W}}
```

### ROI da intervenção

**Investimento (3 meses):** {{horas de squad + ferramentas}} ≈ R$ {{Z}}
**Retorno (12 meses):** R$ {{W}}
**Ratio:** {{W/Z}}x

---

## 7. Próximos 14 dias — ações concretas

- [ ] Rodar 5-10 win/loss interviews com clientes que saíram nos últimos 90 dias (script no Anexo)
- [ ] Implementar Quick Win 1: {{...}}
- [ ] Implementar Quick Win 2: {{...}}
- [ ] Definir owner único de retention metric
- [ ] Agendar review semanal recorrente

---

## Anexo A — Script de win/loss interview (6-8 perguntas)

1. "Pode contar o momento exato em que decidiu cancelar? O que aconteceu no dia/semana?"
2. "Antes de decidir, você tentou resolver isso de outra forma? Como?"
3. "O que o {{competidor ou alternativa}} oferece que a gente não oferecia?"
4. "Olhando pra trás, o que continua valendo do tempo que você foi cliente?"
5. "Se você pudesse voltar 90 dias antes da decisão, o que faria diferente OU o que eu poderia ter feito diferente?"
6. "Em quais condições você consideraria voltar?"
7. "Tem alguma coisa que eu não perguntei mas seria útil eu saber?"
8. "Posso te procurar em 6 meses pra atualizar você sobre o que mudou aqui?"

**Regras:**
- Sem agenda de venda. Cliente sente.
- Toma notas. Não argumenta nem defende.
- Promete confidencialidade (não usa o que falaram em copy sem permissão).

---

*Churn analysis gerado pelo plugin hormozi-gtm. Persona Alex Hormozi aplicada. Humanizer (modo lite) aplicado.*
