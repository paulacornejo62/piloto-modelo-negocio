---
id: caso-nokia-komatsu-2020-lte-privada-flota-autonoma
titulo: "Komatsu y Nokia: por qué la LTE privada reemplazó a Wi-Fi en el transporte autónomo minero (International Mining, junio 2020)"
tipo: caso
tema: Migración de Wi-Fi a LTE privada en sistemas de transporte autónomo (AHS) minero; cifras de disponibilidad y pérdida de paquetes
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [redes-privadas-lte-5g-industriales, mineria-remota-automatizacion, conectividad-red-vehiculo-autonomo]
anio: 2020
autores: [International Mining (nota de prensa técnica sobre webinar Komatsu-Nokia)]
referencia: https://im-mining.com/2020/06/25/komatsu-nokia-outline-upside-private-lte-autonomous-haulage/
motor: WebSearch + WebFetch
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 9
metricas_clave: ["Pérdida de paquetes Wi-Fi ≈4 %", "Problemas de equipos de comunicación = 15,13 % del tiempo perdido en 24 h", "247 camiones autónomos en operación (2020); >350 previstos a fin de 2020", ">50 % (siete faenas) sobre LTE de Nokia", "Disponibilidad declarada LTE privada: 99,99 %; 5G esperado 99,999 %"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Qué documenta

Presentación conjunta Komatsu–Nokia sobre por qué el sistema de transporte autónomo (AHS, FrontRunner) migró de Wi-Fi a LTE privada.

Citas textuales recogidas del artículo:
> "coverage, capacity and latency – which mean it is now the preferred solution over WiFi"
> "LTE usually has much higher allowed output power, resulting in a longer range" · "licensed and coordinated frequencies leading to less noise"
> "WiFi packet loss was about 4%" · "if two frames are sent at once, both are lost and must retry"
> "comms equipment problems accounted for 15.13% of time lost in a 24 hour period"
> "reliability of message delivery is orders of magnitude better on LTE versus 802.11 WiFi"
> Disponibilidad: "99.99% availability" para LTE privada, "99.999%" esperado con 5G.
> Escala: "247 autonomous haul trucks in operation"; "over 50% (seven sites) are running on Nokia LTE".

## Relevancia / brecha para el estado del arte

- **Problema resuelto**: la conectividad para **flota autónoma** (no teleoperada) en faena minera está industrializada sobre LTE privada, con cifras de disponibilidad de 99,99 % y cientos de camiones en producción. Wi-Fi quedó desplazado por pérdida de paquetes y tiempo perdido por fallas de comunicación.
- **Lo que NO cubre**: la autonomía tolera cortes breves (el camión sigue su misión); la **teleoperación con lazo humano cerrado** no. Una disponibilidad de 99,99 % equivale a ~53 min/año de indisponibilidad — aceptable para autonomía, pero relevante si cada corte dispara un safe-stop en una operación 24/7.
- Alerta metodológica: cifras provenientes de un webinar de proveedores reportado por prensa técnica (no paper ni documento primario auditable) → **evidencia parcial**.

> Relaciones con otras fichas → `../../indice.json`.
