---
name: mn-form-w5
description: Paso FORM_W5 del flujo de modelo de negocio (Fase 2 — redacción). QA de coherencia (reglas del motor) y entrega del paquete de entregables del modelo de negocio al consultor. NO hay envío en plataforma. Cierra la Fase 2. Escribe el bloque qa_entrega. Lo invoca el orquestador mn-orquestar.
---

# FORM_W5 — QA de coherencia y entrega

**Objetivo:** verificar la coherencia interna del paquete y entregarlo al consultor como
borrador de apoyo. **No hay envío irreversible en plataforma**: el consultor integra estas
secciones al formulario completo del fondo y revisa contra la plataforma antes de presentar.

**Inputs:** `narrativa`, `formulario_oficial`, `plan_escalamiento`, `impacto_continuidad`,
`modelo_negocio`, `investigacion_mercado`.

## 1. QA de coherencia (motor de reglas — obligatorio antes de entregar)
```bash
python3 -c "import sys, json; sys.path.insert(0,'motor-reglas'); import reglas; \
print(json.dumps(reglas.qa_coherencia_modelo( \
  mercado={'tam_clp':<TAM>,'sam_clp':<SAM>,'som_clp':<SOM>}, \
  penetracion_som_pct=<modelo_negocio.encaje_mercado.penetracion_som_pct>, \
  supuestos=<supuestos_modelo.supuestos>, \
  supuestos_a_confirmar=<impacto_continuidad.supuestos_a_confirmar>, \
  secciones_formulario=<formulario_oficial.secciones>, \
  cifras_formulario_cuadran=<bool>), ensure_ascii=False, indent=2))"
```
- **Reglas 1-4** (embudo de mercado TAM≥SAM≥SOM; proyección cabe en el SOM; supuestos sin
  confirmar registrados; secciones dentro del tope): las calcula el motor con los datos del
  expediente.
- **Regla 5** (las cifras citadas en el formulario cuadran con `modelo_negocio`): es
  **semántica** — debes **leer `formulario_oficial` y `narrativa`** y confirmar (booleano)
  si los números de mercado, precio y proyección coinciden con el modelo. El motor no la da
  por buena sin tu confirmación.
- Guarda el resultado en `qa_entrega.qa_coherencia`. **Si hay `alerta`, NO entregues**:
  vuelve al paso correspondiente a corregir; deja las que queden en `observaciones_abiertas`.

## 2. Completitud de las secciones en alcance (gate duro)
```bash
python3 render/render.py <tenant> --formulario
```
Todas las secciones `en_alcance_piloto: true` del fondo deben estar respondidas y dentro del
tope. Si sale **INCOMPLETO**: NO entregues — vuelve a FORM_W2.

## 3. Paquete de entregables completo (gate duro)
```bash
python3 tools/postulacion.py scaffold <tenant>   # re-deriva lo que ya generó el sistema
python3 tools/postulacion.py estado <tenant>     # exit 1 si falta algún obligatorio
```
Si **faltan obligatorios**: NO entregues — pide al cliente/consultor los insumos pendientes
(descripción del proyecto, datos comerciales) y márcalos al llegar:
`python3 tools/postulacion.py marcar <tenant> "<documento>" listo`.

## 4. Entrega
Solo si el QA está sin alertas **y** el paquete está completo:
- Genera el documento de las secciones redactadas:
  ```bash
  python3 render/formulario.py <tenant>     # → proyectos/<tenant>/formulario-modelo-negocio.md
  ```
- Guarda `qa_entrega = { qa_coherencia, entregado: true, fecha_entrega, paquete_path,
  observaciones_abiertas[] }`; pon `meta.paso_actual = "ENTREGADO"`.
- Entrega al consultor con un resumen de qué contiene, qué supuestos quedan por confirmar y
  qué secciones (fuera de alcance del piloto) debe completar el equipo GT antes de presentar.

**DoD:** reglas de coherencia en `ok` (o justificadas en `observaciones_abiertas`);
secciones en alcance completas y dentro de tope; paquete de entregables completo; documento
generado; entrega registrada. Valida y renderiza.
