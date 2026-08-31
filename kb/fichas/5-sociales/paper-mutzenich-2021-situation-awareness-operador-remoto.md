---
id: paper-mutzenich-2021-situation-awareness-operador-remoto
titulo: "Updating our understanding of situation awareness in relation to remote operators of autonomous vehicles (Mutzenich, Durant, Helman & Dalton 2021)"
tipo: revision
tema: Factores humanos y conciencia situacional (situation awareness) del operador remoto de vehículos
area_oecd: "5 Ciencias Sociales (5.1 Psicología)"
topicos: [factores-humanos-operador-remoto, teleoperacion-supervision-remota, latencia-teleoperacion]
anio: 2021
autores: [Clare Mutzenich, Szonya Durant, Shaun Helman, Polly Dalton]
referencia: https://pmc.ncbi.nlm.nih.gov/articles/PMC7892648/ (Cognitive Research: Principles and Implications 6:9, DOI 10.1186/s41235-021-00271-8)
motor: WebSearch (Springer redirigió a login) + PMC full-text
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "1-3 (revisión conceptual y agenda de investigación)"
metricas_clave: ["propone niveles SAE ampliados 3b/4b/5b para intervención remota", "cita el umbral de ~50 ms a partir del cual la imagen del operador ya está desactualizada", "cobertura 4G rural del Reino Unido citada en 9%"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Pregunta / objetivo de investigación
¿Siguen siendo válidos los marcos clásicos de conciencia situacional (situation awareness, SA) cuando el conductor no está físicamente en el vehículo? ¿Qué riesgos específicos introduce la operación remota y cómo mitigarlos?

## Hipótesis
Los marcos de SA existentes no reconocen los desafíos propios del operador remoto; la SA remota se construye desde cero, mediada por pantallas, y eso introduce riesgos no contemplados por las taxonomías de automatización vigentes.

## Metodología
- **Diseño:** revisión crítica y conceptual (no experimental).
- **Datos / muestra:** literatura de factores humanos, ergonomía cognitiva y automatización vehicular; casos de operación remota reportados.
- **Técnicas:** análisis de los modelos de SA frente al caso remoto; propuesta de extensión taxonómica.

## Resultados principales
- El operador remoto sufre **out-of-the-loop (OOTL)**: no tiene exposición previa al contexto y debe construir el modelo mental desde cero — "An RO cannot begin to take control until they have built up adequate SA".
- **Pérdida de encarnación (embodiment)**: sin realimentación vestibular ni propioceptiva se distorsiona la percepción de velocidad y riesgo; los operadores describen la experiencia como conducir "sordo" o "como si fuera un juego".
- **Latencia**: el artículo recoge que retardos superiores a ~50 ms ya implican que la imagen que ve el operador está desactualizada para la interacción útil; y que la cobertura móvil rural es una restricción real (9% de cobertura 4G rural en el Reino Unido citado).
- **Campo visual reducido**: la visión mediada por cámaras pierde paralaje de movimiento y profundidad.
- Propone niveles SAE ampliados (3b, 4b, 5b) para reconocer explícitamente la intervención remota, y mitigaciones: VR/AR para recuperar perspectiva egocéntrica, mapas precompilados, control de cámaras, realimentación audiovisual espacial y vistas sintéticas.

## Conclusiones
La operación remota no es "conducir con pantallas": es una tarea cognitivamente distinta cuyos riesgos de SA no están cubiertos por los marcos ni por las taxonomías actuales. Se requiere investigación empírica y marcos regulatorios de entrenamiento y certificación de operadores remotos.

## Limitaciones
- Revisión conceptual: no aporta datos experimentales propios.
- Contexto de vías públicas y vehículos livianos; no analiza faena industrial cerrada ni vehículos pesados.
- Datos de cobertura de red referidos al Reino Unido en 2021.

## Relevancia / brecha para el estado del arte
Sostiene que el desempeño y la seguridad de una operación telecomandada dependen tanto del **diseño de la estación y del entrenamiento del operador** como del enlace. Para un proyecto donde el operador estará a cientos de kilómetros, el desafío de conciencia situacional y de traspaso de control es una brecha vigente y medible (tiempo para construir SA, errores, carga de trabajo). Se conecta con [[paper-li-2023-conductor-remoto-5g-camion-40t]] (evidencia empírica con conductores de camión pesado) y con [[norma-bsi-flex-1887-factores-humanos-operacion-remota]].

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
