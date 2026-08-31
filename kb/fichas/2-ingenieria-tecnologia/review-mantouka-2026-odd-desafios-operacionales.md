---
id: review-mantouka-2026-odd-desafios-operacionales
titulo: "Automated Vehicle Traffic: A Review of Operational Challenges, Infrastructure Requirements and Research Directions (Mantouka et al., 2026)"
tipo: revision
tema: Revisión de desafíos operacionales vigentes, ODD y requisitos de infraestructura para vehículos automatizados
area_oecd: "2 Ingeniería y Tecnología (2.1 Ingeniería civil)"
topicos: [recinto-privado-odd, conectividad-red-vehiculo-autonomo, vehiculo-autonomo-shuttle]
anio: 2026
autores: [Eleni G. Mantouka, K. Vakrinou, K. N. Christidis, B. Magoutas, A. Kiousi, Eleni I. Vlahogianni]
referencia: https://doi.org/10.3390/s26041232
motor: Europe PMC → PMC12943904 (full-text open access)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: ["retrorreflectividad mínima de demarcación 150 mcd/lux/m2", "ISO 34503:2023 como norma de ODD", "brecha entre validación en simulación y aprobación regulatoria"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
¿Qué desafíos operacionales, requisitos de infraestructura y brechas de investigación condicionan hoy el despliegue escalable de movilidad conectada, cooperativa y automatizada (CCAM) en condiciones reales?

## Hipótesis
El Operational Design Domain (ODD) no es solo una propiedad del vehículo: está condicionado por la infraestructura física y digital, y su fragmentación normativa es una barrera al despliegue.

## Metodología
- **Diseño:** revisión de literatura y de normativa, integrando estandarización, adaptaciones de infraestructura física, habilitadores tecnológicos y gobernanza.
- **Datos / muestra:** literatura de CCAM, normas SAE (EE.UU.), ISO/ETSI (Europa), incluida ISO 34503:2023.
- **Técnicas:** síntesis temática por dimensión (ODD, infraestructura, conectividad, gobernanza).

## Resultados principales
- **ODD fragmentado:** las definiciones de ODD siguen fragmentadas entre jurisdicciones (SAE/EE.UU., ISO/UE, ETSI) y hay validación limitada en escenarios reales de tráfico mixto denso; persiste una brecha entre el aseguramiento de seguridad basado en simulación y la aprobación regulatoria para despliegue real.
- **Percepción colaborativa poco explorada en terreno:** "much of the existing literature focuses on collaborative maneuvering at the theoretical or algorithmic level, while collaborative perception... remains comparatively underexplored in real-world settings".
- **Brecha normativa V2I/V2X:** ISO 34503:2023 "could benefit from expansion and elaboration on specific CCAM applications, such as Vehicle-to-Infrastructure (V2I) and Vehicle-to-Everything (V2X) communication conditions".
- **Infraestructura condiciona el ODD:** demarcación con retrorreflectividad mínima de 150 mcd/lux/m²; pérdida de señal GPS en túneles; fallas de percepción con poca luz; clima adverso sigue siendo una limitación mayor del ODD.
- **Habilitadores propuestos:** gemelos digitales, arquitectura V2I/V2X estandarizada y gestión descentralizada de datos que permita "real-time ODD extendibility".

## Conclusiones
El despliegue escalable requiere definir el ODD como una propiedad conjunta del vehículo, la infraestructura y la operación, con monitoreo dinámico en tiempo real. Las direcciones abiertas incluyen monitoreo dinámico del ODD, integración human-in-the-loop en tráfico mixto y validación progresiva simulación→despliegue.

## Limitaciones
Revisión centrada en vía pública y en el marco europeo/estadounidense; no aborda específicamente recintos privados ni shuttles de baja velocidad. No aporta datos primarios.

## Relevancia / brecha para el estado del arte
Es la referencia de 2026 que acredita que los desafíos de ODD, percepción en clima adverso y conectividad **siguen abiertos en la literatura**, no resueltos por el producto comercial. Sustenta que definir y validar el ODD de un recinto privado concreto (con su infraestructura y su conectividad) es una actividad de investigación aplicada, no una configuración.

> Relaciones → `../../indice.json`. Ver [[review-kamtam-2024-latencia-teleoperacion-cav]], [[paper-anund-2022-lecciones-sitios-demo-shuttle-autonomo]].
