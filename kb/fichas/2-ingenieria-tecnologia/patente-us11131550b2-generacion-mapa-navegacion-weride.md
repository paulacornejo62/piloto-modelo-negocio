---
id: patente-us11131550b2-generacion-mapa-navegacion-weride
titulo: "Method for generating road map for vehicle navigation and navigation device — US11131550B2 (WeRide Corp.)"
tipo: patente
tema: Generación de mapa de alta definición (carriles, propiedades de tráfico, waypoints) a partir de imágenes de vía para navegación autónoma
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [G01C21/32, G01C21/3804, G01C21/26, G06V20/56, G06V20/588]
topicos: [vehiculo-autonomo-l4, localizacion-y-mapeo, mapeo-de-rutas-comisionamiento]
anio: 2018
titular: WeRide Corp.
referencia: US11131550B2
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: caducada
jurisdicciones: [US, CN]
fecha_prioridad: 2018-03-29
trl_relevante: 8
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Problema técnico que resuelve

Un vehículo autónomo L4 no navega con un mapa de navegación comercial: necesita un mapa con **semántica de carril** (bordes, sentido, propiedades de tráfico, señales, semáforos) y waypoints sobre los cuales planificar. Construir ese mapa a mano para cada sitio es caro y es el cuello de botella del despliegue en un recinto nuevo.

## Reivindicaciones clave (qué protege)

Reivindicación independiente 1 (cita literal del inicio): *"A method for generating a road map for vehicle navigation, comprising: providing original road image data having an image of a road; identifying boundary lines defining respective lane segments of the road from the original road image data; associating traffic properties with the lane segments defined by the boundary lines, respectively..."*

Lo que monopoliza: el **pipeline de generación del mapa** — de imagen original de la vía a segmentos de carril delimitados por líneas de borde, con propiedades de tráfico asociadas y objetos de control (señales/semáforos) vinculados, más los waypoints que guían el movimiento autónomo.

## Solución técnica (cómo lo hace)

Se parte de datos de imagen del recorrido (barrido del sitio), se detectan las líneas de borde que definen cada segmento de carril, se asocian propiedades de tráfico a cada segmento y se vinculan objetos de control de tráfico; el resultado es un mapa con waypoints consumible por el planificador del vehículo. Es, en esencia, la **actividad de mapeo y comisionamiento de ruta** que todo despliegue en sitio nuevo requiere.

## Alcance y limitaciones

Cubre la generación del mapa a partir de imágenes; no cubre localización en línea contra ese mapa ni el control del vehículo. Estado legal en Google Patents: *"Expired - Fee Related"* — expiración nominal 2039-10-23, pero con caducidad por no pago de anualidades efectiva 2025-09-28. Familia: US16/359,991 y contraparte china CN201910251656.3A (esta última con vigencia propia a verificar).

## Relevancia FTO / novedad

Doble lectura. (1) **FTO**: al estar caducada por falta de pago en US y sin evidencia de familia chilena, el riesgo de bloqueo es bajo; además, el mapeo del recinto lo ejecuta normalmente el proveedor del vehículo como parte del comisionamiento. (2) **Novedad**: el mapeo de rutas y la generación del mapa semántico son **estado del arte industrial desde 2018** — un proyecto que declare como I+D "mapear el recinto" está describiendo integración, no investigación. La novedad defendible tendría que estar en algo específico del entorno (mapa que se degrada por cambio de layout de patio, tráfico mixto con grúas/personas, condiciones locales), no en el acto de mapear.

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
