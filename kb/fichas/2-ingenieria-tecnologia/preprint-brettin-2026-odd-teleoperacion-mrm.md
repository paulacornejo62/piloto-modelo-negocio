---
id: preprint-brettin-2026-odd-teleoperacion-mrm
titulo: "Teleoperation Operational Design Domain based on Minimal Risk Maneuver Capability (Brettin, Salem, Hans & Maurer 2026)"
tipo: preprint
tema: Definir el ODD de un sistema de teleoperación a partir de la capacidad del vehículo de ejecutar una maniobra de riesgo mínimo, no del desempeño de la red
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [recinto-privado-odd, teleoperacion-fallback, seguridad-funcional-av, teleoperacion-supervision-remota]
anio: 2026
autores: [Leon Johann Brettin, Nayel Fabian Salem, Ole Hans, Markus Maurer]
referencia: https://arxiv.org/abs/2605.29818
motor: WebSearch + arXiv (página de abstract)
profundidad_lectura: abstract
estado_evidencia: parcial
trl_relevante: "2-3 (propuesta conceptual con caso de uso)"
metricas_clave: ["preprint sin revisión por pares al momento de la consulta"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Pregunta / objetivo de investigación
¿Cómo definir el dominio operacional (ODD) de un sistema teleoperado, dado que la fiabilidad del enlace no puede garantizarse?

## Hipótesis
Basar el ODD de teleoperación en el desempeño de la red es frágil; conviene basarlo en la **capacidad del vehículo teleoperado de ejecutar una maniobra de riesgo mínimo** mediante un sistema dedicado.

## Metodología
- **Diseño:** propuesta conceptual (adaptación del concepto de ODD de la conducción automatizada al caso teleoperado), ilustrada con un caso de uso.
- No se accedió al texto completo: los elementos anteriores provienen del resumen publicado en arXiv.

## Resultados principales
- Los autores parten de que en las conexiones de red "it is almost impossible to guarantee sufficient reliability", lo que motiva desplazar el criterio de ODD desde la red hacia la capacidad de maniobra segura.
- Propuesta: el ODD del sistema de teleoperación queda determinado por dónde y cuándo el vehículo puede ejecutar una maniobra de riesgo mínimo por sí mismo.

## Conclusiones
(Preliminares — el manuscrito declara estar en preparación y sin revisión por pares.) La seguridad de un sistema teleoperado debería especificarse por su capacidad de fallo seguro autónomo, no por supuestos de disponibilidad de enlace.

## Limitaciones
- **Preprint sin revisión por pares**; sin resultados experimentales verificados.
- Solo se leyó el resumen; no hay verificación del caso de uso ni de las condiciones propuestas.

## Relevancia / brecha para el estado del arte
Es la formulación explícita, en 2026, de que la pregunta "¿cómo garantizo el enlace 100% del tiempo?" está mal planteada en la literatura reciente: el enfoque emergente es **diseñar el dominio de operación alrededor de la capacidad de detenerse con seguridad sin enlace**. Continúa la línea de [[paper-brettin-2025-fallback-perdida-conexion-conduccion-remota]] del mismo grupo (TU Braunschweig) y dialoga con la estrategia de estado de riesgo mínimo de [[norma-5gaa-2021-tod-arquitectura-requisitos]].

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
