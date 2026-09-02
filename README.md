# piloto-modelo-negocio — la herramienta (vista técnica)

Piloto **aislado**. Adaptación del motor de formulación de financiamiento de la iniciativa
F19 (herramienta agéntica "GTF") para que, en vez de formular postulaciones a Ley I+D,
**construya modelos de negocio** de proyectos de innovación y **redacte las secciones de
modelo de negocio / mercado / escalamiento** de los formularios de subsidios CORFO (Crea y
Valida, Innova Alta Tecnología, Consolida y Expande, Capital Humano).

> 👤 **¿Vas a usar la herramienta?** Empieza por **[GUIA-USUARIO.md](GUIA-USUARIO.md)**
> (pendiente de actualizar). Este README es la vista técnica.
>
> **Aislado:** git local propio, sin conexión al repo brinca ni a GitHub. `proyectos/`
> arranca vacío, sin datos de clientes. Se puede romper y rehacer: se commitea seguido.

## Componentes
| Carpeta / archivo | Qué es |
|---|---|
| `CLAUDE.md` | **Instrucciones del agente** (rol de orquestador, flujo P1…P5 + W1…W5, reglas transversales). Se carga al lanzar `claude` desde aquí. |
| `.claude/skills/` | Pasos del flujo, prefijo `mn-`: `mn-nuevo-proyecto`, `mn-orquestar`, `mn-estado`, Fase 1 (`mn-eval-reunion-1`, `-deep-research-1`, `-reunion-2`, `-preparar-caso`, `-comite`), `mn-form-perfil` (Fase 1 CORFO), Fase 2 (`mn-form-w1`…`w5`), `mn-qa-veracidad`, `mn-kb-agregar` |
| `.claude/agents/` | Agentes reutilizables: `mn-deep-researcher` (investigador de mercado), `mn-qa-veracidad` (verificador adversarial de cifras) |
| `motor-reglas/` | Motor determinista: `parametros.json` (umbrales — **POR VALIDAR con ing. comercial**) + `reglas.py` (mercado, unit economics, proyección, compuerta de viabilidad, QA de coherencia) · `formularios.json` (secciones del formulario por fondo, con flag `en_alcance_piloto`) · `documentos_postulacion.json` (manifiesto de entregables de modelo de negocio por fondo) |
| `expediente.schema.json` | Contrato del estado de un caso: `perfil_comercial` → `investigacion_mercado` → `supuestos_modelo` → `modelo_negocio` → `revision_viabilidad` → `narrativa` → `formulario_oficial` → `plan_escalamiento` → `impacto_continuidad` → `qa_entrega` |
| `render/` | `render.py` (expediente→md, con Panel del consultor), `formulario.py`, `gantt.py`. **Pendiente de adaptar** (bloque siguiente). |
| `tools/` | `browse.mjs` (navegador), `fuentes.json`/`.py` (fuentes de mercado), `kb.py` (base de conocimiento), `postulacion.py` (paquete de entregables + CHECKLIST por fondo), `estado`/`bitacora`/`panel` (flujo y sesiones) |
| `kb/` | Base de conocimiento transversal de mercado (informes, comparables, benchmarks): clasificada por **sector económico** + tipo de fuente. **Arranca vacía.** |
| `proyectos/` | Una carpeta por caso (aislada, gitignoreada). Vacío; se crean con `mn-nuevo-proyecto`. Al entrar a Fase 2 se agrega `postulacion/` (entregables + `CHECKLIST.md`). |
| `SETUP.md` · `setup/` · `.mcp.json` · `package.json` | Instalación y configuración |

## Estado del piloto

### Sesión 2026-09-01 — adaptación financiamiento I+D → modelo de negocio

**TAREA 1 — renombre de prefijo** (`11858c0`): 16 skills + 2 agentes `gtf-*` → `mn-*`,
frontmatter y todas las referencias cruzadas.

**TAREA 2 — adaptación de contenido**, por bloques:

| Bloque | Commit | Qué cambió |
|---|---|---|
| `CLAUDE.md` | `cc7966a` | Rol = asistente de modelo de negocio; flujo P1…P5 (construir el modelo) + W1…W5 (redactar secciones); compuerta **SÓLIDO / AJUSTAR / INVIABLE / DEVOLVER**; 12 reglas transversales (determinismo del motor, anclar cifras de mercado a fuente verificable, QA independiente, supuesto ≠ dato). Equipo/capacidades del beneficiario queda fuera del piloto (lo cubre F19). Sin envío irreversible. |
| `expediente.schema.json` | `f6774dc` | Bloques `eval_p*`/`form_w*` → bloques de modelo de negocio. `unit_economics` separa ENTRADAS de SALIDAS del motor. Eliminado: Frascati, elegibilidad, arancel, TRL, profesional acreditador, encuesta Ley I+D. |
| `motor-reglas/` | `590cf93` · `fca12da` | `reglas.py`: `mercado_coherencia`, `unit_economics`, `proyeccion(_escenarios)`, `encaje_mercado`, `indicadores_viabilidad`, `compuerta_viabilidad`, `qa_coherencia_modelo` (se conserva `coherencia_cifras_cliente`). Nuevo `parametros.json` (umbrales, reemplaza `instrumentos.json`). `formularios.json` sin `ley_id`, cada sección con `en_alcance_piloto`. `documentos_postulacion.json` acotado a entregables de modelo de negocio. Tests pasan. |
| Skills — Lote 1 (andamiaje) | `2329f11` | `mn-orquestar` (flujo nuevo, tabla paso→skill→bloque, gates), `mn-nuevo-proyecto` (fondos CORFO, entradas: proyecto de innovación + datos comerciales), `mn-estado`, `mn-deep-researcher` + `mn-qa-veracidad` (investigación/verificación **de mercado**), `mn-kb-agregar`. `tools/fuentes.json` → fuentes de mercado (INE, Banco Central, SII, CMF, Mercado Público, gremios, prensa de negocios, competidores). `kb/` reseteada; taxonomía por sector; plantillas `informe-mercado` y `comparable` (reemplazan paper/patente); ~229 fichas F19 eliminadas. |
| Skills — Lote 2 (Fase 1) | `cb8b88b` | `mn-eval-reunion-1` → `perfil_comercial`; `mn-eval-deep-research-1` → `investigacion_mercado` (TAM/SAM/SOM, competidores, precios); `mn-eval-reunion-2` → `supuestos_modelo`; `mn-eval-preparar-caso` → `modelo_negocio` (Canvas + llamadas al motor); `mn-eval-comite` → `revision_viabilidad` (compuerta del motor). |
| Skills — Lote 3 (Fase 2) | `06bbd0f` | `mn-form-perfil` (Perfil CORFO acotado a modelo de negocio); `mn-form-w1` → `narrativa`; `mn-form-w2` → `formulario_oficial` (solo secciones `en_alcance_piloto`); `mn-form-w3` → `plan_escalamiento`; `mn-form-w4` → `impacto_continuidad`; `mn-form-w5` → `qa_entrega` (entrega, sin envío). |

### Sesión 2026-09-02

| Bloque | Commit | Qué cambió |
|---|---|---|
| `render/*` + `tools/*.py` | `bdab1d4` | `render.py` reescrito (Panel del consultor + secciones por bloque nuevo; `--formulario` chequea solo `en_alcance_piloto`); `gantt.py` → Unit economics + Proyección + Hitos; `formulario.py` → `formulario-modelo-negocio.md`. `estado.py`/`panel.py`: PASOS/compuerta/`ENTREGADO`. `postulacion.py`: fondo desde `meta.instrumento_objetivo`. Shim UTF-8 en la salida (consola Windows). Probado con expediente sintético completo. |
| Docs de raíz | `<este commit>` | `SETUP.md`, `COMO-CORRER.md`, `GUIA-USUARIO.md`, `setup/setup.sh` reescritos para el flujo de modelo de negocio. |

### Pendiente
1. **Validación con ingeniería comercial** — los umbrales de `motor-reglas/parametros.json`
   (margen de contribución mínimo, LTV/CAC, payback, penetración de SOM) y la guía de
   redacción fina por sección CORFO (`formularios.json` lo marca como pendiente del equipo GT).
2. **Prueba con un caso real** end-to-end.

Cómo correrlo: **[COMO-CORRER.md](COMO-CORRER.md)**.
