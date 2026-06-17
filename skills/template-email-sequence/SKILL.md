---
name: template-email-sequence
description: "Internal output skeleton for the /hormozi-gtm:email command. Loaded by the command, not for direct use."
---

# Template — email-sequence.md

Canonical output skeleton for an email sequence. The `/hormozi-gtm:email` command loads this skill and fills the skeleton below with the user's inputs. Reproduce the exact structure: frontmatter + every section + `{{...}}` placeholders.

```markdown
---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: email
type: {{cold | warm | nurture | re-engagement}}
version: 1
status: draft
created: {{ISO8601}}
client: {{company_slug}}
product: {{product_slug}}
sequence_length: {{N}}
sequence_span_days: {{N}}
frameworks:
  - hook-framework
  - ad-copy-formula
  - value-equation
  - guarantees
humanizer_pass: true
humanizer_mode: full
language: {{language}}
audit_ref: {{path_or_null}}
parent_version: {{path_to_previous_v_or_null}}
---

# Email Sequence — {{type}} for {{product_name}}

## TL;DR

**Type:** {{cold | warm | nurture | re-engagement}}
**Number of emails:** {{N}}
**Sequence span:** {{N}} days (from send to breakup)
**Target ICP:** {{1-line description}}
**Primary CTA across the sequence:** {{ex: book a free 20min audit}}

---

## Sequence strategy

**Main angle:** {{dream outcome | pain | contrarian | secret}}
**Objection we attack:** {{in 1 sentence}}
**Why this type (cold/warm/nurture/re-engagement) fits here:** {{rationale in 2-3 lines}}

---

## Emails

### Email 1 — {{short name, ex: "Opening hook"}}

**Subject:** {{short line, ≤ 50 chars, no clickbait}}
**Timing:** Day 0 (initial send)

**Body:**

> {{Opener line — specific reference to the prospect / recognizable pain}}
>
> {{2-3 lines of agitation: why the problem costs them}}
>
> {{1-2 lines showing you've solved this before (short proof)}}
>
> {{Specific CTA — not "want to chat?", but "I'll send you a 5-page PDF, 10min read"}}
>
> — {{name}}

**Expected metric:** {{target open rate | target reply rate}}

---

### Email 2 — {{short name, ex: "Proof point"}}

**Subject:** {{short line}}
**Timing:** Day {{N}} (+{{N}} days)

**Body:**

> {{Reference to email 1 — "yesterday I sent you about X..."}}
>
> {{Specific case study: real name (with permission), context, numeric before/after}}
>
> {{Tie to the prospect's pain — "if you're in a similar spot..."}}
>
> {{CTA: can be the same as email 1 or vary}}
>
> — {{name}}

---

### Email 3 — {{short name, ex: "Objection reframe"}}

**Subject:** {{short line}}
**Timing:** Day {{N}}

**Body:**

> {{Name the common objection: "Most people who get this email think X..."}}
>
> {{Reframe in 2-3 lines: "But what I've seen across the last N clients is Y..."}}
>
> {{Additional proof: data, number, case}}
>
> {{CTA}}

---

### Email 4 — {{short name, ex: "Value, no ask"}}

**Subject:** {{short line}}
**Timing:** Day {{N}}

**Body:**

> {{Your own educational content — link to a post / video / framework}}
>
> {{Why this content is relevant to the prospect}}
>
> {{No sales CTA — just "thought this might interest you"}}

---

### Email 5 — {{Last attempt | Soft pitch}}

**Subject:** {{short line — genuine scarcity if applicable}}
**Timing:** Day {{N}}

**Body:**

> {{Quick recap of the points from the earlier emails}}
>
> {{Scarcity anchored in an operational fact (a slot, cohort, real deadline) — see scarcity-urgency skill}}
>
> {{More direct final CTA}}

---

### Email 6 — Breakup (optional but recommended)

**Subject:** {{ex: "Closing out follow-up — one last question"}}
**Timing:** Day {{N}}

**Body:**

> {{Honesty: "I'm going to stop writing for now. Before I do, I wanted to ask..."}}
>
> {{1 sincere question — not a pitch — to understand why they didn't reply}}
>
> {{Leave the door open without begging: "If you ever want to pick this back up, just reply."}}
>
> — {{name}}

---

### Email 7 — Re-attempt (optional, 6 weeks later)

**Subject:** {{short line — NEW angle}}
**Timing:** Day {{N+45}}

**Body:**

> {{Acknowledge you reached out before — don't hide it}}
>
> {{New angle (different from email 1) — something that happened since, a new case, a new product feature}}
>
> {{Light CTA}}

---

## Suggested test

**Minimum sample:** 10-15 contacts per type (gives basic statistical signal)

**Metrics to track:**
- **Cold:** reply rate (target: ≥ 5% for qualified prospects)
- **Warm:** click-to-call (target: ≥ 15%)
- **Nurture:** open rate per email + click rate on email 6-7 (the real CTA)
- **Re-engagement:** % who reply "yes, keep going" on email 1

**Iteration criteria:**
- Reply rate < 3% → swap the subject + opener of email 1.
- Open rate consistently < 30% → problem in the subject or domain (reputation).
- Clicks without replies → CTA isn't strong enough, redo emails 3-5.

---

## Anti-patterns

- Emails with no signature or a heavy corporate signature
- "I don't respond to cold outreach emails" (gets flagged by antispam)
- Multiple links in one email (1 CTA, 1 link)
- Shallow personalization ("Hi {Name}!") instead of real research
- A sequence with no breakup — leaves the lead lukewarm indefinitely

---

*Email sequence generated by the hormozi-gtm plugin. Alex Hormozi persona applied. Humanizer (full mode) applied.*
```
