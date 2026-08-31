---
id: paper-bhatt-2024-watonobus-clima-adverso
titulo: "WATonoBus: Field-Tested All-Weather Autonomous Shuttle Technology (Bhatt et al., 2023/2024)"
tipo: preprint
tema: Arquitectura modular de shuttle autónomo probada en campo durante casi dos años en clima adverso (lluvia, nieve, niebla)
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [vehiculo-autonomo-shuttle, percepcion-lidar-clima, recinto-privado-odd]
anio: 2023
autores: [Neel P. Bhatt, Ruihe Zhang, Minghao Ning, Ahmad Reza Alghooneh, Joseph Sun, Pouya Panahandeh, Ehsan Mohammadbagher, Ted Ecclestone, Ben MacCallum, Ehsan Hashemi, Amir Khajepour]
referencia: https://arxiv.org/abs/2312.00938
motor: WebSearch → arXiv (abstract + HTML parcial)
profundidad_lectura: full-text
estado_evidencia: parcial
trl_relevante: 6-7
metricas_clave: ["servicio en días hábiles durante casi 2 años en campus (U. Waterloo)", "velocidad máxima 20 km/h", "6 cámaras + 3 LiDAR 32 canales + GNSS/RTK + 2 radares + Jetson Orin AGX"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
¿Cómo diseñar una arquitectura de autonomía capaz de operar en todo tipo de clima (lluvia, nieve, niebla) integrando percepción, decisión, planificación y monitoreo de seguridad, en lugar de resolver módulo por módulo?

## Hipótesis
Una arquitectura multi-módulo y modular, con consideraciones de clima adverso incorporadas transversalmente (por ejemplo, detección de bordes de calzada cubiertos de nieve), permite operación sostenida donde los enfoques mono-módulo basados en modelos fallan.

## Metodología
- **Diseño:** reporte de sistema con validación en operación real de servicio.
- **Datos / muestra:** plataforma WATonoBus en el campus de la Universidad de Waterloo, servicio en días hábiles durante casi dos años, ruta de anillo predefinida de última milla, velocidad máxima 20 km/h.
- **Técnicas:** fusión LiDAR-cámara-radar; uso de mapas HD para particionar puntos candidatos a bordillo; monitoreo de seguridad.

## Resultados principales
- Operación diaria sostenida durante casi dos años con manejo de lluvia, nieve y niebla; los autores destacan la utilidad de los casos límite (edge cases) observados en operación.
- **Detección de bordillo bajo nieve:** "LiDAR-only detection can perceive snow-covered curbs by employing HD maps to partition potential curb points in the point cloud into adjacent road regions" — la detección depende de un mapa HD previo del sitio.
- **Rol del radar:** "the radar's capacity to measure distance and speed plays a crucial role, especially when fused with the camera's high-definition imaging" — el radar complementa cuando el LiDAR se degrada.
- Referencia a experiencia comparable: copos de nieve, lluvia intensa e incluso hojas volando causaron paradas de emergencia frecuentes en despliegues previos.

## Conclusiones
La operación en clima adverso es alcanzable, pero exige una arquitectura diseñada de extremo a extremo para ello (fusión multimodal + mapas HD + monitoreo de seguridad), no un módulo de percepción genérico.

## Limitaciones
Preprint; no reporta métricas cuantitativas públicas de uptime, disengagements ni incidentes en la porción consultada. Lectura del HTML de arXiv asistida: las citas se localizaron pero **no se auditaron línea por línea sobre el PDF**, por lo que la ficha se marca como evidencia parcial. Campus universitario canadiense: clima frío, no polvo industrial.

## Relevancia / brecha para el estado del arte
Muestra el estado del arte académico en robustez climática: es alcanzable, pero requiere I+D específica de arquitectura y **depende de un mapa HD del sitio**. Refuerza que adaptar un shuttle a un recinto nuevo con condiciones propias (polvo, camiones, superficies) es trabajo de desarrollo, no de instalación.

> Relaciones → `../../indice.json`. Ver [[paper-anund-2022-lecciones-sitios-demo-shuttle-autonomo]].
