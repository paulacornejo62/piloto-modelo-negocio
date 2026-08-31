---
id: paper-serhat-2024-sensor-multiespectral-cadena-frio-pollo
titulo: "Low-cost multispectral sensor reveals cold chain breaks, meat type, and storage time in chicken meat samples (Serhat et al., 2024/2025)"
tipo: paper
tema: Sensor multiespectral de bajo costo + clasificador SVC para detectar quiebre de cadena de frío, tipo de producto y tiempo de almacenamiento en pollo
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [sensor-multiespectral-cadena-frio]
anio: 2024
autores: [Serhat, et al.]
referencia: https://doi.org/10.1016/j.foodcont.2024.110816
motor: PDF directo (texto completo en carpeta, compartido por consultora)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: ["93% accuracy detectando quiebre de cadena de frío", "92% accuracy tipo de producto", "83% accuracy tiempo de almacenamiento"]
fecha_registro: 2026-08-21
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Evaluar si un sensor multiespectral de bajo costo (AS7265x), combinado con un clasificador SVC (support vector classifier), puede detectar quiebres de cadena de frío, tipo de producto y tiempo de almacenamiento en muestras de carne de pollo.

## Hipótesis
Que la firma espectral capturada por un sensor multiespectral de bajo costo contiene suficiente información para clasificar, mediante un modelo SVC, el estado de la cadena de frío, el tipo de producto y el tiempo de almacenamiento de la carne de pollo.

## Metodología
- **Diseño:** experimental — captura espectral + clasificación supervisada.
- **Datos / muestra:** muestras de carne de pollo con distintas condiciones de cadena de frío, tipo de producto y tiempo de almacenamiento.
- **Técnicas:** sensor multiespectral de bajo costo AS7265x + clasificador SVC (support vector classifier).
- **Métricas:** accuracy de clasificación por tarea.

## Resultados principales
- **93% de accuracy** detectando quiebre de cadena de frío.
- **92% de accuracy** clasificando tipo de producto.
- **83% de accuracy** clasificando tiempo de almacenamiento.

## Conclusiones
Un sensor multiespectral de bajo costo, combinado con un clasificador SVC relativamente simple, logra accuracy alta (83-93% según tarea) para tres tareas de control de calidad/trazabilidad en carne de pollo, sin requerir instrumentación de laboratorio costosa.

## Limitaciones
Ficha registrada con menor nivel de detalle (prioridad TIER 2); el PDF completo está disponible en carpeta. No aborda predicción de peso ni composición de purín — es un sensor de calidad/trazabilidad post-proceso, no de proceso productivo.

## Relevancia / brecha para el estado del arte
Evidencia de que sensórica de bajo costo + ML simple (SVC, no deep learning) puede lograr accuracy alta en tareas de control de calidad cárnica — relevante como antecedente de la viabilidad de soluciones sensóricas económicas en la industria cárnica, aunque de un dominio distinto (trazabilidad de cadena de frío) al de los Objetivos 2 y 4 de Agrosuper.

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
