---
id: paper-he-2024-yolo-oclusion-vehiculos
titulo: "Enhancing YOLO for occluded vehicle detection with grouped orthogonal attention and dense object repulsion (He, Chen, Liu, Luo & Liu, 2024)"
tipo: paper
tema: Degradación de YOLO estándar con objetos ocluidos (entre clases y dentro de la misma clase apilada); solución con atención y función de pérdida modificada
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [limitaciones-yolo-oclusion-transparencia]
anio: 2024
autores: [He, Chen, Liu, Luo, Liu]
referencia: https://doi.org/10.1038/s41598-024-70695-x
motor: WebFetch (PMC)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: ["+4.7% precisión vs. YOLOv5 base", "+3.6% AP@0.5 vs. YOLOv5 base"]
fecha_registro: 2026-08-21
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Mejorar la detección de vehículos ocluidos (parcialmente tapados por otros objetos o vehículos) mediante modificaciones a la arquitectura YOLO.

## Hipótesis
Que YOLO estándar sufre degradación significativa ante oclusión (entre clases distintas y dentro de la misma clase, como objetos apilados/superpuestos), y que módulos de atención especializados junto con una función de pérdida modificada pueden mitigar esa degradación.

## Metodología
- **Diseño:** desarrollo y evaluación de una variante de arquitectura YOLO.
- **Datos / muestra:** imágenes de vehículos con distintos grados de oclusión.
- **Técnicas:** módulo de atención ortogonal agrupada (grouped orthogonal attention) + función de pérdida de repulsión de objetos densos (dense object repulsion), integrados sobre YOLOv5 base.
- **Métricas:** precisión y AP@0.5, comparados contra YOLOv5 base.

## Resultados principales
- Confirma que YOLO estándar sufre **"degradación severa"** con oclusión, tanto entre clases distintas como dentro de la misma clase (objetos apilados/superpuestos).
- Requiere módulos de atención nuevos y una función de pérdida modificada — **no basta con más datos de entrenamiento** para resolver el problema.
- Mejora medida vs. YOLOv5 base: **+4.7% en precisión, +3.6% en AP@0.5**.

## Conclusiones
La oclusión es una limitación estructural de las arquitecturas YOLO estándar que requiere modificaciones arquitectónicas específicas (atención, función de pérdida) para mitigarse — agregar más datos de entrenamiento no es suficiente.

## Limitaciones
Es un estudio de detección de **vehículos**, no de piezas cárnicas — el dominio de aplicación es distinto, aunque el mecanismo de falla (degradación por oclusión) es transferible conceptualmente. Las mejoras (+4.7%/+3.6%) son significativas pero no eliminan el problema por completo.

## Relevancia / brecha para el estado del arte
**Relevante para la incertidumbre técnica del Objetivo 4** (piezas semicongeladas apiladas/pegadas): confirma con evidencia cuantitativa que YOLO estándar sin módulos adicionales sufre degradación real ante oclusión — respalda la incertidumbre técnico-científica declarada para ese objetivo, sin resolverla, y confirma que "más datos" no es la solución esperable.

Relacionada con [[preprint-zhang-2026-sep-yolo-objetos-transparentes]] — ambos papers calzan con el problema descrito por el equipo técnico de Agrosuper (piezas semicongeladas translúcidas y pegadas).

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
