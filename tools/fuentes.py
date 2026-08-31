#!/usr/bin/env python3
"""Registro de fuentes de consulta (papers/patentes) — fácil de manejar.

Lee `tools/fuentes.json`. Permite ver todas las fuentes, solo las usables, o
validar el archivo. Para AGREGAR una fuente, edita `fuentes.json` (no este script).

Uso:
    python3 tools/fuentes.py listar       # todas, por categoría y estado
    python3 tools/fuentes.py usables       # solo las que el Deep Research puede recorrer ahora
    python3 tools/fuentes.py validar       # chequea el JSON
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

CFG = Path(__file__).resolve().parent / "fuentes.json"
USABLES = {"activo", "parcial", "intermitente"}
ICONO = {"activo": "✅", "parcial": "🟡", "intermitente": "🟡", "requiere_key": "🔑", "bloqueado": "⛔", "manual": "✋"}


def _cargar() -> dict:
    return json.loads(CFG.read_text(encoding="utf-8"))


def listar(solo_usables: bool = False) -> None:
    d = _cargar()
    for cat in ("papers", "patentes"):
        print(f"\n== {cat.upper()} ==")
        for f in d.get(cat, []):
            est = f.get("estado", "?")
            if solo_usables and est not in USABLES:
                continue
            print(f"  {ICONO.get(est,'·')} {f['nombre']:28} [{est}]  {f.get('como','')}")
            if f.get("nota"):
                print(f"       ↳ {f['nota']}")
    if not solo_usables:
        print("\nLeyenda: ✅ activo · 🟡 parcial · 🔑 requiere key (configurar en .mcp.json) · ⛔ bloqueado · ✋ manual")
        print("Agregar/activar una fuente: edita tools/fuentes.json")


def resumen() -> None:
    from collections import Counter
    d = _cargar()
    for cat in ("papers", "patentes"):
        fuentes = d.get(cat, [])
        cnt = Counter(f.get("estado", "?") for f in fuentes)
        usables = sum(v for k, v in cnt.items() if k in USABLES)
        print(f"{cat:9}: {len(fuentes)} fuentes · {usables} usables ahora · {dict(cnt)}")
    print("Editar/agregar fuentes: tools/fuentes.json · Activar API/MCP (key): sistema/.mcp.json")


def validar() -> None:
    d = _cargar()
    req = {"id", "nombre", "tipo", "estado"}
    errs = []
    for cat in ("papers", "patentes"):
        for f in d.get(cat, []):
            faltan = req - set(f)
            if faltan:
                errs.append(f"{cat}/{f.get('id','?')}: faltan {faltan}")
    if errs:
        print("INVÁLIDO:"); [print("  -", e) for e in errs]; sys.exit(1)
    print("OK: fuentes.json válido.")


def main() -> None:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "listar"
    if cmd == "usables":
        listar(solo_usables=True)
    elif cmd == "validar":
        validar()
    elif cmd == "resumen":
        resumen()
    else:
        listar()


if __name__ == "__main__":
    main()
