---
id: paper-neumeier-2019-feasibility-tod-redes-moviles
titulo: "Measuring the Feasibility of Teleoperated Driving in Mobile Networks (Neumeier, Walelgne, Bajpai, Ott, Facchi — TMA 2019)"
tipo: paper
tema: Medición en campo (5.200 km de conducción) de latencia, jitter y throughput de redes móviles comerciales frente a los requisitos de conducción teleoperada
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [teleoperacion-supervision-remota, requisitos-red-latencia-jitter, conectividad-red-vehiculo-autonomo, bonding-multiconectividad]
anio: 2019
autores: [Stefan Neumeier, Ermias Andargie Walelgne, Vaibhav Bajpai, Jörg Ott, Christian Facchi]
referencia: "2019 Network Traffic Measurement and Analysis Conference (TMA), pp. 113–120 — PDF público: https://vaibhavbajpai.com/documents/papers/proceedings/teleoperated-driving-tma-2019.pdf"
motor: WebSearch + WebFetch (PDF) — lectura por páginas
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 4-5
metricas_clave: ["Dataset: ~5.200 km / ~78 h de conducción en Alemania (2017)", "Latencia mediana ~55 ms RTT; 96 % bajo 250 ms; ~1 % > 1 s", "Jitter mediano ~10 ms; ~5 % del tiempo no apto para ToD", "Uplink mediano ~12 Mbit/s; 13 % del tiempo insuficiente (<3 Mbit/s)", "Handover con cambio de tecnología radio: uplink cae a ~3 Mbit/s", "Umbral tolerable de latencia de red derivado en simulador: 250 ms; jitter <150 ms"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Pregunta / objetivo de investigación

¿Es factible la conducción teleoperada sobre redes móviles comerciales contemporáneas? Se mide latencia, jitter y throughput reales conduciendo y se contrastan con requisitos derivados.

## Metodología

- **Diseño:** campaña de medición en carretera real (rural, suburbana, urbana) en Alemania, mayo–diciembre 2017, con smartphone Android y gateway LTE SierraWireless RV50X (dos antenas) sobre Vodafone DE.
- **Datos:** ~5.200 km / ~4.660 min; herramientas `ping` (ICMP), `netradar` (UDP/TCP) e `iperf3`; servidores destino en Múnich y Fráncfort (~300 km entre sí).
- **Requisitos de referencia:** derivados por los autores más un estudio con 5 usuarios en simulador 3D (OpenROUTS3D).

## Resultados principales

Requisitos derivados:
> "It turned out that values above 300 ms make controlled driving nearly impossible. Subtracting the latency of sensors and actuators (roughly 50 ms), the maximum tolerable network latency is 250 ms."
> "We also identified that, if the jitter stays below 150 ms, it is possible to safely control a car."
> Uplink: "for transmitting a view of 150° at least 3 MBit/s of uplink are required"; comandos de dirección cada 10 ms ≈ 0,25 MBit/s de downlink.

Mediciones:
> "The median latency is ∼55.14 ms in RTT... About 96% of the total RTT values are below the critical 250 ms. Unfortunately, there are about 4% of higher RTT values, partly greater than one second (1%). This makes Teleoperated Driving infeasible."
> "The median jitter is at acceptable ∼10 ms (all technologies), but in about 5%, jitter is not suitable for Teleoperated Driving."
> "The median uplink speed is ∼12 MBit/s. In about 87% of the measurements the uplink speed is above 3 MBit/s and thus sufficient for Teleoperated Driving... there is a high percentage of about 13%, where the uplink speed is insufficient."
> Handover: "In general it can be said, that Teleoperated Driving is feasible when switching cells but keeping radio technology and infeasible when switching radio technology." (al cambiar de tecnología el uplink cae a ~3 MBit/s y el downlink a ~3 MBit/s).
> Distancia al centro de teleoperación (300 km entre servidores): "a higher distance between vehicle and teleoperation station does not significantly lead to higher latency, but its variation drastically increases."

Mitigaciones que discute el propio paper:
> "it is also possible to use multiple sim-cards [17] of different providers. This enables the option to always use the best network available and transmit important information using multiple paths."
> Propone además *whitelisting*: habilitar ToD solo en áreas medidas con desempeño suficiente.

## Conclusiones

La teleoperación sobre red móvil pública **es posible la mayor parte del tiempo pero no de forma garantizada**: la varianza (colas de latencia, caídas de uplink, handover entre tecnologías) es el problema, no la mediana. Los autores concluyen que "the high variance of network parameters makes it difficult to use the system at all times".

## Limitaciones

- Datos de 2017, red LTE (pre-5G) y de un solo operador.
- Requisitos de latencia derivados en simulador con 5 usuarios (muestra pequeña).
- Rutas específicas; no exhaustivo para casos reales.

## Relevancia / brecha para el estado del arte

Aporta el dato más citable para la pregunta "¿la distancia al centro de operación agrega latencia?": a 300 km **la mediana casi no cambia, pero la variabilidad sí crece mucho**. Es decir: para operación a 1.200 km el riesgo dominante es la **estabilidad/jitter y la cola de la distribución**, no el retardo medio. También documenta que el enemigo operacional es el handover con cambio de tecnología y la caída de uplink — precisamente el escenario de una faena con cobertura heterogénea (Wi-Fi + LTE privada + macro celular).

> Relaciones con otras fichas → `../../indice.json`.
