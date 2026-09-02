#!/usr/bin/env python3
"""Bitácora de sesiones por caso: guarda y lista avances.

Cada entrada queda en `proyectos/<tenant>/bitacora.md` con fecha, para retomar
el trabajo sin releer todo. Sin dependencias externas.

Uso:
    python3 tools/bitacora.py registrar <tenant> "Qué se hizo" ["detalle opcional"]
    python3 tools/bitacora.py listar <tenant>
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

for _s in (sys.stdout, sys.stderr):  # consola Windows (cp1252) no soporta emojis/guiones
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

SISTEMA = Path(__file__).resolve().parent.parent


def _ruta(tenant: str) -> Path:
    base = SISTEMA / "proyectos" / tenant
    if not base.exists():
        sys.exit(f"ERROR: no existe el proyecto {tenant}")
    return base / "bitacora.md"


def registrar(tenant: str, resumen: str, detalle: str = "") -> None:
    bit = _ruta(tenant)
    if not bit.exists():
        bit.write_text(f"# Bitácora — {tenant}\n\n", encoding="utf-8")
    entrada = f"## {date.today().isoformat()} — {resumen}\n"
    if detalle:
        entrada += f"\n{detalle}\n"
    entrada += "\n"
    with bit.open("a", encoding="utf-8") as f:
        f.write(entrada)
    print(f"Registrado en {bit}")


def listar(tenant: str) -> None:
    bit = _ruta(tenant)
    if not bit.exists():
        print("(sin bitácora todavía)")
        return
    print(bit.read_text(encoding="utf-8"))


def main() -> None:
    a = sys.argv
    if len(a) >= 4 and a[1] == "registrar":
        registrar(a[2], a[3], a[4] if len(a) > 4 else "")
    elif len(a) == 3 and a[1] == "listar":
        listar(a[2])
    else:
        sys.exit('Uso: bitacora.py registrar <tenant> "resumen" ["detalle"] | listar <tenant>')


if __name__ == "__main__":
    main()
