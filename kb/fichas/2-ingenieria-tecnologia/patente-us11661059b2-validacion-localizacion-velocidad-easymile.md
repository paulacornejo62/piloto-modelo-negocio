---
id: patente-us11661059b2-validacion-localizacion-velocidad-easymile
titulo: "Method and system for modifying the speed of a vehicle depending on the validation of its calculated localization field — US11661059B2 (EasyMile)"
tipo: patente
tema: Validación cruzada de la localización de un shuttle autónomo con fuentes independientes y reducción automática de velocidad cuando la localización no es consistente
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [G05D1/0077, G05D1/0231, G01S5/0263, B60W30/146, G01S13/931]
topicos: [vehiculo-autonomo-l4, localizacion-y-mapeo, shuttle-autonomo-pasajeros, seguridad-funcional-av]
anio: 2019
titular: EasyMile (Easymile SAS)
referencia: US11661059B2
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: vigente
jurisdicciones: [US, EP]
fecha_prioridad: 2019-05-06
trl_relevante: 9
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Problema técnico que resuelve

Un shuttle autónomo de baja velocidad que opera en circuitos mapeados depende críticamente de saber dónde está. Si la localización calculada (fusión de GNSS, LiDAR contra mapa, odometría) se degrada —zonas sin cobertura satelital, entornos que cambian, sensores sucios— el vehículo puede seguir moviéndose con una pose errónea. El problema es cómo **detectar en línea que la localización dejó de ser confiable** y degradar la operación de forma segura, sin detener la operación completa cada vez.

## Reivindicaciones clave (qué protege)

Reivindicación independiente 1 (cita literal del inicio): *"A method of modifying the speed of a vehicle equipped with a plurality of independent localization sources of data, wherein a calculated localization source of data provides a calculated location of the vehicle with a first uncertainty as a result of processing data from a subset of the plurality of independent localization sources of data..."*

Lo que monopoliza: el **método de validación cruzada** de la localización calculada contra un conjunto de fuentes de localización independientes, con umbral de consistencia, y la **modificación (reducción) automática de la velocidad** del vehículo como consecuencia de esa validación fallida. Es una reivindicación de método + sistema, no de hardware particular.

## Solución técnica (cómo lo hace)

El vehículo lleva varias fuentes de localización independientes (p.ej. GNSS, LiDAR/mapa, odometría, radar). Una fuente "calculada" entrega una pose con una incertidumbre asociada. El sistema compara esa pose con las demás fuentes; si un número suficiente de fuentes independientes no concuerda dentro de la incertidumbre, se considera no validada y se **reduce la velocidad** (hasta detener) hasta restablecer la consistencia. Las clasificaciones asignadas (G05D1/0077 "vehicle control with redundant signals or controls", G01S5/0263 posicionamiento híbrido, B60W30/146 speed limiting) confirman el eje: redundancia de localización → limitación de velocidad.

## Alcance y limitaciones

Cubre el mecanismo de validación-y-degradación de velocidad; no cubre el algoritmo de localización en sí (SLAM, matching de nube de puntos), ni la planificación de ruta, ni el mapeo del recinto. Vigente: *"Active, expires 2040-07-23"* (Google Patents). Familia: solicitud EP prioritaria (EP 19315032.3) + concesión US.

## Relevancia FTO / novedad

Para un piloto que **compra** un shuttle a un proveedor internacional, esta patente es del proveedor de la plataforma (EasyMile) y opera dentro del producto: quien la practica es el fabricante, no el operador del recinto. **No bloquea** la operación ni el mapeo de rutas del cliente. Sí delimita el espacio de novedad si el proyecto pretendiera desarrollar **su propio** módulo de validación de localización con degradación de velocidad — ahí habría que esquivar (p.ej. lógica de degradación distinta de la velocidad, o validación no basada en fuentes independientes). No hay evidencia de familia en Chile (no verificado en INAPI; ver cobertura del Deep Research).

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
