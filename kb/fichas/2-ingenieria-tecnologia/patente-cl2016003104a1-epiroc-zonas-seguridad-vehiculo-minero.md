---
id: patente-cl2016003104a1-epiroc-zonas-seguridad-vehiculo-minero
titulo: "Sistema y método de seguridad para la operación automatizada de vehículos mineros en una zona de trabajo — CL2016003104A1 (Epiroc Rock Drills AB)"
tipo: patente
tema: Prior art presentado en Chile sobre operación automatizada/remota de vehículos mineros y definición dinámica de zonas de seguridad
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [E21F17/18, G05D1/0011]
topicos: [teleoperacion-minera, prior-art-chile, seguridad-parada-remota, autonomia-supervisada-flota]
anio: 2014
titular: Epiroc Rock Drills AB (ex Atlas Copco)
referencia: CL2016003104A1 (familia: WO2015187081A1, SE538029C2, CA2949360C, AU2015268954B2, ZA201607812B)
motor: Google Patents (pasada país=CL)
profundidad_lectura: abstract
estado_evidencia: parcial
estado_legal: desconocido (publicada en CL; estado de concesión no verificado — requiere consulta manual en INAPI)
jurisdicciones: [CL, SE, CA, AU, ZA, WO]
fecha_prioridad: 2014-06-05
trl_relevante: 9
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Problema técnico que resuelve
Cómo delimitar y hacer cumplir **zonas de seguridad** en una faena donde operan vehículos mineros automatizados/controlados remotamente, sin tener que reconfigurar el sistema de seguridad cada vez que cambia la zona.

## Reivindicaciones clave (qué protege)
Claim 1 (síntesis verificada): sistema de seguridad con una **unidad de control principal**, al menos una **unidad de control remoto**, varias **unidades de control de barrera** y una unidad de control del vehículo, que permite **definir zonas de seguridad para la operación automatizada** sin reconfigurar el sistema.

Cita textual del resumen:
> "A security system… comprising at least one remote control unit, a main control unit, a plurality of barrier control units… where safety zones for the automated operation of mining vehicles can be defined… without reconfiguring the safety system."

## Solución técnica (cómo lo hace)
Arquitectura distribuida de control de acceso: barreras/portales instrumentados que reportan a un control central, el cual habilita o inhibe la operación automatizada o remota dentro de la zona definida.

## Alcance y limitaciones
- Cubre la **capa de seguridad de la faena** (quién puede entrar mientras la máquina opera sin operador a bordo), no el enlace de datos ni la conducción.
- **Está presentada en Chile**: es el hallazgo FTO nacional más relevante de esta pasada.
- Estado de concesión/vigencia en CL **no verificado** — Google Patents muestra la publicación; INAPI no es consultable automáticamente.

## Relevancia FTO / novedad
Confirma que los OEM mineros (Epiroc, y también Sandvik con CL2017001713A1 "Control de paso de zona") **sí protegen en Chile** el entorno de la operación automatizada. Cualquier proyecto que instale camiones sin operador a bordo en faena chilena debe considerar esta capa (segregación de zonas, control de acceso de personas) en su análisis de libertad de operación. **El FTO formal en INAPI queda como paso manual.**

> Relaciones con otras fichas → `../../indice.json`.
