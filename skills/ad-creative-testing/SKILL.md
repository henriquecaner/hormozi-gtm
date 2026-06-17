---
name: ad-creative-testing
description: Statistical creative-testing framework. Test matrix (change 1 element at a time), required sample size, kill criteria with a number, scale winner vs. pivot the whole creative. For the founder who spends $200 on an ad and loses faith — this skill teaches the minimum you have to invest to get a real signal.
---

# Ad Creative Testing

Source: Alex Hormozi, *$100M Leads* (Ch. 4, "Ad Mechanics") + cross-reference with `ad-copy-formula` and `hook-framework`.

## Why this skill exists

`ad-copy-formula` teaches **what to write** in an ad. This one covers **how to test it systematically** to find out which version works, with statistical sample size and objective kill criteria. Without it, a founder spends $200 on an ad, sees a bad result, loses faith, and attacks the wrong problem (thinks it's the copy when it might be the audience, or vice versa).

Most founders kill a creative on day 1-2, before there's a statistical signal. The ones who test systematically find the winner 3x faster on the same budget.

## Test matrix — change 1 element at a time

You can only isolate which element moved the result if you change 1 at a time. Changing 3 at once is gambling, not testing.

**Element hierarchy (most impactful to least):**

1. **Hook (first 3 seconds)** — 50-70% of CTR comes from here.
2. **Audience / targeting** — 20-30%.
3. **Creative format (video vs. image vs. carousel)** — 10-20%.
4. **CTA and body copy** — 5-15%.
5. **Visual details (color, font, thumbnail)** — 2-5%.

**Rule:** optimize top-down. Don't touch the font while the hook is weak.

**Example matrix:**

```
Variable            Variation A          Variation B          Variation C
Hook                "Cut CAC 38%"        "Stop losing leads"  "The SDR mistake"
Audience            ICP-1                ICP-2                ICP-1
Format              15s video            15s video            15s video
CTA                 "Get the PDF"        "Get the PDF"        "Get the PDF"
```

You're testing **Hook only** (3 variations). Audience constant (control). Format constant. CTA constant. Once you find the winning Hook, switch to it, then test Audience with the Hook fixed.

## Sample size — how much to invest to get a real signal

Minimum sample size depends on the expected CTR/conversion rate. Heuristic by stage:

| Test stage | Minimum investment per variant | Why that number |
|---|---|---|
| **Hook test (3-5 variants)** | $150-300 each | Enough for 1,000-2,000 impressions, identifies a winner if CTR diff ≥ 30% |
| **Audience test (2-4 segments)** | $300-500 each | Needs a larger sample to isolate the audience effect |
| **Creative format test** | $500-1,000 each | Format affects the engagement signal, needs more impressions |
| **Full funnel (with conversion)** | $1k-3k each | Needs 20-50 conversions for a reliable ratio |

**Rule of thumb:** if you can't invest the minimum, **don't test yet**. Wait until you have the budget. An underpowered test gives a false signal.

**Simple calculation (Hook test):**
- Expected baseline CTR: ~1-2% on cold ads.
- To detect a 30% CTR difference (e.g., 1.5% → 2%): you need ~500-1,000 clicks per variant.
- 1.5% × 1,000 clicks = 67k impressions. On paid social: ~$200-300.

## Kill criteria — when to kill a variant

Founders kill too early (12h, 50 impressions) or too late (run it 7 days with horrible performance). Objective criterion:

**Kill the variant when:**
1. ≥ 1,000 accumulated impressions (sufficient sample)
2. **AND** CTR < 50% of the best performer
3. **AND** no improvement in the last 250 impressions

Example:
```
Variant A: 2.1% CTR (best performer, 1,200 impressions)
Variant B: 1.8% CTR (1,150 impressions) → keep, within margin
Variant C: 0.8% CTR (1,050 impressions) → KILL (< 50% of A, no improvement)
```

**Don't kill based on:**
- 1 day of data (timing/day of week affects it).
- "Feel" (personal taste).
- Comments from 3 friends.

## Scale winner vs. pivot the whole creative

After you find a winner, the critical decision: double down, or question whether the whole creative needs a pivot?

**Scale the winner when:**
- Winner has consistent ROAS > 2.5x for ≥ 3 days.
- CTR > niche average (Meta Ads B2B: > 1.5%).
- Cost per lead < 50% of LTV target.

**Pivot the whole creative when:**
- Even the winner has ROAS < 1.5x.
- All hooks have CTR < 1%.
- Multiple tests don't break through.

**Signs it's an offer problem, not a creative problem:**
- High CTR (>2%) but low conversion (<3%) — the ad copy attracts, the offer doesn't close.
- Multiple winners over months, ROAS always tight — the offer is worth 1/3 of the price; it's not the creative.

**Fix:** go back to `grand-slam-offer` or `value-equation`. A creative doesn't fix a weak offer.

## Sustainable testing cadence

Founders try to test everything in one week and burn the budget. Realistic cadence:

| Account maturity | Cadence |
|---|---|
| Early (month 1-2) | 1 hook test every 1-2 weeks (4-6 variants total/month) |
| Mid (month 3-6) | 1 hook test + 1 secondary test per week |
| Mature (month 6+) | Continuous test pipeline, 3-5 new variants/week always running |

**Principle:** tests need time to accumulate a sample. Rushing before then destroys the signal.

## Anti-patterns

**1. Killing a variant on day 1 with 200 impressions.**
The sample isn't statistical — you're watching luck.

**2. Changing 3 elements at once.**
"Changed hook + audience + CTA, CTR dropped 50%." You don't know which element did it.

**3. Not documenting what you tested.**
3 months later, you re-run the same test you already ran.

**4. Testing audience without testing the hook first.**
A perfect audience with a bad hook still gives bad CTR. Hook comes first.

**5. "I'll test everything on Instagram first."**
The platform affects everything. A hook that works on Meta Ads doesn't work on LinkedIn Ads. Test on each platform separately.

**6. Comparing your creative vs. a competitor's without the same audience.**
Different audience, different ROAS. Not comparable.

**7. Keeping a loser out of personal attachment.**
"But I like that creative." The market decides, not you.

## Test roadmap — first 90 days

**Month 1: Hook hunt**
- Week 1: 4 different dramatic hooks ($200 each = $800).
- Week 2: top 2 hooks vs. 2 new ones ($800).
- Week 3-4: refine the winning hook with micro-variations.

**Month 2: Audience hunt**
- Hook fixed (the winner).
- 3-4 different audiences (ICP-1 broad, ICP-1 narrow, ICP-2, lookalike).
- $300-500 per audience.

**Month 3: Format + CTA**
- Audience + hook fixed.
- Test 15s video vs. 30s vs. image.
- Test CTA "Get the PDF" vs. "Tell me more" vs. "Book the audit".

By the end of the 90 days, you have a solid winning combination and can scale with confidence.

## Application by use case

| Case | How to use |
|---|---|
| `/hormozi-gtm:hooks` | Output is 8-12 hooks — this skill guides how to test them (sample size, kill criteria) |
| `/hormozi-gtm:plan` for a founder running paid | Includes a test budget in the acquisition roadmap |
| ROAS tightening on campaigns → pivot or refine? | Skill helps diagnose: hook? audience? offer? |

## When it does NOT apply

- Founder before their first 50 paid leads (no data to test).
- 100% organic / referral business (doesn't run paid).
- Site conversion / pricing test → use `pricing-playbook`.

## Detailed reference

`reference/100m-leads-extracts.md` ch. 4 ("Ad Mechanics").
