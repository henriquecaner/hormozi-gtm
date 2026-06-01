---
name: template-email-sequence
description: "Esqueleto interno do output do comando /hormozi-gtm:email. Carregado pelo comando, não para uso direto."
---

# Template — email-sequence.md

Esqueleto canônico do output de sequência de email. O comando `/hormozi-gtm:email` carrega esta skill e preenche o esqueleto abaixo com os inputs do usuário. Reproduza a estrutura exata: frontmatter + todas as seções + placeholders `{{...}}`.

```markdown
---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: email
tipo: {{cold | warm | nurture | re-engagement}}
version: 1
status: draft
created: {{ISO8601}}
client: {{empresa_slug}}
product: {{produto_slug}}
sequence_length: {{N}}
sequence_span_days: {{N}}
frameworks:
  - hook-framework
  - ad-copy-formula
  - value-equation
  - guarantees
humanizer_pass: true
humanizer_mode: full
audit_ref: {{caminho_ou_null}}
parent_version: {{caminho_v_anterior_ou_null}}
---

# Email Sequence — {{tipo}} para {{produto_nome}}

## TL;DR

**Tipo:** {{cold | warm | nurture | re-engagement}}
**Quantidade de emails:** {{N}}
**Duração da sequência:** {{N}} dias (de envio até breakup)
**ICP alvo:** {{descrição em 1 linha}}
**CTA primário ao longo da sequência:** {{ex: agendar 20min de auditoria gratuita}}

---

## Estratégia da sequência

**Ângulo principal:** {{dream outcome | dor | contrarian | secret}}
**Objeção que combatemos:** {{em 1 frase}}
**Por quê esse tipo (cold/warm/nurture/re-engagement) faz sentido aqui:** {{justificativa em 2-3 linhas}}

---

## Emails

### Email 1 — {{nome curto, ex: "Hook inicial"}}

**Subject:** {{linha curta, ≤ 50 chars, sem clickbait}}
**Timing:** Dia 0 (envio inicial)

**Body:**

> {{Linha de opener — referência específica ao prospect / dor reconhecível}}
>
> {{2-3 linhas de agitação: por que o problema custa}}
>
> {{1-2 linhas mostrando que você resolveu antes (proof curto)}}
>
> {{CTA específico — não "vamos conversar?", e sim "te mando PDF de 5 páginas, leva 10min de leitura"}}
>
> — {{nome}}

**Métrica esperada:** {{open rate alvo | reply rate alvo}}

---

### Email 2 — {{nome curto, ex: "Proof point"}}

**Subject:** {{linha curta}}
**Timing:** Dia {{N}} (+{{N}} dias)

**Body:**

> {{Referência ao email 1 — "ontem te mandei sobre X..."}}
>
> {{Case study específico: nome real (com permissão), contexto, antes/depois numérico}}
>
> {{Conexão com a dor do prospect — "se você está em situação parecida..."}}
>
> {{CTA: pode ser o mesmo do email 1 ou variar}}
>
> — {{nome}}

---

### Email 3 — {{nome curto, ex: "Reframe da objeção"}}

**Subject:** {{linha curta}}
**Timing:** Dia {{N}}

**Body:**

> {{Identifica a objeção comum: "A maioria que recebe esse email pensa que X..."}}
>
> {{Reframe em 2-3 linhas: "Mas o que vi nos últimos N clientes é Y..."}}
>
> {{Prova adicional: dado, número, caso}}
>
> {{CTA}}

---

### Email 4 — {{nome curto, ex: "Valor sem ask"}}

**Subject:** {{linha curta}}
**Timing:** Dia {{N}}

**Body:**

> {{Conteúdo educacional próprio — link pra post / vídeo / framework}}
>
> {{Por que esse conteúdo é relevante pro prospect}}
>
> {{Sem CTA de venda — só "achei que poderia interessar"}}

---

### Email 5 — {{Última tentativa | Soft pitch}}

**Subject:** {{linha curta — escassez genuína se aplicável}}
**Timing:** Dia {{N}}

**Body:**

> {{Recap rápido dos pontos dos emails anteriores}}
>
> {{Escassez ancorada em fato operacional (vaga, cohort, prazo real) — vide skill scarcity-urgency}}
>
> {{CTA final mais direto}}

---

### Email 6 — Breakup (opcional mas recomendado)

**Subject:** {{ex: "Encerrando follow-up — uma última pergunta"}}
**Timing:** Dia {{N}}

**Body:**

> {{Honestidade: "Vou parar de te escrever por enquanto. Antes disso, queria perguntar..."}}
>
> {{1 pergunta sincera — não pitch — pra entender por que não respondeu}}
>
> {{Deixa porta aberta sem implorar: "Se quiser retomar, é só responder este email."}}
>
> — {{nome}}

---

### Email 7 — Re-attempt (opcional, 6 semanas depois)

**Subject:** {{linha curta — ângulo NOVO}}
**Timing:** Dia {{N+45}}

**Body:**

> {{Reconhece que tentou antes — não esconde}}
>
> {{Novo ângulo (ângulo diferente do email 1) — algo que aconteceu desde então, novo case, nova feature do produto}}
>
> {{CTA leve}}

---

## Teste sugerido

**Sample mínimo:** 10-15 contatos por tipo (gera sinal estatístico básico)

**Métricas a monitorar:**
- **Cold:** reply rate (alvo: ≥ 5% pra prospects qualificados)
- **Warm:** click-to-call (alvo: ≥ 15%)
- **Nurture:** open rate por email + click rate no email 6-7 (CTA real)
- **Re-engagement:** % que respondem "sim, continua" no email 1

**Critério de iteração:**
- Reply rate < 3% → troca subject + opener do email 1.
- Open rate consistente < 30% → problema no subject ou domínio (reputação).
- Click sem reply → CTA não é forte o suficiente, refaz email 3-5.

---

## Anti-padrões

- Emails sem assinatura ou com assinatura corporativa pesada
- "Não respondo a emails de cold outreach" (passa por antispam)
- Múltiplos links no mesmo email (1 CTA, 1 link)
- Personalização rasa ("Olá {Nome}!") em vez de research real
- Sequência sem breakup — deixa lead morno indefinidamente

---

*Email sequence gerada pelo plugin hormozi-gtm. Persona Alex Hormozi aplicada. Humanizer (modo full) aplicado.*
```
