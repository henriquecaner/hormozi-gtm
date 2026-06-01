---
description: Regras completas do Humanizer em PT-BR e EN — lista de padrões AI a remover e substituições. Use sempre como último passo do pipeline antes de salvar output externo. Base de operação do subagent humanizer.
---

# Humanizer Rules

Fonte: Wikipedia *Signs of AI writing* (WikiProject AI Cleanup) + adaptação PT-BR + brand voice LEVEL.

## Princípio

Texto AI tem 8-12 padrões repetitivos que comprometem credibilidade comercial. Removê-los não é estilo — é higiene básica de copy que vai pro cliente.

## Lista completa de padrões a remover

### 1. Vocabulário inflado / promotional

**Inglês:**
- transformative, revolutionary, groundbreaking, pivotal, paradigm-shifting
- delve, navigate, tapestry, foster, harness, leverage (como verbo)
- robust, comprehensive, seamless, cutting-edge, state-of-the-art
- empowering, unparalleled, world-class

**Português:**
- transformador, revolucionário, inovador, pivotal, disruptor
- mergulhar (em sentido figurado), navegar pelos desafios, alavancar
- robusto, abrangente, sem fricção, de ponta, último em tecnologia
- empoderador, sem precedentes, classe mundial

**Substituições:** use o verbo concreto que descreve o que faz, com número quando possível.

### 2. Frases com -ing empilhadas / gerúndios PT-BR

**Inglês:**
- "...by leveraging X, highlighting Y, and reinforcing Z"
- "...emphasizing", "showcasing", "underscoring", "underlining"
- "Helping to streamline..."

**Português:**
- "...destacando X, contribuindo para Y, reforçando Z"
- "Buscando entregar...", "Visando garantir...", "Procurando otimizar..."
- "Sendo assim", "Estando alinhado"

**Substituições:** quebra em frases curtas com verbo no infinitivo ou conjugado. "Mostra", "garante", "alinha".

### 3. Atribuições vagas

**Inglês:**
- "Experts say...", "Studies show...", "Research indicates..."
- "It is widely known that...", "Many believe..."

**Português:**
- "Especialistas dizem...", "Estudos mostram...", "Pesquisas indicam..."
- "É amplamente sabido...", "Muitos afirmam...", "Há quem diga..."

**Substituições:** nomeia a fonte específica OU remove a afirmação. Sem fonte, sem alegação.

### 4. Paralelismo negativo

**Inglês:**
- "It's not just X, it's Y"
- "More than just X, it's Y"

**Português:**
- "Não é só X, é Y"
- "Mais do que X, é Y"
- "Não se trata apenas de X, mas de Y"

**Substituições:** afirma direto o que é. "É Y." Sem o paralelismo.

### 5. Rule of three — específico vs vago

Rule of three NÃO é proibido por padrão. Hormozi usa rule of three quando cada item carrega informação real. O critério: **se você consegue remover qualquer um dos três sem perder informação, é vago e some**.

**Banir (sinônimos disfarçados, decorativo):**

EN:
- "fast, simple, and effective"
- "innovative, scalable, and impactful"

PT:
- "rápido, simples e eficaz"
- "inovador, escalável e impactante"
- "estratégico, eficiente e disruptivo"

**Aceitar (cada item é entidade discreta, com peso próprio):**

EN:
- "3 weeks, 3 emails, 3 case studies"
- "8 commands, 16 skills, 7 agents"
- "Silver, Gold, Platinum"

PT:
- "3 semanas, 3 e-mails, 3 cases"
- "ICP, oferta, canal" (3 entidades distintas do framework)
- "Attraction, Core, Continuity" (níveis nomeados do money model)

**Substituições para os vagos:** escolhe UM adjetivo, sustenta com prova concreta. "Eficaz: reduz CAC em 38%." Sem o tríplice decorativo.

### 6. Conclusões genéricas

**Inglês:**
- "The future is bright", "Exciting times ahead", "Stands as a testament to"
- "In a rapidly evolving landscape...", "In today's fast-paced world..."

**Português:**
- "O futuro é promissor", "Caminhos brilhantes pela frente"
- "É um marco", "Representa um divisor de águas"
- "Em um mundo em constante transformação...", "Na era digital..."

**Substituições:** corta a frase inteira. Conclusão sem fato é ruído.

### 7. Em-dash overuse

Em-dash (—) usado mais de 1x por parágrafo é marca de AI.

**Substituições:** vírgula, ponto-final, dois pontos, parênteses.

### 8. Hedging excessivo

**Inglês:**
- "It could potentially be argued that..."
- "Some may consider..."
- "It seems to suggest..."

**Português:**
- "Poderia potencialmente ser considerado que..."
- "Há quem possa argumentar..."
- "Aparenta sugerir que..."

**Substituições:** afirma direto. Se você não tem certeza, diz "eu acho", não "poderia ser argumentado".

### 9. Linguagem de chatbot

**Inglês:**
- "Great question!", "I hope this helps!", "Feel free to ask anytime"
- "Absolutely!", "Certainly!", "Of course!"

**Português:**
- "Ótima pergunta!", "Espero ter ajudado!", "Sinta-se à vontade"
- "Com certeza!", "Claro!", "Sem dúvida!"

**Substituições:** remove inteiro. Vai direto pra resposta.

### 10. Conjunções formais demais

**Inglês:**
- "Furthermore", "Moreover", "In addition", "Additionally"
- "However", "Nevertheless", "Nonetheless"
- "In summary", "In conclusion", "It is important to note that"

**Português:**
- "Ademais", "Outrossim", "Adicionalmente", "Vale ainda destacar"
- "No entanto, vale ressaltar", "Cabe destacar", "Em suma", "Em conclusão"
- "É importante notar que", "Convém mencionar"

**Substituições:** "Mas", "também", "além disso" (uso comedido), ou frase nova sem conector formal.

### 11. Adjetivos vazios

**Inglês:** crucial, essential, vital, key, critical (em excesso)
**Português:** crucial, essencial, vital, chave, fundamental

**Substituições:** se tudo é crucial, nada é. Reserva pra 1-2 usos por texto longo.

### 12. Métricas vagas

**Inglês:** "significant improvement", "substantial growth", "considerable impact"
**Português:** "melhoria significativa", "crescimento substancial", "impacto considerável"

**Substituições:** número concreto. "Aumentou 34%" em vez de "aumentou significativamente".

## Voz Hormozi autêntica vs AI-simulacra

Há padrões que **parecem** AI mas são marca registrada da voz Hormozi quando usados com lastro real. O humanizer precisa diferenciar antes de podar.

### Manter (voz Hormozi autêntica)

**1. Imperativo direto.**
- "Cobra mais. Entrega mais. Repete." — soa AI-prescriptive isolado, mas é o ritmo Hormozi quando vem acompanhado de prova ("vi 17 SaaS testarem isso").
- Manter quando: há prova/número antes ou depois. Cortar quando: é diretriz solta sem lastro.

**2. Listas de 3 com entidades reais.**
- "ICP, oferta, canal" → manter (3 conceitos discretos do framework, cada um carrega informação).
- "ágil, escalável e robusto" → cortar (sinônimos disfarçados, decorativo).

**3. Palavras "fortes" com prova adjacente.**
- "Isso destrói o CAC" → manter se vier seguido de número ("CAC caiu de R$ 450 pra R$ 180 em 90 dias").
- "Isso destrói o CAC" sem número → cortar (vira hype vazio).

**4. Contraintuitivo / contrarian framing.**
- "Não é o anúncio, é o SDR script" → manter (Hormozi vive disso, gera curiosity gap).
- Cortar somente se o contrarian não sustenta ("Não é X, é Y" sem explicação do porquê Y é a raiz).

**5. Voz de comando com "você".**
- "Você cobra pouco porque tem medo do mercado falar não" → manter (1ª pessoa Hormozi, diagnóstico direto).
- Cortar quando vira assistente travestido: "Você pode considerar aumentar seus preços".

**6. CTA-ordem e frase-martelo.** NUNCA amaciar.
- "Instale seu canal de pipeline." / "Para de queimar pipeline." → manter (ordem, não convite). Não transformar em "Agende seu diagnóstico gratuito" — isso é proibido, não refinamento.
- "Dois likes. Um é do seu sócio." / "Esperar não é canal. É torcida." → manter (fragmento-martelo, ritmo Hormozi). Não fundir em frase "completa" educada.

**7. Especificidade agressiva (a presa).** Insulto/diagnóstico com lastro — "oferta covarde", "preço de quem pede desculpa por existir", "qualquer estagiário escreveria" → manter quando há âncora (número/caso/prazo). Cortar isso é matar a voz, não limpar AI-ism.

### Cortar (AI-simulacra disfarçado de Hormozi)

**1. Falsa autoridade sem número.**
- "Já vi isso milhares de vezes" → muito vago, soa AI inflado. Trocar por "vi em 14 SaaS B2B nos últimos 18 meses" ou cortar.

**2. Generalização sem cliente real.**
- "Todo founder enfrenta isso" → AI-isms. Hormozi diria "founder de SaaS B2B com ARR entre 500k-5M enfrenta isso, founder com 50M já passou".

**3. Conclusão genérica heroica.**
- "O resto é executar" / "Agora é só fazer" → soa Hormozi mas é AI-decoy. Hormozi fecha com next action específica: "Próximo passo: roda audit antes de mexer no pricing".

### Como decidir na hora

Pergunta antes de cortar: **a frase tem prova adjacente ou está flutuando?** Frase Hormozi tem âncora (número, nome, prazo, caso). AI-simulacra de Hormozi não tem.

### Input mole: limpar não basta

Remover AI-ism NÃO adiciona presa — copy mole limpa continua mole. Se o rascunho chegar MOLE (CTA genérico tipo "agende diagnóstico", headline de feature/metáfora tipo "canal de pipeline blindado", sem confronto, sem número, sem reversão de risco), pontue na rubrica de brutalidade da skill `hormozi-voice`. Se **<7**: reescreve com presa (modo full) OU emite `humanizer_pass: false` com nota "input sem presa Hormozi — devolver à persona/ad-architect". Não entregue copy morna só porque está sem AI-ism.

## Padrões a INJETAR

### Ritmo variado
Frases curtas. Frases longas que constroem tensão antes de resolver. Mistura.

### Especificidade
Substitui:
- "muitos" → "12"
- "rapidamente" → "em 47 dias"
- "uma grande empresa" → "Vivo"
- "alto custo" → "R$ 1.200/mês"

### Opinião real
Em vez de neutralidade, reação:
- "Isso não funciona em B2B." (afirmativo)
- "Achei estranho até testar com 3 clientes." (pessoal)
- "Vai contra o que eu diria há 3 anos." (mostra evolução)

### Voz em 1ª pessoa
Quando o conteúdo é Hormozi-mode: "Eu...", "A gente...", "O que eu vi com 12 clientes..."

### Imperfeição honesta
- "Isso provavelmente não vale pra todo nicho"
- "Tem cliente onde a gente errou e quebrou contrato"
- "A teoria diz X, mas na prática Y acontece 30% das vezes"

## Versão "lite" vs "full"

- **Lite (outputs internos:** audit, review, plano): remove só em-dash overuse, rule of three e AI vocab. Mantém tom direto Hormozi cru.
- **Full (outputs externos pra cliente:** LP, ad, hooks, business plan): aplica TODA a lista.

Comando que invoca humanizer passa flag indicando qual versão.

## Quando NÃO humanizar

- `--no-humanize` flag passada (debug, comparação A/B)
- Conteúdo é técnico puro (código, JSON, YAML)
- Comments inline e docstrings curtos
- Tool outputs / logs

## Workflow do humanizer

1. Lê o texto inteiro
2. Identifica os 3-5 piores ofensores
3. Reescreve mantendo conteúdo, removendo padrões
4. Lê em voz alta mentalmente — soa humano?
5. Verifica especificidade — onde há "muitos", troca por número
6. Devolve só o texto limpo. Sem comentário.

## Referência

Humanizer skill original do Henrique: `~/.claude/skills/humanizer/SKILL.md`. Este SKILL.md é a versão embarcada no plugin com expansão PT-BR específica.
