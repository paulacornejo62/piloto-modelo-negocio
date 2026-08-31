---
id: paper-min-2022-orfd-freespace-offroad
titulo: "ORFD: A Dataset and Benchmark for Off-Road Freespace Detection (Min et al., ICRA 2022)"
tipo: paper
tema: Primer dataset y benchmark de detección de área transitable (freespace) fuera de carretera; comparación solo-cámara vs fusión cámara+LiDAR
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [freespace-traversabilidad, superficie-no-pavimentada, entorno-semi-estructurado, percepcion-obstaculos-outdoor]
anio: 2022
autores: [Chen Min, Weizhong Jiang, Dawei Zhao, Jiaolong Xu, Liang Xiao, Yiming Nie, Bin Dai]
referencia: https://arxiv.org/abs/2206.09907 (ICRA 2022, DOI 10.1109/ICRA46639.2022.9812139)
motor: WebSearch → arXiv (PDF full-text, tablas leídas directamente)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "3-4 (dataset y modelo de investigación)"
metricas_clave: ["solo RGB (cámara): F1 80,6% / IoU 67,5%", "RGB + normal de superficie desde LiDAR: F1 90,3% / IoU 82,3%", "brecha cámara-sola vs fusión: 14,8 puntos de IoU y 9,7 de F1", "12.198 pares nube de puntos + imagen; 1.856 frames con niebla, 1.971 con nieve, 4.510 en oscuridad"]
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
¿Cómo detectar el área transitable en entornos fuera de carretera (bosque, campo agrícola, pradera, camino rural), donde no hay calzada pavimentada ni bordes claramente delineados, y cuánto aporta la fusión LiDAR-cámara frente a la cámara sola?

## Hipótesis
Una sola modalidad no basta: la imagen RGB aporta semántica pero no estructura, y el LiDAR aporta geometría pero no semántica; la fusión dinámica (cross-attention) de ambas debería superar a cualquiera por separado.

## Metodología
- **Diseño:** construcción de dataset + benchmark comparativo de modelos.
- **Datos / muestra:** 12.198 pares sincronizados de nube de puntos LiDAR e imagen RGB, en cuatro escenas (bosque, campo agrícola, pradera, campo rural), cuatro climas (soleado 5.230, lluvia 3.141, **niebla 1.856**, nieve 1.971) y cuatro condiciones de luz (luz intensa 1.380, día 5.320, crepúsculo 1.588, **oscuridad 4.510**), en tres estaciones. Anotación de área transitable / no transitable / inalcanzable.
- **Técnicas:** OFF-Net, arquitectura Transformer con módulo de fusión dinámica por cross-attention entre la imagen RGB y la normal de superficie calculada desde el LiDAR. Comparación con FuseNet y SNE-RoadSeg.
- **Métricas:** accuracy, precision, recall, F-score, IoU.

## Resultados principales
- **Ablación de modalidad (Tabla 3):** solo RGB → accuracy 88,8%, F1 80,6%, IoU 67,5%. Solo normal de superficie → F1 88,2%, IoU 78,9%. RGB + profundidad dispersa → F1 83,2%, IoU 71,3%. **RGB + normal de superficie (fusión) → accuracy 94,5%, F1 90,3%, IoU 82,3%.**
- Es decir: pasar de cámara sola a fusión cámara+LiDAR sube el IoU de 67,5% a 82,3% (**+14,8 puntos**).
- La cross-attention sube el IoU de 80,9% a 82,3% frente a la fusión sin ella.
- Cita textual: *"The on-road environment provides many structural cues, such as lane markings and roadway signs while there are no well paved and clearly outlined roadways in off-road environment."*
- Cita textual: *"detecting freespace in an unstructured off-road environment is more challenging than in the on-road environment."*
- Los propios autores reportan casos de falla: *"there are some failure cases, especially when the scene is very unstructured."*

## Conclusiones
La detección de área transitable fuera de carretera es un problema abierto y sustancialmente más difícil que en vía estructurada; el LiDAR no es redundante sino determinante del desempeño, y aun con fusión quedan fallas en las escenas más desestructuradas.

## Limitaciones
- Escenas naturales (bosque/agro), no patios logísticos industriales con tráfico mixto.
- El benchmark mide segmentación, no seguridad operacional ni tasa de intervención.
- Un solo sitio de recolección por escena; generalización a otros terrenos no demostrada.

## Relevancia / brecha para el estado del arte
Es la evidencia cuantitativa más limpia para decidir entre **robo-shuttle (cámaras+LiDAR) y cargo van (solo cámaras)** en el Centro Logístico Kaufmann: en entorno no estructurado, quitar el LiDAR cuesta del orden de 15 puntos de IoU en la tarea básica de "dónde puedo circular". En un piso de maicillo compactado sin marcas —donde la superficie transitable y su entorno tienen color y textura casi idénticos— la variante solo-cámaras parte con una desventaja medida, no supuesta. Además confirma que el problema de "dónde está el camino" no está resuelto ni siquiera con fusión.

> Relaciones: complementa a [[paper-lu-2020-deteccion-borde-camino-mina]]; misma línea que [[review-min-2024-conduccion-autonoma-entornos-no-estructurados]] (mismo primer autor).
