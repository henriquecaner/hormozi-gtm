# Changelog

Todas as mudanças relevantes deste plugin ficam aqui. Formato baseado em [Keep a Changelog](https://keepachangelog.com/), versionamento [SemVer](https://semver.org/).

## [Unreleased]

### Planejado
- Onboarding doc específico para clientes da LEVEL
- Comando `/hormozi-gtm:help` com matriz de decisão
- Hook PostToolUse opcional para flagrar AI-isms residuais

## [0.1.0] — 2026-05-19

### Adicionado
- Estrutura inicial do plugin (`plugin.json`, README, LICENSE)
- 7 subagents: `hormozi-persona`, `offer-architect`, `ad-architect`, `pricing-strategist`, `leads-strategist`, `money-model-architect`, `humanizer`
- 16 skills cobrindo os frameworks centrais (Grand Slam Offer, Value Equation, Core Four, Money Models, LTV:CAC, Pricing Playbook, Leila Scaling, Hook Framework, Bonus Stacking, Scarcity/Urgency, Lead Magnets, VSL 7-step, Guarantees, Ad Copy Formula, Humanizer Rules, Output Conventions)
- 8 comandos: `/init`, `/audit`, `/lp`, `/roteiro`, `/plano`, `/review`, `/hooks`, `/pricing`
- 9 templates de output
- SessionStart hook informativo
- Reference corpus com excertos curtos atribuídos (fair-use)
