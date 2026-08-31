---
id: review-kamtam-2024-latencia-teleoperacion-cav
titulo: "Network Latency in Teleoperation of Connected and Autonomous Vehicles: A Review of Trends, Challenges, and Mitigation Strategies (Kamtam, Lu, Bouali, Haas & Birrell, 2024)"
tipo: revision
tema: Requisitos de red y umbrales de latencia para teleoperación/supervisión remota de vehículos autónomos
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [teleoperacion-supervision-remota, conectividad-red-vehiculo-autonomo]
anio: 2024
autores: [Sidharth Bhanu Kamtam, Qian Lu, Faouzi Bouali, Olivier C. L. Haas, Stewart Birrell]
referencia: https://doi.org/10.3390/s24123957
motor: Europe PMC → PMC11207977 (full-text open access)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 5-7
metricas_clave: ["latencia <170 ms impacto menor; 170-300 ms adaptable; >700 ms casi imposible", "5G 11-13 ms vs 4G ~100 ms vs WiFi ~50 ms", "uplink requerido 8-50 Mbps; downlink 0.25-5 Mbps", "fiabilidad 99% uplink / 99.999% downlink", "~230 artículos revisados"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
  - kaufmann-telecomando
---

## Pregunta / objetivo de investigación
¿Cuál es el impacto de la latencia de red en la teleoperación de vehículos conectados y autónomos, qué tecnologías inalámbricas la habilitan y qué estrategias de mitigación existen?

## Hipótesis
La latencia de red es un factor limitante crítico para la teleoperación, y su variabilidad (jitter) — no solo su magnitud — determina el desempeño del operador remoto.

## Metodología
- **Diseño:** revisión sistemática de literatura de la última década (~230 artículos identificados, ~75% incluidos tras cribado).
- **Datos / muestra:** literatura sobre teleoperación de CAV, tecnologías inalámbricas (3G/4G/5G/WiFi), requisitos de QoS.
- **Técnicas:** síntesis comparativa de umbrales de latencia, requisitos de ancho de banda y estrategias de mitigación (control y percepción).
- **Métricas:** latencia (ms), ancho de banda (Mbps), fiabilidad (%), resolución/frame rate de video.

## Resultados principales
- **Umbrales de latencia:** "A constant latency of less than 170 milliseconds has a minor impact and is easily manageable whilst the operator can adapt to latency below 300 ms." Entre 300 y 500 ms la teleoperación es desafiante y exige bajar la velocidad; "Latencies above 700 ms make it nearly impossible for the teleoperator to interact with the vehicle in a timely manner."
- **La variabilidad manda:** "The major problem is with the variability (unpredictable fluctuations) of the delay rather than its magnitude, which degrades the teleoperation performance."
- **Comparación de tecnologías:** 5G 11–13 ms (1–10 Gbps); 4G/LTE ~100 ms (100 Mbps–1 Gbps); WiFi ~50 ms (11–1000 Mbps); 3G 121–217 ms.
- **Requisitos de la aplicación:** uplink de 8–50 Mbps (datos sensoriales), downlink de 0,25–5 Mbps (comandos de control), resolución mínima 640×480, 25–30 fps, fiabilidad 99% uplink y 99,999% downlink.
- **Impactos de la pérdida de conexión:** degradación en la toma de decisiones y el comportamiento del operador, sobre/sub-dirección del vehículo remoto, aumento de carga mental y de la probabilidad de accidente.
- **Mitigación:** métodos basados en pasividad, predicción (LSTM/RNN), MPC, autonomía adaptativa a bordo, pantallas predictivas, Mobile Edge Computing, SDN y Time-Sensitive Networking.

## Conclusiones
5G habilita teleoperación viable pero requiere optimización; la latencia variable es un desafío mayor que la latencia constante; los métodos predictivos combinados (control + percepción) son los más efectivos. Falta investigación específica para CAV frente a robótica tradicional, especialmente a distancias largas y en entornos reales.

## Limitaciones
Revisión: no aporta datos primarios. Se centra en teleoperación de conducción activa (remote driving), no en supervisión remota de nivel superior (monitoring/asistencia por eventos), que es el modo típico de los shuttles de baja velocidad. No cubre específicamente redes privadas WiFi en recintos industriales.

## Relevancia / brecha para el estado del arte
Convierte "la conectividad es un riesgo" en **requisitos verificables** para el diseño de un piloto en recinto propio: latencia objetivo <170 ms, jitter acotado, ~8–50 Mbps de subida por vehículo y fiabilidad de enlace de control. Es la referencia para justificar la caracterización de la cobertura WiFi/celular del recinto como actividad de I+D. Brecha: no existe literatura que caracterice el desempeño de una red WiFi de patio industrial para este uso.

> Relaciones → `../../indice.json`. Ver [[paper-li-2023-teleoperador-remoto-5g-nivel4]], [[review-majstorovic-2022-conceptos-teleoperacion-vehiculos]] (taxonomía de conceptos de teleoperación) y [[paper-musicant-2026-predictive-display-teledriving]] (evidencia experimental a 150 ms).
