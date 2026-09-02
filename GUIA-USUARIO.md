# Guía de usuario — Asistente de Modelo de Negocio (piloto)

Para el consultor. Esta herramienta te **acompaña** a construir el modelo de negocio de un
cliente y a redactar las secciones de **modelo de negocio, mercado y escalamiento** que
piden los formularios de subsidios CORFO (Crea y Valida, Innova Alta Tecnología, Consolida y
Expande, Capital Humano): investiga el mercado, arma el Business Model Canvas y los unit
economics, y redacta las respuestas — **tú decides**.

> ¿Eres quien instala/mantiene la herramienta? Ver [SETUP.md](SETUP.md). ¿Detalle técnico?
> [COMO-CORRER.md](COMO-CORRER.md).
>
> **Es un piloto.** Se enmarca dentro de un proyecto de innovación; muchas cifras del
> modelo serán supuestos — la herramienta los marca como tales, no los esconde. El detalle
> de equipo/capacidades y las secciones técnicas del formulario los completa el equipo GT.

## 1. Instalar (una sola vez)

Necesitas **Python 3** y **Node** (si no los tienes, pídelos a soporte). En una terminal,
ubícate en esta carpeta y corre:
```bash
bash setup/setup.sh
```
Deja todo listo (navegador para investigar, dependencias, un autotest). Al final dice
**"Setup completo"**.

## 2. Abrir la herramienta

Desde esta carpeta:
```bash
claude
```
(La primera vez te puede pedir aprobar el navegador — acepta.)

## 3. Empezar un caso

Escríbele, en lenguaje natural:

> **"Nuevo caso de modelo de negocio para [Empresa]"**

Te pedirá el **fondo objetivo** (uno de los 4 CORFO) y creará un espacio aislado con un
**buzón `entradas/`**. Deja ahí:
- **`reunion-1.md`** — notas de la primera reunión (qué vende, a quién hoy, por qué canal,
  qué resultado de negocio busca, presupuesto).
- **`proyecto.md`** — la descripción del **proyecto de innovación** (qué se desarrolla, en
  qué estado, a qué mercado apunta). El modelo de negocio se construye sobre esto.
- **`datos-comerciales.md`** — precios actuales, costos, nº de clientes, estados financieros
  si existen.
- Cualquier otro documento del cliente.

## 4. Avanzar el proceso

Cuando esté, escríbele:

> **"Orquesta [empresa]"**

Irá paso a paso:
- **Perfil comercial** (ordena los datos del cliente).
- **Investigación de mercado** (tamaño TAM/SAM/SOM, competidores, precios, benchmarks, con
  navegador real) + **QA de veracidad** (verifica cada cifra, su año y su geografía).
- **Supuestos del modelo** (segmentos, propuesta de valor, ingresos, costos, CAC — se
  validan contigo y el cliente).
- **Construir el modelo** (Business Model Canvas + unit economics + proyección por
  escenarios — la matemática la calcula el motor).
- **Revisión de viabilidad** → una compuerta: **SÓLIDO** (a redactar), **AJUSTAR** (mover
  pricing/segmento/canal/costos y recalcular), **INVIABLE** (informe al cliente),
  **DEVOLVER** (falta info del cliente).
- Si es SÓLIDO: **redacción** de las secciones del formulario del fondo + **entrega** del
  paquete.

Va contándote qué hizo y qué sigue. Para en los puntos de decisión y te pide aprobación.

## 5. Ver los resultados

Todo queda en `proyectos/[empresa]/`:
- **`expediente.md`** — el expediente legible: Panel del consultor arriba (compuerta, unit
  economics, datos por confirmar) + el detalle de cada paso.
- **`modelo-negocio.md`** — resumen del modelo (Canvas, unit economics, proyección,
  supuestos a confirmar).
- **`qa-veracidad-*.md`** — el informe de verificación de las cifras de mercado.
- **`plan-trabajo.xlsx`** — Unit economics + Proyección por escenario + Hitos comerciales.
- **`formulario-modelo-negocio.md`** — al cerrar la Fase 2, las secciones redactadas como
  documento entregable (borrador de apoyo; el equipo GT lo integra al formulario completo).
- **`postulacion/CHECKLIST.md`** — qué entregables están listos y qué falta.

### Cómo leer la evidencia (importante)
Cada cifra de mercado trae un marcador:
- ✅ **verificado** — se abrió la fuente y el dato (número, año, geografía) coincide.
- 🟡 **parcial** — solo se vio el resumen (informe completo tras pago).
- ⚠️ **no verificado** — referenciado pero sin confirmar (tómalo con pinzas).
- **supuesto** — es una estimación, no un dato de fuente.

Y una sección **"Cobertura de búsqueda"** que dice, sin esconder nada, qué fuentes se
cubrieron y cuáles no. **La herramienta nunca presenta como hecho algo que no pudo
confirmar.**

## 6. Ver dónde vas, retomar y la cartera completa
- **"¿Dónde va [empresa]?"** o **"estado de [empresa]"** → qué pasos se completaron, en
  cuál vas y qué hacer ahora.
- **"Retoma [empresa]"** → te resume dónde quedaste sin releer todo.
- **"Panel"** o **"¿cómo va todo?"** → la cartera completa.

Cada bloque de trabajo queda en una **bitácora** por caso (fecha + qué se hizo).

## 7. Sobre los umbrales del motor
Los cortes que decide la compuerta (margen de contribución mínimo, LTV/CAC, payback,
penetración de SOM) están en `motor-reglas/parametros.json` marcados **POR VALIDAR con
ingeniería comercial** — son una primera versión genérica. Conviene revisarlos con alguien
con experiencia en modelos de negocio para CORFO antes de apoyarse en el veredicto.

## 8. Confidencialidad
Los datos de cada cliente quedan **aislados** en su carpeta y **no se suben** a ningún
repositorio (protegidos por `.gitignore`). Un caso por cliente; no mezcles.

## 9. ¿Algo no funciona?
- Corre de nuevo `bash setup/setup.sh` (te dirá qué falta).
- Si una fuente sale como "no_accesible", es una limitación conocida (algunas exigen cuenta
  o pago); la herramienta lo deja declarado, no inventa.
