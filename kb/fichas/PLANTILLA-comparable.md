---
id: <comparable|benchmark>-<slug-unico>   # p.ej. comparable-nubox-contabilidad-pyme
titulo: <nombre de la empresa comparable / del benchmark>
tipo: comparable                       # comparable | benchmark | regulacion (../taxonomia.json)
tema: <qué compara / qué indicador, frase libre>
sector: <slug-sector>                  # define la CARPETA (fichas/<slug-sector>/)
topicos: [<tópico 1>, <tópico 2>]
geografia: <dónde opera / a qué mercado aplica>
fuente: <sitio de la empresa | Crunchbase | G2 | informe X>
referencia: <URL / identificador>      # verificable
profundidad_lectura: full-text        # full-text | resumen | metadata
estado_evidencia: verificado          # verificado | parcial | no_verificado | supuesto
fecha_registro: <YYYY-MM-DD>
proyectos:
  - <tenant>
---

<!-- Para tipo=comparable: -->
## Qué ofrece
<Producto/servicio, propuesta de valor, a qué segmento le vende.>

## Modelo de ingresos y precio
<Cómo cobra (suscripción, transacción, licencia, servicio) y precios publicados, con fecha.>

## Escala y tracción
<Nº de clientes / usuarios declarados, dotación (proxy), financiamiento levantado, mercados donde opera.>

## Fortalezas / debilidades
- **Fortaleza:** <…>
- **Debilidad / brecha:** <dónde no llega — ahí puede estar el espacio del cliente.>

<!-- Para tipo=benchmark: reemplaza las secciones anteriores por: -->
## Indicador
<Qué mide (margen bruto típico, CAC por canal, LTV/CAC, ciclo de venta, múltiplo EV/ventas) y su valor o rango.>

## Alcance de aplicación
<Para qué tipo de negocio / sector / etapa aplica. Un benchmark de SaaS no sirve para hardware.>

## Relevancia para el caso
<Cómo se usa: para comparar la diferenciación, para sustentar un supuesto de unit economics, para el pricing.>

> Relaciones con otras fichas (competidor_de, mismo_mercado, complementa) → `../indice.json`.
