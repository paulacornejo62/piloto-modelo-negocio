# Guía de usuario — Asistente de Formulación de Financiamiento (GT)

Para el consultor de Gestión Tecnológica. Esta herramienta te **acompaña** a evaluar y formular postulaciones a Ley I+D e instrumentos CORFO: hace tareas, investiga el estado del arte y arma material — **tú decides**.

> ¿Eres quien instala/mantiene la herramienta? Ver también [SETUP.md](SETUP.md). ¿Detalle técnico? [COMO-CORRER.md](COMO-CORRER.md).

## 1. Instalar (una sola vez)

Necesitas tener instalado en tu computador: **Python 3** y **Node** (si no los tienes, pídelos a soporte). Luego, en una terminal, ubícate en la carpeta `sistema/` y corre:

```bash
bash setup/setup.sh
```

Esto deja todo listo (descarga el navegador para investigar, instala dependencias y hace una prueba). Al final te dirá **"Setup completo"**. Si algo falta, el mismo mensaje te dice qué instalar.

## 2. Abrir la herramienta

Desde la carpeta `sistema/`, abre Claude Code:

```bash
claude
```

(La primera vez te puede pedir aprobar el navegador — acepta.)

## 3. Empezar una postulación

Escríbele, en lenguaje natural:

> **"Nuevo proyecto de financiamiento para [Empresa]"**

Te creará un espacio aislado para esa empresa con un **buzón `entradas/`**. Pega las **notas de la Reunión #1** en `entradas/reunion-1.md` (lo que tengas: quién es la empresa, el problema, el resultado esperado, el presupuesto), y **deja en `entradas/` cualquier otro documento del cliente** (transcripciones, specs, estudios previos, PDFs) — el agente busca ahí los insumos de cada paso, incluso entre reuniones y sesiones.

## 4. Avanzar el proceso

Cuando las notas estén, escríbele:

> **"Orquesta [empresa]"**

La herramienta irá paso a paso:
- **Perfil Preliminar** (ordena los datos del cliente).
- **Deep Research** (investiga papers y patentes en profundidad, con navegador real).
- **QA de veracidad** (verifica cada fuente y descarta cualquier dato no confirmado).

Va a ir contándote qué hizo y qué sigue.

## 5. Ver los resultados

Todo queda en la carpeta del proyecto, `proyectos/[empresa]/`:
- **`expediente.md`** — el expediente legible (perfil, estado del arte, hipótesis, preguntas, Frascati, perfil de subsidios, formulación).
- **`qa-veracidad-eval_p2.md`** — el informe de verificación de fuentes.
- **`formulario-ley-id.md` / `.docx`** — al cerrar la Formulación, el **formulario Ley I+D** como documento entregable (borrador de apoyo; revisar contra la plataforma oficial antes de enviar).
- **`plan-trabajo.xlsx`** — la **Carta Gantt + Presupuesto** estructurada como el formato oficial (insumo de arranque que traspasas al archivo oficial de CORFO).

### Cómo leer la veracidad (importante)
En el estado del arte cada hallazgo trae un marcador:
- ✅ **verificado** — se abrió la fuente y el dato coincide.
- 🟡 **parcial** — solo se vio el resumen (texto completo tras pago).
- ⚠️ **no_verificado** — referenciado pero sin confirmar (tómalo con pinzas).

Y una sección **"Cobertura de búsqueda"** que dice, sin esconder nada, qué buscadores se cubrieron y cuáles no. **La herramienta nunca presenta como hecho algo que no pudo confirmar.**

## 6. Ver dónde vas, retomar y la cartera completa
- **"¿Dónde va [empresa]?"** o **"estado de [empresa]"** → te muestra qué pasos se completaron, en cuál vas y **qué hacer ahora**.
- **"Retoma [empresa]"** → te resume dónde quedaste y qué sigue, sin releer todo (útil al volver tras unos días).
- **"Panel"** o **"¿cómo va todo?"** → la **cartera completa**: todas las postulaciones con su estado de un vistazo.

Cada bloque de trabajo queda guardado en una **bitácora** por proyecto (fecha + qué se hizo), así nunca pierdes el hilo.

## 7. Confidencialidad
Los datos de cada cliente quedan **aislados** en su carpeta y **no se suben** a ningún repositorio (están protegidos por `.gitignore`). Un proyecto por cliente; no mezcles.

## 8. ¿Algo no funciona?
- Corre de nuevo `bash setup/setup.sh` (te dirá qué falta).
- Si un buscador sale como "no_accesible", es una limitación conocida (algunos exigen acceso especial); la herramienta lo deja declarado, no inventa.
- Soporte: el equipo de IA de Brinca (programa-ia).
