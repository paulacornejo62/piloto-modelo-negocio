---
id: paper-gu-2025-early-warning-sos
titulo: "Early warning of thermal runaway based on state of safety for lithium-ion batteries (Gu et al. 2025)"
tipo: paper
tema: Alerta temprana de fuga térmica mediante un índice State of Safety (SOS) multivariable
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [deteccion-temprana-fuga-termica, bms-monitoreo, fuga-termica-bateria]
anio: 2025
autores: [Xin Gu, Yunlong Shang, Jinglun Li, Yuhao Zhu, Xuewen Tao, Hao Geng, Zhen Zhang, Chenghui Zhang]
referencia: https://doi.org/10.1038/s44172-025-00442-1
motor: Europe PMC / PMC (PMC12152129)
profundidad_lectura: full-text
estado_evidencia: verificado
trl_relevante: 4
metricas_clave: ["indice SOS compuesto: alerta hasta 5 h antes", "voltaje 1.47 h / temperatura 0.57 h / acustico 0.3 h (Tabla 5)", "strain ~906 s (~15 min) antes que temperatura"]
nota_qa: "QA EVAL_P2: el '5 h' es del METODO SOS compuesto, no del strain aislado (strain ~906 s antes que temperatura). Metricas corregidas. Fuente abierta, cita verbatim OK."
fecha_registro: 2026-07-14
proyectos:
  - lipigas
---

## Pregunta / objetivo de investigación
Proponer un indicador cuantitativo de seguridad (State of Safety, 0–100%) que integre múltiples señales para anticipar la fuga térmica con más margen que los métodos monoseñal.

## Hipótesis
La deformación mecánica (strain) de la celda es un precursor más temprano que temperatura o voltaje; un SOS que la incorpore da mayor tiempo de alerta.

## Metodología
- **Diseño:** experimental, tres condiciones de abuso (sobrecalentamiento, sobrecarga, sobrevelocidad de carga).
- **Datos:** señales de celda individual: aumento de temperatura, voltaje mediano, capacidad, potencia y deformación.
- **Técnicas:** cuantificación del SOS a partir de parámetros multidimensionales; integrable a BMS.
- **Métricas:** tiempo de anticipación de la alerta previo al TR.

## Resultados principales
- Anticipación de hasta 5 h con el método SOS basado en strain.
- Comparativa: voltaje 1.47 h; temperatura 0.57 h; acústico 0.3 h — el strain dispara antes ("the strain trigger time for thermal runaway is earlier than the temperature").
- "multidimensional parameters such as temperature rise, median voltage, capacity, power, and strain are used to quantify the SOS".

## Conclusiones
El SOS facilita integración en BMS, entrega información de seguridad consolidada y permite optimizar estrategias de carga/descarga y vida útil.

## Limitaciones
Requiere sensores de deformación embebidos (mayor costo); validado solo en tres modos de abuso a escala de celda.

## Relevancia / brecha para el estado del arte
Aporta evidencia directa al "monitoreo celda a celda" y "sensores inteligentes" que Lipigas quiere para mitigar el riesgo junto a carga de GLP: cuantifica cuánto margen de alerta da cada señal. Un margen de horas cambia radicalmente la respuesta operativa vs. los segundos de otros enfoques.

> Relaciones con otras fichas → `../../indice.json`.
