---
id: paper-golchin-2024-unc-charlotte-desempeno-confiabilidad
titulo: "UNC Charlotte Autonomous Shuttle Pilot Study: An Assessment of Operational Performance, Reliability, and Challenges (Golchin, Grandhi, Gore, Pulugurtha & Ghasemi, 2024)"
tipo: paper
tema: Desglose cuantitativo de las causas de disengagement y de la confiabilidad de servicio de un shuttle autónomo en campus
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [vehiculo-autonomo-shuttle, disengagement-kpi-piloto, percepcion-lidar-clima, conectividad-red-vehiculo-autonomo, localizacion-gnss-rtk]
anio: 2024
autores: [Mohammadnavid Golchin, Abhinav Grandhi, Ninad Gore, Srinivas S. Pulugurtha, Amirhossein Ghasemi]
referencia: https://doi.org/10.3390/machines12110796
motor: Google Académico (browse.mjs scholar) + Crossref (DOI) + mirror PDF de MDPI (full-text)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 6-7
metricas_clave: ["244 disengagements en 6 meses", "55.8% técnicos/señal (44.6% intersecciones semaforizadas, 7.9% pérdida de señal 3G/GNSS/RTK, 3.4% códigos de falla)", "25.8% seguridad/interacción (18.4% otros usuarios de la vía)", "14.2% ambientales (9% vegetación, 4.9% detección de obstáculos, 0.4% clima)", "4.1% navegación/desviación de ruta", "825 viajes / 565 pasajeros; 64 viajes sin pasajeros", "batería 33 kWh; carga 4 h a 7.2 kW"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
Evaluar el desempeño operacional, la confiabilidad y los desafíos de un shuttle autónomo Navya Autonom en una ruta de campus en tráfico mixto, a partir de sensores de a bordo, logs del sistema y reportes del operador.

## Hipótesis
Los disengagements son un indicador válido de la robustez del servicio autónomo, y su distribución por causa y por ubicación permite identificar los cuellos de botella tecnológicos concretos.

## Metodología
- **Diseño:** análisis cuantitativo de datos operacionales de un piloto real.
- **Datos / muestra:** piloto CASSI en UNC Charlotte, junio–diciembre 2023 (el más largo de Carolina del Norte, cubriendo desde calor de verano hasta aguanieve de invierno); ruta de 2,2 millas en tráfico mixto con 4 semáforos; datos provistos por Beep.
- **Técnicas:** filtrado espacial con buffer de 50 pies alrededor de la ruta para retener solo disengagements atribuibles al trayecto; clasificación de causas en cuatro categorías; análisis espacio-temporal.
- **Métricas:** disengagements por causa y por mes, horas programadas vs. operacionales, uptime, uso de batería, velocidad promedio, % de autonomía, viajes y pasajeros.

## Resultados principales
- **244 disengagements** durante el piloto. Desglose verificado:
  - **Técnicos y de señal: 55,8%** — intersecciones semaforizadas 44,6% (119 incidentes), pérdida de señal 3G/GNSS/RTK 7,9% (21), códigos de falla 3,4% (9).
  - **Seguridad e interacción con terceros: 25,8%** — otros usuarios de la vía 18,4% (49), estación bloqueada 6,7% (18), usuarios vulnerables y seguridad 0,4% cada uno.
  - **Factores ambientales: 14,2%** — vegetación 9% (24), detección de obstáculos 4,9% (13), condiciones climáticas 0,4% (1).
  - **Navegación y desviación de trayectoria: 4,1%** — zona de prioridad 3,4% (9), desviación manual de la ruta aprobada 0,7% (2).
- La definición operativa de pérdida de señal es explícita: "The shuttle lost its 3G/GNSS/RTK signal, making it unable to continue in automated mode. The shuttle operator navigated manually until the signal was restored".
- Vegetación como causa formal: "Vegetation obstructed the shuttle's path, preventing automated operation."
- Variación mensual de disengagements: máximo en agosto (59), mínimo en octubre y noviembre (28) — sugiere efecto estacional y curva de aprendizaje.
- 825 viajes y 565 pasajeros; 64 viajes se realizaron sin pasajeros a bordo.
- Mejora progresiva: "the shuttle showed a progressive improvement in operational efficiency, with higher uptime percentages and better consistency as the months progressed."
- Contexto de mercado citado por los autores: estos shuttles alcanzan velocidades de 15 a 45 km/h y llevan 8 a 15 pasajeros, con baterías de 20 a 33 kWh.

## Conclusiones
El piloto demuestra potencial pero revela barreras: los disengagements por problemas técnicos y de señal en intersecciones son el obstáculo principal a la operación plenamente autónoma; los factores ambientales (clima, vegetación) e interacciones con otros usuarios contribuyen en menor medida. Recomendaciones: mejorar recepción GNSS e implementar protocolos V2I robustos, optimizar la gestión de batería, mejorar los algoritmos de detección y evasión de obstáculos, y entrenar de forma continua a los acompañantes.

## Limitaciones
Un vehículo, un sitio, seis meses. Datos de disengagement provistos por el operador (clasificación propietaria). La alta incidencia de intersecciones semaforizadas es propia de una ruta con semáforos públicos: **no es directamente extrapolable a un recinto privado sin semáforos**, donde ese 44,6% desaparecería y el peso relativo de vegetación, obstáculos e interacción con terceros aumentaría.

## Relevancia / brecha para el estado del arte
Es la **fuente cuantitativa más granular disponible** sobre por qué se desconecta un shuttle autónomo. Permite construir la taxonomía de causas para el instrumento de medición de un piloto propio y anticipar que, retirados los semáforos, los factores dominantes serán interacción con terceros (18,4%), vegetación/obstáculos (~14%) y pérdida de señal (~8%). No existe publicación equivalente para un recinto industrial privado con tránsito de camiones y polvo.

> Relaciones → `../../indice.json`. Complementa [[reporte-ncdot-2024-cassi-unc-charlotte]] y [[paper-grandhi-2025-disengagements-shuttle-velocidad]] (mismo dataset, distinto análisis).
