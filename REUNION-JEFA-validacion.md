# Reunión con la jefa — Validación del flujo de modelo de negocio

**Objetivo:** que revises (a) el flujo que tenemos definido, (b) qué se levanta en cada reunión y en la búsqueda de mercado, (c) **los supuestos que levantamos con el cliente** para construir el modelo, y (d) un set de definiciones para cerrar.

**Qué necesito de ti hoy:**
1. Visto bueno (o ajustes) al flujo y al nº de reuniones.
2. **Validar la lista de supuestos que le pedimos al cliente** (sección 4).
3. Cerrar 5 definiciones (sección 5): pricing por defecto, qué hace un modelo no postulable, cuándo usar LTV/CAC, indicadores de tracción, bottom-up vs top-down.

---

## 1. Contexto (2 min)

- Piloto **aislado** para construir el **modelo de negocio** de un proyecto y redactar las secciones de **mercado / modelo / escalamiento** del formulario del subsidio CORFO.
- El resto del formulario (metodología técnica, actividades de I+D, equipo) y la formulación final la hace **F19**.
- No hay envío en plataforma: el piloto **entrega un borrador** que F19 integra.
- Si funciona → se propone como expansión de F19 (PR, coordinando con Pablo Ferreiro).

## 2. El flujo definido (5 min)

**Fase 1 — Construir el modelo** · 2 reuniones con el cliente + 1 búsqueda de mercado independiente:

```
R#1  Perfil comercial + solución  ──►  (tarea de datos al cliente)
        │
   Búsqueda de mercado (sin cliente, verificada cifra por cifra)
        │
R#2  Completar el lienzo Canvas
        │
   Construir el modelo (Canvas + economía simple + proyección de ventas)
        │
   Revisión ──► compuerta:
        SÓLIDO    → Fase 2 (redacción)
        AJUSTAR   → mover palancas (pricing / segmento / canal / costos) y recalcular
        INVIABLE  → informe al cliente
        DEVOLVER  → otra reunión con el cliente
```

**Fase 2 — Redacción** (solo si SÓLIDO): narrativa → secciones del formulario del fondo → plan de escalamiento → impacto → QA de coherencia → **entrega a F19**.

**Tiempo:** ~1 mes, en paralelo a la formulación técnica de F19.

## 3. Qué se levanta en cada instancia (10 min)

### Reunión #1 — con el cliente (≈45 min)
- La empresa (razón social, tamaño, antigüedad, contacto).
- **Solución / Producto:** qué es el proyecto de innovación y en qué estado está.
- **Cliente objetivo (grueso):** a quién le vende hoy, cuántos clientes, ventas actuales.
- **Problema:** qué le duele al cliente y qué hace hoy para resolverlo.
- **Propuesta de valor (primer borrador):** "ayudo a [X] a lograr [Y] haciendo [Z]".
- Resultado de negocio buscado; presupuesto; historia previa.
- Cierre: se le manda al cliente la **tarea de datos** (precios, costos fijos y variables, BOM si aplica, pipeline de clientes, estados financieros).

### Búsqueda de mercado — sin cliente, el equipo con navegador
- **Tamaño de mercado:** TAM / SAM / SOM, con método (bottom-up para Chile) y fuentes.
- **Competidores y sustitutos:** qué ofrecen, a qué precio, fortalezas y debilidades.
- **Curva de valor:** contra qué se compite; precios de referencia; benchmarks de industria (márgenes típicos, ciclo de venta).
- Tendencias y regulación que mueven el mercado.
- → Cada cifra se verifica una por una (año y geografía) con un QA independiente.

### Reunión #2 — con el cliente (≈60 min)
- **Segmentos:** prioriza el segmento objetivo de hoy.
- **Propuesta de valor por segmento;** contra qué compite realmente ("no hacer nada" suele ser el rival).
- **Canales y relación con clientes:** cómo llega y cómo entrega la propuesta de valor.
- **Fuentes de ingreso + pricing:** qué cobra, cómo (único / recurrente), a qué precio y **cómo lo fija** (comparación con el mercado / margen sobre costo / valor capturable).
- **Estructura de costos:** fijos y variables; ¿economía de escala o de alcance?
- **Recursos, actividades y asociaciones clave.**
- **Prueba y aprendizaje:** qué se valida en la primera fase.
- **Indicadores de tracción:** cómo el cliente medirá el éxito.
- Capacidad de ejecución: quién decide, qué le falta a la empresa.
- Lista de supuestos, cada uno marcado confirmado / por confirmar.

## 4. Los supuestos que levantamos con el cliente — **VALIDAR** (15 min)

En un proyecto de innovación, buena parte del modelo son **supuestos** (el producto todavía no se vende, o se vende poco). Los levantamos, los marcamos "por confirmar" y los listamos aparte en la postulación — no se esconden.

| Bloque del lienzo | Qué le pedimos al cliente | Suele ser | Reunión |
|---|---|---|---|
| **Segmento objetivo** | Cuál es el segmento prioritario hoy; cuántos clientes potenciales hay; quién decide la compra | dato + supuesto | R#1 → R#2 |
| **Problema** | Cuánto le cuesta hoy el problema (pérdida / costo / frecuencia); qué hace hoy para resolverlo | supuesto / estimación | R#1 |
| **Propuesta de valor** | Qué mejora concreta entrega (cuánto ahorra / cuánto mejora) | supuesto hasta que haya pilotos | R#1 → R#2 |
| **Canales** | Cómo va a llegar al cliente; cuánto tarda en cerrar una venta (ciclo) | supuesto | R#2 |
| **Pricing** | Qué cobra, cómo (único / recurrente), a qué precio y cómo lo fijó | supuesto si no validó con clientes | R#2 |
| **Retención** (si es recurrente) | Cuánto tiempo dura un cliente pagando | supuesto | R#2 |
| **Costo variable** | Costo de producir una unidad (BOM, insumos, horas) | dato o estimación | R#2 + tarea de datos |
| **Costos fijos** | Equipo, arriendo, licencias mensuales | dato | R#2 + tarea de datos |
| **Costo de adquirir un cliente** | Gasto comercial ÷ clientes conseguidos | supuesto | R#2 |
| **Recursos / actividades / asociaciones clave** | Qué necesita sí o sí y no tiene (capital, equipo, permisos, un socio) | dato | R#2 |
| **Proyección** | Cuántas unidades / clientes el año 1; a qué ritmo crece (%/año); hasta dónde quiere llegar y cuándo | supuesto | R#2 → construcción |
| **Impacto** | Ventas incrementales, empleos, impacto ambiental esperados | derivado + validación | construcción |
| **Indicadores de tracción** | Cómo va a medir que le va bien | dato | R#2 |

**Pregunta para ti:** ¿esta lista cubre lo necesario para armar un modelo de negocio **postulable**? ¿Falta algo? ¿Pedimos algo que en la práctica el cliente nunca tiene?

## 5. Definiciones a cerrar (15 min)

| # | Definición | Opciones | Mi recomendación |
|---|---|---|---|
| 1 | **Estrategia de pricing por defecto** | comparación con el mercado · margen sobre costo · valor capturable | empezar por **comparación con el mercado** y contrastar con valor capturable |
| 2 | **Qué hace un modelo NO postulable** (compuerta INVIABLE) | (a) el lienzo está incompleto o incoherente (segmento sin propuesta de valor que le calce, sin forma de cobrar definida) · (b) cada venta pierde plata (margen de contribución < 0) y no hay palanca · (c) el punto de equilibrio no cabe en el mercado alcanzable (SOM) | los 3, con **(b) y (c) como criterio duro** |
| 3 | **LTV / CAC / payback** | siempre · solo si es recurrente / suscripción · nunca | **solo recurrentes**; para el resto, margen de contribución + punto de equilibrio bastan |
| 4 | **Indicadores de tracción a pedir** | nº de clientes · ventas / contratos · % de cumplimiento de hitos · cartas de interés · renovaciones | los 5 en la lista; el cliente compromete **2–3** |
| 5 | **Dimensionamiento de mercado** | bottom-up (nº de empresas / personas del segmento × ticket, datos INE / SII) · top-down (% de un informe global) | **bottom-up como principal**, top-down para contrastar |
| — | Horizonte de proyección | 3 o 5 años | 5, ajustable por fondo |

> Glosario rápido: **margen de contribución** = precio − costo variable de esa unidad (lo que queda para pagar los costos fijos). **Punto de equilibrio** = cuántas unidades hay que vender para que ingresos = costos totales. **CAC** = gasto comercial ÷ clientes conseguidos. **LTV** = plata total que deja un cliente en toda su relación. **LTV/CAC** = cuántas veces recuperas lo que costó traer al cliente.

## 6. Cosas que ya están claras (confirmar, no discutir)

- **Guía de redacción de fondos:** es **F19** — ahí se formula contra las bases. El piloto entrega el borrador de las secciones de modelo de negocio; F19 lo integra.
- **Bases de los fondos:** estables gobierno a gobierno; entre convocatorias pueden cambiar focos o alguna pregunta, pero es poco probable; pueden salir convocatorias nuevas. → No hace falta cargar el texto literal de cada convocatoria en el piloto; **basta la estructura + los criterios de evaluación** (que ya están en `motor-reglas/formularios.json`).
- **Caso real de prueba:** el modelo de negocio de la **postulación a Crea y Valida que se rechazó**. Sirve para revisar cómo queda con el flujo nuevo.

**Preguntas para ti:**
- ¿Hay hoy un **ingeniero comercial** en el equipo que pueda dar una pasada de 30 min a las definiciones 1–5?
- ¿Corremos el caso rechazado por el flujo y lo revisamos juntas, o lo dejo listo y lo comentamos?
- ¿En qué **formato** le sirve a F19 el borrador del piloto (un documento, campos estructurados, una planilla)?

## 7. Próximos pasos

1. Ajustar el piloto según las definiciones de la sección 5.
2. Correr el caso real (Crea y Valida rechazado) de punta a punta.
3. Revisarlo con el ingeniero comercial, si lo hay.
4. Decidir cuándo se propone a F19.
