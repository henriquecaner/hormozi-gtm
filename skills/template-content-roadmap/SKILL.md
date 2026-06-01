---
name: template-content-roadmap
description: "Esqueleto interno do output do comando /hormozi-gtm:content-hub. Carregado pelo comando, não para uso direto."
---

# Template — content-roadmap.md

Esqueleto canônico do output do comando `/hormozi-gtm:content-hub`. O comando carrega esta skill e preenche o esqueleto abaixo com os inputs do usuário. Reproduza a estrutura exata: frontmatter + todas as seções + placeholders `{{...}}`.

O roadmap é diagnóstico/estratégia interna — sai cru, sem humanizer. O frontmatter já carrega `humanizer_pass: false`, `humanizer_mode: n/a`, `voz: crua`. (As peças de conteúdo produzidas DEPOIS, a partir deste roadmap, são copy externa e passam por humanizer full na hora de produzir.)

```markdown
---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: content-hub
version: 1
status: draft
created: {{ISO8601}}
client: {{empresa_slug}}
product: {{produto_slug}}
duracao_dias: {{30 | 60 | 90}}
plataforma_primaria: {{linkedin | instagram | youtube | x}}
plataformas_secundarias: [{{lista ou vazio}}]
cadencia_posts_semana: {{N}}
frameworks:
  - content-engine
  - hook-framework
  - ad-copy-formula
  - leila-scaling
humanizer_pass: false
humanizer_mode: n/a
voz: crua
parent_version: {{caminho_v_anterior_ou_null}}
---

# Content Roadmap — {{produto_nome}}

## Visão geral

**Período:** {{N}} dias
**Plataforma primária:** {{nome}}
**Plataformas secundárias:** {{nomes ou "nenhuma"}}
**Cadência sustentável:** {{N}} posts/semana
**Total de conteúdos planejados:** {{N}}

**Mix planejado:**
- Educacional: {{N}}% ({{X}} posts)
- Entertainment/Contrarian: {{N}}% ({{X}} posts)
- Promocional: {{N}}% ({{X}} posts)

---

## Tema central do período

**Pillar message:** {{1 frase que conecta toda a produção do período. Ex: "Founder de SaaS B2B pode reduzir ciclo de venda em 60% sem trocar SDR ou aumentar budget."}}

---

## Tópicos por funnel stage

### Awareness (problema reconhecível)

1. {{Tópico — ex: "Por que ciclo de venda B2B fica 90+ dias mesmo com bom produto"}}
2. {{...}}
3. {{...}}

### Consideration (análise de método/framework)

1. {{Tópico — ex: "Os 3 elementos do SDR script que mais impactam taxa de conversão"}}
2. {{...}}
3. {{...}}

### Decision (case study, FAQ, comparação)

1. {{Case — Stark Bank cortou ciclo de 90 para 28 dias em 3 meses}}
2. {{FAQ — "É possível aplicar isso sem trocar o time?"}}
3. {{Comparação — "Consultoria de growth vs. workshop interno"}}

### Retention (advocacy)

1. {{Dica operacional — só para quem já é cliente, mas gera advocacy via share}}

---

## Calendar semanal

### Semana 1

| Dia | Plataforma | Tópico | Funnel stage | Formato | CTA |
|---|---|---|---|---|---|
| {{seg}} | {{LinkedIn}} | {{tópico}} | {{stage}} | {{post longo}} | {{nenhum / soft}} |
| {{qua}} | {{LinkedIn}} | {{tópico}} | {{stage}} | {{carrossel}} | {{...}} |
| {{sex}} | {{LinkedIn}} | {{tópico}} | {{stage}} | {{post curto}} | {{...}} |

### Semana 2

[mesma estrutura]

### Semana 3

[...]

### Semana 4

[...]

(Continua para todo o período definido.)

---

## Repurpose plan

Para cada conteúdo principal (vídeo longo ou artigo de 1500+ palavras), produz:

| Origem | LinkedIn | Instagram | YouTube | X | Newsletter |
|---|---|---|---|---|---|
| Artigo Pricing Playbook | 1 post longo | 1 carrossel | 1 vídeo curto 5min | 1 thread 8 tweets | 1 section |
| Framework SDR script | 1 post curto | 2 Reels 60s | 1 vídeo 12min | 1 thread 6 tweets | 1 section |

Princípio: 1 conteúdo principal → 4-8 derivados consumindo audience diferente.

---

## Formatos por plataforma

### LinkedIn (primária)

| Formato | Frequência | Comprimento | Função |
|---|---|---|---|
| Post longo (educacional) | 2x/semana | 1500-2500 chars | Autoridade |
| Carrossel | 1x/semana | 6-10 slides | Save-friendly |
| Story / quick take | 1x/semana | 300-600 chars | Engagement |

### Instagram (secundária, se aplicável)

| Formato | Frequência | Comprimento | Função |
|---|---|---|---|
| Reel 60s | 2x/semana | 60s | Reach orgânico |
| Carrossel | 1x/semana | 5-10 slides | Save |
| Story | diária | n/a | Conexão diária |

---

## Métricas e cadência de review

### Mês 1-2 (foundation)

**Métricas primárias:**
- Reach total
- Save rate por post
- Profile views

**Alvo realista:**
- Reach crescendo 10-20%/mês
- Save rate > 2% em educacional
- Profile views 50+/post de média

**Review semanal:** vendo top 1 e bottom 1 da semana, registra padrão.

### Mês 3-4 (consistency + first leads)

**Métricas primárias:**
- DM inbound qualificado / semana
- Link clicks (lead magnet ou LP)
- 1-3 first deals via organic

**Alvo:**
- 2-5 DMs inbound qualificados/semana
- 1-3 primeiros clientes via organic

### Mês 6+ (canal estável)

**Métricas primárias:**
- Leads/mês via organic
- CAC via organic vs paid
- % do revenue atribuído ao organic

**Alvo:**
- 20-50 leads/mês
- CAC organic < 50% do paid
- Organic responde por 20-40% dos novos clientes

---

## Princípios operacionais

1. **Cadência sustentável > viral.** 50 posts médios > 1 viral + 49 ruins.
2. **1 plataforma primária primeiro.** Não dilui em 4 plataformas no mês 1.
3. **Documentar > Inventar.** Cada framework usado em projeto vira tópico.
4. **Repurpose obsessivo.** 1 conteúdo principal → 4-8 derivados.
5. **Lag 3-6 meses até primeiro lead.** Quem para no mês 2 não colhe.
6. **Founder-voice obrigatória.** Audience compra pessoa, não marca.

---

## Anti-padrões a evitar

- Cadência aspiracional (1 post/dia sem time)
- Esperar viral em vez de compound
- Pedir feedback de amigos em vez de medir mercado
- Comparar com criadores 5+ anos à frente
- Plataforma errada para ICP
- Postar e não engajar com comentários
- Sem métricas → sem ajuste

---

*Content roadmap gerado pelo plugin hormozi-gtm. Persona Alex Hormozi aplicada. Voz crua — diagnóstico interno não passa por humanizer.*
```
