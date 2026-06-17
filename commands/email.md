---
description: Email sequence (cold, warm, nurture, re-engagement). Generates 5-7 sequential emails with hook + agitation + proof + CTA, timing between touches, and context per touch. Tuned for B2B cold outreach — direct voice, no superlatives, specific proof.
argument-hint: "[--type=cold|warm|nurture|re-engagement] [--product=<slug>] [--ref=<file>] [--focus=<section>] [--no-humanize]"
---

# /hormozi-gtm:email

An email sequence that turns a cold lead into a warm one, or a warm lead into a qualified opportunity. Not a blast — a sequenced cadence where every touch has a job.

## Persona loading

Orchestrator: `hormozi-persona`. Delegate the specific copy to `ad-architect` (which writes each email in the first-person Hormozi tone). Final pass through `humanizer` in **full** mode (external output delivered to the client's leads).

Load the `hormozi-voice` skill via the Skill tool and **imitate the register** (rhythm, first person with personal stakes, CTA-as-command, number instead of adjective). Don't rely on the `ad-architect`/`hormozi-persona` subagent alone — in Cowork it may not run, so the voice needs to be loaded in-context in this command.

**This is external copy (it goes to the client's lead): each email only ships at brutality ≥7 on the `hormozi-voice` rubric.** Subjects and CTAs below 7 get rewritten before delivery.

Generate all client-facing copy in the language set in gtm-context `language` (default English). The voice and brutality rules are language-independent and apply in every language.

## Active skills

- `hormozi-voice` (brutal voice register — load in-context and imitate)
- `template-email-sequence` (output skeleton — load in-context at Step 7)
- `hook-framework` (subject + opener for each email)
- `ad-copy-formula` (body structure)
- `value-equation` (anchoring on benefits)
- `guarantees` (closing email)
- `humanizer-rules` (full mode)
- `output-conventions`

## Arguments

| Argument | Behavior |
|---|---|
| (empty) | Interactive mode: asks for sequence type + product + ICP in chat |
| `--type=cold` | Cold outreach (lead has never heard of you). 5-7 emails. |
| `--type=warm` | Warm (lead engaged — downloaded a lead magnet, opened the LP). 4-5 emails. |
| `--type=nurture` | Educational nurture (lead on the list 30+ days, hasn't bought). 5-7 emails. |
| `--type=re-engagement` | Re-engage an inactive lead (90+ days, no opens). 3-4 emails. |
| `--product=<slug>` | Product/offer slug (read from gtm-context.md or input) |
| `--ref=<file>` | Refine an existing sequence (creates v2) |
| `--focus=<section>` | In refine mode: focuses on a specific part (subject, opener, CTA, sequence flow) |

## Prerequisites

1. `gtm-context.md` exists → loads ICP, offer, brand voice, external audience, tone intensity
2. Recent audit (≤30 days)? → loads as `audit_ref` (soft warning if absent)
3. For `--type=cold`: ideally a sample list of 5-10 real prospects (LinkedIn, sites) — feeds personalization

## Flow

### Step 1: Detect type + validate context

If `--type` wasn't passed: ask.
If `gtm-context.md` is stale (>30 days): suggest `/init --refresh`.

### Step 2: Load the offer briefing

If there's a valid `audit_ref`, read the `offer-architect` briefing. Otherwise, read the offer straight from `gtm-context.md` or ask for 3 minimum inputs:
- What transformation does the offer deliver?
- Who is the ICP?
- What's the main objection that shows up on sales calls?

### Step 3: Define the structure by type

**Cold (5-7 emails):**
- Email 1: Hook + a specific observation about the prospect (research). Light CTA (PDF, link, micro-question).
- Email 2 (+3 days): Specific proof point — case study with names + numbers.
- Email 3 (+5 days): Reframe the common objection ("most people think X, but it's Y").
- Email 4 (+7 days): Value content with no ask (links to your own educational content).
- Email 5 (+14 days): Last attempt with genuine scarcity (a spot, a cohort, a real deadline).
- Email 6 (+21 days, optional): Breakup email — "closing out the follow-up, but if you change your mind...". Often the one that converts most.
- Email 7 (+45 days, optional): Re-attempt 6 weeks later — new sequence, different angle.

**Warm (4-5 emails):**
- Email 1: Acknowledge the engagement ("saw you downloaded X"), go deeper on the specific pain.
- Email 2 (+2 days): Show how the product solves the pain — 1 sentence + 1 short case.
- Email 3 (+4 days): Invite the next step (demo, 15-min call, trial).
- Email 4 (+7 days): Reframe + urgency if applicable.
- Email 5 (+14 days): Breakup.

**Nurture (5-7 emails, more spaced out):**
- Email 1 through 5 (1 per week): Each one teaches 1 framework / shows 1 case / answers 1 question. No explicit sales CTA until email 5.
- Email 6 (week 6): Soft pitch of the offer with context from what they learned in the prior weeks.
- Email 7 (week 8): Hard ask with genuine scarcity.

**Re-engagement (3-4 emails):**
- Email 1: Honest — "I noticed you haven't opened my emails in 90 days. I can take you off the list, or do you want to stay?". A direct question.
- Email 2 (+5 days if they clicked "stay"): Re-introduce what's changed since last time.
- Email 3 (+7 days): A special re-engagement offer (not a generic discount — something genuinely new).
- Email 4 (+14 days): Last call.

### Step 4: Build the emails

Delegate to `ad-architect` with a structured briefing for each email (subject, hook, body, CTA). It returns the full sequence.

### Step 5: Humanizer pass (full)

Full pass mandatory. The sequence goes to the client's lead — the voice needs to be clean.

### Step 6: Metrics and suggested test

Include in the output:
- Primary metric to track (reply rate / open rate / click-to-call)
- Minimum sample size (10-15 contacts per type to get a signal)
- Iteration criterion (if reply rate < 3%, swap the subject; if < 1%, swap hook + opener)

### Step 7: Save

Load the `hormozi-gtm:template-email-sequence` skill via the Skill tool and fill the skeleton with the generated sequence. Save to `outputs/email/email-{type}-{product_slug}-{YYYYMMDD}-v{n}.md`.

### Step 8: Preview in the conversation

```
✅ Saved to: outputs/email/email-cold-{slug}-20260520-v1.md
📋 Preview:
   • Sequence: cold, 7 emails, 45-day span
   • Email 1 subject: "{{X}}"
   • Primary CTA (each email): "{{Y}}"
   • Humanizer status: ✓ full pass

👉 Next steps:
   1. Test on 10-15 contacts first
   2. Measure reply rate over 14 days
   3. If < 3%, run /hormozi-gtm:review --ref=outputs/email/...
```

## Done criteria

- [ ] Each email has a specific subject (not generic)
- [ ] Email 1's hook passes the tweet test (reads on its own)
- [ ] Each email has 1 unique, specific CTA
- [ ] The sequence has defined timing between emails
- [ ] Breakup email included (if applicable)
- [ ] Humanizer full applied
- [ ] Primary metric and iteration criterion documented

## Anti-patterns

- A "let's chat?" email with no specific proposal
- Every email ends in "book a call" (the lead loses the rhythm)
- Generic subject ("Opportunity") or clickbait ("Open?")
- Identical copy across every touch (the lead notices)
- Fake personalization ("Hi [name], loved your post about [random topic]")
- No breakup email (leaves the warm lead hanging indefinitely)
- Sequence with no clear success/iteration metric
