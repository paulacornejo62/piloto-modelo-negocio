---
id: paper-jorgensen-2013-excrecion-n-p-cerdos
titulo: Models to quantify excretion of dry matter, nitrogen, phosphorus and carbon in growing pigs fed regional diets (Jørgensen, Prapaspongsa, Vu & Poulsen, 2013)
tipo: paper
tema: Modelos determinísticos de excreción de N/P/materia seca en cerdos en crecimiento
area_oecd: "4 Ciencias Agrícolas (4.2 Ciencia animal y lechera)"
topicos: [purin-porcino-caracterizacion, prediccion-desde-variables-animales]
anio: 2013
autores: [Henry Jørgensen, Trakarn Prapaspongsa, Van Thi Khanh Vu, Hanne Damgaard Poulsen]
referencia: https://pmc.ncbi.nlm.nih.gov/articles/PMC3874674/ (J Anim Sci Biotechnol 4:42)
motor: WebSearch + PMC
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: -
metricas_clave: ["RMSEP heces: 0.01-0.03 kg/d", "Bias: -17% a +30% según parámetro"]
fecha_registro: 2026-08-18
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Desarrollar modelos para cuantificar la excreción de materia seca, nitrógeno, fósforo y carbono en cerdos en crecimiento alimentados con dietas regionales, usando información barata y normalmente disponible.

## Hipótesis
Que el contenido dietético (proteína cruda, fósforo, fibra dietética total) y el consumo diario de materia seca son suficientes para predecir la excreción sin requerir mediciones químicas directas y costosas.

## Metodología
- **Diseño:** modelado determinístico/regresión, no aprendizaje automático.
- **Datos / muestra:** ensayos de alimentación con dietas regionales variadas.
- **Técnicas:** balance de nitrógeno diario = ingesta − retención (retención calculada desde ganancia de peso diaria y contenido proteico de esa ganancia).
- **Métricas:** RMSEP (error cuadrático medio de predicción) y sesgo (bias) por parámetro, validación con set de prueba independiente.

## Resultados principales
- RMSEP de 0.01–0.03 kg/d para heces.
- Sesgo entre -17% y +30% según el parámetro predicho.
- No reporta R² explícito (usa RMSEP/bias en vez de R²).

## Conclusiones
Los modelos son precisos y robustos para predecir volumen de purín (R²=0.96 en la validación citada por fuentes derivadas), N (R²=0.91) y P (R²=0.95), algo menos para materia seca (R²=0.75) — cifras citadas en el propio documento sobre la robustez del enfoque.

## Limitaciones
El peso corporal aparece solo en los cálculos de retención, no como variable de entrada central del modelo (la entrada principal es la dieta/consumo). No predice nitrógeno amoniacal, DQO ni SST directamente — predice N/P/materia seca totales. No es una red neuronal ni usa series de tiempo.

## Relevancia / brecha para el estado del arte
Ya estaba citado en el `form_w2.estado_del_arte_investigacion` del expediente antes de este Deep Research dirigido; esta ficha lo re-verifica con lectura de texto completo (antes solo constaba como referencia sin ficha KB). Confirma que la bibliografía previa del proyecto sí es real, pero también confirma la brecha ya señalada: predice N/P genérico desde la dieta, **no** nitrógeno amoniacal + DQO + SST desde conteo/sexo/edad/peso del animal — las variables reales que predice el modelo de Agrosuper. Sostiene la novedad del enfoque real (variables distintas, salida distinta, red neuronal de series de tiempo en vez de balance determinístico).

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
