#!/usr/bin/env bash
# Empacota o plugin hormozi-gtm em ZIP pronto para upload no Claude Cowork.
# Roda do diretório raiz do repo.
set -euo pipefail

cd "$(dirname "$0")/.."

if [ ! -f ".claude-plugin/plugin.json" ]; then
  echo "::error:: .claude-plugin/plugin.json não encontrado. Rode do diretório raiz do repo." >&2
  exit 1
fi

VERSION=$(python3 -c "import json; print(json.load(open('.claude-plugin/plugin.json'))['version'])")
OUT="hormozi-gtm-v${VERSION}.zip"

rm -f "$OUT"

zip -r "$OUT" \
  .claude-plugin \
  agents \
  commands \
  skills \
  hooks \
  templates \
  reference \
  README.md \
  CHANGELOG.md \
  LICENSE \
  -x "*.DS_Store" "*/.git/*" "*/outputs/*" "*/__pycache__/*" \
  > /dev/null

SIZE=$(du -h "$OUT" | cut -f1)
echo "✓ ${OUT} (${SIZE})"
