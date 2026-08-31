---
id: paper-lucas-estan-2023-tod-sobre-5g-tdd
titulo: "Support of Teleoperated Driving with 5G Networks (Lucas-Estañ, Coll-Perales, Khan, Avedisov, Altintas, Gozalvez, Sepulcre — IEEE VTC2023-Fall)"
tipo: paper
tema: Capacidad real de redes 5G centralizadas para sostener los requisitos de ToD definidos por 5GAA (TDD vs FDD, ancho de banda, escalabilidad)
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [teleoperacion-supervision-remota, requisitos-red-latencia-jitter, conectividad-red-vehiculo-autonomo, qos-predictivo-slicing]
anio: 2023
autores: [M.C. Lucas-Estañ, B. Coll-Perales, M.I. Khan, S.S. Avedisov, O. Altintas, J. Gozalvez, M. Sepulcre]
referencia: "doi:10.1109/VTC2023-Fall60731.2023.10333656 — postprint público: https://uwicore.umh.es/files/paper/2023_internacional/VTC2023Fall-ToD_UMH-Toyota_vfinal.pdf"
motor: WebSearch + WebFetch (PDF postprint) — lectura por páginas
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 3-4
metricas_clave: ["Requisito 5GAA: UL 32 Mbps / 100 ms / 99 %; DL 400 Kbps / 20 ms / 99,999 %; 10 veh/km²", "TDD comunes requieren >60 MHz para 1 vehículo ToD por celda", "Latencia de Internet al centro de control: 50,1 ms en percentil 99,999", "Con 32 Mbps y BW=30 MHz, el requisito falla más allá de 551 m del gNB"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Pregunta / objetivo de investigación

¿Puede una red 5G con despliegue centralizado sostener los requisitos de servicio de ToD que definió 5GAA, y bajo qué configuraciones (estructura de trama TDD, ancho de banda, densidad de vehículos)?

## Metodología

- **Diseño:** modelado analítico de latencia 5G (radio + transporte + core + Internet hasta el centro de control) validado sobre modelos previos publicados por el grupo; escenario de celda única 5G NR (SCS 30 kHz, 2 capas MIMO, radio de celda 866 m), BW 30–100 MHz.
- **Configuraciones:** FDD y tres estructuras TDD — DDDSU (TDD1), DDDDDDDSUU (TDD2) y DUDU (TDD3, balanceada).
- **Carga:** requisitos 5GAA (4 cámaras × 8 Mbps = 32 Mbps UL) y alternativa reducida de 4,5 Mbps observada en ensayos europeos (5GCroCo, 5GMobix).

## Resultados principales

Requisitos que asume (Tabla I, tomados de 5GAA):
> "5GAA considers that ToD vehicles should mount 4 cameras, and each camera generates 8 Mbps. This results in a total UL video bitrate per vehicle of 32 Mbps. 5GAA establishes a 100 ms service latency requirement and a 99% reliability requirement for UL transmissions."
> "5GAA imposes even more stringent requirements for the DL transmission of 1KB-command messages... these commands should be sent every 20 ms (400 Kbps) with a 99.999% reliability requirement."

Hallazgos:
> "commonly utilized 5G TDD frame structures require more than 60 MHz to support the ToD service specified by the 5GAA even when there is a single ToD vehicle per cell. This is due to the unbalanced distribution of slots between UL and DL."
> "the ToD reliability requirement cannot be met for distances greater than 551 m when BW=30 MHz. If BW increases to 50 MHz, it is possible to guarantee the reliability requirement up to a distance of 787 m."
> "the 20 ms latency requirement cannot be met due to the latency introduced by the Internet connection to the ToD control center (equal to 50.1 ms for the 99.999 percentile)."
> "Supporting the very stringent requirements established by the 5GAA to transmit ToD commands from the remote center to the vehicles requires transitioning from centralized to Multi-Access Edge Computing (MEC)-based network deployments due to the latency introduced by the Internet connection to the ToD control center."

## Conclusiones

Con las configuraciones 5G comerciales típicas (TDD asimétrica, favorable al downlink), la teleoperación con video completo **no escala**: hay que subir ancho de banda a >60 MHz, cambiar a trama balanceada/FDD, o **bajar el bitrate de video**. Y el enlace hacia el centro de control por Internet, no la radio, es lo que rompe el requisito de latencia del downlink de comandos.

## Limitaciones

- Simulación/modelado analítico, no medición de campo.
- Escenario de autopista con celda única; no modela minería, terreno abierto ni redes privadas dedicadas.
- No incluye retardos de procesamiento ni tiempo de reacción humana ("we do not consider processing delays or human reaction times").

## Relevancia / brecha para el estado del arte

Es la evidencia más directa de que **el cuello de botella no es solo la radio sino el trayecto hasta el centro de control**: mientras la latencia radio ronda 2–8 ms, el tramo transporte+core+Internet aporta decenas de ms y domina el percentil alto. Para un centro de operación a cientos o miles de km, esto convierte el diseño del backhaul dedicado (fibra propia, MEC en faena, rutas redundantes) en el problema central, no un detalle de implementación. Refuerza además la palanca del **uplink reducido** ([[whitepaper-5gaa-2021-tod-casos-de-uso-requisitos]]).

> Relaciones con otras fichas → `../../indice.json`.
