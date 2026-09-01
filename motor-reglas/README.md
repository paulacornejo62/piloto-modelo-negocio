# Motor de reglas (determinista)

La **columna determinista** del piloto: cálculos exactos y repetibles que NO se
dejan al criterio del LLM (un modelo podría alucinar un umbral). Separado de lo
generativo.

## Archivos
- **`parametros.json`** — umbrales editables: margen de contribución mínimo, LTV/CAC
  mínimo, payback máximo, penetración de SOM (alerta/crítico), horizonte de
  proyección por defecto. **PRIMERA VERSIÓN — todos POR VALIDAR con ingeniería
  comercial** (varían por tipo de negocio). Se ajustan aquí, no en `reglas.py`.
- **`formularios.json`** — secciones del formulario oficial por fondo (*fund-aware*).
- **`documentos_postulacion.json`** — manifiesto de los entregables del modelo de
  negocio por fondo (lo que arma el paquete de `tools/postulacion.py`).
- **`reglas.py`** — funciones puras, sin dependencias externas.

## Funciones
| Función | Qué calcula | Se usa en |
|---|---|---|
| `mercado_coherencia(tam, sam, som)` | verifica SOM ≤ SAM ≤ TAM; marca lo que falta/no cuadra | EVAL_P2 / EVAL_P4 |
| `unit_economics(precio, costo_var, fijos, cac, vida)` | margen de contribución, LTV, LTV/CAC, payback, punto de equilibrio | EVAL_P4 |
| `proyeccion(precio, costo_var, fijos, u_año1, crec_%, años)` | tabla anual ingresos/costos/resultado | EVAL_P4 |
| `proyeccion_escenarios(unit_in, escenarios, años)` | corre `proyeccion()` por escenario (pesimista/base/optimista) | EVAL_P4 |
| `encaje_mercado(ingresos_año_final, som)` | penetración de SOM + estado ok/alerta/crítico | EVAL_P4 |
| `indicadores_viabilidad(ue, enc)` | estado (ok/alerta/crítico/sin_dato) de cada indicador vs. su umbral | EVAL_P5 |
| `compuerta_viabilidad(indicadores, info_suficiente, pe, som, opt)` | **SÓLIDO / AJUSTAR / INVIABLE / DEVOLVER** | EVAL_P5 |
| `coherencia_cifras_cliente(cifras)` | inconsistencias entre cifras declaradas por el cliente | transversal (`render --validar`) |
| `qa_coherencia_modelo(...)` | 5 reglas de coherencia de la Fase 2 (embudo de mercado, proyección vs SOM, supuestos registrados, límite de caracteres, cifras vs modelo) | FORM_W5 |

### Convención de las funciones de unit economics / proyección
Toman **ENTRADAS** (precio, costo variable, fijos, CAC, vida del cliente, crecimiento)
y devuelven **SALIDAS** calculadas. La "unidad" es lo que el modelo defina (un
cliente/mes, una transacción, un equipo). `proyeccion()` interpreta precio y costo
variable como valores **anuales** por unidad activa: si el modelo es mensual, el
caller anualiza (×12) antes de llamar. **POR VALIDAR con ingeniería comercial.**

## Probar
```bash
python3 motor-reglas/reglas.py --test    # asserts
python3 motor-reglas/reglas.py --demo    # ejemplo legible
```

> Los skills (construir modelo, revisión, QA) **invocan estas funciones** en vez de
> razonar los umbrales.
