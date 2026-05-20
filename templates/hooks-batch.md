---
plugin: hormozi-gtm
plugin_version: 0.1.0
command: hooks
version: 1
status: draft
created: {{ISO8601}}
client: {{slug}}
product: {{produto-slug}}
quantidade: {{N}}
angulos: [dream, problem, secret, contrarian, proof]
frameworks:
  - hook-framework
  - ad-copy-formula
humanizer_pass: true
humanizer_mode: full
---

# Hooks Batch — {{produto}}

## TL;DR

{{N}} hooks gerados, distribuídos em {{X}} ângulos.
Top 3 do agent listados ao final com justificativa.

---

## 📊 Tabela completa

| # | Hook | Ângulo | Mecanismo | Onde usar |
|---|------|--------|-----------|-----------|
| 1 | {{frase}} | dream | {{aspiração}} | LP headline |
| 2 | {{frase}} | dream | {{aspiração}} | ad short |
| 3 | {{frase}} | dream | {{aspiração}} | email subject |
| 4 | {{frase}} | problem | {{reframe}} | ad cold |
| 5 | {{frase}} | problem | {{reframe}} | LP H1 |
| 6 | {{frase}} | problem | {{reframe}} | post LinkedIn |
| 7 | {{frase}} | secret | {{curiosity gap}} | email subject |
| 8 | {{frase}} | secret | {{curiosity gap}} | YouTube title |
| 9 | {{frase}} | secret | {{curiosity gap}} | ad paid |
| 10 | {{frase}} | contrarian | {{shock}} | post LinkedIn |
| 11 | {{frase}} | contrarian | {{shock}} | ad short |
| 12 | {{frase}} | contrarian | {{shock}} | LP H2 |
| 13 | {{frase}} | proof | {{authority}} | ad paid |
| 14 | {{frase}} | proof | {{authority}} | LP testimonial header |
| 15 | {{frase}} | proof | {{authority}} | retargeting ad |

---

## 🏆 Top 3 do agent

### 🥇 #{{N}} — {{título curto do ângulo}}

> "{{hook completo}}"

**Por que é o top:** {{justificativa específica — não "mais forte" mas "tem especificidade numérica + reframe contraintuitivo + curiosity gap"}}

**Onde testar primeiro:** {{plataforma + formato}}

---

### 🥈 #{{N}} — {{título curto}}

> "{{hook completo}}"

**Por que:** {{...}}

**Onde testar primeiro:** {{...}}

---

### 🥉 #{{N}} — {{título curto}}

> "{{hook completo}}"

**Por que:** {{...}}

**Onde testar primeiro:** {{...}}

---

## ✅ Critérios de qualidade aplicados

Cada hook passou nos 3 testes:
- [x] **Especificidade numérica:** tem número (idade, valor, tempo, %, quantidade)
- [x] **Tweet test:** lê isoladamente como tweet
- [x] **Curiosity gap:** leitor precisa saber o que vem depois

---

## 🧪 Plano de teste sugerido

**Fase 1 (semana 1):**
Rodar Top 3 com mesmo budget e plataforma. Mata o pior em CTR após 200 impressions.

**Fase 2 (semana 2):**
Top 2 sobreviventes contra 3 hooks da metade (#4-9). Mata 2 piores.

**Fase 3 (semana 3):**
Winner geral vai pra escala. Gera 5 variações dele com `/hormozi-gtm:hooks --foco=<ângulo do winner>`.

---

## 🔄 Próximos passos

1. Filme/teste os 3 top primeiro
2. Se nenhum dos top 3 funcionar, prova que ICP ou oferta tem problema — rodar `/hormozi-gtm:audit`
3. Se algum funcionar, escalar variações com `--foco` no ângulo vencedor

---

*Hooks gerados pelo plugin hormozi-gtm. Persona Alex Hormozi aplicada. Humanizer (modo full) aplicado.*
