# CLAUDE.md — hormozi-gtm

Este arquivo orienta Claude Code (claude.ai/code) ao trabalhar neste repo.

## O que este repo é

Plugin Claude Code da LEVEL — não é uma aplicação executável. Os "artefatos" são Markdown estruturado (slash commands, agents, skills, templates) que outras instâncias do Claude Code carregam. Não há build, lint, test runner ou pacote a instalar.

## Arquitetura

```
hormozi-gtm/
├── .claude-plugin/plugin.json      # manifest
├── commands/                       # 17 slash commands (entry points)
├── agents/                         # 7 subagents (hormozi-persona + 5 especialistas + humanizer)
├── skills/                         # 25 skills (frameworks + estratégia + utilities)
├── hooks/session-start.json        # banner informativo
├── templates/                      # skeletons que os comandos preenchem
└── reference/                      # extratos atribuídos dos livros (fair-use)
```

**Pipeline canônico de um comando:**

```
slash command (commands/<x>.md)
    └─ orquestrador: hormozi-persona (sempre)
         └─ delegate a especialista: offer-architect | ad-architect | pricing-strategist | leads-strategist | money-model-architect
              └─ skills carregadas conforme o comando lista em "Skills ativas"
         └─ último passo: subagent humanizer (lite ou full) — escreve em outputs/
```

Regras invariantes:

1. **Persona Hormozi sempre ativa** em qualquer comando `/hormozi-gtm:*`. 1ª pessoa, sem voz de assistente. Não relaxar mesmo em pergunta operacional curta. Detalhes em `agents/hormozi-persona.md`.
2. **Humanizer obrigatório** antes de salvar output externo. `lite` para outputs internos (audit, review, plano); `full` para outputs externos do cliente (lp, roteiro, hooks, pricing). Flag `--no-humanize` existe só para debug. Regras em `skills/humanizer-rules/SKILL.md` e agent em `agents/humanizer.md`.
3. **Frameworks são fonte da verdade.** Não inventar conselho de GTM fora do que está em `skills/` + `reference/`. Citar capítulo/seção do livro ao ampliar.

## Contrato `gtm-context.md`

Comandos exceto `/hormozi-gtm:init` leem `gtm-context.md` na raiz do projeto-consumidor (não deste repo). É a memória persistente de empresa/cliente: ICP, oferta, brand voice, Core Four split, stage.

- Schema canônico: `templates/gtm-context.md`.
- Se ausente, comandos disparam `/hormozi-gtm:init` automaticamente antes de prosseguir.
- Se `last_updated` >30 dias, comandos avisam "contexto stale" e sugerem `--refresh`.
- Editar fluxos de comando preservando esse contrato — quebrar a auto-detecção quebra todo o plugin.

## Convenção de outputs

Definida em `skills/output-conventions/SKILL.md`. Detalhes load-bearing:

- Caminho: `outputs/<tipo>/<tipo>-<slug>-<YYYYMMDD>-v<n>.md` no projeto-consumidor.
- Versionamento incrementa. Nunca sobrescrever sem `--overwrite`.
- Frontmatter obrigatório: `plugin`, `plugin_version`, `command`, `version`, `status`, `created`, `client`, `product`, `frameworks`, `humanizer_pass`, `humanizer_mode`.
- `humanizer_pass: false` é gate de release externo.

## Convenção de argumentos

Todos os commands seguem o padrão `--flag=valor`. Não há argumentos posicionais — evita ambiguidade entre "slug do produto" e "caminho de arquivo".

**Flags compartilhadas (mesmo significado em todos os commands):**

| Flag | Função |
|---|---|
| `--produto=<slug>` | Slug do produto (kebab-case). Lido de `gtm-context.md` se omitido, ou perguntado no chat. |
| `--ref=<caminho>` | Caminho para um output anterior (refinar / criar v2). Ex: `--ref=outputs/lp/lp-revops-20260519-v1.md`. |
| `--foco=<secao>` | Em modo refinar (`--ref`), foca em parte específica do material. Ex: `--foco=hero` na LP. |
| `--full-rewrite` | Em modo refinar (`--ref`), cria v2 do zero usando o anterior só como `parent_version`. |
| `--no-humanize` | Pula o humanizer pass (debug ou A/B test). Salva com `humanizer_pass: false`. |

**Flags específicas por command:**
- `init`: `--refresh` (reabre entrevista mantendo `gtm-context.md` como base).
- `roteiro`: `--formato=vsl|reels|shorts|tiktok`, `--batch`, `--n=N`.
- `hooks`: `--n=N`, `--angulo=dream|problem|secret|contrarian|proof`.
- `lp`: `--skip-audit` (ignora warning de audit ausente).
- `plano`: `--tipo=empresa|produto`.
- `email`: `--tipo=cold|warm|nurture|re-engagement`.

**Regra:** se está pensando em adicionar arg posicional novo, transforme em `--flag` primeiro. Evita "esse caminho é referência ou destino?" e mantém o autocomplete do Claude Code útil.

## Tarefas comuns

### Validar um comando manualmente

Não há test runner. Validação é executar o comando dentro de um projeto-consumidor real:

```bash
claude --plugin-dir .   # do diretório raiz do plugin, ou path absoluto se rodando de outro lugar
/hormozi-gtm:init
/hormozi-gtm:audit
```

### Adicionar novo comando

1. Criar `commands/<nome>.md` com frontmatter (`description`, `argument-hint`).
2. Listar persona orquestradora, especialista, skills, template, regra de humanizer.
3. Adicionar template em `templates/<nome>.md` se output novo.
4. Atualizar `skills/output-conventions/SKILL.md`.
5. Bump `version` em `.claude-plugin/plugin.json` + entrada no `CHANGELOG.md`.

### Publicar nova versão

1. Bump `version` em `.claude-plugin/plugin.json` (SemVer).
2. Bump `metadata.version` e `plugins[0].version` em `.claude-plugin/marketplace.json` (mesmo SemVer — o workflow `release.yml` valida que os três batem).
3. Atualizar `CHANGELOG.md` (mover de `[Unreleased]` para nova seção `[X.Y.Z]`).
4. Commit, push para `main`.
5. `git tag vX.Y.Z && git push origin vX.Y.Z` — dispara workflow `release.yml` (gera ZIP, cria release, extrai notes do CHANGELOG).
6. Clientes recebem via `/plugin update hormozi-gtm` (marketplace integrado no mesmo repo).

> Os templates usam `plugin_version: {{plugin_version}}` como placeholder dinâmico. Não precisa editar templates a cada bump — o command lê o valor de `.claude-plugin/plugin.json` na hora de gerar o output.

## Roadmap

> v0.1.x → v0.4.x: encerradas (ver `CHANGELOG.md` para detalhes).

### [0.5.0+] Roadmap distante (opcional)
- `settings.json` customization (cliente declara `humanizer_mode_default`, intensidade Hormozi, preferências de output).
- Multi-cliente em paralelo (gtm-context.md singular hoje — futuro: `gtm-context-{slug}.md` por cliente).
- Comando `/hormozi-gtm:export` — empacota outputs de 1 cliente num zip pra entrega.
- A/B testing automation — integração com plataformas de ads (depende de API externa).

### Não planejado (workflow manual necessário)
- CRM sync (manutenção de `gtm-context.md` manual por enquanto).

## Editando conteúdo

- **Persona** (`agents/hormozi-persona.md`): invariante de voz. Não suavizar.
- **Humanizer** (`agents/humanizer.md` + `skills/humanizer-rules/SKILL.md`): listas EN+PT-BR de AI-isms. Adicionar padrão novo nos dois arquivos.
- **Reference** (`reference/*.md`): só extratos curtos (≤10% de capítulo), com atribuição e fair-use disclaimer no topo.
- **CHANGELOG**: toda mudança em `commands/`, `agents/`, `skills/` ou `templates/` precisa entrada.
