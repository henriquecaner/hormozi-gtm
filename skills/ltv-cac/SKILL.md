---
name: ltv-cac
description: Unit economics math — LTV (Lifetime Value), LTGP (Lifetime Gross Profit), CAC (Customer Acquisition Cost), payback period, ratio. Use to validate model viability, calibrate pricing, and justify (or kill) ads.
---

# LTV : CAC Math

Source: Alex Hormozi, *$100M Leads*, Chapter 8 (Paid Ads Part II).

## Definitions

### LTGP — Lifetime Gross Profit
```
LTGP = (Average Price - Average Variable Cost) × Months Retained
```

Use LTGP, not LTV. LTV counts revenue; LTGP counts only what's LEFT after you serve the customer. That's what pays for ads.

### CAC — Customer Acquisition Cost
```
CAC = Total Ad Spend / Customers Acquired
```

Include acquisition tools, the sales headcount you assign, commissions. Not just raw ad spend.

### LTGP : CAC Ratio
```
Ratio = LTGP / CAC
```

**Benchmarks:**
- `< 1:1` — you're losing money. Stop scaling.
- `1:1 to 3:1` — you survive. Doesn't scale well.
- `3:1 to 5:1` — healthy. Scale paid with confidence.
- `> 5:1` — you're leaving money on the table in ad spend. Raise the budget.

### Payback period
```
Payback = CAC / (Monthly Profit per Customer)
```

**Benchmarks:**
- `< 30 days` — Client-Financed Acquisition. Unlimited paid scaling.
- `30-90 days` — healthy if you have the capital.
- `> 90 days` — risk of a cash crunch as you scale.

> **Source note:** the canonical thresholds in the corpus (`reference/100m-leads-extracts.md`) are **ratio ≥ 3:1** and **payback ≤ 30 days**. The intermediate bands (1:1–3:1, 3:1–5:1, >5:1, 30–90, >90) are practical/heuristic calibration for diagnosis — not numbers quoted verbatim from the book.

## How to model from scratch

1. **Average sale price:** single deal size + average upsell × take rate
2. **Average variable cost:** cost to serve 1 customer (not overhead)
3. **Average retention:** if one-time, 1; if recurring, average months before churn
4. **LTGP = (Price - Cost) × Retention**
5. **Current or target CAC**
6. **Ratio and payback**

## Example (digital course + community)

```
Core offer: $4,997 one-time
Upsell take rate: 30% × $1,997 = $599 expected
Continuity: 20% upgrade × $297/mo × 6 months = $357 expected
Blended average price: $4,997 + $599 + $357 = $5,953
Variable cost: $350 (hosting + support + payment processing)
LTGP = $5,953 - $350 = $5,603

Target paid CAC: $1,200
Ratio = 5,603 / 1,200 = 4.67:1 ✓
Payback = 1,200 / 1,997 (upsell profit within 30 days) = ~18 days ✓
```

Both benchmarks pass. Scale paid.

## Trouble signals

- LTGP < 2x CAC → pricing too low or churn too high
- Payback > 6 months → cash-intensive model, demands capital
- Ratio drops as you scale → CAC rising faster than LTGP (channel saturation)
- LTV high but LTGP low → bad margin, fix delivery or price

## When to use this skill

| Case | Application |
|---|---|
| Offer audit | Compute current ratio and identify whether the problem is revenue or cost |
| Pricing review | Justify a new price range via target ratio |
| Business plan | Unit-economics section with conservative/realistic/optimistic scenarios |

## Detailed reference

See `reference/100m-leads-extracts.md` (Paid Ads + Money Math section).
