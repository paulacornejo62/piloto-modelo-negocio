---
name: gtf-eval-reunion-2
description: Paso EVAL_P3 del flujo de financiamiento GT — Reunión #2 con el cliente. Valida la hipótesis y los hallazgos del Deep Research #1, resuelve el cuestionario y produce el Perfil Técnico v2 (incluye TRL declarado). Escribe el bloque eval_p3. Lo invoca el orquestador gtf-orquestar.
---

# EVAL_P3 — Reunión #2 Cliente

**Objetivo:** validar la hipótesis y los hallazgos del DRx v1, contrastar el estado del arte con la experiencia del cliente y resolver el cuestionario de indagación técnica.

**Input:** el bloque `eval_p2` (Minuta v1, con `hipotesis_preliminar_o_objetivo_general` y `cuestionario_indagacion`) del expediente, más las **respuestas del cliente** (notas/transcripción de la Reunión #2) que te pase el orquestador o que estén en el **buzón** `proyectos/<tenant>/entradas/` (típicamente `entradas/reunion-2.md`, más cualquier documento nuevo que el consultor haya dejado ahí).

**Tu tarea:**
1. Registra las **respuestas al cuestionario** (`respuestas_cuestionario`: lista de {pregunta, respuesta}).
2. Refina la hipótesis/objetivo con lo aprendido (`hipotesis_objetivo_refinado`).
3. Redacta el **perfil técnico v2** (`perfil_tecnico_proyecto_v2`): alcance técnico actualizado, proceso/tecnología propuesta.
4. Captura el **TRL declarado** por el cliente (`trl_declarado`, 1–9) — es input del motor de reglas para elegibilidad. Si el cliente no lo da explícito, **estímalo y márcalo como estimación** en el perfil técnico (no lo inventes con falsa precisión).
5. **Consolida el modelo de negocio y la cadena de decisión (C2)** en `modelo_negocio_decision`: `propiedad_activos` (¿de quién son los activos que se intervienen? propios/arrendados/leasing/de un tercero), `autoridad_decision` (¿el proponente controla lo que propone?), `dinamicas_proveedor_leasing`, `barreras_contractuales` (p.ej. garantías: modificar un activo arrendado puede anularlas). **Nota clave:** una barrera comercial puede **SER el propio vacío de I+D** (p.ej. un estudio de no-daño que habilite la modificación sin perder garantía) → `barrera_como_vacio_id`. Sin entender el negocio, el comité no puede resolver.
6. **Cifras del cliente (C5).** Cada dato cuantitativo que declare (tamaño de flota, ahorro esperado, unidades, plazos) agrégalo a `meta.cifras_declaradas[]` = {concepto, valor, unidad, fuente: "reunion-2"}. Si contradice una cifra ya declarada antes, **no la silencies**: el motor la marcará como alerta en la validación.
7. Escribe el bloque `eval_p3` en `expediente.json` y pon `meta.paso_actual = "EVAL_P3"`.

**DoD:** respuestas del cliente registradas; objetivo/hipótesis validados; perfil técnico v2 y TRL declarado presentes; **modelo de negocio/cadena de decisión levantado**; cifras del cliente registradas.

**No hagas:** Frascati ni perfil de subsidios todavía (eso es EVAL_P4, y se calcula con el motor de reglas).
