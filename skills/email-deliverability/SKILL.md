---
name: email-deliverability
description: Cold/warm email deliverability — domain warm-up (4-6 weeks), SPF/DKIM/DMARC setup, reputation management, antispam triggers to avoid. Complements /hormozi-gtm:email. For a founder about to launch outbound at scale (50+ emails/day) who doesn't want to burn the main domain.
---

# Email Deliverability

Source: Alex Hormozi, *$100M Leads* (Ch. 3, "Cold Outreach") + deliverability literature (Lemlist, Smartlead, Instantly playbooks).

## Why this skill exists

`sales-sequencing` teaches the 5-touch sequence. `/hormozi-gtm:email` generates the copy. This one covers the technical layer underneath: **the email actually landing in the inbox**. Genius copy in the spam folder converts zero.

A founder will often fire 200 cold emails from the main corporate Gmail, burn the reputation in 7 days, then discover that every sales email (including warm) lands in spam for 3-6 months.

## The 3 pillars of deliverability

### 1. Authentication (SPF + DKIM + DMARC)

**SPF** (Sender Policy Framework) — authorizes which servers can send email on behalf of your domain.

**DKIM** (DomainKeys Identified Mail) — digitally signs each email. The inbox provider validates that the email is genuine.

**DMARC** (Domain-based Message Authentication, Reporting, and Conformance) — the policy for what to do with emails that fail SPF/DKIM (reject, quarantine, or let through).

**Minimum acceptable setup (before any outbound):**
- SPF record configured and valid.
- DKIM active on the email provider (Google Workspace, Microsoft 365, ProtonMail).
- DMARC with policy `p=quarantine` (at minimum) or `p=reject` (ideal).

**Diagnostic:** run `mxtoolbox.com` or `mail-tester.com` on your domain. A score < 8/10 = mandatory fixes before cold outreach.

### 2. Domain warm-up (4-6 weeks)

A new domain, or one idle for > 90 days, needs warm-up before sending volume.

**Warm-up cadence without an automated tool:**

| Week | Emails/day | Type | Audience |
|---|---|---|---|
| 1 | 5-10 | Real conversational (reply expected) | Close network |
| 2 | 15-25 | Conversational + 1-2 warm emails | Network + referrals |
| 3 | 30-50 | Mix of warm/transactional | Your own opt-in list |
| 4 | 50-80 | + 10 highly segmented cold emails | Add first prospects |
| 5 | 80-120 | + cold scaling | Qualified cold list |
| 6 | 100-200 | Operational volume | Segmented cold list |

**Principle:** every warm-up email needs to **generate a human response** (reply, click, open). The inbox provider measures engagement, not volume.

**Automated warm-up tools:** Lemlist Warmup, Mailwarm, Warmbox, Folderly. They run for 4-8 weeks in parallel with your normal use. Cost: $80-300/mo per domain.

### 3. Domain & inbox strategy

**Critical rule:** **never** run cold outreach from your main production domain.

**Recommended setup:**
- Main domain: `company.com` (transactional email, support, warm communication with clients).
- Outbound domains: `getcompany.com`, `trycompany.com`, `company.io` (registered close to the main one, pointing to the site but sending outbound).
- 2-4 inboxes per outbound domain, each sending 30-50 emails/day max.

**Capacity math:**

```
3 secondary domains × 3 inboxes/domain × 40 emails/day = 360 emails/day
~10,800 emails/month without burning reputation
```

Want to send 500/day? You need 4-5 domains or a multi-inbox tool like Smartlead/Instantly.

## Antispam triggers — what to avoid

### Subject-line triggers

Avoid classic spam words (filtered by Bayes). These are the words that trip *English* spam filters — localize the list per target language:
- "Free", "100%", "Guaranteed", "Urgent", "Act now", "Winner", "Limited time", "Special offer", "Risk-free"
- Caps lock on any word ("OPPORTUNITY", "URGENT")
- Too many exclamation points (≥2 !!)
- Emojis in the subject (varies by provider; Outlook is more sensitive)
- Excessive punctuation (?? !! ...)

### Body triggers

- Heavy HTML / design templates (B2B cold email should be plain text)
- Multiple links (1 link is OK, 3+ raises the spam score)
- Images (≥ 1 image in a B2B cold email raises a flag)
- Attachments (an attachment in the first email = almost always spam)
- A non-functional "Unsubscribe" (cold outreach needs a working opt-out link, or it gets marked spam when the prospect tries to leave)
- A large corporate footer (logo + address + social icons = picks up a "mass promotion" flag)

### Behavior triggers

- Sending velocity > 80 emails/inbox/day → flagged as bulk
- Bounce rate > 5% → reputation drops (clean the list first)
- Complaint rate > 0.3% → reputation burns fast
- Reply rate < 1% → the algorithm reads it as "nobody wants this email"
- The exact same message sent to >50 prospects → flagged as a spam pattern

## Metrics that matter

| Metric | Target | What it measures |
|---|---|---|
| **Deliverability rate** | ≥ 95% | % of emails that land (didn't bounce) |
| **Inbox placement** | ≥ 85% | % landing in the inbox (not spam) — GlockApps or Mail-tester |
| **Bounce rate** | < 3% | Is the list clean? |
| **Open rate** | ≥ 35% | Subject + sender reputation |
| **Reply rate** | ≥ 5% | Is the whole sequence working? |
| **Complaint rate** | < 0.1% | Reputation preserved |

Warning signs:
- Open rate dropping week after week → reputation running out.
- Bounce rate > 5% → bought or outdated list (kill it).
- High reply rate + dropping open rate → the spam folder caught you.

## Recovery plan if the domain burned

Signs of a burned domain:
- Inbox placement < 50% (test with mail-tester.com).
- Cold open rate drops from 40% to 15% with no change in copy.
- Warm clients complaining they don't receive your emails.

**Recovery (4-8 weeks):**
1. **Stop all outbound** on the burned domain for 30 days.
2. **Run automated warm-up** in parallel (Lemlist Warmup, Mailwarm) — generates a high conversational reply rate.
3. **Check blacklists** (Spamhaus, Barracuda, Sorbs) via mxtoolbox. If you're on one, request removal.
4. **Reinstall SPF/DKIM/DMARC** if there was drift.
5. **Reintroduce volume gradually** (week 5-8): 10 → 30 → 80 → 200 emails/day.

**If the main domain is burned:** consider abandoning it for outbound, keeping it only for transactional, and registering a new domain for outbound.

## Technical setup (operational sequence)

**Week 0:**
- Register 2-3 secondary domains similar to the main one.
- Configure each: SPF, DKIM, DMARC.
- Buy an inbox on each (Google Workspace ~$35/mo each).
- Set up a simple signature (name + title + 1 line).

**Week 1-4:** automated warm-up in parallel (Lemlist Warmup or similar).

**Week 5+:** start real outbound respecting the cadence.

## Anti-patterns

- Cold outreach from the main domain (burns everything).
- Buying a ready-made list (bounce > 20%, burns reputation in 48h).
- Using a single inbox for 200+ emails/day (flagged as bulk).
- Skipping warm-up ("I've used this email for years") — casual use ≠ outbound.
- A colorful HTML template in cold (looks like marketing automation, goes to the promotions tab).
- Multiple CTAs / links in a cold email (always 1 link).
- Not checking Mail-tester before each new campaign.
- Continuing to send to bouncebacks (burns reputation cumulatively).

## Application by use case

| Case | How to use |
|---|---|
| `/hormozi-gtm:email --type=cold` before launching | Skill guides the technical setup before the first campaign |
| `/hormozi-gtm:plan` with a Core Four split high in cold (>30%) | Plan includes setup of 2-3 secondary domains + warm-up budget |
| Reply rate dropping with no change in copy | Diagnosis: deliverability problem, not a copy problem |

## When it does NOT apply

- Outbound 100% via LinkedIn DM (doesn't use email).
- Volume < 20 emails/day (can use the main domain if warm).
- 100% inbound business (no cold outreach).

## Detailed reference

`reference/100m-leads-extracts.md` ch. 3 ("Cold Outreach") + external deliverability literature (not included in the plugin).
