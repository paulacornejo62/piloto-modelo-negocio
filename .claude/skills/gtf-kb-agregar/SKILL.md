---
name: gtf-kb-agregar
description: Agrega una fuente (paper, patente, producto) a la base de conocimiento transversal a partir de una URL o referencia. Lee la fuente (full-text si se puede), extrae el contenido estructurado, verifica duplicados y crea una ficha rica y clasificada + su nodo/relaciones. Invocar con "agrega a la KB <url>" o al cerrar un Deep Research.
---

# Agregar fuente a la base de conocimiento

Convierte una fuente en una **ficha rica, estructurada y clasificada** de la KB transversal. Una ficha NO es un par de bullets: captura los puntos, hipótesis, metodología, resultados y conclusiones (paper) o las reivindicaciones y el análisis FTO (patente). La veracidad manda.

## Principio: leer, no ojear
**Lee el texto completo siempre que sea accesible** (abre el PDF/HTML del artículo o el documento de la patente), y llena las secciones desde ahí. Deja explícito en `profundidad_lectura` qué leíste:
- `full-text` — leíste el artículo/patente completo.
- `abstract` — solo abstract (paper) o resumen+reivindicaciones (patente); el full-text está en paywall/no accesible.
- `metadata` — solo título/autores/año.

Si solo llegaste al abstract, **dilo** (`profundidad_lectura: abstract`) y llena lo que haya, sin inventar las secciones que no puedes sustentar.

## Pasos
1. **Leer y verificar** la fuente: `node tools/browse.mjs open "<url>"` (o WebFetch). Intenta el **full-text**; si hay paywall, usa abstract/resumen indexado y baja `profundidad_lectura`. Marca `estado_evidencia` (verificado/parcial/no_verificado) según lo que pudiste confirmar.
2. **Dedup**: `python3 tools/kb.py dedup "<título>"`. Si hay similar, **NO dupliques**: abre la existente (`ver <id>`), agrega el proyecto a `proyectos:` y una arista si corresponde; termina.
3. **Clasificar** (estándares de `kb/taxonomia.json`, no inventes): `tipo`; `area_oecd` → **define la carpeta** (`fichas/<slug-área>/`); `ipc` **solo patentes** (código de Google Patents); `topicos` — **reusa** los de `kb/topicos.json` cuando apliquen (así conecta), agrega uno si falta.
4. **Crear la ficha** en `kb/fichas/<slug-área>/<id>.md` con la **plantilla según el tipo**:
   - **Paper** → `kb/fichas/PLANTILLA-paper.md`: Pregunta/objetivo · Hipótesis · Metodología (diseño·datos/muestra·técnicas·métricas) · Resultados principales (con cifras) · Conclusiones · Limitaciones · Relevancia/brecha.
   - **Patente** → `kb/fichas/PLANTILLA-patente.md`: Problema técnico · **Reivindicaciones clave (qué protege)** · Solución técnica · Alcance y limitaciones · **Relevancia FTO/novedad** (¿bloquea? ¿esquivable? estado legal + jurisdicciones). No hagas una patente "con forma de paper".
   - Llena el frontmatter completo (incluye `profundidad_lectura` y `estado_evidencia`).
5. **Indexar**: agrega el nodo a `kb/indice.json` (`{id, titulo, tipo, area_oecd, ipc?, topicos, anio, proyectos}`), actualiza `kb/topicos.json` (tópicos → este id), y agrega **aristas** con otras fichas (vocabulario en `kb/README.md`).
6. **Verificar**: `python3 tools/kb.py salud` (sin huérfanos/sin-ficha) y `python3 tools/kb.py ver <id>`.

**DoD:** ficha **rica** creada (secciones del tipo correcto, con sustancia), `profundidad_lectura` y `estado_evidencia` honestos, clasificada según la taxonomía, indexada con relaciones, y `kb.py salud` sin inconsistencias.
