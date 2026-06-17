---
name: humanizer-rules
description: Full Humanizer ruleset in English and PT-BR — the list of AI writing patterns to strip and what to replace them with. Always run as the last step of the pipeline before saving external copy. Operating base for the humanizer subagent.
---

# Humanizer Rules

Source: Wikipedia *Signs of AI writing* (WikiProject AI Cleanup) + PT-BR adaptation + LEVEL brand voice.

This file keeps both English and Portuguese pattern lists. Generated copy follows the `language` set in gtm-context (default English), so the humanizer has to catch AI-isms in whichever language the output ships in. The two lists are detection data — keep them intact in both languages.

## Principle

AI-generated text carries 8-12 repetitive patterns that wreck commercial credibility. Stripping them isn't a style choice — it's basic hygiene for copy that goes to a client.

## Full list of patterns to strip

### 1. Inflated / promotional vocabulary

**English:**
- transformative, revolutionary, groundbreaking, pivotal, paradigm-shifting
- delve, navigate, tapestry, foster, harness, leverage (as a verb)
- robust, comprehensive, seamless, cutting-edge, state-of-the-art
- empowering, unparalleled, world-class

**Português:**
- transformador, revolucionário, inovador, pivotal, disruptor
- mergulhar (em sentido figurado), navegar pelos desafios, alavancar
- robusto, abrangente, sem fricção, de ponta, último em tecnologia
- empoderador, sem precedentes, classe mundial

**Replacement:** use the concrete verb that says what it does, with a number when you can.

### 2. Stacked -ing phrases / PT-BR gerunds

**English:**
- "...by leveraging X, highlighting Y, and reinforcing Z"
- "...emphasizing", "showcasing", "underscoring", "underlining"
- "Helping to streamline..."

**Português:**
- "...destacando X, contribuindo para Y, reforçando Z"
- "Buscando entregar...", "Visando garantir...", "Procurando otimizar..."
- "Sendo assim", "Estando alinhado"

**Replacement:** break into short sentences with a real verb. "It shows", "it guarantees", "it aligns."

### 3. Vague attributions

**English:**
- "Experts say...", "Studies show...", "Research indicates..."
- "It is widely known that...", "Many believe..."

**Português:**
- "Especialistas dizem...", "Estudos mostram...", "Pesquisas indicam..."
- "É amplamente sabido...", "Muitos afirmam...", "Há quem diga..."

**Replacement:** name the specific source OR cut the claim. No source, no claim.

### 4. Negative parallelism

**English:**
- "It's not just X, it's Y"
- "More than just X, it's Y"

**Português:**
- "Não é só X, é Y"
- "Mais do que X, é Y"
- "Não se trata apenas de X, mas de Y"

**Replacement:** state what it is, straight. "It's Y." No parallelism.

### 5. Rule of three — specific vs vague

Rule of three isn't banned by default. Hormozi uses it when each item carries real information. The test: **if you can drop any one of the three without losing information, it's vague — cut it.**

**Ban (disguised synonyms, decorative):**

EN:
- "fast, simple, and effective"
- "innovative, scalable, and impactful"

PT:
- "rápido, simples e eficaz"
- "inovador, escalável e impactante"
- "estratégico, eficiente e disruptivo"

**Keep (each item a discrete entity, carrying its own weight):**

EN:
- "3 weeks, 3 emails, 3 case studies"
- "8 commands, 16 skills, 7 agents"
- "Silver, Gold, Platinum"

PT:
- "3 semanas, 3 e-mails, 3 cases"
- "ICP, oferta, canal" (3 distinct entities in the framework)
- "Attraction, Core, Continuity" (named levels of the money model)

**Replacement for the vague ones:** pick ONE adjective, back it with concrete proof. "Effective: cuts CAC by 38%." Drop the decorative triple.

### 6. Generic conclusions

**English:**
- "The future is bright", "Exciting times ahead", "Stands as a testament to"
- "In a rapidly evolving landscape...", "In today's fast-paced world..."

**Português:**
- "O futuro é promissor", "Caminhos brilhantes pela frente"
- "É um marco", "Representa um divisor de águas"
- "Em um mundo em constante transformação...", "Na era digital..."

**Replacement:** cut the whole sentence. A conclusion with no fact is noise.

### 7. Em-dash overuse

An em-dash (—) used more than once per paragraph is an AI tell.

**Replacement:** comma, period, colon, parentheses.

### 8. Excessive hedging

**English:**
- "It could potentially be argued that..."
- "Some may consider..."
- "It seems to suggest..."

**Português:**
- "Poderia potencialmente ser considerado que..."
- "Há quem possa argumentar..."
- "Aparenta sugerir que..."

**Replacement:** state it straight. If you're not sure, say "I think", not "it could be argued".

### 9. Chatbot voice

**English:**
- "Great question!", "I hope this helps!", "Feel free to ask anytime"
- "Absolutely!", "Certainly!", "Of course!"

**Português:**
- "Ótima pergunta!", "Espero ter ajudado!", "Sinta-se à vontade"
- "Com certeza!", "Claro!", "Sem dúvida!"

**Replacement:** delete it whole. Go straight to the answer.

### 10. Over-formal conjunctions

**English:**
- "Furthermore", "Moreover", "In addition", "Additionally"
- "However", "Nevertheless", "Nonetheless"
- "In summary", "In conclusion", "It is important to note that"

**Português:**
- "Ademais", "Outrossim", "Adicionalmente", "Vale ainda destacar"
- "No entanto, vale ressaltar", "Cabe destacar", "Em suma", "Em conclusão"
- "É importante notar que", "Convém mencionar"

**Replacement:** "But", "also", "on top of that" (sparingly), or a fresh sentence with no formal connector.

### 11. Empty adjectives

**English:** crucial, essential, vital, key, critical (in excess)
**Português:** crucial, essencial, vital, chave, fundamental

**Replacement:** if everything is crucial, nothing is. Reserve it for 1-2 uses in a long piece.

### 12. Vague metrics

**English:** "significant improvement", "substantial growth", "considerable impact"
**Português:** "melhoria significativa", "crescimento substancial", "impacto considerável"

**Replacement:** a concrete number. "Up 34%" instead of "up significantly".

## Authentic Hormozi voice vs AI-simulacra

Some patterns **look** like AI but are the signature of the Hormozi voice when they're backed by something real. The humanizer has to tell them apart before it prunes.

### Keep (authentic Hormozi voice)

**1. Direct imperative.**
- "Charge more. Deliver more. Repeat." — sounds AI-prescriptive on its own, but it's the Hormozi rhythm when proof rides with it ("I watched 17 SaaS companies test this").
- Keep when: there's proof/a number before or after. Cut when: it's a free-floating directive with nothing under it.

**2. Lists of three with real entities.**
- "ICP, offer, channel" → keep (3 discrete concepts in the framework, each carries information).
- "agile, scalable, and robust" → cut (disguised synonyms, decorative).

**3. "Strong" words with proof next to them.**
- "This destroys your CAC" → keep if a number follows ("CAC dropped from $450 to $180 in 90 days").
- "This destroys your CAC" with no number → cut (it becomes empty hype).

**4. Counterintuitive / contrarian framing.**
- "It's not the ad, it's the SDR script" → keep (Hormozi lives on this; it opens a curiosity gap).
- Cut only when the contrarian doesn't hold up ("It's not X, it's Y" with no explanation of why Y is the root).

**5. Command voice aimed at "you".**
- "You underprice because you're scared the market will say no" → keep (first-person Hormozi, direct diagnosis).
- Cut when it slides into assistant-in-disguise: "You may want to consider raising your prices."

**6. CTA-as-command and the hammer line.** NEVER soften.
- "Install your pipeline channel." / "Stop burning pipeline." → keep (a command, not an invitation). Don't turn it into "Book your free audit" — that's banned, not a refinement.
- "Two likes. One's your co-founder." / "Waiting isn't a channel. It's hope." → keep (hammer-line fragment, Hormozi rhythm). Don't fuse it into one polite "complete" sentence.

**7. Aggressive specificity (the bite).** An insult or diagnosis with proof under it — "a coward's offer", "pricing that apologizes for existing", "any intern could've written that" → keep when there's an anchor (number/case/deadline). Cutting this kills the voice; it isn't AI-ism cleanup.

### Cut (AI-simulacra dressed as Hormozi)

**1. False authority with no number.**
- "I've seen this a thousand times" → too vague, sounds AI-inflated. Swap for "I saw it in 14 B2B SaaS companies over the last 18 months" or cut.

**2. Generalization with no real client.**
- "Every founder deals with this" → AI-ism. Hormozi would say "a B2B SaaS founder with $500k-5M ARR deals with this; the one at $50M is already past it."

**3. Generic heroic conclusion.**
- "The rest is just execution" / "Now you just do it" → sounds Hormozi but it's an AI decoy. Hormozi closes on a specific next action: "Next step: run the audit before you touch pricing."

### How to decide on the spot

Ask before you cut: **does the line have proof next to it, or is it floating?** A Hormozi line has an anchor (number, name, deadline, case). AI-simulacra of Hormozi has none.

### Soft input: cleaning isn't enough

Stripping AI-isms does NOT add bite — soft copy with the AI-isms removed is still soft. If the draft arrives SOFT (a generic CTA like "book an audit", a feature/metaphor headline like "a bulletproof pipeline channel", no confrontation, no number, no risk reversal), score it on the brutality rubric in the `hormozi-voice` skill. If it's **<7**: rewrite with bite OR emit `humanizer_pass: false` with a note "input has no Hormozi bite — return to persona/ad-architect". Don't ship lukewarm copy just because it's clean of AI-isms.

## Patterns to INJECT

### Varied rhythm
Short sentences. Long sentences that build tension before they resolve. Mix them.

### Specificity
Replace:
- "many" → "12"
- "quickly" → "in 47 days"
- "a big company" → "Salesforce"
- "high cost" → "$1,200/mo"

### Real opinion
Instead of neutrality, a reaction:
- "This doesn't work in B2B." (a flat claim)
- "I thought it was weird until I tested it with 3 clients." (personal)
- "It runs against what I'd have said 3 years ago." (shows evolution)

### First-person voice
When the content is Hormozi-mode: "I...", "We...", "What I saw across 12 clients..."

### Honest imperfection
- "This probably doesn't hold for every niche"
- "There's a client where we screwed it up and lost the contract"
- "Theory says X, but in practice Y happens 30% of the time"

## Scope: external copy only

The humanizer runs **only on external client copy** (lp, script, hooks, email, case-study, webinar, content pieces, winback). There it applies the WHOLE list.

Internal/diagnostic output (audit, review, plan, pricing, objections, positioning, churn analysis, onboarding) **does not pass through the humanizer** — it ships raw, brutal Hormozi, unfiltered. Those go out with `humanizer_pass: false` / `humanizer_mode: n/a`.

> The `lite` mode was discontinued in v1.0. There's no "partial humanizer" anymore: either it's external copy (full), or it's internal (raw, no humanizer).

## When NOT to humanize

- `--no-humanize` flag passed (debug, A/B comparison)
- Content is pure technical (code, JSON, YAML)
- Inline comments and short docstrings
- Tool outputs / logs

## Humanizer workflow

1. Read the whole text
2. Find the 3-5 worst offenders
3. Rewrite keeping the content, removing the patterns
4. Read it aloud in your head — does it sound human?
5. Check specificity — wherever there's a "many", swap in a number
6. Return only the clean text. No commentary.

## Reference

Henrique's original humanizer skill: `~/.claude/skills/humanizer/SKILL.md`. This SKILL.md is the version embedded in the plugin, with the PT-BR-specific expansion.
