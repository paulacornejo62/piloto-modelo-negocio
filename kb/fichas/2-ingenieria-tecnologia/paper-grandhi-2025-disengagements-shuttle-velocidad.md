---
id: paper-grandhi-2025-disengagements-shuttle-velocidad
titulo: "Mixed-Effects Model to Assess the Effect of Disengagements on Speed of an Automated Shuttle with Sensors for Localization, Navigation, and Obstacle Detection (Grandhi, Gore & Pulugurtha, 2025)"
tipo: paper
tema: Cuantificación estadística del efecto de los disengagements sobre la velocidad de un shuttle automatizado en campus
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [vehiculo-autonomo-shuttle, disengagement-kpi-piloto, percepcion-lidar-clima]
anio: 2025
autores: [Abhinav Grandhi, Ninad Gore, Srinivas S. Pulugurtha]
referencia: https://doi.org/10.3390/s25020573
motor: Europe PMC → PMC11769011 (full-text open access, lectura asistida por WebFetch; no auditado tabla por tabla)
profundidad_lectura: full-text
estado_evidencia: parcial
trl_relevante: 6-7
metricas_clave: ["244 disengagements analizados en 6 meses (totales mensuales de la Tabla 1: 47+59+39+28+28+43)", "ruta de 2.2 millas, 7 paradas", "8 LiDAR + 3 cámaras + GNSS + IMU + RSU en 3 intersecciones"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
¿Cómo afectan los disengagements (transferencia de control del sistema automatizado al operador humano) a la velocidad operacional de un shuttle automatizado, y qué factores del entorno (geometría vial, actividad peatonal, clima, vegetación) los explican?

## Hipótesis
Los disengagements no son eventos neutros: degradan medible y sistemáticamente el desempeño del servicio (velocidad), y su frecuencia depende del segmento de ruta y de condiciones ambientales identificables.

## Metodología
- **Diseño:** modelado estadístico multinivel (mixed-effects, Gaussian log-link) sobre datos de operación real.
- **Datos / muestra:** shuttle del programa CASSI operado en el campus de UNC Charlotte, julio–diciembre 2023; ruta de 2,2 millas con 7 ubicaciones de parada; registros de disengagements, datos GPS por parada (Passio GO App), datos meteorológicos (Visual Crossing API) y características viales (Google Earth).
- **Técnicas:** modelo de efectos mixtos con segmento como efecto aleatorio.
- **Métricas:** frecuencia de disengagements por segmento, coeficiente de efecto sobre la velocidad esperada, varianza segmental.

## Resultados principales
- 244 disengagements analizados en seis meses de operación (los totales mensuales de la Tabla 1 suman 244; una cifra de "264 documentados" registrada en una lectura previa **no aparece** en el texto del paper).
- La frecuencia se concentra en segmentos con intersecciones semaforizadas, alta actividad peatonal y vegetación: "Signalized intersections, high pedestrian activity, and environmental factors like vegetation significantly affected the automated shuttle performance in terms of the frequency of disengagements".
- Efecto medible sobre el desempeño: cada evento reduce significativamente la velocidad esperada (coeficiente −0,803), con alta variabilidad entre segmentos (varianza de efectos aleatorios 0,981). El desglose porcentual verificado de las causas de esos mismos 244 eventos está en [[paper-golchin-2024-unc-charlotte-desempeno-confiabilidad]] (55,8% técnicos/señal, 25,8% seguridad/interacción, 14,2% ambientales, 4,1% navegación).
- Los autores definen el fenómeno: "Disengagements involve a transfer of control from the automated system to a human operator, typically due to interruptions in the shuttle's decision-making process".
- Sobre la localización: "Signal loss or degradation can result in the autonomous system being unable to determine its precise location, necessitating human intervention".
- Sobre V2I: "Vehicle-to-infrastructure communication failures can disrupt the shuttle's ability to make informed driving decisions".

## Conclusiones
Los disengagements tienen impacto operacional directo y medible sobre la velocidad, y su distribución no es uniforme: depende de la geometría y de las condiciones locales del segmento. Esto implica que la caracterización de la ruta (por tramo) es un insumo necesario para predecir el desempeño de un servicio de shuttle.

## Limitaciones
Datos GPS discontinuos (registrados solo en paradas) impidieron analizar la reacción inmediata del operador. Un solo vehículo, un solo sitio, seis meses. La categorización de causas depende de los registros del operador. El coeficiente puntual del modelo no se auditó tabla por tabla: para cifras citables usar el desglose verificado de Golchin et al. (2024) sobre el mismo dataset.

**Nota QA (2026-07-29):** cita textual de la definición de disengagement confirmada en PMC11769011; concentración por segmento y reducción de velocidad confirmadas. Se eliminó la cifra "264 eventos documentados" porque no aparece en el paper (el total es 244).

## Relevancia / brecha para el estado del arte
Aporta el **método** para medir el desafío que el proyecto declara (adaptación de ruta y detección de obstáculos): el disengagement por tramo como KPI, modelado contra variables de entorno. Es el precedente metodológico más cercano a lo que un piloto en recinto privado debería medir. La brecha: no existe equivalente publicado para recintos privados industriales (patios, tránsito de camiones, polvo).

> Relaciones → `../../indice.json`. Complementa [[reporte-ncdot-2024-cassi-unc-charlotte]] (mismo despliegue, datos del operador).
