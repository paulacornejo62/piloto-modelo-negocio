---
id: review-iclodean-2020-autonomous-shuttle-bus
titulo: "Autonomous Shuttle Bus for Public Transportation: A Review (Iclodean, Cordoș & Varga, 2020)"
tipo: revision
tema: Revisión del estado del arte de shuttles autónomos de pasajeros — arquitecturas, sensores, despliegues mundiales y marco legal
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [vehiculo-autonomo-shuttle, localizacion-gnss-rtk, recinto-privado-odd]
anio: 2020
autores: [Calin Iclodean, Nicolae Cordoș, Bogdan Varga]
referencia: https://doi.org/10.3390/en13112917
motor: WebSearch + Semantic Scholar (metadatos) + mirror PDF de MDPI (full-text)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 6-7
metricas_clave: ["velocidad de operación típica hasta 25 km/h", "capacidad máxima 15 personas", "58 despliegues tabulados (Navya Arma, EasyMile EZ10, Baidu Apollo, Local Motors Olli)", "rutas de 0.3 a 26 km", "GNSS/RTK con refresco de 1-20 Hz"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
Revisar el estado de implementación de vehículos autónomos en la forma de shuttle bus de transporte público: evolución científica, marco legal comparado, soluciones tecnológicas de los principales fabricantes (componente por componente), algoritmo de control y factores sociales de la introducción masiva.

## Hipótesis
Supuesto de partida: pese a la baja capacidad de transporte (máximo 15 personas), el uso de estas unidades en grandes aglomeraciones urbanas es beneficioso para la sociedad, y su aceptación depende de la eficiencia en el servicio diario.

## Metodología
- **Diseño:** revisión narrativa exhaustiva (45 páginas) con tabulación sistemática de despliegues.
- **Datos / muestra:** catálogo de despliegues por marca (Navya Arma, EasyMile EZ10, Baidu Apollo, Local Motors Olli) con ubicación, operador, número de vehículos, fecha de lanzamiento, largo de ruta, tarifa y **tipo de entorno** (área peatonal / vía pública / propiedad privada / propiedad estatal).
- **Técnicas:** análisis comparativo de powertrain, sensores (LiDAR, cámara, radar, GNSS/RTK, IMU), arquitectura de control y legislación por país.
- **Métricas:** velocidad de operación, largo de ruta, tipo de entorno, precisión de localización.

## Resultados principales
- **El nicho es el entorno acotado:** "in some countries/cities, autonomous shuttle buses have been implemented on less-traveled routes where they can travel at speeds up to 25 km/h without hindering the public's circulation, such as university campuses, industrial areas, airports, and sports bases."
- **Existen despliegues explícitamente en propiedad privada:** la tabla incluye Local Motors Olli en Goodyear Colmar-Berg (Luxemburgo, "Private property"), The Goodyear Tire en Akron Ohio ("Private property", on-demand), GoMentum Station en Concord California ("Private property") y University of Buffalo ("Private property"); EasyMile EZ10 en el aeropuerto Velizy-Villacoublay ("Government property"). Rutas típicas entre 0,3 y 4 km (excepción: 26 km en Yangquan, China, con 22 vehículos Baidu Apollo).
- **Localización:** GNSS necesita precisión centimétrica que solo se alcanza con corrección RTK desde una estación base, y "The transfer of GNSS/RTK differential corrections from the reference base stations to the AV is carried out via mobile communications or the Internet (3G/4G/5G)" — es decir, la localización precisa depende de la red. El GNSS+RTK usado por Navya tiene un refresco bajo (1–20 Hz), razón por la cual otros fabricantes (EasyMile) usan SLAM con LiDAR y cámaras; la desventaja del SLAM es que "there is no delimitation of the mapped space, which requires extra hardware and software resources".
- **Brecha sensor vs. cerebro humano:** los autores señalan que los sensores no pueden ver a través de niebla o lluvia intensa y que el algoritmo del AV no alcanza el poder de procesamiento del cerebro humano para compensar factores perturbadores del entorno.
- **Marco legal desigual:** la legislación sobre AV es extremadamente dispar a nivel global, con vacíos en homologación, registro e implementación en vía pública, lo que empuja a las ciudades a integrarlos vía programas de prueba.

## Conclusiones
Los shuttles autónomos ya son parte de la vida cotidiana de grandes ciudades, pero su aceptación como medio estratégico de transporte depende de su eficiencia en el servicio diario. El primer paso hacia la conducción autónoma se ha dado en todos estos contextos; el marco legal sigue siendo el cuello de botella.

## Limitaciones
Revisión de 2020: el catálogo de despliegues está desactualizado respecto de 2024-2026 (no incluye WeRide, HOLON, Ohmio ni la consolidación/quiebras del sector). No reporta métricas de confiabilidad (uptime, disengagements) de los despliegues tabulados. **No aparece ningún despliegue en Chile ni en Sudamérica en la tabla** (verificado por búsqueda de texto).

## Relevancia / brecha para el estado del arte
Establece el mapa base del estado del arte: el shuttle autónomo de baja velocidad se despliega precisamente en campus, áreas industriales y aeropuertos, y hay antecedentes en propiedad privada (Goodyear). Sirve para acreditar que la tecnología existe comercialmente pero **no como solución llave en mano validada para un recinto nuevo**: la localización depende de RTK sobre red móvil y del mapeo previo del sitio.

> Relaciones → `../../indice.json`. Ver [[paper-anund-2022-lecciones-sitios-demo-shuttle-autonomo]] y [[reporte-ncdot-2024-cassi-unc-charlotte]].
