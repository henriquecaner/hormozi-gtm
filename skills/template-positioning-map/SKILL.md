---
name: template-positioning-map
description: "Esqueleto interno do output do comando /hormozi-gtm:positioning. Carregado pelo comando, não para uso direto."
---

# Template — positioning map

Esqueleto canônico do positioning map gerado por `/hormozi-gtm:positioning`. O comando carrega esta skill e preenche o esqueleto abaixo com os inputs do usuário e a análise competitiva. Reproduza a estrutura exata: frontmatter + todas as seções + placeholders `{{...}}`. Output interno (diagnóstico competitivo) — voz crua, sem humanizer.

```markdown
---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: positioning
version: 1
status: draft
created: {{ISO8601}}
client: {{empresa_slug}}
product: {{produto_slug}}
competidores_mapeados: {{N}}
frameworks:
  - value-equation
  - grand-slam-offer
  - pricing-playbook
  - niche-selection
humanizer_pass: false
humanizer_mode: n/a
voz: crua
audit_ref: {{caminho_ou_null}}
parent_version: {{caminho_v_anterior_ou_null}}
---

# Positioning Map — {{produto_nome}}

## Positioning statement

> "{{Frase exata. Para [ICP específico], [empresa] é a única que [unique value] sem [trade-off comum].}}"

**Eixo único defendido:** {{1 linha — ex: "Velocidade de implementação (5 dias vs 3-6 semanas do mercado)"}}

**Sustentação:** {{1 linha — case real ou razão estrutural — ex: "3 cases documentados (Stark, Cora, Pix Bank) + framework de onboarding em 4 sessions"}}

---

## 1. Competitive Map

| Competidor | Posicionamento declarado | Preço | ICP primário | Mensagem chave | Força | Fraqueza |
|---|---|---|---|---|---|---|
| {{A}} | {{...}} | R$ {{...}} | {{...}} | "{{tagline}}" | {{...}} | {{...}} |
| {{B}} | {{...}} | R$ {{...}} | {{...}} | "{{tagline}}" | {{...}} | {{...}} |
| {{C}} (premium) | {{...}} | R$ {{...}} | {{...}} | "{{tagline}}" | {{...}} | {{...}} |
| {{D}} (barato) | {{...}} | R$ {{...}} | {{...}} | "{{tagline}}" | {{...}} | {{...}} |
| Substituto não-óbvio: {{ex: "fazer interno"}} | n/a | R$ {{custo time interno}} | {{...}} | n/a | Controle | Velocidade |

---

## 2. Sua posição

| Dimensão | Você |
|---|---|
| Posicionamento | {{1 linha}} |
| Preço | R$ {{...}} |
| ICP primário | {{específico}} |
| Mensagem chave | "{{tagline}}" |

---

## 3. Eixos de diferenciação (defensáveis com fato)

### Eixo 1: {{ex: Velocidade de implementação}}

**Status no mercado:**
- A: {{4-6 semanas}}
- B: {{3-4 semanas}}
- C: {{2-3 semanas}}
- **Você:** {{5 dias}}

**Sustentação:** {{Case story ou razão estrutural. Ex: "3 cases documentados (Stark, Cora, Pix Bank) onde implementação foi em 5 dias. Razão: framework de onboarding em 4 sessions vs 12 da maioria."}}

**Como comunicar:** {{Frase punchy para hero copy. Ex: "Funcionando em 5 dias, não 5 semanas."}}

---

### Eixo 2: {{ex: Specificidade do nicho}}

**Status no mercado:**
- A: {{atende SaaS B2B geral}}
- B: {{atende qualquer B2B}}
- **Você:** {{SaaS B2B fintech com ciclo > 60 dias}}

**Sustentação:** {{12 dos últimos 14 clientes são SaaS B2B fintech. Founder-market fit nativo.}}

**Como comunicar:** {{"Único framework feito especificamente para fintech B2B com ciclo > 60 dias."}}

---

### Eixo 3: {{ex: Garantia condicional}}

**Status no mercado:**
- A: garantia "satisfação ou dinheiro de volta" (genérica)
- B: sem garantia
- C: garantia limitada a 14 dias

**Você:** "90 dias com ciclo reduzido em 40% ou devolvemos investimento + R$ 10k bonus."

**Sustentação:** {{Único player no nicho a oferecer garantia condicional com compensação acima do reembolso.}}

**Como comunicar:** {{"A única consultoria que paga pra você se não funcionar."}}

---

## 4. Trade-offs explícitos

Posicionamento defensável precisa dizer **o que você não é**. Cliente sabe que escolheu o trade-off certo:

- **Você NÃO é:** {{ex: "consultoria broad de growth — não atendemos B2C, e-commerce, ou SaaS B2C"}}
- **Você NÃO promete:** {{ex: "transformação cultural — focamos em métricas operacionais de venda"}}
- **Quem deve escolher outro:** {{ex: "founders pré-PMF sem dados de vendas; cliente que precisa fazer M&A"}}

---

## 5. Derivados de copy

### Hero copy (LP) — 3 variações

**Variação 1 (foco em velocidade):**
> "{{frase punchy de 6-10 palavras}}"
> "{{subtítulo de 15-25 palavras com prova}}"

**Variação 2 (foco em specificity):**
> "{{frase punchy}}"
> "{{subtítulo}}"

**Variação 3 (foco em garantia):**
> "{{frase punchy}}"
> "{{subtítulo}}"

### Cold email subject — 3 variações

1. "{{subject específico, ≤ 50 chars}}"
2. "{{subject 2}}"
3. "{{subject 3}}"

### LinkedIn bio (1)

> "{{1-3 linhas. Tom direto. Inclui ICP + value único + proof}}"

### Frase de abertura de sales call

> "{{2-3 frases. Não 'me apresento'. Algo que estabelece autoridade + cria curiosity gap nos primeiros 30s da call.}}"

---

## 6. Plano de teste

Como validar que o positioning funciona:

**Semana 1-2:** ad com 3 hero copy variações (R$ 200 cada). Mede CTR.
**Semana 3:** vencedor vira headline na LP. Mede conversão LP.
**Semana 4-5:** vencedor vira cold email subject. Mede reply rate.
**Critério:** positioning é considerado validado se CTR e reply rate sobem ≥ 25% vs baseline anterior.

---

*Positioning map gerado pelo plugin hormozi-gtm. Persona Alex Hormozi aplicada. Voz crua — diagnóstico competitivo interno não passa por humanizer.*
```
