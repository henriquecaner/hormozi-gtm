---
name: template-gtm-context
description: "Internal output skeleton for the /hormozi-gtm:init command. Loaded by the command, not for direct use."
---

# Template — gtm-context.md

Canonical skeleton for the `gtm-context.md` file. The `/hormozi-gtm:init` command loads this skill and fills the skeleton below with the user's inputs. Reproduce the exact structure: frontmatter + every section + `{{...}}` placeholders.

```markdown
---
company_name: {{company_name}}
company_slug: {{company_slug}}
last_updated: {{YYYY-MM-DD}}
version: 1
plugin: hormozi-gtm
language: en
---

# GTM Context — {{company_name}}

Persistent context file. Every plugin command reads it automatically. Update it whenever something relevant changes (offer, price, ICP, channel). Old versions stay in git.

> **`language` field:** output language for generated copy (`en` | `pt-br` | ...). Defaults to `en`. The voice and brutality rules are language-independent and apply in every language — the copy is written native in the target language, never translated.

## Company

- **Category/market** (1 specific sentence):
  > {{category}}

- **Current stage:**
  > {{validating-offer | scaling-acquisition | optimizing-monetization | exit-prep}}

## ICP

- **ICP in 1 ultra-specific sentence** (include segment, size, role, primary pain):
  > {{icp}}

- **Anti-ICP** (who you do NOT serve, to filter):
  > {{anti-icp}}

## Offer

- **Core offer** (1 sentence with the promised transformation):
  > {{core-offer}}

- **Current price:**
  > {{price}}

- **Model:** one-time | recurring | hybrid
  > {{model}}

- **Promised transformation** (in how long, who becomes what):
  > {{transformation}}

- **Last audit:** {{path_to_recent_audit_or_none}}

## Brand Voice

- **Tone:** {{ex: intelligent, practical, structured, direct, occasionally provocative}}
- **Hormozi vs own-voice mix:** {{ex: 70% Hormozi + 30% LEVEL voice}}
- **External audience:** {{senior B2B | end consumer | mid-market | enterprise}}
- **Tone intensity:** {{low | medium | high}} — calibrates the aggressiveness of the copy

**Example of copy that resonates with the ICP** (paste 1-2 paragraphs of existing material, a LinkedIn post, a founder email):

> {{copy_example}}

## Channels

**Current Core Four split (sums to 100):**

| Channel | % | Status |
|---|---|---|
| Warm (1:1) | {{ex: 30}}% | {{active/inactive}} |
| Cold (1:1) | {{ex: 10}}% | {{active/inactive}} |
| Organic (1:many free) | {{ex: 40}}% | {{active/inactive}} |
| Paid (1:many paid) | {{ex: 20}}% | {{active/inactive}} |

**Active lead magnet:** {{name_or_none}}

## Unit economics (if known)

- **Blended average price:** $ {{}}
- **Variable cost:** $ {{}}
- **Estimated LTGP:** $ {{}}
- **Current CAC:** $ {{}}
- **LTGP:CAC ratio:** {{}}
- **Payback period:** {{days}}

## Additional context

- **Biggest current bottleneck** (1 honest sentence):
  > {{bottleneck}}

- **Past attempts that failed:**
  > {{list_or_n_a}}

- **Recent or open decisions:**
  > {{list_or_n_a}}

---

## How to update

Run `/hormozi-gtm:init --refresh` when:
- The ICP changed
- The core offer changed
- The price changed >10%
- The dominant channel changed
- The company's stage advanced

The plugin warns "context stale" if `last_updated` is >30 days old.
```
