---
description: Money Models — Attraction Offer, Core Offer, Upsell, Downsell, Continuity. Use para desenhar revenue model que escala, garantir Client-Financed Acquisition, projetar ascension ladder com matemática.
---

# Money Models — Ascension Ladder

Fonte: Alex Hormozi, *$100M Money Models* + $100M Leads (Cap. 5).

## Os 4 níveis

### 1. Attraction Offer
**Função:** capturar intent, gerar lista quente, qualificar audiência.

Formatos:
- Lead magnet gratuito (PDF, vídeo, planilha, calculadora)
- Tripwire pago de baixo ticket (R$ 7-47)
- Webinar / mini-curso

**Métrica:** cost per lead (CPL) + opt-in rate

### 2. Core Offer
**Função:** resolver o problema central. Onde está a maior margem absoluta.

Características:
- Preço alvo: 10-100x o tripwire ou >100x o lead magnet
- Deve ser Grand Slam Offer completa (use skill `grand-slam-offer`)
- Margem gross alvo: 70%+ (serviços), 80%+ (digital)

**Métrica:** core offer conversion rate + AOV

### 3. Upsell Offer
**Função:** absorver CAC em 30 dias (Client-Financed Acquisition).

Formatos:
- Order bump (+R$ 27-97 no checkout)
- OTO (one-time offer) pós-checkout
- Upsell page com versão premium
- Implementação done-for-you

**Regra de ouro:** upsell take rate alvo = 20-40%. Profit do upsell alvo >= CAC.

**Métrica:** upsell take rate × upsell margem

### 4. Continuity / Downsell

**Continuity:** recorrência mensal/anual. Maximiza LTV.
- Comunidade paga
- Mentoria recorrente
- Software / SaaS layer
- Suporte continuado

**Downsell:** opção para quem disse não ao core.
- Versão self-paced do programa group
- Mini-curso vs imersão completa
- Pagamento parcelado mais longo

**Métrica:** MRR / ARR + churn rate

## Client-Financed Acquisition (regra crítica)

> Se profit do upsell >= CAC em 30 dias, você pode escalar paid ads sem limite de capital.

Como modelar:
```
Profit Upsell em 30 dias >= CAC
```

Se sim → paid scaling ilimitado.
Se não → trabalha pra fazer ficar verdadeiro antes de escalar.

## Workflow de design

1. Define core offer (existe? está validada?)
2. Calcula LTGP (lifetime gross profit) atual do core
3. Define CAC atual ou pretendido
4. Avalia: existe upsell? Se sim, qual take rate e qual profit?
5. Avalia: existe continuity? Qual % do core upgrade para continuity?
6. Avalia: existe downsell? Quanto recupera dos no-buys?
7. Calcula LTV:CAC ratio (use skill `ltv-cac`)
8. Identifica o nível MAIS QUEBRADO e prioriza fix

## Sinais de Money Model fraco

- Só core offer, sem upsell (CAC paga lento, paid não escala)
- Sem continuity (LTV plano = ratio sempre apertado)
- Upsell take rate < 10% (oferta errada ou momento errado)
- Downsell inexistente (perde 70% dos que disseram não)
- Core offer com margem < 50% (modelo não fecha)

## Aplicação por caso de uso

| Caso | Como usar Money Models |
|---|---|
| LP de vendas | LP do core mostra upsell page pós-checkout; downsell aparece em popup de saída |
| Roteiro de ad | Ads diferentes por nível (lead magnet ads cheap CPC; core offer ads high intent) |
| Business plan | Seção "Money Model" projeta os 4 níveis com take rate, margem, ratio LTV:CAC |

## Referência detalhada

Veja `reference/100m-money-models-extracts.md`.
