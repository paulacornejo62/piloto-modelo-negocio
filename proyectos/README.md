# proyectos/ — postulaciones

Una **carpeta por postulación** (tenant), aislada del resto. Estructura:
```
proyectos/<slug>/
├── expediente.json     # estado tipado de la postulación
├── README.md           # estado del caso en una hoja: dónde va, por qué, qué falta para retomar
├── bitacora.md         # memoria de sesiones (tools/bitacora.py)
├── entradas/           # BUZÓN: inputs del cliente (reuniones, docs, transcripciones) — los agentes buscan aquí
│   ├── reunion-1.md · reunion-2.md · <docs del cliente>
│   └── README.md
└── <generados>         # expediente.md, laminas-comite.md, formulario-<fondo>.md, plan-trabajo.xlsx…
```

El `README.md` del tenant es para el humano que retoma: **estado del caso** (paso alcanzado,
si está activo / frenado / cerrado y por qué), qué quedó construido y reutilizable, y qué haría
falta para seguir. El `expediente.md` es la proyección completa y generada; el README es la
hoja de entrada. Se escribe/actualiza al cerrar un bloque de trabajo o al cambiar el estado
del caso.

- **Arranca vacío.** Se crea una postulación con el skill `mn-nuevo-proyecto` (que crea el buzón `entradas/`).
- **El consultor deja los inputs en `entradas/`** (entre pasos y sesiones); los pasos que necesitan input del cliente buscan ahí.
- Los datos de cliente son **confidenciales**: las carpetas de postulaciones reales están **gitignoreadas** (no se versionan).
- Fixtures de prueba (caso ficticio) NO van aquí — viven en [`../../desarrollo/pruebas/`](../../desarrollo/pruebas/).
