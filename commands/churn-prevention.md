---
description: Win/loss interview + churn analysis + retention playbook. Focuses on retention (not acquisition) — where 80% of the current plugin is focused. For B2B SaaS with churn > 5%/month, consulting with renewal rate < 70%, or a recurring business on a plateau.
argument-hint: "[--product=<slug>] [--ref=<path>] [--mode=churn|winback|retention] [--no-humanize]"
---

# /hormozi-gtm:churn-prevention

Expensive acquisition is a given (CAC always climbing). Retention is where the margin lives. This skill structures: why the client left, what to reverse fast, what to change structurally.

## Persona loading

Use `hormozi-persona` to orchestrate. Delegate to `money-model-architect` for the financial-impact analysis (LTV, churn ratio), and to `offer-architect` if the root cause is the original offer (weak Probability → client gives up early).

**Load the `hormozi-gtm:hormozi-voice` skill via the Skill tool inside the command's own flow and imitate the register** — don't rely on the subagent alone (in Cowork it may not run). All output in first-person Hormozi mode, no assistant voice: number and verb instead of marketing adjectives, the diagnosis to the client's face.

Generate all client-facing copy in the language set in gtm-context `language` (default English). The voice and brutality rules are language-independent and apply in every language.

**Humanizer scope (mixed mode):**
- **Churn analysis** (`--mode=churn` / `--mode=retention` and the `churn-analysis` output): internal diagnostic → ships **raw, no humanizer**.
- **Winback sequence** (`--mode=winback` and the `winback-sequence` output): external copy to the client who left → **humanizer full mode**, and only ships at **brutality ≥7 on the `hormozi-voice` rubric**.

## Active skills

- `hormozi-voice` (brutal voice register — loaded explicitly in the flow)
- `template-churn-analysis` (skeleton for the churn-analysis output)
- `leila-scaling` (5 Star Service framework — retention operations)
- `value-equation` (diagnoses whether Probability/Effort were weak)
- `money-models` (financial impact of churn)
- `ltv-cac` (retention math)
- `humanizer-rules` (full mode — winback sequence only; the churn analysis ships raw)
- `output-conventions`

## Arguments

| Argument | Behavior |
|---|---|
| (empty) | Interactive mode: asks for product + churn metrics + access to churned clients |
| `--product=<slug>` | Product slug |
| `--ref=<path>` | Refine an existing analysis |
| `--mode=churn` | Past-churn analysis (understand why clients left) |
| `--mode=winback` | Winback sequence (recover clients who left in the last 90 days) |
| `--mode=retention` | Preventive playbook (reduce future churn) |
| `--no-humanize` | Skips the humanizer |

## Prerequisites

1. `gtm-context.md` exists → loads ICP, offer, average deal size
2. Retention data: current churn rate, % of clients who left in the last 6 months
3. List of clients who left (ideally with a stated reason)
4. For `--mode=winback`: list of still-valid contacts for the clients who left

## Flow

### Step 1: Collect churn data

In interactive mode, ask:

1. **Primary metric:** current monthly churn rate (or quarterly)?
2. **Trend:** up/down over the last 6 months?
3. **Cohort comparison:** does churn vary a lot by entry period?
4. **Average lifetime:** how many months does a client stay on average before leaving?
5. **% of churn by stated reason:** price / product didn't deliver / internal team took over / switched vendor / other?

### Step 2: Analysis by churn type

Identify the dominant pattern:

**Early churn (< 30 days):**
- Root: bad onboarding or broken expectation on the sales call.
- Immediate fix: revise the sales script + the first 14 days of onboarding.

**Mid churn (30-90 days):**
- Root: the Value Equation failed at delivery (Time Delay > promised, Effort > expected).
- Fix: run `/hormozi-gtm:audit` on the original offer.

**Late churn (>90 days):**
- Root: the product delivered initially but failed to sustain value (weak continuity offer).
- Fix: look at the `money-models` skill — the continuity tier needs rethinking.

**Voluntary churn (client actively cancels):**
- Root: a better alternative showed up or the budget changed.
- Fix: positioning + genuine scarcity for the premium tier.

**Passive churn (client stops using but doesn't cancel):**
- Root: engagement dropped, perceived value went with it.
- Fix: re-engagement sequence (`sales-sequencing` skill).

### Step 3: Win/loss interview script

For `--mode=churn` or `--mode=winback`:

Generates a script of 6-8 questions to interview 5-10 clients who left. The key question:

> "Look, no sales agenda — I just want to understand. If you could go back 90 days before the decision to cancel, what would you do differently OR what could I have done differently?"

Plus another 5-7 structured questions to extract:
- The exact moment they decided to leave (the trigger).
- What they tried before canceling.
- What the competitor/alternative offers that you didn't.
- What still holds up (don't throw it all out).
- Under what conditions they'd come back.

### Step 4: Reason categorization

After 5-10 interviews:

| Reason | How many clients | % | Root in the Value Equation |
|---|---|---|---|
| Price | {{N}} | {{X}}% | Dream Outcome ↓ or Probability ↓ |
| Didn't deliver as expected | {{N}} | {{X}}% | Probability ↓ |
| Internal team took over | {{N}} | {{X}}% | Effort ↓ (client managed to reduce it) |
| Switched vendor | {{N}} | {{X}}% | Market saturation |
| Change in the business | {{N}} | {{X}}% | Not avoidable (don't try) |

### Step 5: Retention playbook

For `--mode=retention`, generate a playbook in 4 blocks:

**Block 1 — Quick wins (0-30 days):**
3-5 concrete actions to implement this week. E.g.:
- Add a weekly check-in during a new client's first 30 days.
- Automatic NPS survey on day 30 + 60 + 90.
- One-Done Guarantee on client replies (reply within 4 business hours).

**Block 2 — Structural changes (30-90 days):**
- Rebuild onboarding (`leila-scaling` skill, 5 Star Service).
- Rebuild the continuity offer (`money-models` skill).
- Rethink the pricing tier (`pricing-playbook` skill).

**Block 3 — Metrics and monitoring (always):**
- North star metric for retention (e.g. NPS, day-90 product adoption, expansion revenue).
- "At-risk client" threshold (e.g. 0 logins in 14 days).
- Automatic intervention trigger.

**Block 4 — Culture and operations:**
- One person owning retention metrics (not diluted).
- Weekly churn review in the squad.
- Post-mortem on every cancellation (even if it was inevitable).

### Step 6: Winback (if `--mode=winback`)

A sequence of 3-4 emails to clients who left in the last 90 days:

**Email 1 (at the moment they leave):**
- Honesty + 1 direct question ("what could I have done differently?")
- No sales CTA.

**Email 2 (+30 days):**
- Update on what's changed since they left (new feature, new case, product refinement).
- Very light CTA ("keep an eye out").

**Email 3 (+60 days):**
- A specific winback offer (not a generic discount — something genuinely new).
- CTA: a short 15-min, no-pressure conversation.

**Email 4 (+90 days):**
- Last call. Honest that you'll stop emailing.
- Door always open.

### Step 7: Financial impact

Delegate to `money-model-architect`:

```
Current scenario:
- Churn rate: {{X}}%/month
- Current LTV: ${{X}}
- What is each 1% reduction in churn worth?

Projection:
- Reduce churn from {{X}}% to {{Y}}% in 90 days
- LTV rises to ${{Z}}
- Impact on ARR/12 months: ${{W}}
```

### Step 8: Humanizer scope (mixed mode)

**Churn analysis (`churn-analysis`) — raw voice (no humanizer).** It's an internal diagnostic: it does NOT go through the humanizer. It ships raw, Hormozi brutal, direct. In the output frontmatter: `humanizer_pass: false`, `humanizer_mode: n/a`, `voice: raw`.

**Winback sequence (`winback-sequence`) — humanizer full mode.** It's external copy to the client who left: it goes through the humanizer in full mode and only ships at brutality ≥7 on the `hormozi-voice` rubric. In that output's frontmatter: `humanizer_pass: true`, `humanizer_mode: full`.

### Step 9: Save

Load the `hormozi-gtm:template-churn-analysis` skill via the Skill tool and fill in the skeleton. Save to `outputs/retention/churn-analysis-{product_slug}-{YYYYMMDD}-v{n}.md`.

If `--mode=winback`: also save `outputs/retention/winback-sequence-{product_slug}-{YYYYMMDD}-v{n}.md`. Load the `hormozi-gtm:template-email-sequence` skill via the Skill tool and fill in the skeleton (the winback sequence inherits the email-sequence structure).

### Step 10: In-conversation preview

```
✅ Saved to: outputs/retention/churn-analysis-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Current churn: {{X}}%/month
   • Dominant reason: {{type}} ({{N}}% of cases)
   • Quick wins identified: {{N}}
   • Financial impact of 90-day retention: ${{X}}
   • Humanizer status: raw voice (no humanizer) — winback, if generated, ships with humanizer full

👉 Next steps:
   1. Run 5-10 win/loss interviews this week (script in the output)
   2. Implement 3 quick wins from Block 1 over the next 30 days
   3. Re-measure churn in 90 days and generate v2 of the analysis
```

## Definition of done

- [ ] Churn rate measured and contextualized vs. benchmark
- [ ] Dominant reason identified (with %)
- [ ] Concrete quick wins (3-5) implementable in 30 days
- [ ] Structural changes identified with the matching Hormozi framework
- [ ] Financial impact quantified ($ per % of churn reduced)
- [ ] Win/loss interview script (≥ 6 questions)
- [ ] For `--mode=winback`: a sequence of 3-4 emails

## Anti-patterns

- "Let's discount to retain them" (a client who leaves over value won't come back over price)
- Ignoring passive churn (only looking at formal cancellations)
- Win/loss interview without asking "if you came back" (loses insight)
- Generic quick wins ("improve support") — has to be specific
- Structural change with no owner (nobody responsible = nothing changes)
- Forgetting the post-mortem (loses the learning from each case)
- Winback as spam (same sequence for every client who left)
