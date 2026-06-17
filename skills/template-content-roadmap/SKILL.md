---
name: template-content-roadmap
description: "Internal output skeleton for the /hormozi-gtm:content-hub command. Loaded by the command, not for direct use."
---

# Template — content-roadmap.md

Canonical output skeleton for the `/hormozi-gtm:content-hub` command. The command loads this skill and fills the skeleton below with the user's inputs. Reproduce the exact structure: frontmatter + every section + `{{...}}` placeholders.

The roadmap is internal diagnostic/strategy — it ships raw, no humanizer. The frontmatter already carries `humanizer_pass: false`, `humanizer_mode: n/a`, `voice: raw`. (The content pieces produced LATER, from this roadmap, are external copy and go through full humanizer at production time.)

```markdown
---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: content-hub
version: 1
status: draft
created: {{ISO8601}}
client: {{company_slug}}
product: {{product_slug}}
duration_days: {{30 | 60 | 90}}
primary_platform: {{linkedin | instagram | youtube | x}}
secondary_platforms: [{{list or empty}}]
posts_per_week: {{N}}
frameworks:
  - content-engine
  - hook-framework
  - ad-copy-formula
  - leila-scaling
humanizer_pass: false
humanizer_mode: n/a
voice: raw
language: {{language}}
parent_version: {{path_to_previous_v_or_null}}
---

# Content Roadmap — {{product_name}}

## Overview

**Period:** {{N}} days
**Primary platform:** {{name}}
**Secondary platforms:** {{names or "none"}}
**Sustainable cadence:** {{N}} posts/week
**Total content planned:** {{N}}

**Planned mix:**
- Educational: {{N}}% ({{X}} posts)
- Entertainment/Contrarian: {{N}}% ({{X}} posts)
- Promotional: {{N}}% ({{X}} posts)

---

## Central theme for the period

**Pillar message:** {{1 sentence that connects all output for the period. Ex: "A B2B SaaS founder can cut sales-cycle length 60% without swapping SDRs or raising budget."}}

---

## Topics by funnel stage

### Awareness (recognizable problem)

1. {{Topic — ex: "Why B2B sales cycles stay 90+ days even with a good product"}}
2. {{...}}
3. {{...}}

### Consideration (method/framework breakdown)

1. {{Topic — ex: "The 3 elements of the SDR script that move conversion most"}}
2. {{...}}
3. {{...}}

### Decision (case study, FAQ, comparison)

1. {{Case — Acme Corp cut its cycle from 90 to 28 days in 3 months}}
2. {{FAQ — "Can I apply this without swapping the team?"}}
3. {{Comparison — "Growth consultancy vs. internal workshop"}}

### Retention (advocacy)

1. {{Operational tip — only for existing clients, but drives advocacy via shares}}

---

## Weekly calendar

### Week 1

| Day | Platform | Topic | Funnel stage | Format | CTA |
|---|---|---|---|---|---|
| {{Mon}} | {{LinkedIn}} | {{topic}} | {{stage}} | {{long post}} | {{none / soft}} |
| {{Wed}} | {{LinkedIn}} | {{topic}} | {{stage}} | {{carousel}} | {{...}} |
| {{Fri}} | {{LinkedIn}} | {{topic}} | {{stage}} | {{short post}} | {{...}} |

### Week 2

[same structure]

### Week 3

[...]

### Week 4

[...]

(Continues for the full defined period.)

---

## Repurpose plan

For each pillar piece (long video or 1500+ word article), produce:

| Source | LinkedIn | Instagram | YouTube | X | Newsletter |
|---|---|---|---|---|---|
| Pricing Playbook article | 1 long post | 1 carousel | 1 short 5min video | 1 thread (8 tweets) | 1 section |
| SDR script framework | 1 short post | 2 Reels (60s) | 1 12min video | 1 thread (6 tweets) | 1 section |

Principle: 1 pillar piece → 4-8 derivatives reaching a different audience.

---

## Formats by platform

### LinkedIn (primary)

| Format | Frequency | Length | Role |
|---|---|---|---|
| Long post (educational) | 2x/week | 1500-2500 chars | Authority |
| Carousel | 1x/week | 6-10 slides | Save-friendly |
| Story / quick take | 1x/week | 300-600 chars | Engagement |

### Instagram (secondary, if applicable)

| Format | Frequency | Length | Role |
|---|---|---|---|
| Reel 60s | 2x/week | 60s | Organic reach |
| Carousel | 1x/week | 5-10 slides | Save |
| Story | daily | n/a | Daily connection |

---

## Metrics and review cadence

### Month 1-2 (foundation)

**Primary metrics:**
- Total reach
- Save rate per post
- Profile views

**Realistic target:**
- Reach growing 10-20%/month
- Save rate > 2% on educational
- 50+ profile views/post on average

**Weekly review:** look at the week's top 1 and bottom 1, log the pattern.

### Month 3-4 (consistency + first leads)

**Primary metrics:**
- Qualified inbound DMs / week
- Link clicks (lead magnet or LP)
- 1-3 first deals via organic

**Target:**
- 2-5 qualified inbound DMs/week
- 1-3 first clients via organic

### Month 6+ (stable channel)

**Primary metrics:**
- Leads/month via organic
- CAC via organic vs paid
- % of revenue attributed to organic

**Target:**
- 20-50 leads/month
- Organic CAC < 50% of paid
- Organic accounts for 20-40% of new clients

---

## Operating principles

1. **Sustainable cadence > viral.** 50 average posts > 1 viral + 49 bad ones.
2. **One primary platform first.** Don't spread across 4 platforms in month 1.
3. **Document > Invent.** Every framework used on a project becomes a topic.
4. **Obsessive repurpose.** 1 pillar piece → 4-8 derivatives.
5. **3-6 month lag to the first lead.** Whoever quits in month 2 never reaps it.
6. **Founder-voice required.** The audience buys a person, not a brand.

---

## Anti-patterns to avoid

- Aspirational cadence (1 post/day with no team)
- Waiting for viral instead of compounding
- Asking friends for feedback instead of measuring the market
- Comparing yourself to creators 5+ years ahead
- Wrong platform for the ICP
- Posting and never engaging with comments
- No metrics → no adjustment

---

*Content roadmap generated by the hormozi-gtm plugin. Alex Hormozi persona applied. Raw voice — internal diagnostic does not go through humanizer.*
```
