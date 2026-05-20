---
plugin: hormozi-gtm
plugin_version: 0.1.0
command: pricing
version: 1
status: draft
created: {{ISO8601}}
client: {{slug}}
product: {{produto-slug}}
frameworks:
  - pricing-playbook
  - value-equation
  - ltv-cac
  - money-models
humanizer_pass: true
humanizer_mode: lite
audit_ref: {{caminho_ou_null}}
---

# Pricing Review — {{produto}}

## TL;DR

**Preço atual:** R$ {{X}}
**Recomendação:** range R$ {{Y}} a R$ {{Z}} (default Gold tier)
**Maior alavanca:** {{...}}
**Risco principal:** {{...}}

---

## 📊 Snapshot

| Campo | Valor |
|---|---|
| Produto | {{nome}} |
| Preço atual | R$ {{X}} |
| Modelo | one-time \| recorrência \| híbrido |
| Margem gross atual | {{X}}% |
| Volume mensal | {{N}} clientes |
| LTGP estimado | R$ {{X}} |
| CAC atual | R$ {{X}} |
| Ratio LTGP:CAC | {{X}}:1 |

---

## 🏛 Concorrência direta

| Concorrente | Oferta similar | Preço | Observação |
|---|---|---|---|
| {{nome 1}} | {{...}} | R$ {{X}} | {{...}} |
| {{nome 2}} | {{...}} | R$ {{X}} | {{...}} |
| {{nome 3}} | {{...}} | R$ {{X}} | {{...}} |
| {{nome 4}} (ancora superior) | {{...}} | R$ {{X}} | {{...}} |

**Sua posição no mercado:** {{baixo | mid | mid-high | premium}}

---

## ⚖️ Análise das 5 Leis

### Lei 1: Compete em valor, não em preço
**Score:** {{verde | amarelo | vermelho}}
**Diagnóstico:** {{...}}
**Recomendação:** {{...}}

### Lei 2: Cobra o que vale, não o que custa
**Score:** {{...}}
**Diagnóstico:** {{...}}
**Recomendação:** {{...}}

### Lei 3: Preço sinaliza qualidade
**Score:** {{...}}
**Diagnóstico:** {{...}}
**Recomendação:** {{...}}

### Lei 4: Tiering captura mais mercado
**Score:** {{...}}
**Diagnóstico:** {{tem tiers? funcionam?}}
**Recomendação:** {{...}}

### Lei 5: Runway maior, ask maior
**Score:** {{...}}
**Diagnóstico:** {{...}}
**Recomendação:** {{...}}

---

## 💡 É problema de preço OU de percepção?

{{Análise específica diferenciando os dois. Se o problema é percepção de valor, baixar preço não resolve — fortalece probability primeiro.}}

**Conclusão:** {{problema é preço | problema é percepção | ambos}}

---

## 🎯 Recomendação

### Estrutura de tiers proposta

**Tier 1 — Silver: R$ {{X}}**
- {{deliverables}}
- {{Para quem: entrada/budget-conscious}}

**Tier 2 — Gold (DEFAULT): R$ {{Y}}** ← destacar visualmente
- {{deliverables}}
- {{Para quem: bulk do mercado, 60-70%}}

**Tier 3 — Platinum: R$ {{Z}}**
- {{deliverables}}
- {{Para quem: high-touch, ancoragem)}}

### Ancoragem
{{Como apresentar visualmente: "vs Mentoria C a R$ X" ou "valor agregado da stack R$ Y"}}

### Estrutura de pagamento
- À vista: R$ {{X}}
- {{N}}x sem juros: R$ {{X/N}}
- {{12}}x com juros: R$ {{X/12 + juros}}

### Downsell
{{Para quem disse não ao Silver — formato + preço}}

### Upsell (pós-checkout)
{{Order bump ou OTO — formato + preço + função absorver CAC em 30 dias}}

---

## 🧪 Teste de validação (1-2 semanas)

**Cenário:**
Próximos 10-20 leads vão receber o novo pricing.

**Métricas:**
- Conversion rate lead → close
- AOV (average order value)
- Take rate por tier (qual escolhem)
- Tempo médio de decisão
- Razões de "não" (entrevista qualitativa em 3-5 no-buys)

**Critério de sucesso:**
Conversion rate cai <30% E AOV sobe >50% → mantém novo preço
Conversion rate cai >30% E AOV sobe <50% → reverte ou ajusta

---

## ⚠️ Riscos da recomendação

1. **{{Risco 1 — ex: "Audit da oferta indica Probability fraca (4/10). Subir preço sem fortalecer probability primeiro pode quebrar conversão."}}**
2. **{{Risco 2 — ex: "Concorrente Y está rodando promoção até DD/MM. Timing pode confundir o teste."}}**
3. **{{Risco 3 — ex: "Sem cases visíveis na LP, ancoragem do Platinum pode parecer artificial."}}**

---

## 🔄 Próximos passos

1. Se há audit prévia E Probability ≥ 7, ative novo pricing em 2-3 dias
2. Se Probability < 7, rode `/hormozi-gtm:audit` primeiro e fortaleça oferta antes de mexer no preço
3. Após teste de 2 semanas, revisita com `/hormozi-gtm:pricing` (versionamento gera v2)

---

*Pricing review gerado pelo plugin hormozi-gtm. Persona Alex Hormozi aplicada. Humanizer (modo lite) aplicado.*
