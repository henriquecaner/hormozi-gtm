---
name: template-webinar-agenda
description: "Internal output skeleton for the /hormozi-gtm:webinar command. Loaded by the command, not for direct use."
---

# Template — webinar-agenda.md

Canonical output skeleton for a webinar. The `/hormozi-gtm:webinar` command loads this skill and fills the skeleton below with the user's inputs. Reproduce the exact structure: frontmatter + every block + `{{...}}` placeholders.

````markdown
---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: webinar
version: 1
status: draft
created: {{ISO8601}}
client: {{company_slug}}
product: {{product_slug}}
duration_min: {{30 | 45 | 60}}
format: {{zoom | youtube | prerecorded}}
frameworks:
  - hook-framework
  - vsl-7-step
  - grand-slam-offer
  - value-equation
  - guarantees
humanizer_pass: true
humanizer_mode: full
language: {{language}}
audit_ref: {{path_or_null}}
parent_version: {{prior_version_path_or_null}}
---

# Webinar — {{product_name}}

## Overview

**Webinar title:** {{punchy title, ≤ 60 chars}}
**Subtitle / promise:** {{1 line with a specific Dream Outcome}}
**Planned length:** {{N}} min
**Format:** {{zoom (live) | youtube | prerecorded}}
**Target ICP:** {{1-line description}}
**Primary CTA:** {{e.g.: "book a 30min strategy audit"}}

---

## Agenda — block by block

| Block | Time | Topic | Function |
|---|---|---|---|
| 1. Open + housekeeping | 0:00-0:03 | Hook + agenda + Q&A rules | Grabs attention, sets expectations |
| 2. Problem diagnosis | 0:03-0:11 | How it shows up, the cost, why nobody fixes it | Establishes pain + authority |
| 3. Named mechanism | 0:11-0:23 | Signature framework + 4-6 components | Teaches, becomes the reference |
| 4. Cases | 0:23-0:31 | 2-3 numeric before/after | Proof of Probability |
| 5. Offer + bonuses + guarantee | 0:31-0:38 | Grand Slam + visual tier + scarcity | Sells |
| 6. Q&A | 0:38-0:43 | Live (real) or scripted (prerecorded) | Breaks objections, reinforces authority |
| 7. Close + CTA | 0:43-0:45 | Final direction + next steps | Moves to action |

(Scale proportionally for 30min or 60min.)

---

## Block 1 — Open (0:00-0:03)

### Hook (first 30 seconds — critical)

> "{{Hook written out in full. Hormozi voice, first person. Passes the tweet-test: read in isolation it opens a curiosity gap. E.g.: 'The B2B SaaS companies that scale from $5M to $50M ARR all share one thing nobody talks about. And it's not the founder, not capital, not product-market fit.'}}"

### Agenda announced

> "Over the next {{N}} minutes we're going to cover 4 things:
> 1. {{topic 1}}
> 2. {{topic 2}}
> 3. {{topic 3}}
> 4. {{topic 4}}
>
> At the end, I'll open Q&A for {{N}} minutes."

### Housekeeping (Q&A)

> "{{Q&A rule — e.g.: 'Drop questions in the chat anytime, I'll answer the best ones at the end. If you have to leave early, the recording will be available in 24h.'}}"

---

## Block 2 — Diagnosis (0:03-0:11)

### How the problem shows up

{{2-3 paragraphs describing the problem from the ICP's point of view. Not "theory" — concrete symptoms. E.g.:}}

> "You run $30k/mo on Meta Ads, generate 200 qualified leads, but the B2B sales cycle stalls at 75 days. Your SDR team added 2 people and conversion per SDR halved. The customer signs, but takes 90 days to complete onboarding. Every one of those months burns $80k in CAC with no return."

### Cost of the problem

> "{{Quantify it. Not 'expensive'. $X per month of lost opportunity + Y of overhead + Z of team morale.}}"

### Why nobody fixes it

> "{{Contrarian reframe. E.g.: 'Most consultants attack this as a sales-page copy problem. It isn't. Copy doesn't move a B2B buying committee. What moves it is the communication framework applied at the SDR stage, before the lead ever hits the sales call.'}}"

---

## Block 3 — Named mechanism (0:11-0:23)

### Name of the framework

**{{Proper name of the framework}}**

> {{1 sentence defining what it is}}

### The {{N}} components

**Component 1: {{Name}}**
- {{1-2 paragraphs explaining}}
- Why it matters: {{in 1 line}}

**Component 2: {{Name}}**
- {{description}}

**Component 3: {{Name}}**
- {{description}}

**Component 4: {{Name}}**
- {{description}}

(Keep it to 4-6 components — more is confusing, fewer is shallow.)

---

## Block 4 — Cases (0:23-0:31)

### Case 1: {{Customer}}

- **From:** {{before in 1 line}}
- **To:** {{after in 1 line}}
- **In:** {{time}}
- **Mechanism applied:** {{components 1, 2}}
- **Quote:** "{{customer line}}"

### Case 2: {{Customer}}

[same structure]

### Case 3: {{Customer, optional}}

[same structure]

---

## Block 5 — Offer + Bonuses + Guarantee (0:31-0:38)

### The offer — {{Proper name of the offer}}

**What you get:**
- {{named deliverable 1}}
- {{deliverable 2}}
- {{deliverable 3}}

**In how long:** {{specific timeframe}}

### Bonus stack (3-5, odd number)

- **{{Bonus 1 — name via naming psychology}}** (${{value}})
- **{{Bonus 2}}** (${{value}})
- **{{Bonus 3}}** (${{value}})

(Total stack value: ${{X}})

### Guarantee

> "{{Conditional + metric + compensation. E.g.: 'In 90 days your B2B sales cycle is cut by 40% or we refund the investment + a $10,000 bonus.'}}"

### Investment

**Default tier (Gold):** ${{Y}}/mo or ${{N×Y with discount}}/yr paid in full.

Show the 3 tiers visually (Silver / Gold highlighted / Platinum).

### Genuine scarcity

> "{{Operational reason for the limit. E.g.: 'Next cohort starts August 12. I have 6 spots to keep the framework at one hour per client per week.'}}"

---

## Block 6 — Q&A (0:38-0:43)

### Plant questions (live) or Scripted Q&A (prerecorded)

**Question 1:** {{common objection 1}}
> Answer: {{2-3 sentences. Hormozi voice. Reframe.}}

**Question 2:** {{common objection 2}}
> Answer: {{...}}

**Question 3:** {{common objection 3}}
> Answer: {{...}}

**Question 4:** {{price objection}}
> Answer: {{...}}

**Question 5:** {{timing objection}}
> Answer: {{...}}

---

## Block 7 — Close + CTA (0:43-0:45)

### Recap (30 seconds)

> "{{Summary in 2-3 sentences: the problem, the mechanism, the offer.}}"

### Specific CTA

> "{{Exact direction. Not 'visit the site'. Something like: 'Click the link in the chat. You'll land on a page with a 5-minute application. Anyone who applies in the next 48h, I review personally and reply on whether it's a fit.'}}"

### Next steps

> "{{Confirm timing: 'Applications open until [date]. Apply in that window and you get a reply within 72h.'}}"

---

## Production notes

### Slides (suggestions)

- Slide 1 (Hook): big text, no decoration. 1 sentence.
- Slides 2-4 (Diagnosis): 1 symptom per slide, with a number.
- Slides 5-10 (Mechanism): 1 component per slide + icon.
- Slides 11-13 (Cases): 1 case per slide, before/after big.
- Slide 14-15 (Offer): Silver/Gold/Platinum tiering visual.
- Slide 16 (Guarantee): visual highlight.
- Slide 17 (CTA): big URL + QR code.

### Minimum equipment (live)

- 1080p camera (a modern smartphone works).
- External mic (not the laptop built-in).
- Neutral or branded background.
- Front lighting (key light).
- Internet ≥ 50 Mbps.

### For prerecorded

- 3 takes minimum per block.
- Edit in a simple tool (Descript, Riverside).
- Add pattern interrupts (zoom in, cut to b-roll) every 90 seconds.

---

*Webinar generated by the hormozi-gtm plugin. Alex Hormozi persona applied. Humanizer (full mode) applied.*
````
