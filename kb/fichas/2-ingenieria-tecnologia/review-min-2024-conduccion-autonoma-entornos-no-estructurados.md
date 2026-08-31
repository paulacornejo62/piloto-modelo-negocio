---
id: review-min-2024-conduccion-autonoma-entornos-no-estructurados
titulo: "Autonomous Driving in Unstructured Environments: How Far Have We Come? (Min et al. 2024)"
tipo: revision
tema: Brecha entre conducción autónoma en entornos estructurados (madura) y no estructurados/semi-estructurados (abierta)
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [vehiculo-autonomo-carga, entorno-semi-estructurado, percepcion-obstaculos-outdoor]
anio: 2024
autores: [Chen Min, Shubin Si, Xu Wang, Hanzhang Xue, Weizhong Jiang, Yang Liu, Juan Wang, Qingtian Zhu]
referencia: https://arxiv.org/abs/2410.07701
motor: WebSearch + arXiv (HTML full-text, lectura parcial de secciones)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: ["revisión de percepción, mapeo, localización y planificación en entornos no estructurados"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
Sistematizar el estado del arte de la conducción autónoma fuera de entornos estructurados (sin señalización, marcas ni geometría estandarizada) y determinar qué está resuelto y qué sigue abierto.

## Hipótesis
No experimental. Tesis de trabajo: los métodos maduros de entorno urbano estructurado no transfieren directamente a entornos no estructurados por ausencia de los elementos que esos métodos asumen.

## Metodología
- **Diseño:** revisión de literatura por bloques funcionales (percepción, mapeo, estimación de pose, planificación) y datasets.

## Resultados principales
- En entornos no estructurados la información útil de los mapas previos cae drásticamente por la falta de señales, marcas y calzada pavimentada.
- La complejidad semántica (bordes difusos, categorías confundibles) excede la del entorno estructurado y dificulta definir características con reglas previas.
- Pose/localización: dependencia de GNSS vulnerable a interferencia y de mapas previos.
- Está relativamente resuelto: SLAM offline con fusión LiDAR/GNSS, odometría visual y LiDAR en varios escenarios, traversabilidad con deep learning, planificación por búsqueda/muestreo.

## Conclusiones
Persisten desafíos fundamentales en percepción, mapeo actualizable y planificación bajo incertidumbre alta cuando el entorno no es estructurado.

## Limitaciones
El foco son entornos off-road/agrícolas/forestales; un recinto logístico privado es **semi-estructurado** (intermedio): tiene caminos definidos pero carece de la infraestructura vial estandarizada. La transferencia debe declararse como analogía, no como equivalencia.

## Relevancia / brecha para el estado del arte
Es la referencia clave para la discusión Frascati indoor-vs-outdoor: sostiene con literatura que la madurez de la autonomía cae al salir del entorno estructurado, lo que permite distinguir integración estándar (AGV indoor, ruta fija) de conocimiento nuevo (operación outdoor semi-estructurada con tráfico mixto).

**Citas textuales:**
- "Even in unstructured environments where pre-collection of data is possible, the lack of key traffic elements like signs, markings, and paved roads leads to a drastic reduction in the amount of useful information contained in the prior maps."
- "The complexity of unstructured environments significantly exceeds that of structured environments."

> Relaciones con otras fichas → `../../indice.json`.
