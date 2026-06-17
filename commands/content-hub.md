---
description: 30-90 day organic content roadmap. Topic × format × funnel stage × CTA. Healthy mix (60% educational, 25% entertainment, 15% promotional). For the founder/consultant who wants organic compounding over 6-18 months, not one viral post.
argument-hint: "[--product=<slug>] [--ref=<path>] [--duration=30|60|90] [--platform=linkedin|instagram|youtube|x]"
---

# /hormozi-gtm:content-hub

An operational content plan. Not "post ideas" — a roadmap for a sustainable cadence, with topics mapped to funnel stages, formats per platform, and metrics per quarter.

## Persona loading

Orchestrator: `hormozi-persona`. Delegate to `ad-architect` to distill topics into consumable formats.

Load the `hormozi-voice` skill via the Skill tool and imitate the register (don't rely on the subagent alone — in Cowork it may not run). The roadmap is internal diagnostic/strategy: raw voice, number and verb, zero marketing adjectives, straight to their face. No ≥7 gate, no humanizer here.

The **content pieces produced LATER** from this roadmap are external copy. When they get produced (in other commands: `/hormozi-gtm:hooks`, `/hormozi-gtm:script`), external copy only ships at **brutality ≥7 on the hormozi-voice rubric** and runs through humanizer full. This command, though, only delivers the roadmap — raw.

Generate all client-facing copy in the language set in gtm-context `language` (default English). The voice and brutality rules are language-independent and apply in every language.

## Active skills

- `content-engine` (sustainable cadence, mix, metrics)
- `hook-framework` (every topic becomes a potential hook)
- `ad-copy-formula` (short formats)
- `leila-scaling` (sustainable vs aspirational cadence)
- `hormozi-voice` (voice register — load in-context and imitate)
- `template-content-roadmap` (output skeleton — load in-context)
- `output-conventions`

## Arguments

| Argument | Behavior |
|---|---|
| (empty) | Interactive mode: asks for product + duration + primary platform |
| `--product=<slug>` | Product slug |
| `--ref=<path>` | Refine an existing roadmap |
| `--duration=30\|60\|90` | Roadmap window in days (default 90) |
| `--platform=linkedin\|instagram\|youtube\|x` | Primary platform. Can be multiple. |

## Prerequisites

1. `gtm-context.md` exists → loads ICP, offer, brand voice, tone intensity
2. Founder-market fit defined (skill `founder-market-fit`) — without fit, organic content builds no authority
3. For `--duration=90`: ideally some case study available to slot in as promotional content

## Flow

### Step 1: Calibrate a sustainable cadence

Ask:
- How much time per week can the founder realistically dedicate (real, not aspirational)?
- Is there a content team (strategist, editor)?
- Is there a library of documented cases / frameworks?

Set the cadence:
- Solo, 4-6h/week: 2-3 posts/week on 1 platform.
- Solo + assistant, 8h/week: 3-4 posts/week on 1 platform + repurpose to a 2nd.
- Small team (3 people): 1 post/day on 2-3 platforms.

### Step 2: Define the mix per quarter

Healthy mix (see skill `content-engine`):
- **60% educational** (authority): frameworks, tutorials, public case breakdowns.
- **25% entertainment/contrarian**: hot takes, personal story, failure post.
- **15% promotional**: client case, current offer, "here's what I do".

Early stage (months 1-3): drop promotional to 5-10% (audience still forming).

### Step 3: Map topics to funnel stages

Each topic serves 1 stage of the funnel:

- **Awareness:** a recognizable problem for an audience that does NOT know a solution exists.
- **Consideration:** method/framework breakdown, comparison of approaches.
- **Decision:** case study with a measurable result, FAQ, direct comparison.
- **Retention:** operational tips for existing clients (turns into advocacy).

### Step 4: Weekly calendar

For the window (30/60/90 days), distribute topics across a calendar:

| Week | Topic 1 | Topic 2 | Topic 3 |
|---|---|---|---|
| 1 | {{educ topic}} | {{contrarian}} | {{educ}} |
| 2 | {{educ}} | {{promo - case}} | {{educ}} |
| ... | ... | ... | ... |

### Step 5: Formats per platform

For each topic, suggest the ideal format per platform:

| Topic | LinkedIn | Instagram | YouTube | X |
|---|---|---|---|---|
| {{Pricing framework}} | Long post + carousel | 60s Reel + carousel | 8-12min video | 8-tweet thread |

### Step 6: Repurpose plan

For each anchor piece (long video or article), define 4-6 derivatives:
- 1 LinkedIn post
- 2-3 Reels/Shorts
- 1 X thread
- 1 quote card
- 1 newsletter section

### Step 7: Metrics and review cadence

Set primary metrics per month:
- Month 1-2: reach + save rate
- Month 3-4: inbound DMs + profile views
- Month 6+: leads/month via organic

### Step 8: Raw voice (no humanizer)

The roadmap is internal diagnostic/strategy — it does **NOT** run through humanizer. It ships raw, Hormozi straight. (Humanizer gates external copy only; here it would soften the exact voice that needs to stay sharp.) Keep the `hormozi-voice` register: number and verb, zero marketing adjectives, a realistic cadence laid out to the founder's face.

The content pieces generated from this roadmap (posts, hooks, scripts) are external copy and run through humanizer full **at production time**, in other commands.

### Step 9: Save

Load the `hormozi-gtm:template-content-roadmap` skill via the Skill tool and fill the skeleton (replace every `{{...}}`). Save to:

`outputs/content/content-roadmap-{product_slug}-{YYYYMMDD}-v{n}.md`

### Step 10: Preview in the conversation

```
✅ Saved to: outputs/content/content-roadmap-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Window: {{N}} days
   • Primary platform: {{name}}
   • Cadence: {{N}} posts/week
   • Total pieces in the roadmap: {{N}}
   • Mix: {{N}}% educ / {{N}}% entertain / {{N}}% promo
   • Voice: raw (internal roadmap, no humanizer)

👉 Next steps:
   1. Block 4-6h/week on the calendar for production
   2. Document 1 framework per week (becomes an educational topic)
   3. Track reach + save rate weekly for the first 30 days
```

## Done criteria

- [ ] Cadence defined and realistic (not aspirational)
- [ ] Healthy mix (not 100% promotional or 100% educational)
- [ ] Topics mapped to funnel stages
- [ ] Weekly calendar filled in
- [ ] Repurpose plan for anchor pieces
- [ ] Primary metrics per month defined
- [ ] Raw voice applied (internal roadmap — no humanizer; frontmatter humanizer_pass: false / humanizer_mode: n/a / voice: raw)

## Anti-patterns

- Aspirational cadence (1 post/day with no team)
- 100% promotional mix (turns into a boring ad)
- Topics with no funnel stage (the client loses the thread)
- Wrong platform for the ICP (B2B enterprise on Instagram, B2C on LinkedIn)
- No repurpose (underuses each anchor piece)
- Roadmap with no metrics (no way to measure progress)
- Waiting for viral instead of compounding
