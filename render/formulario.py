#!/usr/bin/env python3
"""Genera el documento de las secciones de modelo de negocio del fondo elegido.

Parte determinista (render): toma el estado tipado y arma el documento entregable
con las secciones de modelo de negocio / mercado / escalamiento que redactó el
piloto (narrativa, formulario_oficial en alcance, modelo, plan de escalamiento,
impacto y continuidad). El equipo GT integra este borrador al formulario completo
del fondo y completa las secciones técnicas / de equipo antes de presentar.
Salida en Markdown; si está pandoc, también .docx.

Uso:
    python3 render/formulario.py <tenant>          # genera formulario-modelo-negocio.md (+ .docx si hay pandoc)
    python3 render/formulario.py <tenant> --md     # solo Markdown
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):  # consola Windows (cp1252) no soporta emojis/guiones
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

SISTEMA = Path(__file__).resolve().parent.parent
FORMULARIOS_PATH = SISTEMA / "motor-reglas" / "formularios.json"


def _g(d: dict, *path, default=""):
    for k in path:
        d = (d or {}).get(k, {})
    return d or default


def _fmt_clp(v) -> str:
    try:
        return f"${float(v):,.0f}"
    except (TypeError, ValueError):
        return "—"


def _fondo_nombre(fondo: str) -> str:
    try:
        spec = json.loads(FORMULARIOS_PATH.read_text(encoding="utf-8"))["fondos"]
        if fondo in spec:
            return spec[fondo]["nombre"]
        for v in spec.values():
            if v.get("nombre", "").split(" (")[0] == (fondo or "").strip():
                return v["nombre"]
    except Exception:
        pass
    return fondo or "(fondo por definir)"


def construir(datos: dict) -> str:
    pc = datos.get("perfil_comercial", {}) or {}
    nv = datos.get("narrativa", {}) or {}
    fo = datos.get("formulario_oficial", {}) or {}
    mn = datos.get("modelo_negocio", {}) or {}
    pe = datos.get("plan_escalamiento", {}) or {}
    ic = datos.get("impacto_continuidad", {}) or {}
    fondo = fo.get("fondo") or (datos.get("meta") or {}).get("instrumento_objetivo", "")
    out: list[str] = []

    out += [f"# Modelo de negocio — {_fondo_nombre(fondo)}",
            f"## {nv.get('titulo_proyecto', '(sin título)')}", "",
            f"**Cliente:** {pc.get('cliente_razon_social', '')} ({pc.get('cliente_tamano', '')})  ",
            f"**Contacto:** {_g(pc, 'contacto_clave', 'nombre')} — {_g(pc, 'contacto_clave', 'email')}", ""]

    # 1. Narrativa
    out += ["## 1. Narrativa (problema · mercado · propuesta de valor)", "",
            f"**Resumen.** {nv.get('resumen', '')}", "",
            f"**Problema / oportunidad.** {nv.get('problema_oportunidad', '')}", "",
            f"**Mercado objetivo.** {nv.get('mercado_objetivo', '')}", "",
            f"**Propuesta de valor.** {nv.get('propuesta_valor', '')}", "",
            f"**Diferenciación.** {nv.get('diferenciacion', '')}", ""]

    # 2. Secciones del formulario oficial (en alcance del piloto)
    out += [f"## 2. Secciones del formulario — {_fondo_nombre(fondo)}", ""]
    secciones = [s for s in fo.get("secciones", []) or [] if s.get("en_alcance_piloto") is not False]
    if secciones:
        for s in secciones:
            aviso = "" if s.get("cumple_requisitos") else "  _(requisitos por confirmar)_"
            out += [f"### {s.get('titulo', s.get('id', ''))}{aviso}", "", s.get("respuesta", ""), ""]
    else:
        out += ["_Secciones del formulario aún no redactadas (FORM_W2)._", ""]
    fuera = [s.get("titulo", s.get("id", "")) for s in fo.get("secciones", []) or []
             if s.get("en_alcance_piloto") is False]
    if fuera:
        out += ["> _Secciones que completa el equipo GT (fuera del piloto): "
                + "; ".join(fuera) + "._", ""]

    # 3. Modelo de negocio (Canvas + unit economics)
    canvas = mn.get("canvas", {}) or {}
    ue = mn.get("unit_economics", {}) or {}
    if canvas or ue:
        out += ["## 3. Modelo de negocio", ""]
        if canvas:
            for k, lbl in [("segmentos_cliente", "Segmentos de cliente"),
                           ("propuesta_valor", "Propuesta de valor"), ("canales", "Canales"),
                           ("relacion_clientes", "Relación con clientes"),
                           ("fuentes_ingreso", "Fuentes de ingreso"), ("recursos_clave", "Recursos clave"),
                           ("actividades_clave", "Actividades clave"), ("socios_clave", "Socios clave"),
                           ("estructura_costos", "Estructura de costos")]:
                if canvas.get(k):
                    out.append(f"- **{lbl}:** {canvas[k]}")
            out.append("")
        if ue:
            out += ["**Unit economics.** "
                    f"Margen de contribución {_fmt_clp(ue.get('margen_contribucion_unitario'))} "
                    f"({(str(round(ue['margen_contribucion_pct'] * 100)) + '%') if ue.get('margen_contribucion_pct') is not None else '—'}) · "
                    f"LTV {_fmt_clp(ue.get('ltv_clp'))} · LTV/CAC {ue.get('ltv_cac_ratio', '—')} · "
                    f"payback CAC {ue.get('payback_cac_meses', '—')} meses · "
                    f"punto de equilibrio {ue.get('punto_equilibrio_unidades', '—')} unidades "
                    f"({_fmt_clp(ue.get('punto_equilibrio_clp'))}).", ""]
        base = next((e for e in (mn.get("proyeccion", {}) or {}).get("escenarios", []) or []
                     if e.get("nombre") == "base"), None)
        if base and base.get("anios"):
            ult = base["anios"][-1]
            out += [f"**Proyección (escenario base, año {ult.get('anio', '?')}).** "
                    f"Ingresos {_fmt_clp(ult.get('ingresos_clp'))} · resultado "
                    f"{_fmt_clp(ult.get('resultado_clp'))}.", ""]

    # 4. Plan de escalamiento
    if pe:
        out += ["## 4. Plan de escalamiento", "",
                f"**Estado actual.** {pe.get('estado_actual', '')}", "",
                f"**Estrategia de escalamiento.** {pe.get('estrategia_escalamiento', '')}", "",
                f"**Metas de tracción.** {pe.get('metas_traccion', '')}", ""]
        if pe.get("hitos_comerciales"):
            out += ["**Hitos comerciales.**", ""]
            for h in pe["hitos_comerciales"]:
                out.append(f"- {h.get('n', '')} {h.get('nombre', '')} — meta: {h.get('meta', '')} "
                           f"({h.get('fecha_objetivo', '')})")
            out.append("")

    # 5. Impacto y continuidad
    if ic:
        ie = ic.get("impacto_esperado", {}) or {}
        out += ["## 5. Impacto y continuidad", "",
                f"**Impacto económico.** {ie.get('economico', '')}", "",
                f"**Impacto social.** {ie.get('social', '')}  ",
                f"**Impacto ambiental.** {ie.get('ambiental', '')}", "",
                f"**Estrategia de continuidad.** {ic.get('estrategia_continuidad', '')}", ""]
        if ic.get("supuestos_a_confirmar"):
            out += ["**Supuestos a confirmar antes de presentar.**", ""]
            for s in ic["supuestos_a_confirmar"]:
                out.append(f"- {s.get('supuesto', '')} (afecta: {s.get('seccion_afectada', '—')}; "
                           f"responsable: {s.get('responsable_confirmar', '—')})")
            out.append("")

    out += ["---", "*Documento generado desde el expediente del piloto de modelo de negocio. "
            "Borrador de apoyo: el equipo GT lo integra al formulario completo del fondo y "
            "completa las secciones técnicas / de equipo antes de presentar.*"]
    return "\n".join(out) + "\n"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Uso: python3 render/formulario.py <tenant> [--md]")
    tenant = sys.argv[1]
    ruta = SISTEMA / "proyectos" / tenant / "expediente.json"
    if not ruta.exists():
        sys.exit(f"ERROR: no existe {ruta}")
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    md_path = ruta.parent / "formulario-modelo-negocio.md"
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
