---
name: mn-form-perfil
description: Paso PERFIL del flujo de financiamiento GT — SOLO fondos CORFO. Fase 1 (Perfil de Proyecto), previa y obligatoria a la formulación completa (Fase 2). Genera el Perfil condensado desde el caso (eval_p4), lo deja listo para presentar, y gestiona el gate de retroalimentación antes de habilitar FORM_W1. Escribe el bloque perfil_corfo. Lo invoca el orquestador mn-orquestar tras un GO cuando el fondo es CORFO.
---

# PERFIL — Fase 1 de los CORFO (Perfil de Proyecto)

**Solo para fondos CORFO** (Crea y Valida, Consolida, Capital Humano, Innova Alta Tec). Ley I+D **no** tiene Perfil → si el fondo es Ley I+D, este paso se omite y se va directo a FORM_W1.

**Por qué existe:** los CORFO exigen una **Fase 1 (Perfil de Proyecto)** obligatoria antes de la postulación completa. Es una versión **condensada** que recibe **retroalimentación no vinculante** del Subcomité. **No se puede postular a Fase 2 sin haber pasado por Fase 1.**

**Inputs:** el **fondo elegido** (`meta.instrumento_objetivo` / instrumento del comité), `eval_p4` (el caso: problema, objetivo SMART, estado del arte, perfil de subsidios), la spec del fondo (`motor-reglas/formularios.json` → `<fondo>.fase_previa` y `secciones`).

## Paso a paso
1. **Confirma que el fondo es CORFO** (`fondos.<fondo>.paradigma == "subsidio_concursable"`). Si es `certificacion_id` (Ley I+D), NO apliques este paso.
2. **Genera el Perfil condensado** desde `eval_p4`, cubriendo el **núcleo** que evalúa el Subcomité en Fase 1: **problema/diagnóstico · mercado objetivo · solución (metodología + novedad) · capacidades**. Es una síntesis (no el formulario completo). Respeta el foco del fondo (p.ej. Capital Humano = el desafío + la persona; Consolida = escalamiento/negocio).
3. **Escribe `perfil_corfo`**: `{ fondo, secciones: [{id, titulo, respuesta}], enviado: false, feedback_recibido: false }`. Pon `meta.paso_actual = "PERFIL"`, valida y renderiza.
4. **Entrega al consultor**: dile que **presente el Perfil** en la plataforma CORFO y que **quedará a la espera de la retroalimentación** del Subcomité (p.ej. Crea y Valida ~14 días hábiles; Innova incluye una reunión). Marca `enviado = true` + `fecha_envio` al presentarlo.
5. **Genera el paquete de postulación** (esquema de gestión del fondo) para ir reuniendo documentos desde ya, en paralelo a la espera del feedback:
   ```bash
   python3 tools/postulacion.py scaffold <tenant>
   ```
   Arma `proyectos/<tenant>/postulacion/` + `CHECKLIST.md` con las carpetas/documentos que exige el fondo CORFO (Perfil, formulario, presupuesto/Gantt, CVs, antecedentes legales, declaraciones, cartas de compromiso…), distinguiendo cliente/brinca/sistema. Idempotente. Menciónale al consultor qué documentos del **cliente** ir pidiendo (los `[confirmar con GT]` conviene validarlos contra las bases). El paquete **bloquea el envío** (FORM_W5) si falta algo obligatorio.

## Gate de retroalimentación (humano, obligatorio)
El flujo **se detiene aquí** hasta que llegue el feedback. Cuando el consultor traiga la retroalimentación del Subcomité:
- Registra `retroalimentacion` (texto del feedback) y pon `feedback_recibido = true`.
- Incorpora los ajustes del feedback al caso antes de la Fase 2.

**El orquestador NO inicia FORM_W1 mientras `perfil_corfo.feedback_recibido != true`.**

**DoD:** `perfil_corfo` con el Perfil condensado redactado; `enviado`/`feedback_recibido` reflejando el estado real. Solo con `feedback_recibido = true` se habilita la Fase 2.
