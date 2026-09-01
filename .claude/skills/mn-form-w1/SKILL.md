---
name: mn-form-w1
description: Paso FORM_W1 del flujo de modelo de negocio (Fase 2 — redacción). Arquitectura de la narrativa: redacta el hilo problema/oportunidad → mercado objetivo → propuesta de valor → diferenciación que conecta el modelo con lo que pide el fondo. Solo se ejecuta si la compuerta de EVAL_P5 fue SÓLIDO. Escribe el bloque narrativa. Lo invoca el orquestador mn-orquestar.
---

# FORM_W1 — Arquitectura de la narrativa

> **Precondición dura**: `revision_viabilidad.compuerta == "SÓLIDO"`. Si no, NO ejecutar.
> **Precondición Fase 1**: si el fondo tiene Perfil de Proyecto (Crea y Valida, Innova Alta
> Tecnología), FORM_W1 **solo inicia con `perfil_corfo.feedback_recibido == true`** — antes
> va el paso PERFIL (`mn-form-perfil`). Consolida y Expande y Capital Humano entran directo.

**Objetivo:** fijar el **hilo conductor** que atraviesa todas las secciones de mercado /
modelo / escalamiento: el problema de mercado, a quién apunta, qué propone y por qué es
distinto. Es la arquitectura sobre la que FORM_W2 redacta cada sección del fondo.

**Inputs:** `modelo_negocio` (Canvas, unit economics), `investigacion_mercado` (tamaño de
mercado, competidores, precios), `perfil_comercial` (problema/oportunidad, resultado de
negocio).

## Paso 0 — Generar el paquete de entregables (si no se generó en PERFIL)
Consolida y Expande / Capital Humano entran aquí directo, así que crea el árbol + checklist:
```bash
python3 tools/postulacion.py scaffold <tenant>
```
Arma `proyectos/<tenant>/postulacion/` (una carpeta por entregable de modelo de negocio) y
`CHECKLIST.md`, distinguiendo qué provee el **cliente**, qué arma el **consultor** y qué
genera el **sistema**. Idempotente: re-córrelo tras cada paso.

**Productos (`narrativa`), respetando los límites:**
- `titulo_proyecto` (**≤200 car.**): breve y descriptivo.
- `resumen` (≤2000): síntesis problema + mercado + propuesta de valor + resultado esperado.
- `problema_oportunidad`: el problema de mercado **dimensionado con cifras verificadas** (de
  `investigacion_mercado`), no adjetivos.
- `mercado_objetivo`: a quién apunta — segmento, tamaño (TAM/SAM/SOM con su método y
  fuentes), geografía, y por qué es alcanzable para el cliente. Marca los supuestos.
- `propuesta_valor`: qué resuelve y para quién, anclado al Canvas.
- `diferenciacion`: qué lo hace distinto/mejor vs. los competidores y sustitutos
  identificados (`investigacion_mercado.competidores`). La novedad técnica la complementa GT.

**Escritura para el consultor**: expande cada sigla al primer uso y suma al `glosario` los
términos de negocio o del rubro no obvios.

**DoD:** `narrativa` redactada y aprobada por el cliente, con cifras trazables y supuestos
marcados. `meta.paso_actual = "FORM_W1"`. Valida, chequea límites y renderiza.
