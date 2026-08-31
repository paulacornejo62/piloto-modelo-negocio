#!/usr/bin/env bash
# Setup del sistema GTF — deja el tool listo para usar en una máquina nueva.
# Idempotente: se puede correr varias veces. Ejecutar desde la raíz del sistema:
#   bash setup/setup.sh
set -euo pipefail

cd "$(dirname "$0")/.."   # raíz del sistema (sistema/)
echo "== Setup GTF =="

# 1. Prerrequisitos (con guía si falta)
command -v python3 >/dev/null || { echo "FALTA Python 3. Instálalo: https://www.python.org/downloads/ (o 'brew install python3')."; exit 1; }
command -v node    >/dev/null || { echo "FALTA Node (para el navegador del Deep Research). Instálalo: https://nodejs.org (o 'brew install node')."; exit 1; }
command -v npx     >/dev/null || { echo "FALTA npx (viene con Node). Reinstala Node: https://nodejs.org"; exit 1; }
echo "ok: python3 $(python3 --version 2>&1 | awk '{print $2}'), node $(node --version), npx $(npx --version)"

# 2. Dependencias Python en un entorno virtual (.venv)
#    Usamos venv para no tocar el Python del sistema y evitar el bloqueo PEP 668
#    (Homebrew/Debian rechazan 'pip install' global). No-fatal: el flujo básico
#    funciona aunque esto falle (render.py valida en modo simple sin jsonschema).
echo "-- entorno Python (.venv) + dependencias --"
if python3 -m venv .venv 2>/dev/null && .venv/bin/pip install -q -r setup/requirements.txt; then
  echo "ok: .venv + dependencias Python"
else
  echo "AVISO: no se pudo crear el .venv o instalar deps; el flujo básico funciona igual (validación en modo simple)."
fi

# 3. Dependencias Node (Playwright) + navegador para el Deep Research
echo "-- instalando dependencias Node (Playwright) --"
npm install --silent && echo "ok: npm"
echo "-- instalando Chromium para Playwright (puede tardar / ~100MB) --"
npx --yes playwright install chromium && echo "ok: chromium"

# 4. poppler (pdftotext) — aviso si falta
command -v pdftotext >/dev/null && echo "ok: pdftotext" || \
  echo "AVISO: pdftotext no encontrado (PDFs escaneados). Instalar poppler si se requiere ingesta de PDF."

# 5. MCP del navegador presente
[ -f .mcp.json ] && echo "ok: .mcp.json (Playwright MCP)" || echo "AVISO: falta .mcp.json"

# 6. Smoke test del render/validación (usa el .venv si existe; si no, python3 con fallback)
echo "-- smoke test --"
PY=python3; [ -x .venv/bin/python ] && PY=.venv/bin/python
"$PY" render/render.py _ejemplo --validar && echo "ok: validación del expediente _ejemplo"

echo ""
echo "== Setup completo =="
echo "Próximos pasos:"
echo "  1) Abre la herramienta:   claude        (desde esta carpeta, sistema/)"
echo "  2) Empieza una postulación, escríbele:  «Nuevo proyecto de financiamiento para [Empresa]»"
echo "  3) Guía de uso completa:  GUIA-USUARIO.md"
