---
id: patente-cl2024001923a1-uchile-navegacion-campo-abierto
titulo: "Método y sistema para navegar un vehículo autónomo en campo abierto — CL2024001923A1 (Universidad de Chile)"
tipo: patente
tema: Navegación topológica (intersecciones y segmentos) con filtro de partículas y procesos gaussianos para vehículos autónomos en recintos al aire libre sin infraestructura estandarizada
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [G05D1/0272]
topicos: [prior-art-chile, entorno-semi-estructurado, localizacion-gnss-rtk, recinto-privado-odd]
anio: 2021
titular: Universidad de Chile (inventores Ruiz-del-Solar, Herrmann Priesnitz, Parra Tsunekawa, Correa Pérez)
referencia: CL2024001923A1 (prioridad 2021-12-24; entrada nacional CL 2024-06-24; publicación 2024-12-20; familia WO/US/AU/CL/PE)
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: parcial
estado_legal: en trámite (publicación de solicitud CL; no se verificó concesión — Google Patents no muestra estado ni reivindicaciones para este documento)
jurisdicciones: [CL, WO, US, AU, PE]
fecha_prioridad: 2021-12-24
trl_relevante: 5-6
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Problema técnico que resuelve
Navegar de forma autónoma en un recinto **a cielo abierto y sin estructura vial estandarizada** (sin señalización ni carriles pintados), donde la localización métrica fina es frágil.

## Reivindicaciones clave (qué protege)
No se pudo extraer el texto de reivindicaciones: la ficha de Google Patents para CL2024001923A1 no publica el cuerpo de claims (solo resumen traducido). **Pendiente de verificación manual** en INAPI o en el miembro WO/US de la familia.

Resumen (literal, traducido del español por la fuente):
> "Method and system for navigation of an autonomous vehicle in an open-air location. The method comprises: acquiring a plurality of observations (72) and odometry information, from a plurality of discrete poses during driving; accessing a topological map (10) of the open-air location comprising intersections and segments; accessing an observational map (20) of the open-air location with past observations comprising environmental information associated with an intersection or a segment; processing past observations, acquired observations and odometry information, applying a particle filtering technique and Gaussian Processes to model acquired observations of discrete poses as a continuous variable and estimating the current pose and according to a current direction of movement, statistically predicting a next pose of the autonomous vehicle; commanding the autonomous vehicle (30) through actuators controlled by the processing unit (33), based on the detection of whether the autonomous vehicle (30) is in a segment or at an intersection…"

## Solución técnica (cómo lo hace)
Sustituye el mapa métrico de alta definición por un **mapa topológico + mapa observacional** del recinto, y resuelve la pose con filtro de partículas y procesos gaussianos; el comando es "avanzar por el segmento" o "girar en la intersección".

## Alcance y limitaciones
- Es una tecnología **embarcada de navegación**: requiere controlar los actuadores del vehículo. No aplica al caso de vehículo caja negra.
- Estado legal chileno no verificado (no visible en Google Patents); requiere consulta manual a INAPI.

## Relevancia FTO / novedad
Único prior art **chileno** localizado que aborda directamente el entorno no estandarizado al aire libre, y de origen académico nacional (U. de Chile). Dos implicancias para Kaufmann:
1. Si el proyecto se desviara a desarrollar navegación propia, este documento es la primera barrera a revisar en Chile.
2. Como el proyecto es de **capa operacional sobre vehículo cerrado**, no hay solapamiento con el objeto reclamado; refuerza que el eje elegido es distinto del núcleo de conducción.
3. Señala una capacidad local existente (AMTC/U. de Chile) como posible contraparte o referente científico del proyecto.

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
