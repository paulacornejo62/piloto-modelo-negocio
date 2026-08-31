---
id: paper-demmers-2018-nmpc-crecimiento-pollos-cerdos
titulo: "Neural predictive control of broiler chicken and pig growth (Demmers et al., 2018)"
tipo: paper
tema: Red neuronal recurrente + control predictivo no lineal (NMPC) para modelar y controlar el crecimiento de aves y cerdos
area_oecd: "4 Ciencias Agrícolas (4.2 Ciencia animal y lechera)"
topicos: [control-predictivo-crecimiento-animal]
anio: 2018
autores: [Demmers, et al.]
referencia: https://doi.org/10.1016/j.biosystemseng.2018.06.022
motor: PDF directo (texto completo en carpeta, compartido por consultora)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: []
fecha_registro: 2026-08-21
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Desarrollar un marco de modelado y control que combine redes neuronales recurrentes con control predictivo no lineal (NMPC) para representar y controlar el crecimiento de pollos de engorda y de cerdos, dentro de un mismo marco metodológico.

## Hipótesis
Que un modelo de red neuronal recurrente, integrado a un esquema de control predictivo no lineal, puede representar la dinámica de crecimiento tanto de aves como de cerdos con un marco de modelado común, pese a ser especies distintas.

## Metodología
- **Diseño:** modelado con red neuronal recurrente + control predictivo no lineal (NMPC).
- **Datos / muestra:** datos de crecimiento de pollos de engorda y de cerdos (no se detalla tamaño exacto en esta ficha resumida).
- **Técnicas:** red neuronal recurrente para modelar la dinámica de crecimiento; NMPC para usar ese modelo en un esquema de control (p.ej. ajuste de alimentación).
- **Métricas:** no se detallan cifras exactas en esta ficha resumida (PDF completo disponible en carpeta).

## Resultados principales
- Un mismo marco de modelado (red neuronal recurrente + NMPC) es aplicable tanto a pollos de engorda como a cerdos.

## Conclusiones
El control predictivo no lineal basado en redes neuronales recurrentes es una vía viable para modelar y controlar el crecimiento animal en ambas especies (aves, cerdos), dentro de un marco metodológico común.

## Limitaciones
Ficha registrada con menor nivel de detalle (prioridad TIER 2); cifras y detalle metodológico exacto disponibles en el PDF completo en carpeta. Es un modelo de **crecimiento/peso**, no de composición de excreta o purín — distinto objetivo del modelo real de Agrosuper para el Objetivo 2, aunque comparte la familia de herramientas (redes neuronales recurrentes en contexto porcino/avícola).

## Relevancia / brecha para el estado del arte
Antecedente metodológico de aplicación de redes neuronales recurrentes a un problema de modelado dinámico en producción animal (crecimiento, no excreción) — refuerza que el uso de redes recurrentes en contexto porcino/avícola es una práctica ya explorada, aunque con un objetivo de modelado distinto (crecimiento/control de alimentación, no predicción de composición de purín).

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
