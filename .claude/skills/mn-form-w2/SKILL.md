---
name: mn-form-w2
description: Paso FORM_W2 del flujo de modelo de negocio (Fase 2 — redacción). Redacta las secciones de modelo de negocio / mercado / escalamiento del FORMULARIO OFICIAL del fondo elegido (fund-aware): lee la spec en motor-reglas/formularios.json y responde solo las secciones en_alcance_piloto, fundamentándose en el modelo y la investigación de mercado verificada. Escribe el bloque formulario_oficial. Lo invoca el orquestador mn-orquestar.
---

# FORM_W2 — Redacción del formulario oficial (secciones de modelo de negocio)

**Objetivo:** redactar las **respuestas a las secciones de mercado / modelo / escalamiento
del formulario OFICIAL del fondo elegido** — no un molde genérico. Cada fondo CORFO tiene su
estructura y sus ponderadores.

**Inputs:** el **fondo elegido** (`meta.instrumento_objetivo`); `investigacion_mercado`
(tamaño de mercado, competidores, precios, benchmarks — el insumo verificado);
`modelo_negocio` (Canvas, unit economics, proyección); `narrativa` (hilo conductor); la KB.

## Paso a paso
1. **Determina el fondo** y **lee su spec**:
   ```bash
   python3 -c "import json; print(json.dumps(json.load(open('motor-reglas/formularios.json'))['fondos']['<fondo>'], ensure_ascii=False, indent=2))"
   ```
   Trae la lista de `secciones` con `titulo`, lo que hay que `incluir`, el `criterio_pct`, y
   el flag **`en_alcance_piloto`**.
2. **Redacta SOLO las secciones con `en_alcance_piloto: true`** (mercado objetivo,
   diagnóstico, novedad/diferenciación, impacto, escalabilidad, estrategia de negocio…).
   Para las `en_alcance_piloto: false` (metodología técnica, actividades de I+D, equipo),
   escribe la sección con `respuesta: ""`, `en_alcance_piloto: false` y una nota de que la
   completa el equipo GT — no las redactes.
3. Para cada sección en alcance:
   - Cubre **todo lo que pide `incluir`** (apunta a los bloques del expediente:
     `investigacion_mercado`, `modelo_negocio`, `plan_escalamiento`, `impacto_continuidad`).
   - **Sin respuestas genéricas**: cita cifras, fuentes y años del insumo verificado. Lo que
     sea supuesto, márcalo como tal.
   - Respeta el **límite de caracteres** si el fondo lo fija; deja `dentro_limite` reflejando
     la realidad.
   - **Expande cada sigla al primer uso** y suma al `glosario` los términos nuevos.
   - **CORFO evalúa sección por sección con su ponderador** (`criterio_pct`): la sección de
     mayor peso merece la redacción más cuidada.
4. **Escribe `formulario_oficial`** en el expediente: `{ fondo, secciones: [{id, titulo,
   respuesta, en_alcance_piloto, cumple_requisitos, dentro_limite}] }`. Marca
   `cumple_requisitos=true` solo si la respuesta cubre lo exigido por `incluir`.
5. **Chequea completitud**: `python3 render/render.py <tenant> --formulario` (todas las
   secciones **en alcance** presentes, no vacías, dentro del límite).

> **Guía de redacción fina por sección/fondo**: pendiente del equipo GT (`formularios.json`
> lo indica). Por ahora, redacta desde `incluir` + el `criterio_pct` + el modelo.

**Dinámica (reunión 1h):** con el cliente, validar los supuestos que sostienen las cifras de
mercado y de proyección antes de fijarlas en el formulario.

**DoD:** `formulario_oficial` con todas las secciones **en alcance del piloto** cubiertas
(`--formulario` en verde), cada una cita cifras y fuentes, sin genéricos, supuestos marcados,
validado por el cliente. `meta.paso_actual = "FORM_W2"`. Valida y renderiza.
