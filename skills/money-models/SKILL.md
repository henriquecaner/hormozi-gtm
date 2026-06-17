---
name: money-models
description: Money Models — Attraction Offer, Core Offer, Upsell, Downsell, Continuity. Use to design a revenue model that scales, guarantee Client-Financed Acquisition, and project an ascension ladder with the math.
---

# Money Models — Ascension Ladder

Source: Alex Hormozi, *$100M Money Models* + $100M Leads (Ch. 5).

## The 4 levels

### 1. Attraction Offer
**Job:** capture intent, build a warm list, qualify the audience.

Formats:
- Free lead magnet (PDF, video, spreadsheet, calculator)
- Low-ticket paid tripwire ($7-47)
- Webinar / mini-course

**Metric:** cost per lead (CPL) + opt-in rate

### 2. Core Offer
**Job:** solve the central problem. Where the largest absolute margin lives.

Characteristics:
- Target price: 10-100x the tripwire, or >100x the lead magnet
- Must be a complete Grand Slam Offer (use the `grand-slam-offer` skill)
- Target gross margin: 70%+ (services), 80%+ (digital)

**Metric:** core offer conversion rate + AOV

### 3. Upsell Offer
**Job:** absorb CAC within 30 days (Client-Financed Acquisition).

Formats:
- Order bump (+$27-97 at checkout)
- OTO (one-time offer) post-checkout
- Upsell page with a premium version
- Done-for-you implementation

**Golden rule:** target upsell take rate = 20-40%. Target upsell profit >= CAC.

**Metric:** upsell take rate × upsell margin

### 4. Continuity / Downsell

**Continuity:** monthly/annual recurring revenue. Maximizes LTV.
- Paid community
- Recurring coaching
- Software / SaaS layer
- Ongoing support

**Downsell:** an option for whoever said no to the core.
- Self-paced version of the group program
- Mini-course vs. full immersion
- Longer installment plan

**Metric:** MRR / ARR + churn rate

## Client-Financed Acquisition (critical rule)

> If upsell profit >= CAC within 30 days, you can scale paid ads with no capital ceiling.

How to model it:
```
Upsell Profit within 30 days >= CAC
```

If yes → unlimited paid scaling.
If no → work to make it true before you scale.

## Design workflow

1. Define the core offer (does it exist? is it validated?)
2. Compute current LTGP (lifetime gross profit) of the core
3. Define current or target CAC
4. Assess: is there an upsell? If so, what take rate and what profit?
5. Assess: is there continuity? What % of core buyers upgrade to continuity?
6. Assess: is there a downsell? How much does it recover from no-buys?
7. Compute the LTV:CAC ratio (use the `ltv-cac` skill)
8. Identify the MOST BROKEN level and prioritize the fix

## Signs of a weak Money Model

- Core offer only, no upsell (CAC pays back slowly, paid doesn't scale)
- No continuity (flat LTV = ratio always tight)
- Upsell take rate < 10% (wrong offer or wrong moment)
- No downsell (loses 70% of the people who said no)
- Core offer with margin < 50% (the model doesn't close)

## Pre-launch validation order

A beginner founder tries to validate all 4 levels at once, burns capital, and can't tell which level failed. The right order is sequential — only move up to the next level when the previous one hits its gate:

> **Source note:** the corpus (`reference/100m-money-models-extracts.md`) anchors the *structure* — the validation sequence, upsell take rate 20-40%, downsell 10-25%, "each level pays for itself." The **specific numeric gates below** (conversion ≥2%, NPS ≥7, ≥20% fake-door, churn ≤8%/mo, ≥200 no-buys, etc.) are practical calibration heuristics, not thresholds quoted verbatim from the book. Adjust by niche/deal-size context.

**1. Core Offer (always first)**
- Question: is there demand, and does it convert?
- Gate: conversion ≥ 2% on a cold LP with paid traffic + NPS ≥ 7 across the first 20 customers.
- Investment: ~30-90 days.
- If it fails here, **do not build the upsell** — go back to the Value Equation and redo the offer.

**2. Upsell (pre-sold)**
- Question: is there interest before I build it?
- How to validate **without building**: survey your Core customers ("If you could get [upsell] for $X, would you buy?"), a fake door (a "Buy upsell" button on the thank-you page that redirects to "in development, reserve your spot"), or a pre-sale at a discount.
- Gate: ≥ 20% of Core customers show explicit interest (survey 4+/5 or fake-door click >20%).
- If < 20%, the upsell offer is wrong — iterate on the upsell, don't build it yet.

**3. Upsell (launched post-checkout)**
- Question: does the real take rate hit 20-40%?
- Gate: ≥ 20% take rate across the first 50 Core customers. If Core + Upsell is still < 3:1 LTV:CAC, go back to pricing before continuing.
- Investment: ~30-60 days building + 30 days collecting data.

**4. Continuity / Recurring**
- Question: have Core+Upsell customers already shown willingness to pay on an ongoing basis?
- How to validate: offer a "preview" version or a waitlist before building the subscription engine.
- Gate: ≥ 15% of Core+Upsell customers engage with continuity within 60 days post-purchase. 90-day churn ≤ 8%/mo.

**5. Downsell (last)**
- Question: how much of the audience that said no can be recovered?
- Build it only after you have at least 200 no-buys catalogued. Before that, a downsell is premature optimization.
- Gate: recover ≥ 10% of the no-buys at a margin ≥ 30%.

**Principle:** Each level must **pay for itself** before you build the next. If the Core doesn't close, the upsell won't fix it. If the upsell has no take rate, continuity is a fantasy.

## Application by use case

| Case | How to use Money Models |
|---|---|
| Sales LP | The core LP shows the upsell page post-checkout; the downsell appears in an exit popup |
| Ad script | Different ads per level (lead-magnet ads = cheap CPC; core-offer ads = high intent) |
| Business plan | The "Money Model" section projects all 4 levels with take rate, margin, LTV:CAC ratio |

## Detailed reference

See `reference/100m-money-models-extracts.md`.
