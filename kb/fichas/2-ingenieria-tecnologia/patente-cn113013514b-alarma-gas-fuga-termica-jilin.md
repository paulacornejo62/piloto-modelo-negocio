---
id: patente-cn113013514b-alarma-gas-fuga-termica-jilin
titulo: "Thermal runaway gas-sensitive alarm device of vehicle-mounted lithium ion power battery — CN113013514B (Universidad de Jilin)"
tipo: patente
tema: Alarma de fuga termica embarcada con fusion multisensor (gas + termopar celda a celda + masa) y prediccion por cadena de Markov
area_oecd: "2 Ingenieria y Tecnologia (2.2 Ingenieria electrica, electronica e informatica)"
ipc: [H01M10/48, G01N33/00]
topicos: [fuga-termica-bateria, bms-monitoreo, seguridad-bateria-litio]
anio: 2021
titular: Universidad de Jilin (Jilin University)
referencia: CN113013514B
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: vigente
jurisdicciones: [CN]
fecha_prioridad: 2021-02-25
trl_relevante: 5
fecha_registro: 2026-07-14
proyectos:
  - lipigas
---

## Problema tecnico que resuelve
Alerta temprana de fuga termica en la bateria de traccion Li-ion embarcada en un vehiculo, integrando multiples variables fisicas para anticipar el evento y proteger a conductor/pasajeros.

## Reivindicaciones clave (qué protege)
Dispositivo de alarma gas-sensitivo con: caja; multiples modulos de pack dispuestos con canales de campo de flujo de refrigeracion entre ellos; un SENSOR DE GAS a la salida del canal de refrigeracion; multiples TERMOPARES distribuidos dentro de los modulos; multiples SENSORES DE MASA bajo las celdas (correspondencia uno a uno); y un dispositivo de gestion conectado a todos. Metodo: juzga la PROBABILIDAD de fuga termica mediante un MODELO DE PREDICCION DE CADENA DE MARKOV y aplica enfriamiento + alerta.

## Solución técnica (cómo lo hace)
Fusiona tres senales complementarias — gas de venteo (quimica), temperatura celda a celda (termica) y masa/perdida de masa por celda (venteo/expulsion de material) — y las alimenta a un modelo probabilistico (Markov) que estima la probabilidad de fuga termica antes del evento franco, disparando refrigeracion y alarma.

## Alcance y limitaciones
Alcance CN (una sola jurisdiccion). Es un enfoque de investigacion (universidad, TRL medio), no necesariamente producto comercial. No aborda el entorno GLP.

## Relevancia FTO / novedad
Muestra el estado del arte academico de la deteccion predictiva multisensor celda a celda. Para Lipigas es referencia de que la sensorica inteligente celda a celda + prediccion es un campo activo. Al estar limitada a CN, no representa barrera FTO en Chile; es insumo de diseno para el requerimiento de 'sensores inteligentes y monitoreo celda a celda' declarado por la cliente.

> Relaciones: misma_tecnologia con patente-cn113036250b (monitoreo predictivo) y patente-cn114980983a (deteccion por gas). Ver `../../indice.json`.
