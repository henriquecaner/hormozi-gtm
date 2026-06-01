---
description: Matriz de objeções por ICP. Cada objeção mapeada com root cause (oferta / preço / timing), reframe em 2 frases, script palavra-por-palavra pra sales call, mitigação na oferta. Para consultor em sales call e founder mapeando objeções recorrentes.
argument-hint: "[--produto=<slug>] [--ref=<caminho>] [--segmento=<icp_subset>]"
---

# /hormozi-gtm:objections

Matriz operacional de objeções. Não é "lista de respostas prontas" — é diagnóstico estruturado: por que essa objeção aparece, o que ela revela sobre a oferta, e o que dizer quando aparece.

## Carregamento de persona

Use `hormozi-persona` para orquestrar. Delegate ao `offer-architect` se a objeção raiz é de oferta, `pricing-strategist` se é de preço.

Carregue a skill `hormozi-voice` via ferramenta Skill e **imite o registro** (número e verbo, zero adjetivo de marketing, reframe na cara do prospect). Não dependa só do subagent — no Cowork ele pode não rodar; a voz tem que vir carregada in-contexto neste comando. A matriz de objeções é diagnóstico interno e cru: scripts diretos, sem amaciar.

## Skills ativas

- `hormozi-voice` (sempre — registro de voz carregado in-contexto)
- `template-objections-matrix` (sempre — esqueleto do output)
- `value-equation` (diagnóstico de objeção)
- `grand-slam-offer` (mitigação na oferta)
- `pricing-playbook` (objeções de preço)
- `guarantees` (reframe via garantia)
- `output-conventions`

## Argumentos

| Argumento | Comportamento |
|---|---|
| (vazio) | Modo interativo: pergunta produto + segmento + objeções comuns |
| `--produto=<slug>` | Slug do produto (lê de gtm-context.md) |
| `--ref=<caminho>` | Refinar matriz existente |
| `--segmento=<icp_subset>` | Foca em sub-segmento do ICP (ex: SaaS B2B fintech) |

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

### Passo 5: Voz crua (sem humanizer)

objections é interno — NÃO passa por humanizer. Sai cru, Hormozi brutal, direto. Mantenha o registro de `hormozi-voice`: número e verbo, reframe na cara do prospect, sem amaciar. Os scripts palavra-por-palavra carregam essa voz direta — o consultor adapta o tom na sales call ao vivo.

### Passo 6: Salva

Carregue a skill `hormozi-gtm:template-objections-matrix` via ferramenta Skill e preencha o esqueleto. Salva em `outputs/objections/objections-{produto_slug}-{YYYYMMDD}-v{n}.md`.

No frontmatter do output (já refletido no esqueleto): `humanizer_pass: false`, `humanizer_mode: n/a`, `voz: crua`.

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
   • Voz: crua (diagnóstico interno, sem humanizer)

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
- [ ] Voz crua mantida (sem humanizer — diagnóstico interno)

## Anti-padrões

- Scripts que viram "resposta enlatada" detectável em 30s
- Reframe que ignora a objeção real (responde pergunta diferente)
- Tratar objeção de timing como se fosse de preço (descontão não resolve)
- Não fazer pergunta de qualificação antes do reframe (perde info crítica)
- Matriz com 20+ objeções (consultor não decora — foca em top 5)
