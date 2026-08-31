---
id: paper-chen-2022-ann-prediccion-n-excretado-vacas
titulo: "Comparación de regresión lineal múltiple, random forest, support vector regression y red neuronal artificial para predecir nitrógeno excretado en vacas lecheras (Chen, Zheng, Wang & Yan, 2022) — título exacto tal como publicado no transcrito por la fuente de este trabajo, ver DOI/PMC"
tipo: paper
tema: Comparación de métodos de machine learning para predecir nitrógeno excretado en vacas lecheras
area_oecd: "4 Ciencias Agrícolas (4.2 Ciencia animal y lechera)"
topicos: [prediccion-desde-variables-animales]
anio: 2022
autores: ["Xianjiang Chen, Zheng, Wang, Yan — nombres completos no provistos en la fuente de este trabajo; cita corta: Chen, Zheng, Wang & Yan (2022)"]
referencia: https://doi.org/10.1038/s41598-022-16490-y (Scientific Reports)
motor: WebFetch (PMC)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: ["ANN: mejor RMSE y mayor CCC vs. otros 3 métodos", "R²=0.83 (mejor modelo, 6 variables)", "n=951 vacas lecheras, 43 estudios"]
fecha_registro: 2026-08-21
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Comparar el desempeño de cuatro métodos —regresión lineal múltiple, random forest, support vector regression y red neuronal artificial (ANN)— para predecir el nitrógeno excretado por vacas lecheras.

## Hipótesis
Que un modelo de red neuronal artificial puede superar a los métodos estadísticos/de machine learning clásicos (regresión lineal, random forest, SVR) en la predicción de N excretado, usando variables de dieta y desempeño del animal.

## Metodología
- **Diseño:** estudio comparativo de métodos predictivos sobre datos recopilados de múltiples fuentes.
- **Datos / muestra:** 951 vacas lecheras, provenientes de 43 estudios.
- **Técnicas:** regresión lineal múltiple, random forest, support vector regression (SVR) y red neuronal artificial (ANN) — todas entrenadas sobre el mismo conjunto de variables de entrada.
- **Métricas:** RMSE (raíz del error cuadrático medio) y CCC (coeficiente de concordancia).

## Resultados principales
- La **ANN ganó a los otros 3 métodos** (menor RMSE, mayor CCC).
- Mejor modelo: **6 variables de entrada** (N ingerido, N de la dieta, producción de leche, proporción de forraje, peso vivo, energía metabolizable).
- Arquitectura pequeña: **2 capas ocultas, 3 y 6 neuronas**.
- **R²=0.83** para el mejor modelo.

## Conclusiones
Una red neuronal artificial relativamente pequeña (pocas capas/neuronas) y con pocas variables de entrada puede superar a métodos estadísticos clásicos y a otros métodos de ML para predecir N excretado en ganado lechero.

## Limitaciones
Es sobre **vacas lecheras, no cerdos** — problema biológico distinto (predicción a partir de la relación leche/dieta vs. purín porcino). **No es predicción de series de tiempo real** — es una predicción estática dado el estado actual del animal (variables de dieta/desempeño en un momento dado), no una proyección "a 7 días" como el modelo real de Agrosuper.

## Relevancia / brecha para el estado del arte
Respalda metodológicamente la decisión de usar una **red neuronal en vez de regresión simple** (como en Jørgensen et al. 2013) para el modelo de purines del Objetivo 2 — es un precedente concreto de que una ANN gana con **pocas variables y pocas neuronas**, no requiere arquitecturas masivas para superar a la regresión. No cubre, sin embargo, el componente de series de tiempo que sí necesita el modelo de Agrosuper (ver relación con [[paper-wu-2024-cnn-gru-ambiente-nave-porcina]]).

Relacionada con [[paper-wu-2024-cnn-gru-ambiente-nave-porcina]] (ambos son precedentes de redes neuronales en contexto ganadero/porcino, pero ninguno combina ambos elementos que sí necesita Agrosuper: serie de tiempo + composición N/P de purín).

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
