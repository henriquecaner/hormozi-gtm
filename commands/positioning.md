---
description: Competitive teardown + positioning statement. Maps 3-5 direct competitors (features, price, persona, message), finds the differentiation axes, proposes a testable positioning statement. For a founder entering a niche with established competitors, or one who feels their message is "indistinguishable".
argument-hint: "[--product=<slug>] [--ref=<path>] [--competitors=<N>]"
---

# /hormozi-gtm:positioning

Positioning isn't "how you describe yourself". It's **where you sit in the prospect's head** when they compare you against the alternatives. This skill maps the terrain, finds your one axis, and produces a testable statement.

## Persona loading

Use `hormozi-persona` to orchestrate. Delegate to `offer-architect` to run the Value Equation against competitors. Load the `hormozi-gtm:hormozi-voice` skill via the Skill tool and imitate the register (don't rely on the subagent alone — in Cowork it may not run).

Generate all client-facing copy in the language set in gtm-context `language` (default English). The voice and brutality rules are language-independent and apply in every language.

## Active skills

- `hormozi-voice` (raw Hormozi register in the diagnostic)
- `value-equation` (compares vectors between you and competitors)
- `grand-slam-offer` (positioning becomes hero copy)
- `pricing-playbook` (price positioning vs the market)
- `niche-selection` (saturation helps pick the axes)
- `template-positioning-map` (output skeleton)
- `output-conventions`

## Arguments

| Argument | Behavior |
|---|---|
| (empty) | Interactive mode: asks for product + competitors |
| `--product=<slug>` | Product slug |
| `--ref=<path>` | Refine an existing positioning |
| `--competitors=<N>` | Number of competitors to map (default 4) |

## Prerequisites

1. `gtm-context.md` exists → loads ICP, offer, current price
2. Ideally: a list of 3-5 competitors the client would already consider (prior research)
3. For price analysis: public pricing data on the competitors

## Flow

### Step 1: Collect competitors

In interactive mode, ask:
- Who are 3-5 direct competitors (same problem, same ICP)?
- One competitor with more premium positioning (high anchor)?
- One competitor with cheaper positioning (low anchor)?
- One non-obvious substitute (something the client would do instead of buying this category)?

### Step 2: Mapping matrix

Build a matrix with:

| Competitor | Stated positioning | Price | Primary ICP | Key message | Perceived strength | Perceived weakness |
|---|---|---|---|---|---|---|

For each competitor, fill every column with a concrete observation (not creative interpretation).

### Step 3: Find the differentiation axes

Possible axes:
- **Unique problem solved** (we solve a specific X nobody else attacks)
- **Speed** (3 days vs 3 weeks)
- **Specificity** (B2B fintech SaaS vs B2B SaaS in general)
- **Founder-market fit** (ex-CFO consulting ex-CFOs)
- **A unique conditional guarantee**
- **Proprietary methodology**
- **Price** (high or low anchor)
- **Format** (1:1 enterprise vs group vs self-serve)

For each axis, check: can you defend it with an auditable fact?

### Step 4: Differentiation by dimension

For the 2-3 axes where you're defensible:

```
Axis: {{Implementation speed}}

Competitors:
- A: 4-6 weeks
- B: 3-4 weeks
- C: 2-3 weeks
You: 5 days.

Defense: case study X (Stark, Cora) where implementation took 5 documented days.
Structural reason: a 4-session onboarding framework vs the 12 most others run.
```

### Step 5: Positioning statement

Standard structure:

> "For [specific ICP], [company] is the only one that [unique value proposition] without [common trade-off]."

Example:
> "For B2B SaaS with sales cycles over 60 days, LEVEL is the only one that cuts the cycle by 40% in 5 days of implementation without rewriting copy or swapping out the SDR team."

**Statement quality test:**
- Specific ICP (not generic "B2B")?
- Measurable unique value (not "we transform your funnel")?
- Explicit trade-off (the client knows what they DON'T have to give up)?
- Can you back it with a real case?

### Step 6: Application

Generate derivatives:
- Hero copy for the LP (3 variations)
- Cold email subject lines (3 variations)
- LinkedIn bio (1)
- Sales call opening line (1)

### Step 7: Raw voice (no humanizer)

positioning is internal — does NOT pass through humanizer. It ships raw, brutal Hormozi, direct.

### Step 8: Save

`outputs/positioning/positioning-{product_slug}-{YYYYMMDD}-v{n}.md`. Load the `hormozi-gtm:template-positioning-map` skill via the Skill tool and fill in the skeleton.

### Step 9: Preview in chat

```
✅ Saved to: outputs/positioning/positioning-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Competitors mapped: {{N}}
   • Defensible differentiation axes: {{N}}
   • Positioning statement:
     "{{first 100 chars}}..."
   • Derivatives: 3 hero copies + 3 cold subjects + 1 LinkedIn bio
   • Voice: raw (no humanizer)

👉 Next steps:
   1. Test the positioning statement in an ad headline ($200 ad)
   2. Update the LP hero with the new version
   3. /hormozi-gtm:lp to rewrite the full LP with the new positioning
```

## Done criteria

- [ ] ≥ 3 competitors mapped with concrete data
- [ ] ≥ 2 defensible differentiation axes (backed by an auditable fact)
- [ ] Positioning statement passes the quality test
- [ ] Derivatives generated (hero, cold subject, bio)
- [ ] Output raw (no humanizer — internal diagnostic)

## Anti-patterns

- Differentiation with no fact (claim with no case behind it)
- Generic positioning ("the best growth consultancy")
- Competing on an axis that already has 5+ players (no differentiation)
- Invisible trade-off (client doesn't know what they lose by choosing you)
- A positioning statement only you understand (a stranger doesn't get it on one read)
