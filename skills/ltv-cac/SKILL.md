---
description: Matemática de unit economics — LTV (Lifetime Value), LTGP (Lifetime Gross Profit), CAC (Customer Acquisition Cost), payback period, ratio. Use para validar viabilidade de modelo, calibrar pricing e justificar (ou matar) ads.
---

# LTV : CAC Math

Fonte: Alex Hormozi, *$100M Leads*, Capítulo 8 (Paid Ads Part II).

## Definições

### LTGP — Lifetime Gross Profit
```
LTGP = (Preço Médio - Custo Variável Médio) × Meses Retidos
```

Use LTGP, não LTV. LTV inclui receita; LTGP inclui só o que SOBRA depois de servir o cliente. É o que paga ads.

### CAC — Customer Acquisition Cost
```
CAC = Ad Spend Total / Clientes Adquiridos
```

Inclui ferramentas de aquisição, equipe de vendas alocada, comissões. Não só ad spend bruto.

### Ratio LTGP : CAC
```
Ratio = LTGP / CAC
```

**Benchmarks:**
- `< 1:1` — você está perdendo dinheiro. Para de escalar.
- `1:1 a 3:1` — sobrevive. Não escala bem.
- `3:1 a 5:1` — saudável. Escala paid com confiança.
- `> 5:1` — você está deixando dinheiro na mesa em ad spend. Aumenta budget.

### Payback period
```
Payback = CAC / (Profit Mensal por Cliente)
```

**Benchmarks:**
- `< 30 dias` — Client-Financed Acquisition. Paid scaling ilimitado.
- `30-90 dias` — saudável se capital permite.
- `> 90 dias` — risco de cash crunch ao escalar.

## Como modelar do zero

1. **Preço médio de venda:** ticket único + média de upsell × take rate
2. **Custo variável médio:** custo de servir 1 cliente (não overhead)
3. **Retenção média:** se one-time, 1; se recorrência, meses médios antes de churn
4. **LTGP = (Preço - Custo) × Retenção**
5. **CAC atual ou pretendido**
6. **Ratio e payback**

## Exemplo (curso digital + comunidade)

```
Core offer: R$ 4.997 one-time
Upsell take rate: 30% × R$ 1.997 = R$ 599 esperado
Continuity: 20% upgrade × R$ 297/mês × 6 meses = R$ 357 esperado
Preço médio composto: R$ 4.997 + R$ 599 + R$ 357 = R$ 5.953
Custo variável: R$ 350 (hosting + suporte + processamento)
LTGP = R$ 5.953 - R$ 350 = R$ 5.603

CAC pretendido em paid: R$ 1.200
Ratio = 5.603 / 1.200 = 4.67:1 ✓
Payback = 1.200 / 1.997 (profit do upsell em 30 dias) = ~18 dias ✓
```

Ambos benchmarks passam. Escala paid.

## Sinais de problema

- LTGP < 2x CAC → pricing baixo ou churn alto
- Payback > 6 meses → modelo cash-intensive, exige capital
- Ratio cai ao escalar → CAC subindo mais rápido que LTGP (saturação de canal)
- LTV alto mas LTGP baixo → margem ruim, ajusta entrega ou preço

## Quando usar essa skill

| Caso | Aplicação |
|---|---|
| Audit de oferta | Calcula ratio atual e identifica se problema é receita ou custo |
| Pricing review | Justifica range de preço novo via ratio target |
| Business plan | Seção de unit economics com cenários conservador/realista/otimista |

## Referência detalhada

Veja `reference/100m-leads-extracts.md` (seção Paid Ads + Money Math).
