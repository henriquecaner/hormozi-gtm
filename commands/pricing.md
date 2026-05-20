---
description: Pricing review contra as 5 leis do LEAKED Pricing Playbook + Value Equation + LTV:CAC. Analisa preço atual, recomenda range, estrutura de tiers (silver/gold/platinum), ancoragem, teste de validação executável em 2 semanas.
argument-hint: "[caminho_de_pricing_anterior] [--no-humanize]"
---

# /hormozi-gtm:pricing

Análise de pricing — não chute, não "intuição de mercado". Aplica as 5 leis do Pricing Playbook contra dados reais de oferta, concorrência e unit economics.

## Carregamento de persona

Orquestrador: `hormozi-persona`.
Especialista: `pricing-strategist`.

## Skills ativas

- `pricing-playbook` (central — 5 leis)
- `value-equation` (validação cruzada)
- `ltv-cac` (matemática)
- `money-models` (estrutura de ascension)
- `humanizer-rules` (modo lite)
- `output-conventions`

## Argumentos

| Argumento | Comportamento |
|---|---|
| (vazio) | Conversa coletando inputs |
| `outputs/pricing/<arquivo>.md` | Modo refinar — re-roda com novos dados |
| `--no-humanize` | Pula humanizer |
| `--overwrite` | Sobrescreve v{n} |

## Pré-requisitos

1. `gtm-context.md` existe → carrega oferta + canal + stage
2. Audit recente da oferta? → cross-check Value Equation antes de tocar preço
3. Sem audit recente → soft warning: "Sem audit, posso recomendar errado. Quer rodar `/hormozi-gtm:audit` antes?"

## Fluxo

### Passo 1: Coleta de inputs (5 perguntas)

1. **Oferta + preço atual** (à vista, parcelado)
2. **3-5 concorrentes diretos com preços**
3. **Margem-alvo** (gross margin %)
4. **LTV estimado / churn** (se recorrência)
5. **Volume atual de vendas** (clientes/mês)

Pergunta opcional 6: **Existe ancoragem superior?** (algum competidor a 3x+ teu preço?)

### Passo 2: Análise

Delegate a `pricing-strategist`. Aplica as 5 leis:

1. **Compete em valor, não em preço** — diagnóstico
2. **Cobra o que vale, não o que custa** — diagnóstico
3. **Preço sinaliza qualidade** — diagnóstico do posicionamento atual
4. **Tiering** — tem tiers? funcionam? recomendação de estrutura
5. **Runway maior, ask maior** — período de atendimento × ask

Cada lei recebe score (verde/amarelo/vermelho) + diagnóstico + recomendação.

### Passo 3: Diferenciação preço vs percepção

Conclui: o problema é **preço** ou **percepção de valor**? Distinção crítica.
- Se percepção: baixar preço não resolve. Fortalece Probability na Value Equation primeiro.
- Se preço: estrutura de tiers + ancoragem + parcelamento.

### Passo 4: Recomendação numérica

Sempre **range**, não preço único.

Estrutura de tiers proposta:
- Tier 1 — Silver: R$ X (entrada)
- Tier 2 — Gold (DEFAULT): R$ Y (60-70% dos clientes)
- Tier 3 — Platinum: R$ Z (ancoragem)

Com:
- Justificativa por tier (deliverables + público)
- Ancoragem explícita (vs Mentoria C a R$ X)
- Estrutura de pagamento (à vista, parcelado)
- Downsell sugerido (pra quem disse não)
- Upsell sugerido (order bump / OTO pós-checkout)

### Passo 5: Teste de validação

Sempre inclui:
- Cenário (próximos 10-20 leads testam novo pricing)
- Métricas (conversion rate, AOV, take rate por tier, tempo de decisão)
- Critério de sucesso ou reversão (objetivo)

### Passo 6: Riscos

1-3 riscos identificados com mitigação.

### Passo 7: Humanizer (lite)

### Passo 8: Salva

`outputs/pricing/pricing-{slug}-{YYYYMMDD}-v{n}.md` via template `pricing-review.md`.

### Passo 9: Resumo

Mostra:
- Análise das 5 leis (verde/amarelo/vermelho)
- Recomendação principal em 1-2 linhas
- Risco principal em 1 linha
- Caminho do arquivo

## Critério de pronto

- [ ] Cada uma das 5 leis tem nota e justificativa
- [ ] Recomendação é range, não número único
- [ ] Identifica se problema é preço OU percepção
- [ ] Teste de validação executável em 1-2 semanas com métrica clara
- [ ] Riscos identificados com mitigação
- [ ] Tiering proposto com deliverables explícitos
- [ ] Humanizer lite aplicado

## Anti-padrões

- Recomendar baixar preço sem checar Value Equation primeiro
- Preço único como recomendação (sempre range)
- Sem teste de validação ("vai funcionar")
- Sem identificar concorrência (preço sem benchmark é chute)
- Pricing review que não toca em Money Model (mas pricing isolado raramente resolve)

## Output esperado

Arquivo: 1200-2000 palavras
Conversa: ~5 linhas com análise das 5 leis (semáforo) + recomendação principal + caminho
