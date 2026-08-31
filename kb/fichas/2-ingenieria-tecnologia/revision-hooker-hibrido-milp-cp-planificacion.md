---
id: revision-hooker-hibrido-milp-cp-planificacion
titulo: "Métodos híbridos MILP/Constraint Programming para planificación y scheduling (línea Hooker et al.) — incluye caso aplicado de planta de empaque (MDPI Applied Sciences 13(10):6003, 2023)"
tipo: revision
tema: Combinación de programación entera mixta (MILP) y programación por restricciones (CP) para problemas de planificación+scheduling intratables por un solo método
area_oecd: "2 Ingeniería y Tecnología (2.11 Otras ingenierías y tecnologías)"
topicos: [milp-programacion-produccion-carnica, hibrido-milp-cp-scheduling]
anio: 2023
autores: []
referencia: "https://www.mdpi.com/2076-3417/13/10/6003 ; línea de trabajo fundacional: John Hooker (CMU), 'A Hybrid Method for Planning and Scheduling' — https://johnhooker.tepper.cmu.edu/cp04.pdf"
motor: WebSearch (MDPI 403 al fetch directo; PDF de Hooker no decodificable)
profundidad_lectura: metadata
estado_evidencia: parcial
trl_relevante: -
metricas_clave: []
fecha_registro: 2026-08-18
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Cómo combinar MILP y Constraint Programming (CP) — asignando tareas a instalaciones/recursos vía MILP y secuenciándolas vía CP, unidos por descomposición de Benders lógica (línea Hooker) — para resolver problemas de planificación+scheduling que son intratables usando un solo método. El caso aplicado (MDPI 2023) lo hace para una planta de empaque real, modelando un flow shop híbrido y flexible con restricciones de precedencia, máquinas paralelas y setups dependientes de la secuencia.

## Hipótesis
Que ni MILP puro ni CP puro resuelven eficientemente instancias grandes de programación de producción con estas restricciones combinadas, pero un método híbrido que reparte el problema entre ambos paradigmas sí puede — con ganancias de varios órdenes de magnitud en tiempo de cómputo según la línea de Hooker.

## Metodología
- **Diseño:** propuesta de arquitectura híbrida (Hooker) + caso aplicado real (MDPI 2023, planta de empaque).
- **Datos / muestra:** no confirmados a este nivel de acceso (ambas fuentes bloquearon el fetch directo — MDPI 403, PDF de Hooker no decodificable).
- **Técnicas:** MILP para asignación, CP para secuenciación, acoplados por descomposición de Benders basada en lógica (Hooker); en el caso aplicado, además se compara contra una heurística dedicada propia.
- **Métricas:** no confirmadas a este nivel de acceso.

## Resultados principales
Según el agregado de búsqueda (no verificado contra fuente primaria): los métodos híbridos MILP/CP explotan las fortalezas complementarias de ambos para resolver problemas que ninguno de los dos resuelve por separado, con mejoras de varios órdenes de magnitud en tiempo de cómputo frente al estado del arte de MILP o CP puros.

## Conclusiones
No confirmables desde fuente primaria en este pase.

## Limitaciones
**No se accedió a texto completo de ninguna de las dos fuentes** (MDPI 403; PDF de Hooker con contenido no decodificable por el extractor). Toda la caracterización viene de snippets agregados por 2 búsquedas independientes que citaron consistentemente el mismo patrón metodológico (asignación MILP + secuenciación CP + acoplamiento tipo Benders). Autores del caso MDPI no identificados. `estado_evidencia: parcial`.

## Relevancia / brecha para el estado del arte
Confirma que la hibridación MILP+CP (equivalente en espíritu a lo que el plan de Agrosuper llama "MILP + CPSAT") **es un patrón de investigación activo y especializado, no una receta trivial ni de uso rutinario como el MILP puro** — se usa específicamente cuando un solo método no basta. Esto es relevante para el Objetivo 3 (MPS): la extensión a Cecinas/Jamones/Pechugas/Masivos (Carta_Gantt_MPS.xlsx, actividades 2.1.1-2.1.4: "MILP + CPSAT Salchicha", "MILP" y "CPSAT" por separado para Jamones/Pechugas/Masivos, más un paso explícito de "Integración y unión de modelos MILP + CPSAT") es cualitativamente distinta de la parte ya productiva (Hamburguesa/Empanizado, MILP puro, en QA). No decide por sí sola si el caso de Agrosuper es I+D defendible — falta el dato concreto de POR QUÉ el MILP puro no basta para esas líneas (qué restricción específica rompe el modelo) — pero sostiene que la afirmación "MPS es solo ingeniería estándar" no aplica automáticamente a esta parte del alcance.

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
