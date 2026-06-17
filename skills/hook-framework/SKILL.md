---
name: hook-framework
description: Hook Framework from $100M Leads — 3 hook types (dream outcome, problem, secret). Use to generate LP headlines, ad hooks (especially short-form), email subject lines, and opening lines of copy.
---

# Hook Framework

Source: Alex Hormozi, *$100M Leads* (Magnetic Reasons + Lead Magnet hooks) + *$100M Offers* (Naming).

## The 3 hook types

### 1. Dream Outcome Hook
**Structure:** "How [specific person] hit [specific result] in [timeframe] without [common obstacle]"

Examples:
- "How rookie closers went from $8k to $23k MRR in 47 days without switching companies"
- "How freelance designers landed $50k+ contracts without cold email"

**When to use:** aspirational audience, the prospect already sees the desire clearly.

### 2. Problem Hook
**Structure:** "Stop [the wrong behavior]. The problem isn't [shallow diagnosis], it's [the real diagnosis]."

Examples:
- "Stop reading sales books. Your closer's problem isn't technique, it's price objection."
- "Stop spending on ads. Your LP bleeds 80% of its traffic because the offer is weak."

**When to use:** skeptical audience, the prospect has tried other things, needs a reframe.

### 3. Secret Hook
**Structure:** "The thing [an authority/group] won't tell you about [relevant topic]"

Examples:
- "The thing top SaaS closers won't tell you about price objection"
- "The number your pricing spreadsheet is lying to you about"

**When to use:** curious audience, a topic where there's a sense of hidden information.

## Anti-patterns (auto-discard)

- "Discover the secret to X" (generic, no specificity)
- "Want to make more money?" (generic yes/no)
- "Today I'm going to teach you..." (anti-hook, kills attention)
- Excessive emoji
- ALL CAPS
- Obvious rhetorical question

## Quality criteria

A good hook passes 3 tests:

1. **Numeric specificity:** it has a number (age, dollar amount, timeframe, %, quantity)
2. **Tweet test:** does the hook read on its own as a tweet/post? If yes, OK.
3. **Curiosity gap:** does the reader NEED to know what comes next?

## Batch workflow (15 hooks)

When the `/hormozi-gtm:hooks` command is invoked:

1. Collect ICP + offer + promised transformation
2. Generate 5 hooks per type (5 dream + 5 problem + 5 secret) = 15 total
3. For each hook, specify:
   - Angle (dream/problem/secret)
   - Mechanism (which emotion/thought it triggers)
   - Where to use it (LP headline / ad hook / email subject)
4. Identify the agent's top 3 with rationale

Quantities configurable via `--n=N` (default 15).

## Application by use case

| Case | How to use the Hook Framework |
|---|---|
| Sales LP | Primary headline + sub-headline test the 3 different types. Winner rotates |
| Ad script | First 3 seconds = the hook. Short-form lives or dies here |
| Hooks batch | 15-20 variants for A/B testing |

## Platform specialization

| Platform | Hook type that tends to win |
|---|---|
| Reels / TikTok | Problem hook (fast reframe) |
| YouTube | Dream outcome hook (long format supports it) |
| LP headline | Dream outcome hook (high specificity) |
| Email subject | Secret hook (curiosity > specificity) |

## Detailed reference

See `reference/100m-leads-extracts.md` (Magnetic Reasons + Hook Mechanics section).
