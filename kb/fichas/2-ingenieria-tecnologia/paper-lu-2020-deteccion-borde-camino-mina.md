---
id: paper-lu-2020-deteccion-borde-camino-mina
titulo: "Real-Time Mine Road Boundary Detection and Tracking for Autonomous Truck (Lu, Ai & Tian, 2020)"
tipo: paper
tema: Detección en tiempo real del borde de calzada en caminos NO pavimentados (mina) sin solera ni demarcación, con LiDAR
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [superficie-no-pavimentada, percepcion-obstaculos-outdoor, entorno-semi-estructurado, vehiculo-autonomo-carga]
anio: 2020
autores: [Xiaowei Lu, Yunfeng Ai, Bin Tian]
referencia: https://doi.org/10.3390/s20041121 (PMC7070413)
motor: WebSearch → PubMed Central (PMC7070413, open access)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "4-5 (prototipo probado en camión real a 23 km/h)"
metricas_clave: ["precisión 93,65% en tramo recto y 91,14% en curva", "recall 72,84% (recto) y 77,78% (curva)", "F1 81,94% / 83,93%", "LiDAR Velodyne HDL-32E, camión a 23 km/h, procesamiento en tiempo real en un i7-6700"]
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
¿Cómo detectar y seguir en tiempo real el borde de la calzada en un camino de mina —superficie no pavimentada, sin solera (curb) ni demarcación— para guiar un camión autónomo?

## Hipótesis
En ausencia de un borde físico o pintado, el límite de la calzada puede inferirse a partir de los obstáculos y la irregularidad del terreno detectados en la nube de puntos LiDAR, y estabilizarse por seguimiento temporal.

## Metodología
- **Diseño:** experimental, con vehículo real en camino minero.
- **Datos / muestra:** nubes de puntos de LiDAR Velodyne HDL-32E (32 canales, 40° vertical, 360° horizontal, alcance 70 m, precisión 2 cm) en tramos rectos y curvos, camión a 23 km/h.
- **Técnicas:** segmentación de suelo por doble malla, extracción de puntos candidatos por modelo de haces (720 regiones), filtrado de falsos positivos (clasificación + filtro de distancia + RANSAC) y seguimiento por filtro de Kalman.
- **Métricas:** precisión, recall y F1 de los puntos de borde detectados; tiempo de cómputo.

## Resultados principales
- Precisión 93,65% (recto) y 91,14% (curva); recall 72,84% y 77,78%; F1 81,94% y 83,93%.
- Operación en tiempo real sobre CPU industrial (Intel i7-6700) con el camión a 23 km/h.
- El recall (72-78%) es sustancialmente menor que la precisión: **una fracción relevante del borde real no se detecta**.

## Conclusiones
Es posible estimar el borde de un camino no pavimentado sin solera ni marcas, pero por inferencia indirecta (obstáculos y relieve del borde), no por detección de una marca. La calidad depende de que exista un accidente físico lateral discernible.

## Limitaciones
- Rendimiento degradado en pendientes pronunciadas (dispersión de la nube de puntos).
- Pocos puntos de borde en curvas cerradas.
- No aborda de forma completa los obstáculos sobre la calzada.
- Cita textual: *"There is no boundary between the road surface and the non-road surface in the mine road... The road boundary is determined based on the analysis and judgment of obstacles on the roadside."*
- Cita textual: *"The LiDAR scanning line is broken up by the clod or interrupted by the mound, thus it is difficult to extract the road boundary points."*

## Relevancia / brecha para el estado del arte
Evidencia directa de que en superficies no pavimentadas **el concepto de "borde de calzada" deja de estar dado por la infraestructura** y debe reconstruirse por percepción. Para el Centro Logístico Kaufmann (maicillo compactado, terreno plano abierto, demarcación que se pierde con la tierra) esto es peor que el caso de mina: un patio plano y despejado carece incluso de los taludes y montículos laterales que este método explota. La ausencia de referencia lateral física es una brecha técnica vigente, no un problema resuelto por producto.

> Relaciones: complementa a [[review-min-2024-conduccion-autonoma-entornos-no-estructurados]] y a [[paper-min-2022-orfd-freespace-offroad]].
