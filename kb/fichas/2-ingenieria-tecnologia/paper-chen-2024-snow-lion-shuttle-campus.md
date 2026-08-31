---
id: paper-chen-2024-snow-lion-shuttle-campus
titulo: "Enhancing Campus Mobility: Achievements and Challenges of Autonomous Shuttle 'Snow Lion' (Chen, Cheng, Wang, Jiao, Wang & Liu, 2024)"
tipo: preprint
tema: Despliegue de dos meses de un shuttle autónomo de 6 pasajeros en campus universitario (HKUST Guangzhou) con métricas de intervención
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [vehiculo-autonomo-shuttle, disengagement-kpi-piloto, localizacion-gnss-rtk, recinto-privado-odd]
anio: 2024
autores: [Yingbing Chen, Jie Cheng, Sheng Wang, Jianhao Jiao, Lujia Wang, Ming Liu]
referencia: https://arxiv.org/abs/2401.08939
motor: WebSearch → arXiv (HTML full-text)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 6-7
metricas_clave: ["1146 km recorridos y 442 pasajeros en 2 meses", "13.34 km por intervención manual (takeover)", "1 frenada brusca (<=-1 m/s2) cada 0.77 km", "velocidad promedio 7.41 km/h (máx 11.76 km/h)", "vehículo de 6 pasajeros, 4 LiDAR 16 haces + 4 cámaras fisheye + GNSS-RTK"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
Reportar logros y desafíos de un servicio real de shuttle autónomo de campus ("Snow Lion") operado durante dos meses, describiendo la arquitectura completa (percepción, localización, planificación, control) y las lecciones de operación.

## Hipótesis
Un stack modular con localización LiDAR + GNSS-RTK y planificación conservadora es suficiente para operar de forma estable un shuttle de baja velocidad en un campus semi-estructurado, aunque persisten fallos de localización y ruido de percepción.

## Metodología
- **Diseño:** reporte de sistema y de despliegue operacional real.
- **Datos / muestra:** campus de HKUST (Guangzhou), 8 de junio a 7 de agosto de 2023; tres turnos diarios de dos horas; estaciones fijas predefinidas (C1, C6, 1B, NE3). Vehículo de 4,35 × 1,63 × 2,28 m, 6 pasajeros, velocidad máxima de diseño 15 km/h.
- **Técnicas:** 4 LiDAR de 16 haces, 4 cámaras fisheye, IMU, GNSS-RTK; ruteo global A*, planificación de comportamiento y de movimiento (GPMP), control MPC acoplado lateral-longitudinal.
- **Métricas:** distancia recorrida, pasajeros, distancia por intervención manual, distancia por frenada brusca, velocidad promedio/máxima, aceleración/desaceleración.

## Resultados principales
- 1.146 km recorridos y 442 pasajeros transportados en dos meses (promedio 10,82 pasajeros/día); velocidad promedio 7,41 km/h, máxima 11,76 km/h.
- **Una intervención manual (takeover) cada 13,34 km** y **una frenada brusca (≤ -1 m/s²) cada 0,77 km**: la frenada abrupta es un evento mucho más frecuente que la desconexión total.
- **Inestabilidad de localización dependiente del entorno y del tiempo:** "Localization instability may be unavoidable, particularly in scenarios with sparse point cloud features for mapping or when map features evolve over time (e.g., tree growth and leaf expansion affecting the effectiveness of an offline map)." Grandes obstáculos (camiones) y cambios estacionales degradan el desempeño.
- **Percepción ruidosa en entorno poco regulado:** "Results from object detection and trajectory prediction are doomed to be full of noise as the environment is full of uncertainty and less traffic regulations. We found that constant velocity model and a lane-keeping speed planning scheme is enough for a stable navigation performance." La solución práctica fue simplificar el planificador, no sofisticar la predicción.
- **Interacción con otros usuarios como desafío central:** "Clear planning behavior for other road users and the understanding of their intentions are crucial factors for user-friendly autonomous driving... Ensuring clarity in these interactions is vital to prevent sudden braking and ensure safety."
- Obstáculos ambientales adicionales reportados: sombras de árboles que generan ruido perceptual, cruce peatonal fuera de norma, adelantamientos inesperados; dependencia de mapeo manual de "áreas de observación" para intersecciones complejas.

## Conclusiones
Es viable operar un shuttle autónomo de campus con un stack modular y planificación conservadora, pero la operación real depende de mapeo manual de zonas críticas, y la degradación del mapa offline por cambios del entorno (vegetación, obras) es un problema abierto que exige mantenimiento del mapa.

## Limitaciones
Preprint (arXiv), no revisado por pares en la versión consultada. No reporta encuestas cuantitativas de satisfacción ni incidentes formales; el takeover es una métrica indirecta. Dos meses, un vehículo, un campus. Clima subtropical (no cubre polvo industrial ni climas extremos).

## Relevancia / brecha para el estado del arte
Aporta las **cifras de intervención más citables para un caso de 6 pasajeros en recinto acotado** (13,34 km/takeover; 0,77 km/frenada brusca), directamente comparables con el caso de uso de robo-shuttle interno. Confirma que el mapa previo se degrada con el entorno y que la adaptación de ruta no es un evento único de comisionamiento sino un proceso continuo.

> Relaciones → `../../indice.json`. Ver [[paper-anund-2022-lecciones-sitios-demo-shuttle-autonomo]], [[reporte-ncdot-2024-cassi-unc-charlotte]].
