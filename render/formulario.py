#!/usr/bin/env python3
"""Genera el documento del formulario del FONDO ELEGIDO desde el expediente (fund-aware).

Parte determinista (render): toma el estado tipado y arma el documento entregable.
La capa oficial son las respuestas de `formulario_oficial` (según el fondo, ver
motor-reglas/formularios.json); se agregan a los antecedentes del proceso (empresa,
título, objetivo, capacidades, admin). Salida en Markdown; si está pandoc, también .docx.

Uso:
    python3 render/formulario.py <tenant>            # genera formulario-<fondo>.md (+ .docx si hay pandoc)
    python3 render/formulario.py <tenant> --md       # solo Markdown
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

SISTEMA = Path(__file__).resolve().parent.parent
FORMULARIOS_PATH = SISTEMA / "motor-reglas" / "formularios.json"


def _g(d: dict, *path, default=""):
    for k in path:
        d = (d or {}).get(k, {})
    return d or default


def _fondo_nombre(fondo: str) -> str:
    try:
        return json.loads(FORMULARIOS_PATH.read_text(encoding="utf-8"))["fondos"][fondo]["nombre"]
    except Exception:
        return fondo or "(fondo por definir)"


def construir(datos: dict) -> str:
    p1, p4 = datos.get("eval_p1", {}), datos.get("eval_p4", {})
    w1, w3, w4 = datos.get("form_w1", {}), datos.get("form_w3", {}), datos.get("form_w4", {})
    fo = datos.get("formulario_oficial", {}) or {}
    fondo = fo.get("fondo") or (datos.get("meta") or {}).get("instrumento_objetivo", "")
    out: list[str] = []

    out += [f"# Formulario {_fondo_nombre(fondo)} — {w1.get('titulo_proyecto', '(sin título)')}", "",
            f"**Empresa:** {p1.get('empresa_razon_social', '')} ({p1.get('empresa_tamano', '')})  ",
            f"**Contacto:** {_g(p1, 'contacto_clave', 'nombre')} — {_g(p1, 'contacto_clave', 'email')}", ""]

    out += ["## 1. Información general", "",
            f"**Título.** {w1.get('titulo_proyecto', '')}", "",
            f"**Resumen.** {w1.get('resumen_proyecto', '')}", "",
            f"**Objetivo general.** {w1.get('objetivo_general_proyecto', '')}", ""]

    # Capa oficial: las respuestas al formulario del fondo (fund-aware).
    out += [f"## 2. Formulario oficial — {_fondo_nombre(fondo)}", ""]
    if fo.get("secciones"):
        for s in fo["secciones"]:
            aviso = "" if s.get("cumple_requisitos") else "  _(requisitos por confirmar)_"
            out += [f"### {s.get('titulo', s.get('id', ''))}{aviso}", "", s.get("respuesta", ""), ""]
    else:
        # Fallback (expedientes previos a fund-aware): usa los campos form_w2 legacy.
        w2 = datos.get("form_w2", {})
        out += ["_Formulario oficial no poblado; se muestran los campos de redacción I+D disponibles._", "",
                f"**Estado del arte.** {w2.get('estado_del_arte_investigacion', '')}", "",
                f"**Nuevos conocimientos.** {w2.get('nuevos_conocimientos_generados', '')}", "",
                f"**Desarrollo tangible.** {w2.get('descripcion_desarrollo_tangible', '')}", "",
                f"**Atributos de superioridad.** {w2.get('atributos_tecnicos_superioridad', '')}", "",
                f"**Incertidumbre.** {w2.get('incertidumbre_cientifico_tecnologica', '')}", ""]

    fr = p4.get("frascati", {})
    out += ["## 3. Justificación I+D (Manual de Frascati)", "",
            f"Cuadrante **{fr.get('cuadrante', '?')}** (es_id: {fr.get('es_id', '?')}). {fr.get('justificacion', '')}", ""]

    pa = w3.get("profesional_acreditador", {})
    out += ["## 4. Capacidades", "",
            f"**Profesional que acredita capacidades.** {pa.get('nombre', '')} — "
            f"contrato vigente: {pa.get('tiene_contrato_vigente', '?')}, experiencia I+D 36m: {pa.get('experiencia_id_36m', '?')}", ""]
    if w3.get("personal_asociado"):
        out.append("**Personal asociado.**")
        for m in w3["personal_asociado"]:
            out.append(f"- {m.get('nombre', '')} — {m.get('funcion', '')} ({m.get('horas', '?')} h)")
        out.append("")
    if w3.get("subcontratos_habilitados"):
        out += ["**Subcontratos.** " + ", ".join(w3["subcontratos_habilitados"]), ""]

    enc = w4.get("registro_encuesta_ley_id", {})
    out += ["## 5. Antecedentes administrativos y encuesta", "",
            f"**Sistema contable.** {w4.get('nombre_sistema_contable', '')}",
            f"**Fase del proyecto.** {enc.get('fase_proyecto_actual', '')}",
            f"**Tipo / alcance de innovación.** {enc.get('tipo_innovacion_principal', '')} / {enc.get('alcance_innovacion', '')}",
            f"**Modelo de negocio.** {enc.get('modelo_negocio_ingresos', '')}",
            f"**Arancel estimado (Ley I+D).** {w4.get('arancel_clp', '—')} CLP", ""]

    out += ["---", "*Documento generado desde el expediente del sistema GTF. "
            "Borrador de apoyo: revisar contra la plataforma oficial del fondo antes de enviar.*"]
    return "\n".join(out) + "\n"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Uso: python3 render/formulario.py <tenant> [--md]")
    tenant = sys.argv[1]
    ruta = SISTEMA / "proyectos" / tenant / "expediente.json"
    if not ruta.exists():
        sys.exit(f"ERROR: no existe {ruta}")
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    fondo = (datos.get("formulario_oficial", {}) or {}).get("fondo") or \
        (datos.get("meta") or {}).get("instrumento_objetivo", "fondo")
    md_path = ruta.parent / f"formulario-{fondo}.md"
    md_path.write_text(construir(datos), encoding="utf-8")
    print(f"Generado: {md_path}")
    if "--md" not in sys.argv and shutil.which("pandoc"):
        docx = md_path.with_suffix(".docx")
        try:
            subprocess.run(["pandoc", str(md_path), "-o", str(docx)], check=True)
            print(f"Generado: {docx}")
        except subprocess.CalledProcessError as e:
            print(f"AVISO: pandoc falló ({e}); queda solo el .md", file=sys.stderr)
    elif "--md" not in sys.argv:
        print("AVISO: pandoc no instalado; queda solo el .md (instalar pandoc para .docx).")


if __name__ == "__main__":
    main()
