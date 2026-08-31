---
id: patente-us11335197b2-volkswagen-qos-predictiva-teleoperacion
titulo: "Teleoperated driving of a vehicle — US11335197B2 (Volkswagen AG)"
tipo: patente
tema: Ajuste anticipado de los parámetros de teleoperación (p. ej. velocidad máxima) combinando probabilidad de incidente y calidad de red predicha
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [G05D1/00, G08G1/00, H04W4/46, B60W60/00]
topicos: [teleoperacion-supervision-remota, requisitos-red-latencia-jitter, conectividad-red-vehiculo-autonomo, teleoperacion-fallback]
anio: 2019
titular: Volkswagen AG
referencia: US11335197B2 (familia: EP3816749A1, KR102399750B1, CN112817306B)
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: vigente
jurisdicciones: [US, EP, CN, KR]
fecha_prioridad: 2019-10-29
trl_relevante: 6-8
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Problema técnico que resuelve
La mala calidad de red degrada la seguridad de la conducción remota. Reaccionar cuando el enlace ya cayó es tarde: hace falta **anticipar** la caída de QoS y restringir la operación antes de que coincida con una situación crítica de conducción.

## Reivindicaciones clave (qué protege)
Claim 1 (síntesis verificada): sistema electrónico de guiado que (i) recibe datos de sensores del entorno, (ii) **determina una probabilidad de incidente** a partir de esos datos, (iii) **obtiene información predicha de calidad de red** (predictive QoS), y (iv) **define parámetros operacionales — como la velocidad máxima — en función de ambas**.

Cita textual del resumen:
> "A method for teleoperated driving… wherein sensor data concerning an environment of the transportation vehicle are received and a computation system determines a probability for an incident affecting a control of the transportation vehicle based on the sensor data."

## Solución técnica (cómo lo hace)
Cruce de dos predicciones (riesgo del entorno × QoS futura de la red: latencia, ancho de banda, tasa de error) para modular la envolvente operacional del vehículo teleoperado en tiempo real.

## Alcance y limitaciones
- Familia concedida en US, EP, CN, KR — protección amplia.
- No cubre la infraestructura de red en sí, sino el uso de su predicción para limitar el vehículo.
- Verificado: titular, prioridad, familia, CPC y cita del resumen.

## Relevancia FTO / novedad
Cierra la vía de novedad "modulamos la velocidad del camión según la calidad de red predicha": un OEM automotriz ya lo tiene concedido en cuatro jurisdicciones desde prioridad 2019. Para una faena minera, lo no cubierto por esta familia es el **mapa de QoS específico de la ruta minera y su acoplamiento con el plan minero** (dónde y cuándo se puede telecomandar), que es donde puede residir una contribución técnica propia.

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
