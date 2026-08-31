#!/usr/bin/env python3
"""Estado y resumen de una postulación: dónde va, qué se completó, qué sigue.

Lee el expediente del tenant y lo mapea al flujo (Fase 1 Evaluación + Fase 2
Formulación), mostrando pasos hechos, paso actual, siguiente acción y bloqueos.
Sin dependencias externas.

Uso: python3 tools/estado.py <tenant>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

SISTEMA = Path(__file__).resolve().parent.parent

# (código, etiqueta, bloque del expediente) en orden del flujo.
PASOS = [
    ("EVAL_P1", "Reunión #1 — Perfil preliminar", "eval_p1"),
    ("EVAL_P2", "Deep Research #1 + QA de veracidad", "eval_p2"),
    ("EVAL_P3", "Reunión #2 — Perfil técnico v2", "eval_p3"),
    ("EVAL_P4", "Preparar el caso — Frascati + subsidios", "eval_p4"),
    ("EVAL_P5", "Comité + compuerta", "eval_p5"),
    ("FORM_W1", "Formulación: arquitectura técnica", "form_w1"),
    ("FORM_W2", "Formulación: redacción I+D", "form_w2"),
    ("FORM_W3", "Formulación: capacidades + Gantt", "form_w3"),
    ("FORM_W4", "Formulación: admin + encuesta", "form_w4"),
    ("FORM_W5", "Formulación: QA + envío", "form_w5"),
]

SIGUIENTE = {
    "INICIO": "Pega las notas de la Reunión #1 y corre el orquestador (EVAL_P1).",
    "EVAL_P1": "Deep Research #1: investigar estado del arte (orquestador → EVAL_P2).",
    "EVAL_P2": "Agenda la Reunión #2 y registra respuestas del cliente (EVAL_P3).",
    "EVAL_P3": "Preparar el caso: Deep Research #2, Frascati y perfil de subsidios (EVAL_P4).",
    "EVAL_P4": "Presentar al comité y registrar el acta (EVAL_P5).",
    "EVAL_P5": "Según la compuerta: GO → Formulación; PIVOT → volver a EVAL_P4; NO-GO → informe al cliente.",
    "FORM_W1": "Redacción I+D según la clasificación (FORM_W2).",
    "FORM_W2": "Capacidades + Carta Gantt/Presupuesto (FORM_W3).",
    "FORM_W3": "Cumplimiento administrativo + encuesta (FORM_W4).",
    "FORM_W4": "QA de coherencia, generar documentos y enviar (FORM_W5).",
    "FORM_W5": "Postulación cerrada.",
    "ENVIADO": "✅ Postulación enviada. Generar/archivar documentos finales.",
}


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Uso: python3 tools/estado.py <tenant>")
    tenant = sys.argv[1]
    ruta = SISTEMA / "proyectos" / tenant / "expediente.json"
    if not ruta.exists():
        sys.exit(f"ERROR: no existe {ruta}")
    d = json.loads(ruta.read_text(encoding="utf-8"))
    actual = d.get("meta", {}).get("paso_actual", "INICIO")

    print(f"Postulación: {tenant}  ·  paso actual: {actual}\n")
    for code, label, bloque in PASOS:
        hecho = bloque in d
        marca = "✓" if hecho else ("▶" if code == actual else "·")
        print(f"  {marca} {code:8} {label}")
    # Compuerta
    comp = d.get("eval_p5", {}).get("compuerta")
    if comp:
        print(f"\n  Compuerta: {comp}" + ("  → Fase 2 habilitada" if comp == "GO" else ""))
    # QA de formulación
    qa = d.get("form_w5", {}).get("qa_coherencia")
    if qa:
        alertas = [r for r in qa if r.get("estado") == "alerta"]
        print(f"  QA formulación: {'⚠️ ' + str(len(alertas)) + ' alerta(s)' if alertas else '✅ sin alertas'}")
    print(f"\n  Siguiente: {SIGUIENTE.get(actual, '(definir)')}")

    bit = ruta.parent / "bitacora.md"
    if bit.exists():
        lineas = [l for l in bit.read_text(encoding="utf-8").splitlines() if l.startswith("## ")]
        if lineas:
            print(f"\n  Última sesión: {lineas[-1][3:]}")


if __name__ == "__main__":
    main()
