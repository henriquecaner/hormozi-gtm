---
description: Business plan completo (3000-6000 palavras) para empresa ou produto. Estrutura em 10 seções — sumário, mercado, oferta, money model, pricing, aquisição, operação, métricas, riscos, roadmap 30-60-90. Usa Money Models, LTV:CAC, Core Four, Pricing Playbook, Leila Scaling.
argument-hint: "[slug_ou_caminho] [--tipo=empresa|produto] [--no-humanize]"
---

# /hormozi-gtm:plano

Business plan estruturado. Não é deck pra investidor — é documento operacional que define como o negócio gera dinheiro previsivelmente.

## Carregamento de persona

Orquestrador: `hormozi-persona`.
Money model: delegate a `money-model-architect`.
Pricing: delegate a `pricing-strategist`.
Aquisição: delegate a `leads-strategist`.

## Skills ativas

- `money-models` (4 níveis: attraction/core/upsell/continuity)
- `ltv-cac` (matemática unit economics)
- `core-four` (mix de canais)
- `pricing-playbook` (5 leis)
- `leila-scaling` (operação, hiring, métricas)
- `grand-slam-offer` (oferta core)
- `value-equation` (validação de oferta)
- `humanizer-rules` (modo lite — documento interno)
- `output-conventions`

## Argumentos

| Argumento | Comportamento |
|---|---|
| (vazio) | Pergunta tipo (empresa/produto) |
| `slug` | Cria plano com slug |
| `outputs/plano/<arquivo>.md` | Modo refinar — pergunta qual seção atualizar |
| `--tipo=empresa` | Plano de empresa completa |
| `--tipo=produto` | Plano de produto/SKU específico |
| `--no-humanize` | Pula humanizer |
| `--overwrite` | Sobrescreve v{n} |

## Pré-requisitos

1. `gtm-context.md` existe → carrega o máximo
2. Audit recente? → soft warning se ausente (mas não bloqueia)
3. Pricing review recente? → carrega como `pricing_ref` se existir

## Fluxo

### Passo 1: Coleta estruturada (6 perguntas)

Uma de cada vez:

1. **Categoria/mercado** — em 1 frase
2. **ICP detalhado** — segmento + tamanho + papel + dor
3. **Oferta principal e preço**
4. **Modelo** — one-time, recorrência, híbrido
5. **Canais de aquisição planejados** — Core Four split em %
6. **Meta 12 meses** — receita, # clientes, margem alvo

Pergunta opcional 7: **Tamanho de mercado** (TAM/SAM/SOM se estimado)
Pergunta opcional 8: **Maior risco percebido**

### Passo 2: Análise

Delegate em paralelo (em sequência funcional):

- **`money-model-architect`** monta os 4 níveis (attraction/core/upsell/continuity) com matemática
- **`pricing-strategist`** valida pricing contra 5 leis + concorrência
- **`leads-strategist`** valida mix de canais contra stage da empresa
- Agent principal compila Operação (Leila Scaling), Métricas e Roadmap 30-60-90

### Passo 3: Cálculos críticos

Sempre incluir:
- LTGP calculado (não chute)
- CAC pretendido ou atual
- LTGP:CAC ratio (alvo ≥3:1)
- Payback period (alvo ≤30 dias)

Se ratio <3:1, plano sinaliza explicitamente como risco crítico e sugere fix antes de escalar.

### Passo 4: Humanizer (lite)

Documento interno — modo lite preserva tom direto.

### Passo 5: Salva

`outputs/plano/plano-{tipo}-{slug}-{YYYYMMDD}-v{n}.md` via template `plano.md`.

### Passo 6: Pontos críticos

Mostra na conversa:
- LTGP:CAC ratio + payback (✓ verde, ⚠️ amarelo, ❌ vermelho)
- 1-3 riscos identificados
- 1 recomendação contraintuitiva (se aplicável)
- Caminho do arquivo

## Critério de pronto

- [ ] Sumário executivo cabe em 1 página
- [ ] LTGP:CAC ratio modelado com números (não estimativa vaga)
- [ ] Money Model tem 4 níveis (ou justificativa se algum nível não se aplica)
- [ ] Core Four mix tem alocação numérica (% explícito por canal)
- [ ] Métricas semanais e mensais definidas
- [ ] Roadmap 30-60-90 tem ações executáveis (não diretrizes vagas)
- [ ] Riscos identificados com mitigação
- [ ] Humanizer lite aplicado

## Anti-padrões

- "Vamos focar em tudo" — Core Four exige rateio numérico
- LTGP:CAC sem números (chute disfarçado de plano)
- Money Model só com core offer (sem upsell, sem continuity = CAC paga lento)
- Roadmap genérico ("escalar marketing")
- Sem riscos identificados (plano sem risco é plano fake)

## Output esperado

Arquivo: 3000-6000 palavras, 10 seções
Conversa: 5-10 linhas com ratio + payback + 1-3 riscos críticos + caminho
