---
id: paper-sefeedpari-2024-emisiones-purin-cerdos
titulo: Model Adaptation and Validation for Estimating Methane and Ammonia Emissions from Fattening Pig Houses (Sefeedpari, Pishgar-Komleh & Aarnink, 2024)
tipo: paper
tema: Predicción de composición de estiércol y emisiones NH3/CH4 desde variables de desempeño animal
area_oecd: "4 Ciencias Agrícolas (4.2 Ciencia animal y lechera)"
topicos: [purin-porcino-caracterizacion, prediccion-desde-variables-animales]
anio: 2024
autores: [Paria Sefeedpari, Seyyed Hassan Pishgar-Komleh, Andre J A Aarnink]
referencia: https://doi.org/10.3390/ani14060964 (PMC10967431, Animals 14(6):964)
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
Adaptar y validar un modelo (dinámico, basado en balance de masa) para estimar el desempeño animal, la cantidad/composición del estiércol producido, y las emisiones de metano y amoníaco de galpones de cerdos en engorda.

## Hipótesis
Que un modelo mecanístico alimentado con datos de manejo del galpón (peso inicial/final, duración del periodo, consumo de alimento y agua, condiciones climáticas, características del sistema de manejo de estiércol) puede reproducir con precisión el desempeño animal observado y, a partir de él, las emisiones.

## Metodología
- **Diseño:** adaptación y validación de un modelo dinámico existente contra datos reales de granjas.
- **Datos / muestra:** duración del periodo de producción, peso inicial y final, consumo total de alimento y agua, composición de la dieta, temperatura/humedad, especificaciones del edificio y tiempo de almacenamiento del estiércol.
- **Técnicas:** modelo de balance de masa (no es una red neuronal) que calcula día a día el peso, consumo de alimento/agua del animal, y de ahí deriva cantidad y composición del estiércol (incluido nitrógeno amoniacal total, TAN) y las emisiones de NH3/CH4 por fuente (canales, pisos, áreas ensuciadas).
- **Métricas:** comparación de las emisiones/composición estimadas contra mediciones de granja.

## Resultados principales
- El modelo predice el desempeño animal (peso, consumo de alimento y agua por día) y a partir de él deriva la cantidad y composición del estiércol.
- Calcula nitrógeno amoniacal total (TAN) desagregado por fuente dentro del galpón.

## Conclusiones
Un modelo alimentado únicamente con variables de manejo del animal y del galpón (sin mediciones químicas directas del purín) puede estimar razonablemente la composición del estiércol y sus emisiones.

## Limitaciones
Es un modelo mecanístico/determinístico (balance de masa), no un modelo de aprendizaje automático ni una red neuronal de series de tiempo. No predice DQO ni SST explícitamente (se enfoca en TAN, metano y desempeño animal). No incluye sexo como variable de entrada explícita en lo revisado.

## Relevancia / brecha para el estado del arte
Confirma el precedente de que peso, edad (duración del periodo) y consumo de alimento/agua son predictores válidos de la composición del estiércol — la misma familia de variables de entrada que usa el modelo real de Agrosuper (cantidad/sexo/edad/peso). Pero el enfoque es mecanístico, no una red neuronal de series de tiempo con ventana de pronóstico de 7 días hacia el digestor anaerobio, y no predice conjuntamente nitrógeno amoniacal + DQO + SST. Es literatura de respaldo para el vínculo "variables animales → composición del purín", no un precedente que replique el desarrollo de Agrosuper — sostiene la novedad, no la contradice.

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
