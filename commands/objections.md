---
description: Objection matrix by ICP. Every objection mapped to a root cause (offer / price / timing), a two-sentence reframe, a word-for-word sales-call script, and an offer-side mitigation. For the consultant on a sales call and the founder mapping recurring objections.
argument-hint: "[--product=<slug>] [--ref=<path>] [--segment=<icp_subset>]"
---

# /hormozi-gtm:objections

An operational objection matrix. Not a "list of canned answers" — a structured diagnostic: why this objection shows up, what it reveals about the offer, and what to say when it does.

## Persona loading

Use `hormozi-persona` to orchestrate. Delegate to `offer-architect` when the root objection is about the offer, `pricing-strategist` when it's about price.

Load the `hormozi-voice` skill via the Skill tool and **imitate the register** (number and verb, zero marketing adjectives, reframe to the prospect's face). Don't rely on the subagent alone — in Cowork it may not run; the voice has to be loaded in-context inside this command. The objection matrix is internal, raw diagnostic: direct scripts, no softening.

Generate all client-facing copy in the language set in gtm-context `language` (default English). The voice and brutality rules are language-independent and apply in every language.

## Active skills

- `hormozi-voice` (always — voice register loaded in-context)
- `template-objections-matrix` (always — output skeleton)
- `value-equation` (objection diagnosis)
- `grand-slam-offer` (offer-side mitigation)
- `pricing-playbook` (price objections)
- `guarantees` (reframe via guarantee)
- `output-conventions`

## Arguments

| Argument | Behavior |
|---|---|
| (empty) | Interactive mode: asks for product + segment + common objections |
| `--product=<slug>` | Product slug (reads from gtm-context.md) |
| `--ref=<path>` | Refine an existing matrix |
| `--segment=<icp_subset>` | Focuses on an ICP sub-segment (e.g. B2B fintech SaaS) |

## Prerequisites

1. `gtm-context.md` exists → loads ICP, offer, current price
2. Recent audit (≤30 days)? → loads it as `audit_ref`. If missing, asks interactively (3 options)
3. Ideally: qualitative data from real sales calls (transcripts, notes) — feeds the personalization

## Flow

### Step 1: Collect objections

Interactive mode: ask for the 3-5 objections that come up most in sales calls. If possible, with a short example transcript (the prospect's exact words).

### Step 2: Categorize root cause

Every objection maps to 1 of 4 categories:

- **Offer:** the prospect doesn't see enough value (a Value Equation problem).
- **Price:** the prospect sees the value but resists the number (a pricing problem).
- **Timing:** the prospect sees the value and accepts the price but not now (an urgency/scarcity problem).
- **Trust:** the prospect doubts the delivery or the person (a proof / founder-market fit problem).

### Step 3: Diagnose each objection

For every objection:
- The typical phrasing it shows up as
- Root cause (one of the 4 categories)
- What the objection REALLY means (often different from what the prospect says out loud)
- Reframe in 2 sentences (the consultant's exact line on the sales call)
- Offer-side mitigation (a change that makes the objection show up less)

### Step 4: Word-for-word scripts

For the top 3-5 objections:
- Qualifying question ("before I answer, can I understand...")
- Reframe (2-3 sentences)
- Closing question ("does that make sense? want to keep going?")

### Step 5: Raw voice (no humanizer)

objections is internal — it does NOT go through the humanizer. It ships raw, brutal Hormozi, direct. Hold the `hormozi-voice` register: number and verb, reframe to the prospect's face, no softening. The word-for-word scripts carry that direct voice — the consultant adapts the tone live on the sales call.

### Step 6: Save

Load the `hormozi-gtm:template-objections-matrix` skill via the Skill tool and fill in the skeleton. Save to `outputs/objections/objections-{product_slug}-{YYYYMMDD}-v{n}.md`.

In the output frontmatter (already reflected in the skeleton): `humanizer_pass: false`, `humanizer_mode: n/a`, `voice: raw`.

### Step 7: Preview in the conversation

```
✅ Saved to: outputs/objections/objections-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Total objections mapped: {{N}}
   • Distribution by root cause:
     - Offer: {{N}} ({{N}}%)
     - Price: {{N}} ({{N}}%)
     - Timing: {{N}} ({{N}}%)
     - Trust: {{N}} ({{N}}%)
   • Top 3 objections with full script: ✓
   • Voice: raw (internal diagnostic, no humanizer)

👉 Next steps:
   1. Train your SDR/closer on the top 3 scripts (30-min role-play)
   2. If Offer dominates → /hormozi-gtm:audit to strengthen Probability/Effort
   3. If Price dominates → /hormozi-gtm:pricing to restructure tiering
```

## Definition of done

- [ ] ≥ 5 objections mapped
- [ ] Each objection has a categorized root cause
- [ ] Top 3 have a word-for-word script
- [ ] Cross-cut diagnosis: are most objections offer? price? timing?
- [ ] Offer-side mitigation listed (suggested changes to make these objections show up less)
- [ ] Raw voice held (no humanizer — internal diagnostic)

## Anti-patterns

- Scripts that turn into a "canned answer" anyone spots in 30 seconds
- A reframe that ignores the real objection (answers a different question)
- Treating a timing objection like a price objection (a big discount doesn't fix it)
- Skipping the qualifying question before the reframe (loses critical info)
- A matrix with 20+ objections (the consultant won't memorize it — focus on the top 5)
