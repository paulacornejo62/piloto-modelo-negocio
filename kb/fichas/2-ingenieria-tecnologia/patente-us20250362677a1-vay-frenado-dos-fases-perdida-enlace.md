---
id: patente-us20250362677a1-vay-frenado-dos-fases-perdida-enlace
titulo: "Phased minimum risk maneuver for teleoperated vehicles — US20250362677A1 / EP4191357A1 (Vay Technology GmbH)"
tipo: patente
tema: Maniobra de riesgo mínimo por fases (frenado suave y luego frenado fuerte) ante perturbación de la red en un vehículo teleoperado
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [B60W60/00, G05D1/0022]
topicos: [teleoperacion-fallback, teleoperacion-supervision-remota, requisitos-red-latencia-jitter]
anio: 2021
titular: Vay Technology GmbH
referencia: US20250362677A1 (familia: EP4191357A1, US12578720B2)
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: solicitud (continuación; matriz concedida en US)
jurisdicciones: [US, EP]
fecha_prioridad: 2021-12-03
trl_relevante: 8-9
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Problema técnico que resuelve
Qué hace el vehículo teleoperado cuando la red se degrada (picos de latencia celular). La detención inmediata y brusca es insegura en tráfico; no reaccionar es inaceptable.

## Reivindicaciones clave (qué protege)
Claim 1 (síntesis verificada): método de control de un vehículo teleoperado que (i) conduce vía estación de teleoperador, (ii) **detecta una perturbación de red**, (iii) inicia un **primer frenado suave**, y (iv) activa un **segundo frenado fuerte** si la red no se recupera.

Cita textual:
> "a two-phase emergency braking solution, preferably comprising a first phase and a second phase. In the first phase a gentle brake is performed and then, if needed, a harsh brake is performed in the second phase forcing said vehicle to stop."

## Solución técnica (cómo lo hace)
Ventana de gracia temporizada (del orden de cientos de milisegundos según la descripción) entre detección de la caída del enlace y la parada forzada, escalando la severidad de la desaceleración.

## Alcance y limitaciones
- Dominio declarado: movilidad compartida en vía pública, no minería.
- La solicitud US20250362677A1 es una continuación de 2025; la protección efectiva viene de EP4191357A1 y US12578720B2.
- Verificado: titular, fechas, cita del texto. Pliego completo no leído.

## Relevancia FTO / novedad
Define el estado del arte del **safe-stop escalonado por pérdida de enlace**, el mecanismo de seguridad central de cualquier telecomando. Un proyecto que proponga "si se cae el enlace, el camión frena" **no aporta novedad**. El espacio abierto está en la **maniobra de riesgo mínimo adecuada a faena minera** (pendiente, camión cargado de alto tonelaje, pista angosta, tráfico mixto con equipo manual), condiciones que estas familias no contemplan.

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
