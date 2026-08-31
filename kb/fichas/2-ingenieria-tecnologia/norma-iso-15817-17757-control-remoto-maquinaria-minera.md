---
id: norma-iso-15817-17757-control-remoto-maquinaria-minera
titulo: "ISO 15817:2012 (control remoto de maquinaria de movimiento de tierra) e ISO 17757:2019 (sistemas autónomos y semiautónomos en minería)"
tipo: norma
tema: Marco normativo existente para el control remoto y la operación autónoma de maquinaria pesada de movimiento de tierra y minería
area_oecd: "2 Ingeniería y Tecnología (2.3 Ingeniería mecánica)"
topicos: [teleoperacion-supervision-remota, mineria-teleoperacion-equipos, seguridad-funcional-av, recinto-privado-odd]
anio: 2019
autores: [ISO/TC 127 Earth-moving machinery]
referencia: https://www.iso.org/standard/46237.html (ISO 15817:2012) ; https://www.iso.org/standard/76126.html (ISO 17757:2019)
motor: WebSearch (páginas ISO con HTTP 403; metadatos confirmados en ANSI Webstore, iTeh, GlobalSpec, SIS y nota de prensa ISO)
profundidad_lectura: metadata
estado_evidencia: parcial
trl_relevante: "-"
metricas_clave: ["ISO 15817:2012 2a edición, reemplaza a ISO 15817:2005", "ISO 17757:2019 2a edición, reemplaza a ISO 17757:2017", "aplica a EMM según ISO 6165 y a máquinas móviles de minería de superficie y subterránea"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Contexto / qué es
Dos normas ISO delimitan el terreno normativo de la operación a distancia de maquinaria pesada, con una frontera explícita entre ellas:

- **ISO 15817:2012 — "Earth-moving machinery — Safety requirements for remote operator control systems"**: especifica los requisitos esenciales de seguridad de los sistemas de control remoto (inalámbricos y/o cableados) usados en maquinaria de movimiento de tierra definida en ISO 6165. Según los metadatos consultados, **no aplica** a sistemas de control autónomo que operan sin asistencia de un operador, ni al control remoto de implementos sobre máquinas no controladas remotamente; la edición 2005 además no especificaba criterios de desempeño del sistema de control remoto.
- **ISO 17757:2019 — "Earth-moving machinery and mining — Autonomous and semi-autonomous machine system safety"**: requisitos de seguridad para máquinas autónomas y semiautónomas (ASAMS) de movimiento de tierra y minería, superficie y subterránea, incluyendo hardware, software e infraestructura asociada, a lo largo del ciclo de vida. Declara **no ser aplicable a la capacidad de control remoto** (cubierta por ISO 15817), salvo cuando esa capacidad forma parte de un ASAMS.

## Qué implica para un proyecto de telecomando de camiones en faena
- El **control remoto de maquinaria pesada ya tiene norma de seguridad** (ISO 15817), lo que confirma que el telecomando como capacidad de máquina es tecnología establecida y normada — no es, por sí solo, novedad tecnológica.
- La frontera normativa (15817 remoto ↔ 17757 autónomo) deja **sin cobertura explícita** el caso híbrido que aparece en la teleoperación moderna sobre red móvil: enlace de largo alcance, degradación de QoS, estrategias de estado seguro dependientes de la red y ODD de teleoperación. Ese vacío es el que están intentando llenar documentos como BSI Flex 1886/1887 y el trabajo de UNECE GRVA (ver [[norma-bsi-flex-1887-factores-humanos-operacion-remota]]).

## Limitaciones de esta ficha
- **No se accedió al texto de las normas** (iso.org devolvió HTTP 403 y el contenido es de pago). Alcance y exclusiones provienen de las páginas de catálogo de distribuidores oficiales (ANSI Webstore, iTeh, SIS, GlobalSpec) y de la nota de prensa de ISO. Debe verificarse contra el texto oficial antes de citarlo en una postulación.
- No se verificó si existe adopción chilena (NCh) equivalente.

## Relevancia / brecha para el estado del arte
Sirve para el análisis Frascati: la existencia de ISO 15817 sostiene que "operar una máquina por control remoto" es estado del arte normado, mientras que la operación **a gran distancia sobre red pública, con requisitos de continuidad 24/7 y estrategias de degradación**, no está cubierta por estas normas y sigue siendo objeto de investigación (ver [[preprint-brettin-2026-odd-teleoperacion-mrm]]).

> Relaciones con otras fichas (cita_a, contradice, misma_tecnologia, relacionada_con, complementa) → `../../indice.json`.
