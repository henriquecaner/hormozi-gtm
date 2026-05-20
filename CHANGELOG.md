# Changelog

Todas as mudanças relevantes deste plugin ficam aqui. Formato baseado em [Keep a Changelog](https://keepachangelog.com/), versionamento [SemVer](https://semver.org/).

## [Unreleased]

### Planejado
- Onboarding doc específico para clientes da LEVEL
- Comando `/hormozi-gtm:help` com matriz de decisão
- Hook PostToolUse opcional para flagrar AI-isms residuais

## [0.1.2] — 2026-05-20

### Corrigido (Critical)
- `hooks/session-start.json`: `type` mudado de `prompt` (não suportado) para `command` — banner do plugin agora aparece de fato na sessão.
- `commands/pricing.md` + `templates/pricing-review.md`: humanizer corrigido de `lite` para `full` (pricing é output externo entregue ao cliente).
- `commands/plano.md`: path do output simplificado para `plano-{slug}-{YYYYMMDD}-v{n}.md`, alinhado a `output-conventions`. Discriminador `tipo` fica no frontmatter.
- `.github/workflows/validate-manifest.yml`: lógica tautológica corrigida — agora exige seção `[X.Y.Z]` no CHANGELOG ao bumpar versão.
- 8 `templates/*.md`: `plugin_version` agora usa placeholder dinâmico `{{plugin_version}}` lido de `plugin.json`. Acaba o drift de versão hardcoded.

### Modificado (Important)
- `.github/workflows/release.yml`: valida `plugin.json.version`, `marketplace.metadata.version` e `marketplace.plugins[0].version` simultaneamente contra a tag.
- `.github/workflows/lint-hook.yml`: agora rejeita `type` inválido por evento (defesa contra regressão do hook bug).
- `.github/workflows/{validate-manifest,validate-skills,lint-hook}.yml`: `workflow_dispatch` adicionado para permitir execução manual.
- `templates/plano.md`: `slug` renomeado para `product` (alinha com contrato `output-conventions`); adicionados `audit_ref` e `pricing_ref`.
- `templates/review.md`: `frameworks_aplicados` renomeado para `frameworks`; adicionado `product`.
- `templates/hooks-batch.md`: adicionado `audit_ref` (load-bearing para rastreabilidade).
- `commands/review.md`: agora delegate a especialista correspondente (`offer-architect` / `ad-architect` / `pricing-strategist`) por `material_tipo`.
- `commands/lp.md`, `roteiro.md`, `hooks.md`: passam a ler `audience externa` e `intensidade do tom` do `gtm-context.md`.
- `CLAUDE.md`: fluxo "Publicar nova versão" atualizado para o marketplace integrado no próprio repo.

### Modificado (Minor)
- `README.md`: clone via HTTPS em vez de SSH.
- `agents/humanizer.md`: adiciona `tools: Read` para coerência com convenção dos demais agents.
- `agents/hormozi-persona.md`: documenta delegação a `money-model-architect` e `leads-strategist`.
- `commands/lp.md`: desambigua "agent principal" → `hormozi-persona` (orquestrador).
- `.claude-plugin/plugin.json`: removido campo `categories` (não-canonical; emitia warning no `claude plugin validate`).
- `skills/output-conventions/SKILL.md`: documenta placeholder `{{plugin_version}}` e exceção do `gtm-context.md`.

## [0.1.1] — 2026-05-20

### Adicionado
- `.claude-plugin/marketplace.json` no próprio repo (`source: "./"`) — cliente instala via `/plugin marketplace add henriquecaner/hormozi-gtm` + `/plugin install hormozi-gtm@hormozi-gtm-marketplace`, sem precisar de repo separado.

### Modificado
- Email de contato atualizado para `caner@thelevel.com.br` em `plugin.json`, `LICENSE` e referências `mailto` no README.

## [0.1.0] — 2026-05-19

### Adicionado
- Estrutura inicial do plugin (`plugin.json`, README, LICENSE)
- 7 subagents: `hormozi-persona`, `offer-architect`, `ad-architect`, `pricing-strategist`, `leads-strategist`, `money-model-architect`, `humanizer`
- 16 skills cobrindo os frameworks centrais (Grand Slam Offer, Value Equation, Core Four, Money Models, LTV:CAC, Pricing Playbook, Leila Scaling, Hook Framework, Bonus Stacking, Scarcity/Urgency, Lead Magnets, VSL 7-step, Guarantees, Ad Copy Formula, Humanizer Rules, Output Conventions)
- 8 comandos: `/init`, `/audit`, `/lp`, `/roteiro`, `/plano`, `/review`, `/hooks`, `/pricing`
- 9 templates de output
- SessionStart hook informativo
- Reference corpus com excertos curtos atribuídos (fair-use)
