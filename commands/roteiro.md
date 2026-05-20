---
description: Cria ou refina roteiro de vídeo — VSL longo (8-15min) ou short-form (15-60s). Batch mode gera múltiplas variantes. Usa hook framework, VSL 7-step arc, ad copy formula. Humanizer modo full obrigatório.
argument-hint: "[--produto=<slug>] [--ref=<caminho>] [--formato=vsl|reels|shorts|tiktok] [--batch] [--n=N] [--no-humanize]"
---

# /hormozi-gtm:roteiro

Roteiro de ad em vídeo. Suporta VSL longo (8-15min) ou short-form (15-60s). Batch mode gera múltiplas variantes em uma rodada.

## Carregamento de persona

Orquestrador: `hormozi-persona`.
Análise: delegate a `ad-architect`.
Pass final: delegate a `humanizer` (modo full).

## Skills ativas

- `hook-framework` (crítico — primeiros 3s)
- `vsl-7-step` (para formato VSL longo)
- `ad-copy-formula` (estrutura warm/cold/paid)
- `grand-slam-offer` (referência da oferta sendo vendida)
- `scarcity-urgency` (CTA final)
- `humanizer-rules` (modo full)
- `output-conventions`

## Argumentos

| Argumento | Comportamento |
|---|---|
| (vazio) | Pergunta formato no chat |
| `slug` | Cria roteiro com slug informado |
| `outputs/roteiro/<arquivo>.md` | Modo refinar — lê, pergunta o que mudar |
| `--formato=vsl` | VSL longo (8-15min) |
| `--formato=reels` ou `shorts` ou `tiktok` | Short-form (15-60s) |
| `--batch` | Gera 5-10 variantes (default short-form) |
| `--n=N` | Quantidade de variantes em batch |
| `--no-humanize` | Pula humanizer |
| `--overwrite` | Sobrescreve v{n} |

## Pré-requisitos

1. `gtm-context.md` existe → carrega ICP, oferta, brand voice, audience externa, intensidade do tom
2. Audit recente da oferta? → carrega como `audit_ref`. Se ausente, pergunta interativa:

   > "Sua oferta não passou por Value Equation audit nas últimas 2 semanas. Roteiro escrito sobre oferta sem audit frequentemente precisa retrabalho.
   >
   > Como prefere seguir?
   > (1) Rodar `/hormozi-gtm:audit` agora (5min) — recomendado
   > (2) Seguir mesmo assim — entendo o risco, quero o roteiro hoje
   > (3) Cancelar — volto depois"

3. Hooks validados? → soft suggestion (não bloqueante) de rodar `/hormozi-gtm:hooks` se nenhum hook foi escolhido. Se usuário pediu format short-form sem hooks prévios, sugere rodar `/hooks` antes pra testar 10-15 variantes em ad antes de escrever roteiro completo.

## Fluxo

### Formato VSL (8-15min)

#### Passo 1: Coleta

Pergunta:
- Duração alvo (8min, 10min, 12min, 15min)
- Plataforma destino (YouTube, Facebook, LP embed)
- Hook angle preferido (dream / problem / secret) — ou deixar agent escolher
- 1-2 cases reais comparáveis (se existir)

#### Passo 2: Construção

Delegate a `ad-architect`. Constrói os 7 atos via template `vsl.md`:

1. Hook (0-15s)
2. Story (15s-2min)
3. Problem (2-4min)
4. Mechanism (4-7min) — sempre nomeia o sistema
5. Proof (7-9min)
6. Offer (9-11min) — Grand Slam completa
7. CTA + Urgency (11-12min)

#### Passo 3: Humanizer (full)

Pass final pelo subagent `humanizer`.

#### Passo 4: Salva

`outputs/roteiro/vsl-{slug}-{YYYYMMDD}-v{n}.md` com frontmatter completo + timestamps + notas de produção.

#### Passo 5: Preview na conversa

```
✅ Salvo em: outputs/roteiro/vsl-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Hook (0-15s): "{{texto}}"
   • Mecanismo nomeado: {{nome}}
   • CTA final: "{{texto}}"
   • Duração estimada: {{N}} min
   • Status humanizer: ✓ full pass

👉 Próximos passos:
   1. Gravar VSL ou enviar pro time de vídeo
   2. /hormozi-gtm:hooks --produto={{slug}} → variações de hook pra A/B test
   3. /hormozi-gtm:review --ref=outputs/roteiro/... → se quiser revisão brutal
```

### Formato short-form / Batch

#### Passo 1: Coleta

Pergunta:
- Plataforma principal (Reels, TikTok, Shorts)
- Quantos ângulos quer cobrir (3-5 default)
- Quantas variantes total (default 6 = 2 por ângulo)

#### Passo 2: Construção

Delegate a `ad-architect`. Para cada variante:
- Ângulo (dor / desejo / contrarian / curiosidade / prova)
- Versão 30s e versão 60s
- Texto on-screen
- Hook lendo isoladamente como tweet

Aplica testes de qualidade:
- Funciona muted com legenda?
- Hook tem especificidade?
- CTA tem ação verbal?

#### Passo 3: Top 3 do agent

Ranqueia as variantes e justifica top 3 com critério específico (não "achei melhor").

#### Passo 4: Humanizer (full)

#### Passo 5: Salva

`outputs/roteiro/short-{slug}-{YYYYMMDD}-v{n}.md` via template `ad-short.md`.

#### Passo 6: Plano de teste

Sugere sequenciamento de teste A/B (fase 1, 2, 3).

### Modo REFINAR

Lê arquivo existente. Pergunta:
> "Qual variante? Qual seção? (hook / mechanism / proof / oferta / CTA)"

Refina mantendo o resto. Roda humanizer. Salva v{n+1}.

## Critério de pronto

### Para VSL longo
- [ ] Hook tem especificidade nos primeiros 3s
- [ ] Mecanismo nomeado (não "meu método")
- [ ] 3+ cases comparáveis no proof
- [ ] Garantia condicional na seção offer
- [ ] CTA com ação verbal específica
- [ ] Timestamps coerentes
- [ ] Humanizer full aplicado

### Para short-form / batch
- [ ] Funciona muted com legenda
- [ ] Hook lê como tweet
- [ ] CTA tem ação verbal específica
- [ ] Mix de ângulos (não 6 hooks só de dor)
- [ ] Top 3 do agent com justificativa
- [ ] Humanizer full aplicado

## Anti-padrões

- Hook genérico ("hoje vou te ensinar...")
- Story de 5min em VSL de 12min (perdeu o leitor)
- Mecanismo sem nome próprio
- Proof com 1 case só
- CTA "saiba mais" sem ação verbal
- Short-form que precisa de áudio pra fazer sentido

## Output esperado

VSL: 1200-2500 palavras + timestamps + notas de produção
Short-form batch: 6-10 variantes em formato comparável + top 3 do agent + plano de teste
