---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: objections
version: 1
status: draft
created: {{ISO8601}}
client: {{empresa_slug}}
product: {{produto_slug}}
segmento: {{icp_subset_ou_geral}}
frameworks:
  - value-equation
  - grand-slam-offer
  - pricing-playbook
  - guarantees
humanizer_pass: true
humanizer_mode: full
audit_ref: {{caminho_ou_null}}
parent_version: {{caminho_v_anterior_ou_null}}
---

# Matriz de Objeções — {{produto_nome}}

## TL;DR

**Total de objeções mapeadas:** {{N}}
**Root cause dominante:** {{Oferta | Preço | Timing | Trust}} ({{N}}% das objeções)
**Recomendação estrutural:** {{em 1-2 frases}}

---

## Distribuição por root cause

| Categoria | Quantidade | % | Diagnóstico |
|---|---|---|---|
| Oferta | {{N}} | {{X}}% | {{1 frase}} |
| Preço | {{N}} | {{X}}% | {{1 frase}} |
| Timing | {{N}} | {{X}}% | {{1 frase}} |
| Trust | {{N}} | {{X}}% | {{1 frase}} |

---

## Top objeções (com script palavra-por-palavra)

### Objeção 1: "{{frase típica do prospect}}"

**Root cause:** {{Oferta | Preço | Timing | Trust}}

**O que a objeção significa de verdade:** {{2-3 frases. Frequentemente diferente do que o prospect verbaliza. Ex: "Tá caro" pode significar "não vejo valor suficiente" ou "não tenho budget agora" — são reframes diferentes.}}

**Pergunta de qualificação (antes do reframe):**

> "Antes de responder, posso entender uma coisa? {{pergunta específica que separa o tipo real de objeção, ex: 'É problema do preço em si ou do budget disponível esse trimestre?'}}"

**Reframe (script palavra-por-palavra):**

> "{{2-3 frases. Voz direta Hormozi. Sem 'eu entendo perfeitamente'. Reframe ataca a raiz, não o sintoma. Termina com pergunta que move pra próximo passo.}}"

**Mitigação na oferta:**

{{Mudança estrutural que reduz essa objeção aparecer. Ex: "Adicionar garantia condicional reduz objeção 'e se não funcionar' em ~70% dos casos."}}

**Sucesso esperado:** {{X}}% dos prospects movem adiante após reframe (estimativa baseada em pattern matching com casos comparáveis)

---

### Objeção 2: "{{frase típica}}"

[mesma estrutura]

---

### Objeção 3: "{{frase típica}}"

[mesma estrutura]

---

## Objeções secundárias (matriz resumida)

| Frase do prospect | Root cause | Reframe (1 linha) | Mitigação |
|---|---|---|---|
| "{{...}}" | {{cat}} | "{{...}}" | {{...}} |
| "{{...}}" | {{cat}} | "{{...}}" | {{...}} |
| "{{...}}" | {{cat}} | "{{...}}" | {{...}} |

---

## Recomendações estruturais

Baseado na distribuição:

{{Se Oferta domina (≥40%):}}
- **Roda `/hormozi-gtm:audit`** — o problema raiz é Value Equation, não copy de objeção.
- Foco no vetor mais quebrado (Probability geralmente).

{{Se Preço domina (≥40%):}}
- **Roda `/hormozi-gtm:pricing`** — tiering pode estar errado ou ancoragem ausente.
- Considera adicionar Platinum decoy para tornar Gold "óbvio".

{{Se Timing domina (≥40%):}}
- **Reforça escassez genuína** (skill `scarcity-urgency`).
- Considera adicionar urgência operacional (cohort, capacidade, prazo).

{{Se Trust domina (≥40%):}}
- **Audit founder-market fit** (skill `founder-market-fit`).
- Adiciona cases visíveis na LP, depoimentos em vídeo, mídia.

---

## Treinamento sugerido

**Role-play de sales call (30min):**
1. Closer apresenta oferta (2min).
2. SDR/consultor faz 3 objeções da matriz (1 de cada categoria).
3. Closer aplica reframe.
4. Debrief: o que funcionou, o que ficou enlatado, o que precisa refinar.

**Repetir 1x/semana até reframes ficarem naturais (4-6 semanas típico).**

---

## Métricas de sucesso

| Métrica | Como medir | Alvo |
|---|---|---|
| Reframe rate | % de objeções reframeadas com sucesso | ≥ 70% |
| Close rate pós-reframe | % que fecha após objeção | ≥ 40% |
| Objeção dominante muda? | Reagrupar objeções após 30 dias | Distribution diferente = oferta evoluiu |

---

*Matriz de objeções gerada pelo plugin hormozi-gtm. Persona Alex Hormozi aplicada. Humanizer (modo full) aplicado.*
