---
name: mn-estado
description: Estado, resumen y retomar de un caso de modelo de negocio (o de toda la cartera). Dice dónde va un caso, qué se completó, qué sigue, y orienta para reanudar el trabajo sin releer todo. Invocar con "¿dónde va [caso]?", "estado de [caso]", "retoma [caso]", o "panel" para ver toda la cartera.
---

# Estado / Resumen / Retomar

Orienta al consultor sobre un caso o la cartera completa. Solo lectura + guía.

## Para un caso
1. Corre el estado: `python3 tools/estado.py <tenant>` — muestra pasos hechos (✓), paso
   actual, compuerta de viabilidad, QA y la **siguiente acción**.
2. Lee la última sesión: `python3 tools/bitacora.py listar <tenant>` (o la línea "Última
   sesión" del estado).
3. **Retomar guiado**: resume en 2-3 líneas para el consultor: *dónde quedó*, *qué se
   decidió la última vez*, y *qué hacer ahora* (la "Siguiente acción"). Si para avanzar
   falta un insumo del cliente (notas de reunión, datos comerciales, info del proyecto),
   dilo explícito.

## Para la cartera
`python3 tools/panel.py` — todos los casos con su paso, avance, compuerta y última sesión.
Útil para "¿cómo va todo?".

## Registrar avance (al terminar de trabajar)
Después de un bloque de trabajo, **guarda la sesión** para poder retomar:
```bash
python3 tools/bitacora.py registrar <tenant> "Qué se hizo" "decisiones / contexto"
```
El orquestador también lo hace al cerrar cada paso del flujo.
