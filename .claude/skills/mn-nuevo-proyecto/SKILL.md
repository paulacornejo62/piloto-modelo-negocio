---
name: mn-nuevo-proyecto
description: Inicia una nueva postulación de financiamiento (tenant). Crea la carpeta del proyecto con el expediente semilla y una plantilla para las notas de la Reunión #1, y le dice al consultor qué hacer a continuación. Invocar al empezar una postulación nueva, p.ej. "nuevo proyecto de financiamiento para <Empresa>".
---

# Nuevo proyecto de financiamiento

Guía al consultor para arrancar una postulación. No hace análisis; solo prepara el espacio de trabajo aislado del proyecto y orienta.

## Pasos
1. **Pide los datos mínimos** si no los dio: nombre de la empresa y un slug corto (kebab-case, sin tildes/espacios, p.ej. `acuitech`). Si te dan el nombre, propone tú el slug. Pregunta también, **si se sabe a priori** (si no, "por definir" y lo resuelve el flujo):
   - **Tipo de proyecto** (p.ej. desarrollo de producto, mejora de proceso).
   - **Fondo/instrumento objetivo**: Ley I+D · Crea y Valida · Consolida y Expande · Capital Humano · Innova Alta Tecnología · por definir.
   - **Carpeta de Drive del cliente** (URL o id): dónde el equipo GT reúne los documentos. Se **vincula ahora** para que, al entrar a formulación, el paquete de postulación se espeje ahí y suba los entregables. Si no la tienen aún, se puede vincular después.
2. **Crea la carpeta** `proyectos/<slug>/` (si ya existe, avisa y no la pises).
3. **Crea `proyectos/<slug>/expediente.json`** semilla (incluye tipo y fondo si se supieron; si no, "por definir"):
   ```json
   { "meta": { "tenant": "<slug>", "creado": "<fecha>", "actualizado": "<fecha>", "paso_actual": "INICIO", "tipo_proyecto": "<tipo o 'por definir'>", "instrumento_objetivo": "<fondo o 'por definir'>" } }
   ```
   (usa la fecha que te dé el usuario/sistema).
4. **Crea el BUZÓN de entrada** `proyectos/<slug>/entradas/` — aquí caen todos los inputs del cliente (reuniones, documentos, transcripciones) y los agentes los buscan. Crea dentro:
   - `entradas/README.md`:
     ```markdown
     # entradas/ — buzón del proyecto
     Deja aquí TODO input: notas/transcripciones de reuniones, documentos del cliente
     (specs, estudios previos, PDFs), correos relevantes. Los agentes buscan aquí los
     insumos de cada paso. Nombra los archivos claro (reunion-1.md, reunion-2.md,
     estudio-previo.pdf…). Confidencial: gitignoreado.
     ```
   - `entradas/reunion-1.md` con la plantilla para pegar las notas de la Reunión #1:
     ```markdown
     # Reunión #1 — <empresa>

     > Pega aquí las notas/transcripción de la primera reunión con el cliente.
     > Útil incluir: empresa (razón social, tamaño, inicio de actividades), contacto,
     > el problema/oportunidad, el resultado esperado y el presupuesto estimado.

     <!-- pega aquí -->
     ```
   - `entradas/historia-previa.md` para recuperar antecedentes (C4) — el caso casi nunca parte de cero:
     ```markdown
     # Historia previa — <empresa>

     > Si el proyecto tiene antecedentes, déjalos aquí (o pega los documentos en entradas/).
     > - Prevaluaciones o postulaciones anteriores (a este u otro fondo) y su resultado.
     > - Alcance ORIGINAL de la idea, antes de estrecharse.
     > - Qué se sacó del alcance y por qué (costo, riesgo, "no era financiable").
     >   Ojo: lo descartado suele ser donde vivía el I+D — vale la pena revisarlo.

     <!-- pega aquí, o deja los documentos en entradas/ -->
     ```
5. **Vincula la carpeta de Drive** (si la dieron): `python3 tools/postulacion.py vincular <slug> "<url-o-id>"` (guarda el id en `meta.drive_carpeta`). Es la raíz donde luego el paquete de postulación se espeja y se suben los documentos. Si no la dieron, sáltalo y recuérdalo como pendiente.
6. **Valida** que el expediente semilla esté OK: `python3 render/render.py <slug> --validar`.
7. **Orienta al usuario** con los próximos pasos, claros y concretos:
   - "Pega las notas de la Reunión #1 en `proyectos/<slug>/entradas/reunion-1.md`, y deja cualquier otro documento del cliente en `entradas/`."
   - "Si el proyecto tiene **antecedentes** (postulaciones/evaluaciones previas, un alcance anterior), déjalos en `entradas/historia-previa.md` o como documentos — no partimos de cero."
   - "Cuando esté, pídeme: **orquesta `<slug>`** — arrancaré por EVAL_P1 (Perfil) y seguiré con el Deep Research."
   - Recuérdale que los datos del cliente son confidenciales y quedan aislados en su carpeta (no se versionan, ver `.gitignore`).

**Importante:** un proyecto por postulación; nunca mezcles datos de dos clientes en el mismo tenant.
