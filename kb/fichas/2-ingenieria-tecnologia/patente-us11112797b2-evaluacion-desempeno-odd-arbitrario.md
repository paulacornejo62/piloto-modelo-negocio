---
id: patente-us11112797b2-evaluacion-desempeno-odd-arbitrario
titulo: "System and method for improving autonomous vehicle safety performance — US11112797B2 (Bin-Nun, individual)"
tipo: patente
tema: Protocolo de evaluación que crea un ODD arbitrario a partir de condiciones externas y compara el desempeño del vehículo autónomo con el de un vehículo conducido por humano en ese mismo ODD
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [G05D1/0088]
topicos: [recinto-privado-odd, disengagement-kpi-piloto, seguridad-funcional-av]
anio: 2017
titular: Amitai Yisrael Bin-Nun (inventor individual, sin cesionario empresarial)
referencia: US11112797B2 (solicitud US16/197,506; prioridad 2017-11-30; concedida 2021-09-07; expiración ajustada 2039-04-16)
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: caducada por falta de pago (Status "Expired - Fee Related")
jurisdicciones: [US]
fecha_prioridad: 2017-11-30
trl_relevante: 5-6
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Problema técnico que resuelve
Cómo medir si un vehículo autónomo se desempeña bien **en un dominio operacional definido a propósito**, usando como referencia el desempeño humano en el mismo dominio y las mismas maniobras.

## Reivindicaciones clave (qué protege)
Claim 1 (literal, verificado, extracto):
> "1. A method for evaluating safety performance of an autonomous vehicle, the method comprising: creating, by at least one processor, at least one arbitrary operational design domain based on at least one condition that is external to a driver-operated vehicle; controlling… an autonomous-operated vehicle to perform a first maneuver by an autonomous-vehicle-operation within the at least one operational design domain; controlling… at least one first sensor to sense first sensor data characterizing the autonomous-vehicle-operation…; determining… an autonomous-operated vehicle performance within the at least one operational design domain by comparing the first sensor data… to a first threshold to obtain a first driving quality value; determining… a driver-operated vehicle performance within the at least one operational design domain by comparing second sensor data characterizing a driver-operation… to a second threshold to obtain a second driving quality value; performing a comparison… of the driver-operated vehicle performance to the autonomous-operated vehicle performance…"

## Solución técnica (cómo lo hace)
Diseño experimental: se **define** un ODD por condiciones externas, se ejecuta la misma maniobra en modo autónomo y en modo humano, se sensa cada ejecución, se umbraliza a un "driving quality value" y se comparan ambos.

## Alcance y limitaciones
- **Caducada por falta de pago de anualidades** ("Expired - Fee Related") → el contenido cayó al dominio público en EE.UU. salvo reinstauración.
- Familia solo US; inventor individual, sin respaldo corporativo.
- Requiere sensores que caractericen la operación (propios o del vehículo); no resuelve el caso de logs pobres.

## Relevancia FTO / novedad
Es el arte previo del **protocolo comparativo autónomo vs humano dentro de un ODD definido ad hoc** — muy cercano al eje (a) de Kaufmann. Dos lecturas:
1. **FTO: libre.** Patente caducada y sin familia chilena: nada impide usar ese esquema experimental.
2. **Novedad: acotada.** No se puede reclamar "comparar desempeño autónomo vs humano en un ODD definido". Lo que sigue abierto es el **contenido del protocolo para un recinto industrial no estandarizado** (variables de superficie/polvo/neblina/tráfico mixto, criterios de aceptación, muestreo, decisión de habilitación) y su replicabilidad entre sitios.

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
