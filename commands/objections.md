---
description: Matriz de objeções por ICP. Cada objeção mapeada com root cause (oferta / preço / timing), reframe em 2 frases, script palavra-por-palavra pra sales call, mitigação na oferta. Para consultor em sales call e founder mapeando objeções recorrentes.
argument-hint: "[--produto=<slug>] [--ref=<caminho>] [--segmento=<icp_subset>] [--no-humanize]"
---

# /hormozi-gtm:objections

Matriz operacional de objeções. Não é "lista de respostas prontas" — é diagnóstico estruturado: por que essa objeção aparece, o que ela revela sobre a oferta, e o que dizer quando aparece.

## Carregamento de persona

Use `hormozi-persona` para orquestrar. Delegate ao `offer-architect` se a objeção raiz é de oferta, `pricing-strategist` se é de preço. Pass final pelo `humanizer` modo **full** (scripts vão pra cliente usar em sales call).

## Skills ativas

- `value-equation` (diagnóstico de objeção)
- `grand-slam-offer` (mitigação na oferta)
- `pricing-playbook` (objeções de preço)
- `guarantees` (reframe via garantia)
- `humanizer-rules` (modo full)
- `output-conventions`

## Argumentos

| Argumento | Comportamento |
|---|---|
| (vazio) | Modo interativo: pergunta produto + segmento + objeções comuns |
| `--produto=<slug>` | Slug do produto (lê de gtm-context.md) |
| `--ref=<caminho>` | Refinar matriz existente |
| `--segmento=<icp_subset>` | Foca em sub-segmento do ICP (ex: SaaS B2B fintech) |
| `--no-humanize` | Pula humanizer (debug) |

## Pré-requisitos

1. `gtm-context.md` existe → carrega ICP, oferta, preço atual
2. Audit recente (≤30 dias)? → carrega como `audit_ref`. Se ausente, pergunta interativa (3 opções)
3. Idealmente: dados qualitativos de sales calls reais (transcript, notas) — alimenta personalização

## Fluxo

### Passo 1: Coleta objeções

Se modo interativo: pergunta as 3-5 objeções mais frequentes em sales call. Se possível, com transcript curto de exemplo (frase exata do prospect).

### Passo 2: Categoriza root cause

Cada objeção é mapeada em 1 de 4 categorias:

- **Oferta:** prospect não vê valor suficiente (Value Equation problema).
- **Preço:** prospect vê valor mas resiste ao número (pricing problema).
- **Timing:** prospect vê valor + aceita preço mas não agora (urgência/escassez problema).
- **Trust:** prospect duvida da entrega ou da pessoa (proof / founder-market fit problema).

### Passo 3: Diagnóstico por objeção

Para cada objeção:
- Frase típica que aparece
- Root cause (das 4 categorias)
- O que a objeção REALMENTE significa (frequentemente diferente do que o prospect verbaliza)
- Reframe em 2 frases (a frase exata do consultor em sales call)
- Mitigação na oferta (mudança que reduz a objeção aparecer)

### Passo 4: Scripts palavra-por-palavra

Para top 3-5 objeções:
- Pergunta de qualificação ("antes de responder, posso entender...")
- Reframe (2-3 frases)
- Pergunta de fechamento ("isso faz sentido? quer que a gente continue?")

### Passo 5: Humanizer (full)

Scripts vão pra cliente usar em sales call ao vivo. Voz precisa estar limpa, sem AI-isms que destruiriam credibilidade.

### Passo 6: Salva

`outputs/objections/objections-{produto_slug}-{YYYYMMDD}-v{n}.md` via template `objections-matrix.md`.

### Passo 7: Preview na conversa

```
✅ Salvo em: outputs/objections/objections-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Total de objeções mapeadas: {{N}}
   • Distribuição por root cause:
     - Oferta: {{N}} ({{N}}%)
     - Preço: {{N}} ({{N}}%)
     - Timing: {{N}} ({{N}}%)
     - Trust: {{N}} ({{N}}%)
   • Top 3 objeções com script completo: ✓
   • Status humanizer: ✓ full pass

👉 Próximos passos:
   1. Treinar SDR/closer nos top 3 scripts (role-play 30min)
   2. Se Oferta domina → /hormozi-gtm:audit para fortalecer Probability/Effort
   3. Se Preço domina → /hormozi-gtm:pricing para reestruturar tiering
```

## Critério de pronto

- [ ] ≥ 5 objeções mapeadas
- [ ] Cada objeção tem root cause categorizado
- [ ] Top 3 têm script palavra-por-palavra
- [ ] Diagnóstico cruzado: maioria das objeções são oferta? preço? timing?
- [ ] Mitigação na oferta listada (mudanças sugeridas para reduzir essas objeções aparecerem)
- [ ] Humanizer full aplicado

## Anti-padrões

- Scripts que viram "resposta enlatada" detectável em 30s
- Reframe que ignora a objeção real (responde pergunta diferente)
- Tratar objeção de timing como se fosse de preço (descontão não resolve)
- Não fazer pergunta de qualificação antes do reframe (perde info crítica)
- Matriz com 20+ objeções (consultor não decora — foca em top 5)
