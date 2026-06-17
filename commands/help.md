---
description: Interactive decision matrix. Answer 3 questions and get the right command recommended. Useful for onboarding a new client or when you don't know where to start a session. Covers all 17 plugin commands.
argument-hint: "[--objective=audit|copy|pricing|plan|review|email|objection|case-study|webinar|positioning|content|churn|onboarding]"
---

# /hormozi-gtm:help

Don't know which command to run? Answer 3 questions and I'll show you the recommended path.

## Persona loading

Use `hormozi-persona` in orientation mode — direct, no wasting the user's time. No "how can I help you?". Straight to the matrix.

## Active skills

No specific skill is loaded — `/help` is a router, not an output producer.

## Arguments

| Argument | Behavior |
|---|---|
| (empty) | Interactive mode: 3 questions in sequence |
| `--objective=audit` | Recommends directly: `/hormozi-gtm:audit` |
| `--objective=copy` | Goes to a sub-question (LP / VSL / hooks / ad short) |
| `--objective=pricing` | Recommends directly: `/hormozi-gtm:pricing` |
| `--objective=plan` | Recommends directly: `/hormozi-gtm:plan` |
| `--objective=review` | Recommends directly: `/hormozi-gtm:review` |
| `--objective=email` | Recommends directly: `/hormozi-gtm:email` |
| `--objective=objection` | Recommends directly: `/hormozi-gtm:objections` |
| `--objective=case-study` | Recommends directly: `/hormozi-gtm:case-study` |
| `--objective=webinar` | Recommends directly: `/hormozi-gtm:webinar` |
| `--objective=positioning` | Recommends directly: `/hormozi-gtm:positioning` |
| `--objective=content` | Recommends directly: `/hormozi-gtm:content-hub` |
| `--objective=churn` | Recommends directly: `/hormozi-gtm:churn-prevention` |
| `--objective=onboarding` | Recommends directly: `/hormozi-gtm:client-onboarding` |

## Prerequisites

None. `/help` runs even without `gtm-context.md` — it's the entry point for a new user.

## Flow

### Step 1: Detect state

```
Do you have a gtm-context.md in this project?
  No → recommend starting with /hormozi-gtm:init before any other command.
  Yes → go to Step 2.
```

### Step 2: Goal question (multiple choice)

```
What do you want to do right now?

(1) Understand whether my offer holds up (diagnostic)
(2) Create external copy (LP, ad, hooks, script)
(3) Validate or structure pricing
(4) Build a 90-day GTM plan / business plan
(5) Get brutal feedback on existing material
(6) Structure an outreach sequence (email/LinkedIn)
(7) Map objections and scripts for the sales call
(8) Structure a case study + proof assets
(9) Plan a B2B webinar (30-45min)
(10) Define positioning vs the competition
(11) Build a 30-90 day organic content roadmap
(12) Diagnose and reduce churn / winback
(13) Structure the first 30 days of client onboarding
(14) Other / not sure
```

### Step 3: Routing by answer

**(1) Diagnostic:**
> `/hormozi-gtm:audit` — offer diagnostic via the Value Equation (Dream Outcome × Probability ÷ Time Delay × Effort). Finds the critical bottleneck, proposes the top 3 levers, rewrites the offer in 1 paragraph.

**(2) External copy:**
> What kind of copy?
> (a) Sales landing page → `/hormozi-gtm:lp`
> (b) Video script (long VSL 8-15min or short-form 15-60s) → `/hormozi-gtm:script`
> (c) Hook battery for ads (10-20 variations) → `/hormozi-gtm:hooks`
>
> ⚠️ I recommend running `/hormozi-gtm:audit` first if you haven't in the last 2 weeks. Copy written over a weak offer is money lost.

**(3) Pricing:**
> `/hormozi-gtm:pricing` — review against the 5 laws of the LEAKED Pricing Playbook + validation against the Value Equation + LTV:CAC math. Output as a range, not a single number, with Silver/Gold/Platinum tiering when applicable.

**(4) 90-day plan:**
> `/hormozi-gtm:plan` — a structured business plan (Core Four split + 4-level money model + roadmap per quarter). Use it for a new company or a new product inside an existing one.

**(5) Brutal review:**
> `/hormozi-gtm:review --ref=<path_to_material>` — constructive feedback, no mercy. A LIGHT/MEDIUM/CRITICAL verdict, top 3 concrete fixes, a rewrite of the critical passages. Has an automatic re-review mode (delta v1↔v2).

**(6) Outreach:**
> `/hormozi-gtm:email` — a 5-7 email sequence (cold, warm, nurture, or re-engagement) with hook + agitation + proof + CTA + reactivation. Tuned for B2B cold outreach. Pair it with the `email-deliverability` skill for the technical setup (domain warm-up, SPF/DKIM/DMARC).

**(7) Objections:**
> `/hormozi-gtm:objections` — a matrix per ICP. Each objection mapped with root cause (offer/price/timing/trust), a 2-sentence reframe, a word-for-word script for the sales call, and a mitigation in the offer. Top 3 with a full role-play-trainable script.

**(8) Case study:**
> `/hormozi-gtm:case-study --client=<name>` — a structured case study (auditable numeric before/after + the exact quote + a named mechanism). Generates a full version + 1-paragraph (cold email) + 1-line (LP headline) + quote card.

**(9) Webinar:**
> `/hormozi-gtm:webinar --duration=30|45|60` — a B2B structure in 7 blocks (open + diagnostic + mechanism + cases + offer + Q&A + CTA). Different from a direct-response VSL (12min). Includes plant questions for the Q&A.

**(10) Positioning:**
> `/hormozi-gtm:positioning` — a competitive teardown with 3-5 competitors, defensible differentiation axes, a testable positioning statement. Generates hero copy (3 variations) + cold subject (3) + LinkedIn bio + a sales-call opener.

**(11) Organic content:**
> `/hormozi-gtm:content-hub --duration=30|60|90` — a content roadmap. Topic × format × funnel stage × CTA. Weekly calendar + repurpose plan + metrics per month.

**(12) Churn / retention:**
> `/hormozi-gtm:churn-prevention` — diagnostic by type (early/mid/late/voluntary/passive), win/loss interview script, a 4-block retention playbook, an optional winback sequence (`--focus=winback`), projected financial impact.

**(13) Client onboarding:**
> `/hormozi-gtm:client-onboarding` — the first 30-day journey across 5 milestones (welcome → kickoff → quick win D7 → NPS D14 → mid-point D21 → wrap D30). Quantitative intervention triggers. Cuts early churn by a typical 40-60%.

**(14) Not sure:**
> By typical stage:
> - **Early (pre-PMF, < 20 clients):** `/hormozi-gtm:init` → `/hormozi-gtm:audit` → `/hormozi-gtm:plan`.
> - **Validating the offer:** `/hormozi-gtm:audit` → `/hormozi-gtm:pricing` → `/hormozi-gtm:lp`.
> - **Have a product, need leads:** `/hormozi-gtm:hooks` → `/hormozi-gtm:email` → `/hormozi-gtm:lp`.
> - **Closing high-ticket deals:** `/hormozi-gtm:objections` → `/hormozi-gtm:positioning` → `/hormozi-gtm:case-study`.
> - **Client signed, now deliver:** `/hormozi-gtm:client-onboarding`.
> - **Reduce churn on a recurring base:** `/hormozi-gtm:churn-prevention`.
> - **Revenue plateau:** `/hormozi-gtm:audit` (look for channel/offer saturation) → `/hormozi-gtm:plan`.

## Done criteria

- [ ] Detected whether `gtm-context.md` exists
- [ ] Presented a clear decision matrix (14 options)
- [ ] Recommended 1 primary command + alternatives if applicable
- [ ] Mentioned prerequisites when relevant (e.g. audit before copy)

## Anti-patterns

- Recommending 4+ commands at once (the user gets lost)
- Repeating the command description instead of pointing straight to it
- Forgetting to check `gtm-context.md` before recommending (a recommendation with no context is generic)
- Sounding like an assistant ("I'll help you find..."). It's Hormozi: straight to it.
- Listing a command that doesn't exist (keep this list aligned with `commands/`)
