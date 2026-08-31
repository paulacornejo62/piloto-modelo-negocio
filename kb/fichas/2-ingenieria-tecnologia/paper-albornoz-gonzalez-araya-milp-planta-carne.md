---
id: paper-albornoz-gonzalez-araya-milp-planta-carne
titulo: An Optimization Model for Planning Operations in a Meat Packing Plant (Albornoz & González-Araya)
tipo: paper
tema: MILP para decidir patrones de corte de canales, rendimiento por producto e inventario
area_oecd: "2 Ingeniería y Tecnología (2.11 Otras ingenierías y tecnologías)"
topicos: [milp-programacion-produccion-carnica]
anio:
autores: [Albornoz, González-Araya]
referencia: "https://link.springer.com/chapter/10.1007/978-3-319-27680-9_9 (también indexado en ResearchGate/Semantic Scholar)"
motor: WebSearch
profundidad_lectura: metadata
estado_evidencia: parcial
trl_relevante: -
metricas_clave: []
fecha_registro: 2026-08-18
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Dar soporte a la planificación de operaciones en una planta de carne, decidiendo cuántas veces aplicar cada patrón de corte sobre las canales para satisfacer demanda de distintos productos.

## Hipótesis
No confirmable — no se accedió al cuerpo del capítulo/paper.

## Metodología
- **Diseño:** modelo de programación lineal entera mixta (MILP).
- **Datos / muestra:** no confirmado a este nivel de acceso.
- **Técnicas:** decisiones sobre número de aplicaciones de cada patrón de corte, rendimiento total por producto, niveles de inventario; considera perecibilidad de productos, capacidad laboral y distintos tipos de canales con distinto rendimiento.
- **Métricas:** maximización del margen económico (según snippet agregado).

## Resultados principales
No confirmables desde fuente primaria a este nivel de acceso.

## Conclusiones
Un modelo MILP puede dar una decisión óptima que maximiza el margen económico y reduce faltantes en productos de mayor margen, balanceando contra inventario de productos de baja demanda.

## Limitaciones
**Fuente no abierta directamente** — el intento de fetch a Semantic Scholar devolvió página vacía (contenido renderizado por JS). La existencia y el resumen del paper se confirman de forma cruzada por 3 listados independientes (Semantic Scholar, Springer, ResearchGate) con detalles consistentes, pero no equivale a lectura de fuente primaria — `estado_evidencia: parcial`, `profundidad_lectura: metadata`. Existe además un antecedente previo relacionado (Stokes, Sturdivant, Rister & McCarl 1998, "mixed integer goal programming" para planificación de meat packing) no verificado en este pase.

## Relevancia / brecha para el estado del arte
Es la mejor aproximación encontrada al problema específico del Objetivo 3 desde la literatura de operaciones cárnicas latinoamericanas (González-Araya trabaja en optimización de cadenas de suministro pecuarias en Chile) — relevante como antecedente de MILP aplicado a decisiones de mezcla de producto en una planta de proteína animal, aunque el problema exacto (patrones de corte de canal) difiere del de Agrosuper (programación de Hamburguesa/Empanizado con función objetivo de 8 componentes). No citar en el formulario oficial con detalle cuantitativo hasta verificar el texto completo.

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
