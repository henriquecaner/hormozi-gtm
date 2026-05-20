---
description: Framework de teste estatístico de creatives. Matrix de teste (muda 1 elemento por vez), sample size necessário, kill criteria com number, scale winner vs pivot creative inteiro. Para founder que gasta R$ 200 em ad e perde fé — esta skill ensina quanto investir mínimo pra ter sinal real.
---

# Ad Creative Testing

Fonte: Alex Hormozi, *$100M Leads* (Cap. 4, "Ad Mechanics") + cross-reference com `ad-copy-formula` e `hook-framework`.

## Por que essa skill existe

`ad-copy-formula` ensina **o que escrever** num ad. Esta cobre **como testar sistematicamente** para descobrir qual versão funciona, com sample size estatístico e kill criteria objetivo. Sem isso, founder gasta R$ 200 num ad, vê resultado ruim, perde fé, e ataca o problema errado (acha que é copy quando pode ser audience, ou vice-versa).

A maioria dos founders brasileiros mata creative no dia 1-2 antes de ter sinal estatístico. Quem testa sistemática descobre o vencedor 3x mais rápido com o mesmo budget.

## Matrix de teste — muda 1 elemento por vez

Você só consegue isolar qual elemento moveu o resultado se mudar 1 de cada vez. Mudar 3 ao mesmo tempo é apostar, não testar.

**Hierarquia de elementos (do mais impactante ao menos):**

1. **Hook (primeiros 3 segundos)** — 50-70% do CTR vem daqui.
2. **Audience / segmentação** — 20-30%.
3. **Creative format (vídeo vs imagem vs carrossel)** — 10-20%.
4. **CTA e copy de corpo** — 5-15%.
5. **Detalhes visuais (cor, font, thumbnail)** — 2-5%.

**Regra:** otimiza top-down. Não mexe em font enquanto hook está fraco.

**Matrix exemplo:**

```
Variável            Variação A           Variação B           Variação C
Hook                "Reduzir CAC 38%"    "Stop perder leads"  "O erro do SDR"
Audience            ICP-1                ICP-2                ICP-1
Format              Vídeo 15s            Vídeo 15s            Vídeo 15s
CTA                 "Ver PDF"            "Ver PDF"            "Ver PDF"
```

Vai testar **só Hook** (3 variações). Audience constante (controle). Format constante. CTA constante. Quando descobre Hook vencedor, troca pra ele, então testa Audience com Hook fixo.

## Sample size — quanto investir pra ter sinal real

Sample size mínimo depende do CTR/conversion rate esperado. Heurística por estágio:

| Estágio do teste | Investimento mínimo por variante | Por que esse valor |
|---|---|---|
| **Hook test (3-5 variantes)** | R$ 150-300 cada | Suficiente para 1000-2000 impressions, identifica winner se CTR diff ≥ 30% |
| **Audience test (2-4 segmentos)** | R$ 300-500 cada | Precisa amostra maior para isolar audience effect |
| **Creative format test** | R$ 500-1000 cada | Format affects engagement signal, precisa mais impressions |
| **Full funnel (com conversão)** | R$ 1k-3k cada | Precisa 20-50 conversões para ratio confiável |

**Regra de bolso:** se você não consegue investir o mínimo, **não teste ainda**. Espera ter budget. Teste subdimensionado dá falso sinal.

**Cálculo simples (Hook test):**
- CTR baseline esperado: ~1-2% em ads frios.
- Para detectar diff de 30% no CTR (ex: 1.5% → 2%): precisa ~500-1000 cliques por variante.
- 1.5% × 1000 cliques = 67k impressions. Em paid social: ~R$ 200-300.

## Kill criteria — quando matar uma variante

Founder mata muito cedo (12h, 50 impressions) ou muito tarde (continua 7 dias com performance horrível). Critério objetivo:

**Mata a variante quando:**
1. ≥ 1000 impressions acumuladas (sample suficiente)
2. **E** CTR < 50% do best performer
3. **E** sem melhora nos últimos 250 impressions

Exemplo:
```
Variante A: 2.1% CTR (best performer, 1200 impressions)
Variante B: 1.8% CTR (1150 impressions) → keep, dentro da margem
Variante C: 0.8% CTR (1050 impressions) → KILL (< 50% do A, sem improvement)
```

**Não mata baseado em:**
- 1 dia de dados (timing/dia da semana afeta).
- "Sentimento" (gosto pessoal).
- Comentários de 3 amigos.

## Scale winner vs pivot creative inteiro

Depois de encontrar winner, decisão crítica: dobra investimento ou questiona se creative inteiro precisa pivot?

**Scale winner quando:**
- Winner tem ROAS > 2.5x consistente por ≥ 3 dias.
- CTR > média do nicho (Meta Ads B2B: > 1.5%).
- Custo por lead < 50% do LTV target.

**Pivot creative inteiro quando:**
- Mesmo winner tem ROAS < 1.5x.
- Todos os hooks têm CTR < 1%.
- Múltiplos testes não destravam.

**Sinais de que é problema de oferta, não de creative:**
- CTR alto (>2%) mas conversão baixa (<3%) — copy do ad atrai, oferta não fecha.
- Vários winners ao longo de meses, ROAS sempre apertado — oferta vale 1/3 do preço, não é creative.

**Fix:** volta para `grand-slam-offer` ou `value-equation`. Creative não conserta oferta fraca.

## Cadência de teste sustentável

Founder brasileiro tenta testar tudo numa semana e queima budget. Cadência realista:

| Maturidade do account | Cadência |
|---|---|
| Início (mês 1-2) | 1 teste de hook a cada 1-2 semanas (4-6 variantes total/mês) |
| Mid (mês 3-6) | 1 teste de hook + 1 teste secundário por semana |
| Mature (mês 6+) | Pipeline de teste contínuo, 3-5 variantes novas/semana sempre rodando |

**Princípio:** testes precisam de tempo para acumular sample. Acelerar antes da hora destrói signal.

## Anti-padrões

**1. Matar variante no dia 1 com 200 impressions.**
Sample não é estatística — você está vendo sorte.

**2. Mudar 3 elementos de uma vez.**
"Mudei hook + audience + CTA, CTR caiu 50%". Não sabe qual elemento foi.

**3. Não documentar o que testou.**
3 meses depois, refaz o mesmo teste já feito.

**4. Testar audience sem testar hook primeiro.**
Audience perfeita com hook ruim ainda dá CTR ruim. Hook é primeiro.

**5. "Vou testar tudo no Instagram primeiro".**
Plataforma afeta tudo. Hook que funciona no Meta Ads não funciona no LinkedIn Ads. Teste em cada plataforma separadamente.

**6. Comparar creative seu vs concorrente sem mesma audience.**
Audience diferente, ROAS diferente. Não é comparável.

**7. Manter loser por afinidade pessoal.**
"Mas eu gosto desse criativo." Mercado decide, não você.

## Roadmap de teste — primeiros 90 dias

**Mês 1: Hook hunt**
- Semana 1: 4 hooks dramáticos diferentes (R$ 200 cada = R$ 800).
- Semana 2: top 2 hooks vs 2 novos (R$ 800).
- Semana 3-4: refina hook vencedor com micro-variações.

**Mês 2: Audience hunt**
- Hook fixo (vencedor).
- 3-4 audiences diferentes (ICP-1 broad, ICP-1 narrow, ICP-2, lookalike).
- R$ 300-500 por audience.

**Mês 3: Format + CTA**
- Audience + hook fixos.
- Testa vídeo 15s vs 30s vs imagem.
- Testa CTA "Ver PDF" vs "Quero saber" vs "Aceito auditoria".

Ao final dos 90 dias, você tem combinação winning sólida e pode escalar com confiança.

## Aplicação por caso de uso

| Caso | Como usar |
|---|---|
| `/hormozi-gtm:hooks` | Output são 8-12 hooks — esta skill orienta como testar (sample size, kill criteria) |
| `/hormozi-gtm:plano` em founder rodando paid | Inclui orçamento de teste no roadmap de aquisição |
| ROAS apertando em campanhas → pivot ou refinar? | Skill ajuda diagnosticar: hook? audience? oferta? |

## Quando NÃO entra

- Founder antes de primeiros 50 leads pagos (não tem data para testar).
- Negócio 100% organic / referência (não roda paid).
- Conversão de site / pricing test → use `pricing-playbook`.

## Referência detalhada

`reference/100m-leads-extracts.md` cap. 4 ("Ad Mechanics").
