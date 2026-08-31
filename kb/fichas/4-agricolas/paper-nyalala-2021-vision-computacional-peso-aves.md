---
id: paper-nyalala-2021-vision-computacional-peso-aves
titulo: "Revisión sobre predicción de peso/volumen de aves por visión computacional y sesgos del pesaje manual/automático (Nyalala, Okinda, Kunjie, Korohou, Nyalala & Chao, 2021) — título exacto tal como publicado no transcrito por la fuente de este trabajo, ver DOI/PMC"
tipo: revision
tema: Sesgos del pesaje manual y de báscula automática de plataforma en aves; visión computacional como alternativa
area_oecd: "4 Ciencias Agrícolas (4.2 Ciencia animal y lechera)"
topicos: [prediccion-peso-volumen-vision, vision-computacional-monitoreo-avicola]
anio: 2021
autores: [I. Nyalala, C. Okinda, C. Kunjie, T. Korohou, L. Nyalala, Q. Chao]
referencia: https://doi.org/10.1016/j.psj.2021.101072 (PMC8010860, Poultry Science 100(5):101072)
motor: WebFetch (PMC)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: []
fecha_registro: 2026-08-21
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Revisar el estado del arte de los sistemas para estimar el peso y volumen corporal de aves de corral, comparando el pesaje manual, las básculas automáticas de plataforma y los sistemas de visión computacional (2D/3D).

## Hipótesis
Es una revisión: no plantea una hipótesis propia, sintetiza y compara la evidencia de métodos existentes de estimación de peso/volumen avícola.

## Metodología
- **Diseño:** revisión bibliográfica.
- **Datos / muestra:** corpus de estudios sobre estimación de peso/volumen de aves mediante distintos métodos (manual, báscula de plataforma, visión 2D, visión 3D).
- **Técnicas:** comparación cualitativa de métodos y sus limitaciones reportadas.
- **Métricas:** no aplica un método único; resume las métricas reportadas por los estudios primarios revisados.

## Resultados principales
- El pesaje manual aumenta la carga laboral, reduce el bienestar animal, y puede afectar la calidad/rendimiento del producto e incluso causar muerte de aves durante la manipulación.
- Las básculas automáticas de plataforma también tienen sesgo estructural: las aves más pesadas visitan la plataforma con menor frecuencia que las más livianas, lo que **subestima sistemáticamente** el peso promedio real del lote.
- La visión computacional (2D/3D) surge como alternativa no invasiva frente a ambos métodos, aunque enfrenta retos propios (oclusión entre aves, variabilidad de postura e iluminación).

## Conclusiones
La validación agregada/no individual del peso (por lote, no ave por ave) es una limitación **reconocida y documentada en toda la industria avícola** — no una particularidad del caso de un productor específico. Ningún método (manual, báscula de plataforma o visión) logra hoy una estimación individual sin sesgo a bajo costo.

## Limitaciones
Al ser una revisión, no reporta cifras de error propias — depende de qué estudios primarios cita en cada punto. No siempre desagrega los hallazgos por especie/línea genética. No cubre en profundidad la predicción a futuro (series de tiempo); se enfoca en la estimación puntual del estado actual del ave/lote. Título exacto tal como aparece publicado no fue transcrito literalmente en la fuente de este trabajo (índice de bibliografía); el DOI, PMC y datos de revista/volumen sí están verificados y son el identificador confiable de la fuente.

## Relevancia / brecha para el estado del arte
Ya estaba citada en `form_w1.contexto_tecnico_proyecto` como [1], pero nunca se había creado su ficha en la KB — esta ficha corrige eso. Sustenta directamente el mecanismo de sesgo citado en esa sección del Formulario Técnico (párrafo de "peso"): confirma con evidencia de revisión que el pesaje —manual o por báscula de plataforma— tiene sesgos estructurales conocidos y documentados en la industria, lo que motiva explorar visión computacional como vía de mejora, sin que ello implique que el problema esté resuelto.

Relacionada con [[paper-mortensen-2016-camara-3d-peso-pollos]] (misma familia de problema: visión computacional para peso avícola).

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
