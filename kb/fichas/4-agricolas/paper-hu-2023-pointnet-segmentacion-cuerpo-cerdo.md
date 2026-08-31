---
id: paper-hu-2023-pointnet-segmentacion-cuerpo-cerdo
titulo: "An improved PointNet++ point cloud segmentation model applied to automatic measurement method of pig body size (Hu et al., 2023)"
tipo: paper
tema: Segmentación de nube de puntos porcina con PointNet++ mejorado para medición automática del tamaño corporal
area_oecd: "4 Ciencias Agrícolas (4.2 Ciencia animal y lechera)"
topicos: [prediccion-peso-volumen-vision]
anio: 2023
autores: [Hu, et al.]
referencia: https://doi.org/10.1016/j.compag.2022.107560
motor: WebSearch (índice de bibliografía de la consultora)
profundidad_lectura: abstract
estado_evidencia: parcial
trl_relevante: "-"
metricas_clave: ["Errores relativos 2.2-5.3% según medida corporal"]
fecha_registro: 2026-08-21
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Desarrollar una versión mejorada de PointNet++ para segmentar la nube de puntos 3D de un cerdo y medir automáticamente distintas dimensiones de su tamaño corporal.

## Hipótesis
Que una versión mejorada de la arquitectura PointNet++ puede segmentar con precisión las distintas partes del cuerpo de un cerdo en una nube de puntos 3D, permitiendo mediciones corporales automáticas y precisas.

## Metodología
- **Diseño:** no confirmable en profundidad — solo se accedió al abstract (paywall).
- **Datos / muestra:** cerdos capturados como nube de puntos 3D.
- **Técnicas:** arquitectura PointNet++ mejorada para segmentación de nube de puntos.
- **Métricas:** error relativo por tipo de medida corporal.

## Resultados principales
- **Errores relativos de 2.2% a 5.3%**, según la medida corporal específica evaluada.

## Conclusiones
Una versión mejorada de PointNet++ permite segmentar y medir automáticamente distintas dimensiones corporales de un cerdo con errores relativos bajos (2.2-5.3%), variando según la medida.

## Limitaciones
**Solo se accedió al abstract** (paywall) — `profundidad_lectura: abstract`, `estado_evidencia: parcial`. No se confirma si el modelo fue validado en condiciones de granja comercial real o solo en laboratorio. Mide **tamaño corporal**, no directamente el peso — requeriría un paso adicional de conversión tamaño→peso.

## Relevancia / brecha para el estado del arte
Antecedente técnico de segmentación de nube de puntos porcina con precisión relativamente alta — parte del corpus de visión 3D aplicada a cerdos (junto con el paper de malla/DNN de peso 2023), relevante como referencia de las técnicas de procesamiento de nube de puntos disponibles para estimación de variables corporales porcinas, insumo potencial para el Objetivo 2 de Agrosuper si se explorara una vía de visión (no es el enfoque descrito por el equipo técnico, que usa cantidad/sexo/edad/peso declarado, no visión).

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
