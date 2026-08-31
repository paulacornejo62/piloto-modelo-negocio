---
id: review-patil-2026-montacargas-autonomos-brecha-despliegue
titulo: "Autonomous Forklifts for Warehouse Automation: A Comprehensive Review (Patil & Farzan, 2026)"
tipo: revision
tema: Revisión sistemática PRISMA de montacargas autónomos; brecha entre desempeño de laboratorio y despliegue industrial en espacios compartidos con personas
area_oecd: "2 Ingeniería y Tecnología (2.3 Ingeniería mecánica)"
topicos: [operacion-mixta-seguridad, logistica-de-patio-yard, vehiculo-autonomo-carga, entorno-semi-estructurado]
anio: 2026
autores: [Aditya Dilip Patil, Siavash Farzan]
referencia: https://doi.org/10.3390/robotics15020030
motor: WebSearch → MDPI (mirror mdpi-res.com, PDF; abstract e introducción leídos directamente)
profundidad_lectura: abstract
estado_evidencia: verificado
trl_relevante: "4-6 (validación mayoritariamente a escala de laboratorio, según los autores)"
metricas_clave: ["despliegue actual a pequeña escala: 2-50 vehículos", "122 artículos revisados (2010-2025), 80 métodos sintetizados", "localización ±1,4 mm y reconocimiento visual 98%+ en laboratorio", "marcos de seguridad reducen riesgo de vuelco 53-59%"]
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
¿Por qué, tras décadas de investigación, los montacargas autónomos siguen desplegados a escala mínima, y qué barreras específicas separan el desempeño publicado del despliegue industrial?

## Hipótesis
Las limitaciones no están en el desempeño puntual de los subsistemas (localización, control, visión), sino en la transición de la validación de laboratorio a entornos industriales con flotas grandes, carga variable y comportamiento humano impredecible.

## Metodología
- **Diseño:** revisión sistemática siguiendo PRISMA (no registrada prospectivamente, según declaran).
- **Datos / muestra:** 122 artículos revisados por pares (2010-2025) de IEEE Xplore, ACM, Elsevier y afines; 80 métodos sintetizados en 8 tablas comparativas.
- **Técnicas:** clasificación en ocho subsistemas (modelado del vehículo, localización, planificación, control, manipulación basada en visión, coordinación multivehículo, seguridad) con evaluación de calidad según rigor de validación.

## Resultados principales
- Cita textual: *"Despite decades of research, autonomous forklifts remain deployed at a small scale (2–50 vehicles), while industrial warehouses require coordinating hundreds of vehicles in environments shared with human workers."*
- Estado del arte en laboratorio: localización con precisión de ±1,4 mm, control de manipulación sub-centimétrico, planificación que reduce tiempos de misión 2-55%, visión con 98%+ de reconocimiento, marcos de seguridad que recortan el riesgo de vuelco 53-59%.
- Cita textual: *"However, validation predominantly occurs at laboratory scale, revealing a critical deployment gap. These achievements do not scale to industrial environments due to fleet coordination complexity, payload variability, and unpredictable human behavior."*
- Prioridades de investigación declaradas: coordinación de flotas mixtas, control mejorado por aprendizaje y **seguridad consciente del humano** ("human-aware safety").
- Sobre espacios compartidos: *"operations in shared workspaces require safety frameworks that offer formal guarantees without compromising productivity"*.

## Conclusiones
La coexistencia segura y productiva de vehículos autónomos con trabajadores y equipos tripulados en un recinto industrial real es un problema abierto que los autores sitúan como prioridad de investigación, no como capacidad disponible.

## Limitaciones
- Foco en montacargas de bodega (interior), no en vehículos de patio exterior sobre superficie no pavimentada: la extrapolación al caso al aire libre debe hacerse con cuidado.
- No revisada prospectivamente; síntesis cualitativa por subsistema.
- Lectura de esta ficha a nivel de resumen e introducción; secciones 11-13 (coordinación multivehículo, seguridad y direcciones futuras) no fueron leídas en detalle.

## Relevancia / brecha para el estado del arte
Aporta la contraparte industrial del riesgo del Centro Logístico Kaufmann: la calzada compartida con **grúas horquilla, camiones, buses y operarios cruzando**. Si en el entorno más controlado posible (bodega interior, piso plano, iluminación estable) la coexistencia con humanos sigue siendo declarada como brecha crítica de despliegue por una revisión de 122 artículos, la afirmación de que esa coexistencia está resuelta en un patio exterior de maicillo con polvo y neblina no es sostenible con la evidencia disponible.

> Relaciones: complementa a [[paper-meyer-2024-safe20-tractor-terminal-automatico-operacion-mixta]] y a [[paper-huemer-2025-adapt-montacargas-autonomo-outdoor]].
