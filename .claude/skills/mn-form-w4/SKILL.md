---
name: mn-form-w4
description: Paso FORM_W4 del flujo de modelo de negocio (Fase 2 — redacción). Impacto, continuidad y supuestos a confirmar: impacto esperado (económico, social, ambiental), estrategia de continuidad y captura de valor post-subsidio, y el registro explícito de los supuestos del modelo que el cliente aún debe confirmar. Escribe el bloque impacto_continuidad. Lo invoca el orquestador mn-orquestar.
---

# FORM_W4 — Impacto, continuidad y supuestos a confirmar

**Objetivo:** cerrar el relato de negocio: qué impacto genera el proyecto, cómo se sostiene
después del subsidio, y qué supuestos quedan pendientes de confirmar antes de presentar.

**Inputs:** `modelo_negocio` (proyección, unit economics), `plan_escalamiento` (hitos,
metas), `supuestos_modelo.supuestos` (los que están `confirmado: false`),
`investigacion_mercado`.

**Productos (`impacto_continuidad`):**
- `impacto_esperado`: `{ economico (ingresos incrementales, ahorro, empleos — con cifras de
  la proyección del escenario base), social, ambiental }`. Números del modelo, no promesas.
- `estrategia_continuidad`: cómo se sostiene el negocio después del subsidio — fuente de
  ingresos, captura de valor, cómo se protege lo desarrollado. Coherente con los unit
  economics: si el modelo cierra (compuerta SÓLIDO), aquí se explica por qué se sostiene solo.
- `riesgos_barreras[]`: `{ riesgo, mitigacion }` — de mercado, de ejecución, regulatorios.
- `supuestos_a_confirmar[]`: **arrastra** cada supuesto de `supuestos_modelo.supuestos` con
  `confirmado: false`, como `{ supuesto, seccion_afectada (qué sección del formulario
  depende de él), responsable_confirmar (cliente/consultor) }`. Es un proyecto de
  innovación: este registro es parte del entregable, no una debilidad a esconder. El
  consultor lo usa para cerrar los pendientes con el cliente antes de presentar.

**Dinámica (reunión 1h):** con el cliente, revisar el impacto comprometido (que sea
alcanzable con la proyección) y repasar la lista de supuestos a confirmar.

**DoD:** impacto con cifras del modelo; estrategia de continuidad coherente con los unit
economics; riesgos con mitigación; **todos** los supuestos no confirmados listados con su
sección afectada y responsable. `meta.paso_actual = "FORM_W4"`. Valida y renderiza.
