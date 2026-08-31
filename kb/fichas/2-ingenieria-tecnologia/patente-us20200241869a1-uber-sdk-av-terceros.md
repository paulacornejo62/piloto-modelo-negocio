---
id: patente-us20200241869a1-uber-sdk-av-terceros
titulo: "Cloud Software Development Kit for Third-Party Autonomous Vehicles — US20200241869A1 (Uber Technologies)"
tipo: patente
tema: Paquete de software (SDK) instalado en el sistema del dueño de los vehículos autónomos que abre un canal con la plataforma de la entidad de servicio, para operar AV de terceros sin acceso a su stack de conducción
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [H04W4/50]
topicos: [flota-y-telemetria, autonomia-supervisada-flota, recinto-privado-odd]
anio: 2019
titular: Uber Technologies Inc (EE.UU.)
referencia: US20200241869A1 (solicitud US16/526,079; prioridad provisional US62/796,974 de 2019-01-25)
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: abandonada (Status "Abandoned" en Google Patents; solo familia US)
jurisdicciones: [US]
fecha_prioridad: 2019-01-25
trl_relevante: 6-7
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Problema técnico que resuelve
Un operador de servicio (quien vende el viaje/la operación) no fabrica ni controla el vehículo autónomo: el stack de conducción es del tercero. ¿Cómo integra su backend (asignación, monitoreo, estado del viaje) con vehículos autónomos ajenos, sin acceder al software de conducción?

## Reivindicaciones clave (qué protege)
Claim 1 (literal, verificado):
> "1. A computer-implemented method for communication between a service entity and a third-party entity, comprising: accessing, by a first computing system comprising one or more computing devices, a software package stored within the first computing system, wherein the first computing system is associated with a third-party entity, wherein the third-party entity is associated with one or more autonomous vehicles, and wherein the software package is associated with a service entity that coordinates a vehicle service for the one or more autonomous vehicles; establishing, by the first computing system via the software package, a communication connection with a second computing system that is associated with the service entity, wherein the second computing system comprises one or more backend services to facilitate the vehicle service; and communicating, between the first computing system and the second computing system, data indicative of a communication associated with the one or more autonomous vehicles via the communication connection."

Reivindicación de sistema (resumen del documento): el lado de la entidad de servicio incluye una *vehicle integration platform* con "a plurality of application programming interfaces", cada una entregando servicios de backend del servicio de vehículos.

## Solución técnica (cómo lo hace)
Arquitectura de dos sistemas: el SDK vive en el sistema del dueño de la flota; el "vehicle integration platform" del operador expone APIs de backend; los mensajes viajan identificados por `vehicle identifier` y pueden batchearse por flota. La capa de operación queda **fuera** del vehículo y **fuera** del stack del vendor.

## Alcance y limitaciones
- Es una **solicitud abandonada**, sin concesión, y solo con familia estadounidense (no hay EP/WO/CL).
- El claim presupone que el tercero **instala** un paquete del operador de servicio: es un modelo cooperativo (con integración acordada), no una capa construida sobre datos que el vendor entrega "a ciegas".
- No cubre analítica, KPIs, ni caracterización del recinto: solo el canal de comunicación.

## Relevancia FTO / novedad
Confirma que la idea genérica "operador de servicio integra AV de un tercero mediante una capa de software propia" ya estaba **publicada en 2020** (aunque abandonada, sigue siendo **arte previo** que destruye novedad de reclamos genéricos de integración). Para Kaufmann: (i) no hay patente viva en Chile ni en EP/WO que bloquee construir esa capa; (ii) la novedad reclamable no puede ser "una capa de integración con el vendor" en abstracto — tiene que estar en el mecanismo específico (p. ej. reconstruir estado operacional a partir de logs sin API, o el protocolo de caracterización del recinto).

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
