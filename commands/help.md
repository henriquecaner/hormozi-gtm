---
description: Matriz de decisão interativa. Responde 3 perguntas e recomenda o command certo. Útil para onboarding de cliente novo ou quando você não sabe por onde começar uma sessão. Cobre os 17 commands do plugin.
argument-hint: "[--objetivo=auditar|copy|pricing|plano|review|email|objection|case-study|webinar|positioning|content|churn|onboarding]"
---

# /hormozi-gtm:help

Não sabe qual comando rodar? Responde 3 perguntas e mostro o caminho recomendado.

## Carregamento de persona

Use `hormozi-persona` em modo orientação — direto, sem economizar tempo do usuário. Sem perguntar "como posso ajudar?". Vai direto pra matriz.

## Skills ativas

Nenhuma skill específica é carregada — `/help` é roteador, não produtor de output.

## Argumentos

| Argumento | Comportamento |
|---|---|
| (vazio) | Modo interativo: 3 perguntas em sequência |
| `--objetivo=auditar` | Recomenda direto: `/hormozi-gtm:audit` |
| `--objetivo=copy` | Vai para sub-pergunta (LP / VSL / hooks / ad short) |
| `--objetivo=pricing` | Recomenda direto: `/hormozi-gtm:pricing` |
| `--objetivo=plano` | Recomenda direto: `/hormozi-gtm:plano` |
| `--objetivo=review` | Recomenda direto: `/hormozi-gtm:review` |
| `--objetivo=email` | Recomenda direto: `/hormozi-gtm:email` |
| `--objetivo=objection` | Recomenda direto: `/hormozi-gtm:objections` |
| `--objetivo=case-study` | Recomenda direto: `/hormozi-gtm:case-study` |
| `--objetivo=webinar` | Recomenda direto: `/hormozi-gtm:webinar` |
| `--objetivo=positioning` | Recomenda direto: `/hormozi-gtm:positioning` |
| `--objetivo=content` | Recomenda direto: `/hormozi-gtm:content-hub` |
| `--objetivo=churn` | Recomenda direto: `/hormozi-gtm:churn-prevention` |
| `--objetivo=onboarding` | Recomenda direto: `/hormozi-gtm:onboarding-cliente` |

## Pré-requisitos

Nenhum. `/help` opera mesmo sem `gtm-context.md` — é o ponto de entrada para usuário novo.

## Fluxo

### Passo 1: Detecta estado

```
Você tem gtm-context.md neste projeto?
  Não → recomenda começar com /hormozi-gtm:init antes de qualquer outro comando.
  Sim → vai para Passo 2.
```

### Passo 2: Pergunta de objetivo (multiple choice)

```
O que você quer fazer agora?

(1) Entender se minha oferta está sustentando (diagnóstico)
(2) Criar copy externa (LP, ad, hooks, roteiro)
(3) Validar ou estruturar pricing
(4) Montar plano GTM 90 dias / business plan
(5) Receber feedback brutal em material existente
(6) Estruturar sequência de outreach (email/LinkedIn)
(7) Mapear objeções e scripts para sales call
(8) Estruturar case study + proof assets
(9) Planejar webinar B2B (30-45min)
(10) Definir positioning vs competição
(11) Montar roadmap de conteúdo orgânico 30-90 dias
(12) Diagnosticar e reduzir churn / winback
(13) Estruturar onboarding dos primeiros 30 dias de cliente
(14) Outro / não tenho certeza
```

### Passo 3: Roteamento por resposta

**(1) Diagnóstico:**
> `/hormozi-gtm:audit` — diagnóstico de oferta via Value Equation (Dream Outcome × Probability ÷ Time Delay × Effort). Identifica o gargalo crítico, propõe top 3 alavancas, reescreve a oferta em 1 parágrafo.

**(2) Copy externa:**
> Que tipo de copy?
> (a) Landing page de vendas → `/hormozi-gtm:lp`
> (b) Roteiro de vídeo (VSL longo 8-15min ou short-form 15-60s) → `/hormozi-gtm:roteiro`
> (c) Bateria de hooks para ads (10-20 variações) → `/hormozi-gtm:hooks`
>
> ⚠️ Recomendo rodar `/hormozi-gtm:audit` primeiro se não fiz nas últimas 2 semanas. Copy escrita sobre oferta fraca é dinheiro perdido.

**(3) Pricing:**
> `/hormozi-gtm:pricing` — revisão contra as 5 leis do Pricing Playbook (LEAKED) + validação contra Value Equation + matemática LTV:CAC. Output em range, não número único, com tiering Silver/Gold/Platinum quando aplicável.

**(4) Plano 90 dias:**
> `/hormozi-gtm:plano` — business plan estruturado (Core Four split + Money Model 4 níveis + roadmap por trimestre). Use para empresa nova ou produto novo dentro de empresa existente.

**(5) Review brutal:**
> `/hormozi-gtm:review --ref=<caminho_do_material>` — feedback construtivo sem mercy. Veredito LEVE/MÉDIO/CRÍTICO, top 3 fixes concretos, reescrita de trechos críticos. Tem modo Re-review automático (delta v1↔v2).

**(6) Outreach:**
> `/hormozi-gtm:email` — sequência de 5-7 emails (cold, warm, nurture ou re-engagement) com hook + agitação + proof + CTA + reactivation. Tunado para B2B brasileiro. Complementa com a skill `email-deliverability` para setup técnico (warm-up de domínio, SPF/DKIM/DMARC).

**(7) Objeções:**
> `/hormozi-gtm:objections` — matriz por ICP. Cada objeção mapeada com root cause (oferta/preço/timing/trust), reframe em 2 frases, script palavra-por-palavra pra sales call, mitigação na oferta. Top 3 com script completo treinável em role-play.

**(8) Case study:**
> `/hormozi-gtm:case-study --cliente=<nome>` — case study estruturado (antes/depois numérico auditable + quote exato + mecanismo nomeado). Gera versão completa + 1-parágrafo (cold email) + 1-linha (headline LP) + quote card.

**(9) Webinar:**
> `/hormozi-gtm:webinar --duracao=30|45|60` — estrutura B2B em 7 blocos (abertura + diagnóstico + mechanism + cases + oferta + Q&A + CTA). Diferente de VSL direct-response (12min). Inclui plant questions para Q&A.

**(10) Positioning:**
> `/hormozi-gtm:positioning` — competitive teardown com 3-5 competidores, eixos de diferenciação defensáveis, positioning statement testável. Gera hero copy (3 variações) + cold subject (3) + LinkedIn bio + abertura de sales call.

**(11) Conteúdo orgânico:**
> `/hormozi-gtm:content-hub --duracao=30|60|90` — roadmap de conteúdo. Tópico × formato × funnel stage × CTA. Calendar semanal + repurpose plan + métricas por mês.

**(12) Churn / retenção:**
> `/hormozi-gtm:churn-prevention` — diagnóstico por tipo (precoce/médio/tardio/voluntário/passivo), win/loss interview script, 4-block retention playbook, sequência winback opcional (`--foco=winback`), impacto financeiro projetado.

**(13) Onboarding de cliente:**
> `/hormozi-gtm:onboarding-cliente` — jornada dos primeiros 30 dias em 5 marcos (welcome → kickoff → quick win D7 → NPS D14 → mid-point D21 → wrap D30). Triggers de intervenção quantitativos. Reduz churn precoce em 40-60% típico.

**(14) Não tenho certeza:**
> Por estágio típico:
> - **Cedo (pré-PMF, < 20 clientes):** `/hormozi-gtm:init` → `/hormozi-gtm:audit` → `/hormozi-gtm:plano`.
> - **Validando oferta:** `/hormozi-gtm:audit` → `/hormozi-gtm:pricing` → `/hormozi-gtm:lp`.
> - **Tem produto, precisa lead:** `/hormozi-gtm:hooks` → `/hormozi-gtm:email` → `/hormozi-gtm:lp`.
> - **Fechando deals high-ticket:** `/hormozi-gtm:objections` → `/hormozi-gtm:positioning` → `/hormozi-gtm:case-study`.
> - **Cliente já fechou, agora entregar:** `/hormozi-gtm:onboarding-cliente`.
> - **Reduzir churn em base recorrente:** `/hormozi-gtm:churn-prevention`.
> - **Plateau de revenue:** `/hormozi-gtm:audit` (procura saturação de canal/oferta) → `/hormozi-gtm:plano`.

## Critério de pronto

- [ ] Detectou se `gtm-context.md` existe
- [ ] Apresentou matriz de decisão clara (14 opções)
- [ ] Recomendou 1 comando primário + alternativas se aplicável
- [ ] Mencionou pré-requisitos quando relevante (ex: audit antes de copy)

## Anti-padrões

- Recomendar 4+ comandos de uma vez (usuário fica perdido)
- Repetir descrição do comando em vez de mandar direto
- Esquecer de checar `gtm-context.md` antes de recomendar (recomendação sem contexto é genérica)
- Soar como assistente ("vou te ajudar a encontrar..."). É Hormozi: vai direto.
- Listar command que não existe (mantém esta lista alinhada com `commands/`)
