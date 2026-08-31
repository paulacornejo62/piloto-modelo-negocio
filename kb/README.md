# Base de conocimiento (KB) — índice + grafo propio

Capa **compartida** entre todos los proyectos (única que no es multitenant): papers y patentes revisadas, sistematizadas como **fichas** clasificadas, con un **índice + grafo** propio (sin Obsidian). Se **consulta** en los Deep Research y se **enriquece** en cada postulación.

## Estructura

```
kb/
├── taxonomia.json  ← clasificación ESTÁNDAR (no inventada): OCDE Fields of Science +
│                     secciones IPC de patentes (+ vocabulario de relaciones). Ampliable.
├── topicos.json    ← tópicos curados (capa de conexión temática) ↔ área ↔ fichas
├── indice.json     ← índice + grafo: nodos (fichas) + aristas (relaciones)
├── originales/     ← PDFs originales (manejo por definir — ver originales/README.md)
└── fichas/
    ├── PLANTILLA-paper.md      ← plantilla RICA de paper (pregunta·hipótesis·metodología·resultados·conclusiones·limitaciones)
    ├── PLANTILLA-patente.md    ← plantilla RICA de patente (problema·reivindicaciones·solución·FTO)
    └── <slug-área>/        ← una carpeta por área OCDE (orden por área)
        └── <id>.md          ← una ficha por fuente
```

**La ficha es rica, no un par de bullets** — se estructura según el tipo (ver plantillas). Dos campos de honestidad en el frontmatter: `profundidad_lectura` (full-text | abstract | metadata — qué se leyó de verdad) y `estado_evidencia` (verificado | parcial | no_verificado). Regla: **leer el full-text siempre que sea accesible**; si solo hay abstract, marcarlo.

## Clasificación (dos capas estándar + tópicos)
1. **Área OCDE** (`area_oecd`) — Fields of Science del Manual de Frascati (el mismo de la evaluación). **Define la carpeta** de la ficha (`fichas/4-agricolas/`, etc.).
2. **IPC** (`ipc`, solo patentes) — Clasificación Internacional de Patentes; el código lo entrega Google Patents (p.ej. `A01K63`). No se inventa.
3. **Tópicos** (`topicos`) — capa de **conexión temática robusta**: dos fichas se relacionan por **tópico compartido**, no solo por citas. Crecen con el uso en `topicos.json`.

> Vocabularios en `taxonomia.json` / `topicos.json`. Si falta una categoría/tópico, **agrégalo** ahí (es ampliable); no inventes variantes sueltas en las fichas.

- **Índice/grafo** (`indice.json`): `nodos` (id + clasificación para filtrar) + `aristas` (relaciones explícitas).

## Vocabulario de relaciones (aristas)
`{origen, destino, tipo, nota}`. Tipos:
- `cita_a` — una fuente cita a otra.
- `misma_tecnologia` — abordan la misma tecnología/enfoque.
- `relacionada_con` — relación temática general.
- `contradice` — hallazgos opuestos.
- `complementa` — se complementan (p.ej. paper + producto que lo materializa).

## Consultar y deduplicar (`tools/kb.py`)
```bash
python3 tools/kb.py listar
python3 tools/kb.py buscar --topico "oxígeno" --tipo paper     # ← consulta por TÓPICO (conexión temática)
python3 tools/kb.py buscar --area agrícolas --texto hipoxia    # por área OCDE / texto
python3 tools/kb.py dedup "<título candidato>"   # ANTES de crear una ficha
python3 tools/kb.py ver <id>      # ficha + su vecindario (relaciones)
python3 tools/kb.py salud         # cobertura + huérfanos + GAP ANALYSIS (tópicos delgados, áreas sin patente, fichas solo-abstract)
python3 tools/kb.py autocablear   # deriva aristas del grafo desde las referencias [[ficha-id]] en el cuerpo (cero LLM)
python3 tools/kb.py export        # grafo a Mermaid (para visualizar)
```
> **Grafo (GTF-19, idea de GBrain):** enlaza fichas relacionadas en el cuerpo con `[[otra-ficha-id]]` y corre `autocablear` — la arista se crea sola. La adyacencia por **tópico compartido** ya vive en `topicos.json` (no se materializa como arista). `salud` reporta las **brechas** de la KB (qué falta cubrir).
**Agregar una fuente** (URL → ficha clasificada + dedup): skill `gtf-kb-agregar`.
- **Consulta** (en Deep Research): `buscar` para traer conocimiento análogo previo de cualquier proyecto.
- **Enriquecimiento con dedup**: antes de crear una ficha, corre `dedup`; si hay similar, **enlaza/actualiza** (agrega el proyecto a `proyectos:` y una arista) en vez de duplicar. La KB es transversal: el aprendizaje se acumula entre postulaciones.
