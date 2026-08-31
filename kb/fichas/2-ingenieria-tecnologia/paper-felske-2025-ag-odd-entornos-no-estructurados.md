---
id: paper-felske-2025-ag-odd-entornos-no-estructurados
titulo: "Toward an Agricultural Operational Design Domain: A Framework (Felske, Redenius, Happich & Schöning, 2025)"
tipo: preprint
tema: Insuficiencia de los marcos ODD viales para entornos no estructurados y propuesta de un marco de ODD para operación agrícola
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [recinto-privado-odd, entorno-semi-estructurado, seguridad-funcional-av]
anio: 2025
autores: [Mirco Felske, Jannik Redenius, Georg Happich, Julius Schöning]
referencia: https://arxiv.org/abs/2511.02937
motor: WebSearch → arXiv (página de abstract)
profundidad_lectura: abstract
estado_evidencia: parcial
trl_relevante: "2-3 (marco conceptual)"
metricas_clave: ["modelo de 7 capas: extiende el modelo de 6 capas de PEGASUS con una capa de proceso", "usa ASAM OpenODD y CityGML como base de descripción"]
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
¿Sirven los conceptos de ODD desarrollados para conducción automatizada en vía pública para especificar el dominio operacional de máquinas autónomas en entornos no estructurados (agrícolas)?

## Hipótesis
No: los marcos ODD existentes están construidos sobre supuestos de la vía pública estructurada y no capturan ni la variabilidad del entorno no estructurado ni la integración entre conducir y trabajar.

## Metodología
- **Diseño:** propuesta de marco conceptual (Ag-ODD).
- **Técnicas:** (1) concepto de descripción sobre ASAM OpenODD y CityGML; (2) modelo de 7 capas que extiende el modelo de 6 capas de PEGASUS con una capa de proceso para las operaciones dinámicas; (3) proceso iterativo de verificación de completitud y consistencia contra escenarios lógicos.

## Resultados principales
- Cita textual: *"existing Operational Design Domain (ODD) concepts do not yet address the unique challenges of agricultural applications."*
- La automatización agrícola difiere porque *"integrates driving and working processes, each of which imposes distinct operational constraints."*
- El marco busca límites operacionales "unambiguous and verifiable".

## Conclusiones
La especificación del ODD para un entorno no estandarizado exige extender las taxonomías viales existentes; no basta con aplicar ISO 34503 / PAS 1883 tal cual.

## Limitaciones
- Preprint reciente (noviembre 2025), sin validación empírica reportada.
- Dominio agrícola, no logístico-industrial; la transferencia al caso de patio debe argumentarse.
- Lectura a nivel de abstract.

## Relevancia / brecha para el estado del arte
Aporta el respaldo conceptual a un componente central del proyecto Kaufmann: **caracterizar y validar el ODD de un recinto privado no estandarizado no tiene hoy un método aceptado y aplicable "de estantería"**. Las normas de ODD disponibles (ISO 34503, PAS 1883, ASAM OpenODD) fueron pensadas para la vía pública estructurada; los propios investigadores están proponiendo extensiones ad hoc para entornos no estructurados. En un patio de maicillo con calzada compartida, la definición del ODD (superficie, visibilidad mínima, densidad de polvo, actores) y su verificación son trabajo de desarrollo, no de configuración.

> Relaciones: complementa a [[review-mantouka-2026-odd-desafios-operacionales]] y a [[paper-anund-2022-lecciones-sitios-demo-shuttle-autonomo]].
