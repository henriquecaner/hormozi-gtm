---
name: ad-copy-formula
description: Formula de ad copy do $100M Leads — estrutura de copy para warm, cold e paid ads com variações por canal. Use ao escrever copy de ad em texto (Facebook, Google, LinkedIn, email), legenda de short-form, anúncios de leads.
---

# Ad Copy Formula

Fonte: Alex Hormozi, *$100M Leads*, Capítulo 4 (Ad Mechanics).

## Estrutura base

```
[Attention] → [Problem/Outcome] → [Mechanism] → [Social Proof] → [CTA + Reason to act now]
```

Mesma estrutura serve aos 3 contextos (warm / cold / paid), com calibragem diferente.

## Variação 1: Warm (1:1, audience te conhece)

**Características:**
- Story-driven OK (audience te dá benefit of the doubt)
- Pode pular Mechanism explícito (já confia em você)
- Social proof opcional (já é a prova)
- Tom direto, pessoal

**Estrutura warm:**
```
1 frase com problema/outcome específico
+ Story ou contexto (1-2 frases)
+ Oferta + CTA direto
```

**Exemplo (DM/email warm):**
> "Lembra do problema que você comentou sobre fechar deal de R$ 50k+ via SDR?
> Acabei de gravar um workshop de 12min mostrando o sistema que funcionou pros últimos 12 clientes meus.
> Quer ver? Te mando o link."

## Variação 2: Cold (1:1, audience não te conhece)

**Características:**
- Curto (3-5 linhas máximo)
- Specifica ICP imediato
- Problem-first (não story)
- Mechanism nomeado pra estabelecer autoridade
- CTA baixa fricção (não pede compra direta)

**Estrutura cold:**
```
ICP-specific opener (1 linha)
+ Problema concreto (1 linha)
+ Mechanism / solução (1 linha)
+ CTA de baixa fricção (1 linha)
```

**Exemplo (cold email):**
> "Vi que você é Head of Sales na [empresa]. SaaS B2B na faixa de 100-500k MRR geralmente perde 40% das oportunidades em objeção de preço.
> A gente desenvolveu um sistema de reframe (Sistema R.A.M.P.) que reverteu isso em 12 empresas no último ano.
> Posso te mandar o playbook em PDF? São 8 páginas, leva 15min pra ler."

## Variação 3: Paid (1:many, feed)

**Características:**
- Hook visual (image/video) + headline + sub-headline + CTA
- Headline pode ser testada isoladamente
- Copy curto (Facebook/IG) ou estruturado (LinkedIn ads)
- CTA pra LP (não pede compra no ad)

**Estrutura paid:**
```
HEADLINE (5-12 palavras, dream outcome ou problem hook)
SUB-HEADLINE (1-2 frases com especificidade)
CTA (3-5 palavras, ação verbal)
```

**Exemplo (Facebook/IG):**
> **Headline:** "Closer de SaaS fechando R$ 50k+ sem cold email"
> **Sub-headline:** "Sistema R.A.M.P. em 8 passos — usado por 12 closers que saíram de R$ 8k pra R$ 23k MRR em 47 dias"
> **CTA:** "Ver workshop gratuito"

## A/B testing

Para cada variação, gera 5-10 versões mudando 1 elemento:
- Versões 1-3: muda só headline
- Versões 4-6: muda só hook (image/video)
- Versões 7-9: muda só CTA

Roda paralelo, mede:
- **CPC** (cost per click)
- **CTR** (click-through rate)
- **CVR** (conversion rate na LP destino)

Mata variações com CPC > 2x mediana.

## Anti-padrões

- Copy genérico ("descubra o segredo")
- Hook sem especificidade
- CTA "saiba mais" (sem ação verbal)
- Promessa vazia sem mechanism
- Tudo em caps lock
- Emoji em excesso (>1 por linha)

## Variações regionais (PT-BR)

Voz brasileira tolera **menos superlativo** que copy americana. "Revolucionário", "transformador", "alavancar", "destacando-se" são sinais de tradução literal de copy EN e queimam credibilidade no Brasil mais rápido que nos EUA.

**Substituições por mercado:**

| Padrão EN | Tradução literal (ruim) | Adaptação BR (boa) |
|---|---|---|
| "transformative results" | "resultados transformadores" | "resultados em 90 dias" / "saiu de R$ X pra R$ Y" |
| "leverage our expertise" | "alavancar nossa expertise" | "usar o que aprendemos com 14 contas" |
| "robust solution" | "solução robusta" | "funciona em SaaS B2B com ciclo > 45 dias" |
| "industry-leading platform" | "plataforma líder do setor" | "uso 3 anos, valido em 6 nichos" |
| "seamless integration" | "integração transparente" | "instala em 1 hora sem mexer no código" |

Regra prática: se o adjetivo poderia estar em copy de qualquer concorrente, troca por fato verificável.

## Exemplo: B2B SaaS Brasil (cold email, ICP fintech)

> **Subject:** Reduzir setup do Olist Pay de 3 semanas pra 3 dias
>
> Vi seu perfil na Olist trabalhando com integração de pagamentos. A maioria das fintechs brasileiras perde 15-20% das transações por objeção de setup inicial (ouvi isso de 6 squads de pricing no último trimestre).
>
> A gente montou um framework que corta setup de 3 semanas pra 3 dias via automação do KYC + onboarding com checkout em 1 página. Validado com Stark Bank, Cora e 4 outras.
>
> Posso te mandar o case study? PDF de 5 páginas, 10min de leitura.
>
> — Henrique, LEVEL

**Por quê funciona:**
- Subject específico (cliente real, número, prazo)
- Opener: prova de research + dado quantificado (15-20% perda)
- Mechanism nomeado (KYC + checkout 1 página)
- Proof point com nomes reais
- CTA específico (não "vamos conversar?", e sim "te mando PDF 5 pgs, 10min")
- Tom direto, sem "transformador" / "revolucionário" / "alavancar"

## Workflow

1. Define canal (warm / cold / paid)
2. Define oferta + ICP target
3. Escolhe ângulo do hook (use skill `hook-framework`)
4. Escreve estrutura base
5. Gera 3-5 variações para A/B
6. Passa pelo humanizer
7. Roda teste, mata losers, escala winner

## Aplicação por caso de uso

| Caso | Uso |
|---|---|
| LP de vendas | Headline da LP herda do ad winner |
| Roteiro de ad | Copy do roteiro espelha estrutura ad formula |
| Hooks batch | Hooks gerados são input pra primeiro elemento (Attention) |

## Referência detalhada

Veja `reference/100m-leads-extracts.md` (seção Ad Mechanics).
