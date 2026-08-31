---
id: paper-bijelic-2020-seeing-through-fog
titulo: "Seeing Through Fog Without Seeing Fog: Deep Multimodal Sensor Fusion in Unseen Adverse Weather (Bijelic et al., CVPR 2020)"
tipo: paper
tema: Fusión multimodal (cámara, LiDAR, radar, cámara gated) bajo clima adverso; el dataset STF y la falla asimétrica de los sensores en niebla
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [percepcion-lidar-clima, percepcion-obstaculos-outdoor, seguridad-funcional-av]
anio: 2020
autores: [Mario Bijelic, Tobias Gruber, Fahim Mannan, Florian Kraus, Werner Ritter, Klaus Dietmayer, Felix Heide]
referencia: https://arxiv.org/abs/1902.08913 (CVPR 2020)
motor: WebSearch → arXiv (página de abstract; no se abrió el PDF completo)
profundidad_lectura: abstract
estado_evidencia: parcial
trl_relevante: "3-4 (investigación; dataset y arquitectura de fusión)"
metricas_clave: ["dataset Seeing Through Fog (STF): más de 10.000 km de conducción en el norte de Europa", "100.000 etiquetas con cámara, LiDAR, radar y cámara gated NIR"]
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
¿Cómo fusionar sensores heterogéneos para detección de objetos cuando el clima adverso distorsiona cada flujo sensorial de manera distinta, y sin disponer de grandes volúmenes de datos etiquetados en esas condiciones raras?

## Hipótesis
Los esquemas de fusión existentes asumen redundancia entre sensores, supuesto válido con buen tiempo y falso con clima adverso: la fusión debe adaptarse a la entropía (confiabilidad) medida de cada flujo.

## Metodología
- **Diseño:** construcción de dataset multimodal + arquitectura de fusión.
- **Datos / muestra:** dataset STF, más de 10.000 km de conducción en el norte de Europa, ~100.000 etiquetas; sensores: cámara RGB, LiDAR, radar y cámara gated NIR. Incluye adquisiciones en cámara de niebla controlada además de conducción real.
- **Técnicas:** modelo de fusión de una etapa ("single-shot") que pondera adaptativamente las características según la entropía de la medición, entrenado sin grandes volúmenes de datos etiquetados en clima adverso.

## Resultados principales
- Cita textual: *"Existing methods exploit redundant information in good environmental conditions, they fail in adverse weather where the sensory streams can be asymmetrically distorted."*
- Cita textual: *"These rare 'edge-case' scenarios are not represented in available datasets, and existing fusion architectures are not designed to handle them."*
- (Las cifras de mejora en detección bajo niebla densa no fueron verificadas en esta lectura; el PDF completo no se abrió.)

## Conclusiones
La niebla no degrada por igual a todos los sensores: distorsiona asimétricamente los flujos, de modo que la redundancia sensorial nominal no se traduce en robustez real. Los datasets estándar no representan estas condiciones.

## Limitaciones
- Lectura a nivel de abstract: no se verificaron cifras de desempeño.
- Escenario de carretera europea (nieve/niebla), no patio industrial con polvo.
- El trabajo es de investigación, no de producto certificado.

## Relevancia / brecha para el estado del arte
Sustenta el argumento central para la neblina de Lampa: **"tiene cámaras y LiDAR" no equivale a "es robusto a niebla"**, porque bajo niebla la degradación es asimétrica y las arquitecturas de fusión comerciales, entrenadas sobre datos de buen tiempo, no están diseñadas para esa condición. También justifica por qué la respuesta del proveedor sobre el comportamiento en neblina es información necesaria y no un detalle de especificación.

> Relaciones: complementa a [[paper-kim-2023-degradacion-lidar-lluvia-niebla]] (medición física) y a [[paper-bhatt-2024-watonobus-clima-adverso]] (validación en campo).
