---
name: gtf-form-w4
description: Paso FORM_W4 del flujo de financiamiento GT (Formulación, Semana 4). Cumplimiento administrativo: sistema financiero contable, encuesta de caracterización (fase, innovación, Ley REP, certificaciones) y cálculo de arancel. Escribe el bloque form_w4. Lo invoca el orquestador gtf-orquestar.
---

# FORM_W4 — Cumplimiento Administrativo y Encuesta (Semana 4)

**Objetivo:** validar el sistema contable, completar la encuesta de caracterización y calcular el arancel.

**Inputs:** respuestas comerciales/sostenibilidad del cliente, captura del ERP/sistema contable.

**Productos (`form_w4`):**
- `nombre_sistema_contable` (SAP, Softland, Defontana, Jepsen…) y `verificacion_sistema_contable` (captura/PDF que muestra **centros de costo** — requisito de la Ley I+D para segregar el proyecto).
- `registro_encuesta_ley_id`:
  - `fase_proyecto_actual`: [Concepto / Prototipo / Prototipo Funcional / PMV / Producto Funcional / Escalando en ventas] → entra a la **regla QA 1** (coherencia TRL↔fase).
  - `tipo_innovacion_principal`, `alcance_innovacion`, `numero_usuarios_actuales`, `numero_clientes_actuales`, `modelo_negocio_ingresos`.
  - `metas_valorizacion_ley_rep[]`, `certificaciones_ambientales_empresa[]`.
- `arancel_utm` / `arancel_clp`: **cálculalo con el motor**, no a ojo: `python3 motor-reglas/reglas.py --arancel <utm_proyecto>`, donde `utm_proyecto = costo_total_clp / valor_utm_clp` (el valor UTM del mes vive en `instrumentos.json` → `ley_id.arancel.valor_utm_clp`; **verifica que sea el del mes de la postulación**, cambia mensualmente). La escala es por tramos con **tope 30 UTM** — NO es un 4% del costo. Guarda `arancel_utm`, `arancel_clp` y el `tramo_utm` que devuelve el motor.
  - _Nota (JP, GT): el arancel es un **dato administrativo menor**, no un driver de decisión — regístralo, pero no lo sobre-pongas en el análisis ni las láminas._

**Dinámica (reunión 1h):** validar sistema contable, completar caracterización socioambiental/género, calcular arancel.

**DoD:** sistema contable validado y arancel calculado listo para facturación/pago. `meta.paso_actual = "FORM_W4"`. Valida y renderiza.
