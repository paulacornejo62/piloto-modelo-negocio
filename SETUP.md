# Setup del piloto de modelo de negocio

Deja la herramienta lista para usar en una máquina nueva.

## Prerrequisitos
- **Python 3.10+** (`python3`)
- **Node 18+** y **npx** (para el navegador de la investigación de mercado vía Playwright)
- Opcional: **poppler** (`pdftotext`) para leer PDFs escaneados — `brew install poppler` / `apt install poppler-utils`

## Instalación (un comando)
Desde la raíz del piloto:
```bash
bash setup/setup.sh
```
Esto: crea un `.venv` e instala las dependencias Python (`setup/requirements.txt`), instala
las dependencias Node, descarga **Chromium** para Playwright, verifica el `.mcp.json` y corre
el autotest del motor de reglas.

## Qué deja configurado
| Componente | Para qué |
|---|---|
| Dependencias Python (`jsonschema`, `openpyxl`, `python-docx`, `pypdf`) | validación del expediente + planillas + lectura de documentos |
| Chromium (Playwright) | navegación real en la investigación de mercado (sitios de competidores, informes, estadísticas) |
| `.mcp.json` → Playwright MCP | expone el navegador como herramienta al correr Claude Code desde esta carpeta |

## Usar el tool
Corre Claude Code **desde esta carpeta** para que cargue el navegador y los skills `mn-`:
```bash
claude
```
La primera vez, Claude Code pide aprobar el MCP server. Luego el orquestador
(`mn-orquestar`) recorre el flujo: construir el modelo de negocio (Fase 1) y redactar las
secciones de mercado / modelo / escalamiento del formulario (Fase 2).
