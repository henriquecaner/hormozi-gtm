---
description: Creates or refines a long-form sales landing page (2000-3500 words). Uses Grand Slam Offer, Value Equation, bonus stacking, scarcity/urgency, guarantees. Humanizer full mode mandatory. Soft warning if there's no recent audit.
argument-hint: "[--product=<slug>] [--ref=<path>] [--focus=<section>] [--skip-audit] [--no-humanize]"
---

# /hormozi-gtm:lp

Builds a sales landing page structured in 10 sections (hero → agitation → offer → who you are → stack → guarantee → proof → pricing → FAQ → final CTA). Each section applies specific frameworks.

## Persona loading

Orchestrator: `hormozi-persona`.
Offer analysis: delegate to `offer-architect` (loads the briefing).
Final pass: delegate to `humanizer` (full mode, mandatory).

**Voice (in-context loading, non-negotiable):** load the `hormozi-voice` skill via the Skill tool and imitate the register (rhythm, attitude, hammer line). Don't rely on the `hormozi-persona` subagent alone — in Cowork the subagent may not run, and the voice needs to be loaded inside the command's own flow. Since this LP is **external copy**, it only ships at **brutality ≥7 on the `hormozi-voice` rubric** — score the headline, sub, CTAs, and body before saving and rewrite anything below 7.

Generate all client-facing copy in the language set in gtm-context `language` (default English). The voice and brutality rules are language-independent and apply in every language.

## Active skills

- `hormozi-voice` (voice register — load in-context, see Persona loading)
- `template-lp` (output skeleton — load via Skill in Step 2)
- `grand-slam-offer` (offer as the core)
- `value-equation` (each section raises 1+ vector)
- `bonus-stacking` (section 5)
- `scarcity-urgency` (sections 6 and 10)
- `guarantees` (section 6)
- `hook-framework` (headline + sub-headline)
- `ad-copy-formula` (microcopy, CTAs)
- `humanizer-rules` (full mode)
- `output-conventions`

## Arguments

| Argument | Behavior |
|---|---|
| (empty) | Creates a new LP. Asks for the product slug. |
| `slug` | Creates a new LP with the given slug |
| `outputs/lp/<file>.md` | Refine mode — reads the file, asks what to improve, creates v{n+1} |
| `--focus=<section>` | In refine mode, focuses on 1 section (hero, agitation, offer, who-you-are, stack, guarantee, proof, price, faq, cta) |
| `--skip-audit` | Skips the soft warning for a missing audit |
| `--no-humanize` | Skips the humanizer pass (debug, A/B comparison) |
| `--overwrite` | Overwrites v{n} instead of creating v{n+1} |

## Prerequisites

1. `gtm-context.md` exists → loads ICP, offer, brand voice, external audience, tone intensity
2. If it doesn't exist → fires `/hormozi-gtm:init` first
3. Recent offer audit (≤14 days)? → loads it as `audit_ref`
4. No recent audit and no `--skip-audit` → interactive prompt (not a passive warning):

> "Your offer hasn't been through a Value Equation audit in the last 2 weeks. Copy written on an offer with no recent audit often needs rework.
>
> How do you want to proceed?
> (1) Run `/hormozi-gtm:audit` now (5min) — recommended, the LP comes out much better
> (2) Go ahead anyway — I get the risk, I want the LP today
> (3) Cancel — I'll run the audit in a separate session and come back"

If (1): runs `/hormozi-gtm:audit` inline, saves the audit, loads `audit_ref` automatically, continues the LP flow.
If (2): proceeds, but writes `audit_ref: null` in the frontmatter with a note.
If (3): exits clean, without creating a file.

## Flow

### CREATE mode

#### Step 1: Collect inputs

Loads whatever it can from `gtm-context.md`. Asks for what's missing:
- ICP (required)
- Main offer (required)
- Price (required)
- Promised transformation — in what timeframe, who becomes what (required)
- Available social proof (optional)
- Current or intended guarantee (optional)
- Available bonuses (optional — agent suggests if there are none)
- Genuine urgency/scarcity (optional — agent flags it if invented)

#### Step 2: Build

Delegate to `offer-architect` to distill the offer briefing. Load the `hormozi-gtm:template-lp` skill via the Skill tool and fill in the skeleton. Then `hormozi-persona` (orchestrator) takes the briefing and builds the 10 sections on top of that skeleton:

1. Hero (headline + sub + CTA + microcopy)
2. Problem agitation (3 symptoms + why other solutions fail)
3. Offer presentation (Grand Slam)
4. Who you are / why listen (story)
5. Bonus stack (3-5, odd count, with $ value)
6. Guarantee (conditional + metric + compensation)
7. Social proof (3+ comparable cases)
8. Pricing + anchoring
9. FAQ (4-6 mapped objections)
10. Final CTA + genuine urgency

#### Step 3: Humanizer pass (full)

Delegate to the `humanizer` subagent. Apply all the rules.

#### Step 4: Save output

Saves to `outputs/lp/lp-{slug}-{YYYYMMDD}-v1.md` with complete frontmatter.

#### Step 5: Preview in the conversation

Shows:

```
✅ Saved to: outputs/lp/lp-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Headline: "{{headline text}}"
   • Guarantee: {{type + clause}}
   • Stack: {{N}} bonuses, total value ${{X}}
   • Primary CTA: "{{text}}"
   • Humanizer status: ✓ full pass

👉 Next steps:
   1. Show it to the client, capture feedback
   2. /hormozi-gtm:hooks --product={{slug}} → test headlines in ads
   3. /hormozi-gtm:review --ref=outputs/lp/... → if you want brutal internal feedback
```

Ends by asking whether to refine any section (without reopening the whole dialogue).

### REFINE mode

#### Step 1: Read the existing file

Loads frontmatter + content. Identifies version, frameworks already applied, audit_ref, parent_version.

#### Step 2: Diagnosis

Asks:
> "What do you want to improve? (1) headline (2) offer (3) guarantee (4) social proof (5) bonus stack (6) FAQ (7) rewrite everything (8) other"

Or if `--focus=<section>` was passed, goes straight to the section.

#### Step 3: Refinement

Applies the change while keeping the rest. Re-runs the humanizer.

#### Step 4: Save v{n+1}

Saves to the same folder as `v{n+1}`. Frontmatter points `parent_version` to `v{n}`.

#### Step 5: Summary diff

Shows:
- What changed (1 line per change)
- Path of the new file

## Done criteria

- [ ] Headline passes the 3 tests (numeric specificity + tweet test + curiosity gap)
- [ ] Offer has a visible stack (3-5 bonuses, odd count)
- [ ] At least 1 conditional guarantee (not "satisfaction guaranteed")
- [ ] CTA repeated 3+ times
- [ ] No generic line ("transform your life", "reach your potential")
- [ ] Humanizer full applied (no em-dash overuse, no rule of three, no AI vocab)
- [ ] File saved to `outputs/lp/` with complete frontmatter
- [ ] Suggested next steps (usually: `/hormozi-gtm:hooks` to test headlines)

## Anti-patterns

- Skipping the Value Equation audit first (an LP on top of a weak offer = money out the door)
- Generic bonus ("community access")
- Generic guarantee ("satisfaction guaranteed")
- "Learn more" CTA (no action verb)
- Cliché copywriter tone (use first-person Hormozi)
- Inventing fake scarcity (use the `scarcity-urgency` skill to check it's genuine)

## Expected output

File: 2000-3500 words, structured in 10 sections with H2 headers.
Conversation: 5-10 lines with highlights + path + next steps.
