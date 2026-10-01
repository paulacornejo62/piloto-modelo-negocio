# Referencia — Crea y Valida ganado vs. rechazado: qué pide el evaluador

Comparación de dos postulaciones reales de Brinca al **Crea y Valida**, para ajustar las
preguntas que el piloto le hace al cliente (R#1 / R#2). **Anonimizado**: sin nombres de
clientes ni cifras suyas. Los originales están en Drive y los vínculos están en el caso
`proyectos/aqp/entradas/README.md`.

| | Caso | Qué hay |
|---|---|---|
| **G** | **Ganado.** Minería, servicio *hardware + software* B2B, formulario 2024 | Formulario completo. **No hay carta de evaluación**, así que se sabe qué ganó pero no su nota por criterio. |
| **R** | **Rechazado.** Alimentos, producto B2C/B2B, convocatoria 2025, **nota 3,20** | Carta de rechazo con nota y justificación **por indicador**, más la retrospectiva interna de Brinca. |

> Las dos versiones del formulario (2024 y 2025) y la plantilla 2026 tienen la **misma
> sección 4** (Impacto Q1–Q3 + Escalabilidad Q4–Q6). Esto confirma la columna vertebral
> S5–S10 de `MAPEO-formularios.md`.

---

## 1. Notas de R por criterio (las que toca el piloto, en negrita)

| Criterio (peso) | Nota R | Qué dijo el evaluador |
|---|---|---|
| Diagnóstico (10%) | 3,0 | Las causas se quedan en argumentos generales y **no se conectan con la solución elegida** ("¿por qué esta vía y no otra?"). |
| **Mercado objetivo (10%)** | **3,0** | Solo identificó consumidores y canales. **Faltaron actores**: competidores, entidades regulatorias, organizaciones de investigación y socios estratégicos. **No demostró el interés o la necesidad** del cliente. |
| Metodología (20%) | 2,2 | TRL de entrada sobreestimado, sin evidencia de prototipo. **Presupuesto de marketing sin actividades comerciales en el plan.** |
| Novedad (10%) | 2,0 | **No comparó directamente** con los productos sustitutos (ingredientes, precio, vida útil…). |
| Actividades I+D (10%) | 4,0 | Estudio de factibilidad técnico-económica, estrategia de PI, transferencia y NDA **no cuentan como I+D**. |
| **Impacto (10%)** | **3,0** | IM1 = 4: el modelo estaba completo pero **no se conectaba del todo con el mercado objetivo** y priorizaba un canal sin justificarlo. IM2: **precios sin justificar frente a los costos de producción** y valores sin respaldo de mercado. IM3 = 2: impactos sociales y ambientales generales, sin cuantificar, y **omitió el impacto ambiental negativo** propio del producto. |
| **Escalabilidad (10%)** | **3,66** | ES1 = 3: **faltaron barreras regulatorias que el evaluador conoce del rubro** (permisos sanitarios, normas de inocuidad) y competidores actuales. ES3 = 3: la continuidad se limitaba a reinvertir y postular a otro fondo, **sin inversión privada, sin nuevas I+D y sin alianzas**. |
| Capacidades (20%) | 4,5 | Faltaba equipo técnico. Incluía personal no pertinente (abastecimiento, RRHH). |

**Retrospectiva interna de R:** levantar más información con el cliente (**al menos 2 reuniones**,
lo mismo que decidió el piloto), que la contraparte sea técnica y presente, y ser más críticos
con la novedad.

## 2. Qué hizo G en las mismas preguntas (el patrón que funciona)

| Pregunta | Cómo la respondió G | Dato que necesitó del cliente |
|---|---|---|
| Mercado objetivo | Separó **clientes** (con nombre), **usuarios** (operadores), **mercado secundario** y **gobierno**. Dio tamaño y crecimiento con fuente y fecha. La **evidencia de interés** fue el número de clientes actuales del producto V.0 más el interés declarado de clientes con nombre. | Lista de clientes actuales y potenciales, con nombre. Países donde ya opera. |
| Impacto Q1: modelo de ingresos | Unidad de cobro explícita (por camión/mes + módulo fijo). Usó el **precio del producto actual** como ancla y un **precio incremental** respaldado en un estudio del área comercial. Adopción base = **% de clientes actuales**. Mencionó canales. | Precio actual, unidad de cobro, nº de clientes y unidades instaladas, margen operacional del producto actual, estimación comercial del precio incremental. |
| Impacto Q2: magnitud | **3 escenarios** construidos con **palancas explícitas**: % de adopción de los clientes actuales, nº de clientes nuevos por año y precio incremental. Ingresos actuales como línea base. **Costos de ejecución unitarios** (equipo por cliente, recurrente anual, % de mantención/marketing). | Ingresos actuales, costos unitarios de implementar, costo recurrente. |
| Impacto Q3: social/ambiental | Social (seguridad del personal) y ambiental (CO₂) **con una cifra y una fuente** (DOI y *benchmark* con clientes). | Un benchmark o medición propia del cliente. |
| Escalab. Q4: barreras | Separó **técnicas / regulatorias / comerciales**, cada una con su mitigación. Mencionó el organismo regulador por nombre. | Qué permisos y normas conoce el cliente, y dónde ya tuvo problemas. |
| Escalab. Q6: continuidad | Año 1: validación local + marketing + PI. Después, expansión a países donde **ya tiene presencia**. | Presencia comercial actual fuera del país, plan comercial del cliente. |

## 3. Ajustes a las preguntas del piloto (propuesta, sin aplicar aún)

Lo que R perdió y G tenía se traduce en preguntas concretas al cliente:

| # | Pregunta nueva o reforzada | Cubre | Cuándo |
|---|---|---|---|
| A1 | **Tracción actual con números**: ventas por año, nº de clientes que compran (con nombre), unidades vendidas, margen del producto actual. Es la **línea base** de los escenarios. Confirma el gap §5 de `MAPEO`. | IM1, IM2, MO1 | R#1 + tarea de datos |
| A2 | **Evidencia de interés**: cartas, pilotos, pedidos, correos o reuniones con clientes que quieren la nueva versión. | MO1 | R#1 / R#2 |
| A3 | **Mapa completo de actores**: además de clientes y usuarios, quiénes son los competidores, quién regula, socios estratégicos y centros de investigación. | MO1, ES1 | R#2 + búsqueda |
| A4 | **Precio ancla y unidad de cobro**: precio actual, a cuánto se vendería la nueva versión y **en qué se basa** esa estimación (cotización, encuesta, comparable). Precio vs. **costo unitario de producción**. | IM1, IM2 | R#2 |
| A5 | **Palancas de los escenarios**: % de clientes actuales que adoptarían, clientes nuevos por año y precio incremental. Que el cliente las valide, no el consultor. | IM2 | R#2 |
| A6 | **Costos de ejecutar la venta**: costo de aplicar/implementar por cliente, recurrentes y comerciales. | IM2 | R#2 |
| A7 | **Impacto con cifra**: un dato medido o de benchmark (con fuente) para el impacto social/ambiental, **y el impacto negativo propio** del producto. | IM3 | R#2 + búsqueda |
| A8 | **Barreras regulatorias del rubro**: qué permisos o registros necesita hoy para vender y cuáles necesitará la nueva versión. | ES1 | R#2 (cliente técnico) |
| A9 | **Continuidad con dinero y aliados**: inversión privada, alianzas, siguientes I+D, mercados donde ya tiene presencia. | ES3 | R#2 |
| A10 | **Coherencia plan ↔ presupuesto comercial**: cada gasto comercial (marketing, ferias, estudios) debe tener su actividad en el plan. Esas actividades **no suman al % de I+D**. | Metodología, I+D | Revisión GT (W5) |

Se aplican al piloto (`mn-eval-reunion-1`, `mn-eval-reunion-2`, schema) cuando se valide el
flujo. **AQP es el primer caso donde se prueban.**
