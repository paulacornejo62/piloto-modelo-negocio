---
name: gtf-eval-comite
description: Paso EVAL_P5 del flujo de financiamiento GT — Comité de pares y compuerta. Registra el acta del comité (voto, comentarios, instrumento) y calcula la compuerta GO/PIVOT/NO-GO con el motor de reglas. Cierra la Fase 1 (Evaluación). Lo invoca el orquestador gtf-orquestar.
---

# EVAL_P5 — Comité y compuerta

**Objetivo:** registrar el dictamen del comité de pares sobre el caso (láminas de EVAL_P4) y determinar el flujo.

**Input:** `eval_p4` (Frascati con `es_id`/`es_id_defendible`, exclusiones, perfil de subsidios, `reencuadre_elegibilidad[]`), `eval_p3.modelo_negocio_decision`, y el **acta/decisión del comité** que te pase el orquestador (o `proyectos/<tenant>/acta-comite.md`).

**Precondición (C2, dura):** el comité **no puede resolver sin entender el negocio**. Antes de registrar el voto, verifica que `eval_p3.modelo_negocio_decision` esté poblado (propiedad de activos, quién decide, barreras contractuales). Si falta lo esencial, **no fuerces un voto**: el desenlace es `info_suficiente = false` → compuerta **DEVOLVER** (paso 4).

**Tu tarea:**
1. Registra el acta + **estrategia de postulación**: `voto_comite` (Aprobado I+D / Rechazado I+D / Condicionado a Ajustes / **Información Insuficiente**), `comentarios_tecnicos[]`, `info_suficiente` (bool), `aplica_ley_id` (booleano), `instrumento_corfo_seleccionado` (de los elegibles en `eval_p4.perfil_subsidios`), `enfoque_postulacion`.
   - Si `eval_p4.frascati.es_id_defendible` es **false**, el comité debe pronunciarse sobre eso: o rechaza (no es I+D), o **condiciona** al reencuadre. **No trates un falso positivo como I+D sólido.**
   - Cuando el caso sea débil, presenta el `reencuadre_elegibilidad[]` **como sugerencias** (C3) — el comité y el cliente deciden; no las impongas ni cambies el veredicto por ellas.
2. **Calcula la compuerta con el motor** (no la decidas tú):
   ```bash
   python3 -c "import sys; sys.path.insert(0,'motor-reglas'); import reglas; print(reglas.compuerta(es_id=<es_id>, voto_comite='<voto>', info_suficiente=<bool>))"
   ```
   (usa el `es_id` de `eval_p4.frascati`, el `voto_comite` y `info_suficiente`).
3. Guarda `eval_p5 = {voto_comite, comentarios_tecnicos, info_suficiente, aplica_ley_id, instrumento_corfo_seleccionado, enfoque_postulacion, compuerta}` y pon `meta.paso_actual = "EVAL_P5"`.
4. **Actúa según la compuerta:**
   - **GO** → informa que se habilita la **Fase 2: Formulación** (FORM_W1…W5).
   - **PIVOT** → el caso vuelve a EVAL_P4 (Deep Research #2) con los comentarios del comité — es un problema de **estado del arte** (falta evidencia técnica).
   - **DEVOLVER** (C6) → **info insuficiente**: se agenda **una reunión con el cliente** para completar el entendimiento (típicamente del modelo de negocio), **NO** un nuevo Deep Research. No es PIVOT.
   - **NO-GO** → se notifica al cliente con informe técnico de por qué no aplica (y, si aplica, las sugerencias de reencuadre); fin del flujo.

**DoD:** acta registrada, compuerta calculada por el motor, y la acción correspondiente comunicada. Valida y renderiza.

> Regla dura (Índice Maestro): no se inicia FORM_W1 si la compuerta no es **GO**.
