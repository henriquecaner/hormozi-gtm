---
description: Structured case study — numeric before/after, context, mechanism applied, client quote. Produces both the full piece and 1-line assets to drop into an LP, ad, and email. For the consultant who needs to turn a won, delivered project into a proof asset.
argument-hint: "[--client=<name>] [--ref=<path>] [--before=<number>] [--after=<number>] [--no-humanize]"
---

# /hormozi-gtm:case-study

A case study is the currency of Probability in the Value Equation. Without a solid case study, any copy reads as a promise. This skill structures a real case study with a numeric before/after, enough context for the reader to relate, and a named mechanism.

## Persona loading

Use `hormozi-persona` to orchestrate. Delegate to `offer-architect` to tie the before/after to the Value Equation. Final pass through the `humanizer` in **full** mode (the case study goes into external LP/ad/email).

Load the `hormozi-voice` skill and imitate the register (don't rely on the subagent alone — in Cowork it may not run). External copy only ships at brutality ≥7 on the `hormozi-voice` rubric.

Generate all client-facing copy in the language set in gtm-context `language` (default English). The voice and brutality rules are language-independent and apply in every language.

## Active skills

- `hormozi-voice` (voice register — load in-context before writing)
- `template-case-study` (output skeleton — load via the Skill tool)
- `value-equation` (before/after mapped to the 4 vectors)
- `grand-slam-offer` (the case validates the offer's promise)
- `ad-copy-formula` (derived short formats)
- `hook-framework` (the case headline)
- `humanizer-rules` (full mode)
- `output-conventions`

## Arguments

| Argument | Behavior |
|---|---|
| (empty) | Interactive mode: asks for client + before + after + context |
| `--client=<name>` | Client name (with permission) |
| `--ref=<path>` | Refine an existing case study |
| `--before=<number>` | Before number (e.g. CAC $450, cycle 75d, ARR $500k) |
| `--after=<number>` | After number |
| `--no-humanize` | Skips the humanizer (debug) |

## Prerequisites

1. `gtm-context.md` exists → loads ICP, offer
2. A real client with permission to use their name, or consented anonymity
3. Quantitative before/after data (not an "intuitive" case)

## Flow

### Step 1: Structured data collection

In interactive mode, ask in sequence:

1. **Client identification** (real name or consented pseudonym + category/industry)
2. **Stage** (ARR or company size when they started)
3. **Specific problem** (in one Hormozi sentence — not "they wanted to grow," but "the B2B sales cycle went from 45 to 90 days")
4. **Before** (3-5 concrete numeric metrics)
5. **Mechanism applied** (which framework / plugin skill was used, in 2-3 lines)
6. **After** (the same 3-5 numeric metrics)
7. **Timeframe** (how long it took)
8. **Client quote** (exact words, in quotation marks)

### Step 2: Validation

Before generating the case, validate with `value-equation`:
- Which vector does the before/after cover (Dream Outcome, Probability, Time Delay, Effort)?
- Is the numeric diff measurable and auditable?
- Does the client quote hold up the narrative?

If a required data point is missing, ask. Don't make it up.

### Step 3: Generation

Delegate to `ad-architect` to write the case narrative (4-6 paragraphs), and it returns:
- Full version (1 page, for use in an LP/proposal)
- 1-paragraph version (for use in an ad / cold email)
- 1-line version (for use in the LP hero / ad hook)

### Step 4: Derived assets

- Quote card (for Instagram / LP testimonial section)
- 1-line case (for ad headline)
- 1-paragraph case (for cold-email proof)

### Step 5: Humanizer (full)

### Step 6: Save

Load the `hormozi-gtm:template-case-study` skill via the Skill tool and fill in the skeleton. Save to `outputs/case-studies/case-study-{client_slug}-{YYYYMMDD}-v{n}.md`.

### Step 7: In-conversation preview

```
✅ Saved to: outputs/case-studies/case-study-{client}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Client: {{name}}
   • Before → After: {{X}} → {{Y}} ({{N}}% change)
   • Timeframe: {{N}} {{days|weeks|months}}
   • Quote: "{{first 50 chars}}..."
   • Assets generated: full + 1-paragraph + 1-line + quote card
   • Humanizer status: ✓ full pass

👉 Next steps:
   1. Get final permission from the client (if not already requested)
   2. Add to an existing outputs/lp/ ("Who used it" section)
   3. /hormozi-gtm:hooks with the 1-line as reference
```

## Definition of done

- [ ] Client identified (real name or consented pseudonym)
- [ ] Numeric before/after auditable (not an estimate)
- [ ] Specific timeframe (not "fast")
- [ ] Named mechanism (framework applied, not "hard work")
- [ ] Client quote in quotation marks (exact words)
- [ ] Full set of versions: 1-page, 1-paragraph, 1-line
- [ ] Humanizer full applied

## Anti-patterns

- Case with no number (adjectives only)
- "The client got an amazing result" (vague, throwaway)
- Inventing an estimated number and marking it as real
- Invented or paraphrased quote (the client notices)
- Case with 5 frameworks applied at once (you can't attribute the result)
- Full version only (no derived short assets)
- Skipping the humanizer on pieces that go to an external client
