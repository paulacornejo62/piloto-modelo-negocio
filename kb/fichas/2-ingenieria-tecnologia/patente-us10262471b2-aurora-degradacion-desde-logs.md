---
id: patente-us10262471b2-aurora-degradacion-desde-logs
titulo: "Autonomous vehicle degradation level monitoring — US10262471B2 (Uber → Aurora Operations)"
tipo: patente
tema: Monitorear logs en vivo de una flota de vehículos autónomos para calcular un nivel de degradación por vehículo y decidir servicio o retiro, con umbral variable según condiciones
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [G07C5/008]
topicos: [flota-y-telemetria, disengagement-kpi-piloto, autonomia-supervisada-flota, seguridad-funcional-av]
anio: 2017
titular: Aurora Operations Inc (cesionaria actual; originada en Uber/UATC, EE.UU.)
referencia: US10262471B2 (solicitud US15/602,303; prioridad 2017-05-23; concedida 2019-04-16; expiración ajustada 2037-08-12)
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: vigente (Status "Active")
jurisdicciones: [US]
fecha_prioridad: 2017-05-23
trl_relevante: 7-8
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Problema técnico que resuelve
Cómo un sistema **externo al vehículo** (el gestor del servicio) detecta que un vehículo autónomo se está degradando, usando el flujo de logs que el vehículo emite en operación.

## Reivindicaciones clave (qué protege)
Claim 1 (literal, verificado):
> "1. An on-trip monitoring system for autonomous vehicles (AVs) comprising: one or more processors; and one or more memory resources storing instructions that… cause the on-trip monitoring system to: monitor live log data from AVs operating throughout a given region; determine a degradation level for a respective AV of the AVs based on the live log data from the respective AV; and when the degradation level exceeds a determined threshold, transmit an update command to the respective AV to service or decommission the respective AV; wherein the determined threshold corresponds to a variable risk threshold dependent upon a set of current conditions comprising at least one of lighting conditions, weather conditions, a time of day, day of week, traffic conditions, or road surface conditions."

Claim 4 (literal): "wherein the live log data comprises at least one of diagnostics data or telemetry data."

## Solución técnica (cómo lo hace)
Analítica de logs en vivo del lado del operador: nivel de degradación por vehículo, umbral **condicionado al contexto** (iluminación, clima, tráfico, superficie del camino) y acción de gestión (servicio o retiro de flota).

## Alcance y limitaciones
- Familia **solo US** (sin EP/WO/CL localizados).
- El claim reclama *live log data* y una acción de comando de vuelta al vehículo ("transmit an update command… to service or decommission"). Una analítica **puramente descriptiva** (KPIs, informes, causas de detención) que no comande el vehículo cae fuera de ese claim.
- Presupone logs con contenido de diagnóstico/telemetría; el caso Kaufmann parte con logs mucho más pobres.

## Relevancia FTO / novedad
Es la referencia central para el eje (b): "instrumentación/analítica propia sobre logs del vendor". Deja claro que:
1. Monitorear logs de flota para inferir estado del vehículo y actuar es arte previo desde 2017 (y con patente **viva** en EE.UU. hasta 2037).
2. En Chile no hay derecho oponible (sin familia CL) → sin riesgo de infracción por operar en el país.
3. La novedad de Kaufmann tiene que estar en la **reconstrucción de variables operacionales no observadas** (causa de detención, uptime real, incidentes) a partir de señales indirectas y pobres, no en el concepto de monitorear logs.

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
