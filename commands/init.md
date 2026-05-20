---
description: Bootstrap do plugin — cria gtm-context.md no projeto consumidor com ICP, oferta, brand voice, canais e stage. Auto-disparado se outros comandos rodarem sem gtm-context.md presente. Suporta --refresh para atualizar contexto stale.
argument-hint: "[--refresh]"
---

# /hormozi-gtm:init

Inicializa o contexto persistente da empresa/cliente que vai usar os outros comandos do plugin. Cria `gtm-context.md` na raiz do projeto consumidor.

## Carregamento de persona

Use o subagent `hormozi-persona` como voz. Toda saída em 1ª pessoa. Sem voz de assistente.

## Skills ativas

- `output-conventions` (segue convenção de naming e frontmatter)
- `humanizer-rules` (modo lite — output é interno, ficar firme no tom direto)

## Argumentos

- Sem argumento: cria `gtm-context.md` se não existir. Se existir, pergunta se quer atualizar.
- `--refresh`: atualiza arquivo existente sem perder versões anteriores (versiona via git ou cria backup `gtm-context.bak.md`).

## Fluxo

### Passo 1: Detecta estado

Verifica se `gtm-context.md` existe na raiz do projeto consumidor (cwd).

- **Não existe:** segue pra Passo 2 (entrevista completa).
- **Existe e foi atualizado <30 dias:** avisa "contexto recente detectado". Pergunta se quer `--refresh` ou abortar.
- **Existe e foi atualizado >30 dias:** avisa "contexto stale (X dias)". Recomenda `--refresh`.

### Passo 2: Entrevista (8 perguntas)

Faz uma pergunta de cada vez. Não dispara as 8 em batch.

1. **Empresa/projeto** — nome
2. **Categoria/mercado** — em 1 frase específica
3. **ICP principal** — em 1 frase ultra-específica (segmento + tamanho + papel + dor)
4. **Oferta principal e preço atual**
5. **Transformação prometida** — em quanto tempo, quem vira o quê
6. **Brand voice** — cola 1-2 parágrafos de material existente OU descreve (formal/casual, técnico/acessível, intensidade Hormozi 0-100%)
7. **Canais ativos** — Core Four split em % (warm, cold, organic, paid)
8. **Stage atual** — validando oferta / escalando aquisição / otimizando monetização / exit prep

Pergunta extra opcional:
9. **Maior gargalo atual** — em 1 frase honesta

### Passo 3: Gera gtm-context.md

Carrega `${CLAUDE_PLUGIN_ROOT}/templates/gtm-context.md` como base. Preenche com inputs do usuário. Salva em `gtm-context.md` na raiz do projeto.

### Passo 4: Resumo + próximos passos

Mostra ao usuário:
- Caminho do arquivo criado
- Highlights do contexto capturado (3-5 bullets)
- Próximos passos sugeridos:
  - Se sem audit: `/hormozi-gtm:audit` pra diagnosticar oferta
  - Se com audit: `/hormozi-gtm:lp` ou `/hormozi-gtm:roteiro` pra produzir copy
  - Se for análise de pricing: `/hormozi-gtm:pricing`

## Modo --refresh

Quando passado:
1. Faz backup do arquivo atual: copia para `gtm-context.bak-YYYYMMDD.md`
2. Lê o atual e preenche pré-respostas das 8 perguntas
3. Pergunta uma de cada vez: "Atual: X. Manter ou atualizar?"
4. Salva nova versão com `last_updated` atualizado e `version` incrementada

## Critério de pronto

- [ ] `gtm-context.md` existe na raiz do projeto consumidor
- [ ] Frontmatter completo com `last_updated`, `version`, `empresa`, `slug`
- [ ] As 8 seções principais preenchidas (não placeholders)
- [ ] Brand voice tem exemplo concreto colado ou descrição detalhada
- [ ] Próximos passos sugeridos baseados no stage informado

## Anti-padrões

- Pular pergunta porque "parece óbvio" — sempre pergunta as 8
- Aceitar resposta genérica em ICP ("PMEs em geral") — pede especificidade
- Pular Brand voice — é o que evita output genérico mais tarde
- Disparar todas as 8 perguntas de uma vez (overwhelm)

## Output esperado

Ao final, usuário vê:
- Caminho do arquivo (`./gtm-context.md`)
- Highlights: empresa, ICP, oferta, gargalo
- 1-3 próximos passos concretos

Mensagem em 1ª pessoa, direto, sem chatbot vibe.
