---
id: caso-redes-privadas-lte-mineria-chile-centinela-salares-norte
titulo: "Redes privadas LTE industriales en faenas mineras de Chile: Minera Centinela (Nokia–Antofagasta Minerals, 2022) y Gold Fields Salares Norte (Claro–Nokia, 2021)"
tipo: caso
tema: Estado de despliegue de redes privadas 4.9G/LTE de grado industrial en minería chilena y qué conectan
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [redes-privadas-lte-5g-industriales, mineria-remota-automatizacion, espectro-regulacion-chile]
anio: 2022
autores: [Nokia / Antofagasta Minerals; Claro Chile / Nokia (notas de prensa corporativas y prensa especializada)]
referencia: "https://www.globenewswire.com/news-release/2022/03/14/2402774/0/en/Nokia-and-Antofagasta-Minerals-deploy-private-wireless-network-to-accelerate-digital-transformation-of-Minera-Centinela-operations-in-Chile.html · https://www.telesemana.com/blog/2021/04/28/claro-chile-anuncia-la-implementacion-de-una-red-privada-lte-en-una-mina/"
motor: WebSearch + WebFetch (nota GlobeNewswire de Nokia; TeleSemana)
profundidad_lectura: full-text
estado_evidencia: parcial
trl_relevante: 9
metricas_clave: ["Centinela: red privada 4.9G/LTE desplegada en 4 meses; plan de digitalización a 5 años", "Centinela: conecta inicialmente una flota de camiones autónomos (11 unidades Komatsu 980E-5 según prensa especializada)", "Salares Norte: 150 sensores y 72 vehículos y máquinas conectadas", "Equipamiento Centinela: AirScale, mobile packet core, routers IP/MPLS, transmisión microondas Wavence"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Qué documenta

**Minera Centinela (Antofagasta Minerals + Nokia, marzo 2022)** — citas textuales de la nota oficial:
> "Private 4.9G/LTE network, deployed within four months, will support operations"
> "will initially connect a fleet of autonomous trucks" (como parte de "a five-year digitalization plan")
> "Nokia AirScale radio equipment, mobile packet core, IP/MPLS service aggregation routers, and Wavence microwave transmission"

La cifra de "11 camiones eléctricos autónomos Komatsu 980E-5 de 363 t" aparece en prensa especializada (International Mining), **no** en la nota oficial revisada → dato parcial.

**Gold Fields Salares Norte (Claro Chile + Nokia, abril 2021)** — citas de TeleSemana:
> "solución privada LTE, que incluye radio AirScale, small cells, núcleo de paquetes, enrutadores IP y sistema de administración de red NetAct"
> "la red conectará 150 sensores para procesos operativos, monitorización y prevención de accidentes, además de 72 vehículos y máquinas conectadas"
> Menciona "camiones, excavadoras, perforadoras y en el futuro, drones a control remoto".

**No verificado / ausente en las fuentes revisadas**: banda de espectro utilizada, régimen de permiso ante Subtel, cifras de latencia, disponibilidad medida o si soportan teleoperación con lazo humano cerrado.

## Relevancia / brecha para el estado del arte

- **Problema resuelto en Chile**: la red privada LTE de grado industrial en faena minera es tecnología comercial disponible localmente (al menos dos despliegues documentados, con integradores locales), incluidos casos que conectan flota autónoma.
- **Brecha**: ninguna fuente pública revisada declara desempeño de red (latencia, jitter, disponibilidad medida) ni el marco de espectro/permiso bajo el que operan. Ese es el dato que un diseño de teleoperación necesita y que no está publicado.
- Complementa a [[caso-nokia-komatsu-2020-lte-privada-flota-autonoma]] (evidencia global) con el aterrizaje chileno.

> Relaciones con otras fichas → `../../indice.json`.
