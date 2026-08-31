---
id: paper-kim-2023-degradacion-lidar-lluvia-niebla
titulo: "Empirical Analysis of Autonomous Vehicle's LiDAR Detection Performance Degradation for Actual Road Driving in Rain and Fog (Kim, Park & Kim, 2023)"
tipo: paper
tema: Cuantificación experimental de la caída del desempeño de un LiDAR automotriz bajo lluvia y niebla controladas en pista real
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [percepcion-lidar-clima, seguridad-funcional-av, recinto-privado-odd]
anio: 2023
autores: [Jiyoon Kim, Bum-jin Park, Jisoo Kim]
referencia: https://doi.org/10.3390/s23062972 (PMC10051412)
motor: WebSearch → PubMed Central (PMC10051412, open access)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "4-5 (ensayo controlado en pista de pruebas climáticas)"
metricas_clave: ["niebla de visibilidad 50 m a 50 m de distancia: NPC cae 26% (mejor material, film retrorreflectante)", "lluvia ≥30 mm/h: NPC cae hasta 56% e intensidad hasta 73%", "aluminio y acero: no observados a 20-30 m bajo niebla densa", "orden de severidad: lluvia leve (10-20 mm/h) < niebla débil (<150 m) < lluvia intensa (30-40 mm/h) < niebla densa (≤50 m)"]
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
¿Cuánto se degrada, en términos medibles, la detección de un LiDAR automotriz de 905 nm bajo lluvia y niebla de intensidad controlada, y cómo influye el material del objeto detectado?

## Hipótesis
La degradación no es uniforme: depende de la intensidad del fenómeno, de la distancia al objeto y del material/reflectancia de la superficie objetivo.

## Metodología
- **Diseño:** experimental controlado en pista real.
- **Datos / muestra:** Hyundai Tucson con Robosense RS-32 (32 canales, 905 nm, 600.000 puntos/s) en el Road Weather Proving Ground del KICT (Corea), con generación controlada de lluvia y niebla sobre asfalto real. Objetivos: paneles de 60×60 cm de film retrorreflectante, aluminio, acero, plástico y lámina negra. Cinco repeticiones por escenario.
- **Técnicas:** medición a 10, 20, 30, 40 y 50 m; lluvia de 10, 20, 30 y 40 mm/h; niebla de visibilidad 50, 100 y 150 m.
- **Métricas:** número de puntos de la nube (NPC) e intensidad, contra la condición despejada.

## Resultados principales
- Niebla densa (visibilidad 50 m), a 50 m de distancia: *"At a detection distance of 50 m with the thickest fog, the NPC decreased by 26%"* — y ese es el **mejor** caso (film retrorreflectante).
- Aluminio y acero bajo niebla densa: no observación a 20-30 m.
- Lluvia intensa: *"Under intense rain with precipitation of 30 mm/h or more, the value of NPC decreased by a maximum of 56%, and the intensity also decreased by a maximum of 73%"*.
- El film retrorreflectante conserva al menos 74% del NPC de la condición despejada bajo lluvia intensa y niebla densa; los materiales no reflectantes caen mucho más.
- Orden de severidad creciente: lluvia leve → niebla débil (<150 m) → lluvia intensa → niebla densa (≤50 m).

## Conclusiones
La niebla densa es la peor condición de las estudiadas para un LiDAR de 905 nm, y su efecto se amplifica con la distancia y con materiales de baja reflectancia. La detectabilidad depende fuertemente de la *retrorreflectividad del objeto*, no solo del sensor.

## Limitaciones
- Objetos estáticos de geometría simple, no peatones ni vehículos reales.
- El NPC no describe si la geometría del objeto queda adecuadamente representada.
- Efectos de "blooming" con materiales retrorreflectantes requieren estudio adicional.
- Un solo modelo de LiDAR (905 nm); no se prueban LiDAR de 1550 nm ni FMCW.

## Relevancia / brecha para el estado del arte
Da la base cuantitativa para el riesgo de **neblina densa de invierno en Lampa**: con visibilidad del orden de 50 m, un LiDAR de 905 nm pierde en torno a un cuarto de sus retornos en el mejor caso y deja de ver objetos de baja reflectancia a 20-30 m. Traducido al caso: un operario con ropa no reflectante o una grúa horquilla sin material retrorreflectante son precisamente los objetivos peor detectados. Refuerza que la respuesta del proveedor sobre operación en neblina (aún pendiente) es un supuesto crítico y no un detalle.

> Relaciones: complementa a [[paper-jiang-2024-filtrado-polvo-lidar-mina]] y a [[paper-bhatt-2024-watonobus-clima-adverso]].
