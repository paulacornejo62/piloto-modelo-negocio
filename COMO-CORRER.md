# Cómo correr el sistema (v1 — esqueleto caminante)

> Estado v1: orquestador + estado + EVAL_P1 + EVAL_P2 + KB + render. Cubre 2 de los 10 pasos; el resto se replica del mismo patrón.

## Estructura

```
sistema/
├── GUIA-USUARIO.md         ← punto de entrada para el consultor (instalar + usar)
├── .claude/skills/         skills nativos Claude Code
│   ├── gtf-nuevo-proyecto/   onboarding: crea una postulación (tenant) y guía al usuario
│   ├── gtf-orquestar/        orquestador (recorre el flujo)
│   ├── gtf-eval-reunion-1/   EVAL_P1 — Reunión #1 → Perfil Preliminar
│   ├── gtf-eval-deep-research-1/  EVAL_P2 — Deep Research #1 → Minuta v1 + fichas KB
│   ├── gtf-qa-veracidad/     QA de veracidad — verifica hallazgos, descarta alucinaciones
│   └── gtf-estado/           estado / resumen / retomar de una postulación o la cartera
├── .claude/agents/         agentes reutilizables: gtf-deep-researcher · gtf-qa-veracidad
├── tools/                  utilidades CLI: browse.mjs (navegador), fuentes.json/.py (registro de
│                            fuentes), kb.py (base de conocimiento), estado/bitacora/panel (flujo)
├── expediente.schema.json  contrato del estado (JSON Schema, con evidencia/cobertura)
├── render/render.py        validación + render JSON → expediente.md (determinista)
├── SETUP.md + setup/       instalación transferible (deps, Chromium, smoke test)
├── .mcp.json               Playwright MCP (navegador para Deep Research)
├── kb/                     base de conocimiento compartida (índice + grafo propio)
├── motor-reglas/           (vacío — compuertas/elegibilidad, GTF-06)
├── plantillas/             (vacío — render de documentos finales)
└── proyectos/<tenant>/     una postulación aislada (multitenant)
    ├── entradas/            BUZÓN: inputs del cliente (reunion-1.md, reunion-2.md, docs…)
    ├── expediente.json       estado (contrato)
    └── expediente.md         render legible (generado)
```

## Flujo

1. Crea el tenant: carpeta en `proyectos/<tenant>/` con el buzón `entradas/` (deja ahí las notas de la Reunión #1 y cualquier doc del cliente) y un `expediente.json` semilla (`{"meta":{"tenant":"<t>","paso_actual":"INICIO"}}`).
2. **Invoca el orquestador** (skill `gtf-orquestar`) apuntando al tenant. Él decide el paso según `meta.paso_actual`, invoca el subagente del paso, valida y renderiza.
   - `INICIO` → EVAL_P1 (perfil preliminar)
   - `EVAL_P1` → EVAL_P2 (deep research + fichas KB)
3. Tras cada paso, el estado queda en `expediente.json` y la vista legible en `expediente.md`.

## Comandos (parte determinista)

```bash
python3 render/render.py <tenant> --validar   # valida contra el schema
python3 render/render.py <tenant>             # genera expediente.md
```

> **Nota sobre skills**: viven en `sistema/.claude/skills/`. Se vuelven invocables como skills nativos cuando el sistema corre como su **propio proyecto Claude Code** (raíz = `sistema/`, o el repo dedicado al graduar en el traspaso). Dentro del workspace Brinca puedes ejercitarlos pasándole a un subagente el `SKILL.md` del paso + la ruta del tenant.

## Herramientas de investigación (Deep Research)

El Deep Research (EVAL_P2/P4) **exige navegación real**, no WebSearch (ver arquitectura). Playwright (Chromium) es dependencia del tool (`npm install` + `npx playwright install chromium`, lo hace `setup.sh`). Dos vías para usar el navegador:

- **Por Bash (sin reiniciar)** — los skills/agentes corren scripts Node con Playwright (`require('playwright')` desde `sistema/`). Funciona en la sesión actual, no necesita MCP. Es la vía por defecto para *ejecutar* el Deep Research.
- **Por MCP (interactivo)** — [`.mcp.json`](.mcp.json) expone Playwright como herramientas del agente; se carga al arrancar Claude Code **desde esta carpeta** (`cd sistema && claude`). Útil para exploración interactiva.
- **Pendiente (GTF-12)**: opcionalmente, MCP de búsqueda profunda por API (Exa/Tavily) para recuperación semántica con texto completo (requiere API key).

## Sin datos de ejemplo
El sistema **arranca limpio**: `proyectos/` vacío y KB sin fichas. El fixture de prueba (caso ficticio `_ejemplo`) vive en [`../desarrollo/pruebas/`](../desarrollo/pruebas/), no aquí — es material de *nuestro* desarrollo, no del producto. Para empezar una postulación real usa `gtf-nuevo-proyecto`.
