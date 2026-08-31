---
id: patente-us20230247443a1-phantom-auto-mapa-geoespacial-red
titulo: "Optimizing wireless networking using a virtual geographic information system — US20230247443A1 (Phantom Auto Inc.)"
tipo: patente
tema: Base de datos geoespacial de desempeño de red que ajusta los parámetros de conexión del vehículo teleoperado según su ubicación prevista
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [H04W4/40, H04L47/00]
topicos: [teleoperacion-supervision-remota, requisitos-red-latencia-jitter, mapa-cobertura-red-ruta, conectividad-red-vehiculo-autonomo]
anio: 2018
titular: Phantom Auto Inc.
referencia: US20230247443A1 (relacionada: US20190383624A1 — ruteo por desempeño de red predicho)
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: abandonada
jurisdicciones: [US]
fecha_prioridad: 2018-04-12
trl_relevante: 6-8
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Problema técnico que resuelve
La teleoperación necesita una calidad de servicio que la red pública no garantiza de forma homogénea a lo largo de una ruta. La solicitud propone **aprender dónde la red funciona bien y dónde no**, y anticiparse.

## Reivindicaciones clave (qué protege)
Claim 1 (síntesis verificada): método que **controla los parámetros de red del vehículo** (ventana de congestión, tasa de bits) ajustándolos dinámicamente según la **ubicación predicha** y datos de desempeño de red almacenados en una base de datos geoespacial de relaciones aprendidas.

Cita textual del resumen:
> "network connection parameters such as a network congestion window and bit rate are automatically adjusted dependent on a location of a vehicle in order to optimize network performance"

## Solución técnica (cómo lo hace)
Mapa vivo (GIS) de desempeño de red por segmento geográfico, alimentado por telemetría de la flota, que alimenta un control anticipativo de la pila de comunicaciones (y, en la familia hermana US20190383624A1, la **selección de ruta** del vehículo según desempeño de red esperado).

## Alcance y limitaciones
- **Estado legal: abandonada** — no ejerce bloqueo, pero **es arte previo publicado** y por lo tanto destruye novedad.
- Solo US; continuación de solicitudes de 2019 y 2021.
- Verificado: titular, prioridad, estado, cita del resumen.

## Relevancia FTO / novedad
Doble lectura importante para una postulación de I+D:
1. **Sin riesgo FTO** (abandonada, solo US).
2. **Con riesgo de novedad**: "mapear la cobertura de la ruta y planificar/ajustar la teleoperación según ese mapa" está publicado desde 2019. Un proyecto que plantee esto como su núcleo innovador debe demostrar el diferencial (p. ej. mapa multi-tecnología celular + satélite + red privada en topografía minera con obstrucción por bancos y polvo, y su acoplamiento con el despacho de flota).

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
