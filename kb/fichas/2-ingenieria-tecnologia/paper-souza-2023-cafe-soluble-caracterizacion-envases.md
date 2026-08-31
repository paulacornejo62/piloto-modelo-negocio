---
id: paper-souza-2023-cafe-soluble-caracterizacion-envases
titulo: "Instant coffee: Products and packaging systems characteristics (Souza, Moreira & Alves — Coffee Science 18:e182150, 2023)"
tipo: paper
tema: Caracterización de cafés solubles y de sus sistemas de envase; entrega la línea base medida del laminado con aluminio y la frase que reencuadra el KPI del oxígeno hacia la humedad — literal pero frágil
area_oecd: "2 Ingeniería y Tecnología (2.11 Otras ingenierías y tecnologías)"
topicos: [vida-util-cafe-soluble, barrera-oxigeno-otr, barrera-vapor-agua-wvtr, envase-flexible-compostable, stick-pack-monodosis]
anio: 2023
autores: [Raquel Massulo Souza, Christiane Quartaroli Moreira, Rosa Maria Vercelino Alves]
referencia: "Coffee Science 18:e182150, 2023 — DOI 10.25186/.v18i.2150 — PDF: https://coffeescience.ufla.br/index.php/Coffeescience/article/download/2150/2438 (CETEA / Instituto de Tecnologia de Alimentos, Campinas)"
motor: Coffee Science (revista open access, PDF completo)
profundidad_lectura: full-text
estado_evidencia: parcial
trl_relevante: "-"
metricas_clave: ["PET 13 µm/Al 12 µm/LDPE 55 µm: OTR <0,005 mL·m⁻²·d⁻¹ (OXTRAN 2/60, 23 °C, ASTM F1307)", "mismo laminado: WVTR <0,01 g·m⁻²·d⁻¹ a 38 °C/90 % HR (PERMATRAN W 3/33)", "umbral de daño ~7 % de humedad de equilibrio", "humedad inicial 2,1–3,0 % b.s. liofilizado / 2,3–4,0 % b.s. spray"]
fecha_registro: 2026-08-07
proyectos:
  - edelpa-compostables
---

## Pregunta / objetivo de investigación
Caracterizar los cafés instantáneos comerciales (liofilizado, spray aglomerado, spray polvo) y los sistemas de envase con que se comercializan, y relacionar las propiedades de barrera del envase con la estabilidad del producto vía isotermas de sorción de humedad.

## Hipótesis
No hay hipótesis experimental declarada: es un trabajo de caracterización. El supuesto de partida es que la estabilidad del café soluble está gobernada por la ganancia de humedad y que las isotermas de sorción permiten predecir vida útil sin ensayo de almacenamiento.

## Metodología
- **Diseño:** caracterización de producto y envase, más modelación de isotermas de sorción. **No hubo ensayo de almacenamiento con oxígeno controlado** — este punto es central para leer bien el trabajo.
- **Muestra:** cafés instantáneos comerciales y sus sistemas de envase, flexibles y rígidos (vidrio, hojalata), identificados por letra en las tablas.
- **Barrera al oxígeno:** OXTRAN 2/60 (Ametek/MOCON) a 23 °C y 0,21 atm de presión parcial de O₂, según ASTM F1307.
- **Barrera al vapor de agua:** PERMATRAN W 3/33, a 38 °C y 90 % HR.
- Las mediciones se hicieron sobre **envase terminado con sus sellos**, no sobre film plano.

## Resultados principales
**La línea base del aluminio, medida y publicada.** El sistema flexible «C» —*«Flexible packaging - stand up pouch - 50 g / PET 13 µm/Al foil 12 µm/LDPE 55 µm»*— dio:
- OTR **<0,005** mL(STP)·m⁻²·día⁻¹
- WVTR **<0,01** g de agua·m⁻²·día⁻¹ a 38 °C/90 % HR

Ambos con la nota al pie *«(***) quantification limit of the method / equipment»*. Es la estructura equivalente a la que hoy usa un convertidor de stick pack de café (poliéster + aluminio + polietileno), y es el número contra el que se mide cualquier alternativa sin aluminio.

**El umbral de daño está en la humedad, no en el oxígeno.** Los cafés mostraron el primer cambio de color a partir de ~**7 %** de humedad de equilibrio (*green point*), y pérdida franca de calidad —aglomeración, problemas de disolución— entre **10 % y 12 %** (base seca), en el rango de actividad de agua 0,4–0,5. La humedad inicial de producto es 2,1–3,0 % b.s. (liofilizado) y 2,3–4,0 % b.s. (spray).

**La frase del reencuadre**, literal:
> «Rigid packaging systems showed values of OTR > 1.000 mL (STP).m-2.day-1 indicating that O2 inside packaging is not a critical parameter for instant coffee products if the moisture of the product does not increase.»

## Conclusiones
Los autores concluyen que el envase de café soluble debe diseñarse en torno a la protección frente a la ganancia de humedad, y que las isotermas de sorción permiten estimar vida útil.

## Limitaciones — ADVERTENCIA DEL QA ADVERSARIAL (obligatoria)
**La cita del reencuadre es literal y exacta, pero su peso probatorio es muy inferior al que un informe apurado le asigna.** Tres razones, cualquiera de ellas utilizable por un evaluador en contra:

1. **La premisa está contradicha por la Tabla 3 del propio artículo.** La mayoría de los sistemas rígidos midió OTR <0,005; solo la muestra F-2 dio «>1.000» (A dio 0,384 y F-1 dio 0,780). La generalización *«rigid packaging systems showed»* descansa en **una sola muestra**.
2. **El «1.000» es tipográficamente ambiguo.** En la misma tabla el punto se usa como separador **decimal** (0.384, 0.780, <0.005). «>1.000» podría leerse como «>1,0» y no como «>1.000».
3. **No hubo ningún ensayo de almacenamiento con oxígeno controlado.** La frase es una **inferencia de los autores**, no un resultado experimental.

**Corrección obligatoria de rótulo:** decir «los autores infieren», nunca «concluyen textualmente» ni «evidencia arbitrada». Es una **hipótesis a validar, no un hecho establecido**. El soporte limpio del mismo reencuadre está en [[paper-souza-2023-envases-flexibles-alternativos-cafe-soluble]] (Food Research International, mismo grupo, con ensayo real de 365 días); esta ficha debe usarse como respaldo **secundario**.

**Dos matices que deben acompañar a la línea base del aluminio:**
- Los dos valores son **límites de cuantificación** (no detectados), no mediciones. El laminado con aluminio puede ser mejor, o simplemente estar bajo la resolución del equipo. **La brecha que se calcule contra él es un piso.** Escribir siempre «<0,01», nunca «0,01».
- La medición es sobre **envase terminado con sellos**, no sobre film plano. Eso favorece a la comparación (un envase sellado suele medir peor que su film), pero no es la misma base que una ficha técnica de film.

## Relevancia / brecha para el estado del arte
Dos aportes distintos y de calidad muy distinta.

El primero, **sólido**: la línea base cuantificada del aluminio. Permite que un proyecto declare la brecha en números en vez de afirmarla retóricamente, con la salvedad de que es un piso.

El segundo, **frágil pero estratégico**: el reencuadre del KPI. Si el cuello de botella real del café soluble es la ganancia de humedad y no el oxígeno, entonces un proyecto que se plantee «recuperar la barrera al oxígeno sin aluminio» está apuntando a la variable **resuelta comercialmente**, y el frente abierto —barrera al vapor de agua a 38 °C/90 % HR— queda sin trabajar. Ese giro cambia el objetivo del proyecto, y por eso mismo no puede apoyarse en una sola frase inferida: hay que llevarlo a la reunión técnica como pregunta y validarlo con el cliente y con el estudio de 365 días.

> Relacionadas: [[paper-souza-2023-envases-flexibles-alternativos-cafe-soluble]] (mismo grupo, soporte experimental del reencuadre) · [[review-2026-asimetria-barrera-oxigeno-agua-recubrimientos-biodegradables]] (por qué el agua es el frente difícil sobre sustrato celulósico) · [[patente-es3061314t3-nestle-papel-metalizado-alta-barrera]].
