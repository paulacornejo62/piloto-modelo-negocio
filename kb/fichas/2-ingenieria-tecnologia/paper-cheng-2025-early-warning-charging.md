---
id: paper-cheng-2025-early-warning-charging
titulo: "Early warning method for charging thermal runaway of EV lithium-ion battery based on charging network (Cheng et al. 2025)"
tipo: paper
tema: Alerta temprana de fuga térmica durante la carga usando datos de red de carga y modelo LSTM-TCN
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [deteccion-temprana-fuga-termica, carga-nocturna, bms-monitoreo]
anio: 2025
autores: [Yuan-Ming Cheng, De-Xin Gao, Feng-Ming Zhao, Qing Yang]
referencia: https://doi.org/10.1038/s41598-025-92738-7
motor: Europe PMC / PMC (PMC11885673)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 4
metricas_clave: ["1/3 de accidentes ocurren en carga", "R²≈0.99", "anticipación 9.95–27.95 s", "MAE 0.009 (NMC)"]
fecha_registro: 2026-07-14
proyectos:
  - lipigas
---

## Pregunta / objetivo de investigación
Predecir la temperatura de la batería y anticipar la fuga térmica durante la carga a partir de parámetros de la red de carga, dado que la carga es una fase crítica de accidentes.

## Hipótesis
Con seis parámetros de carga y un modelo híbrido LSTM-TCN se puede predecir la temperatura con alta precisión y detectar anomalías con anticipación suficiente para intervenir.

## Metodología
- **Diseño:** modelado predictivo con datos de red de carga EV.
- **Datos:** seis parámetros (voltaje/corriente de demanda, voltaje de celda, voltaje/corriente reales de carga, SOC).
- **Técnicas:** modelo híbrido LSTM-TCN; análisis de residuos con ventana deslizante para umbral de alerta.
- **Métricas:** MAE, RMSE, R², tiempo de anticipación.

## Resultados principales
- "thermal runaway of lithium-ion battery charging accounts for one-third of the total accidents" — la carga es momento crítico.
- Precisión: MAE 0.009 / RMSE 0.012 (NMC); MAE 0.027 / RMSE 0.037 (LFP); R²≈0.99.
- Anticipación de la alerta: 9.95–27.95 s antes del evento real; mejora de 9.4% en MAE y 10.2% en RMSE frente a modelos competidores.

## Conclusiones
El método da aviso suficiente para intervenciones protectoras durante la carga.

## Limitaciones
Investigación limitada de configuraciones de carga y diversidad histórica del dataset; se sugiere ampliar modelos de vehículo y estrategias de carga.

## Relevancia / brecha para el estado del arte
Directamente pertinente a la incertidumbre (2) de Lipigas: carga nocturna en instalaciones con almacenamiento de GLP. Confirma que la carga concentra ~1/3 de accidentes y que la detección en red de carga anticipa segundos-decenas de segundos (menos que el SOS por strain, ver paper-gu-2025). Refuerza necesidad de monitoreo del punto de carga.

> Relaciones con otras fichas → `../../indice.json`.
