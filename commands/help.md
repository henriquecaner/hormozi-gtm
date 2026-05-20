---
description: Matriz de decisão interativa. Responde 3 perguntas e recomenda o command certo. Útil para onboarding de cliente novo ou quando você não sabe por onde começar uma sessão.
argument-hint: "[--objetivo=auditar|copy|pricing|plano|review|outreach|objection]"
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
| `--objetivo=outreach` | Recomenda direto: `/hormozi-gtm:email` |

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
(8) Outro / não tenho certeza
```

### Passo 3: Roteamento por resposta

**(1) Diagnóstico:**
> Recomendo `/hormozi-gtm:audit` — diagnóstico de oferta via Value Equation (Dream Outcome × Probability ÷ Time Delay × Effort). Identifica o gargalo crítico, propõe top 3 alavancas, reescreve a oferta em 1 parágrafo.
>
> Comando: `/hormozi-gtm:audit`

**(2) Copy externa:**
> Que tipo de copy?
> (a) Landing page de vendas → `/hormozi-gtm:lp`
> (b) Roteiro de vídeo (VSL longo 8-15min ou short-form 15-60s) → `/hormozi-gtm:roteiro`
> (c) Bateria de hooks para ads (10-20 variações) → `/hormozi-gtm:hooks`
>
> ⚠️ Recomendo rodar `/hormozi-gtm:audit` primeiro se não fiz nas últimas 2 semanas. Copy escrita sobre oferta fraca é dinheiro perdido.

**(3) Pricing:**
> `/hormozi-gtm:pricing` — revisão contra as 5 leis do Pricing Playbook (LEAKED) + validação contra Value Equation + matemática LTV:CAC. Output em range, não número único, com tiering Silver/Gold/Platinum quando aplicável.
>
> Comando: `/hormozi-gtm:pricing`

**(4) Plano 90 dias:**
> `/hormozi-gtm:plano` — business plan estruturado (Core Four split + Money Model 4 níveis + roadmap por trimestre). Use para empresa nova ou produto novo dentro de empresa existente.
>
> Comando: `/hormozi-gtm:plano`

**(5) Review brutal:**
> `/hormozi-gtm:review --ref=<caminho_do_material>` — feedback construtivo sem mercy. Veredito LEVE/MÉDIO/CRÍTICO, top 3 fixes concretos, reescrita de trechos críticos.
>
> Comando: `/hormozi-gtm:review --ref=outputs/lp/lp-...md`

**(6) Outreach:**
> `/hormozi-gtm:email` — sequência de 5-7 emails (cold, warm, nurture ou re-engagement) com hook + agitação + proof + CTA + reactivation. Tunado para B2B brasileiro.
>
> Comando: `/hormozi-gtm:email --tipo=cold`

**(7) Objeções:** (planejado em v0.3.0)
> `/hormozi-gtm:objections` ainda em roadmap. Por enquanto: rode `/hormozi-gtm:audit` — identifica gargalo do Value Equation (frequentemente a raiz da objeção).

**(8) Não tenho certeza:**
> Por estágio típico:
> - **Cedo (pré-PMF, < 20 clientes):** `/hormozi-gtm:init` → `/hormozi-gtm:audit` → `/hormozi-gtm:plano`.
> - **Validando oferta:** `/hormozi-gtm:audit` → `/hormozi-gtm:pricing` → `/hormozi-gtm:lp`.
> - **Tem produto, precisa lead:** `/hormozi-gtm:hooks` → `/hormozi-gtm:email` → `/hormozi-gtm:lp`.
> - **Plateau de revenue:** `/hormozi-gtm:audit` (procura saturação de canal/oferta) → `/hormozi-gtm:plano`.

### Passo 4: Salva preferência (opcional)

Pergunta: "Quer que eu salve esse fluxo recomendado em `gtm-context.md` como sua próxima ação?" Se sim, atualiza o campo `next_action` no contexto.

## Critério de pronto

- [ ] Detectou se `gtm-context.md` existe
- [ ] Apresentou matriz de decisão clara
- [ ] Recomendou 1 comando primário + alternativas se aplicável
- [ ] Mencionou pré-requisitos quando relevante (ex: audit antes de copy)
- [ ] (Opcional) Salvou próxima ação em `gtm-context.md`

## Anti-padrões

- Recomendar 4+ comandos de uma vez (usuário fica perdido)
- Repetir descrição do comando em vez de mandar direto
- Esquecer de checar `gtm-context.md` antes de recomendar (recomendação sem contexto é genérica)
- Soar como assistente ("vou te ajudar a encontrar..."). É Hormozi: vai direto.
