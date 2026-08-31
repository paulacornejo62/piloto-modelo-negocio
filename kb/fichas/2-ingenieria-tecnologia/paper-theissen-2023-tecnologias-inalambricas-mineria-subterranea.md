---
id: paper-theissen-2023-tecnologias-inalambricas-mineria-subterranea
titulo: "Use-Case-Oriented Evaluation of Wireless Communication Technologies for Advanced Underground Mining Operations (Theissen, Kern, Hartmann, Clausen — Sensors, 2023)"
tipo: paper
tema: Evaluación comparada de tecnologías inalámbricas (Wi-Fi, LTE privada, 5G, LPWAN) contra los requisitos de casos de uso mineros, incluida la teleoperación
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [redes-privadas-lte-5g-industriales, mineria-remota-automatizacion, teleoperacion-supervision-remota, requisitos-red-latencia-jitter]
anio: 2023
autores: [Marius Theissen, Leonhard Kern, Tobias Hartmann, Elisabeth Clausen]
referencia: "https://doi.org/10.3390/s23073537 — full-text OA: https://pmc.ncbi.nlm.nih.gov/articles/PMC10099074/"
motor: WebSearch + WebFetch (PubMed Central, open access)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: ["Tele-remoto: RTT <40 ms para control (no relevante a seguridad)", "Supervisión: retardo unidireccional <1000 ms", "Ancho de banda: ~10 Mbit/s por máquina", "Requisito: cobertura constante y roaming sin cortes en el área tele-remota"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Pregunta / objetivo de investigación

¿Qué tecnología inalámbrica satisface qué caso de uso minero avanzado (tele-remoto, autonomía, monitoreo, seguridad), y dónde están las brechas tecnológicas?

## Metodología

Revisión sistemática orientada a casos de uso: se derivan requisitos de comunicación por caso de uso minero y se contrastan con las capacidades declaradas de cada tecnología (Wi-Fi/Wi-Fi 6, LTE privada, 5G, LPWAN, sistemas propietarios), en el contexto específico de minería subterránea.

## Resultados principales

Requisitos de teleoperación (control remoto de maquinaria):
> "Softly bounding time delays round trip (<40 ms) for control (not safety-relevant)"
> "Softly bounding time delays for single way (<1000 ms) for supervision"
> "High-speed connection (~10 Mbit/s) for each machine (possibly higher for VR applications)"
> "Constant coverage and seamless roaming in working/tele-remote areas"

Estado de las tecnologías:
> "5G is suitable for a fully teleoperated or autonomous mining fleet from the specification side; however, the feasibility of the hardware and application in the field of an active mine still needs to be researched"
> "5G and WiFi 6 Ghz have not been extensively tested underground yet, and further research is needed to evaluate their operational capabilities in those environments"
> "There is no technology that offers both a high data rate and a high range–this is due to the lack of penetration"
> "The technology always has to be evaluated within the use case and operational constraints"

## Conclusiones

Desde el papel, 5G cumple las especificaciones de una flota minera teleoperada o autónoma; **la validación en faena activa sigue siendo materia de investigación**. No existe una tecnología única que resuelva simultáneamente alta tasa de datos y largo alcance, lo que empuja a arquitecturas híbridas.

## Limitaciones

- Enfoque en minería **subterránea**; los desafíos de propagación difieren de rajo abierto (aunque comparte el problema de cobertura en topografía cambiante).
- Revisión de especificaciones y literatura, no medición propia en faena.

## Relevancia / brecha para el estado del arte

Fuente académica revisada por pares que declara explícitamente que la aplicación en faena activa de 5G para flota teleoperada **aún requiere investigación**. Es el respaldo para argumentar incertidumbre técnica genuina en el diseño de conectividad minera, y para justificar arquitectura híbrida (privada LTE/5G + enlaces punto a punto + fibra). Nótese que su requisito de RTT (<40 ms) es más laxo que el de 3GPP ([[estandar-3gpp-ts22186-remote-driving]]) y consistente con el control tele-remoto industrial de baja velocidad.

> Relaciones con otras fichas → `../../indice.json`.
