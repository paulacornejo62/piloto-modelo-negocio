#!/usr/bin/env python3
"""Estado y resumen de un caso: dónde va, qué se completó, qué sigue.

Lee el expediente del tenant y lo mapea al flujo (Fase 1 Construcción del modelo +
Fase 2 Redacción de secciones), mostrando pasos hechos, paso actual, siguiente
acción y bloqueos. Sin dependencias externas.

Uso: python3 tools/estado.py <tenant>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):  # consola Windows (cp1252) no soporta ✓/▶
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

SISTEMA = Path(__file__).resolve().parent.parent

# (código, etiqueta, bloque del expediente) en orden del flujo.
PASOS = [
    ("EVAL_P1", "Reunión #1 — Perfil comercial", "perfil_comercial"),
    ("EVAL_P2", "Investigación de mercado + QA", "investigacion_mercado"),
    ("EVAL_P3", "Reunión #2 — Supuestos del modelo", "supuestos_modelo"),
    ("EVAL_P4", "Construir el modelo (Canvas + unit economics)", "modelo_negocio"),
    ("EVAL_P5", "Revisión de viabilidad + compuerta", "revision_viabilidad"),
    ("FORM_W1", "Redacción: arquitectura de la narrativa", "narrativa"),
    ("FORM_W2", "Redacción: formulario oficial del fondo", "formulario_oficial"),
    ("FORM_W3", "Redacción: plan de escalamiento", "plan_escalamiento"),
    ("FORM_W4", "Redacción: impacto y continuidad", "impacto_continuidad"),
    ("FORM_W5", "QA de coherencia + entrega", "qa_entrega"),
]

SIGUIENTE = {
    "INICIO": "Pega las notas de la Reunión #1 y corre el orquestador (EVAL_P1).",
    "EVAL_P1": "Investigación de mercado: tamaño, competidores, precios (orquestador → EVAL_P2).",
    "EVAL_P2": "Agenda la Reunión #2 y levanta los supuestos del modelo (EVAL_P3).",
    "EVAL_P3": "Construir el modelo: Canvas + unit economics + proyección (EVAL_P4).",
    "EVAL_P4": "Revisión de viabilidad y compuerta (EVAL_P5).",
    "EVAL_P5": "Según la compuerta: SÓLIDO → Fase 2; AJUSTAR → volver a EVAL_P4; DEVOLVER → reunión con el cliente; INVIABLE → informe al cliente.",
    "PERFIL": "Presentar el Perfil de Proyecto (Fase 1 CORFO) y esperar la retroalimentación.",
    "FORM_W1": "Redacción: formulario oficial del fondo (FORM_W2).",
    "FORM_W2": "Plan de escalamiento + proyección + hitos (FORM_W3).",
    "FORM_W3": "Impacto, continuidad y supuestos a confirmar (FORM_W4).",
    "FORM_W4": "QA de coherencia, generar documentos y entregar (FORM_W5).",
    "FORM_W5": "Caso cerrado.",
    "ENTREGADO": "✅ Paquete de modelo de negocio entregado al consultor.",
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

    print(f"Caso: {tenant}  ·  paso actual: {actual}\n")
    for code, label, bloque in PASOS:
        hecho = bloque in d
        marca = "✓" if hecho else ("▶" if code == actual else "·")
        print(f"  {marca} {code:8} {label}")
    # Compuerta de viabilidad
    comp = d.get("revision_viabilidad", {}).get("compuerta")
    if comp:
        print(f"\n  Compuerta: {comp}" + ("  → Fase 2 habilitada" if comp == "SÓLIDO" else ""))
    # QA de coherencia (Fase 2)
    qa = d.get("qa_entrega", {}).get("qa_coherencia")
    if qa:
        alertas = [r for r in qa if r.get("estado") == "alerta"]
        print(f"  QA coherencia: {'⚠️ ' + str(len(alertas)) + ' alerta(s)' if alertas else '✅ sin alertas'}")
    print(f"\n  Siguiente: {SIGUIENTE.get(actual, '(definir)')}")

    bit = ruta.parent / "bitacora.md"
    if bit.exists():
        lineas = [l for l in bit.read_text(encoding="utf-8").splitlines() if l.startswith("## ")]
        if lineas:
            print(f"\n  Última sesión: {lineas[-1][3:]}")


if __name__ == "__main__":
    main()
