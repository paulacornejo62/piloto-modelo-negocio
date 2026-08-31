---
id: informe-nrel-2016-md-electric-delivery-trucks
titulo: "Field Evaluation of Medium-Duty Plug-in Electric Delivery Trucks (Prohaska et al., NREL 2017)"
tipo: paper
tema: Evaluación en terreno de camiones eléctricos de reparto medium-duty (flota Frito-Lay, Smith Newton)
area_oecd: "2 Ingeniería y Tecnología (2.3 Ingeniería mecánica)"
topicos: [autonomia-degradacion-ev, electromovilidad-vehiculo-comercial, carga-nocturna]
anio: 2017
autores: [Robert Prohaska, Mike Simpson, Adam Ragatz, Kenneth Kelly, Kandler Smith, Kevin Walkowicz]
referencia: https://docs.nrel.gov/docs/fy17osti/66382.pdf (NREL/TP-5400-66382, 2017)
motor: WebSearch + PDF NREL (literatura gris, informe técnico)
profundidad_lectura: full-text
estado_evidencia: parcial
trl_relevante: 8
metricas_clave: ["+216% (3.15x) economía equivalente: 24.09 vs 7.63 MPGe", "-46% CO2e", "<40 mi/día", "~1.5 h conducción/día", "pack 80 kWh LiFePO4"]
nota_qa: "QA EVAL_P2: informe correctamente identificado (titulo/autores Prohaska/N° 66382), pero URL del expediente estaba mal (fy16osti/66755 -> fy17osti/66382) y anio es 2017. Dominio NREL no accesible en el entorno QA: full-text no reabierto, cifras exactas (216%, 24.09/7.63 MPGe, -46% CO2e, 80 kWh LiFePO4) sin verificar. Baja a parcial."
fecha_registro: 2026-07-14
proyectos:
  - lipigas
---

## Pregunta / objetivo de investigación
Caracterizar el desempeño en uso real de camiones eléctricos de reparto medium-duty (Smith Newton) frente a diésel convencionales en la misma flota y rutas, incluyendo consumo, emisiones e infraestructura de carga.

## Hipótesis
Los EV medium-duty son adecuados para ciclos de reparto urbano de retorno a depósito, con ganancias de eficiencia y emisiones, si la tecnología se ajusta al ciclo de trabajo.

## Metodología
- **Diseño:** evaluación en terreno (in-use), >36,000 millas de datos.
- **Datos:** vehículos Smith Newton (pack 80 kWh LiFePO4) en el centro de distribución de Frito-Lay en Federal Way, Washington; diésel comparables en rutas similares; 10 cargadores instrumentados + medidor en la acometida.

## Resultados principales
- Mejora de +216% (3.15x) en economía de combustible equivalente: 24.09 MPGe (EV) vs 7.63 MPG (diésel); -46% en emisiones CO2e según matriz local.
- Distancia diaria promedio <40 millas; ~1.5 h de conducción por día (los choferes también surten cuentas en ruta).
- La carga coincidió con el pico de demanda de la instalación (subió el peak ~70→110 kW); los cargos por demanda en el Pacífico Noroeste fueron bajos, sin justificar solar in situ ni carga gestionada en ese sitio.

## Conclusiones
El EV medium-duty rinde bien en ciclos de reparto urbano de baja distancia diaria; la clave es hacer coincidir la tecnología con el ciclo de trabajo (duty cycle).

## Limitaciones
Vehículos de generación temprana (Smith); clima del Pacífico Noroeste (no aplica directamente calor/altura de Chile); reparto de snacks, no carga peligrosa.

## Relevancia / brecha para el estado del arte
Referente real de electrificación de flota de reparto medium-duty: valida que rutas urbanas de retorno a depósito (<40 mi/día, ~1.5 h) son el caso favorable, coherente con el foco de última milla de Lipigas. Aporta cifras de eficiencia y el hallazgo de que la carga puede elevar el peak de la instalación (relevante para su carga nocturna).

> Relaciones con otras fichas → `../../indice.json`.
