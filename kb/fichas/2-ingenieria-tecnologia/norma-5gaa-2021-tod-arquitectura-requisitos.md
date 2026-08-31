---
id: norma-5gaa-2021-tod-arquitectura-requisitos
titulo: "5GAA — Tele-operated Driving: Use Cases, System Architecture and Business Considerations (White Paper v0.9, 17 dic 2021)"
tipo: whitepaper
tema: Requisitos de servicio, taxonomía y arquitectura de referencia para conducción teleoperada sobre redes móviles
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [teleoperacion-supervision-remota, latencia-teleoperacion, conectividad-vehiculo-autonomo, teleoperacion-fallback]
anio: 2021
autores: [5G Automotive Association (5GAA)]
referencia: https://5gaa.org/content/uploads/2021/12/5GAA_Tele_operated_Driving_White_Paper.pdf
motor: WebSearch + PDF full-text (lectura directa del documento)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "5-8 (especificación industrial con pilotos y despliegues por etapas)"
metricas_clave: ["latencia E2E de servicio ~120 ms para Direct Control ToD a 50 km/h", "RTT de red 50-60 ms suficiente para ese caso", "300 ms admisible para Indirect Control a 10 km/h", "uplink video hasta 32 Mb/s (4 cámaras x ~8 Mb/s), fiabilidad 99%", "downlink comandos ~400 kb/s cada 20 ms, fiabilidad 99,9% o superior", "red requerida 99,9% o superior de disponibilidad", "50 km/h es la velocidad máxima considerada para conducción remota en condiciones inciertas"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Contexto / qué es
> Documento **distinto** del reporte técnico D1.1 fichado en [[whitepaper-5gaa-2021-tod-casos-de-uso-requisitos]]: este es el white paper de síntesis de diciembre de 2021, que resume D1.1 (casos de uso), D2 (arquitectura) y D3 (negocio). Se complementan.

White paper de la asociación industrial 5GAA (fabricantes, proveedores y operadores móviles) que resume tres reportes técnicos propios (D1.1 casos de uso y requisitos, D2 arquitectura, D3 negocio). **No es una norma obligatoria**, pero es la referencia de facto sobre requisitos de red para teleoperación vehicular y está citada en documentos de trabajo de UNECE GRVA.

## Taxonomía que fija
Cuatro tipos según el nivel de involucramiento del operador remoto en el acto de conducir:
- **Non-ToD** — el operador no participa.
- **Dispatch ToD** — solo funciones estratégicas (ruta, itinerario).
- **Indirect Control ToD** — funciones tácticas (asistencia remota); la tarea dinámica de conducción sigue en el vehículo.
- **Direct Control ToD** — el operador remoto ejecuta toda o parte de la **tarea dinámica de conducción en tiempo real** (Real-Time DDT), incluido OEDR.

Hoja de ruta de despliegue en tres etapas: **Stage 1 — áreas confinadas** (menciona explícitamente "mining sites, seaports, OEM factories industrial areas"), Stage 2 — vías públicas dedicadas, Stage 3 — movilidad interregional (long haul).

## Requisitos técnicos declarados
- Latencia extremo a extremo de servicio: "the typical E2E service-level latency requirement for Direct Control ToD with a vehicle speed of 50 km/h is about 120 ms, including both uplink […] and downlink […] parts"; redes con RTT de 50–60 ms pueden sostener ese caso. Indirect Control a 10 km/h relaja el requisito a ~300 ms.
- Datos: uplink dominado por video (hasta 32 Mb/s con 4 cámaras, fiabilidad 99%); downlink de comandos ~400 kb/s con mensajes cada 20 ms y fiabilidad 99,9% o superior.
- "50 km/h is considered the maximum speed for remote steering under highly uncertain conditions."

## Pérdida de enlace y estado de riesgo mínimo
- "The wireless communication link may fail during the ToD operation. When such failure occurs, safety measures at the vehicle side should be able to detect it and take the necessary steps to ensure safety, e.g. bringing the vehicle to the minimal risk state."
- Pero acota: "when the ToD service is engaged, such events should happen very rarely to ensure an acceptable availability of the ToD service. For this reason, the communication network should meet very high reliability requirements, e.g. 99.9% or higher."
- El vehículo debe poder detectar el mal funcionamiento del sistema ToD y **anular** el subsistema para llevarlo a estado de riesgo mínimo (pérdida de conectividad, intrusión, datos de actuación erróneos).
- Seguridad funcional: recomienda tratar el dominio de comunicaciones como **canal abierto ("black channel")** y concentrarse en el monitoreo seguro de ese canal en ambos extremos; el requisito sobre la comunicación es de **disponibilidad del servicio** más que de seguridad funcional ISO 26262.
- QoS predictiva: la red debería anticipar cambios de QoS al vehículo y al operador (vía NEF de 5G) para ajustar el comportamiento de la aplicación, "e.g. changing the ToD type or the vehicle speed".

## Limitaciones
- Documento de asociación industrial, versión 0.9 (2021); los requisitos son "típicos", no verificados por ensayo independiente y referidos a vehículos de carretera de pasajeros, no a camiones pesados en faena minera.
- No cubre requisitos de operación 24/7 ni continuidad multi-operador móvil con SLA en terreno remoto.

## Relevancia / brecha para el estado del arte
Fija la cifra objetivo (≈120 ms E2E para control directo a 50 km/h; 99,9% de fiabilidad) contra la que se puede contrastar cualquier propuesta de conectividad, y deja explícito que la **degradación graciosa (cambiar tipo de ToD o velocidad ante caída de QoS)** es parte del diseño esperado, no solo el freno de emergencia. La medición de campo de [[paper-testouri-2025-5g-teleoperacion-evaluacion-experimental]] (202 ms glass-to-glass sobre 5G comercial) muestra la distancia entre requisito y realidad medida. Complementa a [[review-kamtam-2024-latencia-red-teleoperacion-cav]].

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
