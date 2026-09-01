---
name: mn-eval-deep-research-1
description: Paso EVAL_P2 del flujo de financiamiento GT — Deep Research #1. Toma el Perfil Preliminar del expediente e investiga el estado del arte (papers/patentes/competidores), formula una hipótesis y un cuestionario para la Reunión #2. Escribe el bloque eval_p2 en el expediente.json y crea fichas en la base de conocimiento. Lo invoca el orquestador mn-orquestar.
---

# EVAL_P2 — Deep Research #1 (DRx)

**Objetivo:** investigar el Estado del Arte (EdA) **en profundidad**, catalogar soluciones existentes y formular un primer marco de hipótesis y desafíos técnicos para empoderar al consultor de cara a la Reunión #2.

**Input:** el bloque `eval_p1` (Perfil Preliminar) de `proyectos/<tenant>/expediente.json`.

## Esto es un Deep Research, no una búsqueda simple

Una sola pasada de `WebSearch` **NO es suficiente** y no cumple el DoD. La investigación debe ser **profunda e iterativa**:
- **Multi-consulta por fuente**: varias queries por motor (términos técnicos, sinónimos, en inglés y español, por subtema).
- **Iterativa**: ronda amplia → afinar con lo encontrado → seguir citas y referencias cruzadas → cerrar brechas. Repite hasta saturación (rondas sin hallazgos nuevos).
- **Profundiza en la fuente**: no te quedes en el snippet; abre el documento (abstract completo, claims de la patente, metodología) con navegador/fetch.
- **Más allá del piso**: las fuentes mandatorias son el **piso, no el techo** — agrega cualquier fuente relevante (revisiones, tesis, repositorios, actores del mercado, normativa).
- **Alcance GLOBAL**: el estado del arte (novedad) es **mundial**. **Nunca** restrinjas la búsqueda de papers/patentes a un país por defecto. El filtro de país (`gp "<query>" CL`) es **solo** para una verificación puntual de *prior art nacional* (patentes chilenas), no para el estado del arte de novedad.

> **Ejecución**: este paso se hace con el **agente reutilizable `mn-deep-researcher`** (puedes correr uno o varios), y luego **`mn-qa-veracidad`**. La lista de fuentes a recorrer está en **`tools/fuentes.json`** (`python3 tools/fuentes.py usables`) — el registro único, fácil de ampliar.

## Herramientas de investigación (obligatorio usarlas, no solo WebSearch)

- **Navegador real (`tools/browse.mjs`, Playwright)** — abre fuentes JS/paywall y busca patentes. **Patentes**: usa `gp "<query>" [PAIS]` (Google Patents, el motor que funciona; agrega EP/WO/US/CN/CL). Los registros oficiales (Espacenet, INAPI, PatentScope) están **bot-protegidos** (ver `tools/README.md`): llama a los modos `espacenet`/`inapi`/`patentscope` solo para **declarar su cobertura con honestidad** (`no_accesible`/`requiere_manual`), no para extraer. Para FTO formal de patentes chilenas queda un paso **manual** en INAPI.
- **Búsqueda profunda por API** (Exa/Tavily, si está configurada) — recuperación semántica con texto completo.
- **WebSearch / WebFetch** — solo como apoyo/triangulación, nunca como única fuente.
- Si una herramienta mandatoria no está disponible en el entorno, **decláralo explícitamente** en la minuta (qué motor no se pudo cubrir y por qué) — no lo escondas.

## Fuentes mandatorias (piso)

Catálogo canónico (mantener sincronizado): [`estado-del-arte.md`](../../../../desarrollo/contexto/resumenes/ley-id-metodologia/estado-del-arte.md).
- **Papers:** IEEE, PubMed, Google Académico, ScienceDirect, Springer Nature Link.
- **Patentes:** WIPO PatentScope, Lens, Espacenet, INAPI (Chile), clasificación IPC (WIPO).

Por cada hallazgo, registra de qué motor proviene (en `referencia`) para trazabilidad.

**Tu tarea:**
1. Investiga el estado del arte **en profundidad** con la metodología y herramientas de arriba: recorre las fuentes mandatorias (papers y patentes) con navegador real + amplía a otras fuentes relevantes + competidores/productos. Prioriza fuentes verificables y citables.
2. Produce la **Minuta de Investigación v1** (esquema `eval_p2` en `../../expediente.schema.json`):
   - `hipotesis_preliminar_o_objetivo_general`: texto estructurado.
   - `sintesis_estado_del_arte`: **síntesis narrativa para lectura rápida** (3-6 frases, lenguaje llano, sin jerga de íconos) — el consultor debe entender el panorama sin leer toda la lista: qué **ya está resuelto/disponible**, qué **sigue abierto**, y **dónde está la brecha** que sostiene el proyecto. Va ARRIBA del detalle (el render la muestra en "En breve" y le suma un resumen automático de conteos/evidencia). **Escríbela siempre**: sin ella el expediente queda confuso de leer.
   - `glosario`: **términos del área en lenguaje llano para el consultor** (que puede no ser experto en el tema). Eres el primer paso que trae nomenclatura técnica pesada: **puebla el glosario** con cada sigla/término no obvio que uses (patógeno, proceso, unidad, norma) — `{termino, sigla, definicion}`, definición en 1-2 frases simples. Y **expande cada sigla al primer uso** en los textos ("Síndrome Rickettsial Salmonídeo (SRS)"). No incluyas términos del dominio de financiamiento (Frascati, TRL, Ley I+D). El render lo muestra en el Panel del consultor.
   - `estado_del_arte_v1`: lista de hallazgos; cada uno `{ tipo, motor (de dónde salió), referencia (URL/ID verificable), hallazgo, cita_textual (localizador que lo respalda), estado_evidencia }`.
     - `estado_evidencia`: **verificado** (abriste la fuente y coincide) / **parcial** (solo abstract/metadata; full-text en paywall) / **no_verificado** (referenciado pero no pudiste abrir/confirmar → tentativo).
   - `cobertura_busqueda`: por cada fuente mandatoria, su estado real: **cubierto / sin_resultados / acceso_parcial / no_accesible**. **Obligatorio** — así no se ocultan lagunas.
   - `desafios_tecnicos_identificados_v1`: barreras técnicas identificadas, con **fact-check crítico**: para cada desafío, evalúa contra el estado del arte si es **realmente vigente** (no resuelto o con escasa solución) o si **ya está resuelto**. No des un desafío por bueno porque el cliente lo dijo; un desafío ya resuelto **no sustenta I+D** (Frascati). Marca la vigencia de cada uno.
   - `cuestionario_indagacion`: un **POOL AMPLIO** de preguntas (**≥8**, el consultor selecciona las mejores), cada una con `categoria`, en **dos ejes**:
     - **`objetivo_es_id`** — preguntas en torno al **objetivo/hipótesis** que ayuden a levantar si el proyecto **es I+D o no** (clave, sobre todo en proyectos de **integración de tecnologías ya validadas**, donde la novedad/incertidumbre no es obvia: ¿qué es lo genuinamente incierto? ¿qué conocimiento nuevo se genera vs. qué es ingeniería/integración estándar?).
     - **`estado_arte_desafios`** — preguntas **técnicas** que indaguen los desafíos y **cómo se atienden** (variables críticas, cómo validan, qué falla hoy).
     Genera varias de cada categoría; no te quedes solo en lo técnico.
3. **Consulta y alimenta la base de conocimiento** (`../../kb/`, transversal a todos los proyectos) — **NO es opcional; es parte del cierre del paso**:
   - **Consulta primero** conocimiento previo: `python3 tools/kb.py buscar --topico "<tema>"` (trae fichas análogas de **otros proyectos** por tópico compartido).
   - Por cada fuente relevante, **antes de crear** corre `python3 tools/kb.py dedup "<título>"`. Si hay similar, **enlaza/actualiza** (agrega el proyecto a `proyectos:` + una arista) en vez de duplicar.
   - Si es nueva: usa el skill **`mn-kb-agregar`** para crear una **ficha RICA** (no bullets): la plantilla según tipo (`PLANTILLA-paper.md` con pregunta·hipótesis·metodología·resultados·conclusiones·limitaciones; `PLANTILLA-patente.md` con problema·reivindicaciones·solución·FTO). **Lee el full-text** cuando sea accesible y marca `profundidad_lectura` (full-text/abstract/metadata) + `estado_evidencia` con honestidad. Pon el `id` en `ficha_kb` del hallazgo.
   - **Cobertura:** cada hallazgo `verificado`/`parcial` del estado del arte debe quedar con su **ficha rica** en la KB (los `no_verificado` se omiten o quedan tentativos). El conocimiento del Deep Research **no se pierde** — se acumula para las próximas postulaciones.
4. Escribe el bloque `eval_p2` en `expediente.json` y pon `meta.paso_actual = "EVAL_P2"`.

**Criterio de salida (DoD):** Minuta v1 con **síntesis narrativa** (`sintesis_estado_del_arte`) + **glosario** de los términos del área usados + estado del arte citado (cada hallazgo con `motor`, `referencia`, `cita_textual` y `estado_evidencia`), `cobertura_busqueda` completa, hipótesis y ≥5 preguntas; y **fichas KB ricas creadas/enlazadas para cada hallazgo verificado/parcial** (con `profundidad_lectura` y `estado_evidencia`) — sin esto el paso NO está cerrado. Después de este paso, el orquestador corre el **QA de veracidad** (`mn-qa-veracidad`) que verifica todo de forma independiente **y sincroniza el `estado_evidencia` de las fichas** con su veredicto.

## Veracidad (regla suprema)
- **No afirmes nada sin respaldo.** Toda cifra/autor/patente debe estar en la fuente abierta; si no la abriste, es `no_verificado` (tentativo), no un hecho.
- **Disponible / parcial / no disponible debe quedar explícito** — en `estado_evidencia` por hallazgo y en `cobertura_busqueda` por motor. Prohibido presentar como verificado algo que es solo abstract o inaccesible.
- **Cero exageración**: reporta exactamente lo que dice la fuente, con su contexto (p. ej. métricas de estanque ≠ jaula).
- Tu salida pasará por verificación adversarial; lo que no se confirme será descartado.
