# Motor de reglas (determinista)

La **columna determinista** del sistema: cálculos exactos y repetibles que NO se dejan al criterio del LLM (un modelo podría alucinar un umbral). Separado de lo generativo.

## Archivos
- **`instrumentos.json`** — datos duros: constantes Ley I+D (crédito 35%, tope 15.000 UTM, contabilidad completa, TRL≥4) y parámetros por instrumento CORFO (TRL mín, topes, % cofinanciamiento por tamaño, bono mujer, antigüedad, plazo). _Revisar contra bases vigentes antes de decisiones reales._
- **`reglas.py`** — funciones puras, sin dependencias externas.

## Funciones
| Función | Qué calcula | Se usa en |
|---|---|---|
| `frascati(comp_i, comp_d)` | cuadrante 2×2 + `es_id` | EVAL_P4-II |
| `ley_id_elegible(contabilidad, trl)` | requisitos duros Ley I+D | EVAL_P4 / QA |
| `instrumentos_elegibles(trl, tamaño, antigüedad, lidera_mujer)` | qué instrumentos aplican + % cofinanciamiento + tope | EVAL_P4-III (perfil de subsidios) |
| `cofinanciamiento(instrumento, tamaño, lidera_mujer)` | % CORFO | — |
| `compuerta(es_id, voto_comite)` | GO / PIVOT / NO-GO | EVAL_P5 |

## Probar
```bash
python3 motor-reglas/reglas.py --test    # asserts
python3 motor-reglas/reglas.py --demo     # ejemplo legible
```

> Los skills (Frascati, perfil de subsidios, compuerta) **invocan estas funciones** en vez de razonar los umbrales. Pendiente: las 4 reglas de QA de coherencia de Formulación (FORM) se agregarán aquí.
