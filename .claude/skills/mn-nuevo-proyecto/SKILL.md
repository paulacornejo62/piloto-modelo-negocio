---
name: mn-nuevo-proyecto
description: Inicia un nuevo caso de modelo de negocio (tenant). Crea la carpeta del caso con el expediente semilla y las plantillas del buzón de entrada (notas de reunión, información del proyecto de innovación), y le dice al consultor qué hacer a continuación. Invocar al empezar un caso nuevo, p.ej. "nuevo caso de modelo de negocio para <Empresa>".
---

# Nuevo caso de modelo de negocio

Guía al consultor para arrancar un caso. No hace análisis; solo prepara el espacio de
trabajo aislado y orienta.

## Pasos
1. **Pide los datos mínimos** si no los dio: nombre de la empresa y un slug corto
   (kebab-case, sin tildes/espacios, p.ej. `acuitech`). Si te dan el nombre, propón tú el
   slug. Pregunta también, **si se sabe a priori** (si no, "por definir" y lo resuelve el
   flujo):
   - **Fondo objetivo** (obligatorio antes de la Fase 2): `Crea y Valida` · `Innova Alta
     Tecnología` · `Consolida y Expande` · `Capital Humano` · `por definir`.
   - **Tipo de negocio**: software/SaaS, hardware, servicios, marketplace, deep tech,
     manufactura… (ajusta qué umbrales de unit economics son razonables).
   - **Carpeta de Drive del cliente/proyecto** (URL o id): dónde se reúnen los documentos.
     Se **vincula ahora** para que, al entrar a Fase 2, los entregables del modelo de
     negocio se espejen ahí. Si no la tienen aún, se puede vincular después.
2. **Crea la carpeta** `proyectos/<slug>/` (si ya existe, avisa y no la pises).
3. **Crea `proyectos/<slug>/expediente.json`** semilla:
   ```json
   { "meta": { "tenant": "<slug>", "creado": "<fecha>", "actualizado": "<fecha>", "paso_actual": "INICIO", "cliente_razon_social": "<empresa>", "tipo_negocio": "<tipo o 'por definir'>", "instrumento_objetivo": "<fondo o 'por definir'>" } }
   ```
   (usa la fecha que te dé el usuario/sistema).
4. **Crea el BUZÓN de entrada** `proyectos/<slug>/entradas/` — aquí caen todos los inputs
   del cliente y los agentes los buscan. Crea dentro:
   - `entradas/README.md`:
     ```markdown
     # entradas/ — buzón del caso
     Deja aquí TODO input: notas/transcripciones de reuniones, la descripción del proyecto
     de innovación, datos comerciales (precios, costos, clientes actuales, estados
     financieros), estudios previos. Los agentes buscan aquí los insumos de cada paso.
     Nombra los archivos claro (reunion-1.md, proyecto.md, precios.xlsx…).
     Confidencial: gitignoreado.
     ```
   - `entradas/reunion-1.md` — plantilla de la primera reunión:
     ```markdown
     # Reunión #1 — <empresa>

     > Pega aquí las notas/transcripción de la primera reunión.
     > Útil incluir: la empresa (razón social, tamaño, inicio de actividades), contacto,
     > qué vende o pretende vender, a quién le vende hoy, por qué canal, el resultado de
     > negocio que busca con el proyecto, y el presupuesto estimado.

     <!-- pega aquí -->
     ```
   - `entradas/proyecto.md` — la información del **proyecto de innovación** que sustenta el
     modelo:
     ```markdown
     # Proyecto de innovación — <empresa>

     > El modelo de negocio se construye sobre este proyecto. Deja aquí (o pega los
     > documentos en entradas/):
     > - Qué se desarrolla (producto/servicio/proceso) y la propuesta técnica.
     > - Estado de desarrollo / TRL, y qué se lograría con el subsidio.
     > - Resultado esperado y a qué mercado apunta.
     > Muchas cifras del mercado futuro serán supuestos — está bien, se marcan como tales.

     <!-- pega aquí, o deja los documentos en entradas/ -->
     ```
   - `entradas/datos-comerciales.md` — lo que ya se sabe del negocio actual:
     ```markdown
     # Datos comerciales — <empresa>

     > Si la empresa ya opera, deja aquí lo que tenga:
     > - Precios actuales y forma de cobro.
     > - Costos (fijos y variables) y márgenes si los conoce.
     > - Número de clientes actuales, ventas, tracción.
     > - Estados financieros / listas de precios como documentos en entradas/.

     <!-- pega aquí -->
     ```
5. **Vincula la carpeta de Drive** (si la dieron):
   `python3 tools/postulacion.py vincular <slug> "<url-o-id>"` (guarda el id en
   `meta.drive_carpeta`). Si no la dieron, sáltalo y recuérdalo como pendiente.
6. **Valida** el expediente semilla: `python3 render/render.py <slug> --validar`.
7. **Orienta al usuario** con los próximos pasos, claros y concretos:
   - "Pega las notas de la Reunión #1 en `proyectos/<slug>/entradas/reunion-1.md`."
   - "Deja la descripción del proyecto de innovación en `entradas/proyecto.md` y los datos
     comerciales que tengas en `entradas/datos-comerciales.md` (o los documentos en `entradas/`)."
   - "Cuando esté, pídeme: **orquesta `<slug>`** — arrancaré por EVAL_P1 (perfil comercial)
     y seguiré con la investigación de mercado."
   - Recuérdale que los datos del cliente son confidenciales y quedan aislados en su carpeta
     (no se versionan, ver `.gitignore`).

**Importante:** un caso por proyecto; nunca mezcles datos de dos clientes en el mismo tenant.
