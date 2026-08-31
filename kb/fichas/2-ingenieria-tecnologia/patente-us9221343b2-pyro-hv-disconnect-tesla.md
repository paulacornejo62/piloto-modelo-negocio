---
id: patente-us9221343b2-pyro-hv-disconnect-tesla
titulo: "Pyrotechnic high voltage battery disconnect — US9221343B2 (Tesla)"
tipo: patente
tema: Desconexion pirotecnica del pack de alta tension del vehiculo, disparada por señal de colision del sistema de retencion (SRS)
area_oecd: "2 Ingenieria y Tecnologia (2.2 Ingenieria electrica, electronica)"
ipc: [B60L3/04]
topicos: [desconexion-emergencia-bateria, seguridad-bateria-litio, electromovilidad-carga-peligrosa]
anio: 2011
titular: Tesla Inc
referencia: US9221343B2
motor: Google Patents
profundidad_lectura: full-text
estado_evidencia: verificado
estado_legal: vigente
jurisdicciones: [US]
fecha_prioridad: 2011-12-16
trl_relevante: 9
fecha_registro: 2026-07-22
proyectos:
  - lipigas
---

## Problema tecnico que resuelve
Desconectar de forma rapida, consistente y direccional el pack de alta tension (HV) del sistema electrico del vehiculo ante un "evento catastrofico", superando la limitacion de los interruptores inerciales convencionales, que operan en un rango amplio de fuerzas g (10-35 g), son insensibles a la direccionalidad y no pueden programarse para responder distinto segun el tipo de evento.

## Reivindicaciones clave (qué protege)
Sistema para desacoplar una fuente HV del sistema electrico del EV que incluye: (i) al menos un contactor electrico (cerrado = pack conectado; abierto = desconectado); (ii) un sistema de retencion suplementario (SRS) que monitorea datos de colision de multiples sensores de impacto y emite una señal de activacion en respuesta a esos datos; y (iii) un interruptor pirotecnico (pyro-switch) con un primer estado pre-activado que da camino conductor y un segundo estado activado que SECCIONA fisicamente el camino conductor e impide reconectar la fuente HV. La desconexion cubre explicitamente el sistema de traccion Y el sistema de carga del EV.

## Solución técnica (cómo lo hace)
El SRS decide con logica programable (direccional, por tipo de evento) cuando la colision amerita el corte y dispara la carga pirotecnica, que rompe irreversiblemente el bus HV en milisegundos, en redundancia con los contactores.

## Alcance y limitaciones
El disparo esta atado a la señal del SRS = datos de COLISION/impacto. La reivindicacion NO contempla activacion autonoma por señal termica de la propia bateria (fuga termica en un vehiculo estacionado/cargando). Solo jurisdiccion US.

## Relevancia FTO / novedad
Confirma que el mecanismo de desconexion pirotecnica full-pack existe y esta patentado desde 2011, PERO su gatillo es la colision, no un precursor termico autonomo. Delimita la novedad del caso Lipigas: lo no cubierto es una desconexion disparada AUTONOMAMENTE por deteccion de fuga termica en un vehiculo detenido cargando de noche, para proteger un peligro externo adyacente (jaula de cilindros GLP), no a los ocupantes en un choque. No bloquea ese escenario; lo delimita.

> Relaciones: misma_tecnologia con producto-bosch-pyrofuse y producto-autoliv-mersen-pyroswitch (mismo mecanismo pyro, mismo gatillo colision); contrasta con patente-us12519189b2 (gatillo termico autonomo, pero a nivel modulo). Ver `../../indice.json`.
