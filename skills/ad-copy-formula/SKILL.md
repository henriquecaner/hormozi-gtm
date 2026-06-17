---
name: ad-copy-formula
description: Ad copy formula from $100M Leads — copy structure for warm, cold, and paid ads with per-channel variations. Use when writing text ad copy (Facebook, Google, LinkedIn, email), short-form captions, or lead ads.
---

# Ad Copy Formula

Source: Alex Hormozi, *$100M Leads*, Chapter 4 (Ad Mechanics).

## Base structure

```
[Attention] → [Problem/Outcome] → [Mechanism] → [Social Proof] → [CTA + Reason to act now]
```

The same structure serves all 3 contexts (warm / cold / paid), with different calibration.

## Variation 1: Warm (1:1, audience knows you)

**Characteristics:**
- Story-driven is fine (the audience gives you the benefit of the doubt)
- Can skip explicit Mechanism (they already trust you)
- Social proof optional (you're already the proof)
- Direct, personal tone

**Warm structure:**
```
1 line with a specific problem/outcome
+ Story or context (1-2 lines)
+ Offer + direct CTA
```

**Example (warm DM/email):**
> "Remember the problem you mentioned about closing $50k+ deals through your SDRs?
> I just recorded a 12-minute workshop showing the system that worked for my last 12 clients.
> Want it? I'll send the link."

## Variation 2: Cold (1:1, audience doesn't know you)

**Characteristics:**
- Short (3-5 lines max)
- Names the ICP immediately
- Problem-first (not story)
- Mechanism named to establish authority
- Low-friction CTA (doesn't ask for the sale directly)

**Cold structure:**
```
ICP-specific opener (1 line)
+ Concrete problem (1 line)
+ Mechanism / solution (1 line)
+ Low-friction CTA (1 line)
```

**Example (cold email):**
> "Saw you're Head of Sales at [company]. B2B SaaS in the 100-500k MRR range usually loses 40% of opportunities to price objection.
> We built a reframe system (the R.A.M.P. System) that flipped that in 12 companies last year.
> Can I send you the playbook PDF? It's 8 pages, 15 minutes to read."

## Variation 3: Paid (1:many, feed)

**Characteristics:**
- Visual hook (image/video) + headline + sub-headline + CTA
- Headline can be tested in isolation
- Short copy (Facebook/IG) or structured (LinkedIn ads)
- CTA points to the LP (doesn't ask for the sale in the ad)

**Paid structure:**
```
HEADLINE (5-12 words, dream outcome or problem hook)
SUB-HEADLINE (1-2 sentences with specificity)
CTA (3-5 words, action verb)
```

**Example (Facebook/IG):**
> **Headline:** "SaaS closers landing $50k+ deals without cold email"
> **Sub-headline:** "The R.A.M.P. System in 8 steps — used by 12 closers who went from $8k to $23k MRR in 47 days"
> **CTA:** "Watch the free workshop"

## A/B testing

For each variation, generate 5-10 versions changing 1 element:
- Versions 1-3: change headline only
- Versions 4-6: change hook only (image/video)
- Versions 7-9: change CTA only

Run in parallel, measure:
- **CPC** (cost per click)
- **CTR** (click-through rate)
- **CVR** (conversion rate on the destination LP)

Kill any variation with CPC > 2x the median.

## Anti-patterns

- Generic copy ("discover the secret")
- Hook with no specificity
- "Learn more" CTA (no action verb)
- Empty promise with no mechanism
- All caps
- Too many emoji (>1 per line)

## Localizing the voice per market

Superlative tolerance varies by market. In some markets, copy translated literally from US English — "transformative", "leverage", "standing out", "revolutionary" — burns credibility faster than it does in the US, because it reads as a translated ad, not a native one. When the target market isn't US English, calibrate the superlative load down and lean harder on verifiable facts.

The substitution principle is universal: trade the adjective any competitor could also claim for a fact only you can prove.

| Marketing adjective (weak) | Verifiable fact (strong) |
|---|---|
| "transformative results" | "results in 90 days" / "went from $X to $Y" |
| "leverage our expertise" | "use what we learned across 14 accounts" |
| "robust solution" | "works for B2B SaaS with cycles > 45 days" |
| "industry-leading platform" | "3 years in use, validated across 6 niches" |
| "seamless integration" | "installs in 1 hour without touching your code" |

Rule of thumb: if the adjective could appear in any competitor's copy, swap it for a verifiable fact. This is hormozi-voice rule #1 — number + verb, never an adjective.

## Example: B2B SaaS (cold email, fintech ICP)

> **Subject:** Cut [product] setup from 3 weeks to 3 days
>
> Saw your profile working on payments integration at [company]. Most fintechs lose 15-20% of transactions to initial-setup objection (heard that from 6 pricing squads last quarter).
>
> We built a framework that cuts setup from 3 weeks to 3 days via KYC automation + single-page checkout onboarding. Validated with [reference client], [reference client], and 4 others.
>
> Can I send you the case study? 5-page PDF, 10-minute read.
>
> — [Name], [Company]

**Why it works:**
- Specific subject (real client, number, timeframe)
- Opener: proof of research + a quantified data point (15-20% loss)
- Named mechanism (KYC + single-page checkout)
- Proof point with real names
- Specific CTA (not "let's chat?", but "I'll send a 5-page PDF, 10 min")
- Direct tone, no "transformative" / "revolutionary" / "leverage"

## Workflow

1. Define the channel (warm / cold / paid)
2. Define the offer + target ICP
3. Choose the hook angle (use skill `hook-framework`)
4. Write the base structure
5. Generate 3-5 variations for A/B
6. Run it through the humanizer
7. Run the test, kill losers, scale the winner

## Application by use case

| Case | Use |
|---|---|
| Sales LP | The LP headline inherits from the winning ad |
| Ad script | The script copy mirrors the ad formula structure |
| Hooks batch | Generated hooks are input for the first element (Attention) |

## Detailed reference

See `reference/100m-leads-extracts.md` (Ad Mechanics section).
