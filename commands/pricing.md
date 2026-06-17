---
description: Pricing review against the 5 laws of the LEAKED Pricing Playbook + Value Equation + LTV:CAC. Analyzes current price, recommends a range, tier structure (silver/gold/platinum), anchoring, and a validation test you can run in 2 weeks.
argument-hint: "[--product=<slug>] [--ref=<path>]"
---

# /hormozi-gtm:pricing

Pricing analysis — no guessing, no "market intuition". Applies the 5 laws of the Pricing Playbook against real data on offer, competition, and unit economics.

## Persona loading

Orchestrator: `hormozi-persona`.
Specialist: `pricing-strategist`.

Load the `hormozi-gtm:hormozi-voice` skill via the Skill tool and imitate the register (don't rely on the subagent alone — in Cowork it may not run).

Generate all client-facing copy in the language set in gtm-context `language` (default English). The voice and brutality rules are language-independent and apply in every language.

## Active skills

- `pricing-playbook` (central — the 5 laws)
- `value-equation` (cross-validation)
- `ltv-cac` (the math)
- `money-models` (ascension structure)
- `hormozi-voice` (raw voice register)
- `template-pricing-review` (output skeleton)
- `output-conventions`

## Arguments

| Argument | Behavior |
|---|---|
| (empty) | Conversation collecting inputs |
| `outputs/pricing/<file>.md` | Refine mode — re-runs with new data |
| `--overwrite` | Overwrites v{n} |

## Prerequisites

1. `gtm-context.md` exists → loads offer + channel + stage
2. Recent offer audit? → cross-check the Value Equation before touching price
3. No recent audit → soft warning: "Without an audit, I might recommend wrong. Want to run `/hormozi-gtm:audit` first?"

## Flow

### Step 1: Collect inputs (5 questions)

1. **Offer + current price** (one-time, installments)
2. **3-5 direct competitors with prices**
3. **Target margin** (gross margin %)
4. **Estimated LTV / churn** (if recurring)
5. **Current sales volume** (clients/month)

Optional question 6: **Is there a high anchor?** (any competitor at 3x+ your price?)

### Step 2: Analysis

Delegate to `pricing-strategist`. Apply the 5 laws:

1. **Compete on value, not price** — diagnosis
2. **Charge what it's worth, not what it costs** — diagnosis
3. **Price signals quality** — diagnosis of the current positioning
4. **Tiering** — are there tiers? do they work? recommended structure
5. **Longer runway, bigger ask** — service period × ask

Each law gets a score (green/yellow/red) + diagnosis + recommendation.

### Step 3: Price vs perception

Conclude: is the problem **price** or **value perception**? Critical distinction.
- If perception: lowering price doesn't fix it. Strengthen Probability in the Value Equation first.
- If price: tier structure + anchoring + installments.

### Step 4: Numeric recommendation

Always a **range**, never a single price.

Proposed tier structure:
- Tier 1 — Silver: $X (entry)
- Tier 2 — Gold (DEFAULT): $Y (60-70% of clients)
- Tier 3 — Platinum: $Z (anchor)

With:
- Rationale per tier (deliverables + audience)
- Explicit anchoring (vs Mentorship C at $X)
- Payment structure (one-time, installments)
- Suggested downsell (for whoever said no)
- Suggested upsell (order bump / OTO post-checkout)

### Step 5: Validation test

Always include:
- Scenario (next 10-20 leads test the new pricing)
- Metrics (conversion rate, AOV, take rate per tier, decision time)
- Success or reversal criterion (objective)

### Step 6: Risks

1-3 risks identified, each with mitigation.

### Raw voice (no humanizer)

pricing is internal — does NOT pass through humanizer. It ships raw, brutal Hormozi, direct.

### Step 8: Save

`outputs/pricing/pricing-{slug}-{YYYYMMDD}-v{n}.md`. Load the `hormozi-gtm:template-pricing-review` skill via the Skill tool and fill in the skeleton.

### Step 9: Preview in chat

```
✅ Saved to: outputs/pricing/pricing-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Current price: ${{X}}
   • Recommendation: ${{Y}} to ${{Z}} (range)
   • Suggested default tier: {{Silver | Gold | Platinum}}
   • Root diagnosis: {{price too low | price too high | weak perception | wrong mix}}
   • 5-law analysis: {{N}}🟢 / {{N}}🟡 / {{N}}🔴
   • Voice: raw (no humanizer)

👉 Next steps:
   1. Share the review with the decision-maker (present the range, defend it with the analysis)
   2. Run a 1-2 week test if the range has more than $1k of spread
   3. /hormozi-gtm:plan --product={{slug}} → if it affects the money model
```

## Done criteria

- [ ] Each of the 5 laws has a score and a rationale
- [ ] Recommendation is a range, not a single number
- [ ] Identifies whether the problem is price OR perception
- [ ] Validation test runnable in 1-2 weeks with a clear metric
- [ ] Risks identified with mitigation
- [ ] Tiering proposed with explicit deliverables

## Anti-patterns

- Recommending a price cut without checking the Value Equation first
- A single price as the recommendation (always a range)
- No validation test ("it'll work")
- No competitive benchmark (a price with no benchmark is a guess)
- A pricing review that never touches the money model (pricing in isolation rarely fixes anything)

## Expected output

File: 1200-2000 words
Chat: ~5 lines with the 5-law analysis (traffic light) + main recommendation + path forward
