---
id: informe-<slug-unico>               # p.ej. informe-2025-saas-b2b-latam-frost
titulo: <título del informe / artículo (fuente, año)>
tipo: informe-mercado                  # informe-mercado | estadistica-oficial (../taxonomia.json)
tema: <mercado / segmento que dimensiona, frase libre>
sector: <slug-sector>                  # define la CARPETA (fichas/<slug-sector>/) — ../taxonomia.json
topicos: [<tópico 1>, <tópico 2>]      # capa de conexión temática (../topicos.json)
anio_dato: <YYYY>                      # año al que se refieren las cifras (NO el de publicación si difieren)
geografia: <Chile | LATAM | global | …>   # alcance de las cifras
fuente: <nombre de la fuente>          # INE, Statista, Diario Financiero, gremio X…
referencia: <URL / identificador>      # verificable
profundidad_lectura: full-text        # full-text | resumen | metadata  ← qué se leyó de verdad
estado_evidencia: verificado          # verificado | parcial | no_verificado | supuesto
fecha_registro: <YYYY-MM-DD>
proyectos:                             # tenants donde se usó/creó (trazabilidad transversal)
  - <tenant>
---

## Qué mercado dimensiona
<Definición del mercado/segmento: producto, cliente, geografía, año.>

## Cifras clave
- **Tamaño (TAM/SAM):** <valor, unidad, año, geografía.>
- **Crecimiento:** <CAGR o tasa, periodo.>
- **Segmentación:** <cómo se reparte (por segmento, canal, región).>
- **Precios de referencia:** <si el informe los trae.>

## Método de la fuente
<Cómo estimó la fuente el tamaño (encuesta, cuentas nacionales, top-down, panel). Si no lo dice, márcalo.>

## Limitaciones / cuidados
<Qué NO cubre, sesgos, si es proyección vs. dato observado, si la geografía obliga a ajustar.>

## Relevancia para el caso
<Qué aporta al TAM/SAM/SOM del modelo, qué hay que ajustar, qué queda como supuesto.>

> Relaciones con otras fichas (mismo_mercado, fuente_de, contradice, complementa) → `../indice.json`.
