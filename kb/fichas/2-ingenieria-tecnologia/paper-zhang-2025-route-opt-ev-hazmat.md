---
id: paper-zhang-2025-route-opt-ev-hazmat
titulo: "Multi-objective route optimization for electric vehicle hazardous materials transportation in uncertain environments (Zhang et al. 2025)"
tipo: paper
tema: Optimización de rutas para transporte de mercancías peligrosas con vehículos eléctricos (riesgo/costo/servicio)
area_oecd: "2 Ingeniería y Tecnología (2.11 Otras ingenierías y tecnologías)"
topicos: [electromovilidad-carga-peligrosa, electromovilidad-vehiculo-comercial]
anio: 2025
autores: [Qian Zhang, Zejian Zhang, Chao Ma]
referencia: https://doi.org/10.1038/s41598-025-32134-3
motor: Europe PMC / PMC (PMC12748956)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 3
metricas_clave: ["riesgo -14.40%", "costo -12.81%", "riesgo -19% al subir capacidad 1.5→3.5 t"]
fecha_registro: 2026-07-14
proyectos:
  - lipigas
---

## Pregunta / objetivo de investigación
Optimizar rutas de transporte de materiales peligrosos con VE minimizando riesgo, costo y maximizando satisfacción del cliente bajo incertidumbre poblacional.

## Hipótesis
La transición a VE para mercancías peligrosas es viable con planificación rigurosa; el volumen de carga y la capacidad del vehículo modulan el riesgo.

## Metodología
- **Diseño:** programación lineal entera multiobjetivo con incertidumbre (densidad poblacional como intervalos).
- **Técnicas:** algoritmo H-NSGA-II (inicialización híbrida 25% greedy + 75% aleatorio).
- **Métricas:** riesgo (probabilidad×población×volumen de carga), costo, satisfacción, hipervolumen.

## Resultados principales
- Frente a NSGA-II estándar: riesgo -14.40%, costo -12.81%, satisfacción +13.53%; hipervolumen 0.752 vs 0.685.
- Análisis de sensibilidad: subir capacidad de 1.5 t a 3.5 t reduce el riesgo total 19% (máximo efecto entre 1.5–2 t).
- "different vehicle cargo volumes will lead to different consequences in case of accident".

## Conclusiones
La electrificación del transporte de mercancías peligrosas es técnicamente factible con planificación de rutas que integra riesgo poblacional dinámico.

## Limitaciones
Estudio de modelado (foco en materiales Categoría 9, p. ej. baterías); no ensaya el escenario físico batería+carga inflamable; TRL bajo.

## Relevancia / brecha para el estado del arte
Es de la escasa literatura que trata explícitamente VE + mercancías peligrosas. Aporta al eje logístico/rutas de Lipigas (última milla urbana) y muestra que el riesgo se gestiona con planificación. No resuelve la coexistencia física batería-GLP: esa brecha refuerza la novedad del piloto.

> Relaciones con otras fichas → `../../indice.json`.
