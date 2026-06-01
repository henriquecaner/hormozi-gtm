---
description: Gera batch de 10-20 variantes de hooks/headlines/subject lines. Mix de ângulos (dream/problem/secret/contrarian/proof). Top 3 do agent ao final com justificativa. Humanizer modo full.
argument-hint: "[--produto=<slug>] [--ref=<caminho>] [--n=N] [--angulo=<dream|problem|secret|contrarian|proof>] [--no-humanize]"
---

# /hormozi-gtm:hooks

Gera bateladas de hooks/headlines/subject lines para testes A/B. Por padrão 15 variantes cobrindo 5 ângulos.

## Carregamento de persona

Orquestrador: `hormozi-persona`.
Especialista: `ad-architect`.
Pass final: `humanizer` (modo full — hooks vão pro cliente).

**Carregamento de voz IN-CONTEXTO (obrigatório):** carregue a skill `hormozi-voice` via ferramenta Skill e imite o registro — não dependa só do subagent (no Cowork ele pode não rodar). Hooks são copy externa: cada hook só sai com **brutalidade ≥7 na rubrica da hormozi-voice**. Abaixo de 7, reescreve antes de listar.

## Skills ativas

- `hormozi-voice` (registro de voz brutal + rubrica 0-10 — carregada in-contexto)
- `hook-framework` (central — 3 tipos canônicos + ângulos extras)
- `ad-copy-formula` (estrutura por canal)
- `template-hooks-batch` (esqueleto do output — carregada in-contexto)
- `humanizer-rules` (modo full)
- `output-conventions`

## Argumentos

| Argumento | Comportamento |
|---|---|
| (vazio) | Pega oferta do `gtm-context.md` |
| `slug` | Slug do produto/oferta |
| `outputs/lp/<arquivo>.md` | Gera hooks pra refinar headline desse material |
| `--n=N` | Quantidade total (default 15) |
| `--angulo=<tipo>` | Foca em 1 ângulo (gera N do mesmo tipo) |
| `--no-humanize` | Pula humanizer |
| `--overwrite` | Sobrescreve v{n} |

## Pré-requisitos

1. `gtm-context.md` existe → carrega ICP, oferta, transformação, audience externa, intensidade do tom
2. Senão → pergunta no chat (3 perguntas mínimas)

## Fluxo

### Passo 1: Coleta inputs (se necessário)

Se `gtm-context.md` está completo, pula direto pro Passo 2.

Senão pergunta:
1. ICP (1 frase específica)
2. Oferta (o que vende)
3. Transformação prometida (em quanto tempo, quem vira o quê)

### Passo 2: Estratégia de mix

Default: distribuição em 5 ângulos
- Dream outcome (3-5 hooks)
- Problem (3-5 hooks)
- Secret (3-5 hooks)
- Contrarian (2-3 hooks)
- Proof (2-3 hooks)

Se `--angulo=X`, gera N do mesmo tipo.

### Passo 3: Geração

Delegate a `ad-architect`. Para cada hook:

- Frase (com especificidade numérica quando possível)
- Ângulo
- Mecanismo (qual emoção/pensamento aciona)
- Onde usar (LP headline / ad short / email subject / etc.)

Aplica os 3 testes de qualidade:
- Especificidade numérica
- Tweet test
- Curiosity gap

### Passo 4: Top 3 do agent

Ranqueia e justifica top 3 com critério específico (não "achei melhor"). Cada top 3 tem:
- Frase completa
- Por que é o top
- Onde testar primeiro (plataforma + formato)

### Passo 5: Humanizer (full)

Hooks são copy externa — modo full obrigatório. Passe os hooks pelo subagent `humanizer` (modo full) E confira contra `humanizer-rules`. Mesmo após o humanizer, cada hook tem que manter brutalidade ≥7 na rubrica da `hormozi-voice` — humanizer remove AI-ism, não amacia a voz. Frontmatter sai com `humanizer_pass: true` / `humanizer_mode: full`.

### Passo 6: Salva

Carregue a skill `hormozi-gtm:template-hooks-batch` via ferramenta Skill e preencha o esqueleto. Salva em `outputs/hooks/hooks-{slug}-{YYYYMMDD}-v{n}.md`.

### Passo 7: Preview na conversa

```
✅ Salvo em: outputs/hooks/hooks-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Quantidade total: {{N}} hooks
   • Top 3 escolhidos pelo agent:
     1. "{{texto}}" — {{ângulo}}, {{critério}}
     2. "{{texto}}" — {{ângulo}}, {{critério}}
     3. "{{texto}}" — {{ângulo}}, {{critério}}
   • Status humanizer: ✓ full pass

👉 Próximos passos:
   1. Testar top 3 em ads (R$ 200-500/cada, 48h)
   2. Vencedor vira headline da próxima LP
   3. /hormozi-gtm:roteiro --produto={{slug}} usando hook vencedor
```

## Critério de pronto

- [ ] Mix de ângulos (não 15 hooks só de dor) — exceto se `--angulo=` foi passado
- [ ] Especificidade numérica em pelo menos 60% dos hooks
- [ ] Nenhum hook genérico ("descubra o segredo")
- [ ] Top 3 do agent com critério explícito
- [ ] Plano de teste sugerido
- [ ] Brutalidade ≥7 na rubrica da `hormozi-voice` em cada hook (copy externa)
- [ ] Humanizer full aplicado
- [ ] Arquivo salvo com frontmatter

## Anti-padrões

- "Descubra o segredo de X" (genérico)
- "Você quer ganhar mais?" (yes/no genérico)
- Hooks que dependem de contexto perdido
- Top 3 sem justificativa específica ("achei melhor")
- Mix homogêneo (15 dream outcomes) sem usuário pedir

## Output esperado

Arquivo: tabela de N hooks + top 3 + plano de teste (~500-800 palavras)
Conversa: top 3 + caminho (~5 linhas)
