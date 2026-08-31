---
id: producto-cat-minestar-command-hauling
titulo: "Cat MineStar Command for hauling — camión minero sin operador a bordo (Caterpillar)"
tipo: producto
tema: Sistema comercial de acarreo autónomo con estaciones de operador remoto; distingue autonomía de flota de teleoperación directa
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [teleoperacion-minera, autonomia-supervisada-flota, teleoperacion-supervision-remota, ratio-operador-maquina]
anio: 2024
autores: [Caterpillar Inc.]
referencia: https://www.cat.com/en_GB/products/new/technology/command/command/1000029430.html
motor: WebSearch (páginas oficiales cat.com; el fetch directo de cat.com dio ETIMEDOUT)
profundidad_lectura: metadata
estado_evidencia: parcial
trl_relevante: 9
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Qué es
Solución comercial de Caterpillar para acarreo minero **sin operador a bordo**. Los camiones responden al llamado de la pala, se posicionan, acarrean al punto de descarga y se reportan a mantención. Incluye **estaciones de operador remoto** para que una persona gestione equipos desde un ambiente controlado.

Cita (página oficial Cat, vía resultados de búsqueda):
> "Command provides the fully integrated operation of autonomous mining systems… Command trucks respond to calls to the shovel, move into position, haul to dump points and even report for maintenance — all without an operator on board."

> "Cat Command has the ability to allow a single operator to control multiple machines in remote locations"

## Escala verificada (parcial)
Alrededor de **600 camiones mineros Cat autónomos** operando en terreno (dato de páginas Cat recogido vía buscador; no se pudo abrir la página directa por timeout del sitio).

## Distinción clave para el proyecto
Command for hauling es **autonomía supervisada**, no conducción remota continua: el operador remoto interviene por excepción, no conduce el camión metro a metro. La familia Cat Command sí incluye **teleoperación directa** en otras líneas (dozing, underground, control no-línea-de-vista), pero el acarreo de superficie a escala está resuelto por autonomía, no por telecomando.

## Lo que no está resuelto / no declarado
- Las páginas consultadas **no publican** requisitos de latencia, arquitectura de red ni distancia máxima admisible del centro de control.
- No hay evidencia pública, en las fuentes consultadas, de **conducción remota continua de un camión de superficie a más de 1.000 km** en operación comercial.

## Relevancia
Es el referente comercial dominante: define lo que un cliente minero considera "probado". Una propuesta de telecomando directo debe explicar por qué no es simplemente adoptar Command (por ejemplo: flota de camiones carreteros de fábrica, no camiones mineros; faena que no justifica AHS completo).

> Relaciones con otras fichas → `../../indice.json`. Evidencia `parcial`: el sitio cat.com no fue accesible por navegador ni WebFetch (timeout); las citas provienen del texto indexado de las páginas oficiales.
