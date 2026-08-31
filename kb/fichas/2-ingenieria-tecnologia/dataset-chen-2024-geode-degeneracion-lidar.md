---
id: dataset-chen-2024-geode-degeneracion-lidar
titulo: "GEODE: Heterogeneous LiDAR Dataset for Benchmarking Robust Localization in Diverse Degenerate Scenarios (Chen et al., 2024)"
tipo: preprint
tema: Fallo de la localización LiDAR (SLAM) en entornos geométricamente degenerados, incluidos terrenos planos y abiertos sin rasgos distintivos
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [localizacion-y-mapeo, localizacion-gnss-rtk, entorno-semi-estructurado]
anio: 2024
autores: [Zhiqiang Chen, Yuhua Qi, Dapeng Feng, Xuebin Zhuang, Hongbo Chen, Xiangcheng Hu, Jin Wu, Kelin Peng, Peng Lu]
referencia: https://arxiv.org/abs/2409.04961
motor: WebSearch → arXiv (abstract verificado en la página oficial; detalles de escenarios y tablas vía lectura HTML asistida)
profundidad_lectura: abstract
estado_evidencia: parcial
trl_relevante: "3 (dataset de investigación / benchmark)"
metricas_clave: ["64 trayectorias, más de 64 km, 7 entornos con distintos grados de degeneración", "derivas reportadas de 10,27 a 70,26 m para FAST-LIO2 en el escenario de vía navegable (dato no verificado en el PDF)"]
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
¿Qué tan robustos son los algoritmos de SLAM LiDAR del estado del arte en entornos geométricamente degenerados, es decir, sin suficientes rasgos estructurales distintivos para el registro de nubes de puntos?

## Hipótesis
Los datasets abiertos existentes no representan escenarios degenerados, lo que impide desarrollar y comparar algoritmos de localización robustos; en esos escenarios los métodos actuales fallan.

## Metodología
- **Diseño:** construcción de dataset multi-LiDAR y benchmark comparativo.
- **Datos / muestra:** cita textual del abstract: *"GEODE comprises 64 trajectories spanning over 64 kilometers across seven diverse settings with varying degrees of degeneracy."* Los siete entornos incluirían superficies planas, escaleras, túneles de metro, terreno abierto (offroad), vías navegables interiores, túneles urbanos y puentes (**detalle no verificado directamente en el PDF**).
- **Técnicas:** evaluación comparativa de métodos SLAM LiDAR/LiDAR-inercial del estado del arte sobre las trayectorias.

## Resultados principales
- Cita textual del abstract: *"existing open-source datasets lack representation of geometrically degenerate environments, limiting the development and benchmarking of robust LiDAR SLAM algorithms."*
- Según la lectura del HTML (no verificada línea a línea en el PDF): todos los métodos evaluados fallan en los escenarios de puente y túnel urbano; en superficies planas con uno de los dispositivos, seis de siete métodos fallan; derivas de decenas de metros en vía navegable.
- Cita reportada (marcada como no verificada de forma independiente): *"In scenarios involving geometric degradation, features useful for localization tend to be sparse. Consequently, feature extraction can result in significant portions of geometric information being ignored, leading to performance degradation."*

## Conclusiones
La localización basada en LiDAR pierde observabilidad cuando el entorno carece de estructura geométrica distintiva; es un modo de falla conocido y no resuelto, además de silencioso (el sistema entrega una pose plausible pero incorrecta).

## Limitaciones
- Ficha construida sobre el abstract verificado más una lectura asistida del HTML: las cifras de la tabla de fallos **no fueron verificadas directamente** y se marcan como tales.
- Preprint (arXiv), sin verificación de versión publicada.
- Escenarios no incluyen un patio logístico como tal.

## Relevancia / brecha para el estado del arte
El Centro Logístico Kaufmann se describe como **terreno plano y abierto** con señalización vertical parcial: geométricamente pobre en rasgos para el registro de nubes de puntos, con el agravante de que los elementos "estructurales" disponibles (camiones estacionados, contenedores, pilas de carga) son **móviles**, es decir, contaminan el mapa entre sesiones. Esta ficha respalda que la localización confiable en ese tipo de recinto no es un problema trivialmente resuelto por SLAM comercial, y que la solución típica pasa por añadir infraestructura (GNSS-RTK, reflectores, balizas) — es decir, habilitación del sitio.

> Relaciones: complementa a [[patente-us11661059b2-validacion-localizacion-velocidad-easymile]] (validación de la localización y reducción de velocidad) y a [[paper-waiwanijchakij-2024-uwb-navegacion-camion-autonomo-industrial]].
