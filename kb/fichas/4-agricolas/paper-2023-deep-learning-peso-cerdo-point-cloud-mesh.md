---
id: paper-2023-deep-learning-peso-cerdo-point-cloud-mesh
titulo: "Deep learning-based weight estimation using a fast-reconstructed mesh model from the point cloud of a pig (2023)"
tipo: paper
tema: Reconstrucción de malla desde nube de puntos + red neuronal profunda para estimar peso de cerdos
area_oecd: "4 Ciencias Agrícolas (4.2 Ciencia animal y lechera)"
topicos: [prediccion-peso-volumen-vision]
anio: 2023
autores: ["Autores no especificados en la fuente de este trabajo"]
referencia: https://doi.org/10.1016/j.compag.2023.107903
motor: WebSearch (índice de bibliografía de la consultora)
profundidad_lectura: abstract
estado_evidencia: parcial
trl_relevante: "-"
metricas_clave: ["97.89% de precisión reportada", "Tiempo de procesamiento <1s"]
fecha_registro: 2026-08-21
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Estimar el peso de cerdos vivos mediante una red neuronal profunda aplicada a una malla 3D reconstruida rápidamente a partir de una nube de puntos del animal.

## Hipótesis
Que una malla 3D reconstruida rápidamente desde una nube de puntos captura suficiente información geométrica para que una red neuronal profunda estime el peso del cerdo con alta precisión y baja latencia.

## Metodología
- **Diseño:** no confirmable en profundidad — solo se accedió al abstract (paywall).
- **Datos / muestra:** cerdos vivos, capturados como nube de puntos 3D.
- **Técnicas:** reconstrucción rápida de malla desde nube de puntos + red neuronal profunda (DNN) para estimación de peso.
- **Métricas:** precisión reportada y tiempo de procesamiento.

## Resultados principales
- **97.89% de precisión** reportada en la estimación de peso.
- Tiempo de procesamiento **menor a 1 segundo** por animal.

## Conclusiones
La combinación de reconstrucción rápida de malla 3D + red neuronal profunda permite estimar el peso de cerdos con alta precisión y en tiempo casi real (menos de 1 segundo).

## Limitaciones
**Solo se accedió al abstract** (paywall) — `profundidad_lectura: abstract`, `estado_evidencia: parcial`. Autores no identificados en la fuente de este trabajo. No se confirma el tamaño de muestra ni las condiciones de captura (granja comercial real vs. laboratorio controlado).

## Relevancia / brecha para el estado del arte
Antecedente directo de visión 3D + deep learning para estimación de peso porcino con alta precisión y baja latencia — parte del corpus de técnicas de estimación de peso/volumen por visión (junto con Nyalala 2021, Mortensen 2016, y el paper de volumen RGB-Depth), esta vez específicamente en cerdos, especie de mayor relevancia directa para el Objetivo 2 de Agrosuper que las referencias avícolas.

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
