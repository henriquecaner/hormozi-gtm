---
name: template-gtm-context
description: "Esqueleto interno do output do comando /hormozi-gtm:init. Carregado pelo comando, não para uso direto."
---

# Template — gtm-context.md

Esqueleto canônico do arquivo `gtm-context.md`. O comando `/hormozi-gtm:init` carrega esta skill e preenche o esqueleto abaixo com os inputs do usuário. Reproduza a estrutura exata: frontmatter + todas as seções + placeholders `{{...}}`.

```markdown
---
empresa_nome: {{empresa_nome}}
empresa_slug: {{empresa_slug}}
last_updated: {{YYYY-MM-DD}}
version: 1
plugin: hormozi-gtm
---

# GTM Context — {{empresa_nome}}

Arquivo de contexto persistente. Todos os comandos do plugin consultam ele automaticamente. Atualize-o quando mudanças relevantes acontecerem (oferta, preço, ICP, canal). Versões antigas ficam em git.

## Empresa

- **Categoria/mercado** (1 frase específica):
  > {{categoria}}

- **Stage atual:**
  > {{validando-oferta | escalando-aquisicao | otimizando-monetizacao | exit-prep}}

## ICP

- **ICP em 1 frase ultra-específica** (incluindo segmento, tamanho, papel, dor principal):
  > {{icp}}

- **Anti-ICP** (quem você NÃO atende, pra filtrar):
  > {{anti-icp}}

## Oferta

- **Core offer** (1 frase com transformação prometida):
  > {{core-offer}}

- **Preço atual:**
  > {{preco}}

- **Modelo:** one-time | recorrência | híbrido
  > {{modelo}}

- **Transformação prometida** (em quanto tempo, quem vira o quê):
  > {{transformacao}}

- **Última audit:** {{caminho_para_audit_recente_ou_nenhum}}

## Brand Voice

- **Tom:** {{ex: inteligente, prático, estruturado, direto, ocasionalmente provocativo}}
- **Mix Hormozi vs voz própria:** {{ex: 70% Hormozi + 30% voz LEVEL}}
- **Audience externa:** {{B2B sênior | consumidor final | mid-market | enterprise}}
- **Intensidade do tom:** {{baixa | média | alta}} — calibra agressividade da copy

**Exemplo de copy que ressoa com o ICP** (cole 1-2 parágrafos de material existente, post no LinkedIn, email do fundador):

> {{exemplo_de_copy}}

## Canais

**Core Four split atual (soma 100):**

| Canal | % | Status |
|---|---|---|
| Warm (1:1) | {{ex: 30}}% | {{ativo/inativo}} |
| Cold (1:1) | {{ex: 10}}% | {{ativo/inativo}} |
| Organic (1:many free) | {{ex: 40}}% | {{ativo/inativo}} |
| Paid (1:many paid) | {{ex: 20}}% | {{ativo/inativo}} |

**Lead magnet ativo:** {{nome_ou_nenhum}}

## Unit economics (se conhecidos)

- **Preço médio composto:** R$ {{}}
- **Custo variável:** R$ {{}}
- **LTGP estimado:** R$ {{}}
- **CAC atual:** R$ {{}}
- **Ratio LTGP:CAC:** {{}}
- **Payback period:** {{dias}}

## Contexto adicional

- **Maior gargalo atual** (1 frase honesta):
  > {{gargalo}}

- **Tentativas anteriores que falharam:**
  > {{lista_ou_n_a}}

- **Decisões recentes ou em aberto:**
  > {{lista_ou_n_a}}

---

## Como atualizar

Rode `/hormozi-gtm:init --refresh` quando:
- ICP mudou
- Oferta principal mudou
- Preço mudou >10%
- Canal dominante mudou
- Stage da empresa avançou

Plugin avisa "contexto stale" se `last_updated` for >30 dias.
```
