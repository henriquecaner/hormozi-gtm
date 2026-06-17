---
description: Generates a batch of 10-20 hook/headline/subject-line variants. Mix of angles (dream/problem/secret/contrarian/proof). Agent picks the top 3 at the end with reasoning. Humanizer full mode.
argument-hint: "[--product=<slug>] [--ref=<path>] [--n=N] [--angle=<dream|problem|secret|contrarian|proof>] [--no-humanize]"
---

# /hormozi-gtm:hooks

Generates batches of hooks/headlines/subject lines for A/B testing. Default is 15 variants covering 5 angles.

## Persona loading

Orchestrator: `hormozi-persona`.
Specialist: `ad-architect`.
Final pass: `humanizer` (full mode — hooks go to the client).

**IN-CONTEXT voice loading (mandatory):** load the `hormozi-voice` skill via the Skill tool and imitate the register — don't rely on the subagent alone (in Cowork it may not run). Hooks are external copy: each hook only ships at **brutality ≥7 on the hormozi-voice rubric**. Below 7, rewrite before listing.

Generate all client-facing copy in the language set in gtm-context `language` (default English). The voice and brutality rules are language-independent and apply in every language.

## Active skills

- `hormozi-voice` (brutal voice register + 0-10 rubric — loaded in-context)
- `hook-framework` (core — 3 canonical types + extra angles)
- `ad-copy-formula` (per-channel structure)
- `template-hooks-batch` (output skeleton — loaded in-context)
- `humanizer-rules` (full mode)
- `output-conventions`

## Arguments

| Argument | Behavior |
|---|---|
| (empty) | Pulls the offer from `gtm-context.md` |
| `slug` | Product/offer slug |
| `outputs/lp/<file>.md` | Generates hooks to refine that asset's headline |
| `--n=N` | Total count (default 15) |
| `--angle=<type>` | Focuses on 1 angle (generates N of the same type) |
| `--no-humanize` | Skips the humanizer |
| `--overwrite` | Overwrites v{n} |

## Prerequisites

1. `gtm-context.md` exists → loads ICP, offer, transformation, external audience, tone intensity
2. Otherwise → asks in chat (3 questions minimum)

## Flow

### Step 1: Collect inputs (if needed)

If `gtm-context.md` is complete, skip straight to Step 2.

Otherwise ask:
1. ICP (1 specific sentence)
2. Offer (what you sell)
3. Promised transformation (in what timeframe, who becomes what)

### Step 2: Mix strategy

Default: spread across 5 angles
- Dream outcome (3-5 hooks)
- Problem (3-5 hooks)
- Secret (3-5 hooks)
- Contrarian (2-3 hooks)
- Proof (2-3 hooks)

If `--angle=X`, generate N of the same type.

### Step 3: Generation

Delegate to `ad-architect`. For each hook:

- The line (with numeric specificity where possible)
- Angle
- Mechanism (which emotion/thought it triggers)
- Where to use it (LP headline / short ad / email subject / etc.)

Run the 3 quality tests:
- Numeric specificity
- Tweet test
- Curiosity gap

### Step 4: Agent's top 3

Ranks and justifies the top 3 with a specific criterion (not "I liked it best"). Each of the top 3 has:
- Full line
- Why it's a top pick
- Where to test it first (platform + format)

### Step 5: Humanizer (full)

Hooks are external copy — full mode is mandatory. Pass the hooks through the `humanizer` subagent (full mode) AND check them against `humanizer-rules`. Even after the humanizer, each hook has to hold brutality ≥7 on the `hormozi-voice` rubric — the humanizer strips AI-isms, it doesn't soften the voice. Frontmatter ships with `humanizer_pass: true` / `humanizer_mode: full`.

### Step 6: Save

Load the `hormozi-gtm:template-hooks-batch` skill via the Skill tool and fill in the skeleton. Save to `outputs/hooks/hooks-{slug}-{YYYYMMDD}-v{n}.md`.

### Step 7: Preview in the conversation

```
✅ Saved to: outputs/hooks/hooks-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Total count: {{N}} hooks
   • Top 3 picked by the agent:
     1. "{{text}}" — {{angle}}, {{criterion}}
     2. "{{text}}" — {{angle}}, {{criterion}}
     3. "{{text}}" — {{angle}}, {{criterion}}
   • Humanizer status: ✓ full pass

👉 Next steps:
   1. Test the top 3 in ads ($200-500 each, 48h)
   2. Winner becomes the headline of the next LP
   3. /hormozi-gtm:script --product={{slug}} using the winning hook
```

## Done criteria

- [ ] Mix of angles (not 15 pain-only hooks) — unless `--angle=` was passed
- [ ] Numeric specificity in at least 60% of the hooks
- [ ] No generic hook ("discover the secret")
- [ ] Agent's top 3 with an explicit criterion
- [ ] Suggested test plan
- [ ] Brutality ≥7 on the `hormozi-voice` rubric for every hook (external copy)
- [ ] Humanizer full applied
- [ ] File saved with frontmatter

## Anti-patterns

- "Discover the secret to X" (generic)
- "Want to make more money?" (generic yes/no)
- Hooks that depend on lost context
- Top 3 with no specific justification ("I liked it best")
- Homogeneous mix (15 dream outcomes) without the user asking for it

## Expected output

File: table of N hooks + top 3 + test plan (~500-800 words)
Conversation: top 3 + path (~5 lines)
