# Changelog

All notable changes to this plugin live here. Format based on [Keep a Changelog](https://keepachangelog.com/), versioning per [SemVer](https://semver.org/).

## [Unreleased]

### Planned
- Onboarding doc specific to LEVEL clients (an operational guide separate from the plugin)
- `settings.json` customization (client declares `humanizer_mode_default`, Hormozi intensity)
- Parallel multi-client (`gtm-context-{slug}.md` per client vs. the single file today)
- `/hormozi-gtm:export` — packages one client's outputs into a zip for delivery

## [2.0.0] — 2026-06-17

English as the authoring base language + multilingual output. Breaking: command and flag names changed.

### Changed (BREAKING)

- **Plugin authored in English.** All commands, agents, skills, templates, reference extracts, README, CLAUDE.md, manifests, and the SessionStart banner were migrated from Brazilian Portuguese to native English. The voice files (`hormozi-voice`, `hormozi-persona`, `humanizer`, `humanizer-rules`) were rebuilt from Hormozi's original English rather than translated, to avoid a round-tripped, translated texture. Chat/runtime output language is independent (see multilingual, below).
- **Commands renamed:** `plano` → `plan`, `roteiro` → `script`, `onboarding-cliente` → `client-onboarding` (the other 14 were already English). Output folders renamed to match (`outputs/plan/`, `outputs/script/`, `outputs/client-onboarding/`).
- **Flags renamed to English:** `--produto` → `--product`, `--tipo` → `--type`, `--objetivo` → `--objective`, `--foco` → `--focus`, `--duracao` → `--duration`, `--competidores` → `--competitors`, `--angulo` → `--angle`, `--formato` → `--format`, `--plataforma` → `--platform`, `--segmento` → `--segment`, `--cliente` → `--client`, `--antes` → `--before`, `--depois` → `--after`. Flag values too (`empresa|produto` → `company|product`, etc.). Output frontmatter keys renamed (`voz` → `voice`, `empresa_*` → `company_*`, `material_tipo` → `material_type`, and the PT template-skeleton keys).

### Added

- **Multilingual output.** A `language` field in `gtm-context.md` (default `en`) drives the language of generated client copy; authoring stays English. The persona and every copy-producing command carry an output-language rule; all 16 output templates carry `language: {{language}}`; `output-conventions` documents the field. The voice and brutality rules are language-independent — copy is written native in the target language, never translated. The humanizer keeps both EN and PT-BR AI-ism lists.

### Fixed

- **Leftover `lite` mode (deprecated in v1.0) removed.** `skills/humanizer-rules/SKILL.md` documented lite/full and assigned "lite" to audit/review/plan — contradicting the invariant (internal = raw, external = full). The scope section was rewritten. `commands/review.md` had a "Humanizer lite applied" checklist item that conflicted with its own body. `skills/output-conventions/SKILL.md`: `humanizer_mode` enum corrected (`full | lite` → `full | n/a`), documented the `voice` field and the internal-output convention, and refreshed the `command:` enum.
- **`--no-humanize` removed from the 4 internal commands** (plan, positioning, pricing, client-onboarding) where it was a no-op — these never humanize. The flag stays only on the external-copy commands.
- **Humanizer scope contradictions resolved.** `agents/hormozi-persona.md` listed "business plan, pricing review" among outputs to humanize (they ship raw); the SessionStart banner listed `pricing` as humanizer-required; `agents/humanizer.md` listed content-hub as external. All aligned to the canonical scope (humanizer = external copy only).
- **`value-equation` description formula** `Dream × Probability ÷ Effort × Time Delay` (which evaluated incorrectly under operator precedence) fixed to `(Dream × Probability) ÷ (Effort × Time Delay)`. The body was already correct.
- **Flag/doc consistency:** `lp` used `--section` and `--focus` for the same idea (unified to `--focus`); `email` was missing `--focus` and `--no-humanize` in its argument-hint; `churn-prevention`'s mode selector was renamed `--focus` → `--mode` to free `--focus` for its shared "refine section" meaning. README fixed (hooks count, `client-onboarding/` tree, removed non-command `/productization`, added `voice`/`language` to the frontmatter list).

### Changed

- **Source disclaimer on heuristic numbers.** `skills/ltv-cac`, `skills/money-models`, and `skills/core-four` presented numeric benchmarks (ratio/payback ranges, pre-launch validation gates, volume/day, channel sequencing) as if they were quoted from the corpus. Added a note distinguishing what's in the extracts from what's derived practical calibration — keeps the "don't invent advice outside skills/ + reference/" invariant honest.
- **`name:` frontmatter added to the 25 framework skills** that only had `description:` — consistency with the `template-*` skills and `hormozi-voice`. Zero functional impact (the loader derived the name from the folder).

## [1.0.1] — 2026-06-01

Post-1.0 hygiene: single-source the skeletons + green CI.

### Changed

- **Templates → single source in skills.** Removed the `templates/` folder (dead duplication — the runtime already loaded the `template-*` skills, never the files). Content preserved in full across the 16 `template-*` skills + the inline `audit` skeleton. Eliminates drift risk (editing a template with no effect). `build-zip.sh`, `release.yml`, `README.md`, `CLAUDE.md`, and `output-conventions` updated.

### CI

- **`lint-hook.yml`** now understands the plugin hook wrapper `hooks/hooks.json` (`{"hooks": {...}}` + `description`), not just the legacy format with events at the top of the JSON.

### Note (by design, not a bug)

- The `claude plugin validate` warning — "root CLAUDE.md is not loaded as context" — is **expected and kept on purpose**: that `CLAUDE.md` is dev documentation (loaded when you open the repo in the Claude Code CLI/IDE), not context meant for the plugin's consumer. Renaming it would break its dev-context role. No action needed.

## [1.0.0] — 2026-06-01

Major release: fixes installation (which hung in both Cowork and the CLI), makes the hooks actually load, resolves template loading, and — the headline — **brutalizes the voice** (output was coming out "polished copywriter," not Hormozi). All validated empirically (CLI + diagnostics). Architecture simplified: single-context pipeline, no tier gate (the "GOD mode with auto-detected subagent" was cut after deep review proved it fragile and no better for the output).

### Fixed (Critical)

- **`.claude-plugin/plugin.json`**: the `repository` field was an object `{type,url}`; the Claude Code schema requires a **string**. This was what hung `/plugin install` (reproduced: "invalid manifest — repository: expected string, received object"). This is the bug that blocked installation.
- **Hooks weren't loading**: they sat in two loose files (`session-start.json`, `post-tool-aiism-check.json`). Claude Code only discovers `hooks/hooks.json` (+ the `"hooks": {}` wrapper). Consolidated into `hooks/hooks.json`; the SessionStart banner and the AI-ism check now fire (proven). Corrects the false claim in CHANGELOG [0.4.2] that the hook had been fixed — it hadn't (the file was never read).
- **Broken template loading (`${CLAUDE_PLUGIN_ROOT}`)**: the variable doesn't interpolate in the markdown body of commands (official issue anthropics/claude-code#9354). Resolved: each template became a **skill** (`skills/template-*`, de-triggered description) loaded by name via the Skill tool, or inline in the body (audit). `init`/`audit` no longer point at the dead path.

### Added

- **`skills/hormozi-voice/`**: single source for the voice register — real examples from the corpus + 8 hard rules (CTA-as-command, zero marketing adjectives, attack the belief before you offer, risk reversal visible) + a **0–10 brutality rubric** (≥7 gate for external copy). Persona, ad-architect, the 5 specialists, and the humanizer all load this skill.
- **16 `template-*` skills**: each output got a loadable skeleton (single source of the format).
- **In-context** voice loading in every command (not dependent on the subagent alone — robustness in Cowork, where the subagent "rarely runs").

### Changed

- **Humanizer = gate for external copy only** (lp, script, hooks, email, case-study, webinar, content, winback). Diagnostic/strategy/internal (`audit`, `review`, `plan`, `pricing`, `objections`, `positioning`, churn analysis, `onboarding`, interactions) stay **raw, brutal Hormozi**. The humanizer now also **unifies the voice** and **protects the bite** (CTA-as-command, hammer line, aggressive specificity — never softens).
- **Channel-split invariant**: orchestration telemetry never enters the `outputs/` file (only the conversation).
- Persona: register taught by **concrete example**, not adjective (the root cause of the lukewarm voice).

### Removed

- **The humanizer `lite` mode** (lightly humanizing internal output softened exactly where the voice has to stay rawest).
- **Tier gate / auto-detected "GOD mode"**: deep review proved tool self-introspection unreliable and no better for the output. Subagent isolation becomes opt-in, not auto-detection.

## [0.4.2] — 2026-05-20

Hotfix for 5 Critical + 6 Important + 3 Minor issues surfaced in the v0.4.1 deep review. Fixes bugs invisible in production (the hook never ran since v0.4.0, a leaky humanizer↔orchestrator contract, undocumented output folders, /help pointing at a shipped command as if it were roadmap).

### Fixed (Critical)

- **`hooks/post-tool-aiism-check.json`**: env var `$CLAUDE_PLUGIN_DIR` (nonexistent) replaced with `${CLAUDE_PLUGIN_ROOT}` (the canonical Claude Code one). The hook hadn't run since v0.4.0 — `||true` swallowed the FileNotFoundError silently. Confirmed against the official docs at code.claude.com/docs/en/hooks.
- **`agents/humanizer.md`**: the contract with the orchestrator is now explicit. The humanizer emits a structured header `humanizer_pass: <bool>` + `humanizer_mode: <lite|full>` before the refined text. Before, the orchestrator validated fields the humanizer never promised to return.
- **`skills/output-conventions/SKILL.md`**: the folder tree was extended with the 9 output folders for the new commands (`email/`, `objections/`, `case-studies/`, `webinar/`, `positioning/`, `content/`, `retention/`, `onboarding/`). Before it listed only 7 folders, violating its own "create the folder before writing" rule.
- **`commands/help.md`**: full retrofit to cover all 17 commands. It used to say "/objections still on the roadmap" though the command has existed since v0.3.0; no entries for email, case-study, webinar, positioning, content-hub, churn-prevention, client-onboarding.
- **`templates/case-study.md`**: a nested placeholder `{{... {{cliente}} ...}}` that broke the parser. Replaced with `{{case_cliente_nome}}`, consistent with the frontmatter. Added an `audit_ref` field to the frontmatter.

### Changed (Important)

- **`hooks/post-tool-aiism-check.json`**: matcher `Write|Edit` → `Write|Edit|MultiEdit`. Before, multi-block edits bypassed the aiism-check gate.
- **`scripts/check-aiisms.py`**: cap of 20 hits per file + a "(+N hits suppressed)" line. A long file with the humanizer skipped no longer floods the terminal.
- **`scripts/check-aiisms.py`**: removed 2 patterns with a high false-positive rate (these were PT-BR-specific; revisit per output language).
- **`.github/workflows/lint-hook.yml`**: hook-type whitelist expanded. PostToolUse/PreToolUse/etc. now accept `{command, mcp_tool, http, prompt, agent}` (the 5 types from the official docs). SessionStart keeps `{command, mcp_tool}` (restricted).
- **`README.md`**: 3 stale "8 commands, 16 skills" strings updated to "17 commands, 25 skills" (hero alt text, tagline, the "What it is" paragraph).
- **`CLAUDE.md`**: "Architecture" section updated from "8 slash commands / 16 skills" to "17 slash commands / 25 skills".

### Polish

- **`CHANGELOG.md`** `[Unreleased]/Planned` cleaned: removed already-delivered items (`/help`, the PostToolUse hook). Replaced with the real v0.5.0+ backlog.
- **`CLAUDE.md`** Roadmap deduplicated: `A/B testing automation` and `Multi-client` appeared in both `[0.5.0+]` and `Not planned`. Each item now sits in a single section.
- **`scripts/build-zip.sh`** + **`.github/workflows/release.yml`**: exclude `* 2.md`, `* 2.json`, `* 2.yml` (macOS Finder/iCloud duplicates). Defense in depth against a `.gitignore` miss.

## [0.4.1] — 2026-05-20

### Fixed (Critical)

- `release.yml` and `scripts/build-zip.sh` now include `scripts/` in the packaged ZIP. v0.4.0 introduced the `post-tool-aiism-check.json` hook, which depends on `scripts/check-aiisms.py`, but the script wasn't in the ZIP — the hook broke silently on Cowork installs (ZIP upload). Clients installing via `/plugin marketplace add` in Claude Code weren't affected (full repo clone).

## [0.4.0] — 2026-05-20

Focus on **retention + high-ticket closing + a last line of defense against AI-isms**. Closes the full acquisition→closing→onboarding→retention loop. The plugin now covers post-sale, not just pre-sale.

### Added — 2 skills (deliverability + closing)

- `email-deliverability` — the technical layer beneath `/email`. Domain warm-up over 4–6 weeks, SPF/DKIM/DMARC setup, a 3-secondary-domain strategy, spam triggers (words + behavior), the metrics that matter (inbox placement, bounce, complaint rate), and a recovery plan if a domain gets burned.
- `proposal-architecture` — high-ticket pricing proposals ($30k+) in 7 sections (reframed problem → mechanism → scope → proof → investment → guarantee → next step) + 5 anti-commoditization patterns (visible tier, odd-numbered bonus stack, conditional guarantee, comparison against real alternatives, genuine scarcity).

### Added — 2 new commands + 2 templates

- `/hormozi-gtm:churn-prevention` + `templates/churn-analysis.md` — churn diagnostic by type (early/mid/late/voluntary/passive), categorization by reason, win/loss interview script (8 questions), a 4-block retention playbook, an optional winback sequence (`--focus=winback`), and projected financial impact.
- `/hormozi-gtm:client-onboarding` + `templates/client-onboarding.md` — a first-30-days journey across 5 milestones (welcome → kickoff → quick win D7 → NPS D14 → mid-point D21 → wrap D30), touch cadence by deal size, quantitative intervention triggers, and success metrics (% reaching milestone 5, day-14 NPS, day-90 retention).

### Added — 1 hook + 1 script (last line of defense)

- `hooks/post-tool-aiism-check.json` — a `PostToolUse` hook with matcher `Write|Edit` that runs `scripts/check-aiisms.py` after each edit/write.
- `scripts/check-aiisms.py` — a conservative Python scanner that checks `outputs/*.md` modified in the last 60s for residual AI-ism patterns (PT-BR + EN). Detects: inflated vocabulary (`transformador`, `revolucionário`, `alavancar`), assistant voice (`great question`, `hope this helps`), generic conclusions, em-dash overuse (≥3 in one paragraph), hedging. Soft warning — never blocks.

### Polish

- `README.md`: badges `commands-17`, `skills-25`, `templates-17`. Command catalog with the 2 new ones. New category "Deliverability + high-ticket closing" (2 skills).
- `CLAUDE.md`: roadmap [0.4.0] moves out of planned. New distant roadmap [0.5.0+] focuses on multi-client, customization via settings.json, output export.

## [0.3.0] — 2026-05-20

### Added — 4 skills (acquisition + advanced conversion)

- `productization` — the transition across formats (1:1 → group → cohort → self-paced → SaaS). A quantitative gate between each transition, pricing adjustment per format, and signals of packaging too early or too late.
- `content-engine` — an engine for consistent organic content. A healthy mix (60% educational / 25% entertainment / 15% promo), sustainable vs. aspirational cadence, metrics by month (3–6 month lag to first lead), a repurpose plan (1 piece → 4–8 derivatives).
- `ad-creative-testing` — a statistical testing framework. A test matrix (change 1 element at a time), minimum sample size ($150–1,000 per variant), objective kill criteria (≥1,000 impressions + CTR < 50% of the best), a 90-day test roadmap.
- `sales-sequencing` — a full outbound sequence (5-step cadence). Timing (1d/3d/7d/14d/30d), 5 rotatable angles so the copy doesn't repeat, a mandatory breakup email, and realistic B2B metrics (localize benchmarks per market).

### Added — 5 commands + 5 templates

- `/hormozi-gtm:objections` + `templates/objections-matrix.md` — an objection matrix by ICP. Each one categorized (offer/price/timing/trust), a 2-sentence reframe, a word-for-word script for the sales call, mitigation built into the offer. Top 3 with a full script you can role-play.
- `/hormozi-gtm:case-study` + `templates/case-study.md` — a case study with an auditable before/after in numbers, the client's exact quote, a named mechanism. Generates a full version + 1-paragraph + 1-line + quote card.
- `/hormozi-gtm:webinar` + `templates/webinar-agenda.md` — a B2B structure, 30–45 min across 7 blocks (open + diagnosis + mechanism + cases + offer + Q&A + CTA). Different from a direct-response VSL. Includes plant questions / scripted Q&A for prerecorded.
- `/hormozi-gtm:positioning` + `templates/positioning-map.md` — a competitive teardown of 3–5 competitors, defensible axes of differentiation, a testable positioning statement. Generates hero copy (3 variations) + cold subject lines (3) + a LinkedIn bio + a sales-call opener.
- `/hormozi-gtm:content-hub` + `templates/content-roadmap.md` — a 30–90 day organic content roadmap. Topic × format × funnel stage × CTA. A weekly calendar + repurpose plan + metrics by month.

### Changed — 5 structural gaps closed

- `agents/hormozi-persona.md` gained:
  - A "Validation before hand-off (output tests)" section — an explicit checklist for every specialist output. The orchestrator returns a weak brief instead of improvising.
  - An "End-to-end pipeline example" — the full path for `/hormozi-gtm:lp` (request → persona → offer-architect → ad-architect → humanizer → output), 10 steps documented.
  - "Recovery / fallback" — what to do when `gtm-context.md` is incomplete, `audit_ref` is broken, the brief is weak, the humanizer rejects, or saving fails.
- `agents/{pricing-strategist,leads-strategist,ad-architect}.md` gained an "Operating modes" section (lite vs. full) — before, only the humanizer made that distinction.
- `agents/{offer-architect,ad-architect,pricing-strategist,leads-strategist,money-model-architect}.md` gained a "Recovery / fallback" section — explicit behavior when required input is incomplete.
- `commands/review.md` + `templates/review.md` gained a **Re-review mode**: detects a prior version, asks interactively between "delta only" vs. "full review," and the template gains a "Review history" section with a state table (resolved / in progress / regressed / new).

### Polish

- `README.md`: badges updated (`commands-15`, `skills-23`, `templates-15`), command catalog extended with the 5 new ones, skill catalog with a new "Acquisition + Conversion (advanced)" category.
- `CLAUDE.md`: "Roadmap" section updated (v0.3.0 moves out of planned, leaving only [0.4.0+] as the distant roadmap).

## [0.2.0] — 2026-05-20

### Added

**3 new skills (strategy / invisible prerequisites):**
- `niche-selection` — 5 vectors of niche quality (pain, purchasing power, saturation, TAM, access) + a reversible 4-step drilling process + common traps.
- `founder-market-fit` — 3 types of fit (native expert, customer-turned-coach, researcher-learner) + which niche fits each + how to build fit when you don't have it.
- `market-saturation-pivot` — 4 quantitative signals of saturation + a pivot gate (3+ simultaneous signals) + 4 types of pivot + a framework for pivoting in place without losing your audience.

**2 new commands:**
- `/hormozi-gtm:help` — an interactive 3-question decision matrix that recommends a command by objective. Solves onboarding for a new client.
- `/hormozi-gtm:email` — an email sequence (cold/warm/nurture/re-engagement) of 5–7 emails with timing, optional breakup email, humanizer full mode.

**1 new template:**
- `templates/email-sequence.md` — rich frontmatter + structure by sequence type + metrics and an iteration criterion.

### Changed (prompt refinement)

- `agents/pricing-strategist.md`, `agents/ad-architect.md`: `maxTurns` now 20 (was 15 and 25 respectively).
- 5 specialists (`offer`, `ad`, `pricing`, `leads`, `money-model`): `tools: Read` + `disallowedTools: Write, Edit` — only the orchestrator writes to disk.
- `skills/humanizer-rules/SKILL.md`: new section "Authentic Hormozi voice vs. AI simulacra" — distinguishes patterns to keep (direct imperative with proof, rule of three with real entities, strong words with adjacent proof) from patterns to cut (false authority with no number, generalization with no real client, generic heroic conclusion).

### Changed (refinement of 6 existing skills)

- `skills/ad-copy-formula/SKILL.md`: added a "Regional variations" section with a swap table and an example B2B SaaS cold email (localize phrasing per market).
- `skills/pricing-playbook/SKILL.md`: a "Tiering by product category" table with 8 categories (course/SaaS/service/mastermind/enterprise) and typical price points + an explanation of the Platinum decoy function + signals of wrong tiering.
- `skills/leila-scaling/SKILL.md`: an "Operationalization — primary metric per framework" section with 5 measurable metrics + primary metrics by function (Sales/CS/Ops/Founder/Engineering).
- `skills/money-models/SKILL.md`: an "Pre-launch validation order" section — 5 sequential steps (Core → Upsell pre-validation → Upsell launched → Continuity → Downsell) with a quantitative gate between each.
- `skills/bonus-stacking/SKILL.md`: a "Naming psychology" section with 8 trigger words (System/Vault/Accelerator/Toolkit/Framework/Playbook/Blueprint/Masterclass) + a before/after table.
- `skills/scarcity-urgency/SKILL.md`: a "Communicating scarcity without sounding desperate" section + 4 communication templates by category (cohort, capacity, bonus window, scheduled price increase).

### Changed (command UX)

- 8 existing commands: standardized `argument-hint`. Shared flags: `--product=<slug>`, `--ref=<path>`, `--focus=<section>`, `--full-rewrite`, `--no-humanize`. Documented in `CLAUDE.md`, "Argument convention" section.
- 5 commands that produce external output (`lp`, `script`, `hooks`, `pricing`, `plan`): a preview block "✅ Saved to … 📋 Preview … 👉 Next steps" — the user doesn't have to open the file to see what came out.
- `/hormozi-gtm:lp`, `/hormozi-gtm:script`: the soft warning for a missing audit becomes an interactive question with 3 options (run audit inline / proceed anyway / cancel).

### Changed (template UX)

- Standardized placeholders across the 9 templates + 1 new: `{{company_slug}}` (instead of `{{slug}}`), `{{product_slug}}` (instead of hyphenated `{{product-slug}}`). Documented in `skills/output-conventions/SKILL.md`, new "Placeholder convention" section.
- `templates/lp.md`, `templates/vsl.md`, `templates/pricing-review.md`: `parent_version: {{prior_version_path_or_null}}` field added to the frontmatter.
- `templates/gtm-context.md`: fields `company: {{company}}` / `slug: {{slug}}` renamed to `company_name: {{company_name}}` / `company_slug: {{company_slug}}` (consistency with outputs).

### Polish

- `README.md`: badges now include `agents-7`, `templates-10`, with updated counts (`skills-19`, `commands-10`).
- `CLAUDE.md`: new "Roadmap" section listing [0.3.0], [0.4.0+], "Not planned".

## [0.1.3] — 2026-05-20

### Fixed (Critical prompt issues — Deep Review)
- **3 specialists reassert the Hormozi persona.** `pricing-strategist`, `leads-strategist`, and `money-model-architect` now open with "You are Alex Hormozi. Right now you're solving X. You keep every rule in `hormozi-persona`." — before, they described applying the persona instead of assuming it, with a drift risk toward assistant voice.
- **5 specialists document boundaries.** Each one (`offer-architect`, `ad-architect`, `pricing-strategist`, `leads-strategist`, `money-model-architect`) gained a `## What you do NOT do` section listing the other 4 territories. Prevents turf invasion between agents.
- **5 specialists have a structured hand-off contract.** Each declares in Markdown the exact output format it returns to the orchestrator or the next agent (Value Equation scores, pricing tiers, money model math, lead gen roadmap, copy structure). Ends the ambiguity about what each agent produces.
- **The humanizer no longer mutilates a legitimate rule of three.** `agents/humanizer.md` and `skills/humanizer-rules/SKILL.md` now distinguish a vague/decorative rule of three ("fast, simple, and effective") from a specific one ("3 weeks, 3 emails, 3 cases"). Rule: if each item carries real information, keep it.
- **`offer-architect` and `ad-architect` gained few-shot examples.** Before/after of an offer rewrite (flabby vs. punchy), a Value Equation diagnosis (bad vs. good), a hook (bad vs. good), a CTA (bad vs. good). Reduces drift in long prompts.

## [0.1.2] — 2026-05-20

### Fixed (Critical)
- `hooks/session-start.json`: `type` changed from `prompt` (unsupported) to `command` — the plugin banner now actually appears in the session.
- `commands/pricing.md` + `templates/pricing-review.md`: humanizer corrected from `lite` to `full` (pricing is external output delivered to the client).
- `commands/plan.md`: output path simplified to `plan-{slug}-{YYYYMMDD}-v{n}.md`, aligned with `output-conventions`. The `type` discriminator stays in the frontmatter.
- `.github/workflows/validate-manifest.yml`: tautological logic fixed — it now requires a `[X.Y.Z]` section in the CHANGELOG when bumping the version.
- 8 `templates/*.md`: `plugin_version` now uses the dynamic placeholder `{{plugin_version}}` read from `plugin.json`. Ends hardcoded version drift.

### Changed (Important)
- `.github/workflows/release.yml`: validates `plugin.json.version`, `marketplace.metadata.version`, and `marketplace.plugins[0].version` simultaneously against the tag.
- `.github/workflows/lint-hook.yml`: now rejects an invalid `type` per event (defense against a regression of the hook bug).
- `.github/workflows/{validate-manifest,validate-skills,lint-hook}.yml`: `workflow_dispatch` added to allow manual runs.
- `templates/plan.md`: `slug` renamed to `product` (aligns with the `output-conventions` contract); added `audit_ref` and `pricing_ref`.
- `templates/review.md`: `frameworks_aplicados` renamed to `frameworks`; added `product`.
- `templates/hooks-batch.md`: added `audit_ref` (load-bearing for traceability).
- `commands/review.md`: now delegates to the corresponding specialist (`offer-architect` / `ad-architect` / `pricing-strategist`) by `material_tipo`.
- `commands/lp.md`, `script.md`, `hooks.md`: now read `external audience` and `tone intensity` from `gtm-context.md`.
- `CLAUDE.md`: the "Publish a new version" flow updated for the marketplace integrated into the repo itself.

### Changed (Minor)
- `README.md`: clone via HTTPS instead of SSH.
- `agents/humanizer.md`: adds `tools: Read` for consistency with the other agents' convention.
- `agents/hormozi-persona.md`: documents delegation to `money-model-architect` and `leads-strategist`.
- `commands/lp.md`: disambiguates "main agent" → `hormozi-persona` (orchestrator).
- `.claude-plugin/plugin.json`: removed the `categories` field (non-canonical; it emitted a warning in `claude plugin validate`).
- `skills/output-conventions/SKILL.md`: documents the `{{plugin_version}}` placeholder and the `gtm-context.md` exception.

## [0.1.1] — 2026-05-20

### Added
- `.claude-plugin/marketplace.json` in the repo itself (`source: "./"`) — the client installs via `/plugin marketplace add henriquecaner/hormozi-gtm` + `/plugin install hormozi-gtm@hormozi-gtm-marketplace`, with no need for a separate repo.

### Changed
- Contact email updated to `caner@thelevel.com.br` in `plugin.json`, `LICENSE`, and the `mailto` references in the README.

## [0.1.0] — 2026-05-19

### Added
- Initial plugin structure (`plugin.json`, README, LICENSE)
- 7 subagents: `hormozi-persona`, `offer-architect`, `ad-architect`, `pricing-strategist`, `leads-strategist`, `money-model-architect`, `humanizer`
- 16 skills covering the core frameworks (Grand Slam Offer, Value Equation, Core Four, Money Models, LTV:CAC, Pricing Playbook, Leila Scaling, Hook Framework, Bonus Stacking, Scarcity/Urgency, Lead Magnets, VSL 7-step, Guarantees, Ad Copy Formula, Humanizer Rules, Output Conventions)
- 8 commands: `/init`, `/audit`, `/lp`, `/script`, `/plan`, `/review`, `/hooks`, `/pricing`
- 9 output templates
- An informative SessionStart hook
- A reference corpus with short attributed excerpts (fair-use)
