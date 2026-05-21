#!/usr/bin/env python3
"""
Check arquivos recém-modificados em outputs/ por padrões AI-isms residuais.

Executado como hook PostToolUse após Write/Edit. Não bloqueia — só avisa.

Critério: arquivos .md modificados há menos de 1 minuto em outputs/<tipo>/.

Padrões verificados (subset do humanizer-rules — só os mais "óbvios"):
- Vocabulário inflado (transformador, revolucionário, alavancar)
- Voz de assistente (ótima pergunta, espero ter ajudado)
- Conclusões genéricas (o futuro é promissor, marco)
- Em-dash overuse (≥ 3 num único parágrafo)
- Hedging excessivo (poderia potencialmente)
"""
from __future__ import annotations

import re
import sys
import time
from pathlib import Path

# Janela: arquivos modificados nos últimos 60 segundos
WINDOW_SECONDS = 60

# Padrões a procurar (case-insensitive) — só os mais óbvios
PATTERNS_PT = [
    (r"\btransformador(?:a|es|as)?\b", "vocabulário inflado: 'transformador'"),
    (r"\brevolucion(?:ário|ária|ar)\b", "vocabulário inflado: 'revolucionário'"),
    (r"\balavancar\b", "AI-vocab: 'alavancar'"),
    (r"\bvale ressaltar\b", "AI-filler: 'vale ressaltar'"),
    (r"\bnav(?:egar|egando)\s+(?:os |pelos )?desafios?\b", "AI-vocab: 'navegar desafios'"),
    (r"\bótima pergunta\b", "voz de assistente: 'ótima pergunta'"),
    (r"\bespero ter ajudado\b", "voz de assistente: 'espero ter ajudado'"),
    (r"\bsinta-se à vontade\b", "voz de assistente: 'sinta-se à vontade'"),
    (r"\b(?:o futuro é promissor|caminhos brilhantes pela frente)\b", "conclusão genérica AI"),
    (r"\bé um marco\b", "inflated significance: 'é um marco'"),
    (r"\bpoderia potencialmente\b", "hedging excessivo: 'poderia potencialmente'"),
    # Removidos por taxa alta de falso positivo em PT-BR:
    # - 'inovador': PT-BR usa substantivo→adjetivo ('produto inovador'), regex tinha lookahead invertido
    # - 'mergulhar': contextos figurativos legítimos ('mergulhar no projeto') predominam
]

PATTERNS_EN = [
    (r"\btransformative\b", "inflated vocab: 'transformative'"),
    (r"\brevolutionary\b(?!\s+(?:war|france))", "inflated vocab: 'revolutionary'"),
    (r"\bgroundbreaking\b", "inflated vocab: 'groundbreaking'"),
    (r"\bdelve into\b", "AI-vocab: 'delve into'"),
    (r"\btapestry\b", "AI-vocab figurative: 'tapestry'"),
    (r"\bstands as a testament\b", "AI-phrase: 'stands as a testament'"),
    (r"\bnavigate the\b", "AI-vocab: 'navigate the'"),
    (r"\bI hope this helps\b", "assistant voice: 'I hope this helps'"),
    (r"\bgreat question\b", "assistant voice: 'great question'"),
    (r"\bfeel free to\b", "assistant voice: 'feel free to'"),
]


def find_recent_outputs(root: Path) -> list[Path]:
    """Retorna .md em outputs/ modificados nos últimos WINDOW_SECONDS."""
    outputs = root / "outputs"
    if not outputs.is_dir():
        return []
    now = time.time()
    files: list[Path] = []
    for md in outputs.rglob("*.md"):
        try:
            if now - md.stat().st_mtime < WINDOW_SECONDS:
                files.append(md)
        except OSError:
            continue
    return files


def scan_emdash_overuse(text: str) -> list[str]:
    """Detecta parágrafos com 3+ em-dashes (overuse típico AI)."""
    hits: list[str] = []
    for i, para in enumerate(text.split("\n\n"), start=1):
        if para.count("—") >= 3:
            hits.append(f"parágrafo {i}: {para.count('—')} em-dashes")
    return hits


def scan_file(path: Path) -> list[tuple[int, str]]:
    """Lê o arquivo e retorna lista de (linha, descrição do padrão)."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []
    hits: list[tuple[int, str]] = []
    # Pula frontmatter
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end > 0:
            body_start = end + 4
            body = text[body_start:]
            offset_lines = text[:body_start].count("\n")
        else:
            body = text
            offset_lines = 0
    else:
        body = text
        offset_lines = 0
    # Padrões inline
    for pattern, label in PATTERNS_PT + PATTERNS_EN:
        for m in re.finditer(pattern, body, re.IGNORECASE):
            line_no = body[: m.start()].count("\n") + 1 + offset_lines
            hits.append((line_no, label))
    # Em-dash overuse
    for note in scan_emdash_overuse(body):
        hits.append((-1, f"em-dash overuse — {note}"))
    return hits


MAX_HITS_PER_FILE = 20


def main() -> int:
    cwd = Path.cwd()
    files = find_recent_outputs(cwd)
    if not files:
        return 0
    any_hits = False
    for path in files:
        hits = scan_file(path)
        if not hits:
            continue
        any_hits = True
        rel = path.relative_to(cwd)
        print(f"\n⚠️  AI-isms residuais em {rel}:")
        shown = hits[:MAX_HITS_PER_FILE]
        for line, label in shown:
            loc = f"linha {line}" if line > 0 else "global"
            print(f"   [{loc}] {label}")
        if len(hits) > MAX_HITS_PER_FILE:
            suppressed = len(hits) - MAX_HITS_PER_FILE
            print(f"   ... (+{suppressed} hits suprimidos — re-rode humanizer)")
    if any_hits:
        print(
            "\n→ Considere re-rodar humanizer ou editar manualmente "
            "(humanizer_pass: false até resolver).\n"
        )
    return 0  # nunca bloqueia


if __name__ == "__main__":
    sys.exit(main())
