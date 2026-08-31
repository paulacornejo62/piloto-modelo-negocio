---
id: review-eljarray-2025-battery-safety-ev
titulo: "Ensuring Battery Safety in Electric Vehicles: Challenges, Developments, and Future Perspectives (ELJarray et al. 2025)"
tipo: revision
tema: Revisión integral de seguridad de baterías Li-ion en EV: causas de fallo, mitigación por niveles y detección
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [seguridad-bateria-litio, fuga-termica-bateria, bms-monitoreo]
anio: 2025
autores: [Oumayma ELJarray, Hongliu Dai, Zhangsen Chen, Subhiksha Venkatesh Raja, Bojia Li, Siyi Cao, Shuhui Sun, Gaixia Zhang]
referencia: https://doi.org/10.1002/smll.202503406
motor: Europe PMC / PMC (PMC12934390)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: ["SEI se descompone 80–120°C", "4 tipos de abuso (térmico/eléctrico/mecánico/electroquímico)"]
fecha_registro: 2026-07-14
proyectos:
  - lipigas
---

## Pregunta / objetivo de investigación
Sistematizar el estado del arte en seguridad de baterías Li-ion para EV: mecanismos de fallo, causas raíz de la fuga térmica, y estrategias de mitigación y detección a nivel de material, sistema y diagnóstico.

## Hipótesis
La seguridad requiere un abordaje multinivel (materiales intrínsecamente seguros + gestión térmica + BMS + detección predictiva), no una sola contramedida.

## Metodología
- **Diseño:** revisión sistemática de literatura, estructurada en cuatro secciones (principios y mecanismos de fallo; causas raíz de TR; tipos de falla, mantenimiento y soluciones; perspectivas futuras).

## Resultados principales
- Cuatro categorías de abuso que disparan la fuga térmica: térmico, eléctrico (sobrecarga/descarga/cortocircuito), mecánico (aplastamiento/penetración) y electroquímico.
- "SEI decomposition accelerates irreversibly above 80–120 °C, triggering exothermic reactions (e.g., anode–electrolyte interactions)" — ventana química de inicio.
- Mitigación por nivel: materiales (electrolitos ignífugos, separadores con apagado térmico, cátodos dopados); sistema (BTMS, BMS con monitoreo en tiempo real, barreras aislantes); detección (ML sobre datos de sensores para predecir fallas y estimar RUL / vida útil remanente).
- "Machine learning techniques analyze vast sensor datasets to predict failures, estimate remaining useful life (RUL), and identify safety hazards like internal short circuits."

## Conclusiones
La seguridad de baterías EV exige colaboración industria-academia-reguladores; brechas: protocolos de emergencia estandarizados globalmente, armonización normativa, escalabilidad de estado sólido, y gemelos digitales impulsados por IA.

## Limitaciones
Revisión cualitativa; no aporta estadísticas propias de incidentes (referencia informe NTSB 2020 sin cifras).

## Relevancia / brecha para el estado del arte
Marco ordenador del eje seguridad para Lipigas: mapea las tres capas de contramedidas (materiales/sistema/detección) que la cliente menciona genéricamente (contención, sensores, monitoreo celda a celda, mantenimiento preventivo). Sustenta la línea base de conocimiento del piloto.

> Relaciones con otras fichas → `../../indice.json`.
