# Plantillas y render de documentos finales

Lo que el consultor **entrega**: del estado tipado del expediente a los documentos oficiales.

## Disponible
- **Formulario Ley I+D** → `render/formulario.py <tenant>`: arma el formulario en la estructura oficial (Información Técnica, Componente I+D rutas A/B, Frascati, Capacidades, Antecedentes/encuesta) desde los bloques `form_*` + `eval_p4`. Salida: `proyectos/<tenant>/formulario-ley-id.md` y, si hay **pandoc**, también `.docx`. _Es un borrador de apoyo: revisar contra la plataforma oficial antes de enviar._

- **Plan de Trabajo (Carta Gantt + Presupuesto)** → `render/gantt.py <tenant>`: genera `proyectos/<tenant>/plan-trabajo.xlsx` con la **estructura del formato oficial CORFO** (hojas Desafíos / Gantt I+D / Presupuesto RRHH), pre-poblado desde `form_w3` (`actividades` → Gantt con columnas-mes; `personal_asociado` con `cuenta`/`valor_hh`/`horas` → presupuesto con totales). Requiere openpyxl (del `.venv` del setup).

## Alcance y límite honesto
El `.xlsx` que generamos es un **insumo de arranque estructurado como el oficial**, NO la planilla macro oficial de CORFO (`...Formulario_de_Desafios_Carta_Gantt_y_Presupuesto....xlsm`, con macros, tablas dinámicas, hojas Inversión/Subcontratos/Memorias de Cálculo). El consultor **traspasa/valida** el contenido al archivo oficial. Referencia del formato: `desarrollo/contexto/fuentes/Ley I+D/Proyectos postulados/Aceptados/` (proyecto SRS).

> Los documentos generados (`.docx`, `.xlsx`) quedan gitignoreados (regenerables); se versiona el `.md`.
