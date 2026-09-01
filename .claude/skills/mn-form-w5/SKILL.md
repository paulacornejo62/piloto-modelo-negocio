---
name: mn-form-w5
description: Paso FORM_W5 del flujo de financiamiento GT (Formulación, Semana 5). Control de calidad de coherencia (4 reglas, vía motor de reglas), pago de arancel y envío del formulario en la plataforma Corfo. Cierra la Fase 2. Escribe el bloque form_w5. Lo invoca el orquestador mn-orquestar.
---

# FORM_W5 — QA de coherencia, cierre y envío (Semana 5)

**Objetivo:** verificar la coherencia interna del formulario, pagar el arancel y enviar.

**Inputs:** `form_w1`..`form_w4`.

## 1. QA de coherencia (motor de reglas — obligatorio antes de enviar)
Corre las 4 reglas con el motor, pasándole los datos del expediente:
```bash
python3 -c "import sys; sys.path.insert(0,'motor-reglas'); import reglas, json; print(json.dumps(reglas.qa_coherencia_formulacion(fase_proyecto_actual='<form_w4.fase>', profesional_contrato_vigente=<bool>, profesional_id_36m=<bool>, nuevo_conocimiento_trazable=<bool>, incertidumbre_justificada=<bool>), ensure_ascii=False))"
```
- **Regla 1** TRL↔fase, **Regla 2** profesional acreditador: las calcula el motor con los datos de `form_w3`/`form_w4`.
- **Reglas 3 y 4** (trazabilidad nuevo conocimiento; incertidumbre vs. ingeniería estándar): son **semánticas** — debes **leer `form_w2`** y confirmar (booleano) si se cumplen; el motor no las da por buenas sin tu confirmación.
- Guarda el resultado en `form_w5.qa_coherencia`. **Si hay `alerta`, NO envíes**: vuelve al sprint correspondiente a corregir.

## 1b. Límites de caracteres (gate duro — obligatorio antes de enviar)
Cada campo del formulario tiene un tope (título 100, objetivo 1000, etc.); un campo sobre el tope **no es enviable** (la plataforma lo trunca/rechaza).
```bash
python3 render/render.py <tenant> --limites
```
Si algún campo **excede** (sale ❌, exit 1): **NO envíes** — vuelve al sprint (FORM_W1/W2) a acortarlo. Solo avanza si todos están dentro del tope.

## 1c. Completitud del formulario OFICIAL del fondo (gate duro — fund-aware)
El formulario del fondo elegido debe tener **todas sus secciones** respondidas (Ley I+D 6 preguntas; CORFO las secciones por criterio):
```bash
python3 render/render.py <tenant> --formulario
```
Si sale **INCOMPLETO** (exit 1): **NO envíes** — falta redactar secciones del fondo (vuelve a FORM_W2). Solo avanza con todas en verde.

## 1d. Paquete de postulación completo (gate duro — gestión documental)
No basta el formulario: el fondo exige un **paquete de documentos** (arancel pagado, CVs, instrumento de representación, sistema contable, subcontratos…). Refresca y revisa el checklist:
```bash
python3 tools/postulacion.py scaffold <tenant>   # re-deriva lo que ya generó el sistema
python3 tools/postulacion.py estado <tenant>     # exit 1 si falta algún obligatorio
```
Si **faltan obligatorios** (exit 1): **NO envíes** — pide al cliente/consultor los documentos pendientes (aparecen con responsable). A medida que lleguen, márcalos: `python3 tools/postulacion.py marcar <tenant> "<documento>" listo`. Los ítems `[confirmar con GT]` en fondos CORFO deben validarse contra las bases antes de dar el paquete por cerrado.

## 2. Cierre y envío
Solo si el QA está sin alertas **y el paquete de postulación está completo**:
- Confirma pago de arancel → `comprobante_arancel_pago`, `numero_transaccion_arancel`.
- Envío formal en plataforma Corfo → `comprobante_envio_ley_id`; pon `enviado = true` y `meta.paso_actual = "ENVIADO"`.

## 3. Generar el documento final
Genera el Formulario Ley I+D como documento entregable:
```bash
python3 render/formulario.py <tenant>     # → proyectos/<tenant>/formulario-ley-id.md (+ .docx si hay pandoc)
```
Es un borrador de apoyo (revisar contra la plataforma oficial). La planilla oficial Gantt/Presupuesto `.xlsx` la arma el consultor (ver `plantillas/README.md`).

**DoD:** las 4 reglas en `ok` (o justificadas), **paquete de postulación completo** (`postulacion.py estado` sin faltantes), formulario generado, envío realizado antes de la fecha límite y certificado de recepción guardado. Valida y renderiza.
