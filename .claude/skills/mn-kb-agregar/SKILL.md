---
name: mn-kb-agregar
description: Agrega una fuente de mercado (informe, estadística oficial, empresa comparable, benchmark de industria, regulación) a la base de conocimiento transversal a partir de una URL o referencia. Lee la fuente, extrae el contenido estructurado, verifica duplicados y crea una ficha rica y clasificada + su nodo/relaciones. Invocar con "agrega a la KB <url>" o al cerrar una investigación de mercado.
---

# Agregar fuente de mercado a la base de conocimiento

Convierte una fuente en una **ficha rica, estructurada y clasificada** de la KB transversal.
Una ficha NO es un par de bullets: captura las cifras con su año y geografía, el método de
la fuente y sus limitaciones (informe), o el modelo de ingresos y la escala (comparable). La
veracidad manda.

## Principio: leer, no ojear
**Lee el contenido completo siempre que sea accesible** (abre el HTML/PDF), y llena las
secciones desde ahí. Deja explícito en `profundidad_lectura` qué leíste:
- `full-text` — leíste el informe/artículo/página completa.
- `resumen` — solo el resumen ejecutivo o la nota de prensa (el informe completo está tras
  pago); llena la cifra titular con su año y su fuente primaria.
- `metadata` — solo título/fuente/fecha.

Si una cifra es una **estimación tuya** (no está literal en la fuente), márcala
`estado_evidencia: supuesto`, nunca `verificado`.

## Pasos
1. **Leer y verificar** la fuente: `node tools/browse.mjs open "<url>"` (o WebFetch).
   Intenta el contenido completo; si hay paywall, usa el resumen/nota de prensa y baja
   `profundidad_lectura`. Marca `estado_evidencia`. **Anota `anio_dato` y `geografia`** de
   cada cifra: una cifra global no dimensiona un mercado nacional; un dato de 2019 no es
   vigente.
2. **Dedup**: `python3 tools/kb.py dedup "<título>"`. Si hay similar, **NO dupliques**: abre
   la existente (`ver <id>`), agrega el caso a `proyectos:` y una arista si corresponde;
   termina.
3. **Clasificar** (estándares de `kb/taxonomia.json`, no inventes):
   - `sector` → **define la carpeta** (`fichas/<slug-sector>/`); usa `transversal` si el
     dato aplica a cualquier sector (p.ej. un benchmark de LTV/CAC por modelo de negocio).
   - `tipo` → `informe-mercado` | `estadistica-oficial` | `comparable` | `benchmark` |
     `regulacion`.
   - `topicos` → **reusa** los de `kb/topicos.json` cuando apliquen (así conecta), agrega
     uno si falta.
4. **Crear la ficha** en `kb/fichas/<slug-sector>/<id>.md` con la **plantilla según el tipo**:
   - **informe-mercado / estadistica-oficial** → `kb/fichas/PLANTILLA-informe-mercado.md`:
     qué mercado dimensiona · cifras clave (tamaño, crecimiento, segmentación, precios) ·
     método de la fuente · limitaciones · relevancia para el caso.
   - **comparable / benchmark / regulacion** → `kb/fichas/PLANTILLA-comparable.md`:
     qué ofrece · modelo de ingresos y precio · escala y tracción · fortalezas/debilidades
     (comparable); o indicador · alcance de aplicación · relevancia (benchmark).
   - Llena el frontmatter completo (incluye `anio_dato`, `geografia`, `profundidad_lectura`,
     `estado_evidencia`).
5. **Indexar**: agrega el nodo a `kb/indice.json` (`{id, titulo, tipo, sector, topicos,
   anio_dato, geografia, proyectos}`), actualiza `kb/topicos.json` (tópicos → este id), y
   agrega **aristas** con otras fichas (vocabulario en `kb/README.md`: `mismo_mercado`,
   `competidor_de`, `fuente_de`, `contradice`, `complementa`).
6. **Verificar**: `python3 tools/kb.py salud` (sin huérfanos/sin-ficha) y
   `python3 tools/kb.py ver <id>`.

**DoD:** ficha **rica** creada (secciones del tipo correcto, con sustancia), `anio_dato` /
`geografia` / `profundidad_lectura` / `estado_evidencia` honestos, clasificada según la
taxonomía, indexada con relaciones, y `kb.py salud` sin inconsistencias.
