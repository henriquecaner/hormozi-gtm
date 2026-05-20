---
description: Cria ou refina landing page de vendas long-form (2000-3500 palavras). Usa Grand Slam Offer, Value Equation, bonus stacking, scarcity/urgency, guarantees. Humanizer modo full obrigatório. Soft warning se sem audit recente.
argument-hint: "[--produto=<slug>] [--ref=<caminho>] [--foco=<secao>] [--skip-audit] [--no-humanize]"
---

# /hormozi-gtm:lp

Constrói landing page de vendas estruturada em 10 seções (hero → agitação → oferta → quem é você → stack → garantia → prova → preço → FAQ → CTA final). Cada seção aplica frameworks específicos.

## Carregamento de persona

Orquestrador: `hormozi-persona`.
Análise de oferta: delegate a `offer-architect` (carrega briefing).
Pass final: delegate a `humanizer` (modo full, obrigatório).

## Skills ativas

- `grand-slam-offer` (oferta como núcleo)
- `value-equation` (cada seção aumenta 1+ vetor)
- `bonus-stacking` (seção 5)
- `scarcity-urgency` (seções 6 e 10)
- `guarantees` (seção 6)
- `hook-framework` (headline + sub-headline)
- `ad-copy-formula` (microcopy, CTAs)
- `humanizer-rules` (modo full)
- `output-conventions`

## Argumentos

| Argumento | Comportamento |
|---|---|
| (vazio) | Cria nova LP. Pede slug do produto. |
| `slug` | Cria nova LP com slug informado |
| `outputs/lp/<arquivo>.md` | Modo refinar — lê arquivo, pergunta o que melhorar, cria v{n+1} |
| `--section=<nome>` | Em modo refinar, foca em 1 seção (hero, agitacao, oferta, quem-voce, stack, garantia, prova, preco, faq, cta) |
| `--skip-audit` | Pula o soft warning de audit inexistente |
| `--no-humanize` | Pula o pass do humanizer (debug, comparação A/B) |
| `--overwrite` | Sobrescreve v{n} em vez de criar v{n+1} |

## Pré-requisitos

1. `gtm-context.md` existe → carrega ICP, oferta, brand voice, audience externa, intensidade do tom
2. Se não existe → dispara `/hormozi-gtm:init` antes
3. Audit recente de oferta (≤14 dias)? → carrega como `audit_ref`
4. Sem audit recente e sem `--skip-audit` → pergunta interativa (não warning passivo):

> "Sua oferta não passou por Value Equation audit nas últimas 2 semanas. Copy escrita sobre oferta sem audit recente frequentemente precisa retrabalho.
>
> Como prefere seguir?
> (1) Rodar `/hormozi-gtm:audit` agora (5min) — recomendado, LP fica muito melhor
> (2) Seguir mesmo assim — entendo o risco, quero a LP hoje
> (3) Cancelar — vou rodar audit em sessão separada e volto"

Se (1): roda `/hormozi-gtm:audit` inline, salva audit, carrega `audit_ref` automaticamente, continua o fluxo de LP.
Se (2): segue, mas grava `audit_ref: null` no frontmatter com nota.
Se (3): sai limpo, sem criar arquivo.

## Fluxo

### Modo CRIAR

#### Passo 1: Coleta inputs

Carrega o que tiver de `gtm-context.md`. Pede o que faltar:
- ICP (obrigatório)
- Oferta principal (obrigatório)
- Preço (obrigatório)
- Transformação prometida — em quanto tempo, quem vira o quê (obrigatório)
- Prova social disponível (opcional)
- Garantia atual ou pretendida (opcional)
- Bônus disponíveis (opcional — agent sugere se não tem)
- Urgência/escassez genuína (opcional — agent flag se inventado)

#### Passo 2: Construção

Delegate a `offer-architect` para destilar briefing de oferta. Em seguida, `hormozi-persona` (orquestrador) recebe o briefing e monta 10 seções via template `lp.md`:

1. Hero (headline + sub + CTA + microcopy)
2. Agitação do problema (3 sintomas + por que outras soluções falham)
3. Apresentação da oferta (Grand Slam)
4. Quem é você / por que ouvir (story)
5. Stack de bonuses (3-5 ímpar com valor R$)
6. Garantia (condicional + métrica + compensação)
7. Prova social (3+ cases comparáveis)
8. Pricing + ancoragem
9. FAQ (4-6 objeções mapeadas)
10. CTA final + urgência genuína

#### Passo 3: Humanizer pass (full)

Delegate ao subagent `humanizer`. Aplica todas as regras (não só lite).

#### Passo 4: Salva output

Salva em `outputs/lp/lp-{slug}-{YYYYMMDD}-v1.md` com frontmatter completo.

#### Passo 5: Preview na conversa

Mostra:

```
✅ Salvo em: outputs/lp/lp-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Headline: "{{texto da headline}}"
   • Garantia: {{tipo + cláusula}}
   • Stack: {{N}} bonuses, valor total R$ {{X}}
   • CTA primário: "{{texto}}"
   • Status humanizer: ✓ full pass

👉 Próximos passos:
   1. Mostra ao cliente, captura feedback
   2. /hormozi-gtm:hooks --produto={{slug}} → testa headlines em ad
   3. /hormozi-gtm:review --ref=outputs/lp/... → se quiser feedback brutal interno
```

Termina perguntando se quer refinar alguma seção (sem reabrir o diálogo todo).

### Modo REFINAR

#### Passo 1: Lê arquivo existente

Carrega frontmatter + conteúdo. Identifica versão, frameworks já aplicados, audit_ref, parent_version.

#### Passo 2: Diagnóstico

Pergunta:
> "O que quer melhorar? (1) headline (2) oferta (3) garantia (4) prova social (5) stack de bonuses (6) FAQ (7) reescrever tudo (8) outro"

Ou se `--section=<nome>` foi passado, vai direto pra seção.

#### Passo 3: Refinement

Aplica mudança mantendo o resto. Re-roda humanizer.

#### Passo 4: Salva v{n+1}

Salva em mesma pasta com `v{n+1}`. Frontmatter aponta `parent_version` para `v{n}`.

#### Passo 5: Diff resumido

Mostra:
- O que mudou (1 linha por mudança)
- Caminho do novo arquivo

## Critério de pronto

- [ ] Headline passa em 3 testes (especificidade numérica + tweet test + curiosity gap)
- [ ] Oferta tem stack visível (3-5 bonuses ímpares)
- [ ] Pelo menos 1 garantia condicional (não "satisfação garantida")
- [ ] CTA repetido 3+ vezes
- [ ] Nenhuma frase genérica ("transforme sua vida", "alcance seu potencial")
- [ ] Humanizer full aplicado (sem em-dash overuse, sem rule of three, sem AI vocab)
- [ ] Arquivo salvo em `outputs/lp/` com frontmatter completo
- [ ] Próximos passos sugeridos (geralmente: `/hormozi-gtm:hooks` pra testar headlines)

## Anti-padrões

- Pular Value Equation audit antes (LP em cima de oferta fraca = dinheiro fora)
- Bonus genérico ("acesso à comunidade")
- Garantia genérica ("satisfação garantida")
- CTA "saiba mais" (sem ação verbal)
- Tom de copywriter clichê (use 1ª pessoa Hormozi)
- Inventar escassez fake (usa skill `scarcity-urgency` pra checar genuíno)

## Output esperado

Arquivo: 2000-3500 palavras, estruturado em 10 seções com headers H2.
Conversa: 5-10 linhas com highlights + caminho + próximos passos.
