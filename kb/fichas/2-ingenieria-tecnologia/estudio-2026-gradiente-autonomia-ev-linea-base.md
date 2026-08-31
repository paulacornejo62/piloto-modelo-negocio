---
id: estudio-2026-gradiente-autonomia-ev-linea-base
titulo: Línea base de autonomía real de VE con carga y pendiente (MDPI Vehicles 2026 + datos de flota payload/pendiente)
tipo: paper
tema: Degradación de autonomía de vehículos eléctricos por pendiente (gradiente) y por carga (payload) — referencia para última milla
area_oecd: "2 Ingeniería y Tecnología (2.3 Ingeniería mecánica)"
topicos: [autonomia-degradacion-ev, electromovilidad-vehiculo-comercial, electromovilidad-reparto-glp]
anio: 2026
autores: ["[MDPI Vehicles 8(3):44, autores POR CONFIRMAR]", "Oeko-Institut (BEV trucks Germany)"]
referencia: https://www.mdpi.com/2624-8921/8/3/44
motor: WebSearch (MDPI resumen; WebFetch 403) + WebSearch (OVL/Auto Capital fleet guides; oeko.de)
profundidad_lectura: abstract
estado_evidencia: parcial
trl_relevante: "-"
metricas_clave: [">62% reducción de rango en tramo sostenido a 4% de pendiente", "+17% consumo a velocidad urbana constante a 4%", "3-5% pérdida de rango por cada 100 kg de carga", "eSprinter 113 kWh: -31% con +1.200 kg", "BEV trucks DE: 0,96 kWh/km; 92→346 Wh/km a 50 km/h de 0% a 4%"]
nota_qa: "Cifras del MDPI y del real-world alemán obtenidas de resúmenes indexados (WebFetch 403 en ambos PDFs). Payload de fleet guides secundarias. TODO marcado 'parcial'. El estudio MDPI es sobre un Tesla (pasajeros), NO N1/van con carga — transferir con cautela."
fecha_registro: 2026-07-22
proyectos:
  - lipigas
---

## Pregunta / objetivo de investigación
Establecer una **referencia de orden de magnitud** para la degradación de la autonomía real de un VE de reparto por dos factores clave de la última milla de cilindros: la **pendiente/topografía** y la **carga (payload ~1 t)**. Sirve para dimensionar el objetivo SMART de autonomía del piloto Lipigas ante la ausencia de línea base chilena.

## Hipótesis
El gradiente y la carga reducen materialmente la autonomía real; en topografía urbana con pendientes y ~1 t de cilindros, la autonomía útil puede quedar muy por debajo de la declarada por fabricantes.

## Metodología
- **MDPI Vehicles 2026 ('Influence of Road Gradient Resistance on the Driving Range of EVs'):** banco dinamométrico + simulación Simulink sobre un VE (Tesla, pasajeros). Rampas de 0%, 2%, 3%, 4%; rango definido por descarga de batería de 80% a 10% SoC.
- **Real-world alemán (Oeko-Institut):** 19 camiones BEV, datos sep-2023 a ene-2025, distintas regiones.
- **Payload:** guías de flota (OVL/Auto Capital) y ejemplo eSprinter 113 kWh.

## Resultados principales
- **Pendiente (MDPI):** relación inversa fuerte gradiente-rango, **>62% de reducción en tramo SOSTENIDO a 4%**; pero el efecto NETO casi se cancela en pendientes moderadas por recuperación en bajada, sobre todo a alta velocidad. **A velocidad urbana constante, el gradiente sí pesa: +17% de consumo a 4%.**
- **Carga (payload):** regla ~**3-5% de pérdida de rango por cada 100 kg**; ejemplo **eSprinter 113 kWh: +1.200 kg reduce el rango de ~260 a ~180 millas (~31%)**.
- **Real-world BEV trucks (DE):** consumo promedio **0,96 kWh/km**; subida a 50 km/h de **~92 Wh/km (0%) a ~346 Wh/km (4%)**.

## Conclusiones
En última milla urbana con pendientes, la topografía castiga el consumo (hasta +17% a 4% a velocidad urbana), mientras que en rutas con subida/bajada balanceada el regen amortigua parte del efecto. La carga cercana a 1 t es un factor de primer orden (−3 a −5%/100 kg). Ambos factores juntos justifican medir la autonomía útil real en el propio piloto.

## Limitaciones
El estudio de gradiente es sobre un vehículo de pasajeros (Tesla), no un N1/clase B con carga; los datos de payload y real-world son de vehículos mayores/distintos y de mercados no chilenos (UE/US). **NO existe línea base publicada para camioneta clase B/N1 con ~1 t de cilindros en topografía y clima de Chile** — vacío confirmado. Cifras obtenidas de resúmenes (full-text 403), estado 'parcial'.

## Relevancia / brecha para el estado del arte
Da a Lipigas un **rango de referencia** para fijar el objetivo SMART de autonomía (rutas 70-80 km/día; diseño 100 km/día útiles; fabricantes 130-140), y a la vez **documenta el vacío**: la autonomía útil real con carga de cilindros en rutas chilenas es incertidumbre técnica genuina a medir en el piloto — insumo directo de la novedad Ley I+D. Complementa `informe-nrel-2016-md-electric-delivery-trucks` y `paper-ghosh-2025-cold-weather-ev-fleets` (degradación por clima frío) ya en la KB.

> Relaciones (complementa) → `../../indice.json` (informe-nrel-2016-md-electric-delivery-trucks; paper-ghosh-2025-cold-weather-ev-fleets).
