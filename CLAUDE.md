# CLAUDE.md — hormozi-gtm

This file guides Claude Code (claude.ai/code) when working in this repo.

## What this repo is

LEVEL's Claude Code plugin — not an executable application. The "artifacts" are structured Markdown (slash commands, agents, skills) that other Claude Code instances load. There's no build, lint, test runner, or package to install.

## Architecture

```
hormozi-gtm/
├── .claude-plugin/plugin.json      # manifest
├── commands/                       # 17 slash commands (entry points)
├── agents/                         # 7 subagents (hormozi-persona + 5 specialists + humanizer)
├── skills/                         # 42 skills (frameworks + strategy + hormozi-voice + 16 template-* skeletons)
├── hooks/hooks.json                # SessionStart banner + aiism-check PostToolUse (consolidated)
└── reference/                      # attributed excerpts from the books (fair-use)
                                    # (output skeletons live in skills/template-*; audit is inline)
```

**Canonical pipeline for a command:**

```
slash command (commands/<x>.md)
    └─ orchestrator: hormozi-persona (always)
         └─ delegate to specialist: offer-architect | ad-architect | pricing-strategist | leads-strategist | money-model-architect
              └─ skills loaded per the command's "Active skills" list
         └─ final step: humanizer subagent — writes to outputs/
```

Invariant rules:

1. **Hormozi persona always on** in any `/hormozi-gtm:*` command. First person, no assistant voice. Don't relax it even on a short operational question. Details in `agents/hormozi-persona.md`.
2. **Humanizer = gate for external copy only** (lp, script, hooks, email, case-study, webinar, content, winback). Diagnostic/strategy/internal work (audit, review, plan, pricing, objections, positioning, churn analysis, onboarding) and interactions stay **raw, brutal Hormozi**. The `lite` mode was removed. Humanizer unifies the voice and protects the bite (command-style CTA, hammer line, aggressive specificity); it never softens. Rules in `skills/humanizer-rules/SKILL.md` and `agents/humanizer.md`.
3. **Frameworks are the source of truth.** Don't invent GTM advice outside what lives in `skills/` + `reference/`. Cite the book chapter/section when you expand on something.
4. **Brutal voice (v1.0).** The voice register lives in `skills/hormozi-voice/` (corpus examples + hard rules + 0–10 brutality rubric, ≥7 gate for external copy). Persona, specialists, and humanizer all load this skill. Commands also load `hormozi-voice` IN-CONTEXT — not just via subagent (robustness in Cowork, where the subagent rarely runs).
5. **Template loading (v1.0).** `${CLAUDE_PLUGIN_ROOT}` does NOT interpolate inside a command body (issue #9354). Each template became a `template-*` skill (de-triggered description) loaded by name through the Skill tool, or inline (audit). The `template-*` skills are the **single source** of the skeleton (the `templates/` folder was removed in 1.0.1 — it was dead duplication); `audit` uses an inline skeleton in the command itself. To change an output's format, edit the matching `template-<name>` skill.
6. **Single-context pipeline (v1.0).** No tier gate / auto-detected "GOD mode" (deep review proved unreliable and added no output gain). Commands orchestrate phases in their own context by loading skills; subagent isolation is opt-in, not auto-detection.

## `gtm-context.md` contract

Every command except `/hormozi-gtm:init` reads `gtm-context.md` at the root of the consuming project (not this repo). It's the persistent company/client memory: ICP, offer, brand voice, Core Four split, stage, output language.

- Canonical schema: the `template-gtm-context` skill.
- If it's missing, commands fire `/hormozi-gtm:init` automatically before proceeding.
- If `last_updated` is >30 days old, commands warn "stale context" and suggest `--refresh`.
- Edit command flows while preserving this contract — breaking the auto-detection breaks the whole plugin.

## Output conventions

Defined in `skills/output-conventions/SKILL.md`. Load-bearing details:

- Path: `outputs/<type>/<type>-<slug>-<YYYYMMDD>-v<n>.md` in the consuming project.
- Versioning increments. Never overwrite without `--overwrite`.
- Required frontmatter: `plugin`, `plugin_version`, `command`, `version`, `status`, `created`, `client`, `product`, `frameworks`, `humanizer_pass`, `humanizer_mode`, `voice`, `language`.
- `humanizer_pass: false` is the external release gate.

## Argument conventions

Every command follows the `--flag=value` pattern. There are no positional arguments — that avoids ambiguity between "product slug" and "file path".

**Shared flags (same meaning across all commands):**

| Flag | Purpose |
|---|---|
| `--product=<slug>` | Product slug (kebab-case). Read from `gtm-context.md` if omitted, or asked in chat. |
| `--ref=<path>` | Path to a prior output (refine / create a v2). E.g. `--ref=outputs/lp/lp-revops-20260519-v1.md`. |
| `--focus=<section>` | In refine mode (`--ref`), focuses on a specific part of the material. E.g. `--focus=hero` on the LP. |
| `--full-rewrite` | In refine mode (`--ref`), creates a v2 from scratch, using the prior version only as `parent_version`. |
| `--no-humanize` | Skips the humanizer pass (debug or A/B test). Saves with `humanizer_pass: false`. **Only exists on external-copy commands** (lp, script, hooks, email, case-study, webinar, content-hub→pieces, churn-prevention→winback). On internal/diagnostic commands (audit, review, plan, pricing, objections, positioning, onboarding) the flag doesn't exist — those ship raw and never humanize. |

**Command-specific flags:**
- `init`: `--refresh` (reopens the interview, keeping `gtm-context.md` as the base).
- `script`: `--format=vsl|reels|shorts|tiktok`, `--batch`, `--n=N`.
- `hooks`: `--n=N`, `--angle=dream|problem|secret|contrarian|proof`.
- `lp`: `--skip-audit` (ignores the missing-audit warning).
- `plan`: `--type=company|product`.
- `email`: `--type=cold|warm|nurture|re-engagement`.

**Rule:** if you're thinking about adding a new positional arg, turn it into a `--flag` first. It avoids "is this path a reference or a destination?" and keeps Claude Code's autocomplete useful.

## Common tasks

### Validate a command manually

There's no test runner. Validation means running the command inside a real consuming project:

```bash
claude --plugin-dir .   # from the plugin's root dir, or an absolute path if running elsewhere
/hormozi-gtm:init
/hormozi-gtm:audit
```

### Add a new command

1. Create `commands/<name>.md` with frontmatter (`description`, `argument-hint`).
2. List the orchestrating persona, the specialist, the skills, the template, the humanizer rule.
3. Add a `template-<name>` skill with the new output's skeleton (de-triggered description), or inline it in the command.
4. Update `skills/output-conventions/SKILL.md`.
5. Bump `version` in `.claude-plugin/plugin.json` + an entry in `CHANGELOG.md`.

### Publish a new version

1. Bump `version` in `.claude-plugin/plugin.json` (SemVer).
2. Bump `metadata.version` and `plugins[0].version` in `.claude-plugin/marketplace.json` (same SemVer — the `release.yml` workflow checks that all three match).
3. Update `CHANGELOG.md` (move from `[Unreleased]` into a new `[X.Y.Z]` section).
4. Commit, push to `main`.
5. `git tag vX.Y.Z && git push origin vX.Y.Z` — fires the `release.yml` workflow (builds the ZIP, creates the release, pulls notes from the CHANGELOG).
6. Clients get it via `/plugin update hormozi-gtm` (marketplace lives in the same repo).

> The skeletons (`template-*` skills) use `plugin_version: {{plugin_version}}` as a dynamic placeholder. You don't need to edit them on every bump — the command reads the value from `.claude-plugin/plugin.json` when it generates the output.

## Roadmap

> v0.1.x → v0.4.x: closed (see `CHANGELOG.md` for details).

### [0.5.0+] Distant roadmap (optional)
- `settings.json` customization (client declares `humanizer_mode_default`, Hormozi intensity, output preferences).
- Multiple clients in parallel (gtm-context.md is singular today — future: `gtm-context-{slug}.md` per client).
- `/hormozi-gtm:export` command — packs one client's outputs into a zip for delivery.
- A/B testing automation — integration with ad platforms (depends on an external API).

### Not planned (manual workflow required)
- CRM sync (`gtm-context.md` stays hand-maintained for now).

## Editing content

- **Persona** (`agents/hormozi-persona.md`): the voice invariant. Don't soften it.
- **Humanizer** (`agents/humanizer.md` + `skills/humanizer-rules/SKILL.md`): EN + PT-BR lists of AI-isms. Add a new pattern in both files.
- **Reference** (`reference/*.md`): short excerpts only (≤10% of a chapter), with attribution and a fair-use disclaimer at the top.
- **CHANGELOG**: any change in `commands/`, `agents/`, or `skills/` (including the `template-*` ones) needs an entry.
