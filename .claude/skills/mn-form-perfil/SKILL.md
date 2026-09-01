---
name: mn-form-perfil
description: Paso PERFIL del flujo de modelo de negocio — SOLO Crea y Valida / Innova Alta Tecnología. Fase 1 (Perfil de Proyecto), previa y obligatoria a la Fase 2. Genera las secciones de modelo de negocio / mercado del Perfil condensado desde el modelo (modelo_negocio + investigacion_mercado), lo deja listo para presentar, y gestiona el gate de retroalimentación antes de habilitar FORM_W1. Escribe el bloque perfil_corfo. Lo invoca el orquestador mn-orquestar tras un SÓLIDO cuando el fondo tiene Fase 1.
---

# PERFIL — Fase 1 CORFO (Perfil de Proyecto)

**Solo para Crea y Valida e Innova Alta Tecnología** (los otros dos fondos no tienen un
Perfil de Proyecto previo → se va directo a FORM_W1).

**Por qué existe:** esos fondos exigen una **Fase 1 (Perfil de Proyecto)** obligatoria antes
de la postulación completa. Es una versión **condensada** que recibe **retroalimentación no
vinculante** del Subcomité. **No se puede pasar a Fase 2 sin haber pasado por Fase 1.**

**Inputs:** el **fondo elegido** (`meta.instrumento_objetivo`), `modelo_negocio` (Canvas,
unit economics, proyección), `investigacion_mercado` (tamaño de mercado, competidores), la
spec del fondo (`motor-reglas/formularios.json` → `<fondo>.fase_previa` y `secciones` con
`en_alcance_piloto`).

## Paso a paso
1. **Confirma que el fondo tiene Fase 1** (`fondos.<fondo>.fase_previa` menciona Perfil de
   Proyecto: `crea_valida`, `innova_alta_tecnologia`). Si no, NO apliques este paso.
2. **Genera el Perfil condensado** — solo la parte de **modelo de negocio / mercado** que le
   toca al piloto: **problema/diagnóstico · mercado objetivo (TAM/SAM/SOM) · propuesta de
   valor y diferenciación · escalabilidad**. Es una síntesis breve, no el formulario
   completo. Deriva de `modelo_negocio` + `investigacion_mercado`; marca los supuestos.
   Las secciones técnicas y de equipo del Perfil las completa el equipo GT.
3. **Escribe `perfil_corfo`**: `{ fondo, secciones: [{id, titulo, respuesta}], enviado:
   false, feedback_recibido: false }`. Pon `meta.paso_actual = "PERFIL"`, valida y renderiza.
4. **Entrega al consultor**: que **presente el Perfil** en la plataforma CORFO y quede a la
   espera de la retroalimentación del Subcomité (Crea y Valida ~14 días hábiles; Innova
   incluye una reunión). Marca `enviado = true` + `fecha_envio` al presentarlo.
5. **Genera el paquete de entregables del modelo de negocio** para ir armándolo en paralelo:
   ```bash
   python3 tools/postulacion.py scaffold <tenant>
   ```
   Arma `proyectos/<tenant>/postulacion/` + `CHECKLIST.md` con las carpetas/documentos de
   modelo de negocio del fondo (investigación de mercado, Canvas + unit economics,
   proyección, plan de escalamiento, secciones del formulario, impacto/continuidad,
   supuestos a confirmar) + los insumos del cliente/consultor. Idempotente. Menciónale al
   consultor qué insumos del **cliente** ir pidiendo. El paquete **bloquea la entrega**
   (FORM_W5) si falta algo obligatorio.

## Gate de retroalimentación (humano, obligatorio)
El flujo **se detiene aquí** hasta que llegue el feedback. Cuando el consultor lo traiga:
- Registra `retroalimentacion` (texto) y pon `feedback_recibido = true`.
- Incorpora los ajustes del feedback al modelo antes de la Fase 2.

**El orquestador NO inicia FORM_W1 mientras `perfil_corfo.feedback_recibido != true`.**

**DoD:** `perfil_corfo` con las secciones de modelo de negocio / mercado redactadas;
`enviado`/`feedback_recibido` reflejando el estado real. Solo con `feedback_recibido = true`
se habilita la Fase 2.
