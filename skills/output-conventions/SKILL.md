---
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
└── pricing/                 # /hormozi-gtm:pricing
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
command: lp                          # init|audit|lp|roteiro|plano|review|hooks|pricing
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
humanizer_pass: true                 # se humanizer foi aplicado (full ou lite)
humanizer_mode: full                 # full | lite
audit_ref: outputs/audit/audit-ketlin-20260518-v1.md  # se aplicável
pricing_ref: outputs/pricing/pricing-revops-20260518-v1.md  # se aplicável
parent_version: outputs/lp/lp-revops-20260519-v1.md  # quando refinement
---
```

### Campos load-bearing

- `plugin_version` → ao preencher o template, ler `.claude-plugin/plugin.json` e substituir `{{plugin_version}}` pelo valor real (ex: `0.1.2`). Nunca hardcoded no template.
- `humanizer_pass: false` → bloqueia release externo (lint check)
- `audit_ref` → rastreia se copy foi escrita sobre oferta auditada
- `parent_version` → árvore de refinamento
- `frameworks` → permite buscar "todos os outputs que usaram skill X"

### Exceção

- `templates/gtm-context.md` é input persistente (não output gerado) — usa frontmatter mínimo (`empresa_nome`, `empresa_slug`, `last_updated`, `version`, `plugin`). Sem `command`/`humanizer_pass`.

### Convenção de placeholders

Todos os templates seguem a mesma convenção para evitar ambiguidade entre nome humano e slug técnico:

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

## Anti-padrões

- Salvar output sem frontmatter
- Sobrescrever sem `--overwrite` explícito
- Nomear arquivo sem incluir `v{n}`
- Salvar na raiz do projeto em vez de `outputs/<tipo>/`
- Esquecer de atualizar `parent_version` em refinement
- Marcar `humanizer_pass: true` sem ter rodado o humanizer
