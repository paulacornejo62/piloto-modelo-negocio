---
id: reporte-ncdot-2024-cassi-unc-charlotte
titulo: "CASSI at UNC Charlotte – Executive Summary / Final Report (NCDOT, julio 2024)"
tipo: reporte
tema: Piloto de 23 semanas de shuttle autónomo Navya Autonom en campus universitario con V2I — KPIs operacionales duros
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [vehiculo-autonomo-shuttle, disengagement-kpi-piloto, localizacion-gnss-rtk, aceptacion-usuario-vehiculo-autonomo]
anio: 2024
autores: [North Carolina Department of Transportation, University of North Carolina at Charlotte, Beep Inc.]
referencia: https://www.ncdot.gov/divisions/integrated-mobility/innovation/cassi/Documents/cassi-ncdot-unc-charlotte-executive-summary.pdf
motor: WebSearch → PDF oficial NCDOT (extracción de texto local)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 6-7
metricas_clave: ["85% uptime (625 h reales de 736 programadas)", "91.0% del tiempo en modo autónomo", "6.2 mph velocidad promedio (12.6 mph máx)", "825 viajes / 565 pasajeros en 23 semanas", "83% buena experiencia; 69% volvería a viajar; 56% tiempo de espera razonable"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
Evaluar el desempeño operacional, la confiabilidad y la aceptación de un shuttle automatizado de baja velocidad en un entorno de campus complejo, con comunicación Vehicle-to-Infrastructure (V2I) en cuatro semáforos reales, como parte del programa CASSI (Connected Autonomous Shuttle Supporting Innovation) de NCDOT.

## Hipótesis
Supuesto de partida del programa: un shuttle automatizado de baja velocidad puede aportar valor como opción de primera/última milla en un sistema multimodal de campus. El piloto pone a prueba ese supuesto y lo refuta parcialmente.

## Metodología
- **Diseño:** piloto operacional real con recolección de datos semanales del operador (Beep) + encuesta a usuarios + eventos de participación comunitaria.
- **Datos / muestra:** 12 de julio a 21 de diciembre de 2023 (23 semanas), ruta de 2,2 millas con 6 paradas conectando la estación LYNX Blue Line, Greek Village, dormitorios, estacionamientos, edificios académicos y el student union. Servicio gratuito, días hábiles 8:30–11:30 y 13:30–16:30 (pausa de carga a mediodía). Encuesta: 59 respondentes que viajaron; participación comunitaria: 11 respondentes.
- **Técnicas:** reportes semanales de operación del proveedor, encuesta en línea, diagramas Sankey de percepción antes/después.
- **Métricas:** uptime, % de tiempo en modo autónomo, velocidad promedio/máxima, viajes, pasajeros, causas de desconexión (disengagement), percepción de seguridad y experiencia.

## Resultados principales
- **Operación:** 565 pasajeros, 825 viajes, **85% de uptime** (625 horas operadas de 736 programadas), **91,0% del tiempo en modo autónomo**, velocidad promedio **6,2 mph (~10 km/h)** y máxima 12,6 mph (~20 km/h).
- **Causa principal de desconexión:** "The most common cause of the shuttle's disengagement from autonomous mode into manual mode was lost connection or miscommunication between the shuttle's Onboard Unit (OBU) and the Roadside Units (RSUs) at the signalized intersections on the route." Es decir, la **falla de conectividad V2I**, no la percepción.
- **Causa principal de fuera de servicio:** "the shuttle was out of service for a considerable amount of time due to technology issues, notably due to Global Navigation Satellite System (GNSS) signal loss and battery insufficiency." La insuficiencia de batería se agravó por el aire acondicionado en días calurosos y por la edad del vehículo.
- **Percepción de usuarios:** 83% tuvo buena experiencia con el shuttle, 92% con el acompañante a bordo, **69% volvería a viajar**, 69% apoya ver más shuttles sin conductor en el campus; pero solo **56% consideró razonable el tiempo de espera** y 61% el tiempo de viaje.
- **Comparación con el piloto previo (Bond Park, Cary):** donde el shuttle era la única opción de transporte, 81% volvería a viajar y 88% apoyaba más shuttles; en UNC Charlotte, compitiendo con buses y caminata, esas cifras bajan a 69%. El 44% habría tomado bus y el 39% habría caminado si no existiera el shuttle.
- **Veredicto de madurez:** "Both pilots concluded that the automated shuttle technology is not mature and is not ready to be mainstreamed or scaled as a conventional transit service. The shuttle is not designed to be fully autonomous. An onboard human attendant is necessary."
- NCDOT devolvió el vehículo a Beep y determinó que no era razonable seguir probándolo en Carolina del Norte dadas las limitaciones identificadas.

## Conclusiones
El entorno operacional complejo del campus **excedió las capacidades** del shuttle y del servicio. No se encontró beneficio de tiempo ni de conectividad frente a las alternativas del campus. Desafíos comunes a ambos pilotos: desempeño poco confiable de la tecnología habilitante (pérdida de señal GNSS, pérdida de conexión o mala comunicación en las intersecciones semaforizadas, fallas de software que requerían reinicios duros), insuficiencia de batería, inconsistencia operacional por clima y problemas técnicos, y ausencia de funciones de accesibilidad.

## Limitaciones
Un solo vehículo (Navya Autonom con cierta antigüedad, lo que afectó la batería), un solo sitio, encuesta con N=59 (autoselección de quienes viajaron). Ruta en tráfico mixto con semáforos públicos — no es un recinto privado cerrado, por lo que la dependencia de V2I es mayor que en un patio industrial sin semáforos.

## Relevancia / brecha para el estado del arte
Es el **benchmark cuantitativo público más útil** para fijar KPIs de un piloto: uptime 85%, 91% en modo autónomo, velocidad promedio ~10 km/h. Muestra que en un piloto bien financiado y acompañado, ~15% de las horas programadas se pierden por tecnología. Confirma que la **conectividad (V2I y GNSS/RTK) es la primera causa de desconexión y de fuera de servicio**, por encima de la percepción de obstáculos.

> Relaciones → `../../indice.json`. Complementa [[paper-grandhi-2025-disengagements-shuttle-velocidad]] (mismo despliegue, análisis estadístico independiente) y [[paper-anund-2022-lecciones-sitios-demo-shuttle-autonomo]].
