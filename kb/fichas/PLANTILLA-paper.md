---
id: paper-<slug-unico>                 # p.ej. paper-cabral-2020-sf9-suspension
titulo: <título del paper (autores, año)>
tipo: paper                             # paper | revision | preprint | tesis (../../taxonomia.json)
tema: <tema principal, frase libre alineada al dominio>
area_oecd: "<N Área (N.x Subcampo)>"    # OCDE Fields of Science — define la CARPETA (fichas/<slug-área>/)
topicos: [<tópico 1>, <tópico 2>]       # capa de conexión temática (../../topicos.json)
anio: <YYYY>
autores: [<autor 1>, <autor 2>, ...]
referencia: <DOI / URL / PMID>          # verificable
motor: <de qué buscador salió>          # PubMed, IEEE, ScienceDirect, Google Académico…
profundidad_lectura: full-text          # full-text | abstract | metadata  ← qué se leyó de verdad
estado_evidencia: verificado            # verificado | parcial | no_verificado (control de veracidad/QA)
trl_relevante: <1-9 o ->
metricas_clave: [<métrica: valor>]      # p.ej. "R²=0.96 a 15 min"
fecha_registro: <YYYY-MM-DD>
proyectos:                              # tenants donde se usó/creó (trazabilidad transversal)
  - <tenant>
---

## Pregunta / objetivo de investigación
<Qué se propusieron responder o lograr.>

## Hipótesis
<La hipótesis (o supuesto de partida). Si el paper no la explicita, dilo.>

## Metodología
- **Diseño:** <experimental / observacional / modelado / revisión…>
- **Datos / muestra:** <qué datos, tamaño, origen, periodo.>
- **Técnicas:** <métodos, modelos, equipos, análisis.>
- **Métricas:** <cómo midieron el resultado (RPS, R², recall…).>

## Resultados principales
- <Resultado 1, con cifra.>
- <Resultado 2, con cifra.>

## Conclusiones
<Qué concluyen los autores.>

## Limitaciones
<Del estudio (muestra, generalización, sesgos) y/o para nuestro caso.>

## Relevancia / brecha para el estado del arte
<Qué resuelve, qué deja abierto, por qué es (o no) novedad frente a lo existente. Cómo aplica a la postulación.>

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
