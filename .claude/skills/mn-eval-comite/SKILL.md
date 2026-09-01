---
name: mn-eval-comite
description: Paso EVAL_P5 del flujo de modelo de negocio — Revisión de viabilidad y compuerta. Registra la revisión del modelo (consultor o par), calcula los indicadores y la compuerta SÓLIDO/AJUSTAR/INVIABLE/DEVOLVER con el motor de reglas, y determina el flujo. Cierra la Fase 1. Escribe el bloque revision_viabilidad. Lo invoca el orquestador mn-orquestar.
---

# EVAL_P5 — Revisión de viabilidad y compuerta

**Objetivo:** revisar el modelo construido en EVAL_P4 y determinar el flujo. **La compuerta
la calcula el motor, no tú.**

**Input:** `modelo_negocio` (Canvas, `unit_economics`, `proyeccion`, `encaje_mercado`),
`investigacion_mercado.tamano_mercado`, y la **revisión** del consultor o de un par que te
pase el orquestador (o `proyectos/<tenant>/revision.md`).

**Precondición (dura):** no se puede evaluar un modelo sin sus números. Si faltan entradas
clave de unit economics o la proyección (el motor las devolvió como `sin_dato` /
`faltan_entradas`), **no fuerces una compuerta**: el desenlace es `info_suficiente = false`
→ **DEVOLVER** (paso 4).

**Tu tarea (esquema `revision_viabilidad` en `../../expediente.schema.json`):**
1. **Calcula los indicadores con el motor**:
   ```bash
   python3 -c "import sys, json; sys.path.insert(0,'motor-reglas'); import reglas; \
   ue=<modelo_negocio.unit_economics como dict>; \
   enc=<modelo_negocio.encaje_mercado como dict>; \
   print(json.dumps(reglas.indicadores_viabilidad(ue, enc), ensure_ascii=False, indent=2))"
   ```
   Guarda la lista en `indicadores[]` (`{indicador, valor, umbral, estado}`).
2. Registra `comentarios_revision[]` (observaciones del consultor / revisor par) e
   `info_suficiente` (bool; default true — ponlo en false solo si faltan datos base para
   evaluar).
3. **Calcula la compuerta con el motor**:
   ```bash
   python3 -c "import sys, json; sys.path.insert(0,'motor-reglas'); import reglas; \
   ind=<indicadores como lista>; \
   print(json.dumps(reglas.compuerta_viabilidad(ind, info_suficiente=<bool>, \
   punto_equilibrio_clp=<modelo_negocio.unit_economics.punto_equilibrio_clp>, \
   som_clp=<investigacion_mercado.tamano_mercado.som_clp>, \
   resultado_optimista_final_clp=<resultado del último año del escenario 'optimista'>), ensure_ascii=False, indent=2))"
   ```
   Guarda `compuerta` (**SÓLIDO / AJUSTAR / INVIABLE / DEVOLVER**) y los `motivos` del motor
   en `comentarios_revision`.
4. Si la compuerta es **AJUSTAR**, poblá `palancas_ajuste[]` = `{ palanca (pricing/segmento/
   canal/estructura_costos/cac/retencion/otro), hipotesis, impacto_esperado }` — **a modo de
   sugerencia**: el consultor y el cliente deciden y pueden descartar. No cambian el
   veredicto por sí solas.
5. Guarda `revision_viabilidad = {indicadores, comentarios_revision, info_suficiente,
   compuerta, palancas_ajuste}` y pon `meta.paso_actual = "EVAL_P5"`.
6. **Actúa según la compuerta:**
   - **SÓLIDO** → se habilita la **Fase 2** (redacción). Si el fondo tiene Fase 1 CORFO
     (Crea y Valida, Innova Alta Tecnología) → `mn-form-perfil`; si no → `mn-form-w1`.
   - **AJUSTAR** → vuelve a **EVAL_P4** con las `palancas_ajuste`: mover pricing / segmento /
     canal / estructura de costos y **recalcular** unit economics y proyección. Es un
     problema del modelo, no del mercado.
   - **DEVOLVER** → **info insuficiente** (faltan datos del cliente para modelar): se agenda
     **una reunión con el cliente**; cuando llegue el input a `entradas/`, se re-corre
     **EVAL_P3**. NO es AJUSTAR.
   - **INVIABLE** → el modelo no cierra ni con supuestos optimistas razonables: informe al
     cliente con los `motivos` del motor; fin del flujo.

**DoD:** indicadores y compuerta **calculados por el motor**; `palancas_ajuste` si es
AJUSTAR; acción comunicada. Valida y renderiza.

> Regla dura: no se inicia la Fase 2 (`FORM_W1`) si la compuerta no es **SÓLIDO**.
