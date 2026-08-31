---
id: whitepaper-5gaa-2021-tod-casos-de-uso-requisitos
titulo: "5GAA — Tele-Operated Driving (ToD): Use Cases and Technical Requirements (Technical Report, agosto 2021)"
tipo: whitepaper
tema: Casos de uso, tipos de control (directo/indirecto), requisitos funcionales y de seguridad para conducción teleoperada
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [teleoperacion-supervision-remota, requisitos-red-latencia-jitter, teleoperacion-fallback, conectividad-red-vehiculo-autonomo]
anio: 2021
autores: [5GAA Automotive Association]
referencia: https://5gaa.org/content/uploads/2021/08/ToD_D1.1-Use-Cases-and-Technical-Requirements.pdf
motor: WebSearch + WebFetch (PDF descargado y leído por páginas)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: ["Direct control: velocidad <15 km/h y rango de maniobra <100 m (User Story 1)", "Indirect control alta velocidad: hasta 80 km/h, rango operacional hasta 5.000 m (User Story 3)", "Slim uplink: imágenes periódicas + objetos en vez de video completo"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Qué establece

Reporte técnico de 5GAA (consorcio automotriz-telco) que define los **cuatro casos de uso** de ToD (ToD; ToD support; ToD para estacionamiento automatizado; ToD basada en infraestructura) y **dos tipos de control**:

- **Direct Control**: "the remote operator fully controls the vehicle... Direct control entails more stringent requirements on the 5G connectivity."
- **Indirect Control**: "the remote operator does not directly drive the vehicle but provides guidelines or a path for the vehicle to overcome the encountered challenge; the vehicle controls the execution of the path."

Cita textual (§5.2.1.3, User Story 3, cruce de frontera de red):
> "During the drive, the vehicle crosses a communication network border, while the remote operator is connected to the vehicle. ... One additional requirement to the communication networks in this example is that the ToD operation should continue without interruption due to the handover between network providers."

Cita textual (§5.2.1.4, User Story 4 — 'slim uplink'):
> "instead of always using full video, the uplink communication from the vehicle to the remote operator can be reduced to periodic 'still' images, compensated with additional vehicle perceived object information, known as 'Slim uplink'. The main goal is to improve the efficiency and scalability of the uplink data channel."

Cita textual (§7.1, Functional Requirements — Communication and Network):
> "Network resources shall be available for the time when the ToD service is needed, and the communication link shall be reliable and encrypted."
> "Service continuity shall be guaranteed during the operation of ToD service."
> "The vehicle shall receive notifications about expected QoS change (i.e. QoS prediction) and then appropriate adaptations should be applied (e.g. reduce speed, enable safe operation etc.)."

Cita textual (§5.3, lecciones aprendidas — fiabilidad):
> "ToD Type 'Direct Control' and ToD Type 'Indirect Control' ... demand high network reliability that may not be achievable with the current 4G/LTE mobile network standard."
> "Cross-border operations impose significant additional challenges for lag-free data transmission when handing over between MNOs."

Cita textual (§7.2, seguridad funcional):
> "In tele-operation, however, the overall system consists not only of the vehicle but also of the Vehicle Control Centre (VCC) in the backend and the communication network connecting the vehicle with the VCC. As the VCC and the communication network are outside the vehicle and the automotive domain ... new challenges arise from a safety point of view."
> "A safe system must be able to monitor all factors forming the ODD ... and stop (fail-safe state) the function or reduce the function capabilities (safe operational state) whenever the system is outside of its ODD."

## Panorama comercial que documenta

La Tabla 2 del reporte lista proveedores (pre-)comerciales de ToD, entre ellos **Phantom Auto** ("ToD deployment kit (HW and SW) for vehicles... ToD support for yard trucks with difficult manoeuvres"), **Designated Driver** ("Six video streams + driving actuations - both Verizon and AT&T's networks using four cellular radios"), **Ottopia**, **Roboauto** ("Onboard Sekonic camera, LTE mobile connection"), **Einride/VERA**, **SEAFAR** (buques no tripulados desde centro en tierra).

## Relevancia / brecha para el estado del arte

- **Problema resuelto (a nivel de arquitectura conceptual)**: hay arquitectura de referencia, taxonomía de control y catálogo de proveedores; la teleoperación en área confinada con un solo MNO y un solo OEM es el escenario "priorizado" del reporte.
- **Brecha declarada por el propio consorcio**: fiabilidad de red suficiente, continuidad de servicio en handover **entre operadores/redes**, seguridad funcional del sistema distribuido (vehículo + red + centro de control fuera del dominio del OEM), y ODD que incluya la conectividad como variable a monitorear.
- Directamente relevante para el caso minero: el "slim uplink" y el control indirecto son las palancas para bajar los requisitos de red cuando el enlace no puede garantizar video completo.

> Relaciones con otras fichas → `../../indice.json`.
