<div align="center">

<a href="https://github.com/henriquecaner/hormozi-gtm">
  <img src=".github/assets/hero.png" alt="Hormozi GTM — LEVEL Edition · 17 commands · brutal Hormozi voice · persona always on" width="100%"/>
</a>

# Hormozi GTM — LEVEL Edition

**Alex Hormozi–style GTM operation for the LEVEL team and its clients.**

A Claude Code plugin with 17 commands, 42 skills (Hormozi frameworks + voice register + output skeletons), 7 specialized subagents, and a `gtm-context.md` contract that persists across sessions. Hormozi persona always on, brutal voice calibrated by a rubric. Humanizer runs on external copy only.

[![License](https://img.shields.io/badge/license-proprietary-blue)](./LICENSE)
[![Latest Release](https://img.shields.io/github/v/release/henriquecaner/hormozi-gtm?color=green&label=release)](https://github.com/henriquecaner/hormozi-gtm/releases/latest)
[![Commands](https://img.shields.io/badge/commands-17-purple)](#command-catalog)
[![Skills](https://img.shields.io/badge/skills-42-purple)](#skill-catalog)
[![Agents](https://img.shields.io/badge/agents-7-blueviolet)](#agent-pipeline)
[![Hooks](https://img.shields.io/badge/hooks-2-orange)](#hooks)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-D97757)](https://docs.claude.com/en/docs/claude-code)
[![Claude Cowork](https://img.shields.io/badge/Claude%20Cowork-ready-D97757)](#installation)

[Quickstart](#quickstart) · [Commands](#command-catalog) · [Skills](#skill-catalog) · [Pipeline](#agent-pipeline) · [Hooks](#hooks) · [Installation](#installation) · [Author](#author)

</div>

---

## What it is

GTM consulting wastes too much time re-explaining the same context to an AI every session. ICP, offer, brand voice, positioning, Core Four split. You spell it all out on Tuesday, lose the details by Friday, spell it out again the next week. Every asset comes out in a slightly different tone than the last. The client notices the inconsistency before you do.

The second problem costs more: AI-generated copy is recognizable in seconds. Em-dash overuse, rule of three, "stands as a testament," "navigating the challenges." When a landing page or ad hook lands on the client's desk reading like that, the project's credibility goes with it.

**Hormozi GTM** solves both at once. `/hormozi-gtm:init` runs a guided interview and writes `gtm-context.md` to the project root; every command after that reads the file automatically, so you never reintroduce anything. Every client-facing output (LP, VSL script, hook, ad, email, proposal) passes through a humanizer agent with EN and PT-BR AI-pattern lists before it's saved, and `humanizer_pass: true` in the frontmatter is the release gate. The Alex Hormozi persona stays in first person across all 17 commands — no "great question" or "hope that helps" — with a 7-agent pipeline hardened against voice drift and specialists straying out of their lane.

Coverage: acquisition (cold/warm/organic/paid), conversion (LP/VSL/hook/objections), high-ticket closing ($30k+ proposals), delivery (30-day onboarding), retention (churn analysis + winback). Frameworks from all four Hormozi books plus the leaked playbook, with a new strategic layer (niche-selection, founder-market-fit, market-saturation-pivot) that most GTM plugins leave out.

## Quickstart

### Case 1 — New client, from scratch

```bash
/plugin marketplace add henriquecaner/hormozi-gtm
/plugin install hormozi-gtm@hormozi-gtm-marketplace
/hormozi-gtm:init                                       # 8-question interview → gtm-context.md
/hormozi-gtm:audit                                      # Value Equation diagnostic
/hormozi-gtm:lp --product="product-name"                # sales LP with humanizer pass
```

### Case 2 — Don't know where to start

```bash
/hormozi-gtm:help                                       # 3-question decision matrix
```

### Case 3 — Validated offer, need leads

```bash
/hormozi-gtm:plan                                      # Core Four split + 90-day money model
/hormozi-gtm:email --type=cold                          # 5–7 touch sequence
/hormozi-gtm:hooks --n=12                               # variants for A/B testing in ads
```

More scenarios in `/hormozi-gtm:help`.

## Command catalog

17 commands organized by GTM funnel stage:

### Onboarding and diagnostic

| Command | Function | Output |
|---|---|---|
| `/hormozi-gtm:init` | Builds `gtm-context.md` via a guided interview | `gtm-context.md` |
| `/hormozi-gtm:help` | Decision matrix — recommends a command by objective | (no output) |
| `/hormozi-gtm:audit` | Value Equation diagnostic (critical bottleneck + top 3 levers) | `outputs/audit/` |

### External copy

| Command | Function | Output |
|---|---|---|
| `/hormozi-gtm:lp` | Landing page (Grand Slam Offer + 10 structured sections) | `outputs/lp/` |
| `/hormozi-gtm:script` | Long-form 7-step VSL or short-form for Reels/Shorts/TikTok | `outputs/script/` |
| `/hormozi-gtm:hooks` | Battery of 10–20 ad variants (default 15) for A/B testing | `outputs/hooks/` |

### Acquisition and closing

| Command | Function | Output |
|---|---|---|
| `/hormozi-gtm:email` | Cold/warm/nurture/re-engagement sequence (5–7 touches) | `outputs/email/` |
| `/hormozi-gtm:objections` | Objection matrix by ICP + sales-call scripts | `outputs/objections/` |
| `/hormozi-gtm:case-study` | Before/after case study + derived assets | `outputs/case-studies/` |
| `/hormozi-gtm:webinar` | B2B 30–45 min structure (educational + sell) | `outputs/webinar/` |
| `/hormozi-gtm:positioning` | Competitive teardown + positioning statement | `outputs/positioning/` |

### Pricing and business model

| Command | Function | Output |
|---|---|---|
| `/hormozi-gtm:pricing` | Review against the 5 Pricing Playbook laws (range + tiering) | `outputs/pricing/` |
| `/hormozi-gtm:plan` | 90-day GTM plan (Core Four + 4-tier money model) | `outputs/plan/` |

### Delivery, retention, and content

| Command | Function | Output |
|---|---|---|
| `/hormozi-gtm:client-onboarding` | First 30 days post-sale (5 milestones + triggers) | `outputs/client-onboarding/` |
| `/hormozi-gtm:churn-prevention` | Win/loss + churn analysis + retention playbook (+ optional winback) | `outputs/retention/` |
| `/hormozi-gtm:content-hub` | 30–90 day organic content roadmap | `outputs/content/` |

### Refinement

| Command | Function | Output |
|---|---|---|
| `/hormozi-gtm:review` | Brutal feedback + Re-review mode (v1↔v2 delta) | new `v{n+1}` version |

**Argument convention:** every command uses `--flag=value`. Shared flags: `--product=<slug>`, `--ref=<path>` (refine), `--focus=<section>`, `--full-rewrite`, `--no-humanize`. Details in [`CLAUDE.md`](./CLAUDE.md).

## Skill catalog

**Hormozi frameworks** (6)
`grand-slam-offer` · `value-equation` · `money-models` · `ltv-cac` · `core-four` · `leila-scaling`

**Strategy (invisible prerequisites)** (3)
`niche-selection` · `founder-market-fit` · `market-saturation-pivot`

**Copy + Ads** (7)
`hook-framework` · `vsl-7-step` · `ad-copy-formula` · `scarcity-urgency` · `guarantees` · `bonus-stacking` · `lead-magnets`

**Advanced acquisition + conversion** (4)
`content-engine` · `ad-creative-testing` · `sales-sequencing` · `productization`

**Deliverability + high-ticket closing** (2)
`email-deliverability` · `proposal-architecture`

**Pricing** (1)
`pricing-playbook`

**Operational + voice** (3)
`output-conventions` · `humanizer-rules` · `hormozi-voice` (brutal voice register + 0–10 brutality rubric)

**Output skeletons** (16) — internal, loaded by the command via the Skill tool (reliable on both CLI and Cowork)
`template-gtm-context` · `template-lp` · `template-vsl` · `template-ad-short` · `template-hooks-batch` · `template-email-sequence` · `template-case-study` · `template-webinar-agenda` · `template-content-roadmap` · `template-churn-analysis` · `template-review` · `template-plan` · `template-pricing-review` · `template-objections-matrix` · `template-positioning-map` · `template-client-onboarding`

Skills load only when a command declares them under `Active skills`. `output-conventions` and `humanizer-rules` run on every external output.

## Agent pipeline

The plugin runs as a 7-agent pipeline with structured hand-off contracts, not as a loose pile of prompts. Every command invocation follows:

```
slash command
    ↓
hormozi-persona (orchestrator — always)
    ↓
delegated specialist (by domain)
    ↓
humanizer (external copy only, before saving)
    ↓
outputs/<type>/<file>.md
```

### The 7 agents

| Agent | Role | When it enters |
|---|---|---|
| `hormozi-persona` | Orchestrator. Invariant first-person Hormozi voice. Validates each specialist's output before hand-off. | Always — entry point for every command |
| `offer-architect` | Diagnoses the offer via Value Equation, proposes top 3 levers, rewrites it in one paragraph | `/audit`, `/lp`, `/script` |
| `ad-architect` | Writes hooks, 7-step VSLs, ad copy | `/lp`, `/script`, `/hooks`, `/email`, `/webinar` |
| `pricing-strategist` | Review against the 5 laws. Range + tiering + anchoring | `/pricing`, `/plan` |
| `leads-strategist` | Core Four split + primary channel + roadmap | `/plan`, `/email` |
| `money-model-architect` | 4 tiers (Attraction/Core/Upsell/Continuity) + LTGP/CAC | `/plan`, `/pricing` |
| `humanizer` | Refines copy against AI patterns (PT-BR + EN) | Last step of every external output |

### Hand-off contracts

Each specialist declares, in structured Markdown, the exact output format it returns to the orchestrator. Examples:

- `offer-architect` → Value Equation scores (1–10 per vector) + critical bottleneck + top 3 levers with expected lift + rewritten offer
- `pricing-strategist` → 5 laws scored (green/yellow/red) + $X–Y range + Silver/Gold/Platinum tiering + validation test
- `money-model-architect` → 4 tiers with pricing + LTGP/CAC/payback math + text funnel diagram

The orchestrator validates each hand-off before invoking the next agent. If the output doesn't meet the checklist, it sends it back with a specific question instead of improvising.

### Recovery / fallback

Each agent has documented behavior for incomplete input:

- `offer-architect` with no quantitative data → assigns a score at intermediate confidence, marks fields as `(estimate)`
- `pricing-strategist` with no unit economics → gives a conservative range + flags "market estimate, not a validated recommendation"
- `humanizer` rejects the output → saves with `humanizer_pass: false` + a note, orchestrator warns the user

Pipeline details and a 10-step end-to-end example in [`agents/hormozi-persona.md`](./agents/hormozi-persona.md).

## Hooks

| Hook | Type | Function |
|---|---|---|
| `session-start` | SessionStart | Banner on session open — reminds you the persona is active and the humanizer is mandatory |
| `post-tool-aiism-check` | PostToolUse (`Write\|Edit\|MultiEdit`) | Scans freshly modified `outputs/*.md` for residual AI-isms. Soft warning, never blocks. Defense in depth if the humanizer misses something. |

Scan script in `scripts/check-aiisms.py` — pure Python stdlib, detects inflated vocabulary, assistant voice, em-dash overuse, hedging. Capped at 20 hits per file to avoid flooding the terminal.

## Outputs

Every command that produces material saves to `outputs/<type>/<slug>-{YYYYMMDD}-v{n}.md` in the consumer project:

```
outputs/
├── audit/                    ├── email/                    ├── retention/
├── lp/                       ├── objections/               ├── client-onboarding/
├── script/                  ├── case-studies/             ├── content/
├── hooks/                    ├── webinar/                  └── review/
├── pricing/                  ├── positioning/
├── plan/
```

Versioning increments; it never overwrites without `--overwrite`. Standard frontmatter: `plugin_version`, `command`, `version`, `status`, `client`, `product`, `frameworks` (skills used), `humanizer_pass`, `humanizer_mode`, `voice`, `language`, `audit_ref`, `pricing_ref`, `parent_version`.

Full convention in [`skills/output-conventions/SKILL.md`](./skills/output-conventions/SKILL.md).

Recommendation: add `outputs/` to the consumer project's `.gitignore`, or version everything depending on your delivery flow.

## Persona and humanizer

The Alex Hormozi persona is active across all `/hormozi-gtm:*` commands. First person, no assistant voice. Even on a plain operational question, the answer comes out in the persona's direct tone. It doesn't relax.

The humanizer runs as the last step before saving any **external** output (LP, script, hooks, email, case study, webinar, content pieces, winback). It gates external copy only. Diagnostic, strategic, and internal output (audit, review, plan, pricing, objections, positioning, churn analysis, onboarding) stays raw — Hormozi brutal, never softened, no humanizer pass. On external copy the humanizer makes two passes and validates against both EN and PT-BR AI-pattern lists; it unifies the voice and protects the bite (command CTAs, hammer lines, aggressive specificity) instead of sanding it down.

It emits `humanizer_pass: <bool>` in the output frontmatter. `humanizer_pass: false` is the external release gate.

The `--no-humanize` flag exists for debugging and A/B tests, and only on the external-copy commands.

Full rules in [`skills/humanizer-rules/SKILL.md`](./skills/humanizer-rules/SKILL.md).

## Installation

### Claude Code (CLI or Desktop)

```bash
/plugin marketplace add henriquecaner/hormozi-gtm
/plugin install hormozi-gtm@hormozi-gtm-marketplace
```

### Claude Cowork (Desktop app)

Download the ZIP from the latest release at [github.com/henriquecaner/hormozi-gtm/releases/latest](https://github.com/henriquecaner/hormozi-gtm/releases/latest). Inside the app:

1. `+` → **Create plugin** → **Upload plugin**
2. Drag in the ZIP

The plugin shows up under **Personal plugins** and the `/hormozi-gtm:*` commands become available.

## Compatibility

| Environment | Status |
|---|---|
| Claude Code CLI | supported |
| Claude Code Desktop (Mac/Win) | supported |
| Claude Cowork (Desktop app) | supported (ZIP upload) |
| Claude.ai (web) | not supported |

## Versioning

SemVer. Changes are cataloged in [`CHANGELOG.md`](./CHANGELOG.md). Releases are automated by a `v*` tag (the `release.yml` workflow):

1. Bump `version` in `.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` (3 places, validated by CI)
2. Add a `## [X.Y.Z]` section to `CHANGELOG.md`
3. `git tag vX.Y.Z && git push origin vX.Y.Z`

The workflow fires, builds the ZIP, extracts notes from the CHANGELOG, and publishes the GitHub release.

### Roadmap

Longer-horizon roadmap in `[0.5.0+]` (see [`CLAUDE.md`](./CLAUDE.md)): customization via `settings.json`, multiple clients in parallel (gtm-context per slug), an `/export` command to package outputs.

## Local development

```bash
git clone https://github.com/henriquecaner/hormozi-gtm.git
cd hormozi-gtm
claude --plugin-dir .
```

To build a local ZIP without triggering an official release:

```bash
bash scripts/build-zip.sh
```

Architecture details in [`CLAUDE.md`](./CLAUDE.md).

## Author

[LEVEL](https://github.com/henriquecaner) — Henrique Caner ([caner@thelevel.com.br](mailto:caner@thelevel.com.br)).

## License

Proprietary — LEVEL. Licensed for use by contract. Distribution restricted to the internal team and contractual clients.
