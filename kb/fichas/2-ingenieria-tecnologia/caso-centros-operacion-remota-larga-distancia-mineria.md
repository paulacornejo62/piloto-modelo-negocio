---
id: caso-centros-operacion-remota-larga-distancia-mineria
titulo: "Centros de operación remota minera a larga distancia: Rio Tinto (Perth ↔ Pilbara, 1.500 km), BHP (Santiago ↔ Escondida/Spence) y Antofagasta Minerals (GIO Antofagasta)"
tipo: caso
tema: Evidencia de que la operación minera remota a cientos/miles de kilómetros ya está en producción, y qué se opera realmente desde esa distancia
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [centro-operacion-remota-larga-distancia, mineria-remota-automatizacion, teleoperacion-supervision-remota]
anio: 2024
autores: [Rio Tinto; BHP (vía prensa especializada chilena); Antofagasta Minerals]
referencia: "https://www.riotinto.com/en/operations/anz/western-australia · https://www.portalminero.com/wp/bhp-pone-en-marcha-nuevo-centro-de-operacion-remoto-pionero-en-sudamerica/ · https://www.aminerals.cl/centro-de-informacion/2022/04/27/antofagasta-minerals-inaugura-su-nuevo-proyecto-en-la-capital-regional-gesti%C3%B3n-integrada-de-operaciones"
motor: WebSearch + WebFetch (sitio corporativo Rio Tinto; Portal Minero)
profundidad_lectura: full-text
estado_evidencia: parcial
trl_relevante: 9
metricas_clave: ["Rio Tinto: operación desde Perth a 1.500 km del Pilbara", "Rio Tinto: ~90 % de la flota de camiones de extracción es autónoma; 40 perforadoras en 7 faenas", "BHP: centro en Santiago, 3.400 m², US$48,3 millones, 5,4 TB diarios, enlace submarino Antofagasta–Santiago", "Antofagasta Minerals: GIO en la ciudad de Antofagasta (Centinela está ~1.350 km al norte de Santiago), 137 personas, ~US$66 millones"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Qué documenta

**Rio Tinto — Operations Centre, Perth** (sitio corporativo, cita textual):
> "Our state-of-the-art Operations Centre in Perth allows the autonomous trucks, trains, plants and drills across our mines, ports and rail systems to be operated from a single location 1,500 kilometres from the Pilbara."
> "Approximately 90% of our haul truck fleet across our Pilbara sites is also autonomous." · flota de "40 production drills across 7 sites" con consolas remotas en Perth.

**BHP — Copper Advanced Services, Santiago** (Portal Minero, citas textuales):
> "permitirá dar servicios para la operación de forma remota y con plena autonomía a las faenas"
> "permite operar maquinarias pesadas de manera remota en entornos complejos"
> "a miles de kilómetros de distancia de las faenas, en sus distintas etapas y procesos unitarios"
> "considera un link submarino desde Antofagasta a Santiago, un nuevo data center"
> "El nuevo centro de operaciones remotas manejará diariamente 5.4 terabyte de información" · "con una inversión total de US$ 48.3 millones"

**Antofagasta Minerals — Gestión Integrada de Operaciones (GIO), Antofagasta**: primer centro de operación remota de la industria ubicado en la ciudad de Antofagasta; 137 personas, ~US$66 millones (fuente corporativa vía prensa).

## Matices críticos (lo que las fuentes NO afirman)

- Ninguna fuente revisada declara **latencia extremo a extremo, disponibilidad del enlace ni arquitectura de redundancia**.
- Rio Tinto describe operación de equipos **autónomos** supervisados y perforadoras con consola remota; **no** afirma control teleoperado continuo de un camión (lazo humano cerrado en tiempo real) a 1.500 km.
- BHP habla de "operar maquinarias pesadas de manera remota" sin especificar qué equipos ni el modo de control.
- Un demo documentado de teleoperación intercity existe fuera de estas fuentes: Caterpillar operó un bulldozer D11T cerca de Tucson (AZ) desde una sala en Las Vegas (NV) durante MINExpo — reportado por prensa técnica, no verificado de primera fuente en esta revisión (**no verificado**).

## Relevancia / brecha para el estado del arte

- **Resuelto**: el *centro de operación remota* a 1.000–1.500 km es práctica industrial establecida, tanto en Australia como en Chile, y hay infraestructura de transporte dedicada (cable submarino Antofagasta–Santiago del caso BHP).
- **No demostrado públicamente**: teleoperación de **control directo** de un camión de faena desde esa distancia con enlace disponible 100 % del tiempo. La distinción entre supervisión/despacho de flota autónoma y control remoto continuo es exactamente donde vive la incertidumbre técnica.
- Complementa a [[paper-neumeier-2019-feasibility-tod-redes-moviles]]: a mayor distancia el problema medido no es la latencia media sino su **variabilidad**.

> Relaciones con otras fichas → `../../indice.json`.
