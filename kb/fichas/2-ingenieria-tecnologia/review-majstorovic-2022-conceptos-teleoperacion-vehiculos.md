---
id: review-majstorovic-2022-conceptos-teleoperacion-vehiculos
titulo: "Survey on Teleoperation Concepts for Automated Vehicles (Majstorović, Hoffmann, Pfab, Schimpe, Wolf & Diermeyer 2022)"
tipo: revision
tema: Taxonomía y revisión sistemática de los conceptos de teleoperación de vehículos (remote driving vs remote assistance)
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [teleoperacion-supervision-remota, latencia-teleoperacion, teleoperacion-fallback, seguridad-funcional-av]
anio: 2022
autores: [Domagoj Majstorović, Simon Hoffmann, Florian Pfab, Andreas Schimpe, Maria-Magdalena Wolf, Frank Diermeyer]
referencia: https://arxiv.org/abs/2208.08876
motor: WebSearch (site:ieeexplore.ieee.org) + arXiv PDF full-text
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "3-6 (revisión de conceptos con prototipos y demostraciones industriales)"
metricas_clave: ["6 conceptos de teleoperación clasificados", "44 referencias técnicas revisadas", "patentes 'vehicle teleoperation' pasan de ~decenas (2000) a >900 publicadas en 2021 (Google Patents)"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Pregunta / objetivo de investigación
Sistematizar los conceptos de teleoperación de vehículos de carretera propuestos en la literatura, agruparlos por funcionalidad técnica respecto del pipeline de conducción automatizada (SENSE–PLAN–ACT) y mapear la actividad industrial y de patentes en el campo.

## Hipótesis
No existe una hipótesis experimental: es una revisión. Supuesto de partida: la teleoperación es una solución de respaldo (fallback) viable para los límites del ODD y los casos borde de la conducción automatizada, y los distintos conceptos coexistirán en vez de converger a uno.

## Metodología
- **Diseño:** revisión de literatura + análisis de patentes/actividad industrial.
- **Datos / muestra:** publicaciones desde 1995 (Kay & Thorpe) hasta 2022; búsqueda de patentes "vehicle teleoperation" en Google Patents (2000–2021, inglés).
- **Técnicas:** clasificación por funcionalidad respecto de módulos del pipeline AD; taxonomía apoyada en SAE J3016:2021, BSI Flex 1890 y BSI PAS 1880.
- **Métricas:** número de publicaciones por concepto, dispositivos de entrada, patentes por año.

## Resultados principales
- Taxonomía adoptada de tres términos paraguas: **Remote Driving** ("System is fully under remote control"), **Remote Assistance** (el sistema recibe asistencia puntual pero sigue a cargo de la tarea de conducción) y **Remote Monitoring** (monitoreo con posibilidad de intervención muy limitada).
- Seis conceptos técnicos: **Direct Control**, **Shared Control**, **Trajectory Guidance** (los tres dentro de remote driving), **Waypoint Guidance**, **Interactive Path Planning** y **Perception Modification** (remote assistance).
- **Direct Control** (el más parecido al telecomando "conducir a distancia"): "the direct control concept has reached a high degree of maturity and is the subject of numerous publications" — pero persisten desafíos: "The performance of the human operator as well as the safety of the vehicle is highly dependent on the latency [32] and stability of the mobile network [34]".
- Mitigaciones documentadas para el control directo: **predictive display** (Chucholowski), **Free Corridor** de Tang et al. — "introduced the Free Corridor to reach a safe end state in the event of a connection failure" — y **Predictive Corridor** (Graf et al.), que combina ambos.
- Los conceptos que delegan el lazo rápido al vehículo (waypoint guidance) son "more robust in the face of network latency issues", a costa de conducción tipo pare-y-siga (stop-and-go) y menor intervención dinámica.
- Actividad industrial amplia: Zoox, Ottopia, Motional, Volkswagen/Fernride, DriveU, EasyMile, Einride, **Mercedes-Benz**, entre otras, con crecimiento exponencial de patentes hasta 2021.

## Conclusiones
Existe una variedad de conceptos de teleoperación capaces de manejar distintos modos de falla o límites de ODD; no todos tienen la misma relevancia y coexistirán como soluciones de respaldo. La elección del concepto es un problema de diseño de sistema (cuánta autonomía queda en el vehículo vs cuánto lazo cierra el operador por la red).

## Limitaciones
- Revisión centrada en **vehículos de carretera** (autos, shuttles, algunos camiones en simulación); no cubre maquinaria minera ni faenas industriales.
- No entrega umbrales cuantitativos propios de latencia ni requisitos de red: remite a la literatura específica (ver [[review-kamtam-2024-latencia-red-teleoperacion-cav]]).
- Corte de datos 2022: no incluye la normalización posterior (BSI Flex 1886/1887, trabajos de ODD de teleoperación).

## Relevancia / brecha para el estado del arte
Es el mapa de referencia para ubicar cualquier proyecto de teleoperación: permite declarar sin ambigüedad si lo que se hará es *direct control / remote driving* (lazo humano cerrado por red, sensible a latencia) o *remote assistance*. Deja explícito que el concepto de control y la estrategia de estado seguro ante falla de enlace (free corridor, predictive corridor) son elementos de **diseño de sistema aún abiertos**, no resueltos por el equipamiento de fábrica. Relacionada con [[paper-brettin-2025-fallback-perdida-conexion-conduccion-remota]] y [[paper-testouri-2025-5g-teleoperacion-evaluacion-experimental]].

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
