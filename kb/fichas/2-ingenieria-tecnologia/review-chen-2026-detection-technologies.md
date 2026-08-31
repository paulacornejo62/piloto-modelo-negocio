---
id: review-chen-2026-detection-technologies
titulo: "Advanced Technologies for Characterizing and Detecting Battery Thermal Failure: A Review (Chen et al. 2026)"
tipo: revision
tema: Revisión de tecnologías de sensado para detección temprana de fallo térmico de baterías (multimodal)
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [deteccion-temprana-fuga-termica, bms-monitoreo, seguridad-bateria-litio]
anio: 2026
autores: [Yongxiu Chen, Zeyu Sun, Wei Zong, Yuhang Dai, Kai Ling Ng, Paul R Shearing]
referencia: https://doi.org/10.1002/advs.202600050
motor: Europe PMC / PMC (PMC13271617)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: "-"
metricas_clave: ["Etapa I 50–70°C (inicio SEI)", "Etapa II ~200°C (contracción separador)", "EIS ~31.62 Hz como alerta temprana (la fuente no cuantifica horas)"]
nota_qa: "QA EVAL_P2: la fuente NO afirma que el EIS detecte 'horas antes'; solo lo describe como indicador temprano. Resto (cita verbatim, etapas 50-70/~200°C) confirmado."
fecha_registro: 2026-07-14
proyectos:
  - lipigas
---

## Pregunta / objetivo de investigación
Revisar el estado del arte de tecnologías de caracterización y detección de fallo térmico de baterías y su integración multimodal a nivel de celda para pasar de diagnóstico reactivo a proactivo.

## Hipótesis
La fusión de señales físicas, químicas, térmicas y electroquímicas a nivel de celda detecta precursores mucho antes que la temperatura externa.

## Metodología
- **Diseño:** revisión de modalidades de sensado: sensores de gas (fibra óptica, VOCs, CO2/HF, H2), fibra óptica de temperatura/presión (Bragg, Fabry-Perot), imagen acústica/ultrasónica, espectroscopía de impedancia (EIS), sensores mecánicos (hinchamiento, piezorresistivos).

## Resultados principales
- Etapas antes del fallo catastrófico: Etapa I 50–70 °C (ruptura térmica de SEI, autocalentamiento); Etapa II ~200 °C (contracción del separador, calentamiento Joule); Etapas III–V (reacciones exotérmicas, venteo, fuego/explosión).
- "gas evolution and electrode delamination occur well before observable external temperature spikes or detectable electrical short-circuiting" — los gases y la delaminación preceden a la temperatura.
- Cambios de fase EIS a ~31.62 Hz dan detección horas antes de la escalada térmica.
- "early detection... through physical (stress, swelling, cracks), chemical (gas emission), thermal, and electrochemical (voltage, resistance) signals has been used for real-time, non-invasive identification of thermal failure precursors".

## Conclusiones
Las redes coordinadas óptica-acústica-electroquímica ofrecen el mayor potencial de detección temprana; la vía a bordo más madura es el seguimiento de impedancia.

## Limitaciones
Durabilidad de sensores bajo ciclado térmico no caracterizada; desacoplamiento de señales (temperatura vs. estrés) aún problemático; barreras de estandarización y costo limitan el despliegue en campo; imagen por rayos X solo para validación de diseño.

## Relevancia / brecha para el estado del arte
Cataloga las tecnologías concretas de "sensores inteligentes y monitoreo celda a celda" que Lipigas necesita ponderar. Señala que gases preceden a temperatura (relevante junto a carga inflamable) y que el despliegue a bordo tiene brechas de costo/durabilidad: oportunidad de I+D del piloto.

> Relaciones con otras fichas → `../../indice.json`.
