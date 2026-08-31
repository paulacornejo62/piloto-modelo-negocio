---
id: paper-vlk-2025-optimizacion-compra-produccion-planta-carnica
titulo: Purchase and Production Optimization in a Meat Processing Plant (Vlk, Sucha, Rudy & Idzikowski, 2025; publicado en ITOR, DOI 10.1111/itor.70081; preprint arXiv:2507.15866)
tipo: paper
tema: Optimización de compra y producción vía programación entera lineal para una empresa cárnica real
area_oecd: "2 Ingeniería y Tecnología (2.11 Otras ingenierías y tecnologías)"
topicos: [milp-programacion-produccion-carnica]
anio: 2025
autores: [Marek Vlk, Premysl Sucha, Jaroslaw Rudy, Radoslaw Idzikowski]
referencia: "https://doi.org/10.1111/itor.70081 (versión publicada en International Transactions in Operational Research — DOI del índice de bibliografía de la consultora, resuelto por doi.org); preprint: https://arxiv.org/abs/2507.15866 (arXiv:2507.15866)"
motor: WebFetch (arXiv) + DOI publicado verificado por doi.org (índice de bibliografía de la consultora)
profundidad_lectura: abstract
estado_evidencia: verificado
trl_relevante: -
metricas_clave: []
fecha_registro: 2026-08-18
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Resolver un problema real de optimización de compra y procesamiento de materiales para una empresa de procesamiento de carne, enfocado puramente en la etapa de producción (no en la cadena de suministro completa).

## Hipótesis
Que las restricciones de cantidad mínima de pedido y de porcentaje mínimo en alternativas de procesamiento —ambas ampliamente descuidadas en la literatura existente— pueden modelarse y resolverse eficientemente pese a ser NP-difíciles.

## Metodología
- **Diseño:** formalización matemática + prueba de complejidad + algoritmo de solución.
- **Datos / muestra:** datos reales de la empresa cárnica ("solved for a meat processing company", con resultados sobre "real data").
- **Técnicas:** programación lineal entera (ILP); enfoque iterativo simple que permite resolver instancias reales incluso con un solver de código abierto.
- **Métricas:** no reportadas en el abstract (requeriría el cuerpo del paper, no accedido en full-text por limitaciones de extracción del PDF).

## Resultados principales
- Prueban que la restricción de cantidad mínima de pedido es NP-difícil.
- Prueban que la restricción de porcentaje mínimo en alternativas de procesamiento es NP-difícil.
- El enfoque iterativo basado en ILP resuelve instancias de tamaño real.

## Conclusiones
Un enfoque de programación entera simple e iterativo es viable para un problema de producción cárnica real con restricciones no triviales, sin requerir un solver comercial.

## Limitaciones
Solo se leyó el abstract completo (el PDF venía comprimido y no se pudo decodificar el cuerpo). No se confirmó el número exacto de productos/materias primas/operaciones del caso real, ni si el objetivo es de un solo componente o multi-objetivo ponderado.

## Relevancia / brecha para el estado del arte
Es el precedente más cercano y ya estaba citado en `form_w2.estado_del_arte_investigacion` como "Vlk et al. 2025"; esta ficha lo verifica formalmente con lectura del abstract completo desde la fuente primaria (antes solo constaba como referencia sin ficha KB ni verificación directa). Confirma que MILP/ILP en plantas cárnicas reales es un área activa — relevante para argumentar que el Objetivo 3 (MPS) usa una técnica de la familia correcta, aunque el objetivo real de Agrosuper (MILP vía Gurobi, función objetivo de 8 componentes ponderados para Hamburguesa/Empanizado) tiene una función objetivo más compleja que este paper.

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
