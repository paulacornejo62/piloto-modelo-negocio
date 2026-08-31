---
id: paper-waiwanijchakij-2024-uwb-navegacion-camion-autonomo-industrial
titulo: "Enhancing Autonomous Truck Navigation with Ultra-Wideband Technology in Industrial Environments (Waiwanijchakij et al. 2024)"
tipo: paper
tema: Posicionamiento híbrido UWB + GPS + LiDAR para navegación de camiones autónomos en recintos industriales
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [conectividad-vehiculo-autonomo, entorno-semi-estructurado, v2i-iot-logistica]
anio: 2024
autores: [Pairoj Waiwanijchakij, Thanapat Chotsiri, Pisit Janpangngern, Chanchai Thongsopa, Thanaset Thosdeekoraphat, Nuchanart Santalunai, Samran Santalunai]
referencia: https://doi.org/10.3390/s24154988
motor: WebSearch + PMC (PMC11314802, full-text open access) — Sensors
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "4-6 (sistema RTLS integrado, validación en entorno industrial)"
metricas_clave: ["UWB: precisión dentro de 0,2 cm el 99% del tiempo", "GPS aislado ~10 cm", "LiDAR aislado ~5 cm", "degradación por interferencia metálica: GPS -40%, LiDAR -25%"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
Evaluar si un sistema de localización en tiempo real (RTLS) basado en UWB, integrado con GPS, LiDAR y cámaras, mejora la navegación de camiones autónomos en entornos industriales donde el GNSS se degrada.

## Hipótesis
Un enfoque híbrido multi-sensor con UWB (TDoA) mantiene precisión de posicionamiento donde GPS y LiDAR se degradan por obstrucción, estructuras metálicas o condiciones ambientales.

## Metodología
- **Diseño:** desarrollo y evaluación de un FI-RTLS con algoritmo TDoA y anclas sincronizadas, integrado con GPS/LiDAR/cámaras.
- **Métricas:** precisión de posicionamiento y degradación bajo interferencia.

## Resultados principales
- UWB integrado alcanza precisión dentro de **0,2 cm el 99% del tiempo**, frente a ~10 cm de GPS y ~5 cm de LiDAR aislados.
- Bajo interferencia metálica, el desempeño de GPS cae ~40% y el de LiDAR ~25%, mientras UWB se mantiene estable.
- Limitaciones señaladas: costo e infraestructura de anclas, sincronización exigente (cableada), multipath en superficies reflectantes.

## Conclusiones
En recintos industriales la localización robusta requiere infraestructura de posicionamiento adicional al GNSS; el enfoque híbrido multi-sensor es la vía recomendada.

## Limitaciones
Validación en un entorno industrial específico; escalabilidad y costo de despliegue de anclas son barreras reconocidas por los propios autores.

## Relevancia / brecha para el estado del arte
Evidencia directa de que en un recinto (naves, estructuras metálicas, patios) **el GNSS no basta** y hay que diseñar la infraestructura de posicionamiento/conectividad del recinto. Es material para justificar como I+D la capa de infraestructura (anclas/APs, cobertura, integración) del piloto Kaufmann.

**Citas textuales:**
- "UWB technology consistently achieves positioning accuracy within 0.2 cm 99% of the time, significantly surpassing the 10 cm and 5 cm accuracies of GPS and LiDAR."
- "UWB is known for its ability to maintain high levels of performance in environments with physical and radio frequency interference, which are common in industrial applications."

> Relaciones con otras fichas → `../../indice.json`.
