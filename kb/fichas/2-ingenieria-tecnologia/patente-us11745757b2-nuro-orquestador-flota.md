---
id: patente-us11745757b2-nuro-orquestador-flota
titulo: "Orchestrator for interconnected autonomous vehicle fleet ecosystem — US11745757B2 (Nuro)"
tipo: patente
tema: Orquestador remoto que monitorea el cumplimiento de un trabajo asignado a un vehículo autónomo y coordina los subsistemas (troubleshooting, operación remota, coordinación de flota) que deben intervenir
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [B60W60/001]
topicos: [autonomia-supervisada-flota, flota-y-telemetria, centro-integrado-operaciones]
anio: 2019  # QA: prioridad más antigua = provisional US 62/916,079 de 2019-10-16
titular: Nuro Inc (EE.UU.)
referencia: US11745757B2 (solicitud US17/065,195 presentada 2020-10-07; **prioridad 2019-10-16** por la provisional US 62/916,079 "Interconnected Command Ecosystem for Autonomous Vehicles"; concedida 2023-09-05; expiración ajustada 2041-10-23)
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
verificacion_qa: observado  # QA 2026-08-03: estado legal y claim 1 confirmados literalmente; corregida la fecha de prioridad (2019-10-16, no 2020-10-07)
estado_legal: vigente (Status "Active"; expiración ajustada 2041-10-23)
jurisdicciones: [US]
fecha_prioridad: 2019-10-16
trl_relevante: 7-8
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Problema técnico que resuelve
Un trabajo (entregar carga de A a B) requiere coordinar varios subsistemas del centro de operaciones. ¿Cómo se orquesta esa coordinación desde fuera del vehículo, sin que cada subsistema opere aislado?

## Reivindicaciones clave (qué protege)
Claim 1 (literal, verificado):
> "1. A computer-implemented method comprising: monitoring, by a fleet management system having at least one processor and being remote from an autonomous vehicle, completion of an assigned job by the autonomous vehicle in a fleet of autonomous vehicles; identifying, by the fleet management system, a plurality of tasks to be completed by a plurality of subsystems of the fleet management system to enable the completion of the assigned job by the autonomous vehicle; coordinating, by the fleet management system, the completion of the plurality of tasks by the plurality of subsystems, wherein the coordinating includes selecting at least two of the plurality of subsystems… ; and causing the at least two of the plurality of subsystems… to control the autonomous vehicle to complete the assigned job based on the coordinating."

## Solución técnica (cómo lo hace)
Una capa de orquestación **remota al vehículo** (fleet management system) descompone el trabajo en tareas por subsistema (troubleshooting, remote operations, fleet operations, fleet coordinator, interfaz) y las coordina hasta cerrar el trabajo.

## Alcance y limitaciones
- Familia **solo US**.
- El claim termina en "control the autonomous vehicle to complete the assigned job": exige que los subsistemas **controlen** el vehículo. Una capa que solo planifica, agenda y mide (sin comandar el vehículo, que es el caso de una caja negra sin API) no cae en el claim literal.
- No cubre analítica de logs ni caracterización de sitio.
- **Nota QA (2026-08-03):** verificado en Google Patents. Status "Active", familia solo US (dos solicitudes US), claim 1 literal —incluido el cierre "control the autonomous vehicle to complete the assigned job based on the coordinating"—. Corrección: la prioridad más antigua es la provisional US 62/916,079 del **16-10-2019**; la ficha anterior consignaba 2020-10-07 (fecha de la solicitud no provisional). Importa para fechar el arte previo.

## Relevancia FTO / novedad
Marca el techo del eje (c) — "capa de software local de operación/planificación": la orquestación de flota con control efectivo del vehículo ya está protegida (Nuro, EE.UU.). El espacio que queda para Kaufmann es el de una capa que **planifica y mide sin comandar**, sobre un vehículo cerrado. Es un espacio más angosto técnicamente, pero libre en patentes.

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
