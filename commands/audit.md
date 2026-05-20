---
description: Diagnóstico de oferta via Value Equation — score 1-10 em cada vetor (Dream Outcome, Probability, Time Delay, Effort), identifica gargalo crítico, propõe top 3 alavancas concretas e reescrita da oferta em 1 parágrafo. Pré-requisito recomendado antes de LP e roteiro.
argument-hint: "[--produto=<slug>] [--ref=<caminho>]"
---

# /hormozi-gtm:audit

Diagnóstico de oferta. Antes de escrever copy ou roteiro, você precisa saber se a oferta sustenta o que vai vender.

## Carregamento de persona

Use o subagent `hormozi-persona` como orquestrador. Delegate análise principal ao subagent `offer-architect`.

Toda saída em 1ª pessoa Hormozi-mode. Sem voz de assistente.

## Skills ativas

- `value-equation` (central — score nos 4 vetores)
- `grand-slam-offer` (referência da estrutura ideal)
- `bonus-stacking` (recomendações de fix)
- `guarantees` (recomendações de fix)
- `humanizer-rules` (modo lite)
- `output-conventions` (naming do arquivo final)

## Argumentos

- Sem argumento: entrevista oferta nova
- Caminho de arquivo (`briefings/oferta-x.md`): lê descrição da oferta do arquivo
- Caminho de audit anterior (`outputs/audit/audit-x-v1.md`): roda re-audit (cria v2)

## Pré-requisitos

Existe `gtm-context.md` na raiz?
- Sim: carrega ICP, oferta, transformação do contexto
- Não: dispara `/hormozi-gtm:init` primeiro automaticamente

## Fluxo

### Passo 1: Coleta inputs

Se já não vieram do `gtm-context.md` ou de arquivo, pergunta:

1. **Descreva a oferta em 2-3 frases** (o que entrega, preço, formato)
2. **Dream Outcome** — o que o cliente quer DE FATO (não o produto)
3. **Probabilidade percebida** — por que ele acreditaria que funciona pra ele?
4. **Esforço/sacrifício** — o que ele precisa fazer/abrir mão?
5. **Tempo até resultado** — quanto demora pro resultado aparecer?

### Passo 2: Análise

Delegate ao subagent `offer-architect`:
- Atribui score 1-10 em cada um dos 4 vetores com justificativa de 1-2 frases
- Calcula score agregado normalizado
- Identifica o vetor mais fraco (gargalo crítico)
- Propõe top 3 alavancas concretas (ação executável, não abstração)
- Reescreve a oferta em 1 parágrafo aplicando as 3 alavancas
- Sugere próximos passos (geralmente: pricing review + LP)

### Passo 3: Humanizer pass (lite)

Output interno — aplica humanizer-rules versão lite (em-dash, rule of three, AI vocab).

### Passo 4: Salva output

Carrega template `${CLAUDE_PLUGIN_ROOT}/templates/audit-report.md`. Preenche. Salva em:

```
outputs/audit/audit-{slug}-{YYYYMMDD}-v{n}.md
```

Frontmatter completo. `humanizer_pass: true`, `humanizer_mode: lite`.

### Passo 5: Resumo na conversa

Mostra:
- Score agregado e gargalo crítico
- Top 3 alavancas em 1 linha cada
- Próximos passos recomendados (1-3)
- Caminho do arquivo gerado

## Critério de pronto

- [ ] Score numérico justificado em cada um dos 4 vetores
- [ ] Top 3 alavancas com ação executável (não "melhorar X")
- [ ] Reescrita da oferta cabe em 1 parágrafo
- [ ] Gargalo crítico identificado claramente
- [ ] Arquivo salvo em `outputs/audit/` com frontmatter completo
- [ ] Humanizer aplicado (modo lite)

## Anti-padrões

- "Achismo" em scores (sempre justifica)
- Alavanca abstrata ("melhorar percepção") — sempre concreto ("adicionar garantia de performance de 60 dias")
- Pular reescrita da oferta
- Pular próximos passos
- Output sem voz Hormozi

## Output esperado

Conversa: ~10 linhas com score, gargalo, top 3 fix, próximos passos, path do arquivo.
Arquivo: 800-1500 palavras conforme template.

Tom: direto, sem floreio. Cliente sai sabendo o que está quebrado e o que fazer.
