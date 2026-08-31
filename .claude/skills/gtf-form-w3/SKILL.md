---
name: gtf-form-w3
description: Paso FORM_W3 del flujo de financiamiento GT (Formulación, Semana 3). Estructuración operativa: capacidades (profesional acreditador, personal asociado, subcontratos) y Carta Gantt/Presupuesto. Escribe el bloque form_w3. Lo invoca el orquestador gtf-orquestar.
---

# FORM_W3 — Capacidades y Carta Gantt (Semana 3)

**Objetivo:** estructurar el equipo humano y el plan de trabajo/presupuesto.

**Inputs:** listado de RRHH de la empresa, CVs y copias de títulos.

**Productos (`form_w3`):**
- `profesional_acreditador`: { `nombre`, `tiene_contrato_vigente` (bool), `experiencia_id_36m` (bool), `cv_path`, `titulo_path` }.
  - Requisito Ley I+D: profesional de ciencia/ingeniería con experiencia en I+D en los **últimos 36 meses** y **contrato vigente** (no honorarios si es permanente; contrato de servicios si es externo). → es la **regla QA 2**.
- `personal_asociado[]`: { nombre, funcion, horas }.
- `subcontratos_habilitados[]`: empresas contratadas (nombre + experiencia).
- `plan_de_trabajo`: ruta a la planilla oficial de Corfo (Carta Gantt + presupuesto, `.xlsx`).
- `desafios_tecnologicos[]`: { `n`, `nombre`, `por_que_incierto`, `por_que_superable` } — la tabla oficial de Desafíos Tecnológicos (la emite `gantt.py`). **Granularidad (H-13):** enumera **un desafío por reto técnico real e incierto**, NO agrupes de más — el evaluador CORFO califica la incertidumbre desafío por desafío (el caso SRS real declaró 7, no 4-5). Sepáralos cuando son incertidumbres distintas (p.ej. cepa/genogrupo, proceso de concentración, escalamiento de producción, modelo de desafío son desafíos distintos).

**Dinámica (reunión 1h):** identificar al profesional que acredita capacidades; definir funciones del personal; revisar cotizaciones de subcontratos.

Captura `personal_asociado[]` con `cuenta` (Director/Investigador/Tecnico), `horas` y `valor_hh`, y `actividades[]` (Gantt). Luego genera la planilla:
```bash
python3 render/gantt.py <tenant>    # → proyectos/<tenant>/plan-trabajo.xlsx (Gantt + Presupuesto, estructura oficial)
```
Es un insumo de arranque; el consultor lo traspasa al formato oficial (ver `plantillas/README.md`).

**DoD:** documentos de capacidades recopilados y **correspondencia exacta de nombres y horas** entre la planilla y los CVs. `meta.paso_actual = "FORM_W3"`. Valida y renderiza.
