---
id: paper-marquez-barja-2021-5g-blueprint-teleoperacion-logistica
titulo: "Enhanced Teleoperated Transport and Logistics: A 5G Cross-Border Use Case (Marquez-Barja et al. 2021)"
tipo: paper
tema: Arquitectura y requisitos de conectividad 5G para transporte y logística teleoperada (proyecto H2020 5G-Blueprint)
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [conectividad-vehiculo-autonomo, teleoperacion-fallback, v2i-iot-logistica]
anio: 2021
autores: [Johann M. Marquez-Barja, Seilendria Hadiwardoyo, Bart Lannoo, Wim Vandenberghe, Eric Kenis, Lauren Deckers, Maria Chiara Campodonico, Klaudia dos Santos, Rakshith Kusumakar, Matthijs Klepper, Joost Vandenbossche]
referencia: https://www.marquez-barja.com/images/papers/marquez-barja21-enhanced-author-version.pdf
motor: WebSearch + PDF full-text (versión de autor; proyecto H2020 nº 952189)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "5-7 (pilotos en puertos y corredores transfronterizos)"
metricas_clave: ["tiempo de reacción humano en cientos de ms", "latencia de red exigida un orden de magnitud menor: decenas de ms", "8 funciones habilitantes (EF1-EF8) definidas", "pilotos en Vlissingen, Amberes y Zelzate"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
  - kaufmann-telecomando
---

## Pregunta / objetivo de investigación
Definir, probar y validar una arquitectura técnica (y modelos de negocio/gobernanza) para transporte teleoperado ininterrumpido basado en 5G, en entornos logísticos reales (puertos, centros de distribución) y transfronterizos.

## Hipótesis
La teleoperación asistida por 5G puede cubrir la brecha entre conductor humano y autonomía plena en logística, siempre que la red garantice latencia y throughput con continuidad (incluido el handover), lo que 4G no permite.

## Metodología
- **Diseño:** proyecto de investigación aplicada con pilotos de campo (H2020 5G-Blueprint).
- **Casos de uso:** control automatizado de barcazas, docking con conductor en el lazo (driver-in-loop) en centros de distribución, platooning CACC, y remote take-over.
- **Sitios piloto:** Vlissingen, Amberes (área portuaria) y zona transfronteriza de Zelzate.
- **Funciones habilitantes:** ocho (EF1 EAD, EF2 VRU, EF3 iTLC, EF4 percepción distribuida, EF5 anticolisión activa, EF6 identificación de contenedor, EF7 ETA, EF8 analítica de escena).

## Resultados principales
- Requisito cuantitativo de latencia: la reacción humana está en el orden de cientos de ms, y la latencia de red debe ser **un orden de magnitud menor** (decenas de ms) para no degradar el desempeño del operador.
- El **handover** entre celdas/operadores es un problema abierto: el paper indica que el core 5G actual no soporta handover entre operadores y que hace falta diseñar y probar relaciones de handover.
- La **pérdida de conectividad detiene el vehículo**: sin conectividad no hay control, lo que sube el riesgo operacional y obliga a comprometer nivel de servicio de red.
- El sensor deprivation del teleoperador (no oír/sentir el entorno) introduce riesgo de seguridad nuevo respecto del conductor a bordo.

## Conclusiones
La teleoperación 5G es viable como paso intermedio hacia la autonomía en logística, pero exige garantías de desempeño de red (slicing), predicción de degradación y estrategias de mitigación antes de que la calidad caiga.

## Limitaciones
Enfocado en vía pública y vía navegable transfronteriza con redes públicas de MNO; no aborda redes privadas de recinto cerrado. Al momento del paper, resultados de pilotos aún no consolidados (paper de diseño/arquitectura, no de medición).

## Relevancia / brecha para el estado del arte
Aporta la evidencia central para el eje conectividad del caso Kaufmann: el requisito no es "tener señal", sino **garantía de desempeño y continuidad**, con predicción de degradación y mitigación preventiva; y declara explícito que sin conexión el vehículo se detiene. Sirve para argumentar que la capa de conectividad supervisada en un recinto no es integración trivial.

**Citas textuales:**
- "To not deteriorate the operator's performance, the latency of the network shall be one order of magnitude lower, i.e., in the range of tens of ms."
- "Focus is needed in i) providing performance guarantees (e.g. with 5G slicing), ii) predicting when the performance will get too poor such that preventive measures can be taken while maneuvering and how the performance guarantees can traverse the border to the other operator"
- "It may be clear that without proper connectivity, there is no control of the vehicle and the vehicle will be required to stop, herewith increasing the risk of accidents."
- "Existing 5G Core standards do not support handovers between operators at this moment."

> Relaciones con otras fichas → `../../indice.json`.
