---
name: template-plano
description: "Esqueleto interno do output do comando /hormozi-gtm:plano. Carregado pelo comando, não para uso direto."
---

# Template — plano (business plan)

Esqueleto canônico do business plan gerado por `/hormozi-gtm:plano`. O comando carrega esta skill e preenche o esqueleto abaixo com os inputs do usuário e os cálculos de unit economics. Reproduza a estrutura exata: frontmatter + as 10 seções + placeholders `{{...}}`. Output interno — voz crua, sem humanizer.

````markdown
---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: plano
tipo: {{empresa | produto}}
version: 1
status: draft
created: {{ISO8601}}
client: {{empresa_slug}}
product: {{produto_slug}}
frameworks:
  - grand-slam-offer
  - value-equation
  - core-four
  - money-models
  - ltv-cac
  - pricing-playbook
  - leila-scaling
humanizer_pass: false
humanizer_mode: n/a
voz: crua
audit_ref: {{caminho_ou_null}}
pricing_ref: {{caminho_ou_null}}
---

# Business Plan — {{empresa | produto}}

## 1. Sumário executivo

{{1 página: o que é, pra quem, modelo de receita, meta 12 meses, maior risco}}

**Em 1 frase:** {{empresa/produto resolve X para Y via Z, gerando R$ N de ARR}}

---

## 2. Mercado e ICP

### Categoria
{{1 frase definindo mercado primário}}

### Tamanho de mercado (TAM/SAM/SOM)
- **TAM** (total addressable): {{R$ X e N empresas/usuários}}
- **SAM** (serviceable available): {{recorte realista}}
- **SOM** (serviceable obtainable): {{1-3 anos}}

### ICP detalhado

**Quem:**
- Função: {{cargo/persona}}
- Empresa: {{tamanho, setor, geografia}}
- Stage: {{onde está na jornada}}

**Dor primária:**
{{1 frase com a dor que justifica gastar R$ alto}}

**Anti-ICP:**
{{quem você NÃO atende}}

---

## 3. Oferta (Grand Slam)

### Core offer
**Nome:** {{nome próprio da oferta}}

**Transformação prometida** (em quanto tempo, quem vira o quê):
{{frase específica e quantificada}}

**O que está incluído:**
- {{deliverable 1 nomeado}}
- {{deliverable 2}}
- {{deliverable 3}}

**Bonuses (stack ímpar):**
- {{bonus 1 — valor R$}}
- {{bonus 2 — valor R$}}
- {{bonus 3 — valor R$}}

**Garantia:**
{{condicional + métrica + compensação}}

**Preço:**
- Tier base: R$ {{X}}
- Tier default (gold): R$ {{Y}}
- Tier premium (platinum): R$ {{Z}}

---

## 4. Money Model (4 níveis)

### Nível 1: Attraction Offer
- **Formato:** {{lead magnet gratuito | tripwire R$ X}}
- **CPL alvo:** R$ {{X}}
- **Funcao:** {{...}}

### Nível 2: Core Offer
- **Preço:** R$ {{X}}
- **Conversion rate alvo:** {{X}}%
- **AOV esperado:** R$ {{X}}
- **Margem gross alvo:** {{X}}%

### Nível 3: Upsell
- **Formato:** {{order bump | OTO | upsell page}}
- **Preço:** R$ {{X}}
- **Take rate alvo:** {{X}}% (20-40%)
- **Função:** absorver CAC em 30 dias (Client-Financed Acquisition)

### Nível 4: Continuity / Downsell

**Continuity:**
- **Formato:** {{...}}
- **Preço:** R$ {{X}}/mês
- **Upgrade rate alvo:** {{X}}%
- **Churn target:** <{{X}}%/mês

**Downsell:**
- **Formato:** {{...}}
- **Preço:** R$ {{X}}
- **Take rate alvo:** {{X}}% dos no-buys

---

## 5. Pricing e unit economics

### LTV / LTGP
```
Preço médio composto: R$ {{X}}
Custo variável médio: R$ {{Y}}
Retenção média: {{N}} meses
LTGP = (R$ {{X}} - R$ {{Y}}) × {{N}} = R$ {{Z}}
```

### CAC
- **CAC atual:** R$ {{X}}
- **CAC alvo escalando paid:** R$ {{X}}

### Ratio + Payback
- **LTGP : CAC:** {{X}}:1 (alvo ≥3:1)
- **Payback period:** {{N}} dias (alvo ≤30)

### 5 leis do Pricing Playbook (aplicadas)
1. **Compete em valor:** {{como}}
2. **Cobra o que vale:** {{justificativa do preço}}
3. **Preço sinaliza qualidade:** {{posicionamento de preço vs mercado}}
4. **Tiering:** {{estrutura silver/gold/platinum}}
5. **Runway maior, ask maior:** {{como aplicado}}

---

## 6. Aquisição (Core Four)

### Mix por canal (% budget/tempo)

| Canal | % | Ativo desde | Métrica primária |
|---|---|---|---|
| Warm | {{X}}% | {{quando}} | {{conversion rate lead→call}} |
| Cold | {{X}}% | {{quando}} | {{reply rate}} |
| Organic content | {{X}}% | {{quando}} | {{leads/mês}} |
| Paid ads | {{X}}% | {{quando}} | {{LTGP:CAC ratio}} |

### Cadência e equipe

| Canal | Cadência | Responsável | Budget mensal |
|---|---|---|---|
| Warm | {{N contatos/dia}} | {{papel}} | R$ {{...}} |
| Cold | {{N contatos/dia}} | {{papel}} | R$ {{...}} |
| Organic | {{N posts/semana}} | {{papel}} | R$ {{...}} |
| Paid | continuous | {{papel}} | R$ {{...}} |

### Roadmap de aquisição (3 trimestres)

**Q1:** {{...}}
**Q2:** {{...}}
**Q3:** {{...}}

---

## 7. Operação (Leila Scaling Frameworks)

### 5 Star Service
- **Concern:** {{como demonstra}}
- **Courtesy:** {{SOP}}
- **One-Done:** {{política de resolução em 1 ida-e-volta}}
- **Consistency:** {{como mantém padrão}}
- **Compensation:** {{política de erro}}

### High-Performance Communication
{{Como é treinado/aplicado no time de sales/CS}}

### Hiring & Onboarding
- **Primeira contratação chave:** {{cargo}}
- **Onboarding** (primeiros 30 dias): {{...}}

### Delegação (75% rule)
{{O que você delega quando atinge 75% quality}}

### Métricas e accountability

| Função | Métrica primária | Cadência review | Owner |
|---|---|---|---|
| {{...}} | {{...}} | semanal | {{...}} |
| {{...}} | {{...}} | mensal | {{...}} |

---

## 8. Métricas-chave e cadência

### North Star Metric
{{1 número que resume saúde do negócio}}

### Dashboard semanal
- Novos leads
- Conversion rate lead→call
- Conversion rate call→close
- AOV
- MRR / ARR
- Churn

### Dashboard mensal
- LTGP:CAC ratio
- Payback period
- Margem gross
- Burn rate (se aplicável)
- NPS (se aplicável)

---

## 9. Riscos e premissas

### Premissas-chave do plano
1. {{premissa 1 — ex: "Conversion rate em paid se mantém em X% ao escalar 5x"}}
2. {{premissa 2}}
3. {{premissa 3}}

### Riscos

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| {{risco 1}} | alta/média/baixa | alto/médio/baixo | {{ação}} |
| {{risco 2}} | | | |
| {{risco 3}} | | | |

---

## 10. Roadmap 30-60-90

### Primeiros 30 dias
- [ ] {{ação 1 — validação de oferta}}
- [ ] {{ação 2 — primeiros 5-10 clientes}}
- [ ] {{ação 3 — KPI setup}}

### Dias 31-60
- [ ] {{ação 1 — escalar canal validado}}
- [ ] {{ação 2 — primeira contratação}}
- [ ] {{ação 3 — refinar oferta com data}}

### Dias 61-90
- [ ] {{ação 1 — adicionar 2º canal}}
- [ ] {{ação 2 — SOPs documentados}}
- [ ] {{ação 3 — quebra de meta intermediária}}

---

## Meta 12 meses

- **Receita (ARR):** R$ {{X}}
- **Clientes ativos:** {{N}}
- **Margem gross:** {{X}}%
- **Team size:** {{N}}
- **Maior mudança esperada:** {{...}}

---

*Plano gerado pelo plugin hormozi-gtm. Persona Alex Hormozi aplicada. Voz crua — documento operacional interno não passa por humanizer.*
````
