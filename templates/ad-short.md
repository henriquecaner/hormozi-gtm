---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: roteiro
formato: short
version: 1
status: draft
created: {{ISO8601}}
client: {{empresa_slug}}
product: {{produto_slug}}
quantidade_variantes: {{N}}
plataforma_principal: {{reels | tiktok | shorts}}
frameworks:
  - hook-framework
  - ad-copy-formula
humanizer_pass: true
humanizer_mode: full
audit_ref: {{caminho_ou_null}}
---

# Roteiro Short-Form (batch) — {{produto}}

## TL;DR

{{N}} variantes geradas, cobrindo {{X}} ângulos (dor/desejo/curiosidade/contrarian/prova).
Duração por variante: 15-60s (versões curta e longa de cada).
Top 3 do agent: {{listados ao final}}

---

## Variantes

### Variante 1 — Ângulo: {{dor | desejo | curiosidade | contrarian | prova}}

**Hook (0-3s):**
{{frase de impacto — testável isoladamente como tweet}}

**Versão 30s:**

```
[0-3s] HOOK
{{visual: enquadramento, ação}}
"{{fala literal}}"

[3-20s] TENSÃO
{{visual}}
"{{fala}}"

[20-25s] PAYOFF
{{visual}}
"{{fala}}"

[25-30s] CTA
{{visual}}
"{{ação verbal específica}}"
```

**Versão 60s (expandida):**

```
[0-3s] HOOK
[3-15s] CONTEXTO
[15-40s] DESENVOLVIMENTO (mechanism + 1 case curto)
[40-55s] PAYOFF + OFERTA
[55-60s] CTA
```

**Texto on-screen:**
- {{frase 1}}
- {{frase 2}}
- {{CTA}}

**Música/áudio:** {{sugestão}}

---

### Variante 2 — Ângulo: {{...}}

{{Repetir estrutura acima}}

---

### Variante 3 — Ângulo: {{...}}

{{...}}

---

### Variante 4 — Ângulo: {{...}}

{{...}}

---

### Variante 5 — Ângulo: {{...}}

{{...}}

---

### Variante 6 — Ângulo: {{...}}

{{...}}

---

## 🏆 Top 3 do agent

### 🥇 Variante {{#}} — {{nome curto}}
**Por que:** {{justificativa específica — ex: "hook tem especificidade numérica + reframe contraintuitivo. Tem maior chance de stop scroll"}}

### 🥈 Variante {{#}} — {{nome curto}}
**Por que:** {{justificativa}}

### 🥉 Variante {{#}} — {{nome curto}}
**Por que:** {{justificativa}}

---

## ✅ Teste de qualidade aplicado

Para cada variante:
- [x] Funciona muted com legenda? (legendas substituem áudio)
- [x] Hook lê isoladamente como tweet?
- [x] CTA tem ação verbal específica (não "saiba mais")?
- [x] Sem promessa vazia
- [x] Mechanism nomeado quando aplicável

---

## 📊 Sequenciamento sugerido pra teste

**Dia 1-3:** rodar variantes 1, 2, 3 com mesmo budget
**Dia 4-7:** rodar variantes 4, 5, 6 com mesmo budget
**Dia 8:** consolidar resultados. Top 2 escalam, resto mata.

**Métrica primária:** custo por LP visit
**Métrica secundária:** retention curve nos primeiros 3s

---

## 🔄 Próximos passos

1. Filmar primeiro hook das 3 variantes top antes do resto (testa só com hook gravado, se 0% retention já mata)
2. Variar visual mantendo copy quando 2+ variantes performam similar
3. Refinar com `/hormozi-gtm:hooks --foco=variante_winner` se quiser mais variantes do ângulo vencedor

---

*Batch gerado pelo plugin hormozi-gtm. Persona Alex Hormozi aplicada. Humanizer (modo full) aplicado.*
