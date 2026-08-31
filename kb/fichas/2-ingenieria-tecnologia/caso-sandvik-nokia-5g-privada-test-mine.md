---
id: caso-sandvik-nokia-5g-privada-test-mine
titulo: "5G en la mina de pruebas subterránea de Sandvik: red privada 5G standalone de Nokia para automatización y tele-remoto (Nokia/Sandvik, 2021)"
tipo: caso
tema: Red privada 4.9G/LTE y 5G SA en entorno minero real, orientada a operación tele-remota de máquinas sobre enlaces de video 4K
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [redes-privadas-lte-5g-industriales, mineria-remota-automatizacion, teleoperacion-supervision-remota]
anio: 2021
autores: [Nokia; Sandvik Mining and Rock Solutions]
referencia: https://www.mining.sandvik/globalassets/campaigns/minexpo-2021/content-library/automation/nokia-sandvik-5g-case-study.pdf
motor: WebSearch + WebFetch (PDF) — lectura por páginas
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 6-7
metricas_clave: [">85 % de las aplicaciones mineras digitales ya corren sobre 4.9G", "Nokia DAC: cobertura pico 20–100 m, micro 0,5–5 km, mini-macro <30 km, macro <50 km", "5G SA en fase temprana de implementación (2021)"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Qué documenta

Caso de estudio Nokia–Sandvik sobre el despliegue de red privada 4.9G/LTE y 5G standalone en la mina de pruebas subterránea de Tampere, Finlandia.

Citas textuales:
> "The new 5G infrastructure will add even more capabilities to automated mining processes and enable remote machine operations over 4K video links between the deep underground and the surface control center."
> "A private LTE network enables fast, reliable and secure voice, data and video communications in a mining setting, which presents highly challenging deployment conditions."
> "many mines still rely on legacy networks that weren't created for the demands of ultra-broadband and mission-critical use cases."
> "more than 85% of digital mining applications can already run on 4.9G today. And, 5G will add even more capabilities, like more bandwidth for (ultra-) high-definition video services and further reduce the latency that is needed for real-time tele-remote control of e.g., robots and drones."
> "With 5G, Sandvik will be able to reserve a certain capacity from the bandwidth to specific applications, resulting in predictable performance and improved reliability."
> Andreas Simoncic (Sandvik): "Mining digitalization and automation are highly dependent on a predictable communication infrastructure. We need reliable data and analytics for telemetry, autonomy and optimization. Without a stable, fast and resilient network none of these would be possible."
> "Sandvik's 5G standalone network implementation in the Test Mine is in early stages and the plan is to gradually further expand the network."
> Sobre estandarización: "5G R16 was just finalized in July 2020 and together with R17 it will bring critical machine connectivity features such as ultra-low latency and time-sensitive networking."

## Relevancia / brecha para el estado del arte

- El **control tele-remoto en tiempo real sobre video 4K** aparece explícitamente como capacidad que 5G "añadirá", no como capacidad ya productiva sobre 4.9G — y el despliegue 5G SA se describe en fase temprana (2021, mina de pruebas del fabricante, no faena en producción).
- La reserva de capacidad por aplicación (antesala del network slicing) se presenta como el mecanismo para lograr "predictable performance" — el atributo que la teleoperación necesita y que el best-effort no entrega.
- Consistente con [[paper-theissen-2023-tecnologias-inalambricas-mineria-subterranea]]: 5G cumple en especificación; la validación operacional en faena activa es lo que falta.

> Relaciones con otras fichas → `../../indice.json`.
