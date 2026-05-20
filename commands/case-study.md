---
description: Case study estruturado — antes/depois numérico, contexto, mecanismo aplicado, quote do cliente. Gera tanto a peça completa quanto assets de 1-linha pra usar em LP, ad e email. Para consultor que precisa converter projeto vencido em proof asset.
argument-hint: "[--cliente=<nome>] [--ref=<caminho>] [--antes=<numero>] [--depois=<numero>] [--no-humanize]"
---

# /hormozi-gtm:case-study

Case study é a moeda de Probability no Value Equation. Sem case study sólido, qualquer copy soa promessa. Esta skill estrutura case study real com antes/depois numérico, contexto suficiente pra leitor relacionar, mecanismo nomeado.

## Carregamento de persona

Use `hormozi-persona` para orquestrar. Delegate ao `offer-architect` para amarrar antes/depois no Value Equation. Pass final pelo `humanizer` modo **full** (case study vai pra LP/ad/email externos).

## Skills ativas

- `value-equation` (antes/depois mapeado nos 4 vetores)
- `grand-slam-offer` (case valida promessa da oferta)
- `ad-copy-formula` (formatos curtos derivados)
- `hook-framework` (headline do case)
- `humanizer-rules` (modo full)
- `output-conventions`

## Argumentos

| Argumento | Comportamento |
|---|---|
| (vazio) | Modo interativo: pergunta cliente + antes + depois + contexto |
| `--cliente=<nome>` | Nome do cliente (com permissão) |
| `--ref=<caminho>` | Refinar case study existente |
| `--antes=<numero>` | Número antes (ex: CAC R$ 450, ciclo 75d, ARR 500k) |
| `--depois=<numero>` | Número depois |
| `--no-humanize` | Pula humanizer (debug) |

## Pré-requisitos

1. `gtm-context.md` existe → carrega ICP, oferta
2. Cliente real com permissão pra usar nome ou anonimato consentido
3. Dados quantitativos do antes/depois (não case "intuitivo")

## Fluxo

### Passo 1: Coleta de dados estruturada

Em modo interativo, pergunta em sequência:

1. **Identificação do cliente** (nome real ou pseudônimo consentido + categoria/setor)
2. **Stage** (ARR ou tamanho da empresa quando começou)
3. **Problema específico** (em 1 frase Hormozi — não "queriam crescer", mas "ciclo de venda B2B subiu de 45 pra 90 dias")
4. **Antes** (3-5 métricas numéricas concretas)
5. **Mecanismo aplicado** (qual framework / skill do plugin foi usado, em 2-3 linhas)
6. **Depois** (mesmas 3-5 métricas numéricas)
7. **Timeframe** (em quanto tempo aconteceu)
8. **Quote do cliente** (frase exata, com aspas)

### Passo 2: Validação

Antes de gerar o case, valida com `value-equation`:
- Antes/depois cobrem qual vetor (Dream Outcome, Probability, Time Delay, Effort)?
- Diff numérico é mensurável e auditable?
- Quote do cliente sustenta a narrativa?

Se faltar dado obrigatório, pergunta. Não inventa.

### Passo 3: Geração

Delegate ao `ad-architect` para escrever a narrativa do case (4-6 parágrafos), e ele devolve:
- Versão completa (1 página, pra usar em LP/proposta)
- Versão 1-parágrafo (pra usar em ad / cold email)
- Versão 1-linha (pra usar em hero da LP / hook de ad)

### Passo 4: Assets derivados

- Quote card (pra Instagram / LP testimonial section)
- 1-line case (pra ad headline)
- 1-paragraph case (pra cold email proof)

### Passo 5: Humanizer (full)

### Passo 6: Salva

`outputs/case-studies/case-study-{cliente_slug}-{YYYYMMDD}-v{n}.md` via template `case-study.md`.

### Passo 7: Preview na conversa

```
✅ Salvo em: outputs/case-studies/case-study-{cliente}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Cliente: {{nome}}
   • Antes → Depois: {{X}} → {{Y}} ({{N}}% mudança)
   • Timeframe: {{N}} {{dias|semanas|meses}}
   • Quote: "{{primeiros 50 chars}}..."
   • Assets gerados: completo + 1-parágrafo + 1-linha + quote card
   • Status humanizer: ✓ full pass

👉 Próximos passos:
   1. Pedir permissão final ao cliente (se ainda não pediu)
   2. Adicionar em outputs/lp/ existente (seção "Quem usou")
   3. /hormozi-gtm:hooks com 1-linha como referência
```

## Critério de pronto

- [ ] Cliente identificado (nome real ou pseudônimo consentido)
- [ ] Antes/depois numéricos auditable (não estimativa)
- [ ] Timeframe específico (não "rápido")
- [ ] Mecanismo nomeado (framework aplicado, não "trabalho duro")
- [ ] Quote do cliente em aspas (palavra exata)
- [ ] Versões completas: 1-página, 1-parágrafo, 1-linha
- [ ] Humanizer full aplicado

## Anti-padrões

- Case sem número (apenas adjetivos)
- "Cliente teve resultado incrível" (vago, descartável)
- Inventar número estimado e marcar como real
- Quote inventada ou parafraseada (cliente percebe)
- Case com 5 frameworks aplicados simultaneamente (não dá pra atribuir resultado)
- Versão completa só (sem assets curtos derivados)
- Pular humanizer em peças que vão pra cliente externo
