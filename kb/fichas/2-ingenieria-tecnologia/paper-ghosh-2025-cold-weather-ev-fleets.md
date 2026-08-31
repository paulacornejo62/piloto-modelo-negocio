---
id: paper-ghosh-2025-cold-weather-ev-fleets
titulo: "From Range Loss to Recovery — Cold Weather Challenges and Design Strategies for Commercial EV Fleets (Ghosh et al. 2025)"
tipo: preprint
tema: Degradación de autonomía real de flotas EV comerciales por clima frío y estrategias de mitigación
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [autonomia-degradacion-ev, electromovilidad-vehiculo-comercial, carga-nocturna]
anio: 2025
autores: [Soham Ghosh, Arpit Bohra, Karthik Saikumar]
referencia: "arXiv/IEEE SEGE 2025 (preprint aceptado) DOI 10.1109/SEGE65970.2025.11203550"
motor: WebSearch + PDF (preprint IEEE SEGE)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 3
metricas_clave: ["pérdida eficiencia 10–35% en frío severo (-10°F)", "SoC se estanca ~80% en subzero", "resistencia interna x5 de 113°F a 10°F", "China ~60% ventas EV globales"]
fecha_registro: 2026-07-14
proyectos:
  - lipigas
---

## Pregunta / objetivo de investigación
Cuantificar la degradación de desempeño de flotas EV comerciales bajo frío extremo (25°F a -25°F) y proponer estrategias de diseño (swapping con seguridad integrada; carga híbrida ruta+depósito).

## Hipótesis
El frío degrada autonomía, eficiencia y tiempos de carga de forma marcada en vehículos comerciales (ciclos de trabajo distintos a los de pasajeros), exigiendo estrategias de "hardening" específicas.

## Metodología
- **Diseño:** análisis con simulaciones Monte Carlo sobre parámetros de flota reales (flota nacional EE.UU. de 28,200 EV comerciales, 5.9 GWh) + datos experimentales de SoC vs. temperatura.

## Resultados principales
- Pérdidas de eficiencia estocásticas: 0–15% en frío promedio (25.9°F) y 10–35% en frío severo (-10°F); demanda diaria de flota +~20% (1.22→1.47 GWh media).
- A subzero, la batería suele quedar en 80–85% de SoC (no alcanza 100%); resistencia interna hasta 5x de 113°F a 10°F (cita a Chacko y Chung).
- Contexto: China ~60% de ventas EV globales; buses EV, camiones y vans urbanas last-mile (80–150 mi, 40–80 kWh) como categoría de baja-moderada sensibilidad de carga útil.
- Bombas de calor más efectivas que calefacción resistiva sobre 10°F; a -10°F el clima de cabina puede consumir ~53% de la potencia del vehículo.

## Conclusiones
El frío es una barrera operativa mayor; se proponen swapping con "design-integrated safety" (contención de fuga térmica) y carga híbrida para sostener utilización sin sacrificar autonomía.

## Limitaciones
Preprint (no editado final); foco en clima frío norteamericano — Chile costero/urbano es menos extremo, pero el mecanismo (autonomía real < nominal, SoC cap) es transferible; la carga en cerros/altura de Lipigas es otro factor no cubierto.

## Relevancia / brecha para el estado del arte
Aporta a la incertidumbre (4) de Lipigas: autonomía y tiempos de carga reales vs. nominales. Cuantifica que el SoC útil real puede quedar en 80% y que la eficiencia cae por condiciones ambientales — clave para dimensionar el piloto (los ~100 km nominales pueden no cumplirse). La carga entre 20–80% que menciona la cliente coincide con la ventana práctica de SoC.

> Relaciones con otras fichas → `../../indice.json`.
