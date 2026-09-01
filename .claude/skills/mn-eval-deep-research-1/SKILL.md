---
name: mn-eval-deep-research-1
description: Paso EVAL_P2 del flujo de modelo de negocio — Investigación de mercado. Toma el Perfil Comercial del expediente e investiga en profundidad el tamaño de mercado (TAM/SAM/SOM), competidores y sustitutos, precios de referencia y benchmarks de industria; prepara un cuestionario para la Reunión #2. Escribe el bloque investigacion_mercado y crea fichas en la base de conocimiento. Lo invoca el orquestador mn-orquestar.
---

# EVAL_P2 — Investigación de mercado

**Objetivo:** dimensionar el mercado del proyecto de innovación y mapear la competencia
**en profundidad**, para empoderar al consultor de cara a la Reunión #2 y alimentar el
modelo de negocio.

**Input:** el bloque `perfil_comercial` de `proyectos/<tenant>/expediente.json` (qué se
vende, a quién, el problema/oportunidad) y `entradas/proyecto.md`.

## Esto es un Deep Research, no una búsqueda simple
Una sola pasada de `WebSearch` **NO** cumple el DoD. La investigación es **profunda e
iterativa**:
- **Multi-consulta por fuente**: varias queries por fuente (términos del rubro, sinónimos,
  código de actividad económica, en español e inglés, por sub-mercado).
- **Iterativa**: ronda amplia → afinar → seguir referencias primarias → cerrar brechas.
  Repite hasta saturación.
- **Profundiza en la fuente**: no te quedes en el snippet; abre el informe, la tabla
  estadística, la página de precios del competidor.
- **Del dato general al accionable**: un tamaño de mercado global no dimensiona Chile.
  Prioriza el **bottom-up** para el mercado servible (nº de empresas/personas del segmento ×
  ticket, con datos de INE/SII por rubro) y contrástalo con el top-down.

> **Ejecución**: este paso se hace con el **agente `mn-deep-researcher`** (uno o varios en
> paralelo, fan-out por sub-mercado o tipo de fuente), y luego **`mn-qa-veracidad`**. Las
> fuentes están en **`tools/fuentes.json`** (`python3 tools/fuentes.py usables`).

## Fuentes (piso, no techo)
- **Tamaño y demanda:** INE, Banco Central, SII (empresas por rubro y tramo de ventas),
  Mercado Público, CEPAL/OCDE/Banco Mundial, gremios del sector.
- **Competencia y precios:** sitios y páginas de precios de competidores, Crunchbase,
  G2/Capterra, LinkedIn (dotación como proxy de escala).
- **Industria:** resúmenes de informes (Statista, IBISWorld, consultoras — cifra titular +
  año + fuente primaria, nunca el número tras el paywall), prensa de negocios (DF, Pulso,
  AméricaEconomía), estudios CORFO / ecosistema.
- Para las bloqueadas o de pago, llama su modo solo para **declarar la cobertura honesta**.

**Tu tarea:**
1. Investiga el mercado **en profundidad** con la metodología y fuentes de arriba.
2. Produce la **Investigación de mercado** (esquema `investigacion_mercado` en
   `../../expediente.schema.json`):
   - `sintesis_mercado`: **síntesis narrativa para lectura rápida** (3-6 frases, lenguaje
     llano) — tamaño y dinámica del mercado, quiénes son los actores, dónde están los
     precios, qué tendencia lo mueve y dónde está el espacio para el cliente. Va ARRIBA del
     detalle. **Escríbela siempre.**
   - `tamano_mercado`: `{ tam_clp, sam_clp, som_clp, cagr_pct, metodo (top-down/bottom-up/
     ambos), geografia, anio_referencia, fuentes[], estado_evidencia }`. Chequea el embudo
     con el motor: `python3 -c "import sys; sys.path.insert(0,'motor-reglas'); import reglas,
     json; print(json.dumps(reglas.mercado_coherencia(<tam>, <sam>, <som>), ensure_ascii=False))"`.
   - `hallazgos`: lista; cada uno `{ tipo (competidor/sustituto/precio_referencia/
     benchmark_industria/tamano_mercado/tendencia/regulacion/cliente_potencial), fuente,
     referencia (URL/ID verificable), hallazgo (con unidad y **año**), cita_textual,
     estado_evidencia }`.
     - `estado_evidencia`: **verificado** (abriste la fuente, la cifra/año/geografía
       coinciden) / **parcial** (solo resumen accesible) / **no_verificado** (tentativo).
   - `competidores`: por cada uno relevante `{ nombre, que_ofrece, precio_aprox, fortaleza,
     debilidad, estado_evidencia }`. Incluye los **sustitutos** (lo que el cliente hace hoy
     sin este producto: una planilla, un proceso manual, "no hacer nada").
   - `cobertura_busqueda`: por cada fuente, su estado real: **cubierto / sin_resultados /
     acceso_parcial / no_accesible**. **Obligatorio.**
   - `preguntas_para_reunion_2`: **POOL** (**≥5**) de preguntas para validar con el cliente,
     cada una con `categoria` (segmento / pricing / costos / canal / ejecucion): ¿qué
     segmento paga de verdad? ¿qué precio acepta el mercado? ¿cuánto cuesta conseguir un
     cliente? ¿qué supuestos del modelo hay que confirmar?
   - `glosario`: si usas términos del rubro no obvios para el consultor, agrégalos
     (`{termino, sigla, definicion}` en lenguaje llano). Los términos de modelo de negocio
     (TAM/SAM/SOM, CAC, LTV) los define EVAL_P4.
3. **Consulta y alimenta la base de conocimiento** (`../../kb/`, transversal) — **parte del
   cierre del paso**:
   - **Consulta primero**: `python3 tools/kb.py buscar --topico "<sector/tema>"` (fichas de
     mercado de otros casos).
   - **Dedup antes de crear**: `python3 tools/kb.py dedup "<título>"`. Si hay similar,
     enlaza/actualiza (agrega el caso a `proyectos:` + una arista).
   - Si es nueva: usa **`mn-kb-agregar`** para crear una **ficha RICA** (plantilla según
     tipo: `PLANTILLA-informe-mercado.md` o `PLANTILLA-comparable.md`), con `anio_dato`,
     `geografia`, `profundidad_lectura` y `estado_evidencia` honestos. Pon el `id` en
     `ficha_kb` del hallazgo.
   - Cada hallazgo `verificado`/`parcial` queda con su ficha; los `no_verificado` se omiten
     o quedan tentativos.
4. Escribe el bloque `investigacion_mercado` en `expediente.json` y pon
   `meta.paso_actual = "EVAL_P2"`.

**Criterio de salida (DoD):** síntesis narrativa + `tamano_mercado` con método y fuentes +
`hallazgos` citados (cada uno con fuente, referencia, cita_textual, año y estado_evidencia) +
`competidores` con sustitutos + `cobertura_busqueda` completa + ≥5 preguntas; **fichas KB
ricas** creadas/enlazadas para cada hallazgo verificado/parcial. Después de este paso el
orquestador corre **mn-qa-veracidad**, que verifica todo de forma independiente y sincroniza
el `estado_evidencia` de las fichas.

## Veracidad (regla suprema)
- **No afirmes ninguna cifra sin abrir la fuente.** Registra **año** y **geografía** de cada
  número. Una estimación tuya va como **supuesto**, nunca como `verificado`.
- **Verificado / parcial / no verificado / supuesto debe quedar explícito** — por hallazgo y
  en `cobertura_busqueda`.
- **Cero exageración**: un mercado regional no es nacional; una proyección no es un dato
  actual; un precio de lista no es el precio efectivo.
- Tu salida pasará por verificación adversarial; lo que no se confirme será descartado.
