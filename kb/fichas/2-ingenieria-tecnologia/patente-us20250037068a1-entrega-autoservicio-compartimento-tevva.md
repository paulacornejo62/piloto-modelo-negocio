---
id: patente-us20250037068a1-entrega-autoservicio-compartimento-tevva
titulo: "Interactive delivery — self-service delivery desde compartimentos asegurados de un vehículo de reparto (Tevva Motors, US20250037068A1)"
tipo: patente
tema: Retiro de carga por el usuario desde compartimentos asegurados de un vehículo de reparto (autónomo o conducido), con mensajería y acceso autenticado
area_oecd: "2 Ingeniería y Tecnología (2.11 Otras ingenierías y tecnologías)"
ipc: G06Q10/083
topicos: [interaccion-carga-usuario, vehiculo-autonomo-carga]
anio: 2021
autores: [Asher Bennett]
referencia: https://patents.google.com/patent/US20250037068A1/en
motor: Google Patents (tools/browse.mjs gp + open)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: ["prioridad GB 2021-12-01", "familia GB WO US", "estado: pendiente (2025-01-30)"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Problema que resuelve
Evitar que el personal de reparto recorra a pie el último tramo: permitir que el destinatario retire su bulto directamente desde un compartimento asegurado del vehículo cuando este está cerca.

## Solución técnica (según descripción y reivindicación 1)
Al cumplirse una condición de proximidad entre el vehículo de reparto y el punto de entrega, el sistema (i) envía al usuario un mensaje ofreciendo la opción de autoservicio, (ii) recibe la selección del usuario, (iii) le envía la información para **acceder a un compartimento asegurado** entre varios del vehículo, y (iv) ordena cargar el ítem en ese compartimento. El vehículo puede permanecer detenido hasta confirmar que el ítem fue retirado y puede desplazarse autónomamente entre puntos.

## Reivindicaciones / alcance
Cubre el flujo completo de entrega autoservicio con compartimentos múltiples y control de la permanencia del vehículo; contempla explícitamente capacidad autónoma del vehículo.

## FTO / lectura para el proyecto
La **autenticación del usuario para abrir un compartimento de carga** es arte previo denso: además de esta solicitud, aparecen familias de Deutsche Post (CN106372827B, entrega autónoma en el vehículo del cliente), BlackBerry (ES2955857T3, control de acceso a compartimentos de una unidad de transporte de carga) y Ford. Para el caso Kaufmann, la apertura por QR para retiro de carga debe tratarse como **integración de tecnología existente** (nivel de riesgo bajo), no como el núcleo de I+D; el aprendizaje declarable está en la integración con la lógica de misión del vehículo y con la telemetría del recinto.

**Cita textual (abstract):**
- "sending, to the user, a second message comprising information relating to accessing a securable compartment from among plural securable compartments associated with the delivery vehicle"

> Relaciones con otras fichas → `../../indice.json`.
