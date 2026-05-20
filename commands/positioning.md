---
description: Competitive teardown + positioning statement. Mapeia 3-5 concorrentes diretos (features, preço, persona, mensagem), identifica eixos de diferenciação, propõe positioning statement testável. Para founder que vai entrar em nicho com competidores estabelecidos ou que sente sua mensagem "indistinguível".
argument-hint: "[--produto=<slug>] [--ref=<caminho>] [--competidores=<N>] [--no-humanize]"
---

# /hormozi-gtm:positioning

Posicionamento não é "como você se descreve". É **onde você está no mapa mental do prospect** quando ele compara você com alternativas. Esta skill mapeia o terreno, identifica seu eixo único e produz statement testável.

## Carregamento de persona

Use `hormozi-persona` para orquestrar. Delegate ao `offer-architect` para amarrar Value Equation contra competidores. Pass final pelo `humanizer` modo **full** (positioning statement vira copy headline / hero da LP).

## Skills ativas

- `value-equation` (compara vetores entre você e competidores)
- `grand-slam-offer` (positioning vira hero copy)
- `pricing-playbook` (posicionamento de preço vs mercado)
- `niche-selection` (saturação ajuda decidir eixos)
- `humanizer-rules` (modo full)
- `output-conventions`

## Argumentos

| Argumento | Comportamento |
|---|---|
| (vazio) | Modo interativo: pergunta produto + competidores |
| `--produto=<slug>` | Slug do produto |
| `--ref=<caminho>` | Refinar positioning existente |
| `--competidores=<N>` | Quantidade de competidores a mapear (default 4) |
| `--no-humanize` | Pula humanizer |

## Pré-requisitos

1. `gtm-context.md` existe → carrega ICP, oferta, preço atual
2. Idealmente: lista de 3-5 competidores que cliente já consideraria (research prévio)
3. Para análise de preço: dados de pricing público dos competidores

## Fluxo

### Passo 1: Coleta competidores

Em modo interativo, pergunta:
- Quem são 3-5 competidores diretos (mesmo problema, mesmo ICP)?
- 1 competidor com posicionamento mais premium (ancora superior)?
- 1 competidor com posicionamento mais barato (ancora inferior)?
- 1 substituto não-óbvio (algo que o cliente faria em vez de contratar essa categoria)?

### Passo 2: Mapping matrix

Constrói matrix com:

| Competidor | Posicionamento declarado | Preço | ICP primário | Mensagem chave | Força percebida | Fraqueza percebida |
|---|---|---|---|---|---|---|

Para cada competidor, preenche cada coluna com observação concreta (não interpretação criativa).

### Passo 3: Identifica eixos de diferenciação

Possíveis eixos:
- **Problema único resolvido** (resolvemos X específico que ninguém ataca)
- **Velocidade** (3 dias vs 3 semanas)
- **Specificidade** (B2B SaaS fintech vs SaaS B2B geral)
- **Founder-market fit** (ex-CFO consultando ex-CFOs)
- **Garantia condicional única**
- **Metodologia proprietária**
- **Preço** (alta ou baixa âncora)
- **Formato** (1:1 enterprise vs group vs self-serve)

Para cada eixo, verifica: você consegue defender com fato auditable?

### Passo 4: Diferenciação por dimensão

Para 2-3 eixos onde você é defensável:

```
Eixo: {{Velocidade de implementação}}

Competidores:
- A: 4-6 semanas
- B: 3-4 semanas
- C: 2-3 semanas
Você: 5 dias.

Defensa: case study X (Stark, Cora) onde implementação foi em 5 dias documentados.
Razão estrutural: framework de onboarding em 4 sessions vs 12 da maioria.
```

### Passo 5: Positioning statement

Estrutura padrão:

> "Para [ICP específico], [empresa] é a única que [unique value proposition] sem [trade-off comum]."

Exemplo:
> "Para SaaS B2B com ciclo de venda > 60 dias, a LEVEL é a única que reduz ciclo em 40% em 5 dias de implementação sem precisar reescrever copy ou trocar o time de SDR."

**Teste de qualidade do statement:**
- ICP específico (não "B2B" genérico)?
- Unique value mensurável (não "transformamos seu funil")?
- Trade-off explícito (cliente sabe o que NÃO precisa abrir mão)?
- Você consegue sustentar com case real?

### Passo 6: Aplicação

Gera derivados:
- Hero copy para LP (3 variações)
- Subject de email frio (3 variações)
- Bio de LinkedIn (1)
- Frase de abertura de sales call (1)

### Passo 7: Humanizer (full)

### Passo 8: Salva

`outputs/positioning/positioning-{produto_slug}-{YYYYMMDD}-v{n}.md` via template `positioning-map.md`.

### Passo 9: Preview na conversa

```
✅ Salvo em: outputs/positioning/positioning-{slug}-{YYYYMMDD}-v{n}.md
📋 Preview:
   • Competidores mapeados: {{N}}
   • Eixos de diferenciação defensáveis: {{N}}
   • Positioning statement:
     "{{primeiras 100 chars}}..."
   • Derivados: 3 hero copies + 3 cold subject + 1 LinkedIn bio
   • Status humanizer: ✓ full pass

👉 Próximos passos:
   1. Testar positioning statement em ad headline (R$ 200 ad)
   2. Atualizar LP hero com nova versão
   3. /hormozi-gtm:lp para reescrever full LP com novo positioning
```

## Critério de pronto

- [ ] ≥ 3 competidores mapeados com dados concretos
- [ ] ≥ 2 eixos de diferenciação defensáveis (com fato auditable)
- [ ] Positioning statement passa teste de qualidade
- [ ] Derivados gerados (hero, cold subject, bio)
- [ ] Humanizer full aplicado

## Anti-padrões

- Diferenciação sem fato (claim sem case sustentando)
- Positioning genérico ("a melhor consultoria de growth")
- Competir em eixo onde já tem 5+ players (não diferencia)
- Trade-off invisível (cliente não sabe o que perde escolhendo você)
- Ignorar substituto não-óbvio (cliente pode "não contratar ninguém" e fazer interno)
- Positioning statement que só você entende (não passa em 1 leitura de stranger)
