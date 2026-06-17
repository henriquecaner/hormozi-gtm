---
name: output-conventions
description: Convenções de naming, estrutura de pasta e frontmatter dos outputs gerados pelo plugin hormozi-gtm. Use sempre antes de escrever arquivo final em outputs/ para garantir consistência, versionamento e rastreabilidade.
---

# Output Conventions

## Estrutura de pasta

Todos os outputs vão para `outputs/` na raiz do projeto consumidor:

```
outputs/
├── audit/                   # /hormozi-gtm:audit
├── lp/                      # /hormozi-gtm:lp
├── roteiro/                 # /hormozi-gtm:roteiro (vsl + short)
├── plano/                   # /hormozi-gtm:plano
├── review/                  # /hormozi-gtm:review
├── hooks/                   # /hormozi-gtm:hooks
├── pricing/                 # /hormozi-gtm:pricing
├── email/                   # /hormozi-gtm:email (cold/warm/nurture/re-engagement)
├── objections/              # /hormozi-gtm:objections
├── case-studies/            # /hormozi-gtm:case-study (plural — case studies geram série)
├── webinar/                 # /hormozi-gtm:webinar
├── positioning/             # /hormozi-gtm:positioning
├── content/                 # /hormozi-gtm:content-hub (roadmap de conteúdo)
├── retention/               # /hormozi-gtm:churn-prevention (churn-analysis + winback)
└── onboarding/              # /hormozi-gtm:onboarding-cliente
```

Se a pasta não existir, criar antes de escrever. Não escrever na raiz do projeto.

## Naming padrão

```
outputs/<tipo>/<tipo>-<slug>-<YYYYMMDD>-v<n>.md
```

**Exemplos:**
- `outputs/audit/audit-curso-fechamento-20260519-v1.md`
- `outputs/lp/lp-revops-diagnostic-20260519-v2.md`
- `outputs/roteiro/vsl-curso-fechamento-20260519-v1.md`
- `outputs/roteiro/short-curso-fechamento-20260519-v3.md`
- `outputs/plano/plano-level-gtm-20260519-v1.md`
- `outputs/review/review-lp-cliente-x-20260519.md`
- `outputs/hooks/hooks-curso-fechamento-20260519-v1.md`
- `outputs/pricing/pricing-curso-fechamento-20260519-v2.md`
- `outputs/email/email-cold-revops-diagnostic-20260519-v1.md` (sub-tipo no prefixo)
- `outputs/objections/objections-revops-diagnostic-20260519-v1.md`
- `outputs/case-studies/case-study-stark-bank-20260519-v1.md`
- `outputs/webinar/webinar-revops-diagnostic-20260519-v1.md`
- `outputs/positioning/positioning-revops-diagnostic-20260519-v1.md`
- `outputs/content/content-roadmap-revops-diagnostic-20260519-v1.md`
- `outputs/retention/churn-analysis-revops-diagnostic-20260519-v1.md`
- `outputs/retention/winback-sequence-revops-diagnostic-20260519-v1.md` (exceção — winback compartilha pasta com churn)
- `outputs/onboarding/onboarding-revops-diagnostic-20260519-v1.md`

**Regras:**
- `<slug>` é kebab-case, derivado do produto/oferta/cliente
- `<YYYYMMDD>` é data de criação ou último update major
- `<v{n}>` autoincrementa. Versão 1 não tem `-v1` ambíguo — sempre `-v1`
- Nunca sobrescrever sem flag `--overwrite`
- Reviews não têm `-v{n}` (one-shot)

## Frontmatter padrão

Todo output começa com frontmatter YAML:

```yaml
---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}   # lido de .claude-plugin/plugin.json no momento da geração
command: lp                          # init|audit|lp|roteiro|plano|review|hooks|pricing|email|objections|case-study|webinar|positioning|content-hub|churn-prevention|onboarding-cliente
version: 2                           # incrementa a cada refinement
status: draft                        # draft | approved | shipped
created: 2026-05-19T14:30:00-03:00   # ISO 8601 com TZ
client: {{empresa_slug}}              # = gtm-context.md:empresa_slug
product: {{produto_slug}}             # slug kebab-case do produto/oferta
frameworks:                          # skills usadas na produção
  - grand-slam-offer
  - value-equation
  - bonus-stacking
  - guarantees
humanizer_pass: true                 # true só em copy externa; false em output interno/diagnóstico
humanizer_mode: full                 # full (copy externa) | n/a (interno/cru)
voz: humanizada                      # humanizada (copy externa) | crua (interno/diagnóstico)
audit_ref: outputs/audit/audit-ketlin-20260518-v1.md  # se aplicável
pricing_ref: outputs/pricing/pricing-revops-20260518-v1.md  # se aplicável
parent_version: outputs/lp/lp-revops-20260519-v1.md  # quando refinement
---
```

### Campos load-bearing

- `plugin_version` → ao preencher o template, ler `.claude-plugin/plugin.json` e substituir `{{plugin_version}}` pelo valor real (ex: `0.1.2`). Nunca hardcoded no template.
- `humanizer_pass: false` → bloqueia release externo (lint check). É o estado correto de todo output interno/diagnóstico (audit, review, plano, pricing, objections, positioning, análise de churn, onboarding) — esses saem `humanizer_mode: n/a` e `voz: crua`, nunca passam por humanizer. Copy externa (lp, roteiro, hooks, email, case-study, webinar, conteúdo, winback) sai `humanizer_pass: true` / `humanizer_mode: full` / `voz: humanizada`. (O modo `lite` foi descontinuado no v1.0.)
- `audit_ref` → rastreia se copy foi escrita sobre oferta auditada
- `parent_version` → árvore de refinamento
- `frameworks` → permite buscar "todos os outputs que usaram skill X"

### Exceção

- O schema do `gtm-context.md` (input persistente, não output gerado) vive na skill `template-gtm-context` — usa frontmatter mínimo (`empresa_nome`, `empresa_slug`, `last_updated`, `version`, `plugin`). Sem `command`/`humanizer_pass`.

### Convenção de placeholders

Todos os esqueletos (skills `template-*`) seguem a mesma convenção para evitar ambiguidade entre nome humano e slug técnico:

| Placeholder | Tipo | Fonte | Exemplo |
|---|---|---|---|
| `{{empresa_nome}}` | texto humano | `gtm-context.md` | "Ketlin Scalco" |
| `{{empresa_slug}}` | slug kebab-case | `gtm-context.md` | "ketlin-scalco" |
| `{{produto_nome}}` | texto humano | input do command | "RevOps Diagnostic" |
| `{{produto_slug}}` | slug kebab-case | input do command | "revops-diagnostic" |
| `{{plugin_version}}` | versão SemVer | `.claude-plugin/plugin.json` | "0.2.0" |
| `{{ISO8601}}` | timestamp | hora de geração | "2026-05-20T14:30:00-03:00" |
| `{{caminho_ou_null}}` | path ou null | input/contexto | "outputs/audit/audit-revops-20260518-v1.md" ou `null` |
| `{{caminho_v_anterior_ou_null}}` | path ou null | em refinements | path da v anterior ou `null` se v1 |

**Regra:** nunca usar `{{slug}}` sozinho (ambíguo — empresa? produto?). Sempre prefixar.

### Campos opcionais

- `tags: [b2b, saas]`
- `assignee: henrique`
- `due: 2026-05-25`
- `feedback: outputs/review/review-lp-revops-20260520.md`

## Refinement loop

Quando comando é invocado com path de arquivo existente:

1. Lê o frontmatter do arquivo
2. Carrega context (frameworks, audit_ref, etc.)
3. Aplica feedback do usuário sobre conteúdo
4. Cria novo arquivo `v{n+1}` na mesma pasta
5. Frontmatter do `v{n+1}` referencia `v{n}` em `parent_version`
6. Humanizer roda de novo
7. Comando entrega o caminho do novo arquivo

## Quando edit-in-place

Default é versioning sempre. Edit-in-place só com flag explícita `--overwrite`. Cenários:

- Fix de typo
- Update de metadata (status: draft → approved)
- Cleanup pré-shipment

Nunca usa overwrite para mudanças de conteúdo substanciais.

## .gitignore recommendation

README do plugin recomenda:

**Opção A:** ignorar outputs do versionamento

```
# .gitignore do projeto
outputs/
!outputs/.gitkeep
```

**Opção B:** versionar tudo (documento de cliente)

Sem entrada em .gitignore. Commits seguem cadência do projeto.

Cada projeto decide. README explica trade-off.

## TL;DR de cada output

Recomendado mas opcional: cada output tem seção `## TL;DR` no topo (após frontmatter) com 2-3 linhas resumindo o entregável. Ajuda quando alguém abre o arquivo 3 semanas depois.

## Invariante: telemetria nunca entra no arquivo

A telemetria de orquestração (plano de fases, narração de transição entre fases, marcador de modo) é **estritamente do canal de conversa**. NUNCA é serializada no arquivo de `outputs/` nem no frontmatter. O arquivo contém só o deliverable.

`--quiet` apenas silencia a conversa — não é o que protege o arquivo. O arquivo é protegido por esta regra, independente de flags. Se uma fase do comando produzir log de orquestração, esse log fica na conversa e é descartado antes de salvar.

## Anti-padrões

- Salvar output sem frontmatter
- Serializar telemetria de orquestração (plano/narração de fase) dentro do arquivo de output
- Sobrescrever sem `--overwrite` explícito
- Nomear arquivo sem incluir `v{n}`
- Salvar na raiz do projeto em vez de `outputs/<tipo>/`
- Esquecer de atualizar `parent_version` em refinement
- Marcar `humanizer_pass: true` sem ter rodado o humanizer
