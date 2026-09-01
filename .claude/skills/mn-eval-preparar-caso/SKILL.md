---
name: mn-eval-preparar-caso
description: Paso EVAL_P4 del flujo de modelo de negocio — Construir el modelo. Consolida el Business Model Canvas y prepara las ENTRADAS de unit economics, tamaño de mercado y proyección; el motor de reglas calcula las SALIDAS (margen de contribución, LTV, LTV/CAC, payback, punto de equilibrio, proyección por escenarios, penetración de SOM). Escribe el bloque modelo_negocio. Lo invoca el orquestador mn-orquestar.
---

# EVAL_P4 — Construir el modelo

**Las decisiones numéricas las calcula el motor de reglas, no tú.** Tu trabajo es
consolidar el Canvas y **preparar entradas limpias y trazables** para el motor.

**Input:** `perfil_comercial` (qué se vende, estado de desarrollo, tamaño de empresa),
`investigacion_mercado` (tamaño de mercado, competidores, precios, benchmarks) y
`supuestos_modelo` (segmentos, ingresos, costos, CAC, supuestos).

> **Escritura para el consultor.** El caso lo lee alguien que puede no ser experto en el
> rubro ni en modelos de negocio. Expande toda sigla al primer uso y **puebla el `glosario`**
> del expediente la primera vez que uses un término de negocio (CAC, LTV, margen de
> contribución, TAM/SAM/SOM, payback, churn) o del rubro — `{termino, sigla, definicion}` en
> lenguaje llano.

## Subetapa I — (opcional) profundizar el mercado
Si al construir el modelo detectas un hueco en la investigación (falta un sub-mercado, un
competidor clave, un precio de referencia), lanza un **`mn-deep-researcher`** acotado a esa
brecha y córrele **`mn-qa-veracidad`** encima. Alimenta la KB con lo nuevo (`mn-kb-agregar`).
No repitas toda la investigación: solo cierra el hueco.

## Subetapa II — Business Model Canvas
Consolida `modelo_negocio.canvas` (9 bloques) desde `supuestos_modelo` +
`investigacion_mercado`, en texto llano: `segmentos_cliente`, `propuesta_valor`, `canales`,
`relacion_clientes`, `fuentes_ingreso`, `recursos_clave`, `actividades_clave`,
`socios_clave`, `estructura_costos`. Cada afirmación debe rastrearse a un supuesto o a un
hallazgo verificado; lo que sea aspiración, márcalo.

## Subetapa III — Unit economics (motor)
1. Define la **unidad del modelo** (`unit_economics.unidad_modelo`): un cliente/mes, una
   transacción, un equipo vendido. Todo lo demás se interpreta respecto de ella.
2. Prepara las **ENTRADAS** desde `supuestos_modelo` (consistentes con la unidad):
   `precio_unitario`, `costo_variable_unitario`, `costos_fijos_mensuales`, `cac_clp`,
   `vida_cliente_meses` (para pago único → 1).
3. **Calcula las SALIDAS con el motor** (no las estimes tú):
   ```bash
   python3 -c "import sys, json; sys.path.insert(0,'motor-reglas'); import reglas; \
   print(json.dumps(reglas.unit_economics(precio_unitario=<P>, costo_variable_unitario=<CV>, \
   costos_fijos_mensuales=<CF>, cac_clp=<CAC>, vida_cliente_meses=<V>), ensure_ascii=False, indent=2))"
   ```
   Copia a `modelo_negocio.unit_economics` las salidas (`margen_contribucion_unitario`,
   `margen_contribucion_pct`, `ltv_clp`, `ltv_cac_ratio`, `payback_cac_meses`,
   `punto_equilibrio_unidades`, `punto_equilibrio_clp`). Si el motor devuelve
   `faltan_entradas`, consíguelas o márcalas `[POR CONFIRMAR]` — no inventes un número para
   que "cierre".

## Subetapa IV — Proyección por escenarios (motor)
1. Fija `meta.horizonte_proyeccion_anios` según el fondo y el caso (típ. 3-5) si no está.
2. Arma `proyeccion.escenarios[]` = pesimista / base / optimista. Cada uno: ENTRADAS
   `supuestos_crecimiento` (texto), `unidades_ano_1`, `crecimiento_anual_pct`.
3. **Calcula la tabla anual con el motor**:
   ```bash
   python3 -c "import sys, json; sys.path.insert(0,'motor-reglas'); import reglas; \
   ue={'precio_unitario':<P_anual>,'costo_variable_unitario':<CV_anual>,'costos_fijos_mensuales':<CF>}; \
   esc=[{'nombre':'base','unidades_ano_1':<U>,'crecimiento_anual_pct':<G>}]; \
   print(json.dumps(reglas.proyeccion_escenarios(ue, esc, <ANIOS>), ensure_ascii=False, indent=2))"
   ```
   **Ojo con la unidad temporal**: `proyeccion()` toma precio y costo variable como
   **anuales** por unidad activa. Si tu modelo es mensual (suscripción), anualiza (×12)
   antes de pasarlos. Copia las filas `anios[]` de cada escenario al expediente.

## Subetapa V — Encaje con el mercado (motor)
```bash
python3 -c "import sys, json; sys.path.insert(0,'motor-reglas'); import reglas; \
print(json.dumps(reglas.encaje_mercado(ingresos_ano_final_clp=<ING_ULT_ANIO_BASE>, som_clp=<SOM>), ensure_ascii=False))"
```
Guarda `modelo_negocio.encaje_mercado` (`som_clp`, `ingresos_ano_final_base_clp`,
`penetracion_som_pct`). Si `penetracion_som_pct > 1` (la proyección no cabe en el SOM),
**dilo**: hay que revisar la proyección o el SOM antes de pasar a la revisión.

## Subetapa VI — Documento del modelo
Arma un **resumen legible del modelo** en `proyectos/<tenant>/modelo-negocio.md`: el Canvas,
la tabla de unit economics (entradas y salidas), la proyección por escenarios, el encaje con
el mercado, y la **lista de supuestos a confirmar** (de `supuestos_modelo.supuestos` con
`confirmado: false`). Es el insumo de la revisión (EVAL_P5) y del gate humano **modelo**.

## Salida
Escribe el bloque `modelo_negocio` (`canvas`, `unit_economics` con entradas + salidas del
motor, `proyeccion.escenarios` con las tablas del motor, `encaje_mercado`) en
`expediente.json`; `meta.paso_actual = "EVAL_P4"`. Valida y renderiza.

**DoD:** Canvas consolidado y trazable; unit economics con las salidas **calculadas por el
motor**; proyección de ≥1 escenario (idealmente 3) con su tabla anual del motor; encaje con
el SOM calculado; supuestos a confirmar listados; documento del modelo escrito.
