# Changelog

Todas as mudanças relevantes deste plugin ficam aqui. Formato baseado em [Keep a Changelog](https://keepachangelog.com/), versionamento [SemVer](https://semver.org/).

## [Unreleased]

### Planejado
- Onboarding doc específico para clientes da LEVEL
- Comando `/hormozi-gtm:help` com matriz de decisão
- Hook PostToolUse opcional para flagrar AI-isms residuais

## [0.4.1] — 2026-05-20

### Corrigido (Critical)

- `release.yml` e `scripts/build-zip.sh` agora incluem `scripts/` no ZIP empacotado. v0.4.0 introduziu hook `post-tool-aiism-check.json` que depende de `scripts/check-aiisms.py`, mas o script não estava no ZIP — hook quebrava silenciosamente em instalações via Cowork (upload ZIP). Cliente instalando via `/plugin marketplace add` no Claude Code não era afetado (clona repo completo).

## [0.4.0] — 2026-05-20

Foco em **retenção + fechamento high-ticket + defesa final contra AI-isms**. Fecha o ciclo completo de aquisição→fechamento→onboarding→retenção. Plugin agora cobre o pós-venda, não só o pré-venda.

### Adicionado — 2 skills (deliverability + fechamento)

- `email-deliverability` — camada técnica abaixo de `/email`. Warm-up de domínio em 4-6 semanas, setup SPF/DKIM/DMARC, 3 domínios secundários estratégia, antispam triggers (palavras + comportamento), métricas que importam (inbox placement, bounce, complaint rate), plano de recovery se domínio queimou.
- `proposal-architecture` — pricing proposal high-ticket (R$ 30k+) em 7 seções (problema reformulado → mechanism → escopo → prova → investimento → garantia → próximo passo) + 5 padrões anti-comoditização (tier visível, bonus stack ímpar, garantia condicional, comparação com alternativas reais, escassez genuína).

### Adicionado — 2 commands novos + 2 templates

- `/hormozi-gtm:churn-prevention` + `templates/churn-analysis.md` — diagnóstico de churn por tipo (precoce/médio/tardio/voluntário/passivo), categorização por motivo, win/loss interview script (8 perguntas), 4-block retention playbook, sequência winback opcional (`--foco=winback`), impacto financeiro projetado.
- `/hormozi-gtm:onboarding-cliente` + `templates/client-onboarding.md` — jornada de primeiros 30 dias em 5 marcos (welcome → kickoff → quick win D7 → NPS D14 → mid-point D21 → wrap D30), cadência de touches por ticket, triggers de intervenção quantitativos, métricas de sucesso (% completa marco 5, NPS dia-14, day-90 retention).

### Adicionado — 1 hook + 1 script (defesa final)

- `hooks/post-tool-aiism-check.json` — hook `PostToolUse` matcher `Write|Edit` que dispara `scripts/check-aiisms.py` após cada edição/escrita.
- `scripts/check-aiisms.py` — Python conservador que escaneia `outputs/*.md` modificados há < 60s buscando padrões AI-isms residuais (PT-BR + EN). Detecta: vocabulário inflado (`transformador`, `revolucionário`, `alavancar`), voz de assistente (`ótima pergunta`, `espero ter ajudado`), conclusões genéricas, em-dash overuse (≥ 3 em 1 parágrafo), hedging. Soft warning — nunca bloqueia.

### Polimento

- `README.md`: badges `commands-17`, `skills-25`, `templates-17`. Catálogo de commands com 2 novos. Nova categoria "Deliverability + Fechamento high-ticket" (2 skills).
- `CLAUDE.md`: roadmap [0.4.0] sai de planejado. Novo roadmap distante [0.5.0+] foca em multi-cliente, customization via settings.json, export de outputs.

## [0.3.0] — 2026-05-20

### Adicionado — 4 skills (aquisição + conversão avançada)

- `productization` — transição entre formatos (1:1 → group → cohort → self-paced → SaaS). Gate quantitativo entre cada transição, pricing adjustment por formato, sinais de empacotar cedo demais ou tarde demais.
- `content-engine` — engine de conteúdo orgânico consistente. Mix saudável (60% educ / 25% entertainment / 15% promo), cadência sustentável vs aspiracional, métricas por mês (lag 3-6 meses até primeiro lead), repurpose plan (1 conteúdo → 4-8 derivados).
- `ad-creative-testing` — framework de teste estatístico. Matrix (muda 1 elemento por vez), sample size mínimo (R$ 150-1000 por variante), kill criteria objetivo (≥ 1000 impressions + CTR < 50% do best), roadmap de teste 90 dias.
- `sales-sequencing` — sequência outbound completa (5-step cadence). Timing (1d/3d/7d/14d/30d), 5 ângulos rotacionáveis para não repetir copy, breakup email obrigatório, métricas realistas B2B BR.

### Adicionado — 5 commands + 5 templates

- `/hormozi-gtm:objections` + `templates/objections-matrix.md` — matriz de objeções por ICP. Cada uma categorizada (oferta/preço/timing/trust), reframe em 2 frases, script palavra-por-palavra pra sales call, mitigação na oferta. Top 3 com script completo treinável em role-play.
- `/hormozi-gtm:case-study` + `templates/case-study.md` — case study com antes/depois numérico auditable, quote exato do cliente, mecanismo nomeado. Gera versão completa + 1-parágrafo + 1-linha + quote card.
- `/hormozi-gtm:webinar` + `templates/webinar-agenda.md` — estrutura B2B 30-45min em 7 blocos (abertura + diagnóstico + mechanism + cases + oferta + Q&A + CTA). Diferente de VSL direct-response. Inclui plant questions / scripted Q&A para prerecorded.
- `/hormozi-gtm:positioning` + `templates/positioning-map.md` — competitive teardown com 3-5 competidores, eixos de diferenciação defensáveis, positioning statement testável. Gera hero copy (3 variações) + cold subject (3) + LinkedIn bio + abertura de sales call.
- `/hormozi-gtm:content-hub` + `templates/content-roadmap.md` — roadmap 30-90 dias de conteúdo orgânico. Tópico × formato × funnel stage × CTA. Calendar semanal + repurpose plan + métricas por mês.

### Modificado — 5 lacunas estruturais fechadas

- `agents/hormozi-persona.md` ganhou:
  - Seção "Validação antes do hand-off (testes de saída)" — checklist explícito para cada saída de especialista. Orquestrador devolve briefing fraco em vez de improvisar.
  - "Exemplo end-to-end de pipeline" — caminho completo de `/hormozi-gtm:lp` (request → persona → offer-architect → ad-architect → humanizer → output), 10 passos documentados.
  - "Recovery / fallback" — o que fazer quando `gtm-context.md` incompleto, `audit_ref` quebrado, briefing fraco, humanizer rejeita, salvamento falha.
- `agents/{pricing-strategist,leads-strategist,ad-architect}.md` ganharam seção "Modos de operação" (lite vs full) — antes só humanizer diferenciava.
- `agents/{offer-architect,ad-architect,pricing-strategist,leads-strategist,money-model-architect}.md` ganharam seção "Recovery / fallback" — comportamento explícito quando input necessário está incompleto.
- `commands/review.md` + `templates/review.md` ganharam **modo Re-review**: detecta versão anterior, pergunta interativa entre "delta apenas" vs "review completa", template ganha seção "Histórico de reviews" com tabela de estado (resolvido / em progresso / piorou / novo).

### Polimento

- `README.md`: badges atualizados (`commands-15`, `skills-23`, `templates-15`), catálogo de commands estendido com os 5 novos, catálogo de skills com nova categoria "Aquisição + Conversão (avançado)".
- `CLAUDE.md`: seção "Roadmap" atualizada (v0.3.0 sai de planejado, fica só [0.4.0+] como roadmap distante).

## [0.2.0] — 2026-05-20

### Adicionado

**3 skills novas (estratégia / pré-requisitos invisíveis):**
- `niche-selection` — 5 vetores de qualidade de nicho (dor, poder de compra, saturação, TAM, acesso) + processo de drilling reversível em 4 passos + armadilhas comuns.
- `founder-market-fit` — 3 tipos de fit (native expert, customer-turned-coach, researcher-learner) + qual nicho cabe cada um + como construir fit quando você não tem.
- `market-saturation-pivot` — 4 sinais quantitativos de saturação + gate de pivot (3+ sinais simultâneos) + 4 tipos de pivot + framework de pivot in-place sem perder audience.

**2 commands novos:**
- `/hormozi-gtm:help` — matriz de decisão interativa em 3 perguntas, recomenda command por objetivo. Resolve onboarding de cliente novo.
- `/hormozi-gtm:email` — sequência email (cold/warm/nurture/re-engagement) de 5-7 emails com timing, breakup email opcional, humanizer modo full. Tunado para B2B brasileiro.

**1 template novo:**
- `templates/email-sequence.md` — frontmatter rico + estrutura por tipo de sequência + métricas e critério de iteração.

### Modificado (refinement de prompts)

- `agents/pricing-strategist.md`, `agents/ad-architect.md`: `maxTurns` agora 20 (era 15 e 25 respectivamente).
- 5 especialistas (`offer`, `ad`, `pricing`, `leads`, `money-model`): `tools: Read` + `disallowedTools: Write, Edit` — só o orquestrador escreve em disco.
- `skills/humanizer-rules/SKILL.md`: nova seção "Voz Hormozi autêntica vs AI-simulacra" — distingue padrões manter (imperativo direto com prova, rule of three com entidades reais, palavras fortes com prova adjacente) de cortar (falsa autoridade sem número, generalização sem cliente real, conclusão genérica heroica).

### Modificado (refinement de 6 skills existentes)

- `skills/ad-copy-formula/SKILL.md`: adicionada seção "Variações regionais (PT-BR)" com tabela de substituições EN→BR + exemplo cold email B2B SaaS brasileiro.
- `skills/pricing-playbook/SKILL.md`: tabela "Tiering por categoria de produto" com 8 categorias (curso/SaaS/serviço/mastermind/enterprise) e valores típicos em R$ + explicação da função decoy do Platinum + sinais de tiering errado.
- `skills/leila-scaling/SKILL.md`: seção "Operacionalização — métrica primária por framework" com 5 métricas mensuráveis + métricas primárias por função (Sales/CS/Ops/Founder/Engineering).
- `skills/money-models/SKILL.md`: seção "Ordem de validação pre-launch" — 5 passos sequenciais (Core → Upsell pre-validation → Upsell launched → Continuity → Downsell) com gate quantitativo entre cada.
- `skills/bonus-stacking/SKILL.md`: seção "Naming psychology" com 8 palavras-gatilho (Sistema/Vault/Acelerador/Toolkit/Framework/Playbook/Blueprint/Masterclass) + tabela antes/depois.
- `skills/scarcity-urgency/SKILL.md`: seção "Comunicando escassez sem soar desesperado" + 4 templates de comunicação por categoria (cohort, capacidade, bonus por window, aumento de preço programado).

### Modificado (UX dos commands)

- 8 commands existentes: `argument-hint` padronizado. Flags compartilhadas: `--produto=<slug>`, `--ref=<caminho>`, `--foco=<seção>`, `--full-rewrite`, `--no-humanize`. Documentado em `CLAUDE.md` seção "Convenção de argumentos".
- 5 commands que produzem output externo (`lp`, `roteiro`, `hooks`, `pricing`, `plano`): preview block "✅ Salvo em ... 📋 Preview ... 👉 Próximos passos" — usuário não precisa abrir o arquivo pra ver o que saiu.
- `/hormozi-gtm:lp`, `/hormozi-gtm:roteiro`: soft warning de audit ausente vira pergunta interativa com 3 opções (rodar audit inline / seguir mesmo assim / cancelar).

### Modificado (UX dos templates)

- Placeholders padronizados nos 9 templates + 1 novo: `{{empresa_slug}}` (em vez de `{{slug}}`), `{{produto_slug}}` (em vez de `{{produto-slug}}` com hífen). Documentado em `skills/output-conventions/SKILL.md` na nova seção "Convenção de placeholders".
- `templates/lp.md`, `templates/vsl.md`, `templates/pricing-review.md`: campo `parent_version: {{caminho_v_anterior_ou_null}}` adicionado ao frontmatter.
- `templates/gtm-context.md`: campos `empresa: {{empresa}}` / `slug: {{slug}}` renomeados para `empresa_nome: {{empresa_nome}}` / `empresa_slug: {{empresa_slug}}` (consistência com outputs).

### Polimento

- `README.md`: badges agora incluem `agents-7`, `templates-10`, contagens atualizadas (`skills-19`, `commands-10`).
- `CLAUDE.md`: nova seção "Roadmap" listando [0.3.0], [0.4.0+], "Não planejado".

## [0.1.3] — 2026-05-20

### Corrigido (Critical de prompts — Deep Review)
- **3 especialistas reafirmam a persona Hormozi.** `pricing-strategist`, `leads-strategist` e `money-model-architect` agora começam com "Você é Alex Hormozi. Neste momento, está resolvendo X. Mantém todas as regras de `hormozi-persona`." — antes descreviam a aplicação da persona em vez de assumi-la, com risco de drift para voz de assistente.
- **5 especialistas documentam boundaries.** Cada um (`offer-architect`, `ad-architect`, `pricing-strategist`, `leads-strategist`, `money-model-architect`) ganhou seção `## O que você NÃO faz` listando os outros 4 territórios. Evita invasão de terreno entre agents.
- **5 especialistas têm hand-off contract estruturado.** Cada um declara em Markdown o formato exato do output que devolve para o orquestrador ou para o próximo agente (Value Equation scores, pricing tiers, money model math, lead gen roadmap, copy structure). Acaba a ambiguidade sobre o que cada agent produz.
- **Humanizer não mutila mais rule-of-three legítimo.** `agents/humanizer.md` e `skills/humanizer-rules/SKILL.md` agora distinguem rule-of-three vago/decorativo ("rápido, simples e eficaz") de rule-of-three específico ("3 semanas, 3 e-mails, 3 cases"). Regra: se cada item carrega informação real, mantém.
- **`offer-architect` e `ad-architect` ganharam few-shot examples.** Antes/depois de reescrita de oferta (flácida vs punchy), diagnóstico Value Equation (ruim vs bom), hook (ruim vs bom), CTA (ruim vs bom). Reduz drift em prompts longos.

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
