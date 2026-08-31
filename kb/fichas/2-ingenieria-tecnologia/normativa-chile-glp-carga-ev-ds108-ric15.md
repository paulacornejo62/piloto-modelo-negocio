---
id: normativa-chile-glp-carga-ev-ds108-ric15
titulo: Chile — carga de vehículos eléctricos en instalaciones de GLP: DS 108/2014 + RIC N°15 (SEC)
tipo: normativa
tema: Marco regulatorio chileno para recarga de VE junto a almacenamiento de GLP (zonas clasificadas/atmósferas explosivas)
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [normativa-carga-ev-atmosfera-explosiva, transporte-glp, carga-nocturna, electromovilidad-carga-peligrosa]
anio: 2014
autores: [Ministerio de Energía (DS 108/2014), Superintendencia de Electricidad y Combustibles (RIC N°15)]
referencia: https://www.sec.cl/transparencia/docs2014/decreto_108_2014.pdf ; https://www.sec.cl/sitio-web/wp-content/uploads/2021/01/RIC-N15-Infra-para-la-recarga-de-vehiculos-electricos.pdf
motor: WebFetch/PDF full-text (SEC/BCN)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: ["DS 108 Art 5, 52-54, 136, 137-138", "RIC N°15 §5.9, §14.8, §14.9", "NFPA 58-2004 (adoptada por DS 108)", "clasificación típica Clase I Div 2 Grupo D"]
fecha_registro: 2026-07-14
proyectos:
  - lipigas
---

## Qué regula
Dos cuerpos normativos chilenos se intersectan para gobernar la **carga nocturna de VE dentro/junto a una planta con almacenamiento de GLP**:
1. **DS 108/2014 (Min. Energía)** — Reglamento de seguridad para instalaciones de almacenamiento, transporte y distribución de GLP.
2. **RIC N°15 (SEC)** — Pliego técnico de infraestructura para la recarga de vehículos eléctricos (fuente legal DFL 4/20.018; reglamento DS 8/2019).

## Disposiciones clave (articulado verificado)
**DS 108/2014:**
- **Art 5**: en materia eléctrica las instalaciones de GLP deben cumplir las normas eléctricas vigentes que correspondan → **puente al RIC N°15**.
- **Art 52**: control de fuentes de ignición según **NFPA 58-2004**.
- **Art 53**: distingue áreas clasificadas vs. no clasificadas (per NFPA 58).
- **Art 54**: terreno de tanques libre de combustibles en un radio de 3 m.
- **Art 136**: los cilindros estibados en camiones estacionados dentro de un almacenamiento **se consideran parte de la instalación de GLP** (implica que un VE cargando en planta entra en el inventario/riesgo regulado).
- **Art 137-138**: evaluación de riesgos **obligatoria** para almacenamientos ≥6.000 kg, con **árbol de eventos** de escape/inflamación, **actualizable ante cambios de entorno** (una electrolinera es un cambio de entorno).

**RIC N°15:**
- **§14.9 (decisivo)**: «Cuando sean instalados SAVE en áreas con atmósferas potencialmente explosivas, se deberán aplicar las disposiciones del pliego normativo correspondiente» → cargar VE junto a zona clasificada de GLP obliga a cumplir normativa de atmósferas explosivas (clasificación Ex, equipos con grado de protección).
- **§5.9**: considerar las influencias externas del emplazamiento.
- **§14.8**: proteger el SAVE frente a impacto mecánico (AG3).
- Versión 2024: prohíbe modos de carga 1 y 2 en instalaciones públicas (privilegia modos 3 y 4).

## Implicancia (qué habilita / qué bloquea)
El marco **NO prohíbe** cargar VE en una planta de GLP, pero **condiciona**: el punto de carga (SAVE) debe emplazarse **fuera de la zona clasificada** o, si está dentro, con **equipos con protección Ex certificada**; y debe **actualizarse la evaluación de riesgos** (DS 108 Art 137-138). Este es el núcleo del diseño de ingeniería/normativo del piloto de Lipigas y el frente de novedad sin precedente documentado en Chile.

## Limitaciones
Ambos textos leídos íntegros y verificados. Falta cruzar con **DS 298/1994** (transporte de cargas peligrosas, articulado no abierto) y con la norma chilena/estándar de clasificación de atmósferas explosivas específica que invoca el §14.9 (identificar el pliego correspondiente).

## Citas textuales
> DS 108 Art 52: «Las Instalaciones de GLP deberán cumplir con los requisitos del control de las fuentes de ignición establecidos en la NFPA 58 - 2004».
> RIC N°15 §14.9: «Cuando sea instalados SAVE en áreas con atmósferas potencialmente explosivas, se deberán aplicar las disposiciones del pliego normativo correspondiente».

> Relaciones (relacionada_con) → `../../indice.json` (normativa-adr-2025-ve-mercancias-peligrosas).
