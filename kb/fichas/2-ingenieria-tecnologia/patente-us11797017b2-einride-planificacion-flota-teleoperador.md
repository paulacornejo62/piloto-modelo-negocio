---
id: patente-us11797017b2-einride-planificacion-flota-teleoperador
titulo: "Method for controlling a fleet of autonomous/remotely operated vehicles — US11797017B2 (Einride AB)"
tipo: patente
tema: Planificación de rutas que evita solapes temporales de los tramos que requieren teleoperador, para que un operador atienda varios vehículos en secuencia
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [G05D1/0287, G08G1/00]
topicos: [teleoperacion-supervision-remota, autonomia-supervisada-flota, ratio-operador-maquina]
anio: 2020
titular: Einride AB (Suecia)
referencia: US11797017B2 (familia: SE2050260A1, EP4118508B1, WO2021183019A1)
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: vigente
jurisdicciones: [US, EP, SE, WO]
fecha_prioridad: 2020-03-09
trl_relevante: 7-8
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Problema técnico que resuelve
El costo de la teleoperación es el operador. Si varios vehículos piden asistencia remota al mismo tiempo, o sobra operador o falta. ¿Cómo dimensionar y **planificar** para que un operador cubra varios vehículos?

## Reivindicaciones clave (qué protege)
Claim 1 (síntesis verificada): asignar rutas predeterminadas con tramos que requieren asistencia de teleoperador, **determinar los solapes temporales** de esos tramos e **insertar retardos o aceleraciones en los tramos autónomos previos** de modo que los tramos teleoperados dejen de solaparse, permitiendo que un operador los atienda secuencialmente.

Cita textual del resumen:
> "…inserting a delay or a speedup in a…autonomous drive road segment…so that said road segments no longer overlap in time."

## Solución técnica (cómo lo hace)
Planificación temporal de la flota que trata la atención del teleoperador como un **recurso compartido a agendar**, desplazando la cinemática de los vehículos para serializar la demanda de operación remota.

## Alcance y limitaciones
- Presupone rutas predeterminadas y tramos teleoperados conocidos de antemano — encaja con circuitos mineros fijos (carguío-botadero) y no con conducción libre.
- Concedida en US y EP: familia relevante.
- Verificado: titular, prioridad, familia, cita del resumen.

## Relevancia FTO / novedad
Es el arte previo del modelo económico "1 operador : N máquinas". Si el proyecto promete productividad vía **ratio operador/camión**, ese mecanismo de planificación ya está protegido por Einride en US/EP (y practicado comercialmente por Sandvik, Teleo y Cat). La novedad tendría que estar en la **planificación conjunta con la disponibilidad de red**, no en la serialización de la atención del operador.

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
