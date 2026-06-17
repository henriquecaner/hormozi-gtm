---
name: email-deliverability
description: Deliverability de cold/warm email — warm-up de domínio (4-6 semanas), SPF/DKIM/DMARC setup, reputation management, antispam triggers a evitar. Complementa /hormozi-gtm:email. Para founder que vai lançar outbound em escala (50+ emails/dia) e não quer queimar domínio principal.
---

# Email Deliverability

Fonte: Alex Hormozi, *$100M Leads* (Cap. 3, "Cold Outreach") + literatura de deliverability (Lemlist, Smartlead, Instantly playbooks) adaptada ao contexto BR.

## Por que essa skill existe

`sales-sequencing` ensina sequência de 5 touches. `/hormozi-gtm:email` gera a copy. Esta cobre a camada técnica embaixo: **o email chegar no inbox**. Copy genial no spam folder converte zero.

Founder brasileiro frequentemente dispara 200 cold emails do gmail corporativo principal, queima reputação em 7 dias, depois descobre que todos os emails de vendas (incluindo warm) caem no spam por 3-6 meses.

## Os 3 pilares de deliverability

### 1. Autenticação (SPF + DKIM + DMARC)

**SPF** (Sender Policy Framework) — autoriza quais servidores podem mandar email pelo seu domínio.

**DKIM** (DomainKeys Identified Mail) — assina digitalmente cada email. Inbox provider valida que o email é genuíno.

**DMARC** (Domain-based Message Authentication, Reporting, and Conformance) — política do que fazer com emails que falharem SPF/DKIM (rejeitar, quarentena, deixar passar).

**Setup mínimo aceitável (antes de qualquer outbound):**
- SPF record configurado e válido.
- DKIM ativo no provedor de email (Google Workspace, Microsoft 365, ProtonMail).
- DMARC com policy `p=quarantine` (no mínimo) ou `p=reject` (ideal).

**Diagnóstico:** rode `mxtoolbox.com` ou `mail-tester.com` no seu domínio. Score < 8/10 = ajustes obrigatórios antes de cold outreach.

### 2. Warm-up de domínio (4-6 semanas)

Domínio novo ou parado por > 90 dias precisa de warm-up antes de mandar volume.

**Cadência de warm-up sem ferramenta automatizada:**

| Semana | Emails/dia | Tipo | Audiência |
|---|---|---|---|
| 1 | 5-10 | Conversacionais reais (reply expected) | Network próprio |
| 2 | 15-25 | Conversacionais + 1-2 warm emails | Network + indicações |
| 3 | 30-50 | Mix warm/transactional | Lista própria opt-in |
| 4 | 50-80 | + 10 cold emails muito segmentados | Adiciona primeiros prospects |
| 5 | 80-120 | + cold scaling | Lista cold qualificada |
| 6 | 100-200 | Volume operacional | Lista frio segmentada |

**Princípio:** cada email do warm-up precisa **gerar resposta humana** (reply, click, abertura). Inbox provider mede engagement, não volume.

**Ferramentas de warm-up automatizado:** Lemlist Warmup, Mailwarm, Warmbox, Folderly. Rodam por 4-8 semanas em paralelo ao seu uso normal. Custo: R$ 80-300/mês por domínio.

### 3. Domain & inbox strategy

**Regra crítica:** **nunca** rode cold outreach do seu domínio principal de produção.

**Setup recomendado:**
- Domínio principal: `empresa.com.br` (email transacional, suporte, comunicação warm com clientes).
- Domínios de outbound: `getempresa.com`, `tryempresa.com`, `empresa.io` (registrados próximos ao principal, apontam para o site mas mandam outbound).
- 2-4 inboxes por domínio de outbound, cada uma mandando 30-50 emails/dia max.

**Cálculo de capacidade:**

```
3 domínios secundários × 3 inboxes/domínio × 40 emails/dia = 360 emails/dia
~10.800 emails/mês sem queimar reputação
```

Quer mandar 500/dia? Precisa 4-5 domínios ou ferramenta multi-inbox tipo Smartlead/Instantly.

## Antispam triggers — o que evita

### Triggers em subject

Evita palavras-spam clássicas (filtradas por Bayes):
- "Grátis", "100%", "Garantido", "Urgente", "Ganhe", "Promoção", "Oportunidade"
- Caps lock em qualquer palavra ("OPORTUNIDADE", "URGENTE")
- Excesso de exclamação (≥2 !!)
- Emojis no subject (varia por provider; Outlook é mais sensível)
- Pontuação excessiva (?? !! ...)

### Triggers em body

- HTML pesado / templates de design (cold email B2B deve ser plain text)
- Múltiplos links (1 link é OK, 3+ aumenta spam score)
- Imagens (>= 1 imagem em cold email B2B levanta flag)
- Anexos (anexo em primeiro email = quase sempre spam)
- "Unsubscribe" não funcional (cold outreach precisa link de opt-out funcionando, ou marca spam quando prospect tenta sair)
- Footer corporativo grande (logo + endereço + redes sociais = pega flag de "promoção em massa")

### Triggers de comportamento

- Sending velocity > 80 emails/inbox/dia → flagrado como bulk
- Bounce rate > 5% → reputation cai (limpa lista antes)
- Complaint rate > 0.3% → reputation queima rapidamente
- Reply rate < 1% → algoritmo entende "ninguém quer esse email"
- Mesma mensagem exata mandada para >50 prospects → flagrado como spam pattern

## Métricas que importam

| Métrica | Alvo | O que mede |
|---|---|---|
| **Deliverability rate** | ≥ 95% | % de emails que chegam (não bouncearam) |
| **Inbox placement** | ≥ 85% | % que cai no inbox (não spam folder) — Glock Apps ou Mail-tester |
| **Bounce rate** | < 3% | Lista limpa? |
| **Open rate** | ≥ 35% | Subject + reputação do remetente |
| **Reply rate** | ≥ 5% | Sequência inteira funcionando |
| **Complaint rate** | < 0.1% | Reputação preservada |

Sinais de problema:
- Open rate caindo semana após semana → reputação esgotando.
- Bounce rate > 5% → lista comprada ou desatualizada (kill).
- Reply rate alto + open rate caindo → spam folder pegou.

## Plano de recovery se domínio queimou

Sinais de domínio queimado:
- Inbox placement < 50% (teste com mail-tester.com).
- Open rate de cold cai de 40% para 15% sem mudança de copy.
- Clientes warm reclamando que não recebem emails seus.

**Recovery (4-8 semanas):**
1. **Para todo outbound** no domínio queimado por 30 dias.
2. **Roda warm-up** automatizado em paralelo (Lemlist Warmup, Mailwarm) — gera conversational reply rate alto.
3. **Inspeciona blacklists** (Spamhaus, Barracuda, Sorbs) via mxtoolbox. Se está em alguma, faz request de remoção.
4. **Reinstala SPF/DKIM/DMARC** se houve drift.
5. **Reintroduce volume gradual** (semana 5-8): 10 → 30 → 80 → 200 emails/dia.

**Se domínio principal está queimado:** considera abandoná-lo para outbound, mantém apenas para transactional, registra novo domínio para outbound.

## Setup técnico (sequência operacional)

**Semana 0:**
- Registra 2-3 domínios secundários parecidos ao principal.
- Configura cada um: SPF, DKIM, DMARC.
- Compra inbox em cada (Google Workspace ~R$ 35/mês cada).
- Configura signature simples (nome + cargo + 1 linha).

**Semana 1-4:** warm-up automatizado em paralelo (Lemlist Warmup ou similar).

**Semana 5+:** começa outbound real respeitando cadência.

## Anti-padrões

- Cold outreach do domínio principal (queima tudo).
- Comprar lista pronta (bounce > 20%, queima reputação em 48h).
- Usar 1 só inbox para 200+ emails/dia (flagrado como bulk).
- Pular warm-up ("eu uso esse email há anos") — uso casual ≠ outbound.
- HTML template colorido em cold (parece marketing automation, vai pra promotional tab).
- Múltiplos CTAs / links no email frio (1 link sempre).
- Não inspecionar Mail-Tester antes de cada campaign nova.
- Continuar mandando para bouncebacks (queima reputação cumulativamente).

## Aplicação por caso de uso

| Caso | Como usar |
|---|---|
| `/hormozi-gtm:email --tipo=cold` antes de lançar | Skill orienta setup técnico antes da primeira campaign |
| `/hormozi-gtm:plano` com Core Four split alto em cold (>30%) | Plano inclui setup de 2-3 domínios secundários + warm-up budget |
| Reply rate caindo sem mudança de copy | Diagnóstico: deliverability problem, não copy problem |

## Quando NÃO entra

- Outbound 100% via LinkedIn DM (não usa email).
- Volume < 20 emails/dia (pode usar domínio principal se warm).
- Negócio 100% inbound (sem cold outreach).

## Referência detalhada

`reference/100m-leads-extracts.md` cap. 3 ("Cold Outreach") + literatura externa de deliverability (não inclusa no plugin).
