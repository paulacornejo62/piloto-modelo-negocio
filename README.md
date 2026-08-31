# sistema/ — la herramienta (Línea 2)

Lo que **se instala, se usa y se traspasa al usuario final**. Herramienta agéntica que acompaña la evaluación, formulación y postulación de proyectos a Ley I+D / CORFO.

> 👤 **¿Vas a instalar/usar la herramienta (consultor GT)?** Empieza por **[GUIA-USUARIO.md](GUIA-USUARIO.md)**. Este README es la vista técnica.
>
> 🚦 **GUARDIÁN (regla operativa fundamental):** aquí va **solo** lo que se instala/usa/traspasa. El **diseño, las decisiones, las pruebas y las validaciones** de *nuestro* proceso viven en [`../desarrollo/`](../desarrollo/) (`diseno/`, `pruebas/`, `validacion/`). Ante la duda, no va aquí.

## Componentes
| Carpeta / archivo | Qué es |
|---|---|
| `CLAUDE.md` | **Instrucciones del agente** al operar la herramienta (rol de orquestador, flujo, reglas transversales). Se carga solo al lanzar `claude` desde aquí. |
| `.claude/skills/` | Pasos del flujo: onboarding, orquestador, EVAL_P1…P5, PERFIL (Fase 1 CORFO), FORM_W1…W5, QA de veracidad, KB |
| `.claude/agents/` | Agentes reutilizables: `gtf-deep-researcher`, `gtf-qa-veracidad` |
| `motor-reglas/` | Motor determinista: `instrumentos.json` + `reglas.py` (Frascati, elegibilidad, compuerta, QA formulación) · `formularios.json` (formulario oficial por fondo) · `documentos_postulacion.json` (manifiesto del paquete de postulación por fondo) |
| `expediente.schema.json` | Contrato del estado de una postulación (los datos tipados que se heredan entre pasos) |
| `render/` | `render.py` (expediente→md, con **Panel del consultor** al inicio: resumen legible + glosario), `formulario.py` (Formulario Ley I+D), `gantt.py` (Gantt+Presupuesto) |
| `tools/` | `browse.mjs` (navegador), `fuentes.json`/`.py` (registro de fuentes), `kb.py` (base de conocimiento), `postulacion.py` (paquete de postulación: carpetas + CHECKLIST por fondo), `estado`/`bitacora`/`panel` (flujo y sesiones) |
| `kb/` | Base de conocimiento transversal (papers/patentes): estructura + taxonomía. **Arranca vacía**; se puebla con conocimiento real y validado al correr postulaciones. |
| `plantillas/` | Render de documentos finales |
| `proyectos/` | Una carpeta por postulación (aislada). Vacío al instalar; se crean con `gtf-nuevo-proyecto`. Al entrar a formulación se le agrega `postulacion/` (árbol de documentos + `CHECKLIST.md`). |
| `SETUP.md` · `setup/` · `.mcp.json` · `package.json` | Instalación y configuración |

## Diseño y estado
El diseño técnico (arquitectura, contexto operacional), el mapa de fidelidad flujo↔agentes y el estado de avance viven en **[`../desarrollo/diseno/`](../desarrollo/diseno/)** — porque son parte de cómo lo construimos, no del producto instalado.

Cómo correrlo: **[COMO-CORRER.md](COMO-CORRER.md)**.
