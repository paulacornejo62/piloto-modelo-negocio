---
id: paper-emmert-2021-bioormocer-recubrimiento-barrera-compostable
titulo: "bioORMOCER®—Compostable Functional Barrier Coatings for Food Packaging (Emmert, Amberg-Schwab et al., Polymers 2021)"
tipo: paper
tema: Recubrimiento barrera híbrido inorgánico-orgánico biodegradable aplicado por flexografía en línea; la única demostración publicada con datos completos de «barrera compostable aplicada en prensa», y la que muestra el precio que se paga en migración
area_oecd: "2 Ingeniería y Tecnología (2.4 Ingeniería química)"
topicos: [recubrimiento-funcional-prensa, envase-flexible-compostable, barrera-oxigeno-otr, tinta-barrera-impresa, migracion-contacto-alimentario]
anio: 2021
autores: [Katharina Emmert, Sabine Amberg-Schwab, Francesca Braca, Agostino Bazzichi, Antonio Cecchi, Ferdinand Somorowsky]
referencia: "Polymers (Basel) 13(8):1257, 2021 — DOI 10.3390/polym13081257 — https://pmc.ncbi.nlm.nih.gov/articles/PMC8068916/ (PMC8068916)"
motor: Europe PMC / PubMed Central (XML full-text)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 5
metricas_clave: ["OTR sustrato desnudo 1413 cm³·m⁻²·d⁻¹·bar⁻¹", "OTR con ORMOCER® 19", "OTR con bioORMOCER® 25 (DIN 53380-3, 23 °C, 50 % HR)", "flexografía 10–80 m/min, 3–4 g/m²", "biodegradación 92,9 % y 93,0 % a 91 días", "migración global 11,8 mg/dm² sobre PLA con ácido acético 3 % a 60 °C (límite 10)"]
fecha_registro: 2026-08-07
proyectos:
  - edelpa-compostables
---

## Pregunta / objetivo de investigación
¿Puede un recubrimiento barrera **biodegradable** aplicarse con el equipamiento de impresión que ya tiene un convertidor —flexografía, a velocidad industrial— y entregar a la vez barrera al oxígeno, compostabilidad certificable y cumplimiento de contacto alimentario? Es exactamente la apuesta que un proyecto de «tinta o recubrimiento barrera compostable» necesita ver demostrada o refutada.

El equipo del Fraunhofer ISC (Würzburg) partió de los ORMOCER® —recubrimientos híbridos inorgánico-orgánicos ya conocidos como barrera— y construyó una versión **bio**, con la pregunta implícita de cuánto desempeño cuesta hacerlos biodegradables.

## Hipótesis
Que la química híbrida sol-gel admite una reformulación con precursores de origen renovable sin perder el efecto barrera de forma sustantiva, y que el recubrimiento resultante puede aplicarse por vía húmeda en unidades de impresión convencionales en vez de exigir metalización al vacío o coextrusión.

## Metodología
- **Diseño:** desarrollo experimental de materiales con escalado a piloto industrial y caracterización completa (barrera, biodegradación, desintegración, ecotoxicidad, migración).
- **Aplicación:** los recubrimientos se aplicaron *«using Uteco flexographic off-line printing units»* a velocidades *«set between 10 and 80 m/min»*, con un peso de capa de **3–4 g/m²** (≈3 µm). Esto es lo decisivo: no es una barra de laboratorio, es una prensa.
- **Sustratos:** film poliolefínico (PO, no biodegradable, usado como referencia de barrera) y films biodegradables PLA y PLA/PBAT.
- **Barrera:** OTR por método isostático con gas portador, **DIN 53380-3, a 23 °C y 50 % HR**.
- **Compostabilidad:** biodegradación en compost y desintegración a 12 semanas.
- **Contacto alimentario:** migración global por inmersión total, 10 días a 60 °C y a 40 °C, con tres simulantes (agua destilada, etanol 10 % v/v, ácido acético 3 % w/v), contra el límite de **10 mg/dm²** del Reglamento (UE) 10/2011.

## Resultados principales
**Barrera al oxígeno.** El texto es literal:
> «The uncoated PO substrate has an OTR of 1413 cm³ m⁻² d⁻¹ bar⁻¹. This value can be massively reduced to 19 cm³ m⁻² d⁻¹ bar⁻¹ by applying a thin layer of about 3 µm of ORMOCER®. With an OTR of 25 cm³ m⁻² d⁻¹ bar⁻¹, the bioORMOCER® coating provides an only slightly worse value, still low enough for numerous packaging applications.»

Es decir: **el peaje de hacerlo biodegradable es 19 → 25**, un deterioro modesto. Y la mejora sobre el sustrato desnudo es de casi dos órdenes de magnitud.

**Compostabilidad.** 92,9 % de biodegradación para PLA + bioORMOCER® y 93,0 % para PLA/PBAT + bioORMOCER® a los 91 días; desintegración completa bajo la fracción de 2 mm en 12 semanas.

**Migración global — aquí falla.** Tabla 13 (60 °C, 10 días), en mg/dm², límite 10:

| Muestra | Agua | Etanol 10 % | Ácido acético 3 % |
|---|---|---|---|
| Film PO | 12 | 15 | 4,2 |
| PO + bioORMOCER® | <0,1 | <0,1 | 7,7 |
| Film PLA | 1,7 | 3,1 | 3,2 |
| **PLA + bioORMOCER®** | 9,5 | 5,9 | **11,8** |
| PLA/PBAT + bioORMOCER® | 5,7 | 3,1 | 6,4 |

Una sola condición supera el límite: **PLA recubierto, simulante ácido, 60 °C → 11,8 mg/dm²**. Los autores lo declaran y lo explican por la temperatura de curado (sobre PO se cura a 130 °C, sobre PLA solo a 80 °C, y el curado más caliente da redes más estables). Reensayado a 40 °C (Tabla 14), el mismo sistema cumple: 7,6 mg/dm².

## Conclusiones
El recubrimiento barrera compostable aplicable en prensa **existe y funciona**, con un costo de desempeño acotado frente a su equivalente no biodegradable, y con un punto de falla identificado y localizado en la combinación PLA + simulante ácido + condición severa.

## Limitaciones
- **El OTR se midió sobre sustrato poliolefínico, no biodegradable.** El número que da la barrera y el que da la compostabilidad **no provienen de la misma muestra**. La estructura íntegramente compostable con barrera medida no está publicada en este trabajo.
- **50 % HR, no condición húmeda de operación.** Todo el desempeño barrera está medido en semiseco. Para un producto higroscópico en clima real, el dato no traslada (ver [[review-2026-asimetria-barrera-oxigeno-agua-recubrimientos-biodegradables]]).
- **No hay WVTR.** El trabajo no reporta barrera al vapor de agua.
- Escala piloto: 10–80 m/min es industrialmente creíble, pero no es producción sostenida validada.

## Advertencias del QA adversarial (deben viajar con el dato)
1. **La norma es la serie EN 1186, no «EN 1186-3» a secas.** El informe original de Deep Research escribió «EN 1186-3»; el QA lo corrigió a *«European standard series EN 1186 (draft methods at the time of testing)»*, que es como el artículo lo enuncia en su sección de métodos, y cuya referencia bibliográfica [24] es EN 1186-1:2002. **Matiz añadido en esta ficha por verificación directa del XML completo (07-ago-2026):** la Tabla 1 del propio artículo **sí nombra «EN 1186-3»** como método de migración global para los tres simulantes. Ambas cosas son ciertas: el cuerpo del texto habla de la serie y de métodos en borrador; la tabla de condiciones especifica la parte 3. Al citar en un formulario, lo seguro es escribir **«serie EN 1186»** y, si se necesita precisión, decir que la Tabla 1 indica EN 1186-3.
2. **No presentar el fallo de migración sin la matización de los autores.** Omitirla exagera la magnitud del problema abierto. La frase, literal:
   > «Nevertheless, the result is comparable with the limit, which means that only small improvements in terms of the efficacy of the application will be needed to reach the overall compliance.»
3. **Contexto que juega en contra de leer esto como «la barrera compostable contamina».** El PLA sin recubrir cumplía (3,2), el PO sin recubrir fallaba en dos simulantes (12 y 15), y el PO con bioORMOCER® dio <0,1. **El recubrimiento mejora la migración en la mayoría de las condiciones.** El fallo es específico de PLA + ácido + 60 °C.

## Relevancia / brecha para el estado del arte
Esta es **la pieza científica más sólida** para sostener que «recubrimiento barrera compostable aplicado en el convertido» es investigación y no compra de catálogo: lo hizo un instituto Fraunhofer, con proyecto europeo detrás, y el resultado publicado todavía deja abiertos el vapor de agua y una condición de migración.

Y es también la que fija el orden de magnitud del desafío: **25 cm³·m⁻²·d⁻¹·bar⁻¹ está uno a dos órdenes por encima de lo que un café exige** (las referencias de vida útil de café manejan OTR bajo 1). La brecha entre lo publicado como barrera compostable y lo que el producto necesita es el espacio de incertidumbre.

Tres frentes que el artículo deja explícitamente abiertos y que un proyecto puede reivindicar como propios: el desempeño de la barrera **a alta humedad relativa**, el **WVTR** (no medido), y la barrera medida **sobre sustrato compostable** en vez de sobre poliolefina.

> Relacionadas: [[patente-wo2025155500a1-sun-chemical-tinta-blanca-barrera-oxigeno]] (la versión reivindicada como tinta) · [[patente-es2981119t3-hubergroup-barrera-gas-impresa]] (la misma idea, ya patentada por vía de impresión) · [[norma-din-certco-esquema-certificacion-compostables]] (el certificador exige el ensayo sobre el artículo completo, no sobre el recubrimiento) · [[review-2026-asimetria-barrera-oxigeno-agua-recubrimientos-biodegradables]].
