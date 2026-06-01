<div align="center">

<a href="https://github.com/henriquecaner/hormozi-gtm">
  <img src=".github/assets/hero.png" alt="Hormozi GTM — LEVEL Edition · 17 comandos · voz Hormozi brutal · persona sempre ativa" width="100%"/>
</a>

# Hormozi GTM — LEVEL Edition

**Operação GTM no estilo Alex Hormozi para o time e clientes da LEVEL.**

Plugin Claude Code com 17 comandos, 42 skills (frameworks Hormozi + registro de voz + esqueletos de output), 7 subagents especializados e contrato `gtm-context.md` que persiste entre sessões. Persona Hormozi sempre ativa, voz brutal calibrada por rubrica. Humanizer só em copy externa.

[![License](https://img.shields.io/badge/license-proprietary-blue)](./LICENSE)
[![Latest Release](https://img.shields.io/github/v/release/henriquecaner/hormozi-gtm?color=green&label=release)](https://github.com/henriquecaner/hormozi-gtm/releases/latest)
[![Commands](https://img.shields.io/badge/commands-17-purple)](#cat%C3%A1logo-de-comandos)
[![Skills](https://img.shields.io/badge/skills-42-purple)](#cat%C3%A1logo-de-skills)
[![Agents](https://img.shields.io/badge/agents-7-blueviolet)](#pipeline-de-agents)
[![Hooks](https://img.shields.io/badge/hooks-2-orange)](#hooks)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-D97757)](https://docs.claude.com/en/docs/claude-code)
[![Claude Cowork](https://img.shields.io/badge/Claude%20Cowork-ready-D97757)](#instala%C3%A7%C3%A3o)

[Quickstart](#quickstart) · [Comandos](#cat%C3%A1logo-de-comandos) · [Skills](#cat%C3%A1logo-de-skills) · [Pipeline](#pipeline-de-agents) · [Hooks](#hooks) · [Instalação](#instala%C3%A7%C3%A3o) · [Autor](#autor)

</div>

---

## O que é

Consultoria GTM gasta tempo demais reexplicando o mesmo contexto a cada sessão de IA. ICP, oferta, brand voice, posicionamento, Core Four split. Você descreve tudo na segunda, perde os detalhes na quinta, redescreve na semana seguinte. Cada artefato sai com tom levemente diferente do anterior. O cliente percebe a inconsistência antes de você.

A segunda dor é mais cara: copy gerada por IA é reconhecível em segundos. Em-dash em excesso, listas de três, "stands as a testament", "navegando os desafios". Quando uma LP ou hook de ad chega assim para o cliente, a credibilidade do projeto vai junto.

**Hormozi GTM** resolve as duas em paralelo. `/hormozi-gtm:init` faz uma entrevista guiada e grava `gtm-context.md` na raiz do projeto; todo comando subsequente lê esse arquivo automaticamente, então você não reintroduz nada. Todo output destinado ao cliente (LP, roteiro VSL, hook, ad, email, proposta) passa por um agent humanizer com listas EN e PT-BR de padrões AI antes de ser salvo, e `humanizer_pass: true` no frontmatter é gate de release. A persona Alex Hormozi fica em 1ª pessoa nos 17 comandos, sem "ótima pergunta" ou "espero ter ajudado", com um pipeline de 7 agents endurecido contra drift de voz e invasão de territórios entre especialistas.

Cobertura: aquisição (cold/warm/orgânico/pago), conversão (LP/VSL/hook/objections), fechamento high-ticket (proposta R$ 30k+), entrega (onboarding 30d), retenção (churn analysis + winback). Frameworks dos 4 livros Hormozi mais o playbook vazado, com camada estratégica nova (niche-selection, founder-market-fit, market-saturation-pivot) que normalmente fica fora de plugins GTM.

## Quickstart

### Caso 1 — Cliente novo, do zero

```bash
/plugin marketplace add henriquecaner/hormozi-gtm
/plugin install hormozi-gtm@hormozi-gtm-marketplace
/hormozi-gtm:init                                       # entrevista 8 perguntas → gtm-context.md
/hormozi-gtm:audit                                      # diagnóstico Value Equation
/hormozi-gtm:lp --produto="nome-do-produto"             # LP de vendas com humanizer full
```

### Caso 2 — Não sabe por onde começar

```bash
/hormozi-gtm:help                                       # matriz de decisão em 3 perguntas
```

### Caso 3 — Tem oferta validada, precisa de leads

```bash
/hormozi-gtm:plano                                      # Core Four split + money model 90d
/hormozi-gtm:email --tipo=cold                          # sequência de 5-7 touches
/hormozi-gtm:hooks --n=12                               # variantes para A/B testing em ad
```

Mais cenários em `/hormozi-gtm:help`.

## Catálogo de comandos

17 comandos organizados pelo estágio do funil GTM:

### Onboarding e diagnóstico

| Comando | Função | Output |
|---|---|---|
| `/hormozi-gtm:init` | Cria `gtm-context.md` via entrevista guiada | `gtm-context.md` |
| `/hormozi-gtm:help` | Matriz de decisão — recomenda command por objetivo | (sem output) |
| `/hormozi-gtm:audit` | Diagnóstico via Value Equation (gargalo crítico + top 3 alavancas) | `outputs/audit/` |

### Copy externa

| Comando | Função | Output |
|---|---|---|
| `/hormozi-gtm:lp` | Landing page (Grand Slam Offer + 10 seções estruturadas) | `outputs/lp/` |
| `/hormozi-gtm:roteiro` | VSL longo 7-step ou short-form para Reels/Shorts/TikTok | `outputs/roteiro/` |
| `/hormozi-gtm:hooks` | Bateria de 8-12 variantes para A/B em ad | `outputs/hooks/` |

### Aquisição e fechamento

| Comando | Função | Output |
|---|---|---|
| `/hormozi-gtm:email` | Sequência cold/warm/nurture/re-engagement (5-7 touches) | `outputs/email/` |
| `/hormozi-gtm:objections` | Matriz de objeções por ICP + scripts para sales call | `outputs/objections/` |
| `/hormozi-gtm:case-study` | Case study antes/depois + assets derivados | `outputs/case-studies/` |
| `/hormozi-gtm:webinar` | Estrutura B2B 30-45min (educacional + venda) | `outputs/webinar/` |
| `/hormozi-gtm:positioning` | Competitive teardown + positioning statement | `outputs/positioning/` |

### Pricing e business model

| Comando | Função | Output |
|---|---|---|
| `/hormozi-gtm:pricing` | Revisão contra 5 leis do Pricing Playbook (range + tiering) | `outputs/pricing/` |
| `/hormozi-gtm:plano` | Plano GTM 90 dias (Core Four + Money Model 4 níveis) | `outputs/plano/` |

### Entrega, retenção e conteúdo

| Comando | Função | Output |
|---|---|---|
| `/hormozi-gtm:onboarding-cliente` | Primeiros 30 dias pós-venda (5 marcos + triggers) | `outputs/onboarding/` |
| `/hormozi-gtm:churn-prevention` | Win/loss + churn analysis + retention playbook (+ winback opcional) | `outputs/retention/` |
| `/hormozi-gtm:content-hub` | Roadmap 30-90 dias de conteúdo orgânico | `outputs/content/` |

### Refinement

| Comando | Função | Output |
|---|---|---|
| `/hormozi-gtm:review` | Feedback brutal + modo Re-review (delta v1↔v2) | nova versão `v{n+1}` |

**Convenção de argumentos:** todos os commands usam `--flag=valor`. Compartilhadas: `--produto=<slug>`, `--ref=<caminho>` (refinar), `--foco=<seção>`, `--full-rewrite`, `--no-humanize`. Detalhes em [`CLAUDE.md`](./CLAUDE.md).

## Catálogo de skills

**Frameworks Hormozi** (6)
`grand-slam-offer` · `value-equation` · `money-models` · `ltv-cac` · `core-four` · `leila-scaling`

**Estratégia (pré-requisitos invisíveis)** (3)
`niche-selection` · `founder-market-fit` · `market-saturation-pivot`

**Copy + Ads** (7)
`hook-framework` · `vsl-7-step` · `ad-copy-formula` · `scarcity-urgency` · `guarantees` · `bonus-stacking` · `lead-magnets`

**Aquisição + Conversão avançada** (4)
`content-engine` · `ad-creative-testing` · `sales-sequencing` · `productization`

**Deliverability + Fechamento high-ticket** (2)
`email-deliverability` · `proposal-architecture`

**Pricing** (1)
`pricing-playbook`

**Operacional + voz** (3)
`output-conventions` · `humanizer-rules` · `hormozi-voice` (registro de voz brutal + rubrica de brutalidade 0-10)

**Esqueletos de output** (16) — internos, carregados pelo comando via ferramenta Skill (confiável no CLI e no Cowork)
`template-gtm-context` · `template-lp` · `template-vsl` · `template-ad-short` · `template-hooks-batch` · `template-email-sequence` · `template-case-study` · `template-webinar-agenda` · `template-content-roadmap` · `template-churn-analysis` · `template-review` · `template-plano` · `template-pricing-review` · `template-objections-matrix` · `template-positioning-map` · `template-client-onboarding`

Skills carregam só quando o comando declara em `Skills ativas`. `output-conventions` e `humanizer-rules` rodam em todo output externo.

## Pipeline de agents

O plugin opera como pipeline de 7 agents com hand-off contracts estruturados, não como coleção de prompts soltos. Toda invocação de comando segue:

```
slash command
    ↓
hormozi-persona (orquestrador — sempre)
    ↓
especialista delegado (por domínio)
    ↓
humanizer (modo lite ou full antes de salvar)
    ↓
outputs/<tipo>/<arquivo>.md
```

### Os 7 agents

| Agent | Papel | Quando entra |
|---|---|---|
| `hormozi-persona` | Orquestrador. Voz Hormozi invariante 1ª pessoa. Valida saída de cada especialista antes do hand-off. | Sempre — entry point de todo comando |
| `offer-architect` | Diagnostica oferta via Value Equation, propõe top 3 alavancas, reescreve em 1 parágrafo | `/audit`, `/lp`, `/roteiro` |
| `ad-architect` | Escreve hooks, VSL 7-step, ad copy. Modos lite/full | `/lp`, `/roteiro`, `/hooks`, `/email`, `/webinar` |
| `pricing-strategist` | Revisão contra 5 leis. Range + tiering + ancoragem | `/pricing`, `/plano` |
| `leads-strategist` | Core Four split + canal primário + roadmap | `/plano`, `/email` |
| `money-model-architect` | 4 níveis (Attraction/Core/Upsell/Continuity) + LTGP/CAC | `/plano`, `/pricing`, `/productization` |
| `humanizer` | Refina copy contra padrões AI (PT-BR + EN). Modos lite/full | Último passo de todo output externo |

### Hand-off contracts

Cada especialista declara em Markdown estruturado o formato exato do output que devolve ao orquestrador. Exemplos:

- `offer-architect` → Value Equation scores (1-10 por vetor) + gargalo crítico + top 3 alavancas com lift esperado + oferta reescrita
- `pricing-strategist` → 5 leis com score (verde/amarelo/vermelho) + range R$ X-Y + tiering Silver/Gold/Platinum + teste de validação
- `money-model-architect` → 4 níveis com pricing + matemática LTGP/CAC/payback + diagrama de funil em texto

Orquestrador valida cada hand-off antes de invocar o próximo agent. Se o output não cumpre a checklist, devolve com pergunta específica em vez de improvisar.

### Recovery / fallback

Cada agent tem comportamento documentado para input incompleto:

- `offer-architect` sem dados quantitativos → atribui score com confidence intermediário, marca campos como `(estimativa)`
- `pricing-strategist` sem unit economics → dá range conservador + avisa "estimativa de mercado, não recomendação validada"
- `humanizer` rejeita output → salva com `humanizer_pass: false` + nota, orquestrador avisa usuário

Detalhes do pipeline e exemplo end-to-end de 10 passos em [`agents/hormozi-persona.md`](./agents/hormozi-persona.md).

## Hooks

| Hook | Tipo | Função |
|---|---|---|
| `session-start.json` | SessionStart | Banner informativo ao abrir sessão — lembra que persona está ativa e humanizer é obrigatório |
| `post-tool-aiism-check.json` | PostToolUse (`Write\|Edit\|MultiEdit`) | Escaneia `outputs/*.md` recém-modificados procurando AI-isms residuais. Soft warning, nunca bloqueia. Defesa em profundidade caso humanizer falhe. |

Script de scan em `scripts/check-aiisms.py` — Python stdlib pura, detecta vocabulário inflado, voz de assistente, em-dash overuse, hedging. Cap de 20 hits por arquivo para não inundar terminal.

## Outputs

Todo comando que produz material salva em `outputs/<tipo>/<slug>-{YYYYMMDD}-v{n}.md` no projeto consumidor:

```
outputs/
├── audit/                    ├── email/                    ├── retention/
├── lp/                       ├── objections/               ├── onboarding/
├── roteiro/                  ├── case-studies/             ├── content/
├── hooks/                    ├── webinar/                  └── review/
├── pricing/                  ├── positioning/
├── plano/
```

Versionamento incrementa, nunca sobrescreve sem `--overwrite`. Frontmatter padrão: `plugin_version`, `command`, `version`, `status`, `client`, `product`, `frameworks` (skills usadas), `humanizer_pass`, `humanizer_mode`, `audit_ref`, `pricing_ref`, `parent_version`.

Convenção completa em [`skills/output-conventions/SKILL.md`](./skills/output-conventions/SKILL.md).

Recomendação: adicione `outputs/` ao `.gitignore` do projeto-consumidor, ou versione tudo dependendo do fluxo de entrega.

## Persona e humanizer

Persona Alex Hormozi ativa em todos os comandos `/hormozi-gtm:*`. 1ª pessoa, sem voz de assistente. Mesmo em pergunta operacional simples, resposta sai no tom direto da persona. Não relaxa.

Humanizer roda como último passo antes de salvar qualquer output externo. Dois modos:

- **lite** — outputs internos (audit, review, plano, churn-analysis, content-roadmap, onboarding). Remove em-dash overuse, rule of three vago, AI vocab. Mantém o tom direto cru.
- **full** — outputs externos do cliente (LP, roteiro, hooks, pricing, email, objections, case-study, webinar, positioning). Duas passadas + validação contra padrões EN e PT-BR.

Humanizer emite `humanizer_pass: <bool>` + `humanizer_mode: <lite|full>` no output. `humanizer_pass: false` é gate de release externo.

Flag `--no-humanize` existe para debug e A/B test.

Regras completas em [`skills/humanizer-rules/SKILL.md`](./skills/humanizer-rules/SKILL.md).

## Instalação

### Claude Code (CLI ou Desktop)

```bash
/plugin marketplace add henriquecaner/hormozi-gtm
/plugin install hormozi-gtm@hormozi-gtm-marketplace
```

### Claude Cowork (Desktop app)

Baixe o ZIP do release mais recente em [github.com/henriquecaner/hormozi-gtm/releases/latest](https://github.com/henriquecaner/hormozi-gtm/releases/latest). Dentro do app:

1. `+` → **Criar plugin** → **Fazer upload de plugin**
2. Arraste o ZIP

O plugin aparece em **Plugins pessoais** e os comandos `/hormozi-gtm:*` ficam disponíveis.

## Compatibilidade

| Ambiente | Status |
|---|---|
| Claude Code CLI | suportado |
| Claude Code Desktop (Mac/Win) | suportado |
| Claude Cowork (Desktop app) | suportado (upload ZIP) |
| Claude.ai (web) | não suportado |

## Versionamento

SemVer. Mudanças catalogadas em [`CHANGELOG.md`](./CHANGELOG.md). Releases automáticas via tag `v*` (workflow `release.yml`):

1. Bump `version` em `.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` (3 lugares, validados pelo CI)
2. Adicionar seção `## [X.Y.Z]` em `CHANGELOG.md`
3. `git tag vX.Y.Z && git push origin vX.Y.Z`

Workflow dispara, gera ZIP, extrai notes do CHANGELOG, publica release no GitHub.

### Roadmap

Roadmap distante em `[0.5.0+]` (vide [`CLAUDE.md`](./CLAUDE.md)): customização via `settings.json`, multi-cliente em paralelo (gtm-context por slug), comando `/export` para empacotar outputs.

## Desenvolvimento local

```bash
git clone https://github.com/henriquecaner/hormozi-gtm.git
cd hormozi-gtm
claude --plugin-dir .
```

Para empacotar um ZIP local sem disparar release oficial:

```bash
bash scripts/build-zip.sh
```

Detalhes de arquitetura em [`CLAUDE.md`](./CLAUDE.md).

## Autor

[LEVEL](https://github.com/henriquecaner) — Henrique Caner ([caner@thelevel.com.br](mailto:caner@thelevel.com.br)).

## Licença

Proprietary — LEVEL. Uso autorizado por contrato. Distribuição restrita ao time interno e clientes contratuais.
