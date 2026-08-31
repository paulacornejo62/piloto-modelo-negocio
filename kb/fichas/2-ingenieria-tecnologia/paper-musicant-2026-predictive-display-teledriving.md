---
id: paper-musicant-2026-predictive-display-teledriving
titulo: "Safety, Efficiency, and Mental Workload of Predictive Display in Simulated Teledriving (Musicant, Kuperman & Barachman 2025/2026)"
tipo: paper
tema: Efecto del retardo moderado y del display predictivo en el desempeño y la carga mental del teleconductor
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [latencia-teleoperacion, factores-humanos-operador-remoto, teleoperacion-supervision-remota]
anio: 2026
autores: [Oren Musicant, Alexander Kuperman, Rotem Barachman]
referencia: https://pmc.ncbi.nlm.nih.gov/articles/PMC12788196/ (Sensors 26(1):221, DOI 10.3390/s26010221)
motor: WebSearch + PMC full-text
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "3-4 (experimento en simulador CARLA)"
metricas_clave: ["N=29 participantes", "condiciones: 50 ms, 150 ms sin PD, 150 ms con PD", "colisiones 0 (50 ms) vs 3 (150 ms)", "errores de navegación 3 vs 5", "NASA-TLX sin diferencias significativas", "PSSUQ 3,52-3,72 / 5"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Pregunta / objetivo de investigación
¿Mejora el display predictivo (que muestra la posición estimada del vehículo compensando el retardo) el desempeño, la seguridad y la carga mental del teleconductor bajo retardos moderados, típicos de redes 4G/5G?

## Hipótesis
Bajo retardo moderado (150 ms), el display predictivo debería mejorar el desempeño y reducir la carga mental respecto de la misma condición sin compensación.

## Metodología
- **Diseño:** experimental intra-sujeto en simulador.
- **Datos / muestra:** 29 estudiantes (21 mujeres, edad media 25 años, 7,5 años de experiencia de conducción).
- **Técnicas:** simulador CARLA, tres monitores de 27", volante Logitech G920 con force feedback; entorno urbano diurno; tres condiciones de retardo (50 ms base; 150 ms sin display predictivo; 150 ms con display predictivo).
- **Métricas:** tiempos de recorrido, errores de navegación, colisiones, intensidad de frenado/dirección, NASA-TLX (carga mental), PSSUQ (usabilidad).

## Resultados principales
- El retardo de 150 ms **no degradó significativamente** el desempeño frente a 50 ms: tiempos de recorrido equivalentes, 3 vs 5 errores de navegación, 0 vs 3 colisiones (diferencias no significativas), NASA-TLX sin diferencias significativas.
- El display predictivo **no produjo mejoras medibles** en esa ventana de retardo: "the predictive display did not yield measurable improvements under moderate delay"; reducción de errores de navegación con OR = 0,2 pero sin significancia estadística.
- Conclusión de los autores: "human teleoperators were able to maintain stable control and workload even with a 150 ms delay"; la utilidad del display predictivo se limitaría a retardos superiores (>200 ms).

## Conclusiones
En la ventana de retardo alcanzable por redes móviles actuales (~150 ms) y a velocidades urbanas, un operador humano mantiene control estable sin compensación; la compensación predictiva importa cuando el retardo crece.

## Limitaciones
- Simulador, no vehículo real: no reproduce jitter real, pérdida de paquetes ni degradación de video.
- Participantes sin experiencia profesional como teleoperadores; tasas bajas de colisión/error limitan la potencia estadística.
- Una sola implementación de display predictivo; vehículo liviano en entorno urbano, no camión pesado ni faena.

## Relevancia / brecha para el estado del arte
Matiza el discurso de "latencia ultrabaja o nada": a ~150 ms el operador humano se desempeña bien. El corolario relevante para un proyecto de telecomando es que el problema crítico no es alcanzar decenas de milisegundos, sino **garantizar que el retardo se mantenga acotado y estable el 100% del tiempo**, y qué ocurre cuando no lo está. Contrasta con los umbrales recopilados en [[review-kamtam-2024-latencia-red-teleoperacion-cav]] y con la latencia glass-to-glass medida en campo por [[paper-testouri-2025-5g-teleoperacion-evaluacion-experimental]].

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
