---
id: paper-tazaki-2025-display-predictivo-tractor-remolque
titulo: "Remote Driving of Tractor-Trailer Vehicles Based on Predictive Display (Tazaki, Takeda, Nagano, Yokokohji & Kameoka 2025)"
tipo: paper
tema: Compensación de latencia mediante display predictivo en la conducción remota de vehículos articulados tractor-remolque
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [latencia-teleoperacion, teleoperacion-supervision-remota, factores-humanos-operador-remoto]
anio: 2025
autores: [Yuichi Tazaki, Yuki Takeda, Hikaru Nagano, Yasuyoshi Yokokohji, Shota Kameoka]
referencia: https://www.fujipress.jp/jrm/rb/robot003700051195/ (Journal of Robotics and Mechatronics 37(5):1195, DOI 10.20965/jrm.2025.p1195)
motor: WebSearch + WebFetch (página del editor: resumen y metadatos; texto completo no accedido)
profundidad_lectura: abstract
estado_evidencia: parcial
trl_relevante: "4 (prototipo con operadores humanos en tarea simulada de transporte)"
metricas_clave: ["display predictivo superpuesto en wireframe sobre video retardado", "visualización en head-mounted display", "mejora reportada de eficiencia y seguridad en la tarea (magnitudes no verificadas)"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Pregunta / objetivo de investigación
¿Puede un display predictivo compensar el retardo de comunicación en la conducción remota de un **vehículo articulado tractor-remolque**, donde la dinámica (especialmente en retroceso) es difícil de anticipar?

## Hipótesis
Superponer la trayectoria predicha del conjunto tractor-remolque sobre el video retardado permite al operador anticipar la respuesta del vehículo y mejorar desempeño y seguridad.

## Metodología
- **Diseño:** desarrollo de sistema + ensayo con operadores humanos en tarea de transporte (según resumen del editor).
- **Técnicas:** modelo de predicción de la trayectoria del vehículo articulado; visualización en wireframe superpuesta al video con retardo, presentada en un head-mounted display.

## Resultados principales
- El display predictivo mejoró de forma significativa eficiencia y seguridad en la tarea de transporte, compensando el retardo de transmisión (según el resumen; magnitudes no verificadas).
- Cita del resumen: "Predictive display helps the driver to compensate for delayed response".

## Conclusiones
La visualización de la trayectoria predicha es una estrategia efectiva para operar remotamente vehículos articulados con retardo.

## Limitaciones
- **Solo se accedió al resumen y metadatos del editor** (texto completo de pago): no se verificaron latencias probadas, número de participantes ni magnitudes de mejora.
- Vehículo articulado en tarea de transporte controlada, no camión minero en faena.

## Relevancia / brecha para el estado del arte
Muestra que la compensación de latencia para **vehículos articulados pesados** sigue siendo objeto de investigación activa en 2025 — es decir, la dinámica del vehículo pesado impone requisitos de interfaz que no se resuelven con el paquete de telecomando de fábrica. Contrasta con [[paper-musicant-2026-predictive-display-teledriving]], que no halló beneficio del display predictivo a 150 ms en auto liviano: la utilidad depende del retardo y de la dinámica del vehículo.

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
