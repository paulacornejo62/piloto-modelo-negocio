# Mapeo — formularios CORFO (modelo de negocio / mercado / escalamiento)

Preguntas de contenido de **tres formularios reales**, marcando cuáles **se repiten** entre fondos, cuáles son **específicas** de uno, y cómo las aborda el piloto.

| Fondo | Convocatoria mapeada | Sección donde vive el modelo de negocio |
|---|---|---|
| **Crea y Valida (CyV)** | 2025 | "Propuesta de Introducción al Mercado" → Impacto + Escalabilidad |
| **Consolida y Expande (CyE)** | 2024 | "Plan de Negocios" → Estrategia de Negocio + Escalabilidad |
| **Innova Alta Tecnología (IAT)** | 2022 | sección propia **"Modelo de negocios"** |

Alcance: 🟢 piloto · ⚪ equipo GT · 🟡 mixto · ⛳ gap del piloto.

> **Referencia viva.** Las bases se actualizan convocatoria a convocatoria: pueden cambiar el foco, alguna pregunta o el orden. Lo que **no** cambia es la estructura — la columna vertebral (§1) se repite entre fondos y entre años (CyE 2024 y CyV 2025 comparten el texto exacto de la pregunta central). El piloto se construye contra esa columna vertebral, no contra el wording de una convocatoria. Al usar el mapeo, verificar contra las bases vigentes del llamado.

---

## Hallazgo principal

**La pregunta central de modelo de negocio aparece en los tres formularios, casi idéntica** — CyV *Impacto Q1* = CyE *Estrategia de Negocio Q1* = IAT *Modelo de Negocios Q2*:

> *"¿Cómo se les cobrará (venta por unidad de producto, licenciamiento de una tecnología, suscripción temporal a un servicio, entre otros), % mercado a abarcar, estrategia para captar y fidelizar clientes... canales de distribución... Debe explicar sus supuestos e indicar claramente cuáles son sus fuentes de datos."*

Diferencia de énfasis entre fondos:
- **CyV**: la pregunta una vez (a futuro). La tracción actual va en la **Encuesta** (números).
- **CyE**: la pregunta **y agrega Escalabilidad** que exige la **tracción actual como texto abierto evaluado** (ventas a la fecha + comprometidas, clientes con pruebas, capital levantado) — es para escalar algo que **ya vende**.
- **IAT**: sección "Modelo de negocios" completa; empuja fuerte la **continuidad financiera** (levantar capital, VC, alianzas). La tracción actual va en la Encuesta.

---

## 1. Columna vertebral compartida (aparece en los tres)

Es el ejercicio a validar con la jefa. Referencias exactas por fondo entre paréntesis.

| # | Pregunta (texto abreviado) | CyV | CyE | IAT | Cómo la aborda el piloto | Reunión · alcance |
|---|---|---|---|---|---|---|
| **S1** | Caracterizar el problema/desafío/oportunidad + causas + fuentes (cualitativo) | Problema Q1 | Problema Q1 | Problema Q1 | `perfil_comercial.problema_u_oportunidad` | R#1 · 🟢 |
| **S2** | **Dimensionar** el problema, cuanti y cuali, con supuestos y **fuentes de datos** | Problema Q2 | Problema Q2 | Problema Q2 | `investigacion_mercado` (magnitud + fuentes verificadas) | Búsqueda de mercado · 🟢 |
| **S3** | Mercado objetivo / **actores** (usuarios, clientes, gremios…) afectados o beneficiados + dimensionar | Problema Q3 | Problema Q3 | Problema Q3 + Modelo Neg. Q1 | `investigacion_mercado.tamano_mercado` + `supuestos_modelo.segmentos` + clientes potenciales | Búsqueda + R#2 · 🟢 |
| **S4** | **Alternativas / sustitutos disponibles** + sus fallas · qué **valor agrega** vs. esas alternativas (CyV pide cuantificar los atributos) | Solución Q11 | Solución Q9 | Solución Q10 + Q13 | `investigacion_mercado.competidores` + `narrativa.diferenciacion` + `supuestos_modelo.propuesta_valor`. Novedad **técnica** → GT | Búsqueda + R#2 · 🟡 |
| **S5** | **Modelo de ingresos / ahorro**: clientes, cómo se cobra, **% mercado a abarcar**, captar/fidelizar, canales, **supuestos + fuentes** | Impacto Q1 | Estrategia Neg. Q1 | Modelo Neg. Q2 | `supuestos_modelo` (pricing, `estructura_ingresos.tipo`, canales) + `modelo_negocio.encaje_mercado` (% mercado = `penetracion_som_pct`) + supuestos con `estado_evidencia`/`fuentes` | R#2 + construcción · 🟢 |
| **S6** | **Magnitud** de ingresos / ahorro, cuantificada y justificada (CyE la ata al escalamiento; IAT pide "a tres años") | Impacto Q2 | Estrategia Neg. Q2 | Modelo Neg. Q3 | `modelo_negocio.proyeccion` (por escenario) + `impacto_continuidad` | Construcción · 🟢 |
| **S7** | Impactos **sociales y/o medioambientales** relevantes, cuantificados | Impacto Q3 | Problema Q4 (+ beneficiarios indirectos) | ODS + foco + Encuesta | `impacto_continuidad.impacto_esperado` | R#2 + construcción · 🟢 |
| **S8** | **Riesgos y barreras comerciales y/o regulatorias** + cómo se abordan (texto idéntico en los tres) | Escalab. Q4 | Problema Q5 | Modelo Neg. Q4 | `impacto_continuidad.riesgos_barreras` (comercial 🟢 / regulatorio 🟡) | R#2 · 🟡 |
| **S9** | **Propiedad intelectual / apropiabilidad** | Escalab. Q5 | Estrategia Neg. Q3 | Modelo Neg. Q5 | — | ⚪ GT |
| **S10** | **Continuidad post-subsidio** (IAT empuja la incorporación de capital: VC, préstamos, alianzas) | Escalab. Q6 | (implícita Escalab. Q10) | Modelo Neg. Q6 | `impacto_continuidad.estrategia_continuidad` (se sostiene con la economía del modelo). Protección de resultados → GT | R#2 + construcción · 🟡 |
| **S11** | Título · Resumen · Objetivo general · Objetivos específicos · Resultados + indicadores | Proyecto Q1–5 | Proyecto Q1–5 | Proyecto Q1–5 | Título/resumen → `narrativa`. Objetivos y resultados técnicos → GT | Redacción · 🟡 |
| **S12** | Mercado objetivo (dropdown) · Tendencia tecnológica (dropdown) · ¿Ha postulado antes? | Proyecto Q6–7, Q18 | Proyecto Q6–7, Q14 | Proyecto Q6–7, Q17 | Selección simple; el piloto tiene el dato (`meta`, `historia_previa`) | R#1 · 🟢 |
| **S13** | Describir la solución / producto / proceso + estado del prototipo · TRL actual y esperado · hipótesis · estado del arte | CyV Solución Q1–10 | CyE Metodología Q1–5 | IAT Solución Q4–12 | Descripción técnica, TRL, hipótesis, estado del arte → GT; el piloto solo referencia `perfil_comercial.estado_desarrollo` | — · ⚪ GT |
| **S14** | Capacidades del beneficiario · recursos · equipo · dedicación horaria · CVs | Participantes | Participantes | Capacidades | — | ⚪ GT |

---

## 2. Específicas de Crea y Valida (2025)

| Pregunta | Alcance |
|---|---|
| ¿Se basa en ciclos biológicos? (plazo hasta 36 meses) | ⚪ GT |
| **Hito técnico de continuidad** dentro de etapa Crea · **hito de cambio Etapa Crea → Valida** (Metodología Q8–9) — CyV tiene 2 etapas | ⚪ GT (hito técnico); el piloto aporta los **hitos comerciales** por separado |
| Sección propia **Actividades de I+D**: ¿nuevo conocimiento / producto-proceso mejorado / ambas? (Q12) + mejora sustancial vs. patentes (Q13) | ⚪ GT |
| Encuesta CyV granular sobre tracción: **año de la primera venta**, **% de ventas al extranjero**, monto de ventas brutas de la solución | 🟡 si se levanta "tracción actual" (§5) |

## 3. Específicas de Consolida y Expande (2024)

| Pregunta | Alcance |
|---|---|
| Duración máx **24 meses** | encuadre |
| **Beneficiarios indirectos** (Mercado Q4) — CyV lo fusiona con impactos sociales/ambientales | 🟢 `impacto_continuidad` |
| **Desafíos de I+D resueltos** durante la generación del producto que se busca escalar (Metodología Q5) + respaldos — mira hacia **atrás** | ⚪ GT |
| Escalabilidad Q4–Q5: **tipo de escalamiento** (nacional/internacional) + **país + fundamento** | 🟢 `plan_escalamiento.estrategia_escalamiento` |
| Escalabilidad Q6: **desafíos del escalamiento** (técnicos/regulatorios/comerciales) | 🟡 comercial 🟢 / técnico-regulatorio ⚪ |
| Escalabilidad **Q7–Q9**: ingresos por ventas a la fecha + comprometidas · nº clientes actuales + pruebas y resultados · inversión propia + capital levantado — **como texto abierto evaluado** | ⛳ **gap** — §5 |
| Escalabilidad Q10: **síntesis** — cómo lo anterior permite el escalamiento | 🟢 `narrativa` + `plan_escalamiento` |

## 4. Específicas de Innova Alta Tecnología (2022)

| Pregunta | Alcance |
|---|---|
| Duración máx **48 meses** (60/72 con ciclos biológicos) | encuadre |
| **ODS principal** + **foco temático** del llamado (era un concurso focalizado: agua, energía, H2, economía circular) | selección; el piloto aporta el encuadre pero el foco lo fija el llamado |
| **Estado del arte** como sección propia con referencias académicas y patentes (Solución Q11) — "novedad **mundial**" | ⚪ GT (fondo I+D-intensivo) |
| Modelo de Negocios Q3: magnitud de ingresos/ahorro **a tres años** | 🟢 (fija el horizonte de proyección en 3 años para este fondo) |
| Modelo de Negocios Q6: continuidad con **foco financiero explícito** — inversionistas ángeles/VC, préstamos, reinversión de socios, financiamiento público, joint venture, alianzas | 🟢 `impacto_continuidad.estrategia_continuidad` — conviene un campo de "vías de financiamiento post-subsidio" |
| Q7–8 (nº usuarios/clientes) y Q6 encuesta (capital levantado) van en la **Encuesta** (números), no como texto evaluado (a diferencia de CyE) | 🟡 el bloque `traccion_actual` (§5) también las cubre |

---

## 5. El gap: "tracción actual" estructurada

Los tres formularios preguntan por la tracción actual, pero:
- **CyV** e **IAT**: en la **Encuesta**, como números (nº usuarios, nº clientes, monto de ventas, año de primera venta, % exportación, capital levantado Sí/No).
- **CyE**: en **Escalabilidad**, como **texto abierto evaluado** (Q7–Q9) — pesa en la nota.

El piloto hoy solo tiene `perfil_comercial.clientes_actuales` (texto libre) y `plan_escalamiento.estado_actual`.

**Propuesta de cambio chico** (agregar a `NOTAS-preparacion-reuniones.md` Parte 4):

- Nuevo bloque **`perfil_comercial.traccion_actual`**:
  `{ ventas_historicas_clp, ventas_comprometidas_clp, anio_primera_venta, n_clientes, n_usuarios,
     pruebas_y_resultados (texto), capital_propio_clp, capital_levantado_clp,
     capital_levantado_publico_pct, export_pct }`.
- Se pide en **R#1** y en la **tarea de datos** post-R#1.
- Lo recogen `mn-eval-reunion-1` + `expediente.schema.json`; `render.py` lo muestra en el Panel.
- Cubre CyE Escalabilidad Q7–Q9 (texto) y alimenta las preguntas numéricas de la Encuesta de CyV/IAT.

---

## 6. Lo que no se lista aquí

- **Administración** (los tres): RUT, razón social, objeto social, representante legal, direcciones, tamaño de empresa, ventas de los últimos 12/24/36 meses, F29, montos del presupuesto, asociados y entidades colaboradoras. → cliente + GT.
- **Encuesta de caracterización** (los tres, ~10–20 preguntas, fines estadísticos): presencia web/RRSS, empresa liderada por mujeres, fase del proyecto de innovación, tipo/alcance de innovación, nº usuarios/clientes actuales, modelo B2B/B2C/B2G, método de protección (Sí/No), capital levantado (Sí/No), créditos, contribución climática, objetivos ambientales/sociales, Ley REP (CyV), RRHH y sueldos, certificaciones ambientales, interés en networking. → en su mayoría se alimenta de lo que el piloto ya levanta + datos del cliente.
