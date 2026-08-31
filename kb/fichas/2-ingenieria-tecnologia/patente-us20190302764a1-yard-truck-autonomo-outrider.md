---
id: patente-us20190302764a1-yard-truck-autonomo-outrider
titulo: "Systems and methods for automated operation and handling of autonomous trucks and trailers hauled thereby (Outrider Technologies / Azevtec, US20190302764A1 → US11429099B2)"
tipo: patente
tema: Operación autónoma de camión de patio (yard truck): acople/desacople de remolques, servidor de seguimiento y estación de puertas
area_oecd: "2 Ingeniería y Tecnología (2.3 Ingeniería mecánica)"
ipc: B60W60
topicos: [vehiculo-autonomo-carga, operacion-mixta-seguridad, v2i-iot-logistica]
anio: 2019
autores: [Andrew F. Smith, Lawrence S. Klein, Stephen A. Langenderfer, Martin E. Sotola, Vikas Bahl, Mark H. Rosenblum, Peter James, Dale Rowley, Matthew S. Johannes, Gary Seminara, Jeremy M. Nett]
referencia: https://patents.google.com/patent/US20190302764A1/en
motor: Google Patents (tools/browse.mjs gp + open)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "7-9 (titular con producto comercial de yard automation)"
metricas_clave: ["familia amplia: CN CA WO EP US ES AU SG (2019-2025)", "136 citas de patentes, 167 citada por", "concedida como US11429099B2 (2022-08-30)"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Problema que resuelve
Las maniobras de patio (acoplar/desacoplar remolques, conectar líneas neumáticas y eléctricas, subir/bajar patas de apoyo, abrir puertas traseras, calzar) son manuales y exigen que el conductor baje del vehículo; se busca automatizarlas dentro de un recinto (planta, puerto, centro de distribución).

## Solución técnica (según descripción)
Sistema de camión de patio autónomo con procesador de conducción autónoma, conjunto de sensores para terreno/objetos y para asistir el acople, **servidor interconectado inalámbricamente** que rastrea el movimiento del camión y determina las posiciones de acople/desacople, más una estación de puertas que abre y asegura las puertas traseras del remolque. Incluye cálculo de altura del remolque, verificación de si el docking es seguro, y traspaso a control manual por un usuario.

## Reivindicaciones / alcance
El alcance cubre el conjunto vehículo autónomo de patio + servidor de gestión + infraestructura de patio (estación de puertas, calzado automatizado, organización de contenedores intermodales).

## FTO / lectura para el proyecto
Señal fuerte de que la **automatización de patio con supervisión por servidor está patentada por actores comerciales** (Outrider) desde 2019 y en fase de producto. Para el caso Kaufmann esto delimita el estado del arte: el concepto "vehículo autónomo de carga en recinto + servidor de monitoreo" no es novedoso en sí; la eventual novedad debe buscarse en el problema específico (operación mixta del recinto chileno, continuidad de conectividad, comportamiento ante pérdida de enlace, interacción de retiro de carga), no en la arquitectura general.

**Cita textual (abstract):**
- "A server, interconnected, wirelessly with the processor, that tracks movement of the truck around and determines locations for trailer connection and disconnection."


> **Aviso de familia:** la KB ya contiene [[patente-us12344057b2-operacion-automatizada-patio-outrider]] (misma familia Outrider, concesión posterior). Leer ambas juntas; no crear nuevas fichas por miembro de familia.

> Relaciones con otras fichas → `../../indice.json`.
