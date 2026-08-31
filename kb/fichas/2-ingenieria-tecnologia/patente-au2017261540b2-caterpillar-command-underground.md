---
id: patente-au2017261540b2-caterpillar-command-underground
titulo: "Command for underground — AU2017261540B2 (Caterpillar Inc.)"
tipo: patente
tema: Sistema de automatización de maquinaria minera con modos conmutables manual / línea de vista / teleremoto / semiautónomo / autónomo y módulo de apagado remoto
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [G05D1/0011, G05D1/0022, G05D1/0038, E02F9/205, E02F9/2025]
topicos: [teleoperacion-minera, teleoperacion-supervision-remota, seguridad-parada-remota, conectividad-red-vehiculo-autonomo]
anio: 2016
titular: Caterpillar Inc.
referencia: AU2017261540B2 (relacionadas: AU2018201213B2, US9797247B1)
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: vigente
jurisdicciones: [AU, US]
fecha_prioridad: 2016-11-21
trl_relevante: 9
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Problema técnico que resuelve
Operar maquinaria en minería subterránea (baja altura de túnel, riesgo de inestabilidad del terreno) sin operador a bordo, permitiendo que las **funciones avanzadas de control de la máquina** (asistencias) se ejecuten **simultáneamente** con los comandos que llegan desde fuera de la máquina. Los sistemas previos no ejecutaban ambas cosas de forma concurrente.

## Reivindicaciones clave (qué protege)
Claim 1 (síntesis verificada): un **Machine Automation System** compuesto por ECMs del vehículo, transceptor inalámbrico local, LAN Ethernet con router y switches, un **AECM** (módulo de control de automatización), un bus CAN, monitoreo del entorno (cámaras IP, micrófono, LADAR) y un **Remote Shutdown Module (RSM)**. El AECM recibe las señales de entrada remotas y genera señales de control hacia los ECMs; el RSM recibe señales de seguridad desde fuera de la máquina. Lo reivindicado incluye ejecutar "advanced machine control features concurrently with execution of the input control signals received from off-board the machine".

Cita textual del resumen:
> "The AECM is configured to generate output control signals, and to transmit the output control signals to at least one of the Vehicle ECMs, wherein the output control signals control an operation of the machine."

## Solución técnica (cómo lo hace)
Arquitectura de a bordo (Ethernet + CAN + AECM) que abstrae el origen del comando: cabina, control de línea de vista, teleremoto guiado por video, semiautónomo o autónomo pleno. Añade una vía **independiente** de parada remota (RSM), separada del canal de control.

## Alcance y limitaciones
- Aplicación declarada: minería subterránea, cargadores LHD. No reivindica la capa de red de larga distancia.
- Familia acotada (AU/US); vencimiento anticipado 2037-11-15.
- Verificado: titular, fechas, CPC, estado legal y frase del resumen.

## Relevancia FTO / novedad
Relevante como **estado del arte de la arquitectura a bordo del telecomando industrial**: la conmutación de modos y la parada remota independiente ya son técnica conocida y patentada por el mayor OEM minero. Un proyecto no puede reclamar novedad en "poder pasar de manual a teleoperado" ni en "parada de emergencia remota". La familia es AU/US: no hay evidencia de protección en Chile, pero sí de **anterioridad** que destruye novedad de reivindicaciones genéricas.

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
