---
id: paper-2023-volumen-rgb-depth-point-cloud-alimentos
titulo: "Measuring food volume from RGB-Depth image with point cloud conversion method (ellipsoid fitting) (2023)"
tipo: paper
tema: Estimación de volumen de alimentos desde nube de puntos RGB-D mediante ajuste de elipsoide
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [prediccion-peso-volumen-vision]
anio: 2023
autores: ["Autores no especificados en la fuente de este trabajo"]
referencia: https://doi.org/10.1016/j.jfoodeng.2023.111656
motor: WebSearch (índice de bibliografía de la consultora)
profundidad_lectura: abstract
estado_evidencia: parcial
trl_relevante: "-"
metricas_clave: ["Error 2.6-3.1% según forma del alimento"]
fecha_registro: 2026-08-21
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Desarrollar un método para estimar el volumen de alimentos a partir de una imagen RGB-Depth, convirtiéndola a nube de puntos y ajustando un elipsoide sobre la forma del alimento.

## Hipótesis
Que el ajuste de un elipsoide sobre la nube de puntos derivada de una imagen RGB-Depth permite estimar el volumen del alimento con un error acotado, sin requerir modelos 3D complejos.

## Metodología
- **Diseño:** no confirmable en profundidad — solo se accedió al abstract (paywall).
- **Datos / muestra:** alimentos de distintas formas, capturados con cámara RGB-Depth.
- **Técnicas:** conversión de imagen RGB-D a nube de puntos + ajuste de elipsoide (ellipsoid fitting).
- **Métricas:** error porcentual de volumen estimado vs. real.

## Resultados principales
- Error de estimación de volumen de **2.6% a 3.1%, según la forma del alimento**.

## Conclusiones
El método de ajuste de elipsoide sobre nube de puntos RGB-D logra una estimación de volumen de alimentos con error relativamente bajo (bajo 3.1%), variando según la complejidad geométrica del alimento.

## Limitaciones
**Solo se accedió al abstract** (paywall, no se leyó el cuerpo del artículo) — `profundidad_lectura: abstract`, `estado_evidencia: parcial`. Autores no identificados en la fuente de este trabajo. No se conoce el tipo de alimento evaluado ni si incluye piezas cárnicas semicongeladas (relevante para el caso de Agrosuper).

## Relevancia / brecha para el estado del arte
Antecedente metodológico de estimación de volumen desde visión 3D (RGB-D) con error acotado y bajo — parte del corpus de técnicas de estimación de peso/volumen por visión (junto con Nyalala 2021, Mortensen 2016), aunque no confirmado si aplica a piezas cárnicas semicongeladas translúcidas, que es el caso específico de mayor incertidumbre técnica para el Objetivo 4 de Agrosuper.

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
