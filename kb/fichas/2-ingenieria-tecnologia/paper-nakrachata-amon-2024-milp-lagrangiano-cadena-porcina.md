---
id: paper-nakrachata-amon-2024-milp-lagrangiano-cadena-porcina
titulo: "Optimizing vertically integrated pork production supply chain: A Lagrangian heuristic approach (Nakrachata-Amon et al., 2024)"
tipo: paper
tema: MILP + heurística Lagrangiana para planificación coordinada de cadena de suministro porcina integrada verticalmente
area_oecd: "2 Ingeniería y Tecnología (2.11 Otras ingenierías y tecnologías)"
topicos: [milp-programacion-produccion-carnica]
anio: 2024
autores: [Nakrachata-Amon, et al.]
referencia: https://doi.org/10.1016/j.heliyon.2024.e26407
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
Optimizar la cadena de suministro de una producción porcina integrada verticalmente (molino de alimento + engorda), mediante programación entera mixta (MILP) combinada con una heurística Lagrangiana.

## Hipótesis
Que un enfoque MILP + heurística Lagrangiana puede coordinar la planificación de producción entre etapas de una cadena porcina integrada verticalmente (molino de alimento y engorda) de forma más eficiente que una planificación no coordinada.

## Metodología
- **Diseño:** formalización matemática (MILP) + heurística Lagrangiana para resolución a escala real.
- **Datos / muestra:** cadena de producción porcina integrada verticalmente (molino de alimento + engorda).
- **Técnicas:** programación entera mixta (MILP) + heurística Lagrangiana para hacer tratable el problema a escala real.
- **Métricas:** no se detallan cifras exactas en esta ficha resumida (PDF completo disponible en carpeta).

## Resultados principales
- Plan de producción coordinado (molino de alimento + engorda) obtenido mediante MILP + heurística Lagrangiana.

## Conclusiones
La combinación de MILP con una heurística Lagrangiana es viable para coordinar la planificación de producción en una cadena porcina integrada verticalmente, a escala de problema real.

## Limitaciones
Ficha registrada con menor nivel de detalle (prioridad TIER 2); cifras exactas disponibles en el PDF completo en carpeta. **No es específico a corte/desposte** (la etapa de programación de producción de planta de proceso que aborda el Objetivo 3 de Agrosuper) — aborda la coordinación aguas arriba (alimento + engorda), una etapa distinta de la cadena.

## Relevancia / brecha para el estado del arte
Refuerza el vacío de estado del arte para el enfoque KNN+MILP de Agrosuper (Objetivo 3, Programación Maestra de Producción): ningún paper encontrado en este lote de revisión combina MILP con las características específicas del problema de Agrosuper (asignación cliente-planta vía KNN + secuenciación de corte/desposte). Este paper confirma que MILP es una técnica activa y vigente para problemas de cadena de suministro porcina, pero en una etapa distinta (molino+engorda, no planta de proceso) — complementa, sin solaparse, a [[paper-vlk-2025-optimizacion-compra-produccion-planta-carnica]] y [[paper-mdpi-2023-food-scheduling-milp-vs-reglas]].

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
