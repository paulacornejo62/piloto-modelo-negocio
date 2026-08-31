---
id: review-rutland-2023-ml-digestion-anaerobia
titulo: A Systematic Review of Machine-Learning Solutions in Anaerobic Digestion (Rutland, You, Liu, Bull & Reynolds, 2023)
tipo: revision
tema: Revisión sistemática de modelos de machine learning aplicados a digestión anaerobia
area_oecd: "2 Ingeniería y Tecnología (2.7 Ingeniería ambiental)"
topicos: [digestion-anaerobia-machine-learning, purin-porcino-caracterizacion]
anio: 2023
autores: [Harvey Rutland, Jiseon You, Haixia Liu, Larry Bull, Darren Reynolds]
referencia: https://pmc.ncbi.nlm.nih.gov/articles/PMC10740876/ (Bioengineering 10(12):1410)
motor: WebSearch + PMC
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: -
metricas_clave: []
fecha_registro: 2026-08-18
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Revisar sistemáticamente qué soluciones de machine learning se han aplicado a la digestión anaerobia (predicción, control, optimización) y qué vacíos quedan abiertos.

## Hipótesis
No aplica (es una revisión sistemática, no un estudio con hipótesis propia).

## Metodología
- **Diseño:** revisión sistemática de literatura.
- **Datos / muestra:** corpus de papers sobre ML aplicado a digestión anaerobia.
- **Técnicas cubiertas:** ANN, DNN, LSTM, CNN, RNN (redes neuronales); SVM, Random Forest, XGBoost, árboles de decisión (métodos tradicionales); métodos híbridos (p.ej. RF+LSTM); métodos emergentes (reinforcement learning, IA explicable). Cubre predicción a un paso y a múltiples pasos (series de tiempo).
- **Métricas:** no aplica (es meta-análisis de métricas reportadas por los estudios revisados).

## Resultados principales
- La mayoría de los modelos ML en digestión anaerobia se concentran en predecir biogás/metano, no nutrientes específicos como nitrógeno amoniacal o SST desde purín porcino.
- Identifica escasez de datos de entrenamiento como limitación transversal ("ML algorithms require large datasets to train on, and in many cases there may not be enough data available").
- Identifica falta de transferibilidad entre sistemas: modelos entrenados en un digestor no son directamente transferibles a otro si los parámetros operativos no se alinean.
- Reinforcement Learning aún no se ha aplicado en digestión anaerobia.

## Conclusiones
El campo tiene modelos ML maduros para biogás/metano, pero deja abierta la predicción conjunta de parámetros de carga específicos (como nitrógeno amoniacal, DQO, SST) desde variables de entrada no químicas.

## Limitaciones
Es una revisión, no aporta un modelo propio ni cifras de desempeño directamente comparables al caso de Agrosuper.

## Relevancia / brecha para el estado del arte
Evidencia a nivel de revisión (no un solo paper aislado) de que no existe consenso ni precedente consolidado de un modelo que combine: red neuronal de series de tiempo + predicción conjunta de nitrógeno amoniacal/DQO/SST + purín porcino + ventana de pronóstico de 7 días + variables de entrada animal (conteo/sexo/edad/peso). Respalda directamente el argumento de NOVEDAD del Objetivo 2 (Purines) para el formulario Ley I+D — junto con la escasez de datos y la falta de transferibilidad entre sistemas, que además sustentan la incertidumbre científico-tecnológica declarada.

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
