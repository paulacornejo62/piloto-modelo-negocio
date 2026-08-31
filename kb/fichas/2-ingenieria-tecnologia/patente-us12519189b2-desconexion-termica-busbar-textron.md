---
id: patente-us12519189b2-desconexion-termica-busbar-textron
titulo: "Thermally disconnecting high power busbars for battery system propagation control — US12519189B2 (Textron/Bell)"
tipo: patente
tema: Actuador termico autonomo que corta el busbar entre modulos para aislar el modulo en fuga termica y frenar la propagacion
area_oecd: "2 Ingenieria y Tecnologia (2.2 Ingenieria electrica, electronica)"
ipc: [H01H85/0241]
topicos: [desconexion-emergencia-bateria, fuga-termica-bateria, seguridad-bateria-litio]
anio: 2022
titular: Textron Innovations Inc / Bell Textron
referencia: US12519189B2
motor: Google Patents
profundidad_lectura: full-text
estado_evidencia: verificado
estado_legal: vigente
jurisdicciones: [US]
fecha_prioridad: 2022-01-11
trl_relevante: 5
fecha_registro: 2026-07-22
proyectos:
  - lipigas
---

## Problema tecnico que resuelve
En sistemas de bateria densamente empacados, la temperatura elevada de un segmento/modulo se propaga facilmente a los adyacentes. Se necesita aislar termica y electricamente el modulo en falla para prevenir/frenar la propagacion del incendio.

## Reivindicaciones clave (qué protege)
Sistema de bateria con metodos para aislar termicamente un modulo en fuga termica: en una realizacion, un ACTUADOR TERMICO corta el busbar que une modulos vecinos, previniendo o ralentizando la propagacion; en otras, un material fusible une porciones del busbar y las altas temperaturas lo funden, rompiendo la conductividad termica/electrica entre porciones y modulos vecinos. El disparo es por TEMPERATURA (autonomo), no por señal de colision.

## Solución técnica (cómo lo hace)
Desconexion gatillada por el propio calor del evento: el actuador/material fusible responde directamente a la temperatura local, sin depender de un sensor externo ni de una señal del SRS/cargador. Actua a nivel de busbar entre modulos.

## Alcance y limitaciones
Es aislamiento INTERNO al pack para control de propagacion entre modulos, NO un desacople full-pack del vehiculo/cargador ni de un peligro externo. No corta el pack completo respecto de su entorno; segrega el modulo en falla. Solo US. Origen aeronautico (Bell/Textron, eVTOL).

## Relevancia FTO / novedad
Es la pieza mas cercana a un disparo TERMICO AUTONOMO de desconexion — confirma que la idea existe en patentes, pero aplicada a la propagacion intra-pack, no al desacople del pack de una fuente/peligro externo (la jaula de GLP). Delimita la novedad de Lipigas: lo no cubierto es un desacople full-pack disparado autonomamente por precursor termico para proteger un almacenamiento de GLP adyacente durante la carga. No bloquea; refuerza que el desafio del gerente de seguridad no esta resuelto comercialmente en esa configuracion.

> Relaciones: contrasta con patente-us9221343b2 (mismo fin de desconexion, pero gatillo colision y a nivel full-pack). Ver `../../indice.json`.
