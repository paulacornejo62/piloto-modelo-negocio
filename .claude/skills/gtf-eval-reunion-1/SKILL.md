---
name: gtf-eval-reunion-1
description: Paso EVAL_P1 del flujo de financiamiento GT — Reunión #1 con el cliente. Toma la declaración inicial del cliente (transcripción, notas o texto libre) y produce el Perfil Preliminar (7 campos tipados). Escribe el bloque eval_p1 en el expediente.json del tenant. Lo invoca el orquestador gtf-orquestar.
---

# EVAL_P1 — Reunión #1 Cliente

**Objetivo:** obtener el contexto comercial de la empresa y levantar a grandes rasgos el problema, oportunidad y resultados que dan origen al proyecto. Es captura estructurada, NO evaluación técnica todavía.

**Input:** la declaración inicial del cliente (transcripción / notas / texto libre) en el **buzón** `proyectos/<tenant>/entradas/` — típicamente `entradas/reunion-1.md`, más **cualquier otro documento** que el consultor haya dejado ahí (specs, estudios previos, PDFs). Revisa la carpeta `entradas/` completa, no solo un archivo. (O el texto que te pase el orquestador.)

**Tu tarea:**
1. Lee la entrada del cliente.
2. Extrae y estructura el **Perfil Preliminar** con estos campos (esquema en `../../expediente.schema.json`, bloque `eval_p1`):
   - `empresa_razon_social`
   - `empresa_tamano`: una de Micro / Pequeña / Mediana / Grande. Además `empresa_tamano_confirmado` (bool): `true` **solo** si el cliente lo confirmó o es claramente determinable; si lo infieres, ponlo en `false` — queda como **supuesto** (determina el % de cofinanciamiento; hay que confirmarlo, no asumirlo en silencio).
   - `empresa_fecha_inicio_actividades`
   - `contacto_clave`: { nombre, cargo, email }
   - `proyecto_presupuesto_estimado`: número en CLP — **obligatorio captarlo**
   - `problema_oportunidad_declarado`: texto libre (contexto general)
   - `resultado_esperado_negocio`: texto libre — el resultado de **negocio/técnico** esperado. **NO metadata de tramitación** (fechas límite de Corfo, timing del beneficio tributario): no es relevante para la evaluación. El **fondo objetivo** (p.ej. "es para Ley I+D") va en `meta.instrumento_objetivo`, no aquí.
   - `historia_previa` (C4): **no trates el caso como "primera postulación sin historia".** Del buzón `entradas/` y de lo que diga el cliente, captura `postulaciones_o_evaluaciones_previas`, `alcance_original` y `alcance_descartado_y_por_que`. **Reconcilia los cambios de alcance**: lo que se sacó (por costo/riesgo/"no era financiable") suele ser donde vivía el I+D — vale la pena recuperarlo y preguntarlo.
3. **Semillas del modelo de negocio (C2).** Aunque el bloque `modelo_negocio_decision` se consolida en la Reunión #2 (`eval_p3`), si en la Reunión #1 aparecen señales de **quién decide, de quién son los activos, o barreras contractuales** (leasing, garantías), anótalas para arrastrarlas — no las pierdas.
4. Si un dato no está en la entrada, **no lo inventes**: déjalo vacío y anótalo como pregunta pendiente para el cliente (en `resultado_esperado_negocio` o donde aplique, marcado `[POR CONFIRMAR]`).
5. Escribe el bloque `eval_p1` en `proyectos/<tenant>/expediente.json` y pon `meta.paso_actual = "EVAL_P1"`, `meta.actualizado` con la fecha que te dé el orquestador.

**Criterio de salida (DoD):** Perfil Preliminar con ≥80% de los campos comerciales y descripción básica del problema redactada. **Es obligatorio** haber captado el presupuesto preliminar (o marcarlo explícito `[POR CONFIRMAR]` si el cliente no lo dio).

**No hagas:** análisis Frascati, estado del arte ni recomendación de instrumento. Eso es de pasos posteriores.
