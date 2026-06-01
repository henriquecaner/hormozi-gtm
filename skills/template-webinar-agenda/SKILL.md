---
name: template-webinar-agenda
description: "Esqueleto interno do output do comando /hormozi-gtm:webinar. Carregado pelo comando, não para uso direto."
---

# Template — webinar-agenda.md

Esqueleto canônico do output de webinar. O comando `/hormozi-gtm:webinar` carrega esta skill e preenche o esqueleto abaixo com os inputs do usuário. Reproduza a estrutura exata: frontmatter + todos os blocos + placeholders `{{...}}`.

````markdown
---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: webinar
version: 1
status: draft
created: {{ISO8601}}
client: {{empresa_slug}}
product: {{produto_slug}}
duracao_min: {{30 | 45 | 60}}
formato: {{zoom | youtube | prerecorded}}
frameworks:
  - hook-framework
  - vsl-7-step
  - grand-slam-offer
  - value-equation
  - guarantees
humanizer_pass: true
humanizer_mode: full
audit_ref: {{caminho_ou_null}}
parent_version: {{caminho_v_anterior_ou_null}}
---

# Webinar — {{produto_nome}}

## Visão geral

**Título do webinar:** {{título punchy, ≤ 60 chars}}
**Subtítulo / promessa:** {{1 linha com Dream Outcome específico}}
**Duração planejada:** {{N}} min
**Formato:** {{zoom (live) | youtube | prerecorded}}
**ICP alvo:** {{descrição em 1 linha}}
**CTA primário:** {{ex: "agendar 30min de auditoria estratégica"}}

---

## Agenda — bloco a bloco

| Bloco | Tempo | Tópico | Função |
|---|---|---|---|
| 1. Abertura + housekeeping | 0:00-0:03 | Hook + agenda + Q&A rules | Captura atenção, define expectativa |
| 2. Diagnóstico do problema | 0:03-0:11 | Como aparece, custo, por que ninguém resolve | Estabelece dor + autoridade |
| 3. Mechanism nomeado | 0:11-0:23 | Framework signature + 4-6 componentes | Ensina, vira referência |
| 4. Cases | 0:23-0:31 | 2-3 antes/depois numérico | Proof de Probability |
| 5. Oferta + bonuses + garantia | 0:31-0:38 | Grand Slam + tier visual + escassez | Vende |
| 6. Q&A | 0:38-0:43 | Live (real) ou simulado (prerecorded) | Quebra objeção, reforça autoridade |
| 7. Fechamento + CTA | 0:43-0:45 | Direção final + próximos passos | Move ação |

(Ajusta proporcionalmente para 30min ou 60min.)

---

## Bloco 1 — Abertura (0:00-0:03)

### Hook (primeiros 30 segundos — crítico)

> "{{Hook escrito por extenso. Voz Hormozi 1ª pessoa. Passa tweet-test: lê isolado e gera curiosity gap. Ex: 'Os 7 SaaS B2B que escalam de R$ 5M para R$ 50M ARR no Brasil têm uma coisa em comum que ninguém comenta. E não é founder, não é capital, não é product-market fit.'}}"

### Agenda anunciada

> "Nos próximos {{N}} minutos vamos cobrir 4 coisas:
> 1. {{tópico 1}}
> 2. {{tópico 2}}
> 3. {{tópico 3}}
> 4. {{tópico 4}}
>
> No final, abro Q&A por {{N}} minutos."

### Housekeeping (Q&A)

> "{{Regra de Q&A — ex: 'Manda pergunta no chat a qualquer momento, respondo as melhores no final. Quem precisar sair antes, gravação fica disponível em 24h.'}}"

---

## Bloco 2 — Diagnóstico (0:03-0:11)

### Como o problema aparece

{{2-3 parágrafos descrevendo o problema do ponto de vista do ICP. Não "teoria" — sintomas concretos. Ex:}}

> "Você roda Meta Ads R$ 30k/mês, gera 200 leads qualificados, mas o ciclo de venda B2B trava em 75 dias. Time de SDR adicionou 2 pessoas, conversão por SDR caiu pela metade. Cliente assina, mas demora 90 dias pra fazer onboarding completo. Cada mês desses custa R$ 80k em CAC sem retorno."

### Custo do problema

> "{{Quantifica. Não 'caro'. R$ X por mês de oportunidade perdida + Y de overhead + Z de moral do time.}}"

### Por que ninguém resolve

> "{{Reframe contrarian. Ex: 'A maioria dos consultores ataca isso como problema de copy de sales page. Não é. Copy não muda comitê de compra B2B. O que muda é o framework de comunicação aplicado no SDR antes de o lead chegar na sales call.'}}"

---

## Bloco 3 — Mechanism nomeado (0:11-0:23)

### Nome do framework

**{{Nome próprio do framework}}**

> {{1 frase definindo o que é}}

### Os {{N}} componentes

**Componente 1: {{Nome}}**
- {{1-2 parágrafos explicando}}
- Por que importa: {{em 1 linha}}

**Componente 2: {{Nome}}**
- {{descrição}}

**Componente 3: {{Nome}}**
- {{descrição}}

**Componente 4: {{Nome}}**
- {{descrição}}

(Mantém 4-6 componentes — mais é confuso, menos é raso.)

---

## Bloco 4 — Cases (0:23-0:31)

### Case 1: {{Cliente}}

- **De:** {{antes em 1 linha}}
- **Para:** {{depois em 1 linha}}
- **Em:** {{tempo}}
- **Mechanism aplicado:** {{componentes 1, 2}}
- **Quote:** "{{frase do cliente}}"

### Case 2: {{Cliente}}

[mesma estrutura]

### Case 3: {{Cliente, opcional}}

[mesma estrutura]

---

## Bloco 5 — Oferta + Bonuses + Garantia (0:31-0:38)

### A oferta — {{Nome próprio da oferta}}

**O que você ganha:**
- {{deliverable 1 nomeado}}
- {{deliverable 2}}
- {{deliverable 3}}

**Em quanto tempo:** {{prazo específico}}

### Bonus stack (3-5, ímpar)

- **{{Bonus 1 — nome via naming psychology}}** (R$ {{valor}})
- **{{Bonus 2}}** (R$ {{valor}})
- **{{Bonus 3}}** (R$ {{valor}})

(Valor total da stack: R$ {{X}})

### Garantia

> "{{Condicional + métrica + compensação. Ex: 'Em 90 dias você tem ciclo de venda B2B reduzido em 40% ou devolvemos o investimento + R$ 10.000 de bonus.'}}"

### Investimento

**Tier default (Gold):** R$ {{Y}}/mês ou R$ {{N×Y com desconto}}/ano à vista.

Mostra os 3 tiers visualmente (Silver / Gold com destaque / Platinum).

### Escassez genuína

> "{{Razão operacional do limite. Ex: 'Próxima turma começa em 12 de agosto. Tenho 6 vagas para manter o framework de 1 hora por cliente por semana.'}}"

---

## Bloco 6 — Q&A (0:38-0:43)

### Plant questions (live) ou Scripted Q&A (prerecorded)

**Pergunta 1:** {{objeção comum 1}}
> Resposta: {{2-3 frases. Voz Hormozi. Reframe.}}

**Pergunta 2:** {{objeção comum 2}}
> Resposta: {{...}}

**Pergunta 3:** {{objeção comum 3}}
> Resposta: {{...}}

**Pergunta 4:** {{objeção sobre preço}}
> Resposta: {{...}}

**Pergunta 5:** {{objeção sobre timing}}
> Resposta: {{...}}

---

## Bloco 7 — Fechamento + CTA (0:43-0:45)

### Recap (30 segundos)

> "{{Resumo em 2-3 frases: o problema, o mechanism, a oferta.}}"

### CTA específico

> "{{Direção exata. Não 'visite o site'. Algo como: 'Clica no link no chat. Você vai pra uma página com 5 minutos de aplicação. Quem aplicar nas próximas 48h, vejo individualmente e respondo se faz fit.'}}"

### Próximos passos

> "{{Confirma timing: 'Aplicação aberta até [data]. Quem aplicar nessa janela, recebe resposta em até 72h.'}}"

---

## Notas de produção

### Slides (sugestões)

- Slide 1 (Hook): texto grande, sem decoração. 1 sentence.
- Slides 2-4 (Diagnóstico): 1 sintoma por slide, com número.
- Slides 5-10 (Mechanism): 1 componente por slide + ícone.
- Slides 11-13 (Cases): 1 case por slide, antes/depois grande.
- Slide 14-15 (Oferta): visual de tiering Silver/Gold/Platinum.
- Slide 16 (Garantia): destaque visual.
- Slide 17 (CTA): URL grande + QR code.

### Equipamento mínimo (live)

- Câmera 1080p (smartphone moderno serve).
- Microfone external (não built-in laptop).
- Background neutro ou marca.
- Iluminação frontal (key light).
- Internet ≥ 50 Mbps.

### Para prerecorded

- 3 takes mínimo por bloco.
- Edição em ferramenta simples (Descript, Riverside).
- Adicionar pattern interrupts (zoom in, cut to b-roll) a cada 90 segundos.

---

*Webinar gerado pelo plugin hormozi-gtm. Persona Alex Hormozi aplicada. Humanizer (modo full) aplicado.*
````
