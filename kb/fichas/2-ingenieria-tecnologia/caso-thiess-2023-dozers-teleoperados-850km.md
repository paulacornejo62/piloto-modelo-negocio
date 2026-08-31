---
id: caso-thiess-2023-dozers-teleoperados-850km
titulo: "Thiess + Caterpillar + Hastings Deering — operación remota de múltiples bulldozers Cat D11 a más de 850 km (Lake Vermont, Queensland, junio 2023)"
tipo: caso
tema: Despliegue comercial de operación remota semiautónoma de maquinaria pesada minera a gran distancia
area_oecd: "2 Ingeniería y Tecnología (2.3 Ingeniería mecánica)"
topicos: [mineria-teleoperacion-equipos, teleoperacion-supervision-remota, recinto-privado-odd]
anio: 2023
autores: [Thiess, Caterpillar, Hastings Deering]
referencia: https://thiess.com/news/innovation/big-names-in-mining-team-up-to-demonstrate-remote-semi-autonomous-dozer-technology
motor: WebSearch + WebFetch (comunicado oficial Thiess; replicado por Caterpillar y Mining Magazine Australia)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "8-9 (producto comercial en operación productiva)"
metricas_clave: ["estación remota a más de 850 km del sitio", "6 bulldozers Cat D11 en Lake Vermont", "8,2 millones de m3 bancados movidos", "+25% de utilización", "hasta 23 h/día de operación (vs ~17 h convencional)", "demostración 28-06-2023 desde el World Mining Congress, Brisbane"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Contexto / caso
En junio de 2023, durante el World Mining Congress en Brisbane, Thiess operó **múltiples bulldozers Cat D11** ubicados en la mina Lake Vermont (Queensland central) desde una estación remota situada "over 850km away from the site", usando **Cat MineStar Command for dozing** con sistemas de tractor semiautónomo (SATS). El comunicado destaca que era "the first time multiple dozers have been controlled off-site for a customer" desde que el producto está comercialmente disponible.

## Cifras del despliegue
- 6 bulldozers Cat D11 operando en Lake Vermont, uno de los mayores despliegues activos de SATS del mundo.
- Más de 8,2 millones de metros cúbicos bancados movidos.
- Mejora de utilización de 25%, llegando hasta 23 horas de operación diaria.
- Con la capa de autonomía habilitada, **un operador controla varios equipos** sin necesidad de estar físicamente en el sitio.

## Qué demuestra y qué no
- **Demuestra**: que la operación remota de maquinaria minera pesada a más de 850 km es tecnología comercial disponible (no experimental) cuando el fabricante provee el paquete completo (máquina + control + infraestructura) y la tarea es semiautónoma y acotada (empuje de material en un área definida).
- **No demuestra**: conducción remota de camiones de carretera en tiempo real por vías mixtas, ni continuidad de enlace garantizada 24/7 sobre red pública; la distancia se resuelve con arquitectura de centro remoto sobre enlaces corporativos, y la carga de tiempo real está aliviada por la capa de autonomía a bordo (el operador no cierra el lazo de estabilización).

## Limitaciones de esta ficha
- Fuente: comunicado corporativo (Thiess) más replicaciones de prensa especializada y de Caterpillar. No hay publicación técnica revisada con métricas de red, latencia ni tasa de incidentes.
- No se verificaron independientemente las cifras de producción ni de utilización.

## Relevancia / brecha para el estado del arte
Es el referente comercial más claro de "operar equipo minero pesado desde otra ciudad": muestra que **la distancia no es la variable crítica** cuando existe autonomía local que absorbe la latencia. Se suma a la evidencia de [[caso-centros-operacion-remota-larga-distancia-mineria]] (Rio Tinto 1.500 km, BHP, AMSA) y refuerza la distinción de [[review-majstorovic-2022-conceptos-teleoperacion-vehiculos]] entre control directo (sensible a latencia) y conceptos con autonomía a bordo (robustos a latencia).

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
