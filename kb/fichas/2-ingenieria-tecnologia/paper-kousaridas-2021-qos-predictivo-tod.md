---
id: paper-kousaridas-2021-qos-predictivo-tod
titulo: "QoS Prediction for 5G Connected and Automated Driving (Kousaridas, Manjunath, Perdomo, Zhou, Zielinski, Schmitz, Pfadler — IEEE Communications Magazine, 2021)"
tipo: paper
tema: Predicción anticipada de calidad de servicio (predictive QoS) como habilitador de la teleoperación segura ante degradación del enlace
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [teleoperacion-supervision-remota, qos-predictivo-slicing, requisitos-red-latencia-jitter, teleoperacion-fallback]
anio: 2021
autores: [Apostolos Kousaridas, Ramya Panthangi Manjunath, José Perdomo, Chan Zhou, Ernst Zielinski, Steffen Schmitz, Andreas Pfadler]
referencia: https://arxiv.org/abs/2107.05000
motor: WebSearch + WebFetch (PDF arXiv) — lectura por páginas
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 3-4
metricas_clave: ["Full video upstream (360°, 8 cámaras, 30 fps): 32 Mbps UL y 40 ms", "Limited video (360°, 5 cámaras): 20 Mbps y 40 ms", "Slim uplink (objetos + fotogramas sueltos): 1 Mbps y 40 ms", "DL control indirecto: 500 Kbps y 80 ms; control directo: 500 Kbps y 40 ms", "Horizonte de predicción necesario: hasta ~6,6 s a 95 km/h para safe stop con desaceleración ≤4 m/s²"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Pregunta / objetivo de investigación

¿Puede la red 5G **anticipar** al vehículo un cambio de QoS con suficiente antelación para que la aplicación de teleoperación se adapte (bajar resolución, reducir velocidad, detenerse) antes de que el enlace se degrade?

## Metodología

- Arquitectura estándar 3GPP Rel-16 (NWDAF + NEF, "QoS sustainability analytics") para notificación anticipada al servidor de aplicación V2X.
- Simulación de sistema con ns-3.33 + SUMO (escenario urbano, 3 macro sitios, ISD 500 m, 2160 MHz, BW 20 MHz FDD), ToD con 20 Mbps de UL y hasta 160 vehículos de tráfico de fondo.
- Predicción del throughput UL con Random Forest; horizonte hasta 7 s; estimación de features futuras con ARIMA.

## Resultados principales

Requisitos por configuración de percepción (§III.A, citando 5GCroCo D2.1):
> "Full video upstream (360°, 8 cameras and high frame rates of up to 30 fps): 32 Mbps data rate and 40 ms latency"
> "Slim Uplink (object data and single frames): 1 Mbps data rate and 40 ms latency"
> "Indirect control: 500 Kbps data rate and 80 ms latency" · "Direct control: 500 Kbps data rate and 40 ms latency. It has stricter latency requirements, than indirect control because the CC directly controls the vehicle actuators."

Horizonte de predicción para una detención segura:
> "Performing a safe stop maneuver in case of communication loss needs to be possible at all time. Emergency stop maneuvers are not desired as the user experience suffers, e.g., deceleration of 10 m/s^2. ... Desired decelerations are lower than 4 m/s^2."
> La Fig. 2 fija el horizonte mínimo por velocidad: 0,4 s a 5 km/h; 1,4 s a 20 km/h; 2,4 s a 35 km/h; 3,5 s a 50 km/h; 4,5 s a 65 km/h; 6,6 s a 95 km/h.

Desempeño de la predicción:
> "for the first three seconds of the prediction horizon the prediction accuracy is high. After the fourth second there is an increase of the prediction error, due to less accurate estimation of future values of the input features."
> "Especially, after the fourth second there is an increase of the QoS prediction error, even with perfect input features. This level of accuracy may not be useful for some applications."

## Conclusiones

La predicción de QoS en tiempo real es **factible** con datos de red y aplicación combinados (MAPE 0,005 en entrenamiento), pero su exactitud se degrada más allá de ~3–4 s de horizonte, y colapsa en escenarios no vistos en entrenamiento.

## Limitaciones

- Simulación, no red real ni entorno minero.
- Escenario urbano LTE-like (2160 MHz, 20 MHz BW).
- Los autores mismos señalan que la predicción en escenarios desconocidos requiere técnicas adicionales (aprendizaje en línea, federado).

## Relevancia / brecha para el estado del arte

Da el marco cuantitativo para el requisito que plantea el cliente ("si cae el enlace, safe-stop"): **el safe-stop no es gratis, exige anticipación**. A 35 km/h se necesitan ~2,4 s de aviso previo para detenerse sin frenada de emergencia; la predicción de QoS publicada es confiable solo hasta ~3–4 s y falla en escenarios nuevos. Ahí queda una brecha genuina: predicción de QoS confiable en un entorno minero (polvo, terreno cambiante, bancos y rampas que ocluyen) no está resuelta en la literatura consultada.

> Relaciones con otras fichas → `../../indice.json`.
