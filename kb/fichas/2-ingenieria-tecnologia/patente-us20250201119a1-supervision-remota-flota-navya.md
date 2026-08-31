---
id: patente-us20250201119a1-supervision-remota-flota-navya
titulo: "Method and system for the remote supervision of a fleet of self-driving vehicles — US20250201119A1 (Navya Mobility)"
tipo: patente
tema: Supervisión remota de shuttles autónomos detenidos por obstáculo — envío de video en vivo e histórico al operador remoto para autorizar el rearranque
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
ipc: [G08G1/20, G08G1/16, B60W60/00, G06V20/58, H04N7/18]
topicos: [vehiculo-autonomo-l4, teleoperacion-supervision-remota, shuttle-autonomo-pasajeros, flota-y-telemetria]
anio: 2022
titular: Navya Mobility (ex Navya SAS)
referencia: US20250201119A1
motor: Google Patents
profundidad_lectura: abstract
estado_evidencia: verificado
estado_legal: solicitud
jurisdicciones: [US, EP, JP, FR, WO]
fecha_prioridad: 2022-03-16
trl_relevante: 8
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Problema técnico que resuelve

El modo de fallo dominante de un shuttle autónomo L4 en recinto no es el choque: es **quedarse detenido**. El vehículo frena ante un obstáculo detectado y no puede decidir por sí solo si el obstáculo desapareció o si era espurio. Sin operador a bordo, alguien remoto debe entender *por qué* se detuvo — y el video en vivo llega **después** del evento, cuando el obstáculo ya no está en cuadro.

## Reivindicaciones clave (qué protege)

Reivindicación independiente 1 (cita literal del inicio): *"A method for the remote supervision of a fleet of self-driving vehicles (10, 20, 30, 40) where each vehicle in the fleet comprises exteroceptive sensors each able to provide information about the environment of the vehicle, a storage unit able to store the information obtained by the exteroceptive sensors, and an automated driving unit able to detect a nearby obstacle on the basis of the information obtained by the exteroceptive sensors and to stop the vehicle in the event a nearby obstacle is detected..."*

Lo que monopoliza: el flujo de supervisión remota **gatillado por la detención de seguridad** — se abre la sesión de comunicación con el centro de supervisión tras el paro, y se transmite tanto el flujo en vivo como el **registro histórico almacenado** de los sensores, para que el operador humano autorice o prohíba el rearranque. No es teleconducción (el remoto no conduce): es autorización de reanudación.

## Solución técnica (cómo lo hace)

Cada vehículo almacena continuamente los datos de sus sensores exteroceptivos. Cuando la unidad de conducción automatizada detecta obstáculo y detiene el vehículo, se establece la sesión inalámbrica con el sistema de supervisión y se envía video/datos en vivo **más** la grabación previa al evento. El supervisor evalúa la causa y emite la orden de rearranque o de mantener el paro. Un operador puede así atender varios vehículos por excepción, no por conducción continua.

## Alcance y limitaciones

Cubre el método de supervisión remota de **flota** ligado al evento de paro por obstáculo, con transmisión de histórico. No cubre teleconducción en tiempo real (control directo del volante/acelerador desde remoto), que es otro cuerpo de patentes (Bosch, Continental, May Mobility). Estado: **solicitud pendiente** en US; familia WO2023175280A1 / EP4494126A1 / JP2025509656A / FR3133698B1.

## Relevancia FTO / novedad

Muy pertinente para el caso "un vehículo autónomo en centro logístico privado": el centro de control y la telemetría del piloto tocan exactamente este territorio. Como es **solicitud** (no concedida) y sin evidencia de familia en Chile, el riesgo FTO en Chile es bajo hoy, pero: (a) si el proyecto desarrolla su propio centro de supervisión con reenvío de histórico pre-evento, esa función específica **no es novedad** — está publicada desde 2023 y sirve como estado del arte que obliga a diferenciar el aporte de I+D; (b) para exportar la solución a otros mercados (US/EP/JP) conviene revisar el estado de concesión cuando se comercialice.

> Relaciones con otras fichas (contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
