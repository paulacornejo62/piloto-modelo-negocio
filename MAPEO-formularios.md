# Mapeo — formularios Crea y Valida (2025) y Consolida y Expande (2024)

Preguntas de contenido de ambos formularios **reales**, marcando cuáles **se repiten**, cuáles son **específicas** de uno, y cómo las aborda el piloto.

Alcance: 🟢 piloto · ⚪ equipo GT · 🟡 mixto (una parte piloto, otra GT) · ⛳ gap del piloto.

> Fuente: formularios de postulación 2024/2025. No se listan las preguntas de administración (RUT, direcciones, montos del presupuesto, autorizaciones) ni la Encuesta de caracterización estadística; se resumen en §5.

---

## Hallazgo principal

**La pregunta central de modelo de negocio es idéntica en ambos formularios** — CyV *Impacto Q1* = CyE *Estrategia de Negocio Q1*, palabra por palabra:

> *"Describa el modelo de ingresos o ahorro de costos económicos... indique quiénes serán los clientes y cómo se les cobrará (venta por unidad de producto, licenciamiento de una tecnología, suscripción temporal a un servicio, entre otros), % mercado a abarcar, estrategia para captar y fidelizar clientes... canales de distribución... Debe explicar sus supuestos e indicar claramente cuáles son sus fuentes de datos."*

Diferencia entre fondos:
- **Crea y Valida** la pregunta una vez (a futuro) y pone la tracción actual en la **Encuesta** (números).
- **Consolida y Expande** la pregunta **y agrega una sección Escalabilidad** que exige la **tracción actual como texto abierto evaluado** (ventas a la fecha + comprometidas, clientes con pruebas y resultados, capital levantado) — porque es para escalar algo que **ya vende**.

---

## 1. Columna vertebral compartida (aparece en ambos formularios)

Es el ejercicio a validar con la jefa. Sirve para CyV, CyE y probablemente Innova Alta Tecnología.

| # | Pregunta (texto abreviado) | CyV | CyE | Cómo la aborda el piloto | Reunión · alcance |
|---|---|---|---|---|---|
| **S1** | Diagnóstico: identificar y caracterizar el problema/desafío/oportunidad + causas + fuentes | Problema Q1 | Problema Q1 | `perfil_comercial.problema_u_oportunidad` (cualitativo, en palabras del cliente) | R#1 · 🟢 |
| **S2** | Diagnóstico: **dimensionar** el problema cuanti y cuali, fundado y documentado | Problema Q2 | Problema Q2 | `investigacion_mercado` (magnitud con cifras y fuentes verificadas) | Búsqueda de mercado · 🟢 |
| **S3** | Mercado objetivo: identificar, caracterizar (con antecedentes que demuestran interés/necesidad) y dimensionar los actores (usuarios/clientes) afectados o beneficiados | Problema Q3 | Problema Q3 | `investigacion_mercado.tamano_mercado` (TAM/SAM/SOM) + `supuestos_modelo.segmentos` + hallazgos de clientes potenciales / pipeline | Búsqueda + R#2 · 🟢 |
| **S4** | Novedad/diferenciación: atributos que agregan valor y diferencian de **sustitutos disponibles en el mercado** (CyV pide *cuantificar*) | Solución Q11 | Solución Q9 | `investigacion_mercado.competidores` + `narrativa.diferenciacion` (diferenciación de mercado). La novedad técnica → GT | Búsqueda + R#2 · 🟡 |
| **S5** | **Modelo de ingresos / ahorro de costos**: clientes, cómo se cobra (unidad/licencia/suscripción), **% mercado a abarcar**, captar/fidelizar, canales, **supuestos + fuentes de datos** | Impacto Q1 | Estrategia Neg. Q1 | `supuestos_modelo` (pricing, `estructura_ingresos.tipo`, canales) + `modelo_negocio.encaje_mercado` (% mercado = `penetracion_som_pct`) + la lista de supuestos con `estado_evidencia` y `fuentes` | R#2 + construcción · 🟢 |
| **S6** | **Magnitud** de los ingresos / ahorro, cuantificada y justificada (CyE la ata al escalamiento nacional/internacional) | Impacto Q2 | Estrategia Neg. Q2 | `modelo_negocio.proyeccion` (por escenario) + `impacto_continuidad` | Construcción · 🟢 |
| **S7** | Impactos **sociales y/o medioambientales** relevantes, cuantificados objetiva y justificadamente | Impacto Q3 | Problema Q4 (+ beneficiarios indirectos) | `impacto_continuidad.impacto_esperado.social/ambiental` | R#2 + construcción · 🟢 |
| **S8** | **Riesgos y/o barreras comerciales y/o regulatorias** + cómo serán abordadas (texto idéntico) | Escalab. Q4 | Problema Q5 | `impacto_continuidad.riesgos_barreras` (comercial 🟢 / regulatorio 🟡) | R#2 · 🟡 |
| **S9** | **Propiedad intelectual / apropiabilidad** (qué/cómo/por qué proteger, o por qué no) | Escalab. Q5 | Estrategia Neg. Q3 | — | ⚪ GT |
| **S10** | **Continuidad del proyecto una vez concluido el subsidio** | Escalab. Q6 | (implícita en Escalab. Q10) | `impacto_continuidad.estrategia_continuidad` (cómo se sostiene con la economía del modelo). La protección de resultados → GT | R#2 + construcción · 🟡 |
| **S11** | Título · Resumen · Objetivo general · Objetivos específicos · Resultados + indicadores | Proyecto Q1–5 | Proyecto Q1–5 | Título y resumen → `narrativa`. Objetivos y resultados técnicos → GT (el piloto aporta el hilo de mercado) | Redacción · 🟡 |
| **S12** | Mercado objetivo (dropdown) · Tendencia tecnológica (dropdown) · ¿Ha postulado antes? | Proyecto Q6–7, Q18 | Proyecto Q6–7, Q14 | Selección simple; el piloto tiene el dato (`meta`, `perfil_comercial.historia_previa`) | R#1 · 🟢 |
| **S13** | Describir la solución / producto / proceso + estado del prototipo actual · TRL | Solución Q1, Q3–5 | Metodología Q1–2 | Descripción técnica y TRL → GT; el piloto solo referencia `perfil_comercial.estado_desarrollo` | — · ⚪ GT |
| **S14** | Capacidades del beneficiario · equipo de trabajo · dedicación horaria · CVs | Participantes Q1, Q5–7 | Participantes Q1, Q4–5 | — | ⚪ GT |

---

## 2. Específicas de Crea y Valida (2025)

| Pregunta | Alcance |
|---|---|
| ¿Se basa en ciclos biológicos? (permite plazo hasta 36 meses) | ⚪ GT (dato técnico) |
| Hipótesis científicas/tecnológicas a poner a prueba (Metodología Q2) | ⚪ GT |
| TRL **esperado** al finalizar el proyecto (Metodología Q5) | ⚪ GT |
| **Hito técnico de continuidad** (dentro de etapa Crea) y **hito de cambio Etapa Crea → Valida** (Metodología Q8–9) — CyV tiene 2 etapas | ⚪ GT (hito técnico). El piloto aporta los **hitos comerciales** por separado (`plan_escalamiento.hitos_comerciales`) |
| Sección propia **Actividades de I+D**: ¿genera nuevo conocimiento / producto-proceso mejorado / ambas? (Q12) + demostrar mejora sustancial vs. patentes existentes (Q13) | ⚪ GT |
| Encuesta CyV más granular sobre tracción: **año de la primera venta**, **% de ventas al extranjero**, monto de ventas brutas de la solución | 🟡 el piloto tiene el dato si se levanta "tracción actual" (§4) |

---

## 3. Específicas de Consolida y Expande (2024)

| Pregunta | Alcance |
|---|---|
| Duración máx **24 meses** | dato de encuadre |
| **Beneficiarios indirectos** (Mercado Q4) — CyV lo fusiona con impactos sociales/ambientales | 🟢 `impacto_continuidad` |
| **Desafíos de I+D resueltos** durante la generación del producto que se busca escalar (Metodología Q5) + respaldos I+D — mira hacia **atrás**, no hacia adelante | ⚪ GT |
| Escalabilidad Q4: **tipo de escalamiento** (nacional / internacional / ambos) | 🟢 `plan_escalamiento` |
| Escalabilidad Q5: **país de expansión + fundamento** (≥ 50 car.) | 🟢 `plan_escalamiento.estrategia_escalamiento` |
| Escalabilidad Q6: **desafíos del escalamiento** (técnicos / regulatorios / **comerciales**) | 🟡 comercial 🟢 / técnico-regulatorio ⚪ |
| Escalabilidad Q7: **ingresos por ventas a la fecha + ventas comprometidas** | ⛳ **gap** — §4 |
| Escalabilidad Q8: **nº de clientes/usuarios actuales + con qué se hicieron pruebas y qué resultados** | ⛳ **gap** — §4 |
| Escalabilidad Q9: **inversión propia + capital levantado** (montos, aportes públicos/privados) | ⛳ **gap** — §4 (más "antecedentes"; va en la tarea de datos) |
| Escalabilidad Q10: **síntesis** — cómo todo lo anterior permite el escalamiento nacional/internacional | 🟢 `narrativa` + `plan_escalamiento` |

---

## 4. El gap: "tracción actual" estructurada

Ambos formularios preguntan por la tracción actual, pero:
- **CyV**: en la Encuesta, como números (nº usuarios, nº clientes, monto de ventas, año de primera venta, % exportación).
- **CyE**: en Escalabilidad, como **texto abierto evaluado** (Q7–Q9) — pesa en la nota.

El piloto hoy solo tiene `perfil_comercial.clientes_actuales` (texto libre) y `plan_escalamiento.estado_actual`.

**Propuesta de cambio chico** (agregar a Parte 4 de `NOTAS-preparacion-reuniones.md`):

- Nuevo bloque **`perfil_comercial.traccion_actual`**:
  `{ ventas_historicas_clp, ventas_comprometidas_clp, anio_primera_venta, n_clientes, n_usuarios,
     pruebas_y_resultados (texto), capital_propio_clp, capital_levantado_clp,
     capital_levantado_publico_pct, export_pct }`.
- Pedirlo explícitamente en **R#1** y en la **tarea de datos** post-R#1.
- `mn-eval-reunion-1` + `expediente.schema.json` lo recogen; `render.py` lo muestra en el Panel.

---

## 5. Lo que no se lista aquí

- **Administración** (ambos): RUT, razón social, objeto social, representante legal, direcciones, tamaño de empresa, ventas de los últimos 12/24 meses, F29, montos del presupuesto (costo total, aporte Corfo, aportes pecuniarios/no pecuniarios), asociados y entidades colaboradoras. → cliente + GT.
- **Encuesta de caracterización** (ambos, ~20 preguntas, solo fines estadísticos): presencia web/RRSS, empresa liderada por mujeres, fase del proyecto de innovación, tipo/alcance de innovación, nº usuarios/clientes actuales, modelo B2B/B2C/B2G, método de protección (Sí/No), capital levantado (Sí/No), créditos, contribución climática, objetivos ambientales/sociales, Ley REP, nº de personas en el proyecto y sueldos, certificaciones ambientales, interés en networking. → en su mayoría se alimenta de lo que el piloto ya levanta (fase, nº clientes, B2B/B2C, modelo de ingresos) + datos del cliente.
