---
id: paper-wu-2024-cnn-gru-ambiente-nave-porcina
titulo: "Arquitectura híbrida BO-SE-CNN-GRU para predicción en tiempo real de temperatura, humedad, CO2 y amoníaco en naves porcinas (Wu, Xu, Chen, Liu & Song, 2024) — título exacto tal como publicado no transcrito por la fuente de este trabajo, ver DOI/PMC"
tipo: paper
tema: Red neuronal híbrida de series de tiempo para predicción ambiental en tiempo real en naves porcinas
area_oecd: "4 Ciencias Agrícolas (4.2 Ciencia animal y lechera)"
topicos: [monitoreo-ambiental-nave-porcina-ml]
anio: 2024
autores: ["Zhi Dong Wu, Xu, Chen, Liu, Song — nombres completos no provistos en la fuente de este trabajo; cita corta: Wu, Xu, Chen, Liu & Song (2024)"]
referencia: https://doi.org/10.1038/s41598-024-82492-7 (Scientific Reports)
motor: WebFetch (PMC)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: ["R²=0.988 para amoníaco", "Errores <1% para temperatura/humedad"]
fecha_registro: 2026-08-21
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Desarrollar un modelo que prediga en tiempo real, mediante series de tiempo, las condiciones ambientales (temperatura, humedad, CO2, amoníaco) dentro de una nave porcina.

## Hipótesis
Que una arquitectura híbrida que combine optimización bayesiana, redes convolucionales (CNN) y una red recurrente GRU puede predecir con alta precisión y en tiempo real las variables ambientales de una nave porcina real, a partir de series de tiempo de sensores.

## Metodología
- **Diseño:** desarrollo y validación de un modelo predictivo sobre datos de sensores de nave porcina real.
- **Datos / muestra:** series de tiempo de sensores ambientales (temperatura, humedad, CO2, amoníaco) en una nave porcina.
- **Técnicas:** arquitectura híbrida **BO-SE-CNN-GRU** (optimización bayesiana + red convolucional CNN + red recurrente GRU).
- **Métricas:** R² y error porcentual por variable predicha.

## Resultados principales
- La arquitectura predice en tiempo real temperatura, humedad, CO2 y amoníaco dentro de una nave porcina real.
- **R²=0.988 para amoníaco.**
- **Errores <1% para temperatura y humedad.**

## Conclusiones
Una red neuronal de series de tiempo (CNN+GRU con optimización bayesiana) es capaz de predecir con alta precisión variables ambientales críticas de una nave porcina en tiempo real, en un contexto porcino comercial real.

## Limitaciones
El modelo predice **condiciones ambientales de la nave (aire)** — temperatura, humedad, CO2, amoníaco —, **no composición del purín** (N/P). Es un problema distinto aunque de la misma familia de herramientas (redes recurrentes GRU/LSTM aplicadas a series de tiempo en contexto porcino).

## Relevancia / brecha para el estado del arte
Es el precedente metodológico **más parecido en espíritu** al modelo de purines descrito para el Objetivo 2 de Agrosuper: red neuronal + series de tiempo + granja porcina real, con métricas de alta precisión (R²=0.988). Junto con [[paper-chen-2022-ann-prediccion-n-excretado-vacas]], sostiene el argumento de que **no existe precedente publicado que combine ambos elementos** — una red neuronal de series de tiempo aplicada específicamente a predecir composición N/P de purín con ventana de pronóstico (p.ej. 7 días) — lo que constituye un vacío de estado del arte específico para el enfoque de Agrosuper, no una réplica de trabajo ya hecho.

Relacionada con [[paper-chen-2022-ann-prediccion-n-excretado-vacas]].

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
