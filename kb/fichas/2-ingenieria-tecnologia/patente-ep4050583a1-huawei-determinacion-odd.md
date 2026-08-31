---
id: patente-ep4050583a1-huawei-determinacion-odd
titulo: "Operational design domain (ODD) determination method and apparatus — EP4050583A1 (Huawei / Shenzhen Yinwang)"
tipo: patente
tema: Determinar si el sistema de conducción automatizada está dentro del ODD de un tramo comparando conjuntos de parámetros ambientales y operativos
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [G05D1/0214]
topicos: [recinto-privado-odd, seguridad-funcional-av, entorno-semi-estructurado]
anio: 2019
titular: Huawei Technologies Co., Ltd. / Shenzhen Yinwang Intelligent Technologies Co., Ltd. (China)
referencia: EP4050583A1 (prioridad CN 2019; PCT 2020-06-24; publicación EP 2022-08-31; familia CN/WO/EP/US)
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: en trámite (Status "Pending" en la publicación EP)
jurisdicciones: [CN, WO, EP, US]
fecha_prioridad: 2019
trl_relevante: 6-7
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Problema técnico que resuelve
Saber, **en operación**, si el vehículo automatizado sigue dentro del dominio de diseño operacional del tramo por el que circula (y no fuera de él).

## Reivindicaciones clave (qué protege)
Claim 1 (literal, verificado, traducción no aplicada):
> "An operational design domain ODD determining method, applied to an automated driving system of a vehicle, wherein the method comprises: determining an ODD of a target road section where the automated driving system is located, wherein a first parameter set corresponding to the ODD comprises a first environmental parameter set and/or a first operating parameter set of the automated driving system; obtaining a second parameter set, wherein the second parameter set comprises a second environmental parameter set and/or a second operating parameter set… of the automated driving system on the target road section; and determining, when it is identified that the second parameter set is a subset of the first parameter set, that the automated driving system does not exceed the ODD of the target road section."

## Solución técnica (cómo lo hace)
Formaliza el ODD como **conjuntos de parámetros** (ambientales y operativos) por tramo, y la verificación de pertenencia como una **relación de subconjunto** entre lo declarado y lo medido. 35 reivindicaciones.

## Alcance y limitaciones
- Es una **verificación embarcada, dentro del sistema de conducción automatizada** ("applied to an automated driving system of a vehicle"): asume acceso al ADS. Kaufmann, con vehículo caja negra, **no** está en ese supuesto.
- Cubre la comprobación en línea; no cubre cómo se **construye empíricamente** el conjunto de parámetros de un recinto industrial no estandarizado.
- Familia amplia (CN/WO/EP/US); **no se encontró publicación chilena** en la consulta a Google Patents.

## Relevancia FTO / novedad
Fija el estándar del arte: la formalización del ODD por tramo y la verificación de pertenencia ya están reclamadas por Huawei. Para Kaufmann esto **empuja la novedad** hacia el lado del explotador: no "verificar el ODD desde el ADS", sino **caracterizar y validar experimentalmente el ODD de un recinto** (maicillo, polvo, neblina, tráfico mixto) desde afuera del vehículo, y decidir con eso la habilitación del sitio. Es un desplazamiento del sujeto (fabricante → operador) y del insumo (telemetría interna → evidencia de campo + logs limitados).

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
