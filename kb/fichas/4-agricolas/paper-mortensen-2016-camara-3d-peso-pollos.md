---
id: paper-mortensen-2016-camara-3d-peso-pollos
titulo: "Estimación de peso de pollos de engorda mediante cámara 3D (Kinect) en granja comercial (Mortensen, Lisouski & Ahrendt, 2016) — título exacto tal como publicado no transcrito por la fuente de este trabajo, ver DOI"
tipo: paper
tema: Predicción de peso de pollos de engorda mediante visión 3D desplegada a escala comercial
area_oecd: "4 Ciencias Agrícolas (4.2 Ciencia animal y lechera)"
topicos: [prediccion-peso-volumen-vision]
anio: 2016
autores: [A.K. Mortensen, P. Lisouski, P. Ahrendt]
referencia: https://doi.org/10.1016/j.compag.2016.03.011 (Computers and Electronics in Agriculture, 123:319-326)
motor: ScienceDirect (índice de bibliografía de la consultora, verificado 29-07-2026)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: ["Error relativo medio: 7.8%", "n=48.000 pollos en granja comercial"]
fecha_registro: 2026-08-21
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Desarrollar y validar un sistema de cámara 3D para estimar el peso vivo de pollos de engorda en una granja comercial real, sin manipulación individual del animal.

## Hipótesis
Que la información de profundidad/volumen capturada por una cámara 3D (Kinect) sobre el lote de aves permite predecir el peso vivo promedio con precisión suficiente para uso comercial, sin pesaje manual ni báscula de plataforma.

## Metodología
- **Diseño:** validación observacional en terreno (no experimento controlado).
- **Datos / muestra:** 48.000 pollos de engorda en una granja comercial real.
- **Técnicas:** cámara de profundidad 3D (Microsoft Kinect) instalada sobre el galpón; procesamiento de la nube de puntos/imagen de profundidad para estimar el volumen corporal de las aves y derivar el peso.
- **Métricas:** error relativo medio frente al peso real medido con báscula de referencia.

## Resultados principales
- Sistema de cámara 3D desplegado en condiciones comerciales reales (no de laboratorio).
- **Error relativo medio de 7.8%** frente al peso real, medido sobre 48.000 pollos.

## Conclusiones
Un sistema de cámara 3D puede estimar el peso de un lote comercial completo con un margen de error de un solo dígito, sin manipulación de las aves — evidencia de viabilidad a escala industrial, no solo de laboratorio.

## Limitaciones
7.8% de error relativo medio es una cifra de magnitud considerable frente a lo que exigiría un sistema de dosificación fina o de decisión individual por ave. El paper (según lo revisado) no distingue si el error es sistemático (sesgo direccional, como el de las básculas de plataforma que describe Nyalala 2021) o solo dispersión aleatoria. El equipo usado (Kinect) está discontinuado comercialmente, lo que limita la reproducibilidad exacta del hardware hoy, aunque no invalida el hallazgo de la cámara 3D como enfoque. Título exacto tal como aparece publicado no fue transcrito literalmente en la fuente de este trabajo (índice de bibliografía); el DOI y datos de revista/volumen/páginas sí están verificados.

## Relevancia / brecha para el estado del arte
Aporta la **cifra de magnitud/error a escala industrial** que falta en el contexto técnico del Formulario Técnico — hoy esa sección solo argumenta el sesgo por frecuencia/recurrencia del pesaje (ver Nyalala 2021), sin una cifra dura de cuánto se equivoca en la práctica un sistema de visión ya desplegado en producción real. Útil para reforzar esa sección con un número concreto y trazable.

Relacionada con [[paper-nyalala-2021-vision-computacional-peso-aves]] (misma familia de problema: visión computacional para peso avícola).

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
