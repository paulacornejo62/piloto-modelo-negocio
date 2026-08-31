# tools/ — acceso a navegador para el Deep Research

`browse.mjs` (Playwright/Chromium) le da al Deep Research y al QA navegación real. Correr desde `sistema/`.

## Modos
| Comando | Qué hace |
|---|---|
| `node tools/browse.mjs open "<url>" [maxChars]` | Abre y extrae título + texto (verificar una fuente). Límite por defecto 200.000 caracteres; si trunca **lo declara** en `truncado`/`aviso` con el total real. |
| `node tools/browse.mjs pat "<numero>"` | **UN documento de patente**: metadatos + **pliego de reivindicaciones COMPLETO** + descripción. **Úsalo SIEMPRE que vayas a afirmar algo sobre el alcance de una patente.** |
| `node tools/browse.mjs gp "<query>" [PAIS]` | **Google Patents** — busca y lista resultados. **Por defecto GLOBAL** (todos los países). `PAIS` es **opcional** y solo para verificación de *prior art nacional* (p.ej. `CL`); el estado del arte de novedad siempre es mundial. **Motor de patentes primario.** |
| `node tools/browse.mjs scholar "<query>"` | Google Académico (puede bloquear bots) |
| `node tools/browse.mjs espacenet\|inapi\|patentscope "<query>"` | Intenta el registro oficial y **reporta honestamente** si es accesible |

### Por qué existe `pat` (corregido 14-ago-2026)
`open` truncaba a **6.000 caracteres sin avisar**. Como un pliego de reivindicaciones pesa entre 6.000 y 30.000, todos los barridos de patentes venían **juzgando alcance sobre documentos cortados** — de ahí los errores repetidos que detectó el QA: una reivindicación conjuntiva leída como alternativa, dependencias mal atribuidas, segundas reivindicaciones independientes que no se veían. `pat` no recorta el pliego y además entrega:

- `titular_actual` **y** `titular_original` — pueden diferir por cesión (p.ej. `US6984694B2`: solicitante Johnson Polymer, titular hoy Clariant). Afirmar el titular equivocado es un error caro.
- `estado_legal` y `anticipada_expiracion` — evita afirmar "vigente" o "expirada" de memoria.
- `familia_paises` y `tiene_miembro_chileno` — responde de una si hay riesgo de infracción **en Chile**, que es lo que importa para operar acá. Una patente sin miembro chileno limita la novedad, no la operación.
- `n_reivindicaciones` y `claims_vacios` — si el pliego **no está expuesto** (habitual en publicaciones `CL`, donde Google Patents deja el andamiaje `Claims ()` vacío), lo dice explícito: sabes qué **divulga**, no qué **reclama**. Con eso NO se afirma alcance de infracción; hace falta INAPI, que es paso manual.

**Regla de lectura:** los *claims* definen el alcance de infracción; la *descripción* cuenta como divulgación y destruye novedad **aunque la patente esté expirada**. Repórtalos por separado.

## Registro de fuentes (`fuentes.json`) — fácil de manejar
**Dónde busca el Deep Research** vive en un solo archivo: `tools/fuentes.json` (papers + patentes, con estado y cómo consultarlas). Para **sumar una fuente** (otra API, página o servicio que use el equipo GT), agrega una entrada ahí; si es API/MCP, configúrala en `sistema/.mcp.json`.
```bash
python3 tools/fuentes.py resumen    # cobertura de un vistazo (cuántas usables, por estado)
python3 tools/fuentes.py usables    # solo las que se pueden recorrer ahora
python3 tools/fuentes.py listar     # todas, por estado
```
- **Papers (full-text):** el caballo de batalla es **PMC / Europe PMC / revistas open access** (PLOS, Frontiers, MDPI) → dan `profundidad_lectura: full-text`. PubMed da abstract/metadata; IEEE/ScienceDirect/Springer suelen quedar en paywall (`parcial`).
- **Patentes:** **Google Patents** es el motor primario; Espacenet/PatentScope están bot-bloqueados; **INAPI (Chile) es manual** para el FTO.
- Listas para configurar (requieren key): **EPO OPS** (patentes globales, cierra Espacenet), **Exa** y **Semantic Scholar** (papers).

## Paquete de postulación (`postulacion.py`) — gestión documental por fondo
Al **entrar a formulación**, cada fondo exige reunir un set de documentos (formulario, estado del arte, CVs, instrumento de representación, arancel, subcontratos…). `postulacion.py` genera —según el fondo— el árbol de carpetas y un **CHECKLIST** que distingue quién provee cada documento (**cliente** / **brinca** / **sistema**) y su estado, y **bloquea el envío** hasta que esté completo. El manifiesto por fondo vive en `motor-reglas/documentos_postulacion.json`. El estado vivo va en el bloque `postulacion` del expediente; `CHECKLIST.md` es su proyección.
```bash
python3 tools/postulacion.py vincular <tenant> "<url-o-id-drive>"  # AL INICIO: vincula la carpeta Drive del cliente
python3 tools/postulacion.py scaffold <tenant>              # crea/actualiza árbol + checklist (idempotente)
python3 tools/postulacion.py estado <tenant>                # % y faltantes (exit 1 si falta un obligatorio → gate)
python3 tools/postulacion.py marcar <tenant> "<doc>" listo  # el cliente/consultor entregó un documento
python3 tools/postulacion.py sync-drive <tenant>            # espejo a Drive: crea árbol + SUBE archivos (usa la carpeta vinculada)
```
Los documentos del **sistema** (formulario, estado del arte, plan de trabajo, arancel) se marcan solos a medida que el flujo los produce. En fondos CORFO, los ítems `[confirmar con GT]` deben validarse contra las bases del fondo antes de cerrar el paquete.

**Espejo a Drive (on-demand).** La carpeta se **vincula al inicio** (`vincular`, también lo hace `gtf-nuevo-proyecto`) y queda en `meta.drive_carpeta`. `sync-drive` crea bajo ella una raíz por tenant + una subcarpeta por documento, y **sube los archivos** que estén en `proyectos/<tenant>/postulacion/<carpeta>/` (local = fuente de verdad; lo ya subido se omite para no duplicar). Requiere `gws` autenticado. Si no hay carpeta vinculada, pásala con `--parent <folderId>`.

## Realidad de los buscadores de patentes (hallazgo GTF-14)
Probados con navegador real (2026-06-23):

| Registro | Resultado | Vía correcta |
|---|---|---|
| **Google Patents** | ✅ funciona; agrega familias EP/WO/US/CN/CL | usar `gp` (con filtro de país) |
| **Espacenet** | ❌ Cloudflare anti-bot (HTTP 403, incluso headed) | EPO **Open Patent Services (OPS)** — API REST, registro/OAuth gratuito |
| **WIPO PatentScope** | ❌ HTTP 403 | API/servicios WIPO o manual |
| **INAPI (Chile)** | ⚠️ formulario ASP.NET, sin API libre; no automatizable de forma fiable | **búsqueda manual** en buscadorpatentes.inapi.cl |

**Conclusión:** la cobertura de patentes se ancla en **Google Patents** (cubre la mayoría de familias). Los registros oficiales están bot-protegidos; los modos `espacenet/inapi/patentscope` existen para **declarar la cobertura con honestidad** (`no_accesible` / `requiere_manual`), no para extraer. Para una **FTO formal** (sobre todo patentes chilenas en INAPI), queda un **paso manual** o integrar la API de EPO OPS (mejora futura).

> No usamos técnicas de evasión anti-bot (stealth): frágil, en contra de los ToS y poco transferible. La honestidad de cobertura es parte del control de veracidad.
