---
id: normativa-nestle-guidance-note-tintas-primers-barnices
titulo: "Nestlé — Guidance Note on Packaging Inks (octubre 2018): requisitos a proveedores sobre tintas, primers y barnices de sobreimpresión"
tipo: normativa
tema: Restricción de CLIENTE que alcanza al desarrollo — exige la Ordenanza Suiza como piso, prohíbe el TAA como promotor de adhesión y usa el impacto sensorial negativo sobre el alimento como criterio de exclusión
area_oecd: "2 Ingeniería y Tecnología (2.4 Ingeniería química)"
topicos: [tinta-barrera-impresa, recubrimiento-funcional-prensa, envase-flexible-compostable]
anio: 2018
autores: [Nestlé — Research, FCM Department; contacto Stephen Klump, Head of Global FCM-Safety & Compliance]
referencia: https://www.nestle.com.pe/sites/g/files/pydnoa276/files/nosotros/informacion-proveedores-nestle/documents/actualizacion%202019/guidance%20note%20on%20packaging%20inks%20-%20version%202018.pdf (PDF, 7 pp., octubre 2018; versión previa septiembre 2016)
motor: WebSearch + extracción con pdftotext; el QA lo obtuvo por vía alterna y leyó el texto completo
profundidad_lectura: full-text por el investigador y el QA; NO reabierto en esta sesión — la URL devuelve HTTP 403 (Cloudflare) verificado el 2026-08-07
estado_evidencia: parcial
trl_relevante: "-"
fecha_registro: 2026-08-07
proyectos:
  - edelpa-compostables
---

## Por qué una guía de cliente entra a la base de conocimiento
Porque **condiciona el espacio de solución técnica aunque la propiedad intelectual del desarrollo quede en el convertidor**. Un envase que no cumple los requisitos del dueño de la marca no se vende, por elegante que sea su química. Cuando el cliente final es Nestlé, esta guía es un borde duro del diseño, no una recomendación.

**Naturaleza de la evidencia:** documento de requisitos de un cliente corporativo a sus proveedores. Evidencia de **restricción comercial vinculante en la práctica**; no es legislación ni norma técnica de organismo normalizador.

## Alcance declarado — y por qué alcanza a una tinta barrera
> «This document equally applies to: **printing inks, primers and overprint lacquers/coatings/varnishes** which are applied by conventional press or digital ink processes.»

La palabra clave es *primers* y *coatings*: una eventual **«tinta barrera»** o un **«primer barrera»** aplicados en la prensa **caen dentro del alcance literal** de la guía. No es un documento sobre el diseño gráfico del envase; es un documento sobre todo lo que la prensa deposita.

## Las tres restricciones que importan al desarrollo

**1. La Ordenanza Suiza como piso, con lista cerrada.**
> «In the absence of local legislation, Nestlé requires inks to be formulated using ingredients that are listed in the Swiss Ink Ordinance on Materials and Articles and respect the migration limits contained therein.»

> «Substances not listed in the Swiss Ink Ordinance are not allowed to be used in any part of a food packaging ink formulation.»

Esto es lo más restrictivo de la guía y merece leerse dos veces: **no es una lista de prohibidos, es una lista de permitidos**. Un ligante nuevo, un aditivo funcional inédito o un componente barrera no listado quedan fuera **por defecto**, aunque nadie haya demostrado que sean nocivos. Para un desarrollo que quiera meter química funcional en la capa impresa, esto acota el espacio de formulación antes de empezar.

**2. Exclusiones nominales.**
> «Titanium Acetyl Acetonate (TAA) must not be used as an adhesion promoter.»

El **TAA queda prohibido como promotor de adhesión** — y la adhesión es justamente el problema que aparece al poner una capa funcional sobre un sustrato celulósico. También quedan fuera los ftalatos *orto* y la nitrocelulosa para envases aptos para horno o microondas.

**3. El criterio sensorial como exclusión.**
> «Press washes and fountain solutions must not contain solvents and other chemicals which give off-odour or taint to the food.»

Y entre los criterios de selección de sus listas, expresamente:
> «negative sensory impact on the packed food or in points of sale»

**Un componente puede ser inocuo, cumplir todos los límites de migración y aun así quedar excluido por alterar el aroma del producto.** Para café soluble —un producto cuyo valor percibido es en buena medida aromático— este criterio no es secundario: es probablemente el más exigente de los tres.

## LIMITACIÓN DE ALCANCE — el matiz del QA que el barrido no declaró
El propósito del documento dice que **«specifically addresses inks used for the OUTSIDE of Nestlé packaging materials»**. De ahí se siguen dos precisiones que hay que hacer siempre:

1. Una capa barrera aplicada en el **interior** de un laminado **podría quedar fuera de su alcance literal**. La lectura de que la guía alcanza a una eventual tinta o primer barrera es correcta **solo para capas exteriores**.
2. **El documento NO cubre adhesivos de laminación.** Si la función barrera se reparte hacia el adhesivo, esa parte del sistema no está regida por esta guía —y hay que buscar cuál otra la rige—.

## Estado de la evidencia y qué falta
- Las **seis citas fueron verificadas literales** por el QA contra el texto completo del PDF (7 páginas), junto con la publicación de octubre de 2018, la versión previa de septiembre de 2016 y el contacto responsable.
- **El PDF está protegido por Cloudflare**: `curl` y navegador devuelven **HTTP 403**. Se confirmó nuevamente el 2026-08-07. Por eso el `estado_evidencia` es **parcial**: las citas están verificadas por el QA, pero la fuente **no es reabrible por la vía declarada** y la ficha no puede auditarse sola.
- **Puede existir una versión posterior.** Una búsqueda arrojó una referencia a «Printing inks St-80-001-01 April 24» que **no fue abierta**. **Confirmar la versión vigente directamente con el cliente** antes de fijar requisitos en un proyecto: trabajar contra una guía de 2018 cuando hay una de 2024 es un riesgo evitable y barato de cerrar.

> Relacionadas: [[informe-siegwerk-aptitud-tintas-envase-compostable]] (el otro borde: EN 13432 limita la masa de tinta; esta guía limita su química) · [[producto-siegwerk-cirkit-oxybar-tinta-barrera-oxigeno]] · [[patente-wo2025155500a1-sun-chemical-tinta-blanca-barrera-oxigeno]] · [[patente-es3061314t3-nestle-papel-metalizado-alta-barrera]] (el mismo cliente, patentando en el vecindario técnico).
