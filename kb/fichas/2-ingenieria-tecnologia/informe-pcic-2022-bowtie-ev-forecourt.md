---
id: informe-pcic-2022-bowtie-ev-forecourt
titulo: "Risk Management of Electric Vehicle Charging on Fuel Forecourts and Enclosed Car Parks (PCIC Europe EUR22_04)"
tipo: informe
tema: Metodología bow-tie / QRA para gestionar el riesgo de carga de VE junto a combustibles y en espacios confinados
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica y electrónica)"
topicos: [carga-cerca-inflamables, normativa-carga-ev-atmosfera-explosiva, seguridad-bateria-litio, carga-nocturna]
anio: 2022
autores: [PCIC Europe]
referencia: https://pcic.energy/wp-content/uploads/EUR22_04.pdf
motor: WebSearch + WebFetch (PDF, full-text) — pcic.energy
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 7
metricas_clave: ["bow-tie (Swiss Cheese, causas + árbol de eventos)", "EVSE = fuente de ignición en áreas peligrosas", "carga 7-20 kW hogar a ultra-rápida en forecourt"]
fecha_registro: 2026-07-22
proyectos:
  - lipigas
---

## Pregunta / objetivo de investigación
Cómo representar y gestionar el riesgo de un incendio de batería Li-ion durante la carga de VE cuando ésta ocurre en estaciones de servicio (forecourts) con combustibles y en estacionamientos cerrados, entornos donde el riesgo "ha sido pobremente entendido por la industria".

## Metodología
- **Modelo bow-tie** (corbatín) adoptado de la industria petroquímica: lado izquierdo = cadenas causales (Swiss Cheese, James Reason); lado derecho = pensamiento de árbol de eventos (event tree). Representa las barreras preventivas y mitigadoras y su "salud".
- Aplicado a la falla e ignición de una celda Li-ion en un cargador (EVSE, EVC) sobre forecourt y en car park cerrado.

## Resultados principales
- "Hydrocarbon re-fuelling activities on forecourts create hazardous areas within which the use of non-rated electrical equipment is restricted." — el EVSE debe considerarse frente a áreas peligrosas existentes; su ubicación y clasificación importan.
- "The failure and subsequent ignition of a Li-ion battery will cause a risk event. Flammable fuels, e.g. a forecourt fuels spillage, will contribute to this risk event." — cruce explícito batería + combustible inflamable.
- Recomienda un checklist de sitio: acceso, flujo de tráfico, consideraciones de área peligrosa, opciones de suministro eléctrico, riesgo de incendio y mitigaciones.
- Para diseños de forecourt: "ensure designers are experienced in hazardous areas management and incorporate these into the design of the equipment and site."

## Conclusiones
El bow-tie/QRA es el método establecido para el cruce carga-VE ↔ atmósfera/combustible inflamable; convierte el análisis de riesgo transversal (que Lipigas ya está haciendo) en una herramienta trazable de barreras.

## Limitaciones
Enfocado en forecourts y car parks cerrados (no en depósitos logísticos de GLP con cilindros); no entrega una distancia de separación numérica (esa la aportan las guías aseguradoras/FM Global).

## Relevancia / brecha para el estado del arte
Provee el ANDAMIAJE METODOLÓGICO (bow-tie + árbol de eventos + gestión de áreas peligrosas para EVSE) que Lipigas necesita para zonificar local a local. Confirma que el problema "carga EV junto a inflamable" ya tiene método de análisis, pero no una solución de diseño estándar para depósitos pequeños de GLP.

> Relaciones con otras fichas → `../../indice.json`.
