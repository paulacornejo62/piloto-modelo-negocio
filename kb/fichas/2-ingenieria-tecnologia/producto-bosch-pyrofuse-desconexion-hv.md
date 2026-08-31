---
id: producto-bosch-pyrofuse-desconexion-hv
titulo: "Bosch pyrofuse (pyrotechnical fuse) — desconexion pirotecnica de alta tension en EV/HEV"
tipo: producto
tema: Fusible pirotecnico comercial que secciona el bus de alta tension de la bateria en milisegundos por señal de disparo
area_oecd: "2 Ingenieria y Tecnologia (2.2 Ingenieria electrica, electronica)"
topicos: [desconexion-emergencia-bateria, seguridad-bateria-litio, electromovilidad-carga-peligrosa]
anio: 2020
titular: Robert Bosch GmbH
referencia: "Bosch pyrofuse — greencarreports 1125462 / catalogo Bosch Mobility"
motor: WebSearch + WebFetch (greencarreports.com)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 9
fecha_registro: 2026-07-22
proyectos:
  - lipigas
---

## Qué es
Dispositivo pirotecnico ("an explosive device designed to break an electrical connection") que impulsa una cuña a traves de las conexiones electricas entre el pack de bateria del EV/HEV y su electronica asociada, seccionando el bus de alta tension. Añade una capa de redundancia a los "kill switches" electronicos ya presentes en EV/HEV. Producto comercial en produccion en serie (proveedor Tier-1).

## Cómo dispara y qué protege
Se activa por SEÑAL (tipicamente desde la unidad de control de airbag / SRS ante colision, o ante cortocircuito/sobrecorriente), cortando el HV en milisegundos para prevenir arco, choque electrico e incendios secundarios. NO detecta ni previene autonomamente la fuga termica de la propia bateria.

## Cita textual
"it adds a layer of redundancy to the existing electronic 'kill switches' already found in hybrid and electric vehicles" — y explicitamente: "[it] won't do anything to prevent thermal runaway and other issues if the battery pack itself is compromised" (greencarreports).

## Relevancia / brecha
Confirma que el corte pirotecnico HV es tecnologia comercial madura (TRL 9), pero su gatillo es la colision/cortocircuito, no un precursor termico autonomo. La propia descripcion admite que no actua ante fuga termica del pack. Esto sostiene la brecha del caso Lipigas: no hay producto comercial que DESACOPLE la bateria disparado autonomamente por señal de fuga termica en un vehiculo estacionado cargando, para proteger un almacenamiento de GLP adyacente.

> Relaciones: misma_tecnologia con patente-us9221343b2 (Tesla) y producto-autoliv-mersen-pyroswitch. Ver `../../indice.json`.
