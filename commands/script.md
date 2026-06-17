---
description: Create or refine a video script — long-form VSL (8-15min) or short-form (15-60s). Batch mode generates multiple variants. Uses hook framework, VSL 7-step arc, ad copy formula. Humanizer full mode required.
argument-hint: "[--product=<slug>] [--ref=<path>] [--format=vsl|reels|shorts|tiktok] [--batch] [--n=N] [--no-humanize]"
---

# /hormozi-gtm:script

Video ad script. Supports long-form VSL (8-15min) or short-form (15-60s). Batch mode generates multiple variants in a single run.

## Persona loading

Orchestrator: `hormozi-persona`.
Analysis: delegate to `ad-architect`.
Final pass: delegate to `humanizer` (full mode).

**BEFORE writing anything, call the Skill tool to load `hormozi-gtm:hormozi-voice` and imitate the register** (don't rely on the subagent alone — in Cowork it may not run). A script is external copy: the output goes to the client's audience. Copy only ships at brutality **≥7 on the `hormozi-voice` rubric** — hook, CTA, and offer in first person, number and verb instead of a marketing adjective, risk reversal visible. Below 7, rewrite before delivering.

Generate all client-facing copy in the language set in gtm-context `language` (default English). The voice and brutality rules are language-independent and apply in every language.

## Active skills

- `hormozi-voice` (voice register — load in-context via Skill)
- `template-vsl` (long-form VSL output skeleton — load in-context via Skill)
- `template-ad-short` (short-form/batch output skeleton — load in-context via Skill)
- `hook-framework` (critical — first 3s)
- `vsl-7-step` (for long-form VSL)
- `ad-copy-formula` (warm/cold/paid structure)
- `grand-slam-offer` (reference for the offer being sold)
- `scarcity-urgency` (final CTA)
- `humanizer-rules` (full mode)
- `output-conventions`

## Arguments

| Argument | Behavior |
|---|---|
| (empty) | Asks for format in chat |
| `slug` | Creates a script with the given slug |
| `outputs/script/<file>.md` | Refine mode — reads, asks what to change |
| `--format=vsl` | Long-form VSL (8-15min) |
| `--format=reels`, `shorts`, or `tiktok` | Short-form (15-60s) |
| `--batch` | Generates 5-10 variants (defaults to short-form) |
| `--n=N` | Number of variants in batch |
| `--no-humanize` | Skips humanizer |
| `--overwrite` | Overwrites v{n} |

## Prerequisites

1. `gtm-context.md` exists → loads ICP, offer, brand voice, external audience, tone intensity
2. Recent offer audit? → loads it as `audit_ref`. If missing, asks interactively:

   > "Your offer hasn't been through a Value Equation audit in the last 2 weeks. A script written on top of an un-audited offer often needs rework.
   >
   > How do you want to proceed?
   > (1) Run `/hormozi-gtm:audit` now (5min) — recommended
   > (2) Go ahead anyway — I get the risk, I want the script today
   > (3) Cancel — I'll come back later"

3. Hooks validated? → soft suggestion (non-blocking) to run `/hormozi-gtm:hooks` if no hook has been chosen. If the user asked for short-form without prior hooks, suggest running `/hooks` first to test 10-15 ad variants before writing the full script.

## Flow

### VSL format (8-15min)

#### Step 1: Intake

Asks:
- Target length (8min, 10min, 12min, 15min)
- Destination platform (YouTube, Facebook, LP embed)
- Preferred hook angle (dream / problem / secret) — or let the agent choose
- 1-2 real comparable cases (if any exist)

#### Step 2: Build

Delegate to `ad-architect`. Load the `hormozi-gtm:template-vsl` skill via the Skill tool and fill in the skeleton. Build the 7 acts:

1. Hook (0-15s)
2. Story (15s-2min)
3. Problem (2-4min)
4. Mechanism (4-7min) — always name the system
5. Proof (7-9min)
6. Offer (9-11min) — full Grand Slam
7. CTA + Urgency (11-12min)

#### Step 3: Humanizer (full)

Before the humanizer, validate the script against the `hormozi-voice` rubric (gate ≥7): hook with specificity, CTA-command with a consequence, number instead of adjective, risk reversal visible. Only then run the final pass through the `humanizer` subagent (full mode) — it strips AI-isms without softening the voice.

#### Step 4: Save

`outputs/script/vsl-{slug}-{YYYYMMDD}-v{n}.md` with full frontmatter + timestamps + production notes.

#### Step 5: Preview in chat

```
✅ Saved to: outputs/script/vsl-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Hook (0-15s): "{{text}}"
   • Named mechanism: {{name}}
   • Final CTA: "{{text}}"
   • Estimated length: {{N}} min
   • Humanizer status: ✓ full pass

👉 Next steps:
   1. Record the VSL or hand it to the video team
   2. /hormozi-gtm:hooks --product={{slug}} → hook variations for A/B testing
   3. /hormozi-gtm:review --ref=outputs/script/... → if you want a brutal review
```

### Short-form / Batch format

#### Step 1: Intake

Asks:
- Primary platform (Reels, TikTok, Shorts)
- How many angles to cover (3-5 default)
- How many variants total (default 6 = 2 per angle)

#### Step 2: Build

Delegate to `ad-architect`. For each variant:
- Angle (pain / desire / contrarian / curiosity / proof)
- 30s version and 60s version
- On-screen text
- Hook that reads on its own as a tweet

Run the quality tests:
- Does it work muted with captions?
- Does the hook have specificity?
- Does the CTA have a verbal action?

#### Step 3: Agent's top 3

Ranks the variants and justifies the top 3 with a specific criterion (not "I liked it better").

#### Step 4: Humanizer (full)

Validate each variant against the `hormozi-voice` rubric (gate ≥7) before running it through the `humanizer` subagent (full mode).

#### Step 5: Save

Load the `hormozi-gtm:template-ad-short` skill via the Skill tool and fill in the skeleton. Save to `outputs/script/short-{slug}-{YYYYMMDD}-v{n}.md`.

#### Step 6: Test plan

Suggests an A/B test sequence (phase 1, 2, 3).

### REFINE mode

Reads an existing file. Asks:
> "Which variant? Which section? (hook / mechanism / proof / offer / CTA)"

Refines while keeping the rest. Runs the humanizer. Saves v{n+1}.

## Done criteria

### For long-form VSL
- [ ] Hook has specificity in the first 3s
- [ ] Named mechanism (not "my method")
- [ ] 3+ comparable cases in the proof
- [ ] Conditional guarantee in the offer section
- [ ] CTA with a specific verbal action
- [ ] Coherent timestamps
- [ ] Full humanizer applied

### For short-form / batch
- [ ] Works muted with captions
- [ ] Hook reads like a tweet
- [ ] CTA has a specific verbal action
- [ ] Mix of angles (not 6 pain-only hooks)
- [ ] Agent's top 3 with justification
- [ ] Full humanizer applied

## Anti-patterns

- Generic hook ("today I'm going to teach you...")
- A 5min story in a 12min VSL (you lost the viewer)
- Mechanism with no proper name
- Proof with a single case
- "Learn more" CTA with no verbal action
- Short-form that needs audio to make sense

## Expected output

VSL: 1200-2500 words + timestamps + production notes
Short-form batch: 6-10 variants in a comparable format + agent's top 3 + test plan
