---
name: mn-form-w2
description: Paso FORM_W2 del flujo de financiamiento GT (Formulación, Semana 2). Redacta el FORMULARIO OFICIAL del fondo elegido (fund-aware): lee la spec del fondo en motor-reglas/formularios.json y responde cada sección/pregunta fundamentándose en el insumo del Deep Research. Escribe el bloque formulario_oficial. Lo invoca el orquestador mn-orquestar.
---

# FORM_W2 — Redacción del formulario oficial del fondo (Semana 2)

**Objetivo:** redactar las **respuestas al formulario OFICIAL del fondo elegido** — no un molde genérico. Cada fondo tiene su estructura (Ley I+D = 6 preguntas de certificación de I+D; CORFO = secciones por criterios de evaluación). El insumo del Deep Research **se mantiene** (arriba); esto **agrega** abajo las respuestas oficiales.

**Inputs:** el **fondo elegido** (`meta.instrumento_objetivo` o el instrumento que fijó el comité en `eval_p5`); `eval_p2`/`eval_p4` (estado del arte, hallazgos verificados = el insumo); `form_w1` (título/objetivo); la KB.

## Paso a paso
1. **Determina el fondo** y **lee su spec**: `python3 -c "import json; print(json.dumps(json.load(open('motor-reglas/formularios.json'))['fondos']['<fondo>'], ensure_ascii=False, indent=2))"`. Trae la lista de `secciones` con su `titulo`, lo que hay que `incluir`, el `limite` de caracteres y (CORFO) el `criterio_pct`.
2. **Redacta cada sección** fundamentándote en el insumo (estado del arte verificado, hallazgos de la KB, datos del expediente). Para cada una:
   - Cubre **todo lo que pide `incluir`** (p.ej. Ley I+D Q1 exige causas + efectos + **dimensión en cifras** + fuentes; Q5 exige atributos **cuantificados vs industria NACIONAL**).
   - Respeta el **límite de caracteres**.
   - **Sin respuestas genéricas**; cita cifras y fuentes del insumo.
   - **Expande cada sigla al primer uso** y suma al `glosario` cualquier término del área nuevo que introduzcas (regla 8 del CLAUDE.md): el consultor que revisa el formulario puede no ser experto en el tema.
   - Omite las secciones con `solo_si_tipo` que no apliquen a este fondo/proyecto (mecanismo genérico del schema). En Ley I+D, la sección "incertidumbre" (Q11) tiene `solo_si_tipo: "informatico"`: el texto oficial de la pregunta es literalmente "Mencione la incertidumbre científico-tecnológica que se ve resuelta **por el desarrollo informático**" — aplica solo cuando el proyecto tiene un componente de desarrollo informático/software, no a todo Desarrollo Experimental. **Historial del error (para no repetirlo):** el 20/21-ago-2026, en edelpa-megaproyecto-a, se quitó esta restricción por error tras una investigación que concluyó (incorrectamente) que "informático" era solo la redacción genérica de Corfo — se redactó y se incluyó Q11 en un proyecto de materiales/extrusión sin componente informático. El 26-ago-2026 el cliente/consultora detectó el error releyendo el texto literal de la pregunta; se restauró `solo_si_tipo` y se quitó Q11 de ese expediente. Si `meta.tipo_proyecto` no contiene la palabra "informático", **Q11 no se responde**.
3. **Escribe `formulario_oficial`** en el expediente: `{ fondo, secciones: [{id, titulo, respuesta, cumple_requisitos}] }`. Marca `cumple_requisitos=true` solo si la respuesta cubre lo exigido.
4. **Chequea completitud**: `python3 render/render.py <tenant> --formulario` (todas las secciones del fondo presentes, no vacías, dentro del límite).

> **CORFO:** las respuestas deben mapear a los **criterios evaluados** (con su ponderador) — el evaluador califica sección por sección. Foco en mercado/negocio/escalamiento/capacidades, no solo I+D.
> **Ley I+D:** las 6 preguntas certifican que hay I+D (Frascati); las reglas QA 3 (nuevo conocimiento nace del estado del arte) y 4 (incertidumbre) se evalúan en FORM_W5.
> **Guía de redacción fina por pregunta:** existe para **Ley I+D** (`desarrollo/contexto/fuentes/preguntas_formulario_i+d.md`). Para los CORFO, redacta desde `incluir` + los criterios (la guía fina por fondo es mejora futura).

**Dinámica (reunión 1h):** entrevistar al cliente sobre desarrollos previos/fallidos, variables críticas, indicadores; validar supuestos.

**DoD:** `formulario_oficial` completo para el fondo (`--formulario` en verde), cada sección cubre sus requisitos, sin genéricos, validado por el cliente. `meta.paso_actual = "FORM_W2"`. Valida y renderiza.
