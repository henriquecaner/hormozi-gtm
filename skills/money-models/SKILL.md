---
name: money-models
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

## Ordem de validação pre-launch

Founder iniciante tenta validar 4 níveis simultaneamente, queima capital e não sabe qual nível falhou. A ordem certa é sequencial — só sobe pro próximo quando o anterior atinge gate:

> **Nota de fonte:** o corpus (`reference/100m-money-models-extracts.md`) ancora a *estrutura* — sequência de validação, take rate de upsell 20-40%, downsell 10-25%, "cada nível se paga sozinho". Os **gates numéricos específicos abaixo** (conversão ≥2%, NPS ≥7, ≥20% fake-door, churn ≤8%/mês, ≥200 no-buys, etc.) são heurística de calibração prática, não thresholds citados literalmente do livro. Ajuste por contexto de nicho/ticket.

**1. Core Offer (sempre primeiro)**
- Pergunta: existe demanda e converte?
- Gate: conversão ≥ 2% em LP fria com tráfego pago + NPS ≥ 7 nos primeiros 20 clientes.
- Investimento: ~30-90 dias.
- Se falha aqui, **não construa upsell** — volta pra Value Equation e refaz a oferta.

**2. Upsell (pré-vendido)**
- Pergunta: existe interesse antes de eu construir?
- Como validar **sem construir**: survey aos clientes Core ("Se tivesse [upsell] por R$ X, compraria?"), fake door (botão "Comprar upsell" na thank-you page, redireciona pra "em desenvolvimento, garante seu spot") ou pre-sale com desconto.
- Gate: ≥ 20% dos clientes Core demonstram interesse explícito (survey 4+/5 ou fake door click >20%).
- Se < 20%, oferta de upsell está errada — itera no upsell, não constrói ainda.

**3. Upsell (lançado pós-checkout)**
- Pergunta: take rate real bate 20-40%?
- Gate: ≥ 20% take rate nos primeiros 50 clientes Core. Se Core + Upsell ratio é < 3:1 LTV:CAC ainda, volta pra pricing antes de continuar.
- Investimento: ~30-60 dias construindo + 30 dias coletando dados.

**4. Continuity / Recorrência**
- Pergunta: clientes Core+Upsell já demonstraram disposição pra pagar contínuo?
- Como validar: oferece versão "preview" ou waitlist antes de construir engine de subscription.
- Gate: ≥ 15% dos clientes Core+Upsell engajam com continuity em 60 dias pós-purchase. Churn em 90 dias ≤ 8%/mês.

**5. Downsell (último)**
- Pergunta: quanto da audiência que disse não pode ser recuperada?
- Construa só depois de ter pelo menos 200 no-buys catalogados. Antes disso, downsell é otimização prematura.
- Gate: recupera ≥ 10% dos no-buys com margem ≥ 30%.

**Princípio:** Cada nível deve **se pagar sozinho** antes de construir o próximo. Se Core não fecha, upsell não conserta. Se upsell não tem take rate, continuity é fantasia.

## Aplicação por caso de uso

| Caso | Como usar Money Models |
|---|---|
| LP de vendas | LP do core mostra upsell page pós-checkout; downsell aparece em popup de saída |
| Roteiro de ad | Ads diferentes por nível (lead magnet ads cheap CPC; core offer ads high intent) |
| Business plan | Seção "Money Model" projeta os 4 níveis com take rate, margem, ratio LTV:CAC |

## Referência detalhada

Veja `reference/100m-money-models-extracts.md`.
