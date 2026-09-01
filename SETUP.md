# Setup del sistema GTF

Deja la herramienta lista para usar en una máquina nueva. **Forma parte del sistema** (no del ambiente de quien lo desarrolló): cuando el tool se transfiera a un usuario, este corre el setup y queda operativo.

## Prerrequisitos
- **Python 3.10+** (`python3`)
- **Node 18+** y **npx** (para el navegador del Deep Research vía Playwright MCP)
- Opcional: **poppler** (`pdftotext`) para ingesta de PDFs escaneados — `brew install poppler` / `apt install poppler-utils`

## Instalación (un comando)
Desde la raíz del sistema (`sistema/`):
```bash
bash setup/setup.sh
```
Esto: instala las dependencias Python (`setup/requirements.txt`), descarga **Chromium** para Playwright, verifica el `.mcp.json` del navegador y corre un smoke test de validación.

## Qué deja configurado
| Componente | Para qué |
|---|---|
| Dependencias Python (`jsonschema`, `openpyxl`, `python-docx`, `python-pptx`, `pypdf`) | validación del expediente + ingesta documental |
| Chromium (Playwright) | navegación real en el Deep Research (Espacenet, INAPI, IEEE, etc.) |
| `.mcp.json` → Playwright MCP | expone el navegador como herramienta al correr Claude Code desde `sistema/` |

## Usar el tool
Corre Claude Code **desde `sistema/`** para que cargue el navegador y los skills:
```bash
cd sistema && claude
```
La primera vez, Claude Code pide aprobar el MCP server. Luego el orquestador (`mn-orquestar`) puede recorrer el flujo con Deep Research real + QA de veracidad.

> **Búsqueda profunda por API** (Exa/Tavily): opcional, no incluida (decisión de no usarla por ahora). Si se adopta, se agrega su MCP al `.mcp.json` con su API key y se documenta aquí.
