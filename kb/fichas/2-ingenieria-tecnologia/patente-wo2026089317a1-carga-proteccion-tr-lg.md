---
id: patente-wo2026089317a1-carga-proteccion-tr-lg
titulo: "Charging station, battery protection apparatus, and battery protection method — WO2026089317A1 (LG Energy Solution)"
tipo: patente
tema: Estacion de carga que prohibe la carga y descarga el pack cuando un bloque de bateria del EV esta en riesgo de fuga termica
area_oecd: "2 Ingenieria y Tecnologia (2.2 Ingenieria electrica, electronica)"
ipc: [H02J7/00]
topicos: [carga-inteligente-autodesconexion, carga-nocturna, deteccion-temprana-fuga-termica, electromovilidad-carga-peligrosa]
anio: 2024
titular: LG Energy Solution Ltd
referencia: WO2026089317A1
motor: Google Patents
profundidad_lectura: full-text
estado_evidencia: verificado
estado_legal: solicitud
jurisdicciones: [WO, KR]
fecha_prioridad: 2024-10-22
trl_relevante: 4
fecha_registro: 2026-07-22
proyectos:
  - lipigas
---

## Problema tecnico que resuelve
Un EV conectado mucho tiempo a una estacion de carga eleva la probabilidad de sobrecarga, causa reconocida de incendio de bateria; y la fuga termica de un bloque puede propagarse ("thermal propagation") a los bloques adyacentes en el pack. Busca proteger el pack del riesgo de incendio durante la carga.

## Reivindicaciones clave (qué protege)
Estacion de carga con un cargador, un descargador conectado por lineas de potencia de estacion, y un controlador de estacion que PROHIBE la operacion de carga cuando al menos uno de los multiples bloques de bateria del pack del EV tiene riesgo de fuga termica; y ejecuta una operacion de DESCARGA del descargador cuando la carga queda prohibida. El controlador selecciona cada bloque en riesgo como objetivo de descarga, transmite su identificacion al EV, y ordena la descarga tras recibir del EV una señal de "descarga lista" (camino de descarga formado). Determina la corriente de descarga objetivo segun el desempeño del descargador y el voltaje de linea.

## Solución técnica (cómo lo hace)
Integracion cargador <-> vehiculo (BMS): la estacion no solo corta la carga ante riesgo de TR, sino que participa activamente descargando los bloques en riesgo por bloque, coordinada con el EV mediante intercambio de identificacion de bloque y señalizacion de disponibilidad.

## Alcance y limitaciones
Solicitud PCT/coreana PENDIENTE (prioridad 2024-10-22, publicada 2026-04-30, status Pending). No hay producto comercial derivado documentado. No aborda el contexto de un vehiculo que porta un peligro externo (GLP): protege el pack, no un almacenamiento adyacente. Requiere BMS del EV cooperativo (acceso bloque a bloque), supuesto no garantizado con packs cerrados.

## Relevancia FTO / novedad
Es la fuente mas cercana al tema 2 (carga inteligente con autodesconexion por precursor de fuga termica). Prueba que la industria (LG) esta PATENTANDO justo ahora el corte de carga por riesgo de TR — la ventana de novedad del mecanismo generico se esta cerrando. Para Lipigas, el diferenciador defendible NO es abortar la carga (esto ya se solicita), sino la INTEGRACION validada en el contexto dual bateria+GLP bajo normativa chilena (DS108/RIC15), la autodesconexion nocturna con vehiculo dormido y la proteccion de la jaula de cilindros adyacente. Revisar si entra a fase nacional en Chile (no verificado).

> Relaciones: complementa a paper-cheng-2025-early-warning-charging (deteccion en el punto de carga) y patente-cn113036250b (monitoreo con vehiculo dormido). Ver `../../indice.json`.
