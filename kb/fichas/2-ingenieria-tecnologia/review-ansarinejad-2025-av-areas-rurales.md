---
id: review-ansarinejad-2025-av-areas-rurales
titulo: "Autonomous Vehicles in Rural Areas: A Review of Challenges, Opportunities, and Solutions (Ansarinejad et al., 2025)"
tipo: revision
tema: Revisión sistemática de despliegues de vehículos autónomos en zonas rurales, con inventario de desafíos por categoría (tecnológico, ambiental, infraestructura, política)
area_oecd: "2 Ingeniería y Tecnología (2.1 Ingeniería civil)"
topicos: [superficie-no-pavimentada, recinto-privado-odd, percepcion-obstaculos-outdoor, disengagement-kpi-piloto, localizacion-gnss-rtk]
anio: 2025
autores: [Melika Ansarinejad, Kian Ansarinejad, Pan Lu, Ying Huang, Denver Tolliver]
referencia: https://doi.org/10.3390/app15084195
motor: WebSearch → MDPI (mirror mdpi-res.com, PDF full-text)
profundidad_lectura: full-text
estado_evidencia: verificado
verificacion_qa: observado  # QA 2026-08-03: fuente abierta y contrastada; se corrigió la atribución de "gravel roads" al listado de cuatro problemas de Drive MN
trl_relevante: "-"
metricas_clave: ["revisión de estudios 2015-2024; distribución metodológica (Figura 4): 26% pruebas de campo, 29% simulación, 23% entrevistas, 3% conceptual, 19% otros", "Drive MN: 4 problemas mayores sobre más de 1.087 millas de caminos rurales (asfalto y hormigón) — visibilidad de carril deficiente, rampas y carriles de viraje, zonas de construcción y marcas de bajo contraste; los 'gravel roads' NO son uno de esos cuatro (aparecen en la frase siguiente, con cita [70])", "Tabla 3 lista 'GPS and localization failures' y 'Unreliable responses to unmarked roads' como desafíos tecnológicos vigentes"]
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
¿Cuál es el estado de la evidencia sobre el despliegue de vehículos autónomos en zonas rurales (caminos sin marcas, no pavimentados, con clima adverso) y qué desafíos siguen abiertos?

## Hipótesis
El grueso de la investigación y de los productos comerciales de conducción autónoma está calibrado para entorno urbano estructurado; los entornos rurales imponen condiciones distintas que la tecnología actual no cubre.

## Metodología
- **Diseño:** revisión sistemática en tres fases (recuperación bibliográfica con la librería `scholarly` sobre Google Scholar, búsqueda extendida a fuentes gubernamentales/industriales, análisis temático asistido por LLM con revisión manual del 90% de las referencias).
- **Datos / muestra:** estudios 2015-2024 sobre despliegue de AV en zonas rurales; ocho proyectos de campo tabulados (DriveOhio, ADS for Rural America, goMARTI, Drive MN, CASSI, TEDDY, entre otros).
- **Técnicas:** clasificación por metodología (campo 26%, simulación 29%, entrevistas 23%, conceptual 3%) y por tema.

## Resultados principales
- **Tabla 3 (desafíos vigentes)** clasifica explícitamente como problemas *tecnológicos*: "Sensor misdetections", "Unreliable responses to unmarked roads", "GPS and localization failures", "Object detection failures", "Frequent disengagements of automation systems"; como *ambientales*: "Unpaved roads, steep gradients", "Extreme weather conditions", "Sharp curves with limited visibility", "Dynamic lighting transitions (shade to sunlight)"; como *de infraestructura*: "Faded or low-contrast markings", "Need for frequent HD mapping updates".
- Cita textual: *"Dynamic lanes, faded edge stripes, unclear or inconsistent lane markings, and gravel roads often lead to detection errors and path deviations. Frequent human overrides further stress the need for robust and reliable systems."*
- Cita textual: *"In work zones, visual disturbances, including faded or conflicting lane markings and crack seal lines, can confuse sensors, causing misdetections."*
- El proyecto Drive MN (Minnesota DOT) identificó cuatro problemas mayores sobre más de 1.087 millas de caminos rurales: visibilidad de carril deficiente, rampas y carriles de viraje, zonas de construcción y marcas de bajo contraste; ensayos bajo niebla y deslumbramiento.
- Axelrod (2019), citado en la revisión, examina el despliegue en **unpaved roads** con mal clima y distancias de visión limitadas, y propone clasificar los caminos por su compatibilidad con AV ("self-driving eligible", "depot-to-depot", "last-mile"), señalando la brecha entre la inversión en tecnología a bordo y la insuficiente adecuación de la infraestructura.
- Recomendación repetida de infraestructura: superficies mejoradas con marcas de alto contraste, retrorreflectantes y visibles en mojado; mapas HD actualizados con frecuencia; GPS localizado con estaciones base RTK.

## Conclusiones
El despliegue en entornos rurales/no pavimentados sigue en fase demostrativa. Los desafíos no son de integración comercial sino técnicos y de infraestructura: percepción sin marcas, localización, clima y superficie. La revisión concluye que se requieren "tailored AV solutions" para estos contextos.

## Limitaciones
- Es revisión: no aporta mediciones propias.
- Sesgo geográfico fuerte hacia Estados Unidos y Europa; ningún caso de Chile ni de América Latina.
- El análisis temático se apoya en LLM sobre abstracts (con revisión manual parcial declarada del 90%).
- **Nota QA (2026-08-03):** las rutas de Drive MN se describen en la fuente como *"two-, four-, and six-lane asphalt and concrete roads"* — es decir, pavimentadas. Los "gravel roads" aparecen en la revisión como causa de errores de detección y desviaciones de trayectoria citando la referencia [70] (ADS for Rural America), **no** como uno de los cuatro problemas mayores de Drive MN. Al usar este hallazgo, no atribuir la evidencia de grava al proyecto Drive MN.

## Relevancia / brecha para el estado del arte
Sostiene, con literatura revisada, que la combinación exacta del caso Kaufmann —**superficie no pavimentada + demarcación degradada o ausente + clima adverso + tráfico mixto**— está catalogada en la literatura como conjunto de desafíos abiertos, no como capacidad de producto. También aporta la contraparte útil: la vía de mitigación conocida pasa por *adecuar el sitio* (superficie, marcas retrorreflectantes, RTK, mapas HD), lo que es precisamente el trabajo de habilitación que la postulación debe describir y cuya eficacia en maicillo compactado no está demostrada.

> Relaciones: complementa a [[review-mantouka-2026-odd-desafios-operacionales]] y a [[paper-mason-2022-shuttle-caminos-grava-rural]].
