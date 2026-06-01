---
name: template-vsl
description: "Esqueleto interno do output VSL longo do comando /hormozi-gtm:roteiro. Carregado pelo comando, não para uso direto."
---

# Template — VSL longo (roteiro)

Esqueleto canônico do output VSL (8-15min) do comando `/hormozi-gtm:roteiro`. O comando carrega esta skill e preenche o esqueleto abaixo com os inputs do usuário. Reproduza a estrutura exata: frontmatter + todas as seções + placeholders `{{...}}`.

````markdown
---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: roteiro
formato: vsl
version: 1
status: draft
created: {{ISO8601}}
client: {{empresa_slug}}
product: {{produto_slug}}
duracao_alvo: 12min
plataforma: {{youtube | facebook | landing-page-embed}}
frameworks:
  - hook-framework
  - vsl-7-step
  - grand-slam-offer
  - ad-copy-formula
humanizer_pass: true
humanizer_mode: full
audit_ref: {{caminho_ou_null}}
parent_version: {{caminho_v_anterior_ou_null}}
---

# VSL — {{produto}}

## TL;DR

Duração: {{X}}min
Hook escolhido: {{tipo + frase}}
Mecanismo nomeado: {{Sistema X.Y.Z}}
CTA final: {{ação verbal específica}}

---

## ⏱ Timestamps

| Tempo | Ato | Conteúdo |
|---|---|---|
| 0:00-0:15 | Hook | {{frase hook}} |
| 0:15-2:00 | Story | {{origem ou case}} |
| 2:00-4:00 | Problem | {{3-5 sintomas + por que outras soluções falham}} |
| 4:00-7:00 | Mechanism | {{Sistema nomeado + 3-5 componentes}} |
| 7:00-9:00 | Proof | {{3-5 cases comparáveis com números}} |
| 9:00-11:00 | Offer | {{stack + preço + garantia + scarcity}} |
| 11:00-12:00 | CTA + Urgency | {{ação + razão de agir agora}} |

---

## 🎬 Roteiro completo

### Ato 1: Hook (0:00-0:15)

{{Frase de abertura com especificidade — não promete vazio. Tipo: dream/problem/secret}}

**Visual sugerido:** {{descrição rápida do enquadramento, prop, ambiente}}

---

### Ato 2: Story (0:15-2:00)

{{Narrativa pessoal ou de cliente. Conflito real, não vitória fácil. 2-3 parágrafos. Especificidade numérica.}}

**Pontos de tensão:**
- {{momento 1 — quando errou ou descobriu}}
- {{momento 2}}
- {{momento 3 — virada}}

---

### Ato 3: Problem (2:00-4:00)

{{Diagnóstico do problema que o cliente reconhece com precisão dolorida.}}

**Sintomas concretos do problema:**
1. {{sintoma específico do ICP}}
2. {{sintoma}}
3. {{sintoma}}

**Por que outras soluções falham:**
{{2-3 parágrafos quebrando alternativas comuns com diagnóstico contraintuitivo}}

**Custo real de não resolver:**
{{Quantificado em R$, tempo ou oportunidade}}

---

### Ato 4: Mechanism (4:00-7:00)

**Apresentando: {{Nome do Sistema/Método}}**

{{1 parágrafo introduzindo o nome próprio + por que esse nome}}

**Os {{N}} componentes:**

1. **{{Componente 1 — letra/nome}}** — {{explicação em 2-3 linhas}}
2. **{{Componente 2}}** — {{explicação}}
3. **{{Componente 3}}** — {{explicação}}
4. **{{Componente 4 — opcional}}** — {{explicação}}

**Insight contraintuitivo:**
{{Algo que parece errado mas funciona — peça central da revelação}}

---

### Ato 5: Proof (7:00-9:00)

**Case 1: {{Cliente — nome + papel + empresa, se possível}}**
{{Antes/Depois numérico. 1 parágrafo.}}

**Case 2: {{Cliente}}**
{{Antes/Depois numérico. 1 parágrafo.}}

**Case 3: {{Cliente}}**
{{Antes/Depois numérico. 1 parágrafo.}}

**Sumário de proof:** {{frase resumindo "X clientes, Y resultado médio, em Z tempo"}}

---

### Ato 6: Offer (9:00-11:00)

**O que você recebe se entrar agora:**

- {{Deliverable 1 — nome próprio + valor}}
- {{Deliverable 2}}
- {{Deliverable 3}}
- Bônus #1: {{nome + valor R$}}
- Bônus #2: {{nome + valor R$}}
- Bônus #3: {{nome + valor R$}}

**Valor total: R$ {{X}}**
**Seu investimento hoje: R$ {{Y}}**

**Garantia: {{Nome da Garantia}}**
{{1-2 frases explicando: condição, tempo, compensação}}

**Vagas: {{X de Y}}**
{{Razão genuína de escassez}}

---

### Ato 7: CTA + Urgency (11:00-12:00)

{{Recap em 30s do que o leitor está prestes a perder se não agir}}

**{{Ação verbal específica — ex: "Clica no link abaixo e responde 3 perguntas"}}**

{{O que acontece depois — "Eu vejo sua aplicação, respondo em 24h, te marco uma call de 15min"}}

**Razão de agir agora:**
{{Deadline real, próxima turma, fast-action bonus}}

---

## 🎥 Notas de produção

- **Tom:** {{conversacional | direto-câmera | story-driven}}
- **B-roll sugerido:** {{lista de cuts visuais por ato}}
- **Texto on-screen:** {{frases-chave a destacar visualmente}}
- **CTA on-screen:** persistente nos últimos 60s
- **Música:** {{none | sutil | dinâmica}}

---

## 📊 Pós-publicação

**Métricas a monitorar:**
- Retention curve (pontos onde audience cai)
- CTR do CTA
- Conversion rate na LP destino
- Cost per acquisition (se rodando em paid)

**Próximos passos recomendados após publicar:**
1. Gerar 5-10 short-form variants do mesmo material (`/hormozi-gtm:roteiro --formato=reels`)
2. Gerar batch de hooks pra testar primeiros 3s (`/hormozi-gtm:hooks`)

---

*VSL gerado pelo plugin hormozi-gtm. Persona Alex Hormozi aplicada. Humanizer (modo full) aplicado.*
````
