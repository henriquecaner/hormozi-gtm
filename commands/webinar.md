---
description: Estrutura de webinar B2B (30-45min) — educacional na superfície, vendedor na estrutura. Diferente de VSL direct-response (12min). Hook + problema + mechanism + cases + oferta + Q&A. Para SaaS B2B, consultoria high-ticket, ofertas que precisam de educação antes do close.
argument-hint: "[--produto=<slug>] [--ref=<caminho>] [--duracao=30|45|60] [--formato=zoom|youtube|prerecorded] [--no-humanize]"
---

# /hormozi-gtm:webinar

VSL é direct-response (12min, B2C/transacional). Webinar é educacional (30-60min, B2B/high-ticket). Mesma persona Hormozi, estrutura diferente. Esta cobre a estrutura B2B.

## Carregamento de persona

Use `hormozi-persona` para orquestrar. Delegate ao `ad-architect` para escrever o roteiro completo, e `offer-architect` para o bloco de oferta. Pass final pelo `humanizer` modo **full** (webinar é entregue ao vivo / gravado para cliente externo).

## Skills ativas

- `hook-framework` (abertura)
- `vsl-7-step` (adaptado para 30-45min)
- `grand-slam-offer` (bloco de oferta)
- `value-equation` (ancoragem do mechanism)
- `guarantees` (CTA com garantia)
- `humanizer-rules` (modo full)
- `output-conventions`

## Argumentos

| Argumento | Comportamento |
|---|---|
| (vazio) | Modo interativo: pergunta duração + formato + objetivo |
| `--produto=<slug>` | Slug do produto |
| `--ref=<caminho>` | Refinar webinar existente |
| `--duracao=30\|45\|60` | Duração total (default 45) |
| `--formato=zoom\|youtube\|prerecorded` | Live (Q&A real) ou pré-gravado (Q&A simulado) |
| `--no-humanize` | Pula humanizer (debug) |

## Pré-requisitos

1. `gtm-context.md` existe → carrega ICP, oferta, brand voice
2. Audit recente → carrega como `audit_ref`
3. Pelo menos 2-3 case studies disponíveis (sem cases, webinar B2B vira teoria)
4. Para `--formato=prerecorded`: roteiro completo precisa cobrir objeções esperadas (sem Q&A real)

## Fluxo

### Passo 1: Calibra duração e formato

| Duração | Formato típico | Use quando |
|---|---|---|
| 30min | Demo + Q&A curto | Cliente já familiar com categoria; produto SaaS B2B; ticket R$ 5-30k/mês |
| 45min | Educacional + venda | Cliente precisa de framework antes; consultoria high-ticket R$ 30-100k |
| 60min | Educacional profundo + Q&A | Cliente novo no problema; ticket R$ 100k+ enterprise |

### Passo 2: Estrutura por bloco (45min como default)

| Bloco | Duração | Função | Dependência |
|---|---|---|---|
| Abertura + housekeeping | 2-3min | Hook + agenda + regras de Q&A | `hook-framework` |
| Diagnóstico do problema | 8min | Como o problema aparece, por que ninguém resolve, custo do problema | Inputs do `gtm-context.md` |
| Mechanism nomeado | 10-12min | Framework proprietário + componentes + como funciona | `value-equation`, frameworks da empresa |
| Cases | 8min | 2-3 antes/depois numérico (não 1, não 5) | `case-study` skill, audit_ref |
| Oferta + bonuses + garantia | 5-7min | Grand Slam Offer + tiering + escassez | `grand-slam-offer`, `guarantees` |
| Q&A | 10-15min | Real (live) ou simulado (prerecorded) | `objections` skill se disponível |
| Fechamento + CTA | 2-3min | Direção final, próximos passos | `ad-copy-formula` (CTA específico) |

### Passo 3: Construção dos blocos

Delegate ao `ad-architect` com briefing por bloco:
- Para "Mechanism nomeado": destila o framework signature da empresa em 4-6 componentes nomeados.
- Para "Cases": puxa 2-3 case studies, cada um com 90-120 segundos de exposição.
- Para "Oferta": delegate ao `offer-architect` para amarrar bonuses + garantia + tiering visual.

### Passo 4: Anti-padrões check

Para `--formato=prerecorded`:
- Q&A simulado precisa cobrir top 3-5 objeções (puxa de `objections` se existir).
- Sem ad-libs improvisados (todo o conteúdo precisa estar no roteiro).

Para `--formato=zoom` (live):
- Q&A pode ser real (não roteirizado).
- Mas tem que ter "plant questions" prep — 3-5 perguntas que você sabe que vão aparecer, com respostas mentais ensaiadas.

### Passo 5: Humanizer (full)

### Passo 6: Salva

`outputs/webinar/webinar-{produto_slug}-{YYYYMMDD}-v{n}.md` via template `webinar-agenda.md`.

### Passo 7: Preview na conversa

```
✅ Salvo em: outputs/webinar/webinar-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Duração total: {{N}} min
   • Formato: {{zoom | youtube | prerecorded}}
   • Hook: "{{primeiros 80 chars}}..."
   • Mechanism nomeado: {{nome}}
   • Cases incluídos: {{N}} (referências: {{slugs}})
   • CTA: "{{texto}}"
   • Status humanizer: ✓ full pass

👉 Próximos passos:
   1. Ensaio 1x (live) ou gravação técnica (prerecorded)
   2. Slides em paralelo (não rodar webinar sem suporte visual)
   3. /hormozi-gtm:objections para preparar Q&A se ainda não tem
```

## Critério de pronto

- [ ] Hook passa tweet-test (lê isolado e gera curiosity gap)
- [ ] Mechanism nomeado com 4-6 componentes
- [ ] 2-3 cases concretos (não mais — diluído)
- [ ] Oferta com bonuses ímpar + garantia condicional
- [ ] CTA específico no fechamento (não "vamos conversar?")
- [ ] Q&A preparado (live: plant questions; prerecorded: scripted)
- [ ] Duração total ≤ planejada + 10% buffer

## Anti-padrões

- Webinar 100% educacional sem oferta (vira aula gratuita)
- Webinar 100% vendedor sem framework (vira pitch chato de 45min)
- Mechanism sem nome próprio (vira "minha metodologia")
- 5+ cases (cliente perde fio condutor)
- Q&A improvisado sem prep (live com perguntas difíceis quebra credibilidade)
- Hook genérico ("Hoje vou compartilhar...")
- Slides com 200 palavras por slide
- Esquecer escassez no CTA (não fechou no webinar → não fecha em 48h)
