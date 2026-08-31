---
id: patente-us10295363b1-statefarm-aptitud-autonomia-mapeo
titulo: "Autonomous operation suitability assessment and mapping — US10295363B1 (State Farm)"
tipo: patente
tema: Puntuar la aptitud de cada tramo de vía para operación autónoma a partir de datos de operación de una flota (accidentes y cuasi-accidentes) y mapear esos puntajes
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [G01C21/3461]
topicos: [recinto-privado-odd, disengagement-kpi-piloto, comisionamiento-mapeo-ruta, flota-y-telemetria]
anio: 2016
titular: State Farm Mutual Automobile Insurance Co (EE.UU.)
referencia: US10295363B1 (solicitud US15/409,143; prioridad 2016-01-22; concedida 2019-05-21; expiración anticipada 2037-01-18)
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: vigente (Status "Active"; expiración anticipada 2037-01-18)
jurisdicciones: [US]
fecha_prioridad: 2016-01-22
trl_relevante: 6-7
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Problema técnico que resuelve
¿Qué partes de una red vial son aptas para operación autónoma y en qué nivel? El problema es exactamente el de "calificar el territorio" antes/durante el despliegue, y mantener esa calificación viva con la operación real.

## Reivindicaciones clave (qué protege)
Claim 1 (literal, verificado, extracto):
> "1. A computer-implemented method for analyzing roadway suitability for autonomous or semi-autonomous vehicle operation, comprising: receiving, at one or more processors, map data including indications of a plurality of road segments; receiving, at the one or more processors, operating data from a plurality of vehicles having at least one autonomous operation feature, wherein the operating data includes location data associated with operation of the plurality of vehicles and wherein the operating data further includes data regarding accidents and data regarding hazardous events other than accidents, the hazardous events other than accidents including near collisions in which some of the plurality of vehicles came within threshold distances of other vehicles; selecting… a road segment to analyze…; associating… a subset of the operating data with the road segment based upon the location data; determining… one or more risk levels associated with the road segment…; determining… one or more suitability scores for the road segment based upon the one or more risk levels, each suitability score indicating a category of suitability for autonomous or semi-autonomous vehicle operation; and storing, in a database, the one or more suitability scores…"

Claim 2: generación de "map tiles including visual representations of the one or more suitability scores".

## Solución técnica (cómo lo hace)
Pipeline: datos de operación de flota georreferenciados → asociación a segmento → nivel de riesgo por segmento → puntaje de aptitud por categoría de autonomía → base de datos y mapa. El insumo son **eventos** (accidentes y cuasi-accidentes), no el código del vehículo.

## Alcance y limitaciones
- Familia **solo US** (no hay EP/WO/CL en la publicación consultada): fuera de Chile no hay derecho oponible.
- El claim exige explícitamente "near collisions… within threshold distances of other vehicles" como parte del dato de operación: si la caracterización usa otras variables (polvo/visibilidad, detenciones, causas de detención, tráfico mixto peatón-grúa), queda fuera del claim literal.
- Está pensado para vía pública y flota amplia; no cubre la **campaña experimental** para caracterizar un recinto privado.

## Relevancia FTO / novedad
Es el arte previo más cercano al eje (a)+(b) de Kaufmann: "puntuar aptitud para autonomía con datos de operación". Consecuencias:
1. No se puede reclamar como novedad "calificar segmentos según datos de operación de la flota" a secas.
2. Sí queda abierto: el **protocolo experimental de campo** (qué se mide, con qué instrumentación, bajo qué condiciones de maicillo/polvo/neblina) para **decidir la habilitación de un recinto no estandarizado**, y la reconstrucción de esos indicadores desde logs pobres del vendor (sin sensores propios ni acceso a percepción).
3. Sin protección en Chile → sin riesgo de infracción local; el valor de la ficha es de **novedad**, no de libertad de operación.

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
