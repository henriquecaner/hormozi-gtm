---
description: Complete business plan (3000-6000 words) for a company or product. Structured into 10 sections — summary, market, offer, money model, pricing, acquisition, operations, metrics, risks, 30-60-90 roadmap. Uses Money Models, LTV:CAC, Core Four, Pricing Playbook, Leila Scaling.
argument-hint: "[--product=<slug>] [--ref=<path>] [--type=company|product]"
---

# /hormozi-gtm:plan

A structured business plan. Not an investor deck — an operational document that defines how the business makes money predictably.

## Persona loading

Orchestrator: `hormozi-persona`.
Money model: delegate to `money-model-architect`.
Pricing: delegate to `pricing-strategist`.
Acquisition: delegate to `leads-strategist`.

Load the `hormozi-gtm:hormozi-voice` skill via the Skill tool and imitate the register (don't rely on the subagent alone — in Cowork it may not run).

Generate all client-facing copy in the language set in gtm-context `language` (default English). The voice and brutality rules are language-independent and apply in every language.

## Active skills

- `money-models` (4 levels: attraction/core/upsell/continuity)
- `ltv-cac` (unit economics math)
- `core-four` (channel mix)
- `pricing-playbook` (5 laws)
- `leila-scaling` (operations, hiring, metrics)
- `grand-slam-offer` (core offer)
- `value-equation` (offer validation)
- `hormozi-voice`
- `template-plan`
- `output-conventions`

## Arguments

| Argument | Behavior |
|---|---|
| (empty) | Asks for type (company/product) |
| `slug` | Creates a plan with the slug |
| `outputs/plan/<file>.md` | Refine mode — asks which section to update |
| `--type=company` | Plan for the whole company |
| `--type=product` | Plan for a specific product/SKU |
| `--overwrite` | Overwrites v{n} |

## Prerequisites

1. `gtm-context.md` exists → loads as much as possible
2. Recent audit? → soft warning if missing (but doesn't block)
3. Recent pricing review? → loads it as `pricing_ref` if it exists

## Flow

### Step 1: Structured intake (6 questions)

One at a time:

1. **Category/market** — in 1 sentence
2. **Detailed ICP** — segment + size + role + pain
3. **Core offer and price**
4. **Model** — one-time, recurring, hybrid
5. **Planned acquisition channels** — Core Four split in %
6. **12-month target** — revenue, # of clients, target margin

Optional question 7: **Market size** (TAM/SAM/SOM if estimated)
Optional question 8: **Biggest perceived risk**

### Step 2: Analysis

Delegate in parallel (in functional sequence):

- **`money-model-architect`** builds the 4 levels (attraction/core/upsell/continuity) with the math
- **`pricing-strategist`** validates pricing against the 5 laws + competition
- **`leads-strategist`** validates the channel mix against the company's stage
- The main agent compiles Operations (Leila Scaling), Metrics, and the 30-60-90 Roadmap

### Step 3: Critical calculations

Always include:
- LTGP calculated (not guessed)
- Intended or current CAC
- LTGP:CAC ratio (target ≥3:1)
- Payback period (target ≤30 days)

If the ratio is <3:1, the plan flags it explicitly as a critical risk and suggests a fix before scaling.

### Raw voice (no humanizer)

plan is internal — it does NOT go through the humanizer. It ships raw, brutal Hormozi, direct.

### Step 5: Save

`outputs/plan/plan-{slug}-{YYYYMMDD}-v{n}.md`. Load the `hormozi-gtm:template-plan` skill via the Skill tool and fill in the skeleton. The `type` discriminator (company | product) goes in the frontmatter, not in the filename.

### Step 6: Preview in the conversation

```
✅ Saved to: outputs/plan/plan-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Type: {{company | product}}
   • LTV:CAC: {{N}}:1 ({{✓ green | ⚠️ yellow | ❌ red}})
   • Payback: {{N}} days (target < 30)
   • Risks identified: {{N}}
   • Counterintuitive recommendation: "{{short text}}"
   • Voice: raw (no humanizer)

👉 Next steps:
   1. Validate projections against real unit economics (3 months of data)
   2. /hormozi-gtm:audit before touching the Core (if ratio < 3:1)
   3. /hormozi-gtm:pricing --product={{slug}} if the tier mix needs adjusting
```

## Definition of done

- [ ] Executive summary fits on 1 page
- [ ] LTGP:CAC ratio modeled with numbers (not a vague estimate)
- [ ] Money Model has 4 levels (or a justification if a level doesn't apply)
- [ ] Core Four mix has a numeric allocation (explicit % per channel)
- [ ] Weekly and monthly metrics defined
- [ ] 30-60-90 roadmap has executable actions (not vague guidelines)
- [ ] Risks identified with mitigation
- [ ] Raw voice (no humanizer) — internal output

## Anti-patterns

- "Let's focus on everything" — Core Four demands a numeric split
- LTGP:CAC with no numbers (a guess disguised as a plan)
- Money Model with only a core offer (no upsell, no continuity = CAC pays back slowly)
- Generic roadmap ("scale marketing")
- No risks identified (a plan with no risk is a fake plan)

## Expected output

File: 3000-6000 words, 10 sections
Conversation: 5-10 lines with ratio + payback + 1-3 critical risks + the path
