---
name: mn-eval-reunion-2
description: Paso EVAL_P3 del flujo de modelo de negocio — Reunión #2 con el cliente. Valida los hallazgos de la investigación de mercado y levanta con el cliente los supuestos del modelo: segmentos, propuesta de valor, canales, estructura de ingresos y de costos, CAC y capacidad de ejecución. Escribe el bloque supuestos_modelo. Lo invoca el orquestador mn-orquestar.
---

# EVAL_P3 — Reunión #2 (supuestos del modelo)

**Objetivo:** contrastar la investigación de mercado con la experiencia del cliente y
**levantar los supuestos que alimentan el modelo de negocio**: quién es el cliente que
paga, qué precio acepta, cómo se le llega, cuánto cuesta conseguirlo y qué cuesta operar.

**Input:** el bloque `investigacion_mercado` (con `preguntas_para_reunion_2`,
`tamano_mercado` y `competidores`) del expediente, más las **respuestas del cliente**
(notas/transcripción de la Reunión #2) que te pase el orquestador o que estén en el buzón
`proyectos/<tenant>/entradas/` (típicamente `entradas/reunion-2.md`).

**Tu tarea (esquema `supuestos_modelo` en `../../expediente.schema.json`):**
1. Registra las **respuestas al cuestionario** (`respuestas_cuestionario`: lista de
   {pregunta, respuesta}).
2. **Segmentos** (`segmentos[]`): `{ nombre, descripcion, tamano_estimado (nº de clientes
   potenciales, con fuente si viene de la investigación), prioridad (primario/secundario/
   futuro) }`. Prioriza con el cliente.
3. **Propuesta de valor por segmento primario** (`propuesta_valor[]`): `{ segmento,
   propuesta, dolor_que_resuelve, alternativa_actual_del_cliente }` — el verdadero competidor
   suele ser "no hacer nada" o una planilla.
4. **Canales** (`canales`) y **relación con clientes** (`relacion_clientes`).
5. **Estructura de ingresos** (`estructura_ingresos[]`): `{ nombre, tipo (suscripcion/
   transaccion/licencia/servicio/venta_unitaria/comision/otro), precio (CLP), unidad (por
   qué se cobra), recurrencia_meses (0 = pago único) }`.
6. **Estructura de costos** (`estructura_costos[]`): `{ concepto, tipo (fijo/variable), monto
   (CLP; si variable = por unidad, si fijo = mensual), unidad }`. El motor necesita la
   separación fijo/variable para el margen de contribución y el punto de equilibrio.
7. **CAC** (`costo_adquisicion_cliente`): `{ valor_clp, base (dato del cliente / benchmark de
   industria / supuesto), estado_evidencia }`.
8. **Recursos y socios clave** (`recursos_y_socios_clave`).
9. **Capacidad de ejecución** (`capacidad_ejecucion`): ¿el cliente PUEDE ejecutar este
   modelo? Quién decide, qué le falta (capital, equipo, permisos, acuerdos). Una barrera de
   ejecución puede ser justo lo que el subsidio viene a resolver — anótalo.
10. **Supuestos consolidados** (`supuestos[]`): TODOS los supuestos del modelo, cada uno
    `{ supuesto, valor, confirmado (bool), impacto_si_falla }`. Es un proyecto de
    innovación: la mayoría partirá con `confirmado: false` — está bien, **se marcan, no se
    esconden**. Los no confirmados se arrastran luego a `impacto_continuidad.supuestos_a_confirmar`.
11. **Cifras del cliente** (C5): cada dato cuantitativo que declare (precio, nº de clientes,
    ventas, costos) agrégalo a `meta.cifras_declaradas[]` = {concepto, valor, unidad, fuente:
    "reunion-2"}. Si contradice una cifra ya declarada, **no la silencies**: el motor la
    marcará como alerta.
12. Escribe el bloque `supuestos_modelo` en `expediente.json` y pon
    `meta.paso_actual = "EVAL_P3"`.

**DoD:** segmentos priorizados; propuesta de valor por segmento primario; estructura de
ingresos y de costos (con fijo/variable); CAC con su base; capacidad de ejecución evaluada;
lista de supuestos consolidada con su flag `confirmado`; cifras del cliente registradas.

**No hagas:** unit economics, proyección ni compuerta todavía — eso es EVAL_P4, y lo calcula
el motor.
