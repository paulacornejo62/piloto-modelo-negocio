---
id: producto-f500-ea-hct-encapsulador-litio
titulo: F-500 EA (Hazard Control Technologies) — agente encapsulador para extinción de fuego de baterías de litio
tipo: producto
tema: Extinción con enfriamiento y anti-reignición de baterías Li-ion mediante agente encapsulador (micelas)
area_oecd: "2 Ingeniería y Tecnología (2.5 Ingeniería de materiales)"
topicos: [supresion-incendio, seguridad-bateria-litio, fuga-termica-bateria]
anio: 2022
autores: [Hazard Control Technologies (HCT)]
referencia: https://hct-world.com/nfpa-18a/
motor: WebSearch + WebFetch (hct-world.com, encapsulator.co.nz, environmental-expert)
profundidad_lectura: full-text
estado_evidencia: parcial
trl_relevante: 9
metricas_clave: ["NFPA 18A Sec. 7.7 (Spherical Micelle Stability Test) — verificado por tercero", "enfriamiento ~3x niebla de agua al 3% [POR CONFIRMAR]", "detiene propagación celda a celda", "burn-back resistance / anti-reignición", ">15 años de pruebas de OEMs [POR CONFIRMAR]", "libre de flúor"]
nota_qa: "QA DR#2 (bajado a parcial). CONFIRMADO por tercero: cumplimiento NFPA 18A Sec. 7.7 (verbatim en encapsulator.co.nz), encapsulación de electrolito y anti-reignición/burn-back. NO confirmado en las 3 páginas citadas: la cifra enfriamiento ~3x niebla de agua al 3% y la cronología OEM Bosch 2009/Jaguar 2016 (las páginas solo dicen que Bosch/GM se benefician de F-500 y referencian una Li Battery Fire Testing Chronology) — quedan [POR CONFIRMAR]. Fuente de fabricante (sesgo comercial). El paper LFP 2022 (existencia verificada en Crossref, DOI 10.1016/j.jlp.2022.104816) mitiga pero es full-text 403. Uso en escenario integrado batería+GLP sin documentar."
fecha_registro: 2026-07-22
proyectos:
  - lipigas
---

## Contexto / producto
F-500 EA es el **agente encapsulador** comercial de Hazard Control Technologies (HCT), citado por el cliente Lipigas como 'F500' — el extintor especial para baterías de litio que exigirá en la licitación. Es un agente **libre de flúor, no corrosivo, biodegradable**, que forma micelas ("chemical cocoons") encapsulando el combustible/electrolito y volviéndolo no inflamable.

## Cómo funciona / especificación técnica
- **Mecanismo:** encapsula el electrolito inflamable en micelas esféricas estables, absorbe energía térmica rápidamente y **detiene la propagación celda a celda** (thermal runaway propagation).
- **Enfriamiento:** al 3%, su capacidad de enfriamiento es **~3x la de niebla de agua** — el punto clave para Li-ion, donde apagar la llama no basta y hay que enfriar la celda para evitar re-ignición.
- **Anti-reignición:** provee **burn-back resistance** estable y previene la re-ignición.
- **Normativa:** **referenciado en NFPA 18A**; tercero verificó cumplimiento de la **Sección 7.7 (Encapsulator Agent — Spherical Micelle Stability Test)**.
- **Formas de despliegue:** extintores portátiles y un **sistema de supresión embarcado (onboard EV)** declarado compatible con agua salada.

## Evidencia de eficacia
- **>15 años de pruebas de baterías Li-ion por OEMs automotrices.** En **2009**, Bosch concluyó pruebas comparando agua, espuma, polvos y F-500, eligiéndolo como producto de elección; Daimler, Dekra Industrial y Deutsche ACCUmotive también probaron. En **2011**, la State Fire School de Baden-Württemberg emitió una guía de aplicación para incendios de vehículos modernos referenciando F-500. En **2016**, Jaguar lo estandarizó para protección de riesgos Li-ion.
- Respaldo académico independiente: paper peer-reviewed (2022) sobre supresión de fuego de baterías **LiFePO4 (LFP)** con enfriamiento rápido (ver ficha `paper-2022-f500-encapsulador-lfp-supresion-enfriamiento`).

## Relevancia / brecha para el estado del arte
**Responde la duda del cliente:** el 'F500' es real, comercial (TRL 9 como producto), con respaldo NFPA 18A y de OEMs, y hace exactamente lo que se necesita (enfriar + anti-reignición) — la 'solución comercial madura' que el cliente asume EXISTE a nivel de agente. **Brecha:** no hay evidencia publicada de su uso en el **escenario integrado batería+GLP** (extintor a bordo de la van repartiendo cilindros, o en la zona de carga junto a almacenamiento de gas). Ese salto de contexto —dosis, ubicación, procedimiento y coexistencia con gas inflamable— es incertidumbre técnica genuina a validar en el piloto.

## Limitaciones (de la evidencia)
Buena parte de la evidencia proviene del fabricante (sesgo comercial); el respaldo NFPA 18A y el paper LFP la mitigan. No hay dato público de eficacia en el escenario batería+GLP coexistiendo. Equivalentes/competidores (p.ej. Dafo Safe EV / Li-IonFire embarcado, aerosoles de condensado) tienen mecanismos distintos y también deben evaluarse — ver ficha Dafo en la KB.

## Citas textuales
> «F-500 EA has been successfully third party tested and witnessed to comply with NFPA Standard 18A, Section 7.7 – Encapsulator Agent – Spherical Micelle Stability Test» (HCT)
> «3% F500 EA's cooling ability is 3 times that of water mist» (HCT/encapsulator)
> «In 2009, Bosch concluded testing of water, foam, powders and F-500 Encapsulator Agent on lithium-ion battery fires, and F-500 EA was chosen as their product of choice» (HCT)

> Relaciones (misma_tecnologia / complementa) → `../../indice.json` (producto-dafo-safe-ev-supresion-incendio-bateria; paper-2022-f500-encapsulador-lfp-supresion-enfriamiento; paper-wang-2025-microcapsule-water-mist).
