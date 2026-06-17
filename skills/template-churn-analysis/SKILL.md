---
name: template-churn-analysis
description: "Internal skeleton for the churn-analysis output of the /hormozi-gtm:churn-prevention command. Loaded by the command, not for direct use."
---

# Template — churn-analysis.md

Canonical skeleton for the churn-analysis output. The `/hormozi-gtm:churn-prevention` command loads this skill and fills the skeleton below with the user's inputs. Reproduce the exact structure: frontmatter + every section + `{{...}}` placeholders.

> **Raw voice.** Churn analysis is an internal diagnostic — it **does not go through the humanizer**. The frontmatter reflects that: `humanizer_pass: false`, `humanizer_mode: n/a`, `voice: raw`. (The winback sequence, when generated, is external copy and uses the `template-email-sequence` template with full humanizer.)

````markdown
---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: churn-prevention
foco: {{churn | winback | retention}}
version: 1
status: draft
created: {{ISO8601}}
client: {{company_slug}}
product: {{product_slug}}
frameworks:
  - leila-scaling
  - value-equation
  - money-models
  - ltv-cac
humanizer_pass: false
humanizer_mode: n/a
voice: raw
language: {{language}}
parent_version: {{prior_version_path_or_null}}
---

# Churn Analysis — {{product_name}}

## TL;DR

**Current churn rate:** {{X}}%/month ({{trend: rising/flat/falling}})
**Dominant reason:** {{type}} ({{N}}% of cases)
**Financial impact:** ${{Y}}/month in lost revenue
**Top recommendation in 1 sentence:** {{...}}

---

## 1. Snapshot

| Metric | Current value | Market benchmark | Status |
|---|---|---|---|
| Monthly churn | {{X}}% | {{2-5% SaaS, 5-15% consulting}} | {{✓ / ⚠️ / ❌}} |
| Average lifetime | {{N}} months | {{...}} | {{...}} |
| Current NPS | {{X}} | {{30-50 healthy}} | {{...}} |
| Net Revenue Retention | {{X}}% | {{100%+ is the target}} | {{...}} |
| % churn in <30 days | {{X}}% | {{<10% healthy}} | {{...}} |

---

## 2. Distribution by churn type

| Type | % of total | Typical window | Root in the Value Equation |
|---|---|---|---|
| Early (<30d) | {{X}}% | Onboarding | Probability ↓ or expectation broken |
| Mid (30-90d) | {{X}}% | Delivery | Probability/Time Delay ↓ |
| Late (>90d) | {{X}}% | Continuity | Weak continuity offer |
| Voluntary | {{X}}% | Any | An alternative showed up or budget changed |
| Passive | {{X}}% | Any | Engagement dropped |

**Dominant pattern:** {{1-2 sentence description}}

---

## 3. Stated reasons (after win/loss interviews)

| Reason | # clients | % | Root category | Reversible? |
|---|---|---|---|---|
| Price | {{N}} | {{X}}% | {{Dream Outcome ↓ / Probability ↓}} | Yes |
| Didn't deliver as expected | {{N}} | {{X}}% | {{Probability ↓}} | Yes |
| Internal team took it over | {{N}} | {{X}}% | {{Effort ↓ — client managed to cut it}} | No (a win, but goodbye) |
| Switched vendors | {{N}} | {{X}}% | {{Saturation or positioning}} | Partially |
| Business change | {{N}} | {{X}}% | {{Unavoidable}} | No |
| Other | {{N}} | {{X}}% | {{...}} | {{...}} |

---

## 4. Win/loss interviews — insights

### 5-10 qualitative interviews conducted

**Recurring quote:**
> "{{line that came up in ≥3 interviews, exact quotation}}"

**Emerging pattern:**
{{2-3 sentences describing what multiple churned clients said in common.}}

**Surprises (what clients asked for that you didn't expect):**
- {{insight 1}}
- {{insight 2}}

**What still holds (don't throw it out):**
- {{aspects of the offer that churned clients still praise}}

---

## 5. Retention Playbook — 4 blocks

### Block 1: Quick wins (0-30 days)

Immediate implementation. Each item: description + owner + success metric.

| Action | Owner | Success metric | Deadline |
|---|---|---|---|
| {{Add a weekly check-in in the first 4 weeks of a new client}} | {{CS}} | {{Day-30 NPS ≥ 7}} | 2 weeks |
| {{Automated NPS survey at D30/D60/D90}} | {{Ops}} | {{≥ 70% response rate}} | 2 weeks |
| {{One-Done Guarantee on ticket responses (4 business hours)}} | {{Support}} | {{First response time < 4h}} | 1 week |
| {{...}} | {{...}} | {{...}} | {{...}} |
| {{...}} | {{...}} | {{...}} | {{...}} |

### Block 2: Structural changes (30-90 days)

| Change | Matching Hormozi skill | Owner | Key milestone |
|---|---|---|---|
| {{Rebuild onboarding into a 4-week structured journey}} | `leila-scaling` (5 Star Service) | {{CS lead}} | First 5 clients on the new journey |
| {{Redesign the continuity offer}} | `money-models` | {{Founder + Pricing}} | Continuity tier launched |
| {{Rethink pricing tier to cut commoditization}} | `pricing-playbook` (Law 4) | {{Founder}} | New tiering tested on 10 sales calls |

### Block 3: Metrics and monitoring

**Retention north star metric:** {{NPS | day-90 product adoption | expansion revenue | net retention}}

**Target (12 months):** {{X}}

**"At-risk client" threshold:**
- {{e.g. 0 logins in 14 days → automatic trigger}}
- {{e.g. day-30 NPS < 5 → mandatory check-in call within 48h}}
- {{e.g. 2 support tickets in 7 days → escalation to senior CS}}

**Intervention trigger:**
{{How the system alerts whoever is responsible when a threshold trips.}}

### Block 4: Culture and operations

- **Owner of the retention metric:** {{1 person, not diluted}}
- **Review cadence:** weekly (squad), monthly (founders)
- **Mandatory post-mortem:** every cancellation produces 1 short doc (15 min of writing) with: reason, what we learned, what changes in operations
- **Ritual:** first Monday of the month, 30 min of retention review

---

## 6. Projected financial impact

### Current scenario

```
Monthly churn: {{X}}%
Current LTV: ${{Y}}
ARR: ${{Z}}
```

### 90-day scenario (after implementing Block 1 + 2)

```
Projected monthly churn: {{X - 1 to 2 percentage points}}%
Projected LTV: ${{Y + 20-40%}}
Additional ARR captured over 12 months: ${{W}}
```

### Intervention ROI

**Investment (3 months):** {{squad hours + tools}} ≈ ${{Z}}
**Return (12 months):** ${{W}}
**Ratio:** {{W/Z}}x

---

## 7. Next 14 days — concrete actions

- [ ] Run 5-10 win/loss interviews with clients who churned in the last 90 days (script in Appendix)
- [ ] Implement Quick Win 1: {{...}}
- [ ] Implement Quick Win 2: {{...}}
- [ ] Name a single owner of the retention metric
- [ ] Schedule a recurring weekly review

---

## Appendix A — Win/loss interview script (6-8 questions)

1. "Can you walk me through the exact moment you decided to cancel? What happened that day/week?"
2. "Before deciding, did you try to solve it another way? How?"
3. "What does {{competitor or alternative}} offer that we didn't?"
4. "Looking back, what still holds up from the time you were a client?"
5. "If you could go back 90 days before the decision, what would you do differently OR what could I have done differently?"
6. "Under what conditions would you consider coming back?"
7. "Is there anything I didn't ask that would be useful for me to know?"
8. "Can I reach out in 6 months to update you on what's changed here?"

**Rules:**
- No sales agenda. The client can feel it.
- Take notes. Don't argue or defend.
- Promise confidentiality (don't use what they said in copy without permission).

---

*Churn analysis generated by the hormozi-gtm plugin. Alex Hormozi persona applied. Raw voice — internal diagnostic does not go through the humanizer.*
````
