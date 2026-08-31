---
id: paper-anund-2022-lecciones-sitios-demo-shuttle-autonomo
titulo: "Lessons learned from setting up a demonstration site with autonomous shuttle operation – based on experience from three cities in Europe (Anund et al., 2022)"
tipo: paper
tema: Lecciones operacionales de puesta en marcha de sitios de demostración con shuttles autónomos (Bruselas, Linköping, Turín)
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [vehiculo-autonomo-shuttle, percepcion-lidar-clima, localizacion-gnss-rtk, comisionamiento-mapeo-ruta, teleoperacion-supervision-remota]
anio: 2022
autores: [Anna Anund, Ricker Ludovic, Brunella Caroleo, Hugo Hardestam, Anna Dahlman, Ingrid Skogsmo, Mathieu Nicaise, Maurizio Arnone]
referencia: https://doi.org/10.1016/j.urbmob.2022.100021
motor: WebSearch + Unpaywall + repositorio DiVA (VTI, Suecia) — PDF full-text
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 6-7
metricas_clave: ["velocidad operacional AV 5–16 km/h (hasta 33 km/h en Turín)", "rutas de 0.7–2.1 km", "18 operadores de seguridad entrenados en un sitio", "operadores de seguridad lesionados por frenado brusco en 2 sitios"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
Consolidar las lecciones aprendidas durante la preparación e implementación de operaciones de shuttles autónomos en entornos cuasi urbanos, para facilitar el montaje de nuevos sitios de operación. Los tres sitios (Bruselas/STIB-MIVB, Linköping/VTI, Turín/ITCILO) operan marcas, número de vehículos e infraestructuras distintos; el foco es lo genérico, no la comparación entre marcas.

## Hipótesis
No hay hipótesis formal: es un estudio de lecciones aprendidas de tipo observacional/experiencial. Supuesto de partida: montar un sitio de operación autónoma implica mucho más que elegir la ruta (permisos, infraestructura, condiciones locales, operadores).

## Metodología
- **Diseño:** estudio observacional multi-sitio de lecciones aprendidas (perspectiva operacional).
- **Datos / muestra:** tres sitios de demostración en Europa: Bruselas (Woluwe Park ~1,7 km en 2 rutas, Solvay 1,6 km, Hospital Brugmann 1,2 km), Linköping (Campus Valla ~2,1 km, ruta de ~15 min), Turín (campus ITCILO, 700 m). Shuttles de distintas marcas, velocidad AV entre 5 y 33 km/h (Tabla 1 del paper).
- **Técnicas:** observación de la operación, retroalimentación de operadores de seguridad, registro de eventos de frenado y detención.
- **Métricas:** velocidad máxima/mínima de operación, causas de detención/frenado brusco, condiciones que degradan la localización.

## Resultados principales
- **Clima y partículas rompen la percepción LiDAR:** la lluvia no se detecta hasta que las gotas alcanzan cierto tamaño, momento en que se identifican como muchos obstáculos pequeños; el shuttle "laguea" (reducción aleatoria de velocidad) y finalmente se detiene. La niebla se detecta como **paredes** alrededor del vehículo. El **polvo** en caminos secos y ventosos es percibido como niebla y, en ciertas circunstancias, es **más crítico que la niebla**: el propio shuttle levanta polvo sobre cierta velocidad y el LiDAR "ve" un muro que dispara una parada de emergencia; si no se le "enseña" a reconocer ese obstáculo, se detendrá en el mismo punto en cada viaje hasta que se retire el polvo.
- **Vegetación y objetos móviles:** pasto crecido, ramas o flores moviéndose con el viento se reconocen como obstáculos móviles y frenan el shuttle — un problema "pasado por alto durante el proceso de mapeo". Bolsas plásticas y pájaros también disparan frenado abrupto; no se encontró solución adecuada para aves/animales.
- **Localización:** se combinan GNSS (mejorado con RTK), odometría y LiDAR contra el mapa registrado. **RTK depende de la disponibilidad de conexión de datos (4G o superior)**. Árboles al borde del camino reducen la cobertura GNSS igual que un túnel, degradando la precisión y por tanto la velocidad. En entornos sin puntos fijos permanentes (desierto, bosque) la localización LiDAR puede volverse inutilizable; algunas marcas exigen **señales físicas de 1 × 1,5 m** como referencias adicionales.
- **Frenado brusco e infraestructura:** los LiDAR no siempre son compatibles con lomos de toro y cruces elevados — el sensor los identifica como objetos e inicia un frenado (duro). Los shuttles priorizan la seguridad externa por sobre la interna; hubo **operadores de seguridad lesionados en dos sitios** por frenados bruscos.
- **Datos y KPIs cerrados:** los OEM no comparten la razón detrás de un frenado externo ni abren su API, lo que obliga a trabajo extra: "most customers need to evaluate the shuttles' performance and hence require data of a rather high resolution, to be able to measure and calculate basic Key Performance Indicators (KPIs) such as acceleration, deceleration, etc."
- **Rol del operador:** las competencias reales no son de conducción sino **de TI** — procedimientos de arranque, verificación continua del alineamiento de los sistemas de procesamiento y telecomunicaciones, procedimientos de reinicio ante eventos inesperados y respaldo de datos al cierre del servicio.

## Conclusiones
El desarrollo adicional de los shuttles AV es vital para que operen sin fricción en situaciones de tráfico complejas considerando ancho de vía, espacios compartidos, nieve, polvo, lluvia, hojas y aves. Los autores recomiendan **evitar adaptar la infraestructura vial** al shuttle y priorizar que el shuttle se adapte al entorno existente, aunque reconocen que hoy eso no es posible. Áreas de mitigación identificadas: infraestructura vial, operación dependiente del clima, operación dependiente de la estación, mejora de la localización, infraestructura digital, condiciones de diseño y trabajo, y experiencia del usuario/ciudadano.

## Limitaciones
Estudio cualitativo/experiencial, no cuantitativo: no reporta tasas de incidentes ni uptime. Tres sitios europeos, marcas no identificadas por diseño (foco genérico). No cubre entornos privados industriales cerrados ni climas extremos fuera de Europa.

**Nota QA (2026-07-29):** verificado contra el PDF de DiVA (diva2:1741137). Cita textual del polvo exacta. Corrección: los largos de ruta de la Tabla 1 son 0,7–2,1 km (Woluwe 1,7; Solvay 1,6; Brugmann 1,2; Linköping 2,1; Turín 0,7); la versión previa de esta ficha decía "0,7–5 km", cifra que no aparece en el paper.

## Relevancia / brecha para el estado del arte
Es la referencia más directa para el problema de **comisionamiento y adaptación de ruta** en un recinto propio: documenta que el mapeo inicial subestima sistemáticamente los falsos positivos de percepción (vegetación, polvo, lomos de toro) y que el ajuste requiere iteración en terreno con datos de alta resolución que los OEM no entregan. El hallazgo de **polvo → parada de emergencia recurrente en el mismo punto** es especialmente relevante para patios logísticos con tránsito de camiones y superficies secas. Deja abierto: no existe método sistemático publicado para caracterizar y mitigar estos falsos positivos en un recinto privado específico.

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`. Ver [[review-iclodean-2020-autonomous-shuttle-bus]] y [[reporte-ncdot-2024-cassi-unc-charlotte]].
