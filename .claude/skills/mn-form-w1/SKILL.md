---
name: mn-form-w1
description: Paso FORM_W1 del flujo de financiamiento GT (Fase 2 — Formulación, Semana 1). Kick-off de formulación y arquitectura técnica: redacta título, resumen, contexto técnico y objetivo general del formulario Ley I+D. Solo se ejecuta si la compuerta de EVAL_P5 fue GO. Escribe el bloque form_w1. Lo invoca el orquestador mn-orquestar.
---

# FORM_W1 — Kick-Off y Arquitectura Técnica (Semana 1)

> **Precondición dura**: `eval_p5.compuerta == "GO"`. Si no, NO ejecutar (Índice Maestro).
> **Precondición CORFO**: si el fondo es CORFO (`subsidio_concursable`), FORM_W1 (Fase 2) **solo inicia con `perfil_corfo.feedback_recibido == true`** — antes va el paso PERFIL (`mn-form-perfil`). Ley I+D no tiene Perfil y entra directo.

**Objetivo:** completar la Sección 1 del formulario del fondo (título, resumen, contexto técnico y objetivo general — transversal). El consultor redacta de forma autónoma; el cliente valida el relato en la reunión semanal (1h).

**Inputs:** `eval_p3.perfil_tecnico_proyecto_v2`, `eval_p4` (objetivo SMART, estado del arte, Frascati).

## Paso 0 — Generar el paquete de postulación (esquema de gestión)
Al **entrar a formulación** (Ley I+D entra aquí directo; los CORFO ya lo generaron en PERFIL), crea el árbol de carpetas + el CHECKLIST del fondo:
```bash
python3 tools/postulacion.py scaffold <tenant>
```
Esto arma `proyectos/<tenant>/postulacion/` (una carpeta por documento exigido) y `CHECKLIST.md`, distinguiendo qué provee el **cliente**, qué arma **brinca** y qué genera el **sistema** (formulario técnico, estado del arte, plan de trabajo, arancel — se marcan solos a medida que el flujo los produce). Es **idempotente**: re-córrelo tras cada semana para refrescar el estado; preserva lo marcado a mano. Menciónale al consultor qué documentos del **cliente** hay que ir pidiendo (aparecen como pendientes) — se gestionan durante toda la Fase 2 y **bloquean el envío** (FORM_W5) si faltan.

**Productos (`form_w1`), respetando los límites del formulario:**
- `titulo_proyecto` (**≤100 car.** — dato duro del formulario): breve y descriptivo. Cuenta los caracteres; si te pasas, acorta.
- `resumen_proyecto` (≤2000): síntesis problema + desafío + objetivo I+D.
- `contexto_tecnico_proyecto` (≤4000): causas del problema, efectos industriales, relevancia, respaldado por fuentes/papers (del estado del arte verificado).
- `objetivo_general_proyecto` (≤1000): estructura *Verbo + Qué + Cómo + Para qué*. **Hereda de `eval_p4.objetivo_general_smart`** (regla de heredabilidad del Índice Maestro: parte de ese texto, no lo reinventes).
- `clasificacion_actividades`: [Investigación / Desarrollo Experimental / Ambas]. Determina la Ruta de FORM_W2.

**DoD:** bloque básico aprobado por el cliente y guardado. `meta.paso_actual = "FORM_W1"`. Valida, **chequea límites** (`python3 render/render.py <tenant> --limites`) y renderiza.
