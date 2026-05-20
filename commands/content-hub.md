---
description: Roadmap 30-90 dias de conteúdo orgânico. Tópico × formato × funnel stage × CTA. Mix saudável (60% educacional, 25% entertainment, 15% promocional). Para founder/consultor que quer organic compondo ao longo de 6-18 meses, não 1 post viral.
argument-hint: "[--produto=<slug>] [--ref=<caminho>] [--duracao=30|60|90] [--plataforma=linkedin|instagram|youtube|x] [--no-humanize]"
---

# /hormozi-gtm:content-hub

Plano operacional de conteúdo. Não é "ideias de post" — é roadmap de cadência sustentável com tópicos mapeados em funnel stages, formatos por plataforma, métricas por trimestre.

## Carregamento de persona

Use `hormozi-persona` para orquestrar. Delegate ao `ad-architect` para destilar tópicos em formato consumível. Pass final pelo `humanizer` modo **lite** (roadmap é interno, posts individuais vão pelo `full` na hora de produzir).

## Skills ativas

- `content-engine` (cadência sustentável, mix, métricas)
- `hook-framework` (cada tópico vira hook potencial)
- `ad-copy-formula` (formatos curtos)
- `leila-scaling` (cadência sustentável vs aspiracional)
- `humanizer-rules` (modo lite)
- `output-conventions`

## Argumentos

| Argumento | Comportamento |
|---|---|
| (vazio) | Modo interativo: pergunta produto + duração + plataforma primária |
| `--produto=<slug>` | Slug do produto |
| `--ref=<caminho>` | Refinar roadmap existente |
| `--duracao=30\|60\|90` | Período do roadmap em dias (default 90) |
| `--plataforma=linkedin\|instagram\|youtube\|x` | Plataforma primária. Pode ser múltipla. |
| `--no-humanize` | Pula humanizer |

## Pré-requisitos

1. `gtm-context.md` existe → carrega ICP, oferta, brand voice, intensidade de tom
2. Founder-market fit definido (skill `founder-market-fit`) — sem fit, conteúdo orgânico não constrói autoridade
3. Para `--duracao=90`: idealmente algum case study disponível para inserir como conteúdo promocional

## Fluxo

### Passo 1: Calibra cadência sustentável

Pergunta:
- Quanto tempo por semana o founder consegue dedicar (realista, não aspiracional)?
- Tem time de conteúdo (estrategista, editor)?
- Existe biblioteca de cases / frameworks documentados?

Determina cadência:
- Solo, 4-6h/semana: 2-3 posts/semana em 1 plataforma.
- Solo + assistente, 8h/semana: 3-4 posts/semana em 1 plataforma + repurpose para 2ª.
- Time pequeno (3 pessoas): 1 post/dia em 2-3 plataformas.

### Passo 2: Define mix por trimestre

Mix saudável (vide skill `content-engine`):
- **60% educacional** (autoridade): frameworks, tutoriais, análises de caso público.
- **25% entertainment/contrarian**: hot takes, story pessoal, failure post.
- **15% promocional**: case do cliente, oferta atual, "o que eu faço".

Em estágio inicial (mês 1-3): reduz promocional para 5-10% (audience ainda formando).

### Passo 3: Mapeia tópicos por funnel stage

Cada tópico atende 1 stage do funil:

- **Awareness:** problema reconhecível para audience que NÃO sabe que existe solução.
- **Consideration:** análise de método/framework, comparação de abordagens.
- **Decision:** case study com resultado mensurável, FAQ, comparação direta.
- **Retention:** dicas operacionais para quem já é cliente (vira advocacy).

### Passo 4: Calendar por semana

Para o período (30/60/90 dias), distribui tópicos em calendar:

| Semana | Tópico 1 | Tópico 2 | Tópico 3 |
|---|---|---|---|
| 1 | {{tópico educ}} | {{contrarian}} | {{educ}} |
| 2 | {{educ}} | {{promo - case}} | {{educ}} |
| ... | ... | ... | ... |

### Passo 5: Formatos por plataforma

Para cada tópico, sugere formato ideal por plataforma:

| Tópico | LinkedIn | Instagram | YouTube | X |
|---|---|---|---|---|
| {{Framework de pricing}} | Post longo + carrossel | Reel 60s + carrossel | Vídeo 8-12min | Thread 8 tweets |

### Passo 6: Repurpose plan

Para cada conteúdo principal (vídeo longo ou artigo), define 4-6 derivados:
- 1 post LinkedIn
- 2-3 Reels/Shorts
- 1 thread X
- 1 quote card
- 1 newsletter section

### Passo 7: Métricas e cadência de review

Define métricas primárias por mês:
- Mês 1-2: reach + save rate
- Mês 3-4: DM inbound + profile views
- Mês 6+: leads/mês via organic

### Passo 8: Humanizer (lite)

Lite — roadmap é interno, não vai pra cliente do cliente.

### Passo 9: Salva

`outputs/content/content-roadmap-{produto_slug}-{YYYYMMDD}-v{n}.md` via template `content-roadmap.md`.

### Passo 10: Preview na conversa

```
✅ Salvo em: outputs/content/content-roadmap-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Período: {{N}} dias
   • Plataforma primária: {{nome}}
   • Cadência: {{N}} posts/semana
   • Total de conteúdos no roadmap: {{N}}
   • Mix: {{N}}% educ / {{N}}% entertain / {{N}}% promo
   • Status humanizer: ✓ lite pass

👉 Próximos passos:
   1. Bloqueia 4-6h/semana no calendar para produção
   2. Documenta 1 framework por semana (vira tópico educacional)
   3. Mede reach + save rate semanalmente nos primeiros 30 dias
```

## Critério de pronto

- [ ] Cadência definida e realista (não aspiracional)
- [ ] Mix saudável (não 100% promocional ou 100% educacional)
- [ ] Tópicos mapeados em funnel stages
- [ ] Calendar por semana preenchido
- [ ] Repurpose plan para conteúdos principais
- [ ] Métricas primárias por mês definidas
- [ ] Humanizer lite aplicado

## Anti-padrões

- Cadência aspiracional (1 post/dia sem time)
- Mix 100% promocional (vira anúncio chato)
- Tópicos sem funnel stage (cliente perde fio)
- Plataforma errada para ICP (B2B enterprise no Instagram, B2C no LinkedIn)
- Repurpose ausente (subutiliza cada conteúdo principal)
- Roadmap sem métricas (sem como medir progresso)
- Esperar viral em vez de compound
