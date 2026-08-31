---
id: patente-us11223667b2-phantom-auto-multiruta-baja-latencia
titulo: "Low latency wireless communication system for teleoperated vehicle environments — US11223667B2 (Phantom Auto Inc. / hoy Serve Operating Co)"
tipo: patente
tema: Transmisión de video de baja latencia para teleoperación sobre múltiples enlaces inalámbricos públicos con redundancia codificada
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [H04L65/752, H04L43/0852, H04L65/70, H04W4/40, H04N19/164]
topicos: [teleoperacion-supervision-remota, enlace-multiruta-bonding, requisitos-red-latencia-jitter, conectividad-red-vehiculo-autonomo]
anio: 2019
titular: Phantom Auto Inc. (cesión registrada a Serve Operating Co, 2025-09-08)
referencia: US11223667B2
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: vigente
jurisdicciones: [US, EP, WO]
fecha_prioridad: 2019-04-30
trl_relevante: 7-9
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Problema técnico que resuelve
La teleoperación exige video ascendente continuo y de baja latencia sobre **redes celulares públicas**, cuya capacidad y retardo varían sin control del operador. La patente declara que "los algoritmos de control de congestión para transmisiones de una sola ruta no pueden proporcionar el nivel de seguridad requerido" por aplicaciones de robótica en la nube: una sola SIM/una sola red no es suficiente para conducción remota segura.

## Reivindicaciones clave (qué protege)
Reivindicación independiente (síntesis verificada del texto): un sistema que **genera múltiples versiones codificadas del mismo segmento de video con datos redundantes**, y un **orquestador de red** que asigna cada versión a **conexiones inalámbricas distintas** (portadoras/enlaces con parámetros de desempeño diferentes) para transmisión simultánea, con monitoreo de retardo/jitter (clasificaciones H04L43/0852, /0864, /087) y adaptación de la codificación a la capacidad medida.

Cita textual del resumen:
> "A system, method, and non-transitory computer-readable storage medium facilitates wireless transmission of low latency video or other data for teleoperation or other remote support, monitoring, or control applications."

## Solución técnica (cómo lo hace)
Multipath con redundancia a nivel de aplicación: en vez de un único stream sobre un único enlace, se emiten variantes codificadas por varios enlaces heterogéneos y el receptor reconstruye a partir de la primera versión utilizable. La adaptación de tasa/codificación responde a mediciones de retardo de ida y vuelta, jitter y umbrales.

## Alcance y limitaciones
- Cubre la **capa de transporte de video/datos** de la teleoperación, no la dinámica del vehículo ni la maquinaria.
- Familia: US11223667B2, US20200351322A1, US11799936B2, US20240015196A1 (continuaciones). Vencimiento anticipado 2040-04-29.
- Verificado: titular, fechas, CPC y frase del resumen. No se leyó el pliego completo de reivindicaciones (profundidad `abstract`).

## Relevancia FTO / novedad
Es la familia **más directamente relevante** para cualquier arquitectura que agregue varias redes celulares (multi-SIM/bonding) con redundancia para telecomando de un camión. No es esquivable por el simple hecho de "usar dos operadores móviles": lo reivindicado es la generación de **versiones redundantes codificadas** asignadas a enlaces distintos por un orquestador. Rutas de diseño diferenciadas: conmutación (no duplicación) por enlace primario/secundario, FEC estándar sin versiones codificadas múltiples, o degradación adaptativa de calidad sobre enlace único.
**Señal FTO:** vigente en US; sin evidencia de familia CL — el análisis formal de libertad de operación en Chile queda como paso manual en INAPI.

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
