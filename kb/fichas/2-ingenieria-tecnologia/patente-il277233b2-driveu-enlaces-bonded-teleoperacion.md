---
id: patente-il277233b2-driveu-enlaces-bonded-teleoperacion
titulo: "Device, system and method for autonomous driving and remotely controlled vehicles — IL277233B2 / JP7308920B2 (DriveU Tech Ltd.)"
tipo: patente
tema: Teleoperación híbrida con IA a bordo y enlace inalámbrico agregado (bonded) de múltiples portadoras, con adaptación de parámetros de conducción a la disponibilidad del enlace
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [G05D1/0022, H04W4/40]
topicos: [teleoperacion-supervision-remota, enlace-multiruta-bonding, conectividad-red-vehiculo-autonomo, teleoperacion-fallback]
anio: 2018
titular: DriveU Tech Ltd. (Israel)
referencia: IL277233B2 (familia: JP7308920B2, CN112074790B, US/EP/KR)
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: vigente
jurisdicciones: [IL, US, EP, CN, JP, KR, WO]
fecha_prioridad: 2018-03-18
trl_relevante: 7-9
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Problema técnico que resuelve
Cómo repartir la inteligencia entre el vehículo y el centro remoto cuando el canal inalámbrico es variable: qué se procesa a bordo, qué se envía, y **cómo degradar la conducción cuando el enlace se deteriora**, sin depender de una sola portadora.

## Reivindicaciones clave (qué protege)
- **Claim 1 (síntesis verificada):** un procesador vehicular asociado a IA a bordo que procesa localmente los sensores, transmite datos relevantes a procesadores remotos por enlaces inalámbricos, recibe comandos calculados remotamente y los ejecuta mediante una unidad autónoma o de teleconducción, **ajustando dinámicamente los parámetros de conducción según la disponibilidad de la comunicación inalámbrica**.
- **Claims 27-38 (verificado):** "two or more transmitters… upload data… via a **bonded wireless communication link**", combinando enlaces celulares, Wi-Fi, V2X, **satelital** y DSRC operando de forma concurrente para elevar la confianza en los comandos de teleoperación.

## Solución técnica (cómo lo hace)
Arquitectura híbrida IA local + teleoperación remota sobre enlace agregado multi-portadora, con lazo de realimentación entre calidad de enlace medida y parámetros de conducción (por ejemplo, velocidad máxima permitida).

## Alcance y limitaciones
- Cubre explícitamente la **inclusión de enlace satelital** dentro del bonding — relevante para faenas mineras sin cobertura celular continua.
- Familia amplia (US, EP, CN, JP, KR, IL): protección multi-jurisdiccional real.
- Verificado por lectura del resumen y de las reivindicaciones citadas en la ficha de Google Patents; no se leyó el pliego íntegro.

## Relevancia FTO / novedad
Junto con US11223667B2 (Phantom Auto) delimita el espacio de **"multi-enlace + adaptación de la conducción a la calidad del enlace"**. Un proyecto cuya novedad se plantee como "agregamos varias redes para telecomandar" tiene **poca novedad y riesgo FTO**: eso está reivindicado desde 2018-2019 con familias concedidas. La novedad defendible debe buscarse en el **caso de uso específico** (camión de fábrica en faena minera, distancia extrema, integración OEM-red privada-satélite, protocolo de traspaso operador-faena) y no en el bonding per se.
**Señal FTO:** sin evidencia de presentación en CL; verificación formal pendiente en INAPI (manual).

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
