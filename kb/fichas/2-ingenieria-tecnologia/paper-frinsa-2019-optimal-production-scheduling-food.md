---
id: paper-frinsa-2019-optimal-production-scheduling-food
titulo: "Optimal production scheduling of food process industries (Computers & Chemical Engineering, dic-2019) — caso real Frinsa del Noroeste S.A."
tipo: paper
tema: MILP de precedencia general para programación semanal de una planta multi-producto/multi-etapa de conservas
area_oecd: "2 Ingeniería y Tecnología (2.11 Otras ingenierías y tecnologías)"
topicos: [milp-programacion-produccion-carnica]
anio: 2019
autores: []
referencia: https://www.sciencedirect.com/science/article/pii/S0098135419309603
motor: WebSearch (ScienceDirect bloqueado 403, solo snippets agregados)
profundidad_lectura: metadata
estado_evidencia: parcial
trl_relevante: -
metricas_clave: []
fecha_registro: 2026-08-18
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Optimizar la programación semanal de producción de una planta real de alimentos (Frinsa del Noroeste S.A., Ribeira, España) multi-producto y multi-etapa, combinando procesos por lotes (descongelado, esterilizado) y continuos (sellado/llenado, empaque).

## Hipótesis
No confirmable — no se accedió al cuerpo del paper.

## Metodología
- **Diseño:** dos modelos MILP con representación de tiempo mixta discreta-continua, más un algoritmo de descomposición por pedidos.
- **Datos / muestra:** datos reales de Frinsa, planta que produce >400 códigos de producto y cumple >100 pedidos por semana; una de las mayores conserveras de pescado de Europa.
- **Técnicas:** MILP basado en precedencia general; enfoque agregado (modela explícito los procesos continuos, usa restricciones de factibilidad válidas para la etapa por lotes).
- **Métricas:** no confirmadas (solo vía snippets de búsqueda, no el paper).

## Resultados principales
No confirmables desde la fuente primaria — la página de ScienceDirect devolvió 403 (bloqueo/paywall). Los datos de esta ficha provienen de agregación de resultados de motor de búsqueda (WebSearch), no de lectura directa.

## Conclusiones
No confirmables desde fuente primaria.

## Limitaciones
**No se pudo verificar contra la fuente primaria** (ScienceDirect 403/paywall). Autores no identificados. Toda la información viene de snippets agregados por el motor de búsqueda a partir de múltiples resultados (ResearchGate, ScienceDirect, capítulos relacionados) que describían consistentemente el mismo caso Frinsa — por eso se registra como `estado_evidencia: parcial` / `profundidad_lectura: metadata`, no como verificado.

## Relevancia / brecha para el estado del arte
Caso análogo de MILP multi-producto/multi-etapa en industria alimentaria real (conservas), de la misma familia de problema que el Objetivo 3 (MPS) de Agrosuper. Útil como referencia de que MILP escala a plantas reales con cientos de productos, pero **no debe citarse en el formulario oficial con afirmaciones específicas de resultados** hasta verificar el texto completo — solo la existencia del caso y su naturaleza general están confirmadas de forma independiente (3 fuentes de búsqueda coincidentes).

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
