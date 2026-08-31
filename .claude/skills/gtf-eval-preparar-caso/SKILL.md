---
name: gtf-eval-preparar-caso
description: Paso EVAL_P4 del flujo de financiamiento GT — Preparar el Caso. Cuatro subetapas: Deep Research #2 (estado del arte específico + objetivo SMART), clasificación Frascati, perfil de subsidios CORFO y láminas de comité. Usa el motor de reglas determinista para Frascati y elegibilidad. Escribe el bloque eval_p4. Lo invoca el orquestador gtf-orquestar.
---

# EVAL_P4 — Preparar el Caso

Análisis interno en cuatro subetapas. **Las decisiones numéricas/booleanas las calcula el motor de reglas, no tú.**

**Input:** `eval_p1` (perfil comercial, tamaño empresa, fecha inicio), `eval_p2` (estado del arte v1) y `eval_p3` (perfil técnico v2, `trl_declarado`).

> **Escritura para el consultor (transversal).** El caso lo lee un consultor que puede no ser experto en el tema. Expande toda sigla al primer uso y **mantén al día el `glosario`** del expediente: si el DR#2 introduce términos del área nuevos, agrégalos ({termino, sigla, definicion} en lenguaje llano). Ver regla 8 del CLAUDE.md.

## Subetapa I — Deep Research #2 (exhaustivo, fan-out paralelo)
Estado del arte **exhaustivo y específico** para robustecer la novedad. Este es el pase profundo: en vez de una sola búsqueda, **abre varias en paralelo** y consolida.
1. **Fan-out**: lanza **varios `gtf-deep-researcher` en paralelo** (subagentes), repartidos por **motor y por tópico** (ver `python3 tools/fuentes.py usables`) — p.ej. uno por Google Patents, otro por papers, otro por un subtema. Cada uno investiga global y profundo, con evidencia y cobertura honesta.
2. **QA**: corre **`gtf-qa-veracidad`** sobre el conjunto (verifica, descarta alucinaciones, sincroniza fichas).
3. **Dedup + síntesis**: deduplica contra la KB (`tools/kb.py dedup`) y consolida en un solo estado del arte.
4. **Alimenta la KB (obligatorio)**: por cada fuente nueva verificada/parcial, crea su **ficha RICA** con `gtf-kb-agregar` (plantilla según tipo, `profundidad_lectura` + `estado_evidencia`, **full-text si es accesible**). El conocimiento del DR#2 se acumula — no se queda solo en el expediente.

> Alternativa para un pase aún más exhaustivo (ad-hoc, opt-in): un Workflow guardado. El fan-out nativo de arriba es la vía por defecto.

Produce:
- `estado_del_arte_especifico`: por qué la solución no es obvia ni asimilable hoy.
- `desafios_tecnicos_consolidados`: incertidumbres técnicas específicas no resueltas por el estado del arte.
- `perfil_tecnico_proyecto_v3`: alcance técnico actualizado tras el DR#2.
- `objetivo_general_smart`: *Verbo + Qué + Métrica de éxito + Plazo*. (Heredará a FORM_W1.)
> Tras este Deep Research, el orquestador corre **gtf-qa-veracidad** (igual que en EVAL_P2).

## Subetapa II — Frascati **adversarial por defecto** (motor de reglas)
No clasifiques como I+D por defecto: **estresa la elegibilidad primero**. El error caro es el **falso positivo** (integración/ingeniería rutinaria vendida como I+D).

1. **Prueba de exclusiones (obligatoria, no a pedido).** Antes de afirmar nada, contrasta el caso contra **cada** no-elegible de la Ley I+D y escribe el veredicto con sustento del estado del arte:
   - `adaptacion_rutinaria` · `ingenieria_estandar` · `adquisicion_puesta_en_marcha` · `validacion_medicion_comercial` · `novedad_solo_local` (nuevo para la empresa/país ≠ nuevo para el estado del arte).
   - Para cada una: `veredicto` = `sorteada` (el caso NO cae aquí, **con** sustento) | `aplica` (el caso CAE — no es I+D por ese flanco) | `pendiente` (falta indagar). "No lo hemos hecho nosotros" y "hay que instalarlo/coordinar" **no** son incertidumbre técnica.
2. Determina los dos booleanos con criterio técnico. Cada componente afirmado debe **nombrar qué exclusión sortea**:
   - `componente_i` (genera nuevo conocimiento / uso no trivial) y `componente_d` (resultado incierto / requiere experimentación).
3. **Calcula** cuadrante, `es_id` y `es_id_defendible` con el motor (no los decidas tú), pasándole las exclusiones:
   ```bash
   python3 -c "import sys,json; sys.path.insert(0,'motor-reglas'); import reglas; \
   print(json.dumps(reglas.frascati(<I>, <D>, exclusiones=[{'exclusion':'adaptacion_rutinaria','veredicto':'sorteada','sustento':'…'}, …]), ensure_ascii=False))"
   ```
   Si `es_id_defendible` es **false** (alguna exclusión aplica o quedó sin sustento), el caso es un **candidato a falso positivo**: no lo lleves como I+D sólido — dilo, y pasa a la Subetapa II-b (reencuadre).
4. Guarda `frascati = {componente_i, componente_d, cuadrante, es_id, es_id_defendible, justificacion, exclusiones_evaluadas[]}`.

## Subetapa II-b — Reencuadre a elegibilidad (**sugerir, no forzar**)
Solo si `es_id` es **débil** (`es_id_defendible` false o dudoso). Cuando el caso, como está, no es I+D, no te limites a decir "no": **ofrece caminos** —a modo de sugerencia— para volverlo elegible. Poblá `reencuadre_elegibilidad[]` con opciones tipo:
- `desarrollar_en_vez_de_comprar` — qué componente convendría desarrollar en lugar de adquirir.
- `socio_academico` — apalancar con una universidad: estudios financiables por la propia ley que habilitan el proyecto completo.
- `estudio_financiable` — qué estudio (p.ej. de no-daño, de seguridad) agregar que sí es I+D.
- `fase_2` — mover el alcance incierto a una fase posterior.

**Reglas duras (coherentes con C1):** son **propuestas que el consultor y el cliente evalúan y pueden descartar**; **no cambian el veredicto** por sí solas (cada opción lleva `es_sugerencia: true`); **no fabriques elegibilidad** para "salvar" el caso. Si no hay camino honesto, deja el array vacío y **dilo**.

## Subetapa III — Perfil de subsidios (motor de reglas)
Si `meta.instrumento_objetivo` está definido (no "por definir"), tenlo presente al **ordenar/priorizar** el perfil — pero la **elegibilidad y el % los manda el motor**, no la preferencia declarada (si el objetivo resulta no elegible, dilo).

Cruza empresa + proyecto con los instrumentos CORFO usando el motor (TRL del `eval_p3`, tamaño y antigüedad del `eval_p1`):
```bash
python3 -c "import sys; sys.path.insert(0,'motor-reglas'); import reglas, json; print(json.dumps(reglas.instrumentos_elegibles(trl=<TRL>, tamano='<Tamaño>', antiguedad_meses=<N>, lidera_mujer=<bool>), ensure_ascii=False))"
```
Para cada instrumento arma `perfil_subsidios[]` = {instrumento, elegible (del motor), cofinanciamiento_pct (del motor), alineacion (Bajo/Mediano/Alto — tu juicio cualitativo de fit), justificacion}. La **elegibilidad y el % son del motor**; la alineación cualitativa es tu aporte.

> **Supuesto de tamaño (regla dura):** si `eval_p1.empresa_tamano_confirmado` no es `true`, el `cofinanciamiento_pct` es **provisorio** — el tamaño de empresa determina el %. NO lo asumas en silencio: incluye "**tamaño de empresa (afecta el cofinanciamiento)**" en los **datos a confirmar** de la recomendación/láminas, y dilo explícito. Lo mismo con `empresa_fecha_inicio_actividades` (antigüedad → elegibilidad) y `contabilidad` (Ley I+D) si vienen sin confirmar.

## Subetapa IV — Consolidado para el comité
Arma el **Consolidado proyecto para Comité** con la **estructura OFICIAL** de GT (fuente: `../../../../desarrollo/contexto/fuentes/estructura_comite.md`) — no inventes secciones. Guárdalo en `proyectos/<tenant>/laminas-comite.md`.

> **Hilo conductor (C7).** Las secciones 3→6 no son tres listas sueltas: **enlaza cada problemática con su solución y con el desafío tecnológico** que la sostiene. El lector debe seguir *problema → solución → desafío técnico (incertidumbre)* para cada dolor, no una lista de problemas y aparte una lista de soluciones sin match. Numera o referencia cruzada para que el match sea explícito.

Secciones (mapea desde el expediente):
1. **Datos del cliente** — datos de la empresa (`eval_p1`) + **contactos de los involucrados en la evaluación**.
2. **Contexto** *(si aplica)* — información del proceso de evaluación, consideraciones particulares, **postulaciones previas**.
3. **Problemática / Oportunidad** — origen y causas + **cuantificación/dimensionamiento** (cifras del estado del arte).
4. **Soluciones existentes** — alternativas de solución + **competidores relevantes** (del estado del arte verificado).
5. **Propuesta de solución** — descripción de la solución (`perfil_tecnico_proyecto_v3`).
6. **Desafíos tecnológicos** — identificación y descripción (`desafios_tecnicos_consolidados`; con el fact-check de vigencia).
7. **Objetivo General** — el objetivo SMART + **KPI clave**.
8. **Línea base** *(si aplica)* — para proyectos previos: diferencias postulación previa vs. actual; y una **tabla comparando los fondos candidatos** (del `perfil_subsidios`), p.ej.:

   | Atributos | Ley I+D | Crea y Valida | … |
   |---|---|---|---|
   | Elegible / cofinanciamiento / tope / plazo / alineación | … | … | … |

   Es el insumo con que el comité decide el instrumento. Incluye la clasificación Frascati (`es_id`) como respaldo de que es I+D, y los **datos a confirmar** (tamaño, contabilidad, antigüedad).
9. **Presupuesto** — análisis de qué compone el presupuesto + **¿es posible aumentarlo?**

## Salida
Escribe el bloque `eval_p4` (estado_del_arte_especifico, desafios_tecnicos_consolidados, perfil_tecnico_proyecto_v3, objetivo_general_smart, **frascati con exclusiones_evaluadas y es_id_defendible**, perfil_subsidios, y **reencuadre_elegibilidad[] si es_id es débil**) en `expediente.json`; `meta.paso_actual = "EVAL_P4"`. Valida y renderiza.

**DoD:** estado del arte específico citado y verificado (QA), objetivo SMART, **Frascati adversarial** calculado por el motor (exclusiones evaluadas + `es_id_defendible`) con justificación, perfil de subsidios con elegibilidad del motor, reencuadre sugerido si el caso es débil, y láminas de comité con el hilo problema→solución→desafío.
