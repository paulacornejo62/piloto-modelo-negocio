# piloto-modelo-negocio — la herramienta (vista técnica)

Piloto **aislado**. Adaptación del motor de formulación de financiamiento de la iniciativa
F19 (herramienta agéntica "GTF") para que, en vez de formular postulaciones a Ley I+D,
**construya modelos de negocio** de proyectos de innovación y **redacte las secciones de
modelo de negocio / mercado / escalamiento** de los formularios de subsidios CORFO (Crea y
Valida, Innova Alta Tecnología, Consolida y Expande, Capital Humano).

> 👤 **¿Vas a usar la herramienta?** Empieza por **[GUIA-USUARIO.md](GUIA-USUARIO.md)**.
> Este README es la vista técnica.
>
> **Aislado:** git local propio, sin conexión al repo brinca ni a GitHub. `proyectos/`
> arranca vacío, sin datos de clientes. Se puede romper y rehacer: se commitea seguido.

## Componentes
| Carpeta / archivo | Qué es |
|---|---|
| `CLAUDE.md` | **Instrucciones del agente** (rol de orquestador, flujo P1…P5 + W1…W5, reglas transversales). Se carga al lanzar `claude` desde aquí. |
| `.claude/skills/` | Pasos del flujo, prefijo `mn-`: `mn-nuevo-proyecto`, `mn-orquestar`, `mn-estado`, Fase 1 (`mn-eval-reunion-1`, `-deep-research-1`, `-reunion-2`, `-preparar-caso`, `-comite`), `mn-form-perfil` (Fase 1 CORFO), Fase 2 (`mn-form-w1`…`w5`), `mn-qa-veracidad`, `mn-kb-agregar` |
| `.claude/agents/` | Agentes reutilizables: `mn-deep-researcher` (investigador de mercado), `mn-qa-veracidad` (verificador adversarial de cifras) |
| `motor-reglas/` | Motor determinista: `parametros.json` (umbrales — **POR VALIDAR con ing. comercial**) + `reglas.py` (mercado, unit economics, proyección, compuerta de viabilidad, QA de coherencia) · `formularios.json` (secciones del formulario por fondo, con flag `en_alcance_piloto`) · `documentos_postulacion.json` (manifiesto de entregables de modelo de negocio por fondo) |
| `expediente.schema.json` | Contrato del estado de un caso: `perfil_comercial` → `investigacion_mercado` → `supuestos_modelo` → `modelo_negocio` → `revision_viabilidad` → `narrativa` → `formulario_oficial` → `plan_escalamiento` → `impacto_continuidad` → `qa_entrega` |
| `render/` | `render.py` (expediente→md, con Panel del consultor + secciones por bloque), `formulario.py` (`formulario-modelo-negocio.md`), `gantt.py` (Unit economics + Proyección + Hitos). |
| `tools/` | `browse.mjs` (navegador), `fuentes.json`/`.py` (fuentes de mercado), `kb.py` (base de conocimiento), `postulacion.py` (paquete de entregables + CHECKLIST por fondo), `estado`/`bitacora`/`panel` (flujo y sesiones) |
| `kb/` | Base de conocimiento transversal de mercado (informes, comparables, benchmarks): clasificada por **sector económico** + tipo de fuente. **Arranca vacía.** |
| `proyectos/` | Una carpeta por caso (aislada, gitignoreada). Vacío; se crean con `mn-nuevo-proyecto`. Al entrar a Fase 2 se agrega `postulacion/` (entregables + `CHECKLIST.md`). |
| `SETUP.md` · `setup/` · `.mcp.json` · `package.json` | Instalación y configuración |

## Estado del piloto

### Sesión 2026-09-01 — adaptación financiamiento I+D → modelo de negocio

**TAREA 1 — renombre de prefijo** (`11858c0`): 16 skills + 2 agentes `gtf-*` → `mn-*`,
frontmatter y todas las referencias cruzadas.

**TAREA 2 — adaptación de contenido**, por bloques:

| Bloque | Commit | Qué cambió |
|---|---|---|
| `CLAUDE.md` | `cc7966a` | Rol = asistente de modelo de negocio; flujo P1…P5 (construir el modelo) + W1…W5 (redactar secciones); compuerta **SÓLIDO / AJUSTAR / INVIABLE / DEVOLVER**; 12 reglas transversales (determinismo del motor, anclar cifras de mercado a fuente verificable, QA independiente, supuesto ≠ dato). Equipo/capacidades del beneficiario queda fuera del piloto (lo cubre F19). Sin envío irreversible. |
| `expediente.schema.json` | `f6774dc` | Bloques `eval_p*`/`form_w*` → bloques de modelo de negocio. `unit_economics` separa ENTRADAS de SALIDAS del motor. Eliminado: Frascati, elegibilidad, arancel, TRL, profesional acreditador, encuesta Ley I+D. |
| `motor-reglas/` | `590cf93` · `fca12da` | `reglas.py`: `mercado_coherencia`, `unit_economics`, `proyeccion(_escenarios)`, `encaje_mercado`, `indicadores_viabilidad`, `compuerta_viabilidad`, `qa_coherencia_modelo` (se conserva `coherencia_cifras_cliente`). Nuevo `parametros.json` (umbrales, reemplaza `instrumentos.json`). `formularios.json` sin `ley_id`, cada sección con `en_alcance_piloto`. `documentos_postulacion.json` acotado a entregables de modelo de negocio. Tests pasan. |
| Skills — Lote 1 (andamiaje) | `2329f11` | `mn-orquestar` (flujo nuevo, tabla paso→skill→bloque, gates), `mn-nuevo-proyecto` (fondos CORFO, entradas: proyecto de innovación + datos comerciales), `mn-estado`, `mn-deep-researcher` + `mn-qa-veracidad` (investigación/verificación **de mercado**), `mn-kb-agregar`. `tools/fuentes.json` → fuentes de mercado (INE, Banco Central, SII, CMF, Mercado Público, gremios, prensa de negocios, competidores). `kb/` reseteada; taxonomía por sector; plantillas `informe-mercado` y `comparable` (reemplazan paper/patente); ~229 fichas F19 eliminadas. |
| Skills — Lote 2 (Fase 1) | `cb8b88b` | `mn-eval-reunion-1` → `perfil_comercial`; `mn-eval-deep-research-1` → `investigacion_mercado` (TAM/SAM/SOM, competidores, precios); `mn-eval-reunion-2` → `supuestos_modelo`; `mn-eval-preparar-caso` → `modelo_negocio` (Canvas + llamadas al motor); `mn-eval-comite` → `revision_viabilidad` (compuerta del motor). |
| Skills — Lote 3 (Fase 2) | `06bbd0f` | `mn-form-perfil` (Perfil CORFO acotado a modelo de negocio); `mn-form-w1` → `narrativa`; `mn-form-w2` → `formulario_oficial` (solo secciones `en_alcance_piloto`); `mn-form-w3` → `plan_escalamiento`; `mn-form-w4` → `impacto_continuidad`; `mn-form-w5` → `qa_entrega` (entrega, sin envío). |

### Sesión 2026-09-02

| Bloque | Commit | Qué cambió |
|---|---|---|
| `render/*` + `tools/*.py` | `bdab1d4` | `render.py` reescrito (Panel del consultor + secciones por bloque nuevo; `--formulario` chequea solo `en_alcance_piloto`); `gantt.py` → Unit economics + Proyección + Hitos; `formulario.py` → `formulario-modelo-negocio.md`. `estado.py`/`panel.py`: PASOS/compuerta/`ENTREGADO`. `postulacion.py`: fondo desde `meta.instrumento_objetivo`. Shim UTF-8 en la salida (consola Windows). Probado con expediente sintético completo. |
| Docs de raíz | `4324e3c` · `fc230e8` | `SETUP.md`, `COMO-CORRER.md`, `GUIA-USUARIO.md`, `setup/setup.sh` reescritos para el flujo de modelo de negocio. |

### Preparación de validación con el negocio (docs de trabajo, no producto)

Para las reuniones con el líder (flujo general de un subsidio, nº de reuniones) y con la jefa
(validar el flujo y las reglas):

| Archivo | Commit | Qué es |
|---|---|---|
| `NOTAS-preparacion-reuniones.md` | `9b8fa13` | Prep personal completa: los **dos lenguajes** (Canvas / Go-to-Market — lo que enseña el curso CORFO Conecta y pide CORFO — vs. unit economics del motor); glosario simple de los términos financieros; la herramienta de captura estilo Canvas mapeada a R#1 / Mercado / R#2; preguntas de los formularios por fondo. |
| `MAPEO-formularios.md` | `a3f07f6` · `9a9a807` · *(este)* | Comparación de **tres formularios reales** (Crea y Valida 2025, Consolida y Expande 2024, Innova Alta Tecnología 2022): la columna vertebral compartida (S1–S14) mapeada a bloque del piloto / GT / mixto y a la reunión donde se levanta; preguntas específicas por fondo; el gap de "tracción actual". Referencia viva (verificar contra las bases del llamado). |
| `REUNION-JEFA-validacion.md` | `de0edca` · `9a9a807` | Guion para la jefa: recorrer las 9 preguntas de la columna vertebral (S1–S10) que aparecen en los 3 formularios, con cómo la aborda el piloto + fila "Sugerencia de la jefa"; + lo propio de Consolida y Expande (escalamiento + tracción actual). Con las sugerencias se ajusta R#1 / R#2. |
| Página visual del flujo | — (artifact) | Lámina proyectable: pipeline P1…P5 + compuerta + Fase 2 + qué se levanta en cada instancia. Privada; se comparte desde la propia página. |

**Hallazgo clave:** el motor sobre-indexó en métricas de startup digital (LTV, CAC, payback).
Propuesta a validar con la jefa: dejarlas **opcionales** (solo modelos recurrentes) y centrar
el motor en (a) completitud/coherencia del lienzo Canvas, (b) tamaño de mercado, (c) margen de
contribución > 0 y punto de equilibrio ≤ SOM, (d) proyección de ventas.

### Sesión 2026-10-01 — primer caso real (AQP) + referencia ganado vs. rechazado

**Para qué es el piloto (meta 2026 de Paula, hoja OI GT):** *"Desarrollar, documentar e
implementar una metodología estandarizada para la elaboración de los apartados de Modelo de
Negocio en las postulaciones a subsidios CORFO"*. Nota 5 = metodología documentada e
implementada y **usada en ≥3 postulaciones** (4 = ≥2 · 3 = ≥1 · 2 = documentada sin uso).
**Período: hasta diciembre 2026.** El entregable final es un **procedimiento escrito**; la
herramienta es su implementación con IA (también aporta a la meta de KB + prompts estándar).

| Bloque | Commit | Qué cambió |
|---|---|---|
| Caso `proyectos/aqp/` | — (gitignoreado) | **Postulación n.º 1**: AQP, Crea y Valida 2026 (postula ~dic-2026), sobre el proyecto Ley I+D bi-modal contra Caligus. Buzón cargado: notas de la coordinación del 25-09, formulario Ley I+D, síntesis del proyecto, datos comerciales conocidos (todo `[POR CONFIRMAR]`) y `preguntas-reunion-2.md`. Drive vinculado. |
| `REFERENCIA-CyV-ganado-vs-rechazado.md` | `616a7d2` | Qué evalúa CORFO por indicador (carta del rechazado, nota 3,20) vs. cómo respondió el ganado → **preguntas A1–A10**, que afinan las S5–S10 de `REUNION-JEFA-validacion.md` (no las reemplazan). |
| `BITACORA-metodologia.md` | `7af9d71` | **Registro de uso** (evidencia del KPI) + aprendizajes por caso. Caso 1 = AQP: resultado de la R#2 (02-10) por bloque Canvas y 7 aprendizajes para el procedimiento (el 7.º: separar modelo actual vs. proyectado). |

Decisiones: no se rehace el formulario — el documento "Sugerencias V2" del compañero queda
como suyo. La metodología = banco de preguntas (S1–S10 + A1–A10) + guía por pregunta.

### Sesión 2026-10-02 — Reunión #2 con AQP + preparación de la #3

| Bloque | Dónde | Qué cambió |
|---|---|---|
| Banco de preguntas por Canvas | `proyectos/aqp/entradas/preguntas-reunion-2.md` | A1–A10 + N1–N3 (relación con clientes, recursos, competencia) ordenadas por los 9 bloques del Canvas + franja CORFO (impacto, permisos, continuidad). |
| Reunión #2 (02-10) | `entradas/reunion-2.md`, `presentacion-modelo-negocio-aqp.md`, `datos-comerciales.md` | AQP trajo su propia presentación del modelo. Datos nuevos por bloque Canvas (todo dato del cliente, sin respaldo aún). Convocatoria CyV: **10-11-2026 → 28-01-2027**. |
| Resultado de la prueba | `BITACORA-metodologia.md` | Bien cubiertos: segmentos, relación, recursos, actividades. Lo cualitativo sí, los números no: propuesta, canales, ingresos, socios, costos. Sin tocar: **franja CORFO**. 6 aprendizajes (el Canvas no trae números; reservar tiempo a la franja CORFO; confirmar cifras por escrito; etc.). |
| Lienzo Canvas (artifact) | https://claude.ai/artifact/G1yqbKgCuEFMa1Z8qHkzKy | Página proyectable: por bloque, lo que ya sabemos + lo que falta + notas en vivo. Actualizada para la R#3. |
| Presentación R#3 | Drive `AQP/2026/2.- Crea y Valida - Noviembre 2026/` | "Crea y Valida AQP - Reunión 3 (08-10-2026).pptx", 10 láminas: lo levantado, lo que falta, cifras a confirmar, pedido de proyecciones de Aquaprime 1.0, pedido de avances técnicos, cruce Ley I+D → CyV, plan de formulación por jueves. |

### Sesión 2026-10-05 — revisión de Paula + nuevas fuentes del cliente

| Bloque | Dónde | Qué cambió |
|---|---|---|
| Presentación R#3 (editada por Paula: portada, índice, separadores, logo Brinca) — **versión final para la R#3 (06-10)**, la revisa con José Pablo: https://docs.google.com/presentation/d/1LzHbTTE044bRKcF17vgp4GW7LwVXuzHx | Drive `AQP/2026/2.- Crea y Valida - Noviembre 2026/` | 18 láminas. Canvas "modelo actual Aquaprime 1.0" (solo producto actual + 2 tipos de compra + capacidad de asistencia). Nueva lámina **propuesta de valor del producto** (atributos con fuente). Tabla **actual → proyectado por los 9 bloques** (baño nuevo vs. oral). Preguntas en 2 columnas (actual / proyectado). Cifras a confirmar ampliadas. **Plan de trabajo por semanas** (S1 = 05-10, apertura S6 = 10-11, perfil S5–S7, formulación S9–S12). Dudas en **rojo**. |
| Lienzo Canvas (artifact) | https://claude.ai/artifact/G1yqbKgCuEFMa1Z8qHkzKy | Cada bloque: hoy (Aquaprime 1.0) · proyectado (baño nuevo + oral) · lo que falta. |
| Nuevas entradas del caso | `entradas/presentacion-aquaprime-antigua.md`, `postulacion-anid-startup-ciencia.md`, `datos-comerciales.md` | Atributos del producto, kit de campo (TRL 3), competidores con nombre, datos de mercado con fuente, **patente PCT WO 2025/107092 A1 verificada: titular Aquacon SpA, no AQP**. Capacidad: 2–3 asistencias por técnico al mes, mejor mes ≈10. |
| Bitácora | `BITACORA-metodologia.md` | Aprendizajes 7–11: separar modelo actual/proyectado, pedir postulaciones previas, revisar titularidad de PI, capacidad operativa = techo, herramientas del curso CORFO Conecta. |

### División de trabajo AQP: piloto ↔ F19 (decidido 2026-10-07)

- **F19** escribe el **formulario completo** (perfil y Crea y Valida): problema, solución, hipótesis,
  hitos, I+D, propiedad intelectual, equipo, presupuesto, y el **cruce técnico** con la Ley I+D
  (Gantt, avances a la fecha, proyección a marzo de 2027).
- **Este piloto** redacta las **secciones de modelo de negocio**: mercado objetivo (en lo comercial),
  modelo de ingresos, cuantificación, impacto, barreras, continuidad (4.1–4.6). Las entrega a F19 como
  borrador, y F19 lo integra y revisa la coherencia con el resto (hitos comerciales ↔ plan de trabajo,
  actividades comerciales fuera del % de I+D).
- **Una sola fuente para los datos comerciales de AQP:** `proyectos/aqp/entradas/`. F19 apunta a esos
  archivos, no los copia. Toda cifra comercial se corrige primero aquí y después se traspasa.
- **Conversaciones separadas**, cada una lanzada desde su carpeta. AQP es el primer caso real del
  traspaso piloto → F19 (pendiente abierto: formato de entrega).

### Sesión 2026-10-08 — Reunión #3 con AQP

| Bloque | Dónde | Qué cambió |
|---|---|---|
| Notas R#3 | `entradas/reunion-3.md` (fuente: Notas de Gemini 08-10 + correcciones de Paula) | Se cerró: **precio US$2.950 + IVA por litro** (incluye acompañamiento; Gemini anotó "950 pesos"); **costo total del baño ≈US$4.000 por jaula** (≈US$1.000 son maniobras externas: HH, buzos, mallas); **permisos = autorización de Directemar por cada producto**; competidor **Sudvet** (Lyptus Plus®, Rosseus Plus® en baño; Aware Plus® oral); **cartas de interés** de los clientes actuales; mortalidad 0,01–0,02%; derechos cedidos por Aquacon. Etapa Crea de 6 meses = propuesta, se define con la Gantt. |
| Dosis efectiva | `entradas/datos-comerciales.md` | Revisadas las transcripciones de formulación Ley I+D (22-05, 05-06, 12-06): no hay un dato explícito. Inconsistencia ppm/ppb: 0,1–0,2 ppm ≈ 1 L por jaula, que cuadra con el precio. **Confirmar con Claudio.** |
| Correo post-reunión | redactado en la conversación; Paula lo envía con la ppt en PDF y la tabla de Hugo en un doc de la carpeta de reuniones | Pedidos para R#4: avances técnicos (Claudio, Rodrigo, Cristian), resumen de Aquaprime (Rodrigo), tabla de Hugo (2025 real · 2026 estimado · 2027–2029 de Aquaprime 1.0). |
| Bitácora | `BITACORA-metodologia.md` (commit e76d737) | Aprendizajes 12–14: lámina de cifras a confirmar + revisar las notas automáticas; preguntar el costo total para el cliente; pedir los datos financieros en tabla. |

### Pendiente
1. **Reunión #4 (jueves 15-10, 15:00–16:00).** AQP presenta los avances técnicos de la Ley I+D
   (prototipos, eficacia, ensayos, estado a mar-27 → TRL) y el estado de la Gantt; Rodrigo trae
   el resumen de Aquaprime; Hugo envía la tabla de datos. Preguntar a Claudio la **dosis efectiva**
   (ppm/ppb, volumen del baño, litros por jaula). Explicación del ensayo de 5 meses con Fernanda.
   Con eso se cierra el levantamiento; la semana siguiente parte la formulación (Gantt → formulario).
   Siguen pendientes: contrato de cesión/licencia de la patente (Aquacon), informes de ensayo,
   gráfico ventas vs. baños, carta de evaluación ANID, canal y precio del oral, fichas de Sudvet.
   Confirmar en las bases técnicas CyV 2026 (Res. 388) las fechas del perfil.
   **Insumo para F19** después de la R#4: Gantt, TRL, cruce 4.3–4.5 ↔ CyV.
2. **Correr el flujo con AQP** (`orquesta aqp`) cuando lleguen los datos. Verificar una por una
   las cifras heredadas de la Ley I+D antes de usarlas.
3. **Procedimiento escrito v0** (después de AQP): objetivo y alcance · etapas · banco de
   preguntas integrado (S + A) · guía por pregunta del formulario con indicadores CORFO y
   errores a evitar · checklist de calidad · **registro de uso** (evidencia del KPI).
4. **Postulaciones n.º 2 y 3** antes de dic-2026 — probablemente otros fondos además de
   Crea y Valida (por eso el procedimiento se apoya en la columna vertebral de `MAPEO-formularios.md`).
5. Aplicar al piloto los ajustes validados (A1–A10 en `mn-eval-reunion-1/2` y el schema,
   bloque `traccion_actual`, cambios de `NOTAS-preparacion-reuniones.md` Parte 4).
6. Sin fecha: reunión con el líder (dónde se inserta el modelo de negocio en el mes de
   postulación) y con la jefa (validar S1–S10). Excepciones al n.º de reuniones: 3 para
   Consolida y Expande, 1 para Capital Humano.
7. Guía de redacción fina por sección CORFO: la aporta F19.

Cómo correrlo: **[COMO-CORRER.md](COMO-CORRER.md)**.
