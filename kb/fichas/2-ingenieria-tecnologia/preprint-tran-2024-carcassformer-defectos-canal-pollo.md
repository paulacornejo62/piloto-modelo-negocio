---
id: preprint-tran-2024-carcassformer-defectos-canal-pollo
titulo: "CarcassFormer: An End-to-end Transformer-based Framework for Simultaneous Localization, Segmentation and Classification of Poultry Carcass Defect (Tran, Truong, Fernandes, Kidd & Le, 2024)"
tipo: preprint
tema: Arquitectura Transformer para detección/segmentación/clasificación simultánea de defectos en canales de pollo
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [deteccion-defectos-vision-carne]
anio: 2024
autores: [Tran, Truong, Fernandes, Kidd, Le]
referencia: arXiv:2404.11429
motor: WebFetch (arXiv)
profundidad_lectura: abstract
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: ["n=7.321 imágenes", "Supera métodos previos en AP, AP@50, AP@75"]
fecha_registro: 2026-08-21
proyectos:
  - agrosuper-transformacion-digital
---

## Pregunta / objetivo de investigación
Desarrollar una arquitectura basada en Transformer que localice, segmente y clasifique simultáneamente defectos en canales de pollo, en un solo modelo end-to-end.

## Hipótesis
Que una arquitectura Transformer end-to-end, más avanzada que detectores tipo YOLO, puede superar a los métodos previos en la tarea combinada de localización + segmentación + clasificación de defectos en canales de pollo.

## Metodología
- **Diseño:** desarrollo y evaluación de un modelo de deep learning (Transformer).
- **Datos / muestra:** 7.321 imágenes de canales de pollo con defectos anotados.
- **Técnicas:** arquitectura Transformer end-to-end (CarcassFormer) que realiza localización, segmentación y clasificación de forma simultánea, en contraste con arquitecturas tipo YOLO.
- **Métricas:** AP (average precision), AP@50, AP@75.

## Resultados principales
- CarcassFormer **supera a métodos previos** en las métricas AP, AP@50 y AP@75.
- Evaluado sobre un dataset propio de 7.321 imágenes de canales de pollo.

## Conclusiones
Una arquitectura Transformer end-to-end es superior a los enfoques previos (incluyendo detectores tipo YOLO) para la tarea combinada de detectar, segmentar y clasificar defectos en canales de pollo.

## Limitaciones
Es un **preprint de arXiv**, no ha pasado por revisión por pares confirmada — `profundidad_lectura: abstract` (no se leyó el cuerpo completo). El dataset (7.321 imágenes) es propio de los autores, no se confirma su disponibilidad pública ni su representatividad frente al caso específico de Agrosuper (piezas semicongeladas, no canales completas).

## Relevancia / brecha para el estado del arte
Evidencia de que arquitecturas más avanzadas que YOLO (Transformer) están siendo aplicadas activamente a detección de defectos en piezas avícolas — relevante como antecedente de la dirección técnica que podría tomar el Objetivo 4 de Agrosuper si los enfoques YOLO estándar resultan insuficientes (ver relación con las limitaciones de YOLO documentadas en [[paper-he-2024-yolo-oclusion-vehiculos]] y [[preprint-zhang-2026-sep-yolo-objetos-transparentes]]).

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
