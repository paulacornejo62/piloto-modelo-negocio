---
id: paper-andersson-2023-operacion-remota-vehiculos-pesados-simulador
titulo: "Exploring remote operation of heavy vehicles — findings from a simulator study (Andersson, Rizgary, Söderman & Vännström 2023; proyecto HAVOC, RISE + Scania)"
tipo: paper
tema: Factores humanos de la operación remota de camiones pesados: evaluación, asistencia y conducción remota en un mismo puesto de trabajo
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [factores-humanos-operador-remoto, teleoperacion-supervision-remota, recinto-privado-odd]
anio: 2023
autores: [Jonas Andersson, Daban Rizgary, Mikael Söderman, Johanna Vännström]
referencia: https://openaccess.cms-conferences.org/publications/book/978-1-958651-45-2/article/978-1-958651-45-2_5 (DOI 10.54941/ahfe1002820; versión ampliada en Human-Intelligent Systems Integration, DOI 10.1007/s42454-024-00051-x)
motor: Google Académico (tools/browse.mjs scholar) + WebFetch (versión de conferencia en acceso abierto; la versión Springer exige login)
profundidad_lectura: abstract
estado_evidencia: verificado
trl_relevante: "3-4 (estudio en simulador con operadores)"
metricas_clave: ["15 participantes", "escenario con 10 camiones simultáneos en vía pública y áreas confinadas (hub de transporte)", "3 modos de control: assessment, assistance, remote driving"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Pregunta / objetivo de investigación
¿Qué requisitos y desafíos de interacción humano-automatización aparecen cuando un operador remoto debe atender **vehículos pesados automatizados** en operación hub-to-hub, alternando entre evaluar, asistir y conducir remotamente?

## Hipótesis
El operador remoto tendrá un rol esencial para compensar las limitaciones de la automatización; ese rol, sin embargo, reintroduce los problemas clásicos de la automatización (fuera del lazo, confianza, atención) en un contexto nuevo.

## Metodología
- **Diseño:** estudio en simulador, colaboración RISE Research Institutes of Sweden + Scania (proyecto HAVOC).
- **Datos / muestra:** 15 participantes.
- **Escenario:** el operador maneja **diez camiones** circulando en vía pública y en áreas confinadas (hub de transporte).
- **Modos evaluados:** evaluación remota (assessment), asistencia remota (assistance) y conducción remota (remote driving).

## Resultados principales
- Se identificaron los tres roles/funciones del operador remoto: "assessment, assistance, and remote driving".
- Aparecen los problemas clásicos de automatización en este contexto nuevo: "Instances of challenges with situational awareness, out-of-the-loop, trust, and attention management were found."
- Punto de partida declarado por los autores: "fully automated driving has posed more challenges than expected", lo que empuja la operación remota como capa de compensación.

## Conclusiones
El puesto de trabajo del operador remoto de camiones pesados —con múltiples vehículos a cargo y transiciones entre modos— es un problema de diseño de factores humanos aún abierto, no un detalle de implementación.

## Limitaciones
- **Solo se leyó el resumen y la información de la versión de conferencia en acceso abierto**; la versión ampliada (Springer 2024) está tras autenticación. Los hallazgos detallados (métricas de carga de trabajo, tiempos de transición) no fueron verificados.
- Estudio en simulador, no en operación real; escenario europeo de transporte hub-to-hub, no faena minera.

## Relevancia / brecha para el estado del arte
Es la evidencia más directa sobre operación remota de **camiones pesados** con operador humano en el lazo, e identifica el modelo realista del puesto (un operador, varios vehículos, transiciones entre modos). Refuerza que el diseño del rol y la conciencia situacional son brechas vigentes, en la misma línea de [[paper-mutzenich-2021-situation-awareness-operador-remoto]] y [[paper-li-2023-teleoperador-remoto-5g-nivel4]].

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
