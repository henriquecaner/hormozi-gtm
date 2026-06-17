---
description: B2B webinar structure (30-45min) — educational on the surface, selling in the structure. Different from a direct-response VSL (12min). Hook + problem + mechanism + cases + offer + Q&A. For B2B SaaS, high-ticket consulting, offers that need education before the close.
argument-hint: "[--product=<slug>] [--ref=<path>] [--duration=30|45|60] [--format=zoom|youtube|prerecorded] [--no-humanize]"
---

# /hormozi-gtm:webinar

A VSL is direct-response (12min, B2C/transactional). A webinar is educational (30-60min, B2B/high-ticket). Same Hormozi persona, different structure. This one covers the B2B structure.

## Persona loading

Use `hormozi-persona` to orchestrate. Delegate to `ad-architect` to write the full script, and `offer-architect` for the offer block. Final pass through the `humanizer` in **full** mode (a webinar is delivered live / recorded for an external client audience).

**In-context voice (non-negotiable):** Load the `hormozi-voice` skill via the Skill tool and imitate the register — don't rely on the subagent alone, in Cowork it may not run. Hook, offer, guarantee, and CTA are external copy: they only ship at brutality **≥7 on the hormozi-voice rubric**. Below that, rewrite before moving on.

Generate all client-facing copy in the language set in gtm-context `language` (default English). The voice and brutality rules are language-independent and apply in every language.

## Active skills

- `hormozi-voice` (voice register — loaded in-context)
- `template-webinar-agenda` (output skeleton — loaded in-context)
- `hook-framework` (opening)
- `vsl-7-step` (adapted for 30-45min)
- `grand-slam-offer` (offer block)
- `value-equation` (mechanism anchoring)
- `guarantees` (CTA with a guarantee)
- `humanizer-rules` (full mode)
- `output-conventions`

## Arguments

| Argument | Behavior |
|---|---|
| (empty) | Interactive mode: asks for length + format + goal |
| `--product=<slug>` | Product slug |
| `--ref=<path>` | Refine an existing webinar |
| `--duration=30\|45\|60` | Total length (default 45) |
| `--format=zoom\|youtube\|prerecorded` | Live (real Q&A) or pre-recorded (simulated Q&A) |
| `--no-humanize` | Skips humanizer (debug) |

## Prerequisites

1. `gtm-context.md` exists → loads ICP, offer, brand voice
2. Recent audit → loads it as `audit_ref`
3. At least 2-3 case studies available (without cases, a B2B webinar turns into theory)
4. For `--format=prerecorded`: the full script needs to cover the expected objections (no real Q&A)

## Flow

### Step 1: Calibrate length and format

| Length | Typical format | Use when |
|---|---|---|
| 30min | Demo + short Q&A | Audience already familiar with the category; B2B SaaS product; deal size $5-30k/mo |
| 45min | Educational + selling | Audience needs a framework first; high-ticket consulting $30-100k |
| 60min | Deep educational + Q&A | Audience new to the problem; deal size $100k+ enterprise |

### Step 2: Block-by-block structure (45min as default)

| Block | Length | Function | Dependency |
|---|---|---|---|
| Open + housekeeping | 2-3min | Hook + agenda + Q&A rules | `hook-framework` |
| Problem diagnostic | 8min | How the problem shows up, why no one solves it, the cost of the problem | Inputs from `gtm-context.md` |
| Named mechanism | 10-12min | Proprietary framework + components + how it works | `value-equation`, company frameworks |
| Cases | 8min | 2-3 numeric before/after (not 1, not 5) | `case-study` skill, audit_ref |
| Offer + bonuses + guarantee | 5-7min | Grand Slam Offer + tiering + scarcity | `grand-slam-offer`, `guarantees` |
| Q&A | 10-15min | Real (live) or simulated (prerecorded) | `objections` skill if available |
| Close + CTA | 2-3min | Final direction, next steps | `ad-copy-formula` (specific CTA) |

### Step 3: Build the blocks

Delegate to `ad-architect` with a per-block brief:
- For "Named mechanism": distill the company's signature framework into 4-6 named components.
- For "Cases": pull 2-3 case studies, each with 90-120 seconds of exposition.
- For "Offer": delegate to `offer-architect` to tie together bonuses + guarantee + visual tiering.

### Step 4: Anti-pattern check

For `--format=prerecorded`:
- The simulated Q&A needs to cover the top 3-5 objections (pull from `objections` if it exists).
- No improvised ad-libs (all content has to be in the script).

For `--format=zoom` (live):
- Q&A can be real (not scripted).
- But you need "plant questions" prep — 3-5 questions you know will come up, with answers rehearsed in your head.

### Step 5: Humanizer (full)

A webinar is delivered live / recorded for the client's audience — external copy. Run the full script through the `humanizer` subagent in **full** mode before saving. Load `humanizer-rules` in-context so you don't rely on the subagent alone. Hook, offer, guarantee, and CTA already cleared the `hormozi-voice` ≥7 gate in Step 3 — the humanizer strips AI-isms without softening the Hormozi voice. In the output frontmatter: `humanizer_pass: true`, `humanizer_mode: full`. (`--no-humanize` saves with `humanizer_pass: false` — debug/A-B only.)

### Step 6: Save

Load the `hormozi-gtm:template-webinar-agenda` skill via the Skill tool and fill in the skeleton (frontmatter + all blocks), replacing every `{{...}}`. Save to:

`outputs/webinar/webinar-{product_slug}-{YYYYMMDD}-v{n}.md`

### Step 7: Preview in chat

```
✅ Saved to: outputs/webinar/webinar-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Total length: {{N}} min
   • Format: {{zoom | youtube | prerecorded}}
   • Hook: "{{first 80 chars}}..."
   • Named mechanism: {{name}}
   • Cases included: {{N}} (references: {{slugs}})
   • CTA: "{{text}}"
   • Humanizer status: ✓ full pass

👉 Next steps:
   1. One rehearsal (live) or technical recording (prerecorded)
   2. Slides in parallel (don't run a webinar without visual support)
   3. /hormozi-gtm:objections to prep the Q&A if you don't have one yet
```

## Done criteria

- [ ] Hook passes the tweet test (reads on its own and opens a curiosity gap)
- [ ] Named mechanism with 4-6 components
- [ ] 2-3 concrete cases (no more — diluted)
- [ ] Offer with an odd number of bonuses + conditional guarantee
- [ ] Specific CTA at the close (not "let's chat?")
- [ ] Q&A prepped (live: plant questions; prerecorded: scripted)
- [ ] Total length ≤ planned + 10% buffer

## Anti-patterns

- 100% educational webinar with no offer (turns into a free class)
- 100% selling webinar with no framework (turns into a boring 45min pitch)
- Mechanism with no proper name (turns into "my methodology")
- 5+ cases (the audience loses the thread)
- Improvised Q&A with no prep (live, hard questions break credibility)
- Generic hook ("Today I'm going to share...")
- Slides with 200 words per slide
- Forgetting scarcity in the CTA (didn't close on the webinar → won't close in 48h)
