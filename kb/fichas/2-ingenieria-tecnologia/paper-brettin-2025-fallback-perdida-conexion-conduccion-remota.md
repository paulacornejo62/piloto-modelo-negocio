---
id: paper-brettin-2025-fallback-perdida-conexion-conduccion-remota
titulo: "Safety Blind Spot in Remote Driving: Considerations for Risk Assessment of Connection Loss Fallback Strategies (Brettin, Braun, Graubohm & Maurer 2025)"
tipo: preprint
tema: Riesgo de las estrategias de fallback ante pérdida de conexión en conducción remota
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [teleoperacion-fallback, conectividad-vehiculo-autonomo, operacion-mixta-seguridad, latencia-teleoperacion]
anio: 2025
autores: [Leon Johann Brettin, Niklas Braun, Robert Graubohm, Markus Maurer]
referencia: https://arxiv.org/abs/2502.10243
motor: WebSearch + arXiv PDF full-text (versión IEEE Access sometida, v1 14-02-2025)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "2-3 (análisis conceptual y simulación)"
metricas_clave: ["~186.000 escenarios simulados del dataset uniD", "tasa de colisión 8,06-8,74% con 1,0 s de reacción y frenado de emergencia naturalista (-3,41 m/s2)", "27,4-46,6% con 1,5 s", "49,0-73,1% con 2,0 s", "con desaceleración moderada (-1,71 m/s2): 1,13% a 1,0 s y 6,2-7,2% a 1,5 s"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
  - kaufmann-telecomando
---

## Pregunta / objetivo de investigación
Cuestionar si la estrategia estándar de fallback ante pérdida de conexión en conducción remota (frenar hasta detenerse de inmediato) es aceptable desde el punto de vista de riesgo.

## Hipótesis
La detención inmediata ante pérdida de enlace, asumida como decisión segura por defecto, puede constituir un peligro relevante para SOTIF y no está suficientemente analizada en las evaluaciones de seguridad.

## Metodología
- **Diseño:** análisis de riesgo (ISO 26262: probabilidad x severidad; discusión de severidad con ISO 21448/SOTIF) + simulación longitudinal 1D.
- **Datos / muestra:** dataset naturalista uniD (grabaciones con dron de vía urbana recta); ~186.000 pares vehículo-seguidor preprocesados.
- **Técnicas:** dos modelos de conductor seguidor (Intelligent Driver Model de Treiber y "sudden braking model"); pérdida de conexión del vehículo líder al inicio del escenario; barrido de tiempos de reacción (0 a 2,5 s) y de desaceleración (-3,41 y -1,71 m/s2).
- **Métricas:** tasa de colisión = escenarios con colisión / total simulado.

## Resultados principales (full-text)
- Con **frenado de emergencia naturalista (-3,41 m/s2)** del vehículo teleoperado tras perder el enlace, la tasa de colisión por alcance del vehículo que lo sigue crece rápido con el tiempo de reacción del conductor humano: 0,92% (0,5 s), 8,06-8,74% (1,0 s), 27,4-46,6% (1,5 s), 49,0-73,1% (2,0 s), 65,1-86,1% (2,5 s).
- Con **desaceleración moderada (-1,71 m/s2)** las tasas caen fuertemente (0,01% a 0,5 s; 1,13% a 1,0 s; 6,2-7,2% a 1,5 s), a costa de una distancia de detención mayor.
- Argumento clave: el conductor humano que sigue **no puede anticipar** la pérdida de enlace ("A human operating the closely following remote-driven vehicle has no chance to anticipate the situation"), a diferencia de un frenado por causa visible.
- Discuten y descartan apoyarse en ADAS de nivel 1-2 como fallback: "Level 1 or Level 2 features cannot be used as a safe fallback either", porque están diseñados para un conductor que supervisa.
- Revisan las alternativas de la literatura: **free corridor** (TU Múnich) — mantener libre un pasillo por delante para poder detenerse — y señalan su problema abierto: si el corredor es largo el operador conduce lento o no logra mantenerlo libre; si es corto, hay que frenar casi al máximo y reaparece el riesgo de alcance.

## Conclusiones
Se requiere evaluación rigurosa de alternativas al "stop inmediato" como fallback de pérdida de conexión (p.ej. maniobra mínima de riesgo con degradación controlada).

## Limitaciones
- Simulación puramente longitudinal (1D) sobre un tramo urbano recto del dataset uniD; sin dinámica lateral ni peatones en el lazo.
- Los parámetros de desaceleración y de tiempo de reacción son supuestos de literatura y los propios autores los declaran discutibles.
- Escenario urbano de vía pública: en recinto privado con tráfico controlado el riesgo residual es menor, pero el argumento metodológico (el fallback debe diseñarse y evaluarse, no asumirse) se mantiene.

## Relevancia / brecha para el estado del arte
Fundamenta que el **fallback ante pérdida de señal es un objeto de diseño e investigación**, no un parámetro de configuración. Directamente aplicable a la incertidumbre declarada por el cliente (conectividad continua) y a la definición de comportamiento seguro del vehículo en zonas de sombra del recinto.

**Citas textuales:**
- "Simulation results from hundreds of scenarios based on naturalistic traffic scenes indicate high collision rates for any immediate substantial deceleration to a standstill."
- "Such a fallback strategy can result in a SOTIF relevant hazard, making it questionable whether such a design decision can be considered acceptable."

> Relaciones con otras fichas → `../../indice.json`.
