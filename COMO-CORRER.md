# Cómo correr el piloto

Piloto de **construcción de modelos de negocio** para las secciones de mercado / modelo /
escalamiento de subsidios CORFO. Adaptación aislada del motor de formulación de
financiamiento (F19). Ver [README.md](README.md) para la vista técnica completa y el estado.

## Estructura

```
piloto-modelo-negocio/
├── GUIA-USUARIO.md         ← punto de entrada para el consultor
├── CLAUDE.md               ← instrucciones del agente (rol, flujo, reglas transversales)
├── .claude/skills/         skills nativos Claude Code (prefijo mn-)
│   ├── mn-nuevo-proyecto/   onboarding: crea un caso (tenant) y guía al usuario
│   ├── mn-orquestar/        orquestador (recorre el flujo)
│   ├── mn-eval-reunion-1/   EVAL_P1 — Reunión #1 → perfil comercial
│   ├── mn-eval-deep-research-1/  EVAL_P2 — Investigación de mercado + QA
│   ├── mn-eval-reunion-2/   EVAL_P3 — Reunión #2 → supuestos del modelo
│   ├── mn-eval-preparar-caso/  EVAL_P4 — construir el modelo (Canvas + unit economics)
│   ├── mn-eval-comite/      EVAL_P5 — revisión de viabilidad + compuerta
│   ├── mn-form-perfil/      PERFIL — Fase 1 CORFO (Crea y Valida / Innova AT)
│   ├── mn-form-w1…w5/       Fase 2 — redacción de secciones + entrega
│   ├── mn-qa-veracidad/     QA de veracidad — verifica cifras de mercado
│   └── mn-estado/           estado / resumen / retomar de un caso o la cartera
├── .claude/agents/         mn-deep-researcher (investigador de mercado) · mn-qa-veracidad
├── motor-reglas/           reglas.py (mercado, unit economics, proyección, compuerta) +
│                            parametros.json (umbrales) + formularios.json + documentos_postulacion.json
├── tools/                  browse.mjs (navegador), fuentes.json/.py (fuentes de mercado),
│                            kb.py (base de conocimiento), postulacion.py, estado/bitacora/panel
├── expediente.schema.json  contrato del estado (los datos tipados que se heredan entre pasos)
├── render/                 render.py (expediente→md), formulario.py, gantt.py
├── kb/                     base de conocimiento de mercado (índice + grafo). Arranca vacía.
└── proyectos/<tenant>/     un caso aislado (multitenant, gitignoreado)
    ├── entradas/            BUZÓN: inputs del cliente (reunion-1.md, proyecto.md, datos-comerciales.md, docs…)
    ├── expediente.json       estado (contrato)
    └── expediente.md         render legible (generado)
```

## Flujo

1. Crea el caso con `mn-nuevo-proyecto`: carpeta en `proyectos/<tenant>/` con el buzón
   `entradas/` y un `expediente.json` semilla (`meta.tenant`, `meta.paso_actual = "INICIO"`,
   `meta.instrumento_objetivo` = el fondo CORFO).
2. Deja en `entradas/` las notas de la Reunión #1, la descripción del proyecto de innovación
   (`proyecto.md`) y los datos comerciales (`datos-comerciales.md`).
3. **Invoca el orquestador** (`mn-orquestar`) apuntando al tenant. Decide el paso según
   `meta.paso_actual`, invoca el subagente del paso, valida y renderiza:
   - `INICIO` → EVAL_P1 (perfil comercial)
   - `EVAL_P1` → EVAL_P2 (investigación de mercado + QA)
   - `EVAL_P2` → EVAL_P3 (supuestos) → EVAL_P4 (construir el modelo) → EVAL_P5 (compuerta)
   - compuerta **SÓLIDO** → Fase 2 (FORM_W1…W5) → **ENTREGADO**
4. Tras cada paso, el estado queda en `expediente.json` y la vista legible en `expediente.md`.

## Comandos (parte determinista)

```bash
python3 render/render.py <tenant> --validar     # valida contra el schema
python3 render/render.py <tenant>               # genera expediente.md
python3 render/render.py <tenant> --formulario  # completitud de las secciones en alcance
python3 render/render.py <tenant> --limites     # largo de campos vs. topes
python3 tools/estado.py <tenant>                # dónde va, qué falta
python3 tools/panel.py                          # la cartera completa
python3 motor-reglas/reglas.py --test           # autotest del motor
python3 motor-reglas/reglas.py --demo           # demo legible del motor
```

## Investigación de mercado (Deep Research)

La usa `mn-deep-researcher` con navegador real (`tools/browse.mjs`, Playwright) sobre el
registro `tools/fuentes.json` (INE, Banco Central, SII, CMF, Mercado Público, gremios,
prensa de negocios, sitios de competidores). `python3 tools/fuentes.py usables` lista las
activas. Todo hallazgo pasa por `mn-qa-veracidad` (verificación adversarial de cada cifra,
su año y su geografía).

## Sin datos de ejemplo

El piloto **arranca limpio**: `proyectos/` vacío y KB sin fichas. Para empezar un caso real
usa `mn-nuevo-proyecto`.
