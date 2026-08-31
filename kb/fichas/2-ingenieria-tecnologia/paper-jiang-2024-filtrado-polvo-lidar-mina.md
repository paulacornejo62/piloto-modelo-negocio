---
id: paper-jiang-2024-filtrado-polvo-lidar-mina
titulo: "Algorithm for Point Cloud Dust Filtering of LiDAR for Autonomous Vehicles in Mining Area (Jiang et al., 2024)"
tipo: paper
tema: Cuantificación del efecto del POLVO en suspensión sobre el LiDAR de un vehículo autónomo y filtrado de la nube de puntos
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [percepcion-lidar-clima, superficie-no-pavimentada, percepcion-obstaculos-outdoor, vehiculo-autonomo-carga, mineria-remota-automatizacion]
anio: 2024
autores: [Xianyao Jiang, Yi Xie, Chongning Na, Wenyang Yu, Yu Meng]
referencia: https://doi.org/10.3390/su16072827
motor: WebSearch → MDPI (mirror mdpi-res.com, PDF full-text)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "6-7 (probado en operación real, mina a cielo abierto Dananhu N.º 2)"
metricas_clave: ["hasta 37 frenadas falsas en un ciclo de transporte, promedio 18,3 antes del filtro", "tras el filtro: 0 a 5 frenadas falsas por día con 4 vehículos, promedio 2,1", "velocidad límite del vehículo no tripulado fijada en 18 km/h por superficie irregular y sin tratar", "carga de cómputo del filtro +9% respecto a no filtrar", "ciclo de transporte 1,64 km ida / 3,28 km lazo cerrado, 20-30 vueltas/día"]
fecha_registro: 2026-08-03
proyectos:
  - kaufmann-vehiculo-autonomo
---

## Pregunta / objetivo de investigación
¿Cómo distinguir en la nube de puntos LiDAR el polvo en suspensión (obstáculo falso) de un cuerpo rígido real, para evitar frenadas espurias de un camión autónomo en una faena de superficie suelta?

## Hipótesis
El polvo, por su gran separación entre partículas, produce retornos parcialmente reflejados/parcialmente transmitidos: baja intensidad de reflectancia y densidad espacial dispersa, características que permiten separarlo de un cuerpo rígido sin recurrir a aprendizaje profundo.

## Metodología
- **Diseño:** experimental con datos de operación real (mina a cielo abierto Dananhu N.º 2, China).
- **Datos / muestra:** nubes de puntos capturadas por vehículo autónomo de carga siguiendo a un camión de gran tonelaje (3,4 m ancho × 9 m largo × 3,9 m alto) a menos de 20 m; ciclo de 1,64 km cargado / 3,28 km lazo cerrado, 20-30 ciclos diarios.
- **Técnicas:** muestreo aleatorio y remoción de fondo; plantilla de confianza inicial basada en reflectividad láser; re-cribado por distancia euclidiana entre puntos vecinos; filtrado final de polvo denso según la plantilla corregida.
- **Métricas:** frecuencia de frenadas falsas por ciclo (validadas por el operador de seguridad a bordo), carga de cómputo, eficiencia de transporte.

## Resultados principales
- **Antes del algoritmo:** *"a maximum of 37 false brakes (the highest recorded number) can occur within a single transportation cycle, with an average of 18.3 brakes."*
- **Después:** *"the occurrence rate of false braking events in a single transportation cycle approached zero, while the incidence of false braking during the joint operation of four vehicles in a single day ranges from 0 to 5 times, with an average frequency of 2.1 occurrences."*
- El polvo se asocia fuertemente a las operaciones de riego de caminos del sitio, pero *"due to the strong randomness of ground dryness, water-spraying volume and evaporation rate, quantification of the association remains challenging."*
- El límite de velocidad del vehículo no tripulado se fija en **18 km/h** por la superficie irregular y sin tratar y las pendientes.
- Tras el filtrado: eficiencia de conducción en vacío +176,84%, con carga +227,92%, ciclo completo +82,3%; sobrecarga de cómputo del filtro solo +9%.

## Conclusiones
El polvo generado por el propio tránsito sobre superficie suelta es, cuantitativamente, el principal degradador de la percepción LiDAR en este entorno: convierte la operación autónoma en una secuencia de frenadas espurias hasta el punto de duplicar la duración del ciclo. Es mitigable con filtrado dedicado, pero requiere desarrollo específico y calibración local.

## Limitaciones
- Validado en un sitio único (una mina), con hardware específico; los autores reportan variaciones entre vehículos por diferencias de hardware.
- Los datos no son públicos.
- No cuantifican precisión/recall del filtro con métricas estándar de detección; la evidencia es operacional (frenadas falsas), no de laboratorio.
- El método asume que el polvo tiene baja reflectividad y densidad dispersa; no se prueba contra niebla densa (los autores la mencionan como trabajo futuro junto con humo y cortinas de agua).

## Relevancia / brecha para el estado del arte
Es la evidencia cuantitativa más directa disponible del riesgo del caso Kaufmann: **superficie no pavimentada (maicillo) + tránsito pesado = polvo en suspensión = falsos positivos de obstáculo que detienen al vehículo**. Muestra tres cosas útiles para la postulación: (1) la magnitud del problema es de decenas de eventos por ciclo, no marginal; (2) existe mitigación, pero es desarrollo a nivel de nube de puntos —es decir, requiere acceso al pipeline de percepción, algo incompatible con un vehículo entregado como caja negra con algoritmos cerrados; (3) la velocidad operativa se limita por la superficie, no solo por seguridad normativa.

> Relaciones: complementa a [[paper-kim-2023-degradacion-lidar-lluvia-niebla]] (misma familia de degradación por partículas, distinto agente) y a [[paper-lu-2020-deteccion-borde-camino-mina]].
