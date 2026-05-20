---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: review
version: 1
status: draft
created: {{ISO8601}}
client: {{empresa_slug}}
product: {{produto_slug}}
material_revisado: {{caminho_do_material}}
material_tipo: {{lp | ad | email | proposta | outro}}
frameworks:
  - value-equation
  - grand-slam-offer
humanizer_pass: true
humanizer_mode: lite
---

# Review — {{nome_do_material}}

## TL;DR

**Veredito:** {{LEVE | MÉDIO | CRÍTICO}}

**Em 1 frase:** {{...}}

**Top 3 fix em ordem:**
1. {{fix 1}}
2. {{fix 2}}
3. {{fix 3}}

---

## 📜 Histórico de reviews

{{Esta seção só aparece quando version > 1 (Re-review). Se v1, deletar essa seção inteira.}}

**Review anterior:** `{{parent_version}}` ({{data v1}})

**Mudanças desde a review anterior:**

| Item v1 | Estado em v2 | Comentário |
|---|---|---|
| {{problema X de v1}} | ✅ Resolvido | {{como foi resolvido}} |
| {{problema Y de v1}} | 🟡 Em progresso | {{o que melhorou, o que falta}} |
| {{problema Z de v1}} | ❌ Piorou | {{por quê}} |
| — | 🆕 Novo problema | {{problema W não existia em v1}} |

**Avanço geral:** {{em 1-2 frases — material melhorou, regrediu, ou estagnou?}}

---

## ✅ O que funciona

(Calibra credibilidade — não economiza no que tá bom)

- {{ponto 1 que funciona com justificativa}}
- {{ponto 2}}
- {{ponto 3}}

---

## 🔴 Problemas em ordem de impacto

### Problema 1 — {{título}}

**Severidade:** CRÍTICO | ALTO | MÉDIO

**O problema:**
{{descrição concreta do que está errado}}

**Por que mata:**
{{efeito específico em conversão / leitor / cliente}}

**Fix concreto:**
{{ação executável, não "melhorar clareza"}}

---

### Problema 2 — {{título}}

**Severidade:** ALTO | MÉDIO

**O problema:**
{{...}}

**Por que mata:**
{{...}}

**Fix concreto:**
{{...}}

---

### Problema 3 — {{título}}

**Severidade:** MÉDIO

**O problema:**
{{...}}

**Por que mata:**
{{...}}

**Fix concreto:**
{{...}}

---

### Problema 4 (se aplicável)

{{...}}

---

### Problema 5 (se aplicável)

{{...}}

---

## 🏆 Top 3 se for fazer só 3 coisas

1. **{{Fix 1}}** — {{1 linha de impacto esperado}}
2. **{{Fix 2}}** — {{1 linha de impacto esperado}}
3. **{{Fix 3}}** — {{1 linha de impacto esperado}}

---

## ✍️ Reescrita de trechos críticos

### Trecho 1 (original)

> {{citação do material original que precisa de fix}}

### Trecho 1 (reescrito)

> {{reescrita aplicando o fix}}

**O que mudou:** {{1 linha explicando o move}}

---

### Trecho 2 (original)

> {{...}}

### Trecho 2 (reescrito)

> {{...}}

**O que mudou:** {{...}}

---

## 🧪 Diagnóstico Value Equation aplicado

Se o material é LP/ad/copy comercial:

| Vetor | Score | Comentário |
|---|---|---|
| Dream Outcome | {{X}}/10 | {{...}} |
| Probability | {{X}}/10 | {{...}} |
| Time Delay | {{X}}/10 | {{...}} |
| Effort | {{X}}/10 | {{...}} |

**Vetor crítico:** {{...}}

---

## 🎯 Próximos passos recomendados

1. {{ação imediata — ex: "Reescreva a seção de oferta aplicando fix 1"}}
2. {{...}}
3. {{Se aplicável: rodar /hormozi-gtm:audit antes de iterar mais a copy}}

---

*Review gerada pelo plugin hormozi-gtm. Persona Alex Hormozi aplicada. Humanizer (modo lite) aplicado.*
