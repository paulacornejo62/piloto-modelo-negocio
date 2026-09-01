# Base de conocimiento (KB) — mercado

Capa **compartida** entre todos los casos (la única que no es multitenant): informes de
mercado, empresas comparables, benchmarks de industria, estadísticas oficiales y regulación,
sistematizados como **fichas** clasificadas, con un **índice + grafo** propio. Se **consulta**
en la investigación de mercado y se **enriquece** en cada caso. **Arranca vacía.**

## Estructura

```
kb/
├── taxonomia.json  ← clasificación: sector económico (define la carpeta) + tipo de fuente
├── topicos.json    ← tópicos curados (capa de conexión temática) ↔ sector ↔ fichas
├── indice.json     ← índice + grafo: nodos (fichas) + aristas (relaciones)
├── originales/     ← PDFs/documentos originales descargados
└── fichas/
    ├── PLANTILLA-informe-mercado.md  ← informe / estadística: qué mercado dimensiona, cifras clave, método, limitaciones
    ├── PLANTILLA-comparable.md       ← empresa comparable / benchmark / regulación
    └── <slug-sector>/          ← una carpeta por sector (agroalimentario, mineria, tecnologia-software, transversal…)
        └── <id>.md              ← una ficha por fuente
```

**La ficha es rica, no un par de bullets** — se estructura según el tipo (ver plantillas).
Campos de honestidad en el frontmatter: `profundidad_lectura` (full-text | resumen |
metadata), `estado_evidencia` (verificado | parcial | no_verificado | supuesto), y en las
cifras de mercado siempre `anio_dato` y `geografia`. Regla: **abrir la fuente**; una cifra
global no dimensiona un mercado nacional.

## Clasificación
1. **Sector** (`sector`) — de `taxonomia.json`. **Define la carpeta** de la ficha
   (`fichas/tecnologia-software/`, etc.). `transversal` para benchmarks que aplican a
   cualquier sector.
2. **Tipo** (`tipo`) — `informe-mercado` | `estadistica-oficial` | `comparable` | `benchmark`
   | `regulacion`.
3. **Tópicos** (`topicos`) — capa de conexión temática: dos fichas se relacionan por tópico
   compartido. Crecen con el uso en `topicos.json`.

> Vocabularios en `taxonomia.json` / `topicos.json`. Si falta un sector/tópico, **agrégalo**
> ahí; no inventes variantes sueltas en las fichas.

## Vocabulario de relaciones (aristas)
`{origen, destino, tipo, nota}`. Tipos: `mismo_mercado` · `competidor_de` · `fuente_de`
(una es la fuente primaria que la otra cita) · `contradice` · `complementa`.

## Consultar y deduplicar (`tools/kb.py`)
```bash
python3 tools/kb.py listar
python3 tools/kb.py buscar --topico "<tema>" --tipo comparable   # consulta por TÓPICO
python3 tools/kb.py buscar --sector tecnologia-software --texto pricing
python3 tools/kb.py dedup "<título candidato>"   # ANTES de crear una ficha
python3 tools/kb.py ver <id>      # ficha + su vecindario (relaciones)
python3 tools/kb.py salud         # cobertura + huérfanos + brechas
python3 tools/kb.py autocablear   # deriva aristas desde las referencias [[ficha-id]] en el cuerpo
python3 tools/kb.py export        # grafo a Mermaid
```
> Enlaza fichas relacionadas en el cuerpo con `[[otra-ficha-id]]` y corre `autocablear`.
> **Agregar una fuente** (URL → ficha clasificada + dedup): skill `mn-kb-agregar`.
> **Enriquecimiento con dedup**: antes de crear una ficha corre `dedup`; si hay similar,
> **enlaza/actualiza** (agrega el caso a `proyectos:` y una arista) en vez de duplicar. La
> KB es transversal: el aprendizaje de mercado se acumula entre casos.
