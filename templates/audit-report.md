---
plugin: hormozi-gtm
plugin_version: 0.1.0
command: audit
version: 1
status: draft
created: {{ISO8601}}
client: {{slug}}
product: {{produto-slug}}
frameworks:
  - value-equation
  - grand-slam-offer
humanizer_pass: true
humanizer_mode: lite
---

# Audit de Oferta — {{produto}}

## TL;DR

Score agregado: **{{X.X}}/10**.
Gargalo crítico: **{{Dream | Probability | Time | Effort}}** ({{X}}/10).
Top 3 fix em ordem: 1) {{...}} 2) {{...}} 3) {{...}}

---

## Snapshot da oferta auditada

- **Produto:** {{nome}}
- **Preço atual:** R$ {{preco}}
- **ICP:** {{icp}}
- **Transformação prometida:** {{transformacao}}
- **Stack atual:** {{lista_resumida}}
- **Garantia atual:** {{descrição}}

---

## Value Equation Score

### Dream Outcome — {{score}}/10

**Diagnóstico:**
{{análise concreta — o que o cliente quer DE FATO, está claro? é específico? quantificado?}}

**Por que essa nota:**
{{justificativa em 2-3 frases}}

### Perceived Probability of Success — {{score}}/10

**Diagnóstico:**
{{análise — tem cases comparáveis? mechanism nomeado? garantia condicional?}}

**Por que essa nota:**
{{justificativa}}

### Time Delay — {{score}}/10

**Diagnóstico:**
{{tempo até primeiro resultado mensurável; tem milestones intermediários?}}

**Por que essa nota:**
{{justificativa}}

### Effort & Sacrifice — {{score}}/10

**Diagnóstico:**
{{quanto cliente investe; tem templates/done-for-you; suporte ativo?}}

**Por que essa nota:**
{{justificativa}}

---

## Score agregado

```
Valor = (Dream × Probability) / (Time × Effort)
       = ({{X}} × {{X}}) / ({{X}} × {{X}})
       = {{resultado}}
```

Normalizado: **{{X.X}}/10**.

---

## Gargalo crítico

**Vetor mais fraco:** {{Dream | Probability | Time | Effort}} ({{score}}/10)

**Por que esse é o gargalo:**
{{análise em 3-5 linhas explicando como esse vetor está limitando os outros e o efeito em conversão}}

---

## Top 3 alavancas (prioridade)

### 1. {{Alavanca concreta com ação}}

**O que fazer:** {{ação executável, não abstrata}}

**Por que muda o jogo:** {{explica o efeito esperado em Value Equation}}

**Como medir sucesso:** {{métrica concreta}}

### 2. {{Alavanca 2}}

**O que fazer:** {{...}}

**Por que muda o jogo:** {{...}}

**Como medir sucesso:** {{...}}

### 3. {{Alavanca 3}}

**O que fazer:** {{...}}

**Por que muda o jogo:** {{...}}

**Como medir sucesso:** {{...}}

---

## Reescrita sugerida da oferta

{{Parágrafo único, 4-6 linhas, reescrevendo a oferta com as 3 alavancas aplicadas. Sem floreio. Em primeira pessoa do cliente ("você") ou terceira ("[cliente] recebe").}}

---

## Próximos passos recomendados

1. {{Geralmente: rodar /hormozi-gtm:pricing pra validar preço contra novo posicionamento}}
2. {{Depois: /hormozi-gtm:lp criando LP com oferta refeita}}
3. {{Depois: /hormozi-gtm:hooks gerando hooks novos pra ICP refinado}}

---

*Audit gerado pelo plugin hormozi-gtm. Persona Alex Hormozi aplicada. Humanizer (modo lite) aplicado.*
