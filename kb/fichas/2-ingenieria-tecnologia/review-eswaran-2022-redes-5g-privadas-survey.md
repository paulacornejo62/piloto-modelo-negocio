---
id: review-eswaran-2022-redes-5g-privadas-survey
titulo: "Private 5G networks: a survey on enabling technologies, deployment models, use cases and research directions (Eswaran & Honnavalli 2022)"
tipo: revision
tema: Modelos de despliegue de redes 5G privadas (campus) y sus casos de uso industriales/logísticos
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [conectividad-vehiculo-autonomo, v2i-iot-logistica]
anio: 2022
autores: [Sivaraman Eswaran, Prasad Honnavalli]
referencia: https://doi.org/10.1007/s11235-022-00978-z
motor: WebSearch + PMC (PMC9676741, full-text open access) — Telecommunication Systems
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "7-9 (tecnología desplegada comercialmente)"
metricas_clave: ["5 modelos de despliegue de red privada", "casos industriales documentados: Samsung Austin (2020), BMW Leipzig (2020)"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
Sistematizar tecnologías habilitantes, modelos de despliegue, casos de uso y direcciones de investigación de las redes 5G privadas (non-public networks).

## Hipótesis
No experimental. Premisa: las redes privadas ofrecen a la empresa control, aislamiento y garantías de desempeño que la red pública no asegura.

## Metodología
- **Diseño:** revisión de literatura y de despliegues industriales documentados.

## Resultados principales
- Cinco modelos de despliegue: LAN 5G privada independiente por la empresa; LAN privada independiente operada por un MNO; RAN y señalización compartidas; network slicing (RAN y core compartidos); RAN y plano de control compartidos.
- Requisitos críticos transversales: confiabilidad vía URLLC, alta disponibilidad por redundancia, seguridad e interoperabilidad entre red privada y pública.
- Direcciones abiertas: armonización de espectro, gestión de red asistida por aprendizaje automático, robustez/alta disponibilidad y asignación de recursos en slicing dinámico.

## Conclusiones
La red 5G privada es una tecnología disponible y con casos industriales reales; lo abierto está en la ingeniería de garantías (disponibilidad, seguridad, slicing) para cada entorno.

## Limitaciones
Es una revisión general de telecomunicaciones: no entrega mediciones de campo ni casos de vehículos autónomos en recintos logísticos. No sustituye una evaluación de cobertura del sitio concreto.

## Relevancia / brecha para el estado del arte
Fija el punto de comparación honesto para la discusión Frascati de la capa de conectividad: **la red privada 5G como producto es estado del arte comercial (integración)**; lo potencialmente novedoso no es desplegarla, sino la arquitectura de operación (fallback, continuidad, garantías) que se construya sobre ella para un vehículo autónomo de carga.

**Citas textuales:**
- "Private 5G networks can be deployed in two ways, viz., an independent private network (SNPN) and integrated private network (PNI-NPN)."
- "5G networks will empower businesses beyond the factory floor, including distribution, supply chain, warehousing, and customer service."

> Relaciones con otras fichas → `../../indice.json`.
