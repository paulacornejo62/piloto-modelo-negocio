# Preparación — reuniones de validación del flujo

Documento de trabajo para las dos reuniones:
- **Mañana · con el líder** — validar si con **dos reuniones** con el cliente se levanta lo necesario del modelo de negocio.
- **Martes · con la jefa** — presentar el flujo de captura, mostrar qué se levanta en cada reunión, y **validar reglas del motor**.

> **Alcance del piloto** (recordar en ambas): construye el **modelo de negocio** y redacta las secciones de **modelo de negocio / mercado / escalamiento**. Metodología técnica, actividades de I+D (GID), propiedad intelectual y equipo/capacidades quedan para el equipo GT / F19.

---

## PARTE A — Preguntas de los formularios por fondo (consolidado)

Fuente: criterios de evaluación de cada instrumento + `motor-reglas/formularios.json`. **Verificar contra las bases vigentes de cada convocatoria** — el detalle fino cambia por llamado. `%` = ponderador del criterio.

Leyenda de columnas:
- **Bloque** — dónde vive en el expediente del piloto.
- **Se levanta en** — R#1 (Reunión #1), Mercado (investigación, sin cliente), R#2 (Reunión #2), Modelo (construcción interna con el motor), Redacción.
- **Alcance** — 🟢 lo cubre el piloto · ⚪ lo cubre GT.

### Crea y Valida Innovación
Fase 1 (Perfil de Proyecto, obligatoria, feedback ~14 días hábiles) → Fase 2. Etapas CREA (prototipo) + VALIDA (validación productiva/comercial).

| Sección (%) | Preguntas típicas | Bloque | Se levanta en | Alcance |
|---|---|---|---|---|
| **Problema / Diagnóstico** (10%) | ¿Cuál es el problema/oportunidad? ¿A quién afecta y con qué magnitud (cifras: frecuencia, costo, % afectados)? ¿Qué lo causa? ¿Por qué ahora? Fuentes. | `perfil_comercial` + `investigacion_mercado` | R#1 + Mercado | 🟢 |
| **Mercado objetivo** (10%) | ¿A qué segmento apunta? Tamaño (TAM/SAM/SOM), Chile y/o exportación. Crecimiento. Clientes potenciales concretos (cartas de interés). | `investigacion_mercado` + `supuestos_modelo` | Mercado + R#2 | 🟢 |
| **Solución — Metodología** (20%) | Descripción técnica. Plan de trabajo: objetivos, actividades, hitos, entregables, Gantt. Indicadores por hito. Presupuesto por ítem + cofinanciamiento. Dedicación horaria. | — | — | ⚪ |
| **Solución — Novedad y diferenciación** (10%) | ¿Qué la hace novedosa vs. lo existente (nacional e internacional)? Comparación con competidores/sustitutos. ¿Incremental o disruptiva? Propiedad intelectual / FTO. | `investigacion_mercado` (competidores) + Redacción `narrativa` | Mercado + R#2 | 🟢 la diferenciación de mercado / ⚪ la novedad técnica y PI |
| **Actividades de I+D (GID)** (10%) | ¿Qué actividades son I+D (Ley 20.241)? % del costo total que es Gasto en I+D. ≥30% → nota máxima. | — | — | ⚪ |
| **Introducción al mercado — Impacto** (10%) | Ventas/ingresos incrementales (3–5 años). Ahorro de costos. Empleos creados. Impacto social/ambiental. | `modelo_negocio` (proyección) + `impacto_continuidad` | Modelo + validación con cliente | 🟢 |
| **Introducción al mercado — Escalabilidad** (10%) | ¿Cómo se escala? (más clientes, nuevos segmentos, exportación). Estrategia de comercialización. Inversión para escalar. | `plan_escalamiento` + `supuestos_modelo` | R#2 + Modelo | 🟢 |
| **Capacidades** (20%) | Equipo del beneficiario, asociados, colaboradores. Experiencia. Infraestructura. | — | — | ⚪ |

### Consolida y Expande Innovación
Escalamiento de algo que **ya requirió I+D** (franja alta de TRL). Evaluación en **2 etapas**. **Peso de negocio muy alto.**

| Sección (%) | Preguntas típicas | Bloque | Se levanta en | Alcance |
|---|---|---|---|---|
| **Etapa 1 · Problema — Diagnóstico** (10%) | Problema/oportunidad de **escalamiento**, con evidencia. | `perfil_comercial` + `investigacion_mercado` | R#1 + Mercado | 🟢 |
| **Etapa 1 · Problema — Mercado objetivo** (20%) | Mercado(s) de destino del escalamiento: tamaño, geografías, crecimiento, por qué alcanzables. | `investigacion_mercado` + `supuestos_modelo` | Mercado + R#2 | 🟢 |
| **Etapa 1 · Solución — Metodología** (30%) | Metodología del escalamiento/validación técnica: plan, hitos, presupuesto. | — | — | ⚪ |
| **Etapa 1 · Solución — Novedad y diferenciación** (40%) | Novedad/diferenciación del producto/proceso frente a la oferta actual. | `investigacion_mercado` + `narrativa` | Mercado + R#2 | 🟢 (mercado) / ⚪ (técnica) |
| **Etapa 2 · Plan de Negocios — Estrategia de negocio** (40%) | Modelo de negocio (canvas), propuesta de valor, canales, estructura de ingresos y costos, **proyección financiera** (ventas, márgenes, punto de equilibrio), inversión y retorno, alianzas. | `modelo_negocio` + `supuestos_modelo` + `plan_escalamiento` | R#2 + Modelo | 🟢 |
| **Etapa 2 · Plan de Negocios — Escalabilidad** (30%) | Plan de expansión nacional e internacional, mercados prioritarios, barreras de entrada y cómo superarlas, hitos comerciales. | `plan_escalamiento` | R#2 + Modelo | 🟢 |
| **Etapa 2 · Capacidades — Beneficiario y asociados** (30%) | Capacidad para ejecutar el escalamiento. | — | — | ⚪ |

### Innova Alta Tecnología
Fase 1 (Perfil + Presentación, con reunión). Requiere **TRL > 3** y **gasto I+D ≥ 30%**.

| Sección (%) | Preguntas típicas | Bloque | Se levanta en | Alcance |
|---|---|---|---|---|
| **Problema — Diagnóstico y análisis tecnológico** (15%) | Diagnóstico del problema/oportunidad + **inteligencia tecnológica** (vigilancia, patentes) + análisis de propiedad intelectual. | `perfil_comercial` + `investigacion_mercado` | R#1 + Mercado | 🟢 el diagnóstico de mercado / ⚪ inteligencia tecnológica y PI |
| **Problema — Mercado objetivo** (10%) | Segmento, tamaño (TAM/SAM/SOM), geografía, por qué alcanzable. | `investigacion_mercado` + `supuestos_modelo` | Mercado + R#2 | 🟢 |
| **Solución — Metodología** (15%) | Solución técnica, plan de trabajo, indicadores, presupuesto, dedicación horaria. | — | — | ⚪ |
| **Solución — Novedad y diferenciación** (15%) | Grado de novedad (idealmente internacional), diferenciación tecnológica. | `investigacion_mercado` + `narrativa` | Mercado + R#2 | 🟢 (mercado) / ⚪ (técnica) |
| **Mercado — Beneficios esperados** (10%) | Ingresos/ahorro, impactos sociales y ambientales. | `impacto_continuidad` + `modelo_negocio` | Modelo + validación cliente | 🟢 |
| **Mercado — Estrategia de continuidad** (15%) | Riesgos y barreras, protección de resultados (PI), captura de valor, **continuidad y financiamiento post-subsidio**. | `impacto_continuidad` | R#2 + Modelo | 🟢 la captura de valor / continuidad / ⚪ la protección de resultados (PI) |
| **Capacidades — Equipo de trabajo** (10%) | Equipo del proyecto. | — | — | ⚪ |
| **Capacidades — Beneficiario y asociados** (10%) | Capacidades del beneficiario y asociados. | — | — | ⚪ |

### Capital Humano para la Innovación
Inserción de **un** profesional/técnico experto (jornada completa, ≥ 12 meses). Foco en la persona. **Aporte del piloto acotado.**

| Sección (%) | Preguntas típicas | Bloque | Se levanta en | Alcance |
|---|---|---|---|---|
| **Caracterización del desafío en la empresa** (35%) | ¿Cuál es el desafío productivo/competitivo/de innovación que motiva contratar a un experto? Magnitud y urgencia. Encuadre de mercado. | `perfil_comercial` + `investigacion_mercado` | R#1 + Mercado | 🟢 |
| **Perfil de los participantes** (35%) | Beneficiario (10%): capacidades, por qué necesita el apoyo. Profesional a contratar (25%): título/grado, experiencia, encaje con el desafío, funciones. | — | — | ⚪ |
| **Metodología y Plan de Trabajo** (20%) | Cómo abordará el desafío la persona; plan de trabajo, hitos. | — | — | ⚪ |
| **Resultados e indicadores comprometidos** (10%) | Resultados esperados (nuevos productos/procesos, capacidades instaladas) e indicadores medibles de negocio. | `plan_escalamiento` + `impacto_continuidad` | R#2 + Modelo | 🟢 |

### Resumen: qué % del formulario cubre el piloto

| Fondo | Secciones en alcance del piloto | Peso aprox. de esas secciones |
|---|---|---|
| Crea y Valida | diagnóstico, mercado objetivo, novedad (mitad), impacto, escalabilidad | ~45–50% |
| Consolida y Expande | diagnóstico, mercado objetivo, novedad (mitad), estrategia de negocio, escalabilidad | ~60–70% (fondo muy comercial) |
| Innova Alta Tecnología | diagnóstico (mitad), mercado objetivo, novedad (mitad), beneficios, continuidad (mitad) | ~40–45% |
| Capital Humano | caracterización del desafío, resultados/indicadores | ~30–40% |

---

## PARTE B — Reunión de mañana (con el líder): ¿bastan 2 reuniones?

**Objetivo:** estresar el flujo de captura contra un subsidio real y decidir si 2 reuniones con el cliente son suficientes, o si hay que ajustar.

**Duración:** 45–60 min. **Llevas:** este documento + el diagrama del flujo (P1→P5) + un `expediente.md` de ejemplo.

### El flujo, tal como está hoy

| Momento | Con el cliente | Qué se levanta |
|---|---|---|
| **R#1** (EVAL_P1 → `perfil_comercial`) | Sí | Qué vende, a quién hoy, canal, problema/oportunidad, resultado de negocio buscado, presupuesto, historia previa, estado del proyecto de innovación. |
| Investigación de mercado (EVAL_P2 → `investigacion_mercado`) | No | TAM/SAM/SOM, competidores, sustitutos, precios de referencia, benchmarks. Todo pasa por QA de veracidad. |
| **R#2** (EVAL_P3 → `supuestos_modelo`) | Sí | Segmentos priorizados, propuesta de valor por segmento, canales, relación con clientes, **estructura de ingresos (precio, forma de cobro)**, **estructura de costos (fijo/variable)**, **CAC**, capacidad de ejecución, lista consolidada de supuestos. |
| Construir el modelo (EVAL_P4 → `modelo_negocio`) | No | Canvas + unit economics + proyección por escenarios (motor). |
| Revisión + compuerta (EVAL_P5 → `revision_viabilidad`) | No (revisión interna o con un par) | Indicadores + compuerta SÓLIDO / AJUSTAR / INVIABLE / DEVOLVER. |

> Ya hay una "válvula de escape": la compuerta **DEVOLVER** = falta información del cliente → se agenda otra reunión y se re-corre R#2.

### Puntos frágiles a poner sobre la mesa (llévalos identificados)

1. **Estructura de costos detallada.** R#2 pide fijo/variable, BOM, CAC. En hardware / deep tech el cliente rara vez lo tiene ordenado → probablemente necesita **tarea de datos** entre R#1 y R#2, no improvisarlo en la reunión.
2. **Validación de los números de proyección e impacto.** La proyección (unidades año 1, crecimiento por escenario) y el impacto (ventas incrementales, empleos) se construyen en EVAL_P4, sin cliente. El cliente debería **confirmarlos** antes de la compuerta → hoy eso solo existe vía DEVOLVER; ¿lo formalizamos como un touchpoint corto (llamada o revisión asíncrona)?
3. **Disposición a pagar / pricing.** R#2 pregunta "qué precio acepta el mercado", pero si el cliente no hizo pilotos ni cotizaciones, es un supuesto. ¿Está bien dejarlo como supuesto marcado?
4. **Consolida y Expande.** Su Etapa 2 (Plan de Negocios) es profunda: estrategia de negocio + escalabilidad + proyección financiera + inversión/retorno. 2 reuniones puede quedar corto **para este fondo en particular** → ¿3 por defecto?
5. **Asimetría R#1 / R#2.** Hoy R#1 es liviana (perfil) y R#2 concentra toda la carga. Alternativa: mover parte de segmentos/pricing a R#1 para que R#2 sea validación + cierre de brechas.

### Preguntas concretas para el líder

- ¿En qué punto del proceso real de un subsidio se inserta el modelo de negocio? ¿Antes de la formulación con GT, en paralelo, después?
- ¿El cliente típico llega con datos comerciales o hay que sacárselos? ¿Sirve mandar una **plantilla de datos** después de R#1 (precios, costos, BOM, pipeline, estados financieros)?
- ¿Qué sección históricamente **cuesta más** levantar en una sola conversación?
- ¿La proyección financiera la valida el cliente formalmente, o basta con dejar los supuestos declarados?
- ¿2 + tarea de datos como estándar, y 3 para Consolida y Expande? ¿O 3 siempre?

### Salida esperada de la reunión
- Nº de reuniones estándar por fondo, acordado.
- Si se agrega: la "tarea de datos" post-R#1 (qué pide) y/o un touchpoint de validación de números.
- Ajustes a qué se pregunta en R#1 vs R#2.

---

## PARTE C — Reunión del martes (con la jefa): presentar el flujo y validar reglas

**Objetivo:** que la jefa entienda el flujo de captura, vea qué se levanta en cada reunión, y **valide las reglas del motor** (es lo que quieres levantar con ella).

**Duración:** 60 min. **Llevas:** presentación del flujo + la tabla "qué se levanta en cada reunión" (Parte B) + `motor-reglas/parametros.json` + un `expediente.md` de ejemplo del rubro que le interese.

### Agenda

1. **(10') Qué resuelve el piloto y su encaje con F19.** Piloto aislado (git propio, sin tocar F19). Si funciona → PR coordinando con Pablo Ferreiro. Alcance: solo modelo de negocio / mercado / escalamiento; el resto lo hace GT. No hay envío en plataforma: se entrega un borrador que GT integra.
2. **(15') El flujo de captura, reunión por reunión** (usar la tabla de la Parte B). Mostrar en el `expediente.md` de ejemplo: el Panel del consultor arriba (compuerta, unit economics, datos por confirmar) y cada bloque abajo.
3. **(20') Validar reglas — el bloque central.**
4. **(10') Guía de redacción fina por sección CORFO.** Hoy `formularios.json` la marca como pendiente del equipo GT. ¿Quién la tiene o la arma? ¿Hay ejemplos de postulaciones ganadoras para calibrar?
5. **(5') Próximos pasos.** Ajustes al piloto, caso real de prueba, timing para proponerlo a F19.

### Reglas a validar con la jefa (una por una)

Todas viven en `motor-reglas/parametros.json`, marcadas **PRIMERA VERSIÓN — POR VALIDAR**:

| Regla | Valor actual | Pregunta para la jefa |
|---|---|---|
| Margen de contribución mínimo | **30%** (≤ 0 = crítico) | ¿Razonable como piso genérico? ¿Debería variar: hardware/deep tech toleran menos, SaaS espera más? |
| LTV / CAC mínimo | **3,0** (< 1 = crítico) | Regla de pulgar SaaS. ¿Aplica a negocios de hardware o servicios con venta única? ¿Otro corte? |
| Payback de CAC máximo | **12 meses** (> 24 = crítico) | ¿Tiene sentido para modelos no recurrentes? ¿Ajustar por fondo o por tipo de negocio? |
| Penetración de SOM (proyección año final / SOM) | alerta **25%**, crítico **100%** | ¿25% es un buen umbral de "proyección agresiva"? ¿Qué espera ver un evaluador CORFO? |
| **Lógica de la compuerta** | INVIABLE si el punto de equilibrio > SOM **o** el escenario optimista termina negativo; AJUSTAR si hay indicadores fuera de umbral; SÓLIDO si todo ok | **La más importante:** un modelo que *no cierra sin el subsidio* — ¿es INVIABLE, o es justo lo que el subsidio viene a habilitar? ¿Dónde ponemos la línea? |
| Método de dimensionamiento de mercado | bottom-up (nº de empresas/personas del segmento × ticket, con datos INE/SII) contrastado con top-down | ¿Es lo que un evaluador CORFO espera? ¿Qué fuentes considera creíbles? |
| Trato de los supuestos | En un proyecto de innovación casi todo es supuesto; se marcan `confirmado: false` y se listan en "supuestos a confirmar" | ¿Cómo se presenta esto en la postulación sin que se lea como debilidad? |
| Horizonte de la proyección | genérico, se fija por caso (típ. 3–5 años) | ¿3 o 5 por defecto? ¿Depende del fondo? |

### Preguntas concretas para la jefa

- ¿Hay un **ingeniero comercial** en el equipo que pueda hacer una pasada de 30 min a los umbrales y a la lógica de la compuerta?
- ¿Qué **caso real** (de un cliente ya cerrado, sin datos sensibles) podríamos usar de prueba end-to-end?
- ¿El modelo de colaboración "el piloto entrega borrador, GT integra y completa lo técnico/equipo" es el correcto? ¿O el piloto debería cubrir más?
- ¿Existe una guía interna de redacción por fondo, o casos ganadores para calibrar el estilo?
- ¿Cada cuánto cambian las bases de estos 4 fondos? (para saber cuánto invertir en el detalle fino del formulario)

### Salida esperada de la reunión
- Umbrales del motor: confirmados o ajustados (aunque sea "provisorio hasta que lo vea el ingeniero comercial").
- Definición de qué hace un modelo INVIABLE vs. AJUSTAR.
- Caso real acordado para la prueba.
- Quién arma la guía de redacción fina por sección.

---

## Anexo — Cheat sheet: qué se levanta en cada reunión

Para mostrar de un vistazo.

**Reunión #1 — Perfil comercial** (≈45 min)
- La empresa: razón social, tamaño, antigüedad, contacto.
- Qué vende o pretende vender (el proyecto de innovación) y en qué estado está.
- A quién le vende hoy, por qué canal, cuántos clientes, ventas actuales.
- El problema de mercado / la oportunidad que persigue.
- Qué resultado de negocio busca (entrar a un mercado, escalar, nuevo segmento).
- Presupuesto estimado del proyecto.
- Historia previa: cómo gana plata hoy, intentos anteriores.
- → *Tarea para el cliente: dejar en un doc precios, costos (fijos y variables), BOM si aplica, pipeline de clientes, estados financieros.*

**Investigación de mercado** (sin cliente — el equipo, con navegador)
- Tamaño de mercado: TAM / SAM / SOM, con método (bottom-up para Chile) y fuentes.
- Competidores y sustitutos: qué ofrecen, a qué precio, fortalezas/debilidades.
- Precios de referencia y benchmarks de industria (márgenes, CAC típico, ciclo de venta).
- Tendencias y regulación que mueven el mercado.
- → Todo verificado cifra por cifra (año y geografía) por un QA independiente.

**Reunión #2 — Supuestos del modelo** (≈60 min)
- Segmentos de cliente priorizados y su tamaño.
- Propuesta de valor por segmento; contra qué compite realmente (a veces "no hacer nada").
- Canales de venta y relación con clientes.
- Estructura de ingresos: qué se cobra, cómo (suscripción / unitaria / servicio…), a qué precio.
- Estructura de costos: fijos mensuales y variables por unidad.
- CAC: cuánto cuesta conseguir un cliente.
- Capacidad de ejecución: quién decide, qué le falta a la empresa para ejecutar el modelo.
- Lista de supuestos, cada uno marcado como confirmado o pendiente.

**Construcción del modelo + revisión** (sin cliente)
- Business Model Canvas consolidado.
- Unit economics: margen de contribución, LTV, LTV/CAC, payback, punto de equilibrio (los calcula el motor).
- Proyección por escenarios (pesimista / base / optimista).
- Compuerta: SÓLIDO → redactar · AJUSTAR → mover palancas y recalcular · INVIABLE → informe al cliente · DEVOLVER → otra reunión con el cliente.
