---
id: estandar-3gpp-ts22186-remote-driving
titulo: "3GPP TS 22.186 — Service requirements for enhanced V2X scenarios: §5.5 Requirements to support Remote Driving (Rel-17, V17.0.0, 2022-03)"
tipo: estandar
tema: KPI normativos de red para conducción remota (remote driving) en sistemas 3GPP
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [teleoperacion-supervision-remota, requisitos-red-latencia-jitter, conectividad-red-vehiculo-autonomo]
anio: 2022
autores: [3GPP TSG SA WG1]
referencia: 3GPP TS 22.186 V17.0.0 (2022-03), Tabla 5.5-1 — copia pública en https://people.computing.clemson.edu/~jmarty/projects/lowLatencyNetworking/finalReport/3GPP-Rel17-RelevantSidelink-SpecsAndStandards/22186-h00.doc
motor: WebSearch + descarga directa del .doc y extracción de texto (textutil)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: ["Max end-to-end latency: 5 ms", "Reliability: 99.999 %", "Data rate UL: 25 Mbps", "Data rate DL: 1 Mbps", "Velocidad soportada: hasta 250 km/h"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Qué establece

Especificación de requisitos de servicio de 3GPP para escenarios V2X mejorados. La sección 5.5 define el grupo de casos de uso **Remote Driving** y su tabla de desempeño.

Cita textual (§4.1):
> "Remote Driving enables a remote driver or a V2X application to operate a remote vehicle for those passengers who cannot drive themselves or a remote vehicle located in dangerous environments. For a case where variation is limited and routes are predictable, such as public transportation, driving based on cloud computing can be used."

Cita textual (§5.5, [R.5.5-001]):
> "The 3GPP system shall support message exchange between a UE supporting V2X application and V2X application server for an absolute speed of up to 250 km/h."

Cita textual (Tabla 5.5-1, requisito [R.5.5-002], escenario "Information exchange between a UE supporting V2X application and a V2X Application Server"):
> Max end-to-end latency (ms): **5** · Reliability (%): **99.999** · Data rate (Mbps): **UL: 25 / DL: 1**

## Requisitos relacionados relevantes

§5.6 (vehicle quality of service support) exige que la red pueda **anticipar** cambios de QoS:
> "The 3GPP network shall notify a V2X application that the current quality of service of a UE's ongoing communication might be unfulfilled (or re-fulfilled) in the future."
> "The 3GPP system shall be able to support continuity of reporting estimated quality of service for a UE even when the PLMN serving the UE changes."

## Relevancia / brecha para el estado del arte

- Es el **piso normativo citable** para la conducción remota: 5 ms extremo a extremo y 99,999 % de fiabilidad, con 25 Mbps de uplink. Nótese que este es un requisito *de sistema 3GPP*, no un valor alcanzado en campo: la literatura experimental (ver [[paper-neumeier-2019-feasibility-tod-redes-moviles]], [[paper-testouri-2025-5g-tod-evaluacion-experimental]]) mide latencias de decenas a centenas de milisegundos en redes reales.
- El requisito de 5 ms es **físicamente incompatible con un centro de control a ~1.200 km** por propagación de fibra sola (~5 µs/km ida → ≈6 ms ida, ≈12 ms ida y vuelta antes de cualquier equipo). Esto delimita qué tipo de teleoperación (control directo vs. indirecto/supervisorio) puede alojarse a larga distancia.
- 3GPP no distingue control directo de indirecto; esa distinción sí la hace 5GAA ([[whitepaper-5gaa-2021-tod-casos-de-uso-requisitos]]), con requisitos operacionales menos extremos (100 ms UL / 20 ms DL).

> Relaciones con otras fichas → `../../indice.json`.
