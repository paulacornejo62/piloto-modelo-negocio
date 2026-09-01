---
name: mn-eval-reunion-1
description: Paso EVAL_P1 del flujo de modelo de negocio — Reunión #1 con el cliente. Toma la declaración inicial del cliente y la descripción del proyecto de innovación (transcripción, notas o texto libre) y produce el Perfil Comercial. Escribe el bloque perfil_comercial en el expediente.json del tenant. Lo invoca el orquestador mn-orquestar.
---

# EVAL_P1 — Reunión #1 (perfil comercial)

**Objetivo:** obtener el contexto comercial de la empresa y del proyecto de innovación:
qué vende o pretende vender, a quién le vende hoy, por qué canal, y qué resultado de negocio
busca. Es captura estructurada, NO análisis del modelo todavía.

**Input:** la declaración inicial del cliente en el **buzón** `proyectos/<tenant>/entradas/`
— típicamente `entradas/reunion-1.md`, `entradas/proyecto.md` (el proyecto de innovación) y
`entradas/datos-comerciales.md`, más cualquier otro documento que el consultor haya dejado
ahí. Revisa la carpeta `entradas/` completa, no solo un archivo. (O el texto que te pase el
orquestador.)

**Tu tarea:**
1. Lee todas las entradas del cliente.
2. Extrae y estructura el **Perfil Comercial** con estos campos (esquema en
   `../../expediente.schema.json`, bloque `perfil_comercial`):
   - `cliente_razon_social`
   - `cliente_tamano`: Micro / Pequeña / Mediana / Grande, y `cliente_tamano_confirmado`
     (bool): `true` **solo** si el cliente lo confirmó o es claramente determinable; si lo
     infieres, `false` → queda como **supuesto** (afecta el % de cofinanciamiento CORFO).
   - `cliente_fecha_inicio_actividades` (algunos fondos exigen antigüedad mínima).
   - `contacto_clave`: { nombre, cargo, email }.
   - `producto_o_servicio`: qué vende o pretende vender, en lenguaje llano.
   - `estado_desarrollo`: idea / prototipo / piloto con clientes / ya vendiendo. Condiciona
     el fondo y el horizonte de proyección.
   - `clientes_actuales`: a quién le vende HOY (segmentos, nombres si los hay, nº de
     clientes, ingresos actuales si los declara).
   - `canal_actual`: cómo llega hoy a sus clientes.
   - `problema_u_oportunidad`: el problema de mercado o la oportunidad que quiere capturar
     con este proyecto.
   - `resultado_negocio_esperado`: entrar a un mercado, escalar ventas, nuevo segmento,
     nuevo producto. **NO metadata de tramitación** (fechas de Corfo). El fondo objetivo va
     en `meta.instrumento_objetivo`, no aquí.
   - `presupuesto_estimado_clp`: número en CLP — **captarlo** (o marcarlo `[POR CONFIRMAR]`).
   - `historia_previa`: `postulaciones_o_evaluaciones_previas`, `modelo_negocio_actual`
     (cómo gana plata hoy, si ya opera), `intentos_previos_y_resultado` (intentos anteriores
     de entrar a este mercado / escalar y por qué no resultaron). **El caso casi nunca parte
     de cero.**
3. **Semillas del modelo (arrástralas, no las pierdas).** Si en la Reunión #1 aparecen
   señales de segmentos, precio, forma de cobro, costos o quién decide en el negocio,
   anótalas para la Reunión #2 — el modelo se consolida en EVAL_P3/P4.
4. **Proyecto de innovación.** Deja claro en el perfil qué se desarrolla y en qué estado
   (`estado_desarrollo`), porque el modelo de negocio se construye sobre eso. Es un proyecto
   de innovación: si el cliente proyecta cifras de mercado futuro, regístralas como lo que
   son (declaraciones a validar), no como hechos.
5. Si un dato no está en la entrada, **no lo inventes**: déjalo vacío y márcalo
   `[POR CONFIRMAR]` como pregunta pendiente para el cliente.
6. Escribe el bloque `perfil_comercial` en `proyectos/<tenant>/expediente.json` y pon
   `meta.paso_actual = "EVAL_P1"`, `meta.actualizado` con la fecha que te dé el orquestador.
   Si el cliente declaró cifras (precio, nº de clientes, ventas), agrégalas a
   `meta.cifras_declaradas[]` = {concepto, valor, unidad, fuente: "reunion-1"}.

**Criterio de salida (DoD):** Perfil Comercial con ≥80% de los campos y el problema/resultado
de negocio redactados; presupuesto captado (o `[POR CONFIRMAR]`); `estado_desarrollo` del
proyecto de innovación claro.

**No hagas:** investigación de mercado, Business Model Canvas, unit economics ni compuerta.
Eso es de pasos posteriores.
