# Reunión con la jefa — Validación pregunta por pregunta

**Objetivo:** recorrer las preguntas de los formularios que tocan el modelo de negocio (comparando **Crea y Valida 2025**, **Consolida y Expande 2024** e **Innova Alta Tecnología 2022**, los tres reales) y que la jefa dé **sugerencias por pregunta**. Con eso se ajusta qué se cubre en R#1 vs R#2.

**Material:** `MAPEO-formularios.md` (comparación de los 3 fondos) + la página visual del flujo.

**Ya decidido — no discutir:** el modelo de negocio se levanta en **2 reuniones con el cliente** + 1 búsqueda de mercado independiente.

---

## 1. Contexto (2 min)

- El piloto construye el **modelo de negocio** y redacta las secciones de **mercado / modelo / escalamiento**. Metodología técnica, actividades de I+D, propiedad intelectual y equipo → **F19**.
- No hay envío en plataforma: el piloto **entrega un borrador**; F19 lo integra al formulario completo.

## 2. Hallazgo (3 min)

La pregunta central de modelo de negocio es **idéntica en los tres formularios**: CyV *Impacto Q1* = CyE *Estrategia de Negocio Q1* = Innova AT *Modelo de Negocios Q2* (clientes, cómo se cobra, % mercado, captar/fidelizar, canales, **supuestos + fuentes de datos**). Y se repite entre convocatorias del mismo fondo → **la estructura es estable**; el piloto se construye contra ella, no contra un llamado puntual.

Diferencia de énfasis:
- **Crea y Valida** e **Innova AT**: la pregunta a futuro; la tracción actual va en la **Encuesta** (números).
- **Consolida y Expande** agrega una sección **Escalabilidad** que exige la **tracción actual como texto abierto evaluado** — ventas a la fecha + comprometidas, clientes con pruebas y resultados, capital levantado. Porque es para escalar algo que **ya vende**.
- **Innova AT** empuja fuerte la **continuidad financiera** (levantar capital: VC, préstamos, alianzas) y fija el horizonte de proyección **a 3 años**.

## 3. La columna vertebral — pregunta por pregunta (30 min)

Aparece en **ambos** formularios. Para cada una: qué pide · cómo la aborda el piloto · en qué reunión. Anotamos tu sugerencia. (Detalle y referencias exactas en `MAPEO-formularios.md` §1.)

| # | Pregunta | Cómo la aborda el piloto | Reunión | Sugerencia de la jefa |
|---|---|---|---|---|
| **S1** | Caracterizar el problema + causas + fuentes | `perfil_comercial` (cualitativo) | R#1 | |
| **S2** | **Dimensionar** el problema, cuanti y cuali, documentado | `investigacion_mercado` (magnitud + fuentes verificadas) | Búsqueda de mercado | |
| **S3** | Actores / usuarios / clientes afectados, con antecedentes de interés, dimensionados | `investigacion_mercado.tamano_mercado` + `supuestos_modelo.segmentos` + clientes potenciales | Búsqueda + R#2 | |
| **S4** | Atributos que diferencian de **sustitutos disponibles** (CyV pide cuantificar) | `investigacion_mercado.competidores` + `narrativa.diferenciacion` (mercado). Novedad técnica → GT | Búsqueda + R#2 | |
| **S5** | **Modelo de ingresos**: clientes, cómo se cobra, % mercado, captar/fidelizar, canales, **supuestos + fuentes** | `supuestos_modelo` (pricing, tipo de ingreso, canales) + `encaje_mercado` (% mercado) + lista de supuestos con evidencia/fuentes | R#2 + construcción | |
| **S6** | **Magnitud** de ingresos / ahorro, cuantificada (CyE la ata al escalamiento) | `modelo_negocio.proyeccion` + `impacto_continuidad` | Construcción | |
| **S7** | Impactos sociales / ambientales, cuantificados | `impacto_continuidad.impacto_esperado` | R#2 + construcción | |
| **S8** | Riesgos y barreras **comerciales / regulatorias** + cómo se abordan | `impacto_continuidad.riesgos_barreras` (comercial 🟢 / regulatorio 🟡) | R#2 | |
| **S10** | **Continuidad post-subsidio** | `impacto_continuidad.estrategia_continuidad` (se sostiene con la economía del modelo). Protección de resultados → GT | R#2 + construcción | |

> S9 (propiedad intelectual), S11–S14 (objetivos/resultados técnicos, descripción de la solución, TRL, equipo) → **GT**. Ver `MAPEO-formularios.md`.

## 4. Lo propio de Consolida y Expande (10 min)

| Pregunta | Cómo la aborda el piloto | Sugerencia de la jefa |
|---|---|---|
| Tipo de escalamiento (nacional/internacional) + país + síntesis | `plan_escalamiento.estrategia_escalamiento` + `narrativa` | |
| Desafíos del escalamiento comerciales | `plan_escalamiento` / `riesgos_barreras` (técnico-regulatorio → GT) | |
| **Tracción actual** — ventas a la fecha + comprometidas, nº clientes con pruebas y resultados, capital levantado | ⛳ **gap** — hoy el piloto no lo estructura | |

**Propuesta para el gap:** bloque `perfil_comercial.traccion_actual` (ventas históricas + comprometidas, año de primera venta, nº clientes/usuarios, pruebas y resultados, capital propio + levantado, % exportación), levantado en **R#1** + la **tarea de datos**. Sirve también para las preguntas de la Encuesta de CyV. ¿De acuerdo?

## 5. Acuerdos y preguntas (10 min)

- **2 reuniones** para el modelo de negocio: decidido. Excepción a validar: **3 para Consolida y Expande** (Escalabilidad + tracción pesan mucho), **1 para Capital Humano**.
- **Caso real de prueba:** el modelo de negocio de la postulación a **Crea y Valida que se rechazó**. ¿Lo corremos por el flujo y lo revisamos juntas, o lo dejo listo y lo comentamos?
- **Ingeniero comercial:** ¿hay hoy alguien en el equipo que pueda revisar cómo queda ese caso?
- **Formato de entrega a F19:** ¿un documento, campos estructurados, una planilla?

### Salida esperada
- La columna "Sugerencia de la jefa" llena (S1–S10 + Consolida y Expande).
- Con eso: qué se mueve de R#2 a R#1 (o viceversa), y si Consolida y Expande necesita 3 reuniones.
- Visto bueno (o no) al bloque `traccion_actual`.
- Caso real acordado y quién lo revisa.

---

## Apéndice — Definiciones abiertas (solo si sobra tiempo)

- **Estrategia de pricing por defecto:** comparación con el mercado / margen sobre costo / valor capturable. (Recomiendo partir por comparación con el mercado.)
- **Qué hace un modelo "no postulable":** lienzo incoherente · cada venta pierde plata sin palanca · el punto de equilibrio no cabe en el mercado alcanzable.
- **LTV / CAC / payback:** solo para modelos recurrentes; para el resto, margen de contribución + punto de equilibrio bastan.
- **Horizonte de proyección:** 3 o 5 años.
