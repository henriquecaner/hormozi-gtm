---
name: template-client-onboarding
description: "Internal skeleton for the /hormozi-gtm:client-onboarding command output. Loaded by the command, not for direct use."
---

# Template — client-onboarding.md

Canonical skeleton for the client-onboarding output. The `/hormozi-gtm:client-onboarding` command loads this skill and fills the skeleton below with the user's inputs. Reproduce the exact structure: frontmatter + every section + `{{...}}` placeholders.

> **Raw voice.** Onboarding is internal/diagnostic material for the operations team — it **does not go through the humanizer**. The frontmatter reflects that: `humanizer_pass: false`, `humanizer_mode: n/a`, `voice: raw`.

````markdown
---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: client-onboarding
version: 1
status: draft
created: {{ISO8601}}
client: {{company_slug}}
product: {{product_slug}}
duration_days: {{14 | 30 | 60 | 90}}
type: {{self-serve | guided | done-with-you | done-for-you}}
avg_ticket_range: {{<5k | 5k-30k | >30k | enterprise}}
frameworks:
  - leila-scaling
  - value-equation
humanizer_pass: false
humanizer_mode: n/a
voice: raw
language: {{language}}
parent_version: {{prior_version_path_or_null}}
---

# Client Onboarding — {{product_name}}

## Overview

**Total length:** {{N}} days
**Type:** {{self-serve | guided | done-with-you | done-for-you}}
**Average deal size:** ${{range}}
**Target time-to-first-value:** {{N}} days
**Primary owner:** {{role}}

---

## Structure by milestone

### Milestone 0 — Welcome (Day 0, hour 0)

**Trigger:** signature confirmed (contract / payment).

**Touch:**
- Automated email within 5 min
- ($30k+ deals) Personal message from the founder within 24h

**Welcome email content:**
```
Subject: Welcome — your next 30 days with {{product_name}}

[Name],

Decision made. The next few weeks decide whether it was the right one.
Here's what happens from now on:

1. [Milestone 1] within 3 days
2. [Quick win] visible by day 7
3. [Mid-point] on day 21
4. [Wrap] on day 30 with NPS

Next action: [link to schedule the kickoff call] — pick a time in the next 3 days.

Any questions, reply to this email. Response within 4 business hours.

[CS lead name]
```

**Metric:** % who open + click the link within 24h. Target ≥ 80%.

---

### Milestone 1 — Kickoff (Day 1-3)

**Trigger:** client scheduled via the welcome link.

**Touch:** 45-60 min call with the CS lead + client.

**Agenda:**
1. (5 min) Recap of what was sold. Realign expectations.
2. (10 min) Client gives current context + the main goal in 1 sentence.
3. (15 min) CS lead presents the 30-day plan with milestones.
4. (15 min) Collect the inputs needed for Milestone 2 (quick win).
5. (5 min) Next steps + schedule Milestone 3.

**Call output:**
- A 1-page doc with goal + plan + responsibilities + next milestones.
- Sent to the client within 24h after the call.

**Metric:** % of calls that happened within 5 days of the sale. Target ≥ 90%.

---

### Milestone 2 — Quick win (Day 7)

**The most important element of the entire onboarding.**

**The quick win must be:**
- Visible (the client shows it to their boss/team)
- Attributable (clearly because of you)
- Within 7 days
- Modest if it has to be (it matters more that it exists than that it's transformational)

**Examples by category:**

| Category | Typical quick win |
|---|---|
| Growth consulting | Funnel audit with 5 immediate actions + ranking |
| Pricing consulting | Recommended range + proposed tiering + 14-day test |
| B2B SaaS | First dashboard configured with the client's real data |
| Education cohort | First framework documented + applied to the student's case |
| Done-for-you | First tangible deliverable (LP draft, copy V1, etc.) |

**Touch:**
- Email delivering the quick win + 1 sentence summing up the value.
- ($30k+ deals) 5-min Loom from CS presenting the quick win.

**Metric:** % of clients who get a confirmed quick win by D7. Target ≥ 95%.

---

### Milestone 3 — NPS check-in (Day 14)

**Trigger:** automated at D14.

**Touch:**
- Short survey (3 questions)
- ($30k+ deals) 30-min call if NPS < 8

**Survey:**
1. "On a scale of 0-10, how likely are you to recommend {{product}} to a colleague?"
2. "What impressed you most in the first 2 weeks?"
3. "What would you change, if anything? (optional)"

**Metric:** % who answer the survey. Target ≥ 70%. Target average NPS ≥ 8.

**Intervention trigger:** NPS < 7 → mandatory CS lead call within 48h.

---

### Milestone 4 — Mid-point review (Day 21)

**Trigger:** automated at D21.

**Touch:** 30-min call with the CS lead.

**Agenda:**
1. (5 min) Recap of what's been delivered so far vs what was promised.
2. (10 min) Client shares what's working + what isn't.
3. (10 min) Realign the next 4-8 weeks post-onboarding.
4. (5 min) Confirm next milestones.

**Output:** short mid-point doc with what was agreed.

**Metric:** % of mid-point reviews held. Target ≥ 90%.

---

### Milestone 5 — Wrap-up + formal NPS (Day 30)

**Trigger:** automated at D30.

**Touch:**
- Email with a summary of what was achieved in the first 30 days
- Formal NPS (Net Promoter Score + 2 open questions)
- Transition to the operational / continuity phase

**Wrap-up content:**
```
Subject: 30 days — where we are and what's next

[Name],

30 days ago you started with us. Here's what happened:

✅ [Milestone 1]: [concrete result]
✅ [Milestone 2]: [quick win delivered]
✅ [Milestone 3]: [progress on a metric]
✅ [Milestone 4]: [next phase aligned]

Quick NPS: [link]

Next phase (days 31-90):
- [What continues]
- [New touch cadence]
- [Next big milestone]

[Owner] stays your main point of contact.

[Founder or CS lead]
```

**Metric:** day-30 NPS ≥ 8. % who complete all 5 milestones ≥ 90%.

---

## Intervention triggers

| Threshold | Who acts | How fast |
|---|---|---|
| No reply to welcome within 48h | CS lead | Direct DM within 4 business hours |
| No-show at kickoff | CS lead | Reschedule + take the temperature by text/messaging |
| Milestone 2 (D7) with no confirmed quick win | CS lead + Founder | Internal escalation within 24h |
| Day-14 NPS < 7 | CS lead + Founder | Mandatory call within 48h |
| 0 logins (SaaS) in 10 days | Automated trigger + CS | DM within 24h |
| 2+ tickets in 7 days | Senior CS takes over | Immediate escalation |
| Day-30 NPS < 6 | Founder directly | Retention call within 72h |

---

## Touch cadence (overview)

| Day | Touch | Type | Owner |
|---|---|---|---|
| 0 | Welcome email | Automated | System |
| 1-3 | Kickoff call | 45-min call | CS lead |
| 7 | Quick win delivery | Email + (Loom if >$30k) | CS lead |
| 14 | NPS check-in | Survey | Automated |
| 21 | Mid-point review | 30-min call | CS lead |
| 30 | Wrap-up + formal NPS | Email + Survey | CS lead + Founder |

For $30k+ deals: add a weekly check-in at D7, D14, D21, D28 (4 extra calls).

---

## Success metrics

| Metric | Target | Why it matters |
|---|---|---|
| % completing milestone 5 (D30) | ≥ 90% | Onboarding is working |
| Day-14 NPS | ≥ 8 | Client sees value early |
| Time-to-quick-win | ≤ 7 days | Milestone 2 delivered |
| % of touches answered | ≥ 70% | Healthy engagement |
| Day-90 retention | ≥ 85% | Correlated with good onboarding |
| Churn in <30 days | < 5% | Direct reflection of onboarding |

---

## Owners and internal cadence

- **Primary owner:** {{role, 1 person}}
- **Backup:** {{role}}
- **Founder involved in:** kickoff (≥ $30k) + day-30 NPS (all).
- **Squad review:** weekly (5 min of "where are the clients in onboarding").
- **Founders review:** monthly (what's the average health of current onboarding).

---

## Anti-patterns to avoid

- Generic welcome with no concrete expectation
- No kickoff call (the client is lost)
- Fragile quick win (the client shows it to no one)
- Touch with no purpose (an email that just says "everything okay?" and adds nothing)
- No automated trigger (an at-risk client slips through)
- Onboarding too long for a small deal
- Onboarding too short for a long program
- No formal NPS (no way to measure health)
- Diluted owner (CS, support, founder — everyone = no one)
- Forgetting the transition to the operational phase (the client feels abandoned at D31)

---

*Onboarding generated by the hormozi-gtm plugin. Alex Hormozi persona applied. Raw output, no humanizer.*
````
