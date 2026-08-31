---
id: patente-cn113036250b-monitoreo-fuga-termica-dormido-changan
titulo: "Power battery thermal runaway whole-time monitoring system — CN113036250B (Changan New Energy Automobile)"
tipo: patente
tema: Monitoreo de fuga termica de la bateria de traccion incluso con el vehiculo en estado dormido (relevante para carga/reposo nocturno)
area_oecd: "2 Ingenieria y Tecnologia (2.2 Ingenieria electrica, electronica e informatica)"
ipc: [H01M10/482, H01M10/48]
topicos: [fuga-termica-bateria, bms-monitoreo, carga-nocturna]
anio: 2021
titular: Chongqing Changan New Energy Automobile Technology Co., Ltd.
referencia: CN113036250B
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: vigente
jurisdicciones: [CN]
fecha_prioridad: 2021-02-27
trl_relevante: 6
fecha_registro: 2026-07-14
proyectos:
  - lipigas
---

## Problema tecnico que resuelve
Un BMS convencional no puede monitorear la fuga termica cuando el vehiculo esta en estado DORMIDO (apagado/reposo). Esto es critico durante la carga o el estacionamiento nocturno, justo el escenario de mayor preocupacion de Lipigas (vehiculos cargando de noche en un deposito con almacenamiento de GLP).

## Reivindicaciones clave (qué protege)
Sistema de monitoreo de fuga termica a tiempo completo con un DISPOSITIVO DE ADQUISICION conectado al BMS. El dispositivo: se auto-despierta periodicamente tras el reposo del BMS; adquiere temperatura y voltaje en tiempo real de cada celda; los compara con umbrales preestablecidos; si el voltaje de cualquier celda cae bajo su umbral y/o la temperatura supera su umbral, DESPIERTA al BMS. El BMS, tras despertar, monitorea la fuga termica por la tasa de subida de temperatura y la tasa de caida de voltaje.

## Solución técnica (cómo lo hace)
Agrega un modulo de adquisicion de bajo consumo que vigila la bateria mientras el BMS principal duerme, despertandolo solo ante indicios de anomalia. Garantiza vigilancia continua sin drenar la bateria, cubriendo el punto ciego de los periodos de vehiculo apagado.

## Alcance y limitaciones
Alcance CN. Aborda la deteccion durante reposo, no la supresion ni el entorno externo (GLP). No especifica interaccion con infraestructura de carga.

## Relevancia FTO / novedad
Aborda directamente la incertidumbre declarada por la cliente sobre la seguridad durante la carga nocturna con vehiculo apagado. Confirma que existe tecnica para el monitoreo en estado dormido (no es un vacio tecnologico), aunque limitada a CN. Insumo de diseno; no es barrera FTO en Chile.

> Relaciones: misma_tecnologia con patente-cn113013514b (deteccion multisensor). complementa a patente-us11703186b2 (seguridad en el punto de carga). Ver `../../indice.json`.
