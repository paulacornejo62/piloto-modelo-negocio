---
id: patente-us11625051b2-uber-odd-derivado-de-viajes
titulo: "Proactive generation of tuning data for autonomous vehicle dispatch — US11625051B2 (Uber Technologies)"
tipo: patente
tema: Derivar los parámetros de ODD de un tipo de vehículo autónomo a partir de datos de movimiento y registros de viajes, y generar viajes nuevos para completar el conocimiento del ODD
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [G06Q50/40]
topicos: [recinto-privado-odd, flota-y-telemetria, disengagement-kpi-piloto, autonomia-supervisada-flota]
anio: 2020
titular: Uber Technologies Inc (EE.UU.)
referencia: US11625051B2 (solicitud US16/750,773; presentada 2020-01-23; concedida 2023-04-11)
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: vigente (Status "Active")
jurisdicciones: [US]
fecha_prioridad: 2020-01-23
trl_relevante: 7
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Problema técnico que resuelve
El operador de la plataforma **no conoce** el ODD real de los vehículos autónomos que despacha (lo declara el fabricante, y no cubre el detalle geográfico). ¿Cómo lo infiere desde la operación y cómo genera evidencia faltante de forma deliberada?

## Reivindicaciones clave (qué protege)
Claim 1 (literal, verificado, extracto):
> "1. A method for dispatching trips to a plurality of autonomous vehicles, the method comprising: receiving a passenger rating for a particular trip… accessing trip records of other trips executed by a set of autonomous vehicles of the first vehicle type…; determining a commonality among the set of autonomous vehicles of the first vehicle type by determining that a threshold number of at least one of negative or positive demonstrations of a capability associated with a first operational design domain (ODD) parameter has been performed by the first vehicle type…; deriving ODD parameters for the set of autonomous vehicles of the first vehicle type based on vehicle movement data and the determined commonality…; determining that the first ODD parameter meets a criterion; generating a first new trip based on the first ODD parameter; selecting an autonomous vehicle from the set of autonomous vehicles to [execute it]…"

Resumen (literal):
> "Operational design domain (ODD) parameters for an autonomous vehicle of a first vehicle type are derived based on vehicle movement data."

## Solución técnica (cómo lo hace)
Ciclo de aprendizaje operacional desde afuera del vehículo: registros de viaje + calificación del pasajero → demostraciones positivas/negativas de una capacidad → parámetros de ODD del **tipo de vehículo** → generación proactiva de viajes que exploran el parámetro poco observado.

## Alcance y limitaciones
- Familia **solo US**.
- El claim está anclado a **passenger rating** y a un contexto de servicio de transporte on-demand; una caracterización que no use calificación de pasajero cae fuera del claim literal.
- La "generación proactiva de viajes" es, esencialmente, **diseño de experimentos operacionales**: es el precedente más directo del protocolo experimental de Kaufmann, aunque orientado a explorar el ODD del *vehículo*, no la aptitud del *recinto*.

## Relevancia FTO / novedad
Prueba que "inferir capacidad/ODD desde datos de operación y provocar viajes para cerrar brechas" es arte previo (2020, EE.UU.). La novedad reclamable de Kaufmann no puede ser el concepto; debe estar en:
- inferir desde **logs pobres y no diseñados para eso** (velocidad, batería, pasajeros, origen/destino), sin telemetría de percepción ni disengagements etiquetados;
- caracterizar un **recinto** (superficie, polvo, neblina, tráfico mixto) y no un tipo de vehículo;
- convertir esa caracterización en un **criterio de habilitación** replicable a otros centros de distribución.

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
