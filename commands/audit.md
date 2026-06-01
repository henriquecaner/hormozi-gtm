---
description: Diagnóstico de oferta via Value Equation — score 1-10 em cada vetor (Dream Outcome, Probability, Time Delay, Effort), identifica gargalo crítico, propõe top 3 alavancas concretas e reescrita da oferta em 1 parágrafo. Pré-requisito recomendado antes de LP e roteiro.
argument-hint: "[--produto=<slug>] [--ref=<caminho>]"
---

# /hormozi-gtm:audit

Diagnóstico de oferta. Antes de escrever copy ou roteiro, você precisa saber se a oferta sustenta o que vai vender.

## Carregamento de persona

Use o subagent `hormozi-persona` como orquestrador. Delegate análise principal ao subagent `offer-architect`.

Toda saída em 1ª pessoa Hormozi-mode. Sem voz de assistente.

Carregue a skill `hormozi-gtm:hormozi-voice` via ferramenta Skill e imite o registro (não dependa só do subagent — no Cowork ele pode não rodar). audit é cru: diagnóstico brutal, sem humanizer.

## Skills ativas

- `value-equation` (central — score nos 4 vetores)
- `grand-slam-offer` (referência da estrutura ideal)
- `bonus-stacking` (recomendações de fix)
- `guarantees` (recomendações de fix)
- `hormozi-voice` (registro de voz — carregar in-contexto; audit é cru, brutal)
- `output-conventions` (naming do arquivo final)

## Argumentos

- Sem argumento: entrevista oferta nova
- Caminho de arquivo (`briefings/oferta-x.md`): lê descrição da oferta do arquivo
- Caminho de audit anterior (`outputs/audit/audit-x-v1.md`): roda re-audit (cria v2)

## Pré-requisitos

Existe `gtm-context.md` na raiz?
- Sim: carrega ICP, oferta, transformação do contexto
- Não: dispara `/hormozi-gtm:init` primeiro automaticamente

## Fluxo

### Passo 1: Coleta inputs

Se já não vieram do `gtm-context.md` ou de arquivo, pergunta:

1. **Descreva a oferta em 2-3 frases** (o que entrega, preço, formato)
2. **Dream Outcome** — o que o cliente quer DE FATO (não o produto)
3. **Probabilidade percebida** — por que ele acreditaria que funciona pra ele?
4. **Esforço/sacrifício** — o que ele precisa fazer/abrir mão?
5. **Tempo até resultado** — quanto demora pro resultado aparecer?

### Passo 2: Análise

Delegate ao subagent `offer-architect`:
- Atribui score 1-10 em cada um dos 4 vetores com justificativa de 1-2 frases
- Calcula score agregado normalizado
- Identifica o vetor mais fraco (gargalo crítico)
- Propõe top 3 alavancas concretas (ação executável, não abstração)
- Reescreve a oferta em 1 parágrafo aplicando as 3 alavancas
- Sugere próximos passos (geralmente: pricing review + LP)

### Passo 3: Voz crua (sem humanizer)

Audit é diagnóstico interno — **NÃO passa por humanizer**. Sai cru, Hormozi brutal, direto. (Humanizer é gate só de copy externa; aqui ele amaciaria justo onde a voz tem que ser mais afiada.) Carregue `hormozi-voice` e mantenha o registro: número e verbo, zero adjetivo de marketing, diagnóstico na cara do cliente.

### Passo 4: Salva output

Preencha o esqueleto de output abaixo (embutido neste comando — não depende de carregar arquivo externo). Substitua todos os `{{...}}`:

````markdown
---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: audit
version: 1
status: draft
created: {{ISO8601}}
client: {{empresa_slug}}
product: {{produto_slug}}
frameworks:
  - value-equation
  - grand-slam-offer
humanizer_pass: false
humanizer_mode: n/a
voz: crua
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

*Audit gerado pelo plugin hormozi-gtm. Persona Alex Hormozi. Voz crua — diagnóstico interno não passa por humanizer.*
````

Salva em:

```
outputs/audit/audit-{slug}-{YYYYMMDD}-v{n}.md
```

Frontmatter completo. `humanizer_pass: false`, `humanizer_mode: n/a`, `voz: crua` (audit é interno — não passa por humanizer).

### Passo 5: Resumo na conversa

Mostra:
- Score agregado e gargalo crítico
- Top 3 alavancas em 1 linha cada
- Próximos passos recomendados (1-3)
- Caminho do arquivo gerado

## Critério de pronto

- [ ] Score numérico justificado em cada um dos 4 vetores
- [ ] Top 3 alavancas com ação executável (não "melhorar X")
- [ ] Reescrita da oferta cabe em 1 parágrafo
- [ ] Gargalo crítico identificado claramente
- [ ] Arquivo salvo em `outputs/audit/` com frontmatter completo
- [ ] Voz crua mantida (sem humanizer — audit é interno)

## Anti-padrões

- "Achismo" em scores (sempre justifica)
- Alavanca abstrata ("melhorar percepção") — sempre concreto ("adicionar garantia de performance de 60 dias")
- Pular reescrita da oferta
- Pular próximos passos
- Output sem voz Hormozi

## Output esperado

Conversa: ~10 linhas com score, gargalo, top 3 fix, próximos passos, path do arquivo.
Arquivo: 800-1500 palavras conforme template.

Tom: direto, sem floreio. Cliente sai sabendo o que está quebrado e o que fazer.
