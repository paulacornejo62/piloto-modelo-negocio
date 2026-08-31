---
id: paper-li-2023-teleoperador-remoto-5g-nivel4
titulo: "Exploration into the Needs and Requirements of the Remote Driver When Teleoperating the 5G-Enabled Level 4 Automated Vehicle in the Real World (Li, Zhang, Edwards & Blythe, 2023)"
tipo: paper
tema: Necesidades y limitaciones del operador remoto de un vehículo automatizado nivel 4 con 5G en operación logística real
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [teleoperacion-supervision-remota, conectividad-red-vehiculo-autonomo]
anio: 2023
autores: [Shuo Li, Yanghanzi Zhang, Simon Edwards, Philip T. Blythe]
referencia: https://doi.org/10.3390/s23020820
motor: Europe PMC → PMC9864956 (full-text open access)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 6
metricas_clave: ["6 operadores remotos entrevistados", "vehículo Terberg nivel 4 SAE en ruta logística real (proyecto 5G CAL)", "pérdidas de conexión 5G registradas durante la operación"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
  - kaufmann-telecomando
---

## Pregunta / objetivo de investigación
¿Qué necesita el conductor remoto para teleoperar con seguridad un vehículo automatizado de nivel 4 habilitado con 5G en el mundo real, y qué limitaciones percibe en la interfaz y en la conectividad?

## Hipótesis
La teleoperación remota exige compensar la pérdida de información perceptual y propioceptiva que el conductor tendría a bordo; sin ello, el desempeño y la confianza del operador se degradan.

## Metodología
- **Diseño:** estudio cualitativo con entrevistas semiestructuradas y análisis temático.
- **Datos / muestra:** 6 operadores remotos con licencia vigente y experiencia activa con el sistema, en el proyecto 5G Connected and Automated Logistics (5G CAL), con un tractocamión eléctrico Terberg de 40 toneladas (modificado por StreetDrone) a nivel 4 SAE operando en la ruta real entre Vantec UK y la planta de Nissan, noreste de Inglaterra, sobre 5G en espectro compartido Ofcom N77.
- **Técnicas:** entrevistas sobre 7 temas clave; análisis temático con 6 temas centrales.
- **Métricas:** cualitativas (necesidades declaradas, incidentes percibidos).

## Resultados principales
- **Campo visual insuficiente:** los operadores reclaman visión de 360 grados equivalente a la de a bordo — "The camera angles, obviously when you're in a car you've got 360 degrees view".
- **Ausencia de retroalimentación de movimiento:** "The main difference is you can't feel it... you can hear it, you turn the wheel, you can hear it. In the remote driver seat, you don't get that at all."
- **Dependencia total de la red:** "Remote operators are responsible for some operations... There were a few instances where the 5G connection was lost" — la continuidad operativa depende del enlace, incluso con 5G dedicado.
- Solicitan interfaces multimodales (alertas audibles además de visuales, retroalimentación háptica).

## Conclusiones
Los operadores mantienen actitud positiva hacia la tecnología, pero requieren mejoras sustanciales en fidelidad perceptual y de movimiento para una operación remota efectiva. La teleoperación no es un respaldo trivial: es un puesto de trabajo con requisitos propios de diseño.

## Limitaciones
Muestra muy pequeña (N=6), cualitativa, un solo proyecto y un vehículo logístico pesado (no un shuttle de pasajeros). No cuantifica latencia ni tasa de pérdida de conexión.

## Relevancia / brecha para el estado del arte
Evidencia empírica de que **la supervisión remota como respaldo tiene fallas de conectividad incluso sobre 5G** y de que la interfaz del operador remoto es un problema de diseño no resuelto. Relevante para dimensionar la estrategia de respaldo del piloto (a bordo vs. remoto) y para justificar la caracterización de la conectividad del recinto.

> Relaciones → `../../indice.json`. Ver [[review-kamtam-2024-latencia-teleoperacion-cav]] y [[paper-mutzenich-2021-situation-awareness-operador-remoto]] (marco de conciencia situacional del operador remoto).
