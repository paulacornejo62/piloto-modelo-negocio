---
id: patente-us20230297100a1-asi-cnh-filtrado-comandos-latencia
titulo: "System and method for assisted teleoperations of vehicles — US20230297100A1 (Autonomous Solutions Inc. / CNH Industrial America LLC)"
tipo: patente
tema: Filtrado a bordo de los comandos del operador remoto cuando la latencia supera un umbral, usando los sensores del propio vehículo
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [G05D1/0022, B60W30/00]
topicos: [teleoperacion-supervision-remota, teleoperacion-fallback, requisitos-red-latencia-jitter]
anio: 2019
titular: CNH Industrial America LLC y Autonomous Solutions Inc.
referencia: US20230297100A1
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: abandonada
jurisdicciones: [US]
fecha_prioridad: 2019-12-23
trl_relevante: 6-8
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Problema técnico que resuelve
Un comando remoto que llega tarde (o mal) puede provocar colisión o vuelco en un vehículo de trabajo pesado. El vehículo necesita **desconfiar** del comando remoto en función de la latencia medida.

## Reivindicaciones clave (qué protege)
Claim 1 (síntesis verificada): el sistema del vehículo recibe comandos remotos y datos de sensores, **determina la latencia de comunicación** y, cuando ésta supera un umbral, **deriva un comando filtrado** (de velocidad) a partir del comando remoto y de los sensores, ajustando la velocidad del vehículo en consecuencia.

Cita textual del resumen:
> "A vehicle system includes at least one sensor and a communications system configured to receive one or more remote operations commands. The control system is further configured to execute an automatic adjustment teleoperations system to derive a filtered speed command based on the one or more remote operations commands and the at least one sensor."

## Solución técnica (cómo lo hace)
Capa de autonomía mínima a bordo que arbitra entre la intención del teleoperador y la percepción local, con la latencia como variable de conmutación. Aplicación declarada: tractores agrícolas.

## Alcance y limitaciones
- **Abandonada** (no se pagó la tasa de concesión, plazo agosto de 2025): no bloquea, pero es arte previo.
- Solo US; dos solicitudes con la misma prioridad.
- ASI (Autonomous Solutions Inc.) es el proveedor de autonomía de Epiroc para camiones mineros: el actor es relevante en minería aunque la reivindicación se ejemplifique en agro.

## Relevancia FTO / novedad
Documenta que la **asistencia local que corrige/limita el comando remoto según latencia** es técnica conocida (prioridad 2019). Un proyecto de telecomando en minería no puede fundar su novedad en "el camión se protege solo si el comando llega tarde". La contribución debe estar en el resto de la cadena (arquitectura de conectividad extremo a extremo, integración con el OEM, operación en faena real, régimen de seguridad).

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
