#!/usr/bin/env python3
"""Genera la planilla Plan de Trabajo (Carta Gantt + Presupuesto) desde el expediente.

Produce un .xlsx **estructurado como el formato oficial CORFO** (hojas Desafíos,
Gantt I+D, Presupuesto RRHH), pre-poblado con lo que hay en `form_w3` / `eval_p4`.
NO es la planilla macro oficial: es un **insumo de arranque** que el consultor
traspasa/valida en el archivo oficial. Requiere openpyxl (en el .venv del setup).

Uso: python3 render/gantt.py <tenant>   (mejor con .venv/bin/python)
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

import openpyxl
from openpyxl.styles import Font

SISTEMA = Path(__file__).resolve().parent.parent
NEG = Font(bold=True)


def _ym(s: str):
    """'2026-03-01' / '2026-03' → (año, mes) o None."""
    try:
        partes = str(s)[:10].replace("/", "-").split("-")
        return int(partes[0]), int(partes[1])
    except Exception:
        return None


def _meses(ini, fin):
    """Lista de (año, mes) entre dos (año,mes) inclusive."""
    out, y, m = [], ini[0], ini[1]
    while (y, m) <= fin:
        out.append((y, m))
        m = 1 if m == 12 else m + 1
        y = y + 1 if m == 1 else y
    return out


def construir(datos: dict, destino: Path) -> None:
    w3 = datos.get("form_w3", {})
    wb = openpyxl.Workbook()

    # --- Hoja Desafíos Tecnológicos ---
    ws = wb.active
    ws.title = "Desafíos Tecnológicos"
    ws.append(["N°", "Nombre del desafío", "Por qué es incierto (incertidumbre)", "Por qué lo superaremos (enfoque)"])
    for c in ws[1]:
        c.font = NEG
    desafios = datos.get("form_w3", {}).get("desafios_tecnologicos", []) or []
    if desafios:
        for d in desafios:
            ws.append([d.get("n", ""), d.get("nombre", ""),
                       d.get("por_que_incierto", ""), d.get("por_que_superable", "")])
    else:
        ws.append(["1", "(completar)", datos.get("eval_p4", {}).get("desafios_tecnicos_consolidados", ""), ""])

    # --- Hoja Gantt I+D ---
    actividades = w3.get("actividades", []) or []
    g = wb.create_sheet("Gantt I+D")
    rangos = [(_ym(a.get("fecha_inicio")), _ym(a.get("fecha_fin"))) for a in actividades]
    rangos = [(i, f) for i, f in rangos if i and f]
    cols_mes = []
    if rangos:
        ini = min(i for i, _ in rangos)
        fin = max(f for _, f in rangos)
        cols_mes = _meses(ini, fin)
    encabezado = ["N°", "Objetivo", "Actividad", "Desafío", "Inicio", "Fin"] + [f"{y}-{m:02d}" for y, m in cols_mes]
    g.append(encabezado)
    for c in g[1]:
        c.font = NEG
    for a in actividades:
        fila = [a.get("n", ""), a.get("objetivo", ""), a.get("nombre", ""), a.get("desafio_n", ""),
                a.get("fecha_inicio", ""), a.get("fecha_fin", "")]
        i, f = _ym(a.get("fecha_inicio")), _ym(a.get("fecha_fin"))
        for (y, m) in cols_mes:
            fila.append("X" if (i and f and i <= (y, m) <= f) else "")
        g.append(fila)
    if not actividades:
        g.append(["(sin actividades en el expediente — completar form_w3.actividades)"])

    # --- Hoja Presupuesto RRHH ---
    pr = wb.create_sheet("Presupuesto RRHH")
    pr.append(["Empresa", "Cuenta", "Nombre", "Función", "Valor HH", "N° horas", "Total (CLP)"])
    for c in pr[1]:
        c.font = NEG
    empresa = datos.get("eval_p1", {}).get("empresa_razon_social", "")
    total = 0
    for p in w3.get("personal_asociado", []) or []:
        vhh = p.get("valor_hh") or 0
        hh = p.get("horas") or 0
        sub = round(vhh * hh)
        total += sub
        pr.append([empresa, p.get("cuenta", ""), p.get("nombre", ""), p.get("funcion", ""), vhh, hh, sub])
    r = pr.max_row + 1
    pr.cell(r, 6, "TOTAL RRHH (por HH×horas)").font = NEG
    pr.cell(r, 7, total).font = NEG

    # Resumen de presupuesto (totales confirmados por el cliente)
    presu = w3.get("presupuesto", {}) or {}
    desg = presu.get("desglose", {}) or {}
    if desg or presu.get("total_clp"):
        pr.append([])
        pr.append(["RESUMEN PRESUPUESTO (totales confirmados)"])
        pr.cell(pr.max_row, 1).font = NEG
        pr.append(["Ítem", "Monto (CLP)"])
        for c in pr[pr.max_row]:
            c.font = NEG
        for k, v in desg.items():
            pr.append([k, v])
        if presu.get("total_clp"):
            pr.append(["TOTAL", presu["total_clp"]])
            for c in pr[pr.max_row]:
                c.font = NEG

    for sh in wb.worksheets:
        for col in sh.columns:
            sh.column_dimensions[col[0].column_letter].width = 18

    wb.save(destino)


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Uso: python3 render/gantt.py <tenant>")
    tenant = sys.argv[1]
    ruta = SISTEMA / "proyectos" / tenant / "expediente.json"
    if not ruta.exists():
        sys.exit(f"ERROR: no existe {ruta}")
    destino = ruta.parent / "plan-trabajo.xlsx"
    construir(json.loads(ruta.read_text(encoding="utf-8")), destino)
    print(f"Generado: {destino} (insumo de arranque; traspasar al formato oficial)")


if __name__ == "__main__":
    main()
