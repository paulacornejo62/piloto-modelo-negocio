---
name: mn-form-w3
description: Paso FORM_W3 del flujo de modelo de negocio (Fase 2 — redacción). Plan de escalamiento: hitos comerciales, metas de tracción, proyección financiera estructurada y estrategia de escalamiento. NO incluye el detalle de equipo/capacidades (fuera del piloto). Escribe el bloque plan_escalamiento. Lo invoca el orquestador mn-orquestar.
---

# FORM_W3 — Plan de escalamiento, proyección y hitos comerciales

**Objetivo:** el plan para pasar del estado actual al mercado: qué hitos, con qué metas
medibles, y la proyección financiera que los sostiene.

**Inputs:** `modelo_negocio` (proyección por escenarios, unit economics),
`investigacion_mercado` (SAM/SOM, geografías), `narrativa` (mercado objetivo), `perfil_comercial`
(estado de desarrollo, tracción actual).

**Productos (`plan_escalamiento`):**
- `estado_actual`: punto de partida comercial (clientes, ventas, tracción hoy — de
  `perfil_comercial`).
- `hitos_comerciales[]`: `{ n, nombre, meta (indicador medible: nº de clientes, ingresos,
  contratos firmados), fecha_objetivo }`. Cada hito con una meta cuantificada, no "avanzar
  en ventas".
- `metas_traccion`: las metas de tracción comprometidas durante el proyecto y cómo se miden.
- `proyeccion_estructurada`: genera la planilla y guarda su ruta:
  ```bash
  python3 render/gantt.py <tenant>    # → proyectos/<tenant>/plan-trabajo.xlsx (proyección + hitos, estructura de apoyo)
  ```
  Es un insumo de arranque; el consultor lo traspasa al formato del fondo.
- `estrategia_escalamiento`: cómo se escala — nuevos segmentos, nuevas geografías, canales,
  alianzas — **anclado al SAM/SOM** y a la proyección por escenarios. Si la penetración de
  SOM del escenario base ya es alta, la estrategia debe explicar cómo se amplía el mercado
  servible, no solo cómo se captura más del actual.

**Fuera del piloto:** el detalle de **equipo y capacidades del beneficiario** (que varios
fondos piden como sección aparte) lo cubre el equipo GT — no lo redactes aquí.

**Dinámica (reunión 1h):** con el cliente, aterrizar los hitos y sus fechas, y validar los
supuestos de crecimiento de cada escenario.

**DoD:** hitos comerciales con metas medibles y fechas; metas de tracción; planilla de
proyección generada; estrategia de escalamiento anclada al SAM/SOM. `meta.paso_actual =
"FORM_W3"`. Valida y renderiza.
