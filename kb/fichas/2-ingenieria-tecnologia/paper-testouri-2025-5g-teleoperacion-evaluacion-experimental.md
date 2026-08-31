---
id: paper-testouri-2025-5g-teleoperacion-evaluacion-experimental
titulo: "5G-Enabled Teleoperated Driving: An Experimental Evaluation (Testouri, Elghazaly, Hawlader & Frank 2025)"
tipo: preprint
tema: Medición experimental de latencias extremo a extremo en conducción teleoperada sobre 5G
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [conectividad-vehiculo-autonomo, teleoperacion-fallback]
anio: 2025
autores: [Mehdi Testouri, Gamal Elghazaly, Faisal Hawlader, Raphael Frank]
referencia: https://arxiv.org/abs/2503.14186
motor: WebSearch + arXiv (HTML full-text)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "4-5 (prototipo experimental sobre red 5G NSA pública)"
metricas_clave: ["latencia glass-to-glass media 202,41 ms (σ 31,56)", "RTT de comandos 46,67 ms (σ 10,05)", "RTT TCP 27,63 ms para 128 KB", "jitter UDP 0,709 ms", "retardo total de dirección hasta 750 ms"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-vehiculo-autonomo
  - kaufmann-telecomando
---

## Pregunta / objetivo de investigación
Cuantificar experimentalmente si una red 5G disponible permite conducción teleoperada segura, midiendo latencias de video y de comandos extremo a extremo.

## Hipótesis
El 5G reduce la latencia de red lo suficiente para teleoperación, pero el cuello de botella puede desplazarse a la cadena de video (captura-codificación-transmisión-render).

## Metodología
- **Diseño:** medición experimental sobre vehículo real y red 5G NSA en banda 3,6 GHz.
- **Datos:** 100 mediciones de latencia glass-to-glass en 90 s; 1000 mediciones de RTT de comandos.
- **Métricas:** RTT TCP/UDP, jitter, pérdida de paquetes, latencia glass-to-glass, retardo de actuación de dirección.

## Resultados principales
- Latencia glass-to-glass media **202,41 ms** (σ 31,56 ms; rango 150 a más de 300 ms): el video sigue siendo el cuello de botella pese al 5G.
- RTT de comandos de control **46,67 ms** (σ 10,05 ms), suficiente para teleoperación a velocidades moderadas.
- Retardo total de dirección (red + actuación del vehículo) de hasta **750 ms**.
- Red: RTT TCP 27,63 ms para paquetes de 128 KB, jitter UDP 0,709 ms, cero pérdida de paquetes en las pruebas.

## Conclusiones
Con 5G la teleoperación es factible en operación acotada (los autores discuten operación limitada a baja velocidad), pero la latencia percibida del video y el retardo de actuación imponen límites de velocidad y exigen diseño explícito del lazo de control.

## Limitaciones
Un solo vehículo, red pública NSA, condiciones favorables (sin pérdida de paquetes). No evalúa handover ni degradación en zonas de sombra ni fallback ante caída de enlace.

## Relevancia / brecha para el estado del arte
Da números duros para dimensionar la capa de monitoreo/control remoto de un vehículo en recinto: la latencia relevante no es la de ping (decenas de ms) sino la de video (200 ms), lo que condiciona velocidad de operación y estrategia de supervisión.

**Citas textuales:**
- "The average G2G latency is 202.41ms with a standard deviation of 31.56ms"
- "These results indicate that even on a 5G network, a live video stream can still induce a significant latency"

> Relaciones con otras fichas → `../../indice.json`.
