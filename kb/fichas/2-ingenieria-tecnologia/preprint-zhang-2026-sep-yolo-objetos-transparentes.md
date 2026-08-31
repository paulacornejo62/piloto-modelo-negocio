---
id: preprint-zhang-2026-sep-yolo-objetos-transparentes
titulo: "SEP-YOLO: Fourier-Domain Feature Representation for Transparent Object Instance Segmentation (Zhang, Yan & Huang, 2026)"
tipo: preprint
tema: YOLO estándar falla con objetos transparentes/semitransparentes; arquitectura nueva en dominio de frecuencia (Fourier)
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [limitaciones-yolo-oclusion-transparencia]
anio: 2026
autores: [Zhang, Yan, Huang]
referencia: arXiv:2603.02648
motor: WebFetch (arXiv)
profundidad_lectura: abstract
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: []
fecha_registro: 2026-08-21
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Desarrollar una arquitectura de segmentación de instancias que resuelva el problema de detección de objetos transparentes o semitransparentes, donde los detectores YOLO estándar fallan genuinamente.

## Hipótesis
Que una representación de características en el **dominio de frecuencia (Fourier)**, en vez del dominio espacial estándar, puede capturar mejor los bordes difusos y el bajo contraste característicos de los objetos transparentes/semitransparentes.

## Metodología
- **Diseño:** desarrollo de una nueva arquitectura de deep learning.
- **Datos / muestra:** objetos transparentes/semitransparentes (no se detalla el dominio específico en el abstract accedido).
- **Técnicas:** representación de características en el dominio de frecuencia (Fourier), integrada a una arquitectura tipo YOLO (SEP-YOLO).
- **Métricas:** no confirmables en detalle a nivel de abstract.

## Resultados principales
- Los autores confirman que YOLO estándar **falla genuinamente** con objetos transparentes/semitransparentes: bordes difusos y bajo contraste generan detecciones deficientes.
- Proponen SEP-YOLO, una arquitectura nueva en el dominio de frecuencia, como solución — publicada en 2026, lo que confirma que es un **problema activo, no resuelto** con herramientas estándar.

## Conclusiones
La detección de objetos transparentes/semitransparentes es un problema no resuelto por arquitecturas YOLO convencionales, y requiere representaciones especializadas (dominio de frecuencia) — activo en la frontera de investigación a 2026.

## Limitaciones
Es un **preprint muy reciente de arXiv (2026)**, no ha pasado por revisión por pares confirmada — `profundidad_lectura: abstract`. No se confirma si el dominio de aplicación de los autores incluye piezas cárnicas semicongeladas específicamente, o si es un dominio genérico (vidrio, plástico, etc.) — aplicabilidad directa al caso de Agrosuper no verificada, solo el patrón de falla de YOLO es directamente relevante.

## Relevancia / brecha para el estado del arte
**Relevante para la incertidumbre técnica del Objetivo 4** (pechugas semicongeladas translúcidas): confirma con evidencia reciente que YOLO estándar sin módulos adicionales sufre degradación real ante objetos transparentes/translúcidos — respalda la incertidumbre técnico-científica declarada para ese objetivo, no la resuelve.

Relacionada con [[paper-he-2024-yolo-oclusion-vehiculos]] — ambos papers calzan con el problema descrito por el equipo técnico de Agrosuper (piezas semicongeladas translúcidas y pegadas) y confirman con evidencia cuantitativa que YOLO estándar sin módulos adicionales sufre degradación real en estos casos.

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
