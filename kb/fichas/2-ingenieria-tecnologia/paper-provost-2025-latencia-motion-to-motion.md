---
id: paper-provost-2025-latencia-motion-to-motion
titulo: "Motion-to-Motion Latency Measurement Framework for Connected and Autonomous Vehicle Teleoperation (Provost, Hawlader, Testouri, Frank — arXiv 2511.22467, 2025)"
tipo: preprint
tema: Medición del lazo completo operador→actuador (motion-to-motion) en teleoperación, más allá del glass-to-glass
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [teleoperacion-supervision-remota, requisitos-red-latencia-jitter, conectividad-red-vehiculo-autonomo]
anio: 2025
autores: [François Provost, Faisal Hawlader, Mehdi Testouri, Raphaël Frank]
referencia: https://arxiv.org/abs/2511.22467
motor: WebSearch + WebFetch (PDF) — lectura por páginas
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 4-5
metricas_clave: ["M2M mediana >750 ms en los cuatro escenarios de campo", "Estático WiFi: 874,5 ms mediana (IQR 198,0 ms)", "Estático 5G: 930,6 ms mediana pero IQR 105,0 ms (−47 % de variabilidad)", "Dinámico 5G: 767,8 ms mediana, 1,4 % de muestras >1 s", "Umbrales citados: >300 ms desafiante; >400 ms difícil de mantener; recomendado <170 ms"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Pregunta / objetivo de investigación

El G2G (cámara→pantalla) solo captura la mitad perceptual del retardo. Los autores miden el **motion-to-motion (M2M)**: desde que el operador gira el volante remoto hasta que el volante del vehículo responde físicamente.

## Metodología

Sensores Hall en ambos volantes (remoto y vehículo), interrupciones por hardware con marcas de tiempo en dos Raspberry Pi 5 sincronizadas por Chrony. Precisión del marco: 10–15 ms. Cuatro escenarios: estático (WiFi vs 5G comercial POST Luxembourg) y dinámico (~10 km/h, dos modos de sincronización).

## Resultados principales

> "Prior studies consistently show that human performance degrades sharply as latency increases. For instance, [1] recommends keeping latency below 170 ms, while [2] reports that delays exceeding 300 ms can make teleoperated driving challenging. Beyond 400 ms [3], real-time teleoperation performance becomes difficult to maintain."
> "Across all cases, the observed median latency exceeds 750 ms."
> "Static 5G results in a slightly higher median latency of 930.6 ms but a substantially narrower IQR of 105.0 ms (a reduction of ∼47%)."
> "Considering both, the measured M2M delay and typical G2G latency values reported in prior work, the overall operator–vehicle responsiveness can approach around one second, which may challenge real-time teleoperation requirements."
> "M2M latency is dominated by the vehicle's steering actuator and its PID controller."

## Conclusiones

El retardo dominante del lazo de teleoperación **no es la red sino la actuación mecánica del vehículo**. Con G2G ~200 ms y M2M >750 ms, la respuesta percibida operador→vehículo→operador se acerca al segundo, muy por encima de los umbrales de desempeño humano citados (170–400 ms).

## Limitaciones

- Preprint reciente (nov. 2025), sin revisión por pares confirmada.
- Vehículo específico (drive-by-wire con controlador PID no optimizado); el piso de actuación depende del vehículo.
- Velocidades bajas (~10 km/h), estacionamiento cerrado.

## Relevancia / brecha para el estado del arte

Aporta un argumento decisivo para el diseño: **optimizar solo la red no resuelve el problema si la cadena de actuación del vehículo introduce cientos de ms**. En un camión telecomandado de fábrica, la latencia de actuación del OEM es un dato a medir, no a suponer. Y refuerza que 5G aporta sobre todo **predictibilidad** (menor IQR), no menor latencia absoluta.

> Relaciones con otras fichas → `../../indice.json`.
