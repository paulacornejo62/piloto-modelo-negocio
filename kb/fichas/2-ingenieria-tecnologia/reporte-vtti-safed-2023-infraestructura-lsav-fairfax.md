---
id: reporte-vtti-safed-2023-infraestructura-lsav-fairfax
titulo: "Evaluation Tools for Low-Speed Automated Vehicle (LSAV) Transit Readiness of the Area — Informe VTTI-05-113 (Safe-D UTC / VTTI), despliegue EZ10 Gen3 en Fairfax County"
tipo: reporte
tema: Evaluación independiente instrumentada de 7 meses del EZ10 Gen3 en vía pública — ODD del fabricante citado del User Guide + efecto de la infraestructura (demarcación, áreas abiertas) sobre las intervenciones
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [vehiculo-autonomo-shuttle, recinto-privado-odd, disengagement-kpi-piloto, percepcion-lidar-clima, entorno-semi-estructurado, localizacion-gnss-rtk]
anio: 2022  # QA: fecha del reporte 22/11/2022 (Final Research Report 01/01/2021-12/31/2022); datos de campo oct-2020 a may-2021
autores: [Yubin Hong, Sheila G. Klauer, Mike Mollenhauer, Jean Paul Talledo Vilela, Noah Goodall, Michael D. Fontaine]
referencia: "VTTI-05-113, Safe-D National UTC / Virginia Tech Transportation Institute, 22-11-2022 — https://rosap.ntl.bts.gov/view/dot/67065 (PDF: /view/dot/67065/dot_67065_DS1.pdf)"
motor: WebSearch → PDF descargado desde safed.vtti.vt.edu (espejo rosap.ntl.bts.gov), extracción de texto local
profundidad_lectura: full-text
estado_evidencia: verificado
verificacion_qa: observado  # QA 2026-08-03: las tres citas textuales se confirmaron en el PDF; se corrigieron título, año y autores de la referencia
trl_relevante: 6-7
metricas_clave: ["ODD EZ10 Gen3 (User Guide, cita de 2ª mano): lluvia hasta >0.4 in/h, nieve/hielo hasta 0.4 in, viento hasta 31 mph, 'dust, fog, or vapor up to 3.2 ft visibility', pendiente 15% limitada, carga 1.1 t", "velocidad real 4-8 mph en intersecciones/áreas abiertas vs 14 mph planificadas", "conclusión: 'not yet operating at SAE Level 4 capability on routes with moderate complexity'"]
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
Evaluar, con instrumentación independiente y desde la perspectiva de la infraestructura, el desempeño de un shuttle automatizado de baja velocidad (EasyMile EZ10 Gen3, servicio Relay de Fairfax County, Virginia) en operación real de 7 meses, identificando qué elementos del entorno degradan la operación autónoma.

## Hipótesis
Los atributos de la infraestructura (demarcación, geometría, estructura lateral del entorno) condicionan de forma medible el desempeño y la confianza operacional de un shuttle L4 comercial.

## Metodología
- **Diseño:** observación instrumentada de la operación comercial real (vía pública pavimentada, complejidad moderada: semáforos, demarcación parcial) durante 7 meses; análisis de intervenciones del operador (circumventions, soft stops) por segmento de ruta.
- **Fuente del ODD:** cita textual del EZ10 Gen3 User Guide (documento no público) dentro del reporte.

## Resultados principales
- **ODD declarado por el fabricante** (cita de segunda mano del User Guide): "the EZ10 can be safely operated in the following conditions... Up to medium-high snowfall... medium (0.4 in/h) or heavy rain... Ice or snow on the road (up to 0.4 in)... Humidity between 5% and 95%... Wind up to 31 mph... **Dust, fog, or vapor up to 3.2 ft visibility**... Temperature 14–113 °F... Slope up to 15% for a limited time... Payload up to 1.1 US ton". **No menciona requisito ni límite de tipo de superficie de rodado** (no aparece pavement/asphalt/gravel/unpaved): ausencia de evidencia de capacidad sobre superficie suelta, no evidencia de capacidad.
- **Efecto de la infraestructura:** "Residential areas, open areas, curvy roads, and segments without clear lane markings saw more circumventions and soft stops... human operators did not trust the ADS under these scenarios." La falta de estructura visual (demarcación, bordes) concentra las intervenciones humanas — sobre pavimento.
- **Madurez real vs claim:** "the results showed that the LSAV did not reach its planned operational speed of 14 mph... average speed was between 4 to 8 mph... These results suggest that the EZ10 Gen 3 vehicle is not yet operating at SAE International Level 4 capability on routes with moderate complexity."
- **Superficie como requisito del sitio (aporte del QA):** aunque el ODD del fabricante no la menciona, el propio reporte sí la incluye entre las *Desirable Route Characteristics*: *"Well-maintained pavements and clear pavement markings. LSAVs perform best on roads with clear pavement markings. Well maintained pavements along the route would also be ideal for LSAVs."* Y en los datos: *"route sections with no clear marking on the pavement showed higher rates of soft stops and circumventions"*. Es decir, el requisito de superficie/demarcación aparece como recomendación del evaluador independiente, no como límite declarado por el fabricante.

## Conclusiones
El shuttle comercial más desplegado del mundo, evaluado independientemente sobre pavimento y complejidad moderada, no alcanza L4 y se degrada justo donde el entorno pierde estructura visual. Para un recinto de maicillo sin demarcación (caso CLK), no existe evidencia pública de capacidad — y el ODD del fabricante acota explícitamente polvo y niebla.

## Limitaciones
- El ODD del EZ10 es cita de segunda mano (el User Guide no es público); el ítem "3.2 ft visibility" es ambiguo en su redacción — no sobre-interpretar.
- Contexto de vía pública urbana de EE.UU.; sin datos de superficie no pavimentada.
- **Nota QA (2026-08-03):** verificado contra el PDF completo (VTTI-05-113). Las tres citas —el listado del ODD con "Dust, fog, or vapor up to 3.2 ft visibility", el hallazgo 4 sobre áreas residenciales/abiertas/sin demarcación y la conclusión sobre SAE L4— son literales. Se corrigieron en el frontmatter el **título** real del reporte, el **año** (22/11/2022, no 2023) y los **autores** (seis personas, no solo las instituciones). El período de datos es 21/10/2020–18/05/2021 (siete meses), no 2023. El `id` del archivo conserva "2023" para no romper referencias del índice.
