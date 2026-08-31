#!/usr/bin/env python3
"""Panel de la cartera: todas las postulaciones con su estado de un vistazo.

Recorre proyectos/<tenant>/expediente.json y resume paso actual, compuerta y
última sesión. Sin dependencias externas.

Uso: python3 tools/panel.py
"""
from __future__ import annotations

import json
from pathlib import Path

SISTEMA = Path(__file__).resolve().parent.parent
PROY = SISTEMA / "proyectos"

ORDEN = ["INICIO", "EVAL_P1", "EVAL_P2", "EVAL_P3", "EVAL_P4", "EVAL_P5",
         "FORM_W1", "FORM_W2", "FORM_W3", "FORM_W4", "FORM_W5", "ENVIADO"]


def _ultima_sesion(carpeta: Path) -> str:
    bit = carpeta / "bitacora.md"
    if bit.exists():
        ls = [l[3:] for l in bit.read_text(encoding="utf-8").splitlines() if l.startswith("## ")]
        if ls:
            return ls[-1][:40]
    return "—"


def main() -> None:
    if not PROY.exists():
        print("(sin proyectos)")
        return
    filas = []
    for carpeta in sorted(PROY.iterdir()):
        exp = carpeta / "expediente.json"
        if not exp.is_file():
            continue
        d = json.loads(exp.read_text(encoding="utf-8"))
        m = d.get("meta", {})
        paso = m.get("paso_actual", "INICIO")
        try:
            avance = f"{ORDEN.index(paso)}/{len(ORDEN) - 1}"
        except ValueError:
            avance = "?"
        comp = d.get("eval_p5", {}).get("compuerta", "")
        emp = d.get("eval_p1", {}).get("empresa_razon_social", "")
        filas.append((carpeta.name, emp, paso, avance, comp, _ultima_sesion(carpeta)))

    if not filas:
        print("(sin postulaciones)")
        return
    print(f"{'PROYECTO':16} {'EMPRESA':22} {'PASO':9} {'AVANCE':7} {'COMP':6} ÚLTIMA SESIÓN")
    for n, emp, paso, av, comp, ses in filas:
        print(f"{n:16} {emp[:22]:22} {paso:9} {av:7} {comp:6} {ses}")
    print(f"\n{len(filas)} postulación(es).")


if __name__ == "__main__":
    main()
