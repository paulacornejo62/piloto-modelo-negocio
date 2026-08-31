---
id: paper-emontsbotz-2024-5g-privado-mina-subterranea
titulo: "Private 5G-networks in underground mines: Promising results from field trials testing radio and radiating cable setups (Emontsbotz & Lottermoser 2024)"
tipo: paper
tema: Desempeño medido de una red 5G privada en una mina subterránea en operación (proyecto 5G.NAMICO)
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [conectividad-vehiculo-autonomo, mineria-teleoperacion-equipos, redes-5g-privadas, latencia-teleoperacion]
anio: 2024
autores: [J. J. Emontsbotz, B. G. Lottermoser]
referencia: https://papers.acg.uwa.edu.au/d/2435_N-01/N-01.pdf (doi:10.36487/ACG_repo/2435_N-01, 9th Int. Conf. and Exhibition on Mass Mining, Kiruna, 17-19 sep 2024)
motor: WebSearch + PDF full-text (Australian Centre for Geomechanics)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "6-7 (red privada 5G stand-alone en mina en operación)"
metricas_clave: ["RTT TWAMP 15,09-16,46 ms en 935 m de galería (σ 0,30 ms)", "descarga UDP máx 541,5 Mbit/s y 341 Mbit/s a 935 m", "subida UDP máx 148,8 Mbit/s, mínimo 50,4 Mbit/s", "alcance de radio direccional >935 m (simulación preveía ~700 m)", "banda n78 3,7-3,8 GHz, TDD 3:8:3 (39% de banda para uplink)", "mina de sal Sondershausen, nivel -700 m"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Pregunta / objetivo de investigación
Determinar el desempeño real utilizable (potencia de señal, throughput y RTT) de una red 5G privada en una mina subterránea en operación, comparando radios direccionales y cables radiantes en distintas configuraciones MIMO.

## Hipótesis
El 5G privado puede entregar cobertura amplia, alto ancho de banda y baja latencia en condiciones subterráneas, habilitando aplicaciones intensivas en red como el monitoreo en tiempo real y la teleoperación de maquinaria.

## Metodología
- **Diseño:** ensayo de campo en tres fases en la mina de sal Sondershausen (Turingia, Alemania), nivel -700 m; galerías de 5 m de alto por 8 m de ancho.
- **Técnicas:** red privada Ericsson EP5G stand-alone (core redundante, radios Ericsson 4408 4x4 MIMO, cables radiantes Euracay RMC 114-G); mediciones pasivas (RSRP) y activas (iPerf3 para throughput UDP/TCP, ping y TWAMP para RTT), en secciones cada 25 m con matriz de 9 puntos por sección.
- **Fases:** (1) alcance de radio direccional en galería A; (2) comparación de configuraciones de cable radiante 1x1, 2x2 y 4x4; (3) radio direccional vs cable radiante 2x2.

## Resultados principales
- A 935 m de la radio: descarga 353 Mbit/s promedio, subida 73 Mbit/s, **RTT bajo 16,5 ms**; el alcance superó la predicción de simulación (~700 m).
- RTT muy estable a lo largo de la galería: 15,09–16,46 ms con desviación estándar de 0,30 ms.
- La configuración de **cable radiante 2x2 resultó la mejor relación desempeño/costo**; la pérdida de línea de vista (depresión topográfica de la galería) degrada la radio direccional, mientras el cable radiante mantiene desempeño.
- El uplink es el recurso escaso: configuración TDD reservó 39% del ancho de banda para subida; el uplink cae de 148,8 Mbit/s a 50,4 Mbit/s al final de la galería.
- Los autores concluyen que 5G subterráneo permite "reliable and uninterruptible teleoperation of underground machinery" y que el handover explícito entre celdas favorece la fiabilidad en aplicaciones críticas en latencia.

## Conclusiones
Una red 5G privada bien diseñada entrega en mina subterránea latencias de red de ~15 ms y cientos de Mbit/s a casi 1 km de la radio; la topografía y la elección de antena (radio vs cable radiante) determinan la homogeneidad de la cobertura.

## Limitaciones
- Mediciones de **red**, no de aplicación: no miden latencia glass-to-glass de video ni teleoperación real de equipos.
- Una sola mina (sal, room-and-pillar, geometría ortogonal); no extrapolable directamente a rajo abierto o a faena con equipos móviles múltiples compartiendo la celda.
- No evalúa disponibilidad sostenida en el tiempo (24/7) ni escenarios de falla/handover bajo carga.

## Relevancia / brecha para el estado del arte
Aporta el dato duro de que la **capa de red no es el cuello de botella** cuando se despliega infraestructura privada dedicada (RTT ~15 ms, cientos de Mbit/s), y que el problema se traslada al diseño de cobertura, al uplink y a la continuidad. Contrasta con [[paper-testouri-2025-5g-teleoperacion-evaluacion-experimental]], donde sobre 5G público el cuello de botella es la cadena de video (202 ms G2G). Complementa a [[norma-5gaa-2021-tod-arquitectura-requisitos]].

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
