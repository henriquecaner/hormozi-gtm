---
description: The client's first 30 days after the sale. A structured touch cadence, early quick wins to validate the purchase decision, visible value milestones. Cuts early churn (< 30 days) by a typical 40-60%. For consulting, agencies, cohort programs, mid-market B2B SaaS.
argument-hint: "[--product=<slug>] [--ref=<path>] [--duration=14|30|60]"
---

# /hormozi-gtm:client-onboarding

Churn inside 30 days is the cheapest kind to reverse — all it takes is onboarding structure. This skill builds a first-30-days journey with a specific cadence, early quick wins to validate the purchase decision, and visible progress milestones.

## Persona loading

Use `hormozi-persona` to orchestrate. Load the `hormozi-gtm:hormozi-voice` skill via the Skill tool and imitate the register (don't rely on the subagent alone — in Cowork it may not run). Delegate to `leads-strategist` to slot onboarding in as a retention engine (not just as UX).

Generate all client-facing copy in the language set in gtm-context `language` (default English). The voice and brutality rules are language-independent and apply in every language.

## Active skills

- `hormozi-voice`
- `leila-scaling` (5 Star Service framework — the pillar of onboarding)
- `value-equation` (Time Delay — the sooner the client sees value, the better)
- `output-conventions`
- `template-client-onboarding`

## Arguments

| Argument | Behavior |
|---|---|
| (empty) | Interactive mode: asks for product + duration + complexity |
| `--product=<slug>` | Product slug |
| `--ref=<path>` | Refine an existing onboarding |
| `--duration=14\|30\|60` | Onboarding window (default 30 days) |

## Prerequisites

1. `gtm-context.md` exists → loads ICP, offer, average deal size
2. For SaaS: product delivered (not onboarding for a product that doesn't exist yet)
3. For consulting/cohort: contract signed / offer sold

## Flow

### Step 1: Calibrate onboarding complexity

Ask:
- **Average deal size:** under $5k? $5k-30k? over $30k?
- **Expected time-to-first-value:** days? weeks? months?
- **Does the client do it solo or with you?:** self-serve, guided, done-with-you, done-for-you?

Determines duration + intensity:

| Deal size | Time-to-value | Type | Onboarding duration | Touches |
|---|---|---|---|---|
| < $5k | < 7 days | Self-serve | 14 days | 5-7 (email, in-app) |
| $5k-30k | 14-30 days | Guided | 30 days | 8-12 (email + 1-2 calls) |
| > $30k | 30-90 days | Done-with-you | 30-60 days | 12-20 (weekly call + async) |
| Enterprise | 60-180 days | Done-for-you | 60-90 days, structured | Dedicated team + progress dashboard |

### Step 2: Structure by milestones (not by days)

Onboarding that works runs on **outcomes**, not on a timeline. Each milestone delivers concrete value.

**Default 30-day structure (guided, $5k-30k deal size):**

- **Milestone 0 (Day 0):** Welcome — confirm the decision, set the expectation, schedule kickoff.
- **Milestone 1 (Day 1-3):** Kickoff call — align on the goal + first data/inputs from the client.
- **Milestone 2 (Day 7):** First visible deliverable (quick win) — something tangible the client can show their boss/team.
- **Milestone 3 (Day 14):** NPS-like check-in + second deliverable.
- **Milestone 4 (Day 21):** Mid-point review — align the next 4 weeks, adjust scope if needed.
- **Milestone 5 (Day 30):** Onboarding wrap-up + transition to the operational phase + formal NPS.

### Step 3: Touches per milestone

Each milestone has specific touches:

**Email + In-app (every deal size):**
- Welcome (D0)
- Quick win achievement (D7)
- NPS check-in (D14)
- Mid-point recap (D21)
- 30-day wrap-up (D30)

**Calls ($5k+):**
- Kickoff (D1-3)
- Mid-point review (D21)
- 30-day formal (D30)

**Extra calls ($30k+):**
- Weekly check-in (D7, D14, D21, D28)

### Step 4: Early quick wins — the load-bearing piece

The most important element of onboarding: the client needs to see concrete value before D7. Without a quick win, post-purchase doubt ("did I buy the right thing?") turns into churn by D60.

A quick win has to be:
- **Visible**: the client can show it to others (boss, team).
- **Attributable**: it's clear it happened because of you.
- **Fast**: < 7 days.
- **Modest if needed**: it doesn't have to be transformational. It can be "we mapped your 3 biggest bottlenecks clearly" or "first audit report with 5 immediate actions".

For each product, identify which quick win lands at Milestone 2 (D7).

### Step 5: Intervention triggers

Define thresholds that fire an action:

- Client didn't reply to the welcome email in 48h → direct DM from the CS lead.
- Client didn't show up to the kickoff call → reschedule + take their temperature.
- Milestone 2 (D7) with no confirmed quick win → internal escalation.
- Day-14 NPS < 7 → dedicated call within 48h with the decision-maker.
- 0 logins (SaaS) in 10 days → automatic trigger fires.

### Step 6: Onboarding success metrics

- **% who complete milestone 5 (D30):** target ≥ 90%.
- **Day-14 NPS:** target ≥ 8.
- **Time-to-quick-win:** target ≤ 7 days.
- **% of touches replied to:** target ≥ 70%.
- **Day-90 retention** (correlated): target ≥ 85% if onboarding worked.

### Step 7: Raw voice (no humanizer)

client-onboarding is internal — it does NOT go through the humanizer. It ships raw, brutal Hormozi, direct.

### Step 8: Save

`outputs/client-onboarding/onboarding-{product_slug}-{YYYYMMDD}-v{n}.md`. Load the `hormozi-gtm:template-client-onboarding` skill via the Skill tool and fill in the skeleton.

### Step 9: Preview in the conversation

```
✅ Saved to: outputs/client-onboarding/onboarding-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Duration: {{N}} days
   • Type: {{self-serve | guided | done-with-you | done-for-you}}
   • Milestones defined: {{N}}
   • Total touches: {{N}} ({{email + calls + in-app}})
   • Quick win set for D7: ✓
   • Intervention triggers: {{N}}
   • Voice: raw (no humanizer — internal output)

👉 Next steps:
   1. Train the CS lead on the triggers (30-min role-play)
   2. Set up automated emails in your provider (HubSpot, ActiveCampaign, etc.)
   3. Name a single owner for the day-30 NPS
```

## Definition of done

- [ ] Duration calibrated by deal size + complexity
- [ ] Milestones defined (5 default for 30 days)
- [ ] Specific quick win identified for D7
- [ ] Touches per milestone with format (email/call/in-app) defined
- [ ] Intervention triggers with a quantitative threshold
- [ ] Success metrics + single owner
- [ ] Raw voice (no humanizer — internal output)

## Anti-patterns

- "I'll wing it" onboarding with no structure (the client feels it)
- Generic welcome email ("Welcome to the family!") in high-ticket B2B
- A fragile quick win (the client can't show it to anyone)
- No intervention trigger (an at-risk client slips by unnoticed)
- Onboarding too long (90 days for a $2k deal = overkill)
- Onboarding too short (7 days for a 6-month program = the client gets lost afterward)
- No single owner (diluted across 3 people = nobody accountable)
- A touch with no purpose (a "just saying hi" email that adds nothing)
