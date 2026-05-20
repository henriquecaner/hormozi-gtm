---
plugin: hormozi-gtm
plugin_version: {{plugin_version}}
command: case-study
version: 1
status: draft
created: {{ISO8601}}
client: {{empresa_slug}}
product: {{produto_slug}}
case_cliente: {{cliente_caso_nome}}
case_cliente_slug: {{cliente_caso_slug}}
permission: {{public | pseudonym | confidential}}
frameworks:
  - value-equation
  - grand-slam-offer
  - hook-framework
humanizer_pass: true
humanizer_mode: full
parent_version: {{caminho_v_anterior_ou_null}}
---

# Case Study — {{cliente_caso_nome}}

## TL;DR

**De:** {{antes em 1 linha — ex: "Ciclo de venda B2B de 90 dias, CAC R$ 450, conversão 8%"}}
**Para:** {{depois em 1 linha — ex: "Ciclo 28 dias, CAC R$ 180, conversão 14%"}}
**Em:** {{N}} {{dias | semanas | meses}}

---

## 1-linha (use em ads / headlines de LP)

> "{{cliente}} reduziu {{métrica}} em {{X}}% em {{tempo}}."

---

## 1-parágrafo (use em cold email / proof point em LP)

{{4-6 linhas que combinam: quem é o cliente (com categoria), problema específico, mecanismo aplicado, resultado numérico, timeframe. Voz Hormozi: direta, sem superlativos. Ex:}}

> A Stark Bank vinha com ciclo de venda B2B de 90 dias quando expandiram além do B2C. Mesmo time de vendas, mesma audience, ciclo dobrou. Aplicamos diagnóstico de Value Equation + reescrita das 3 páginas-chave (LP, demo, proposta) + instalação de SDR script validado. Em 90 dias, ciclo caiu pra 28 dias e CAC reduziu 60%.

---

## Quote do cliente

> "{{frase exata do cliente, em aspas. Ideal 1-3 frases. Mantém voz natural — não 'corrige' português do cliente.}}"
>
> — {{Nome}}, {{Cargo}} na {{Empresa}}

---

## Case completo

### Contexto

{{2-3 parágrafos: quem é {{cliente}}, em qual setor, qual stage (ARR, headcount), o que estava acontecendo antes. Concreto, com números quando possível.}}

### O problema

{{1-2 parágrafos: descrição específica do problema. Não "queriam crescer". Algo como "Ciclo de venda B2B subiu de 45 para 90 dias após expansão pra mercado de meio porte. Time de vendas mantido, mas conversão por SDR caiu 40%."}}

### Diagnóstico

{{1-2 parágrafos: o que descobrimos. Qual vetor do Value Equation estava quebrado, qual mecanismo errado. Ex: "Probabilidade percebida era 4/10. SDR script era de B2C aplicado em B2B — não tratava objeções específicas de comitê de compra."}}

### Mecanismo aplicado

{{2-3 parágrafos: o que foi feito. Specific. Frameworks nomeados. Ex:
- Reescrevemos o SDR script aplicando High-Performance Communication (Leila Scaling Framework).
- Adicionamos garantia condicional ("setup em 5 dias ou devolvemos a primeira parcela").
- Instalamos kit de objeções com top 5 reframes treinados em role-play 1x/semana.

Quantifica o esforço: "3 semanas de implementação, com 2 sessions por semana".}}

### Resultados

| Métrica | Antes | Depois | Mudança | Em quanto tempo |
|---|---|---|---|---|
| {{Métrica primária}} | {{X}} | {{Y}} | {{N}}% | {{tempo}} |
| {{Métrica 2}} | {{X}} | {{Y}} | {{N}}% | {{tempo}} |
| {{Métrica 3}} | {{X}} | {{Y}} | {{N}}% | {{tempo}} |
| {{Métrica 4 — opcional}} | {{X}} | {{Y}} | {{N}}% | {{tempo}} |

### Implicação

{{1-2 parágrafos: o que esse case revela sobre o problema generalizável. Ex: "Founders B2B que migram do B2C frequentemente subestimam quanto SDR script precisa de adaptação. Não é problema de copy — é problema de framework comunicacional. Aplicar Leila Scaling resolve em 60-90 dias."}}

---

## Visualização (mockup descritivo)

```
[Logo {{cliente}}]
"De {{X}} para {{Y}}"

{{quote curta de 1 linha}}

- {{Métrica 1}}: {{X}} → {{Y}}
- {{Métrica 2}}: {{X}} → {{Y}}

[Foto/avatar do cliente]
— {{Nome}}, {{cargo}}
```

(Use esse mockup para passar pro time de design fazer success card / proof block na LP.)

---

## Permissão e uso

- **Permissão de uso:** {{público | pseudônimo | confidencial}}
- **Quando obtida:** {{data}}
- **Onde pode ser usado:** {{LP | Ad | Cold email | Apresentação | Webinar | Todos}}
- **Restrições:** {{nenhuma | sem nome real | sem números absolutos | etc.}}

---

## Anti-padrões aplicados (auto-check)

- [ ] Case tem números antes/depois auditable
- [ ] Quote é exata (não parafraseada)
- [ ] Mecanismo aplicado é específico (não "aplicamos nosso método")
- [ ] Timeframe explícito
- [ ] Sem superlativos vazios ("resultados incríveis", "transformou completamente")
- [ ] Permissão registrada
- [ ] 3 versões geradas: completo, 1-parágrafo, 1-linha

---

*Case study gerado pelo plugin hormozi-gtm. Persona Alex Hormozi aplicada. Humanizer (modo full) aplicado.*
