---
description: Plugin bootstrap — creates gtm-context.md in the consumer project with ICP, offer, brand voice, channels, and stage. Auto-fires if other commands run without gtm-context.md present. Supports --refresh to update stale context.
argument-hint: "[--refresh]"
---

# /hormozi-gtm:init

Initializes the persistent context for the company/client that will use the rest of the plugin's commands. Creates `gtm-context.md` at the root of the consumer project.

## Persona loading

Use the `hormozi-persona` subagent as the voice. All output in first person. No assistant voice.

Load the `hormozi-gtm:hormozi-voice` skill via the Skill tool and imitate the register (don't rely on the subagent alone — in Cowork it may not run). `init` is interaction/setup: raw voice, no humanizer.

## Active skills

- `hormozi-voice` (voice register — load in-context; init is raw interaction, no humanizer)
- `output-conventions` (follows the naming and frontmatter convention)

## Arguments

- No argument: creates `gtm-context.md` if it doesn't exist. If it exists, asks whether to update.
- `--refresh`: updates the existing file without losing prior versions (versions via git or creates a `gtm-context.bak.md` backup).

## Flow

### Step 1: Detect state

Checks whether `gtm-context.md` exists at the root of the consumer project (cwd).

- **Doesn't exist:** go to Step 2 (full interview).
- **Exists and updated <30 days ago:** warns "recent context detected". Asks whether to `--refresh` or abort.
- **Exists and updated >30 days ago:** warns "stale context (X days)". Recommends `--refresh`.

### Step 2: Interview (8 questions)

Ask one question at a time. Don't fire all 8 at once.

1. **Company/project** — name
2. **Category/market** — in 1 specific sentence
3. **Primary ICP** — in 1 ultra-specific sentence (segment + size + role + pain)
4. **Main offer and current price**
5. **Promised transformation** — in what timeframe, who becomes what
6. **Brand voice** — paste 1-2 paragraphs of existing material OR describe it (formal/casual, technical/accessible, Hormozi intensity 0-100%)
7. **Active channels** — Core Four split in % (warm, cold, organic, paid)
8. **Current stage** — validating offer / scaling acquisition / optimizing monetization / exit prep

Optional extra question:
9. **Biggest current bottleneck** — in 1 honest sentence

### Step 3: Generate gtm-context.md

Load the `hormozi-gtm:template-gtm-context` skill via the Skill tool and use its block as the canonical schema. Fill it with the user's inputs. Save to `gtm-context.md` at the root of the consumer project. Default the `language` field to `en` unless the user's brand voice or inputs indicate another output language.

### Step 4: Summary + next steps

Show the user:
- Path of the created file
- Highlights of the captured context (3-5 bullets)
- Suggested next steps:
  - If no audit: `/hormozi-gtm:audit` to diagnose the offer
  - If audit exists: `/hormozi-gtm:lp` or `/hormozi-gtm:script` to produce copy
  - If it's a pricing analysis: `/hormozi-gtm:pricing`

## --refresh mode

When passed:
1. Backs up the current file: copies to `gtm-context.bak-YYYYMMDD.md`
2. Reads the current one and pre-fills answers to the 8 questions
3. Asks one at a time: "Current: X. Keep or update?"
4. Saves the new version with `last_updated` refreshed and `version` incremented

## Done criteria

- [ ] `gtm-context.md` exists at the root of the consumer project
- [ ] Complete frontmatter with `last_updated`, `version`, `company`, `slug`
- [ ] The 8 main sections filled in (not placeholders)
- [ ] Brand voice has a concrete pasted example or detailed description
- [ ] Suggested next steps based on the reported stage

## Anti-patterns

- Skipping a question because it "seems obvious" — always ask all 8
- Accepting a generic ICP answer ("SMBs in general") — push for specificity
- Skipping Brand voice — it's what prevents generic output later
- Firing all 8 questions at once (overwhelm)

## Expected output

At the end, the user sees:
- File path (`./gtm-context.md`)
- Highlights: company, ICP, offer, bottleneck
- 1-3 concrete next steps

First-person message, direct, no chatbot vibe.
