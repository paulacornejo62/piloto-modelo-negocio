#!/usr/bin/env python3
"""Render y validación del expediente de un caso de modelo de negocio.

Parte determinista del sistema (no generativa): valida el expediente.json de un
tenant contra el schema y genera su versión legible expediente.md, con un Panel
del consultor arriba (resumen en lenguaje llano + glosario).

Uso:
    python3 render/render.py <tenant>              # genera proyectos/<tenant>/expediente.md
    python3 render/render.py <tenant> --validar    # solo valida contra el schema
    python3 render/render.py <tenant> --limites    # largo de campos vs. topes del formulario
    python3 render/render.py <tenant> --formulario # completitud de las secciones en alcance

La validación usa jsonschema si está instalado; si no, hace chequeos mínimos.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# La consola de Windows (cp1252) no soporta ✓/✅/⚠; forzar UTF-8 en la salida.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

SISTEMA = Path(__file__).resolve().parent.parent
SCHEMA_PATH = SISTEMA / "expediente.schema.json"
FORMULARIOS_PATH = SISTEMA / "motor-reglas" / "formularios.json"

# Nombres legibles de cada paso (código → etiqueta), reusados de tools/estado.py.
try:
    sys.path.insert(0, str(SISTEMA / "tools"))
    from estado import PASOS as _PASOS  # type: ignore
    NOMBRE_PASO = {code: label for code, label, _ in _PASOS}
    ORDEN_PASOS = [code for code, _, _ in _PASOS]
except Exception:
    NOMBRE_PASO = {}
    ORDEN_PASOS = []


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def _h2(code: str, fallback: str) -> str:
    return f"## {NOMBRE_PASO.get(code, fallback)} ({code})"


def _si_no_bool(v) -> str:
    return "sí" if v is True else ("no" if v is False else "?")


def _fmt_clp(v) -> str:
    try:
        return f"${float(v):,.0f}"
    except (TypeError, ValueError):
        return "—"


def _pct(v) -> str:
    try:
        return f"{float(v) * 100:.0f}%"
    except (TypeError, ValueError):
        return "—"


def _resumir(texto: str, n: int = 320) -> str:
    t = " ".join((texto or "").split())
    if len(t) <= n:
        return t
    corte = t[:n]
    fin = max(corte.rfind(". "), corte.rfind("; "))
    return (corte[:fin + 1] if fin > n // 2 else corte).rstrip() + " […]"


def cargar_expediente(tenant: str) -> tuple[Path, dict]:
    ruta = SISTEMA / "proyectos" / tenant / "expediente.json"
    if not ruta.exists():
        sys.exit(f"ERROR: no existe {ruta}")
    return ruta, json.loads(ruta.read_text(encoding="utf-8"))


def _motor():
    """Importa motor-reglas/reglas.py si se puede (para chequeos de coherencia)."""
    try:
        sys.path.insert(0, str(SISTEMA / "motor-reglas"))
        import reglas  # type: ignore
        return reglas
    except Exception:
        return None


def alertas_cifras(datos: dict) -> list[str]:
    """Corre el motor de coherencia sobre meta.cifras_declaradas. Alerta, no bloquea."""
    cifras = (datos.get("meta") or {}).get("cifras_declaradas") or []
    reglas = _motor()
    if not cifras or reglas is None:
        return []
    try:
        return [f"{r['concepto']}: {r['detalle']}"
                for r in reglas.coherencia_cifras_cliente(cifras) if r["estado"] == "alerta"]
    except Exception:
        return []


# --------------------------------------------------------------------------- #
# Validación
# --------------------------------------------------------------------------- #
def validar(datos: dict) -> list[str]:
    """Valida el expediente contra el schema. Devuelve lista de errores (vacía si OK)."""
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    try:
        import jsonschema  # type: ignore
        validador = jsonschema.Draft7Validator(schema)
        return [f"{'/'.join(map(str, e.path))}: {e.message}" for e in validador.iter_errors(datos)]
    except ImportError:
        # Fallback mínimo sin jsonschema: requeridos de los bloques presentes.
        errores: list[str] = []
        if "meta" not in datos:
            errores.append("meta: bloque requerido ausente")
        reqs = {
            "perfil_comercial": ["cliente_razon_social", "producto_o_servicio",
                                 "problema_u_oportunidad", "resultado_negocio_esperado"],
            "investigacion_mercado": ["sintesis_mercado", "hallazgos", "cobertura_busqueda"],
            "supuestos_modelo": ["segmentos", "propuesta_valor", "estructura_ingresos",
                                 "estructura_costos"],
            "modelo_negocio": ["canvas", "unit_economics", "proyeccion"],
            "revision_viabilidad": ["compuerta"],
        }
        for bloque, campos in reqs.items():
            if bloque in datos:
                for c in campos:
                    if c not in datos[bloque]:
                        errores.append(f"{bloque}/{c}: campo requerido ausente")
        return errores


def limites_caracteres(datos: dict) -> list[dict]:
    """Largo de cada campo de texto con maxLength en el schema vs. su tope."""
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    out = []
    for bloque, bloque_schema in (schema.get("properties") or {}).items():
        datos_bloque = datos.get(bloque)
        if not isinstance(datos_bloque, dict):
            continue
        for campo, campo_schema in (bloque_schema.get("properties") or {}).items():
            lim = campo_schema.get("maxLength")
            val = datos_bloque.get(campo)
            if lim is None or not isinstance(val, str):
                continue
            out.append({"campo": f"{bloque}.{campo}", "largo": len(val),
                        "limite": lim, "excede": len(val) > lim})
    return out


def formulario_completitud(datos: dict) -> list[dict]:
    """Completitud de las secciones EN ALCANCE DEL PILOTO del formulario del fondo.

    Lee motor-reglas/formularios.json, toma el fondo elegido y verifica que cada
    sección `en_alcance_piloto: true` esté presente, no vacía y dentro de su límite.
    Las secciones fuera de alcance se listan como 'fuera_alcance' (no bloquean).
    estado: ok | falta | vacia | excede | fuera_alcance | fondo_desconocido.
    """
    fo = datos.get("formulario_oficial") or {}
    fondo = fo.get("fondo") or (datos.get("meta") or {}).get("instrumento_objetivo")
    # meta.instrumento_objetivo usa el nombre ("Crea y Valida"); formularios.json usa la clave.
    spec = json.loads(FORMULARIOS_PATH.read_text(encoding="utf-8")).get("fondos", {})
    if fondo not in spec:
        nombre_a_clave = {v.get("nombre", "").split(" (")[0]: k for k, v in spec.items()}
        fondo = nombre_a_clave.get((fondo or "").strip(), fondo)
    if not fondo or fondo not in spec:
        return [{"seccion": "-", "titulo": f"fondo '{fondo}'", "estado": "fondo_desconocido"}]
    respuestas = {s.get("id"): s for s in fo.get("secciones", []) or []}
    out = []
    for sec in spec[fondo]["secciones"]:
        r = respuestas.get(sec["id"])
        if not sec.get("en_alcance_piloto"):
            estado = "fuera_alcance"
        elif r is None:
            estado = "falta"
        elif not (r.get("respuesta") or "").strip():
            estado = "vacia"
        elif sec.get("limite") and len(r["respuesta"]) > sec["limite"]:
            estado = "excede"
        else:
            estado = "ok"
        out.append({"seccion": sec["id"], "titulo": sec["titulo"], "estado": estado})
    return out


# --------------------------------------------------------------------------- #
# Panel del consultor
# --------------------------------------------------------------------------- #
def _fondo_legible(datos: dict) -> str:
    return ((datos.get("postulacion") or {}).get("fondo_nombre")
            or (datos.get("meta") or {}).get("instrumento_objetivo")
            or "por definir")


def _datos_por_confirmar(datos: dict) -> list[str]:
    pc = datos.get("perfil_comercial") or {}
    faltan = []
    if pc and pc.get("cliente_tamano_confirmado") is not True:
        faltan.append("tamaño de empresa (afecta el cofinanciamiento CORFO)")
    if pc and not pc.get("cliente_fecha_inicio_actividades"):
        faltan.append("antigüedad de la empresa (elegibilidad de algunos fondos)")
    pend = [s for s in ((datos.get("supuestos_modelo") or {}).get("supuestos") or [])
            if s.get("confirmado") is False]
    if pend:
        faltan.append(f"{len(pend)} supuesto(s) del modelo sin confirmar")
    n = json.dumps(datos, ensure_ascii=False).count("[POR CONFIRMAR]")
    if n:
        faltan.append(f"{n} dato(s) marcados «[POR CONFIRMAR]» en el detalle")
    return faltan


def _proxima_accion(datos: dict) -> str:
    actual = (datos.get("meta") or {}).get("paso_actual", "")
    if actual == "ENTREGADO":
        return "paquete de modelo de negocio entregado — fin del flujo"
    if actual == "FORM_W5":
        return "QA de coherencia y entrega del paquete al consultor"
    if actual in ORDEN_PASOS:
        i = ORDEN_PASOS.index(actual)
        if i + 1 < len(ORDEN_PASOS):
            sig = ORDEN_PASOS[i + 1]
            return f"{NOMBRE_PASO.get(sig, sig)} ({sig})"
    if actual in ("INICIO", ""):
        return f"{NOMBRE_PASO.get('EVAL_P1', 'Reunión #1')} (EVAL_P1)"
    return "—"


def _en_breve_mercado(im: dict) -> list[str]:
    """Síntesis del mercado para lectura rápida: narrativa del agente + resumen automático."""
    lineas = ["**En breve.**"]
    sint = (im.get("sintesis_mercado") or "").strip()
    if sint:
        lineas += [sint, ""]
    tm = im.get("tamano_mercado") or {}
    if any(tm.get(k) is not None for k in ("tam_clp", "sam_clp", "som_clp")):
        extra = f" · CAGR {tm['cagr_pct']}%" if tm.get("cagr_pct") is not None else ""
        lineas.append(
            f"Mercado (≈{tm.get('geografia', '?')}, {tm.get('anio_referencia', '?')}): "
            f"TAM {_fmt_clp(tm.get('tam_clp'))} · SAM {_fmt_clp(tm.get('sam_clp'))} · "
            f"SOM {_fmt_clp(tm.get('som_clp'))}{extra} (método: {tm.get('metodo', '?')})."
        )
        reglas = _motor()
        if reglas is not None:
            try:
                mc = reglas.mercado_coherencia(tm.get("tam_clp"), tm.get("sam_clp"), tm.get("som_clp"))
                if mc.get("alertas"):
                    lineas.append("⚠️ Embudo de mercado: " + " ".join(mc["alertas"]))
            except Exception:
                pass
    hall = im.get("hallazgos", []) or []
    if hall:
        ev = {"verificado": 0, "parcial": 0, "no_verificado": 0}
        for h in hall:
            if h.get("estado_evidencia") in ev:
                ev[h["estado_evidencia"]] += 1
        n_comp = len(im.get("competidores", []) or [])
        lineas.append(
            f"Se registraron **{len(hall)} hallazgos** y {n_comp} competidores/sustitutos. "
            f"Evidencia: {ev['verificado']} ✅ verificados, {ev['parcial']} 🟡 parciales, "
            f"{ev['no_verificado']} ⚠️ sin verificar."
        )
    cob = im.get("cobertura_busqueda") or []
    no_ok = [c.get("fuente", "?") for c in cob if c.get("estado") == "no_accesible"]
    if no_ok:
        lineas.append(f"Sin acceso a: {', '.join(no_ok)}.")
    if not sint:
        lineas += ["", "> _Falta la síntesis narrativa (`sintesis_mercado`): arriba solo el "
                   "resumen automático._"]
    return lineas


def _en_breve_modelo(mn: dict, rv: dict) -> list[str]:
    """El veredicto del modelo en una línea: compuerta + indicadores clave."""
    ue = mn.get("unit_economics") or {}
    enc = mn.get("encaje_mercado") or {}
    partes = []
    comp = (rv or {}).get("compuerta")
    if comp:
        partes.append(f"**Compuerta de viabilidad: {comp}.**")
    if ue.get("margen_contribucion_pct") is not None:
        partes.append(f"Margen de contribución {_pct(ue['margen_contribucion_pct'])}.")
    if ue.get("ltv_cac_ratio") is not None:
        partes.append(f"LTV/CAC {ue['ltv_cac_ratio']}.")
    if ue.get("payback_cac_meses") is not None:
        partes.append(f"Payback CAC {ue['payback_cac_meses']} meses.")
    if enc.get("penetracion_som_pct") is not None:
        partes.append(f"Penetración de SOM (último año, base) {_pct(enc['penetracion_som_pct'])}.")
    return ["**En breve.** " + " ".join(partes)] if partes else []


def _glosario_md(datos: dict) -> list[str]:
    glos = datos.get("glosario") or []
    if not glos:
        return []
    out = ["**Glosario** (términos en simple, para el consultor)", ""]
    for g in glos:
        sigla = f" ({g['sigla']})" if g.get("sigla") else ""
        out.append(f"- **{g.get('termino', '?')}{sigla}:** {g.get('definicion', '')}")
    out.append("")
    return out


def _panel_consultor(datos: dict) -> list[str]:
    meta = datos.get("meta") or {}
    pc = datos.get("perfil_comercial") or {}
    im = datos.get("investigacion_mercado") or {}
    sm = datos.get("supuestos_modelo") or {}
    mn = datos.get("modelo_negocio") or {}
    rv = datos.get("revision_viabilidad") or {}
    post = datos.get("postulacion") or {}
    ue = mn.get("unit_economics") or {}

    out = ["## 🧭 Resumen para el consultor", "",
           "> Vista en lenguaje llano de todo el caso. El **detalle** está más abajo. "
           "Los códigos entre paréntesis (EVAL_P4, FORM_W2…) son las etapas internas del flujo.", ""]

    # --- Estado de un vistazo ---
    paso = meta.get("paso_actual", "?")
    fase = ("Redacción" if paso.startswith(("FORM", "PERFIL"))
            else ("Construcción del modelo" if paso.startswith("EVAL") else "Inicio"))
    donde = f"{fase} · {NOMBRE_PASO.get(paso, paso)} ({paso})" if paso != "?" else "recién creado"
    out += ["**Estado de un vistazo**", "", "| | |", "|---|---|", f"| Dónde va | {donde} |",
            f"| Fondo objetivo | {_fondo_legible(datos)} |"]
    if rv.get("compuerta"):
        out.append(f"| Compuerta de viabilidad | **{rv['compuerta']}** |")
    if ue:
        mc = _pct(ue.get("margen_contribucion_pct"))
        ratio = ue.get("ltv_cac_ratio")
        out.append(f"| Unit economics | margen contrib. {mc}"
                   + (f" · LTV/CAC {ratio}" if ratio is not None else "") + " |")
    if post.get("items"):
        its = post["items"]
        obl = [i for i in its if not i.get("opcional")]
        listos = sum(1 for i in obl if i.get("estado") in ("generado", "listo"))
        faltan_cli = sum(1 for i in obl if i.get("estado") not in ("generado", "listo")
                         and i.get("responsable") == "cliente")
        cola = f" · faltan {len(obl) - listos}" + (f" ({faltan_cli} del cliente)" if faltan_cli else "")
        out.append(f"| Paquete de entregables | {listos}/{len(obl)} listos{cola} |")
    dpc = _datos_por_confirmar(datos)
    if dpc:
        out.append(f"| Datos por confirmar | {'; '.join(dpc)} |")
    out += [f"| Próxima acción | {_proxima_accion(datos)} |", ""]

    # --- El caso, paso a paso ---
    pasos = []
    if pc:
        cli = f"{pc.get('cliente_razon_social', '')} ({pc.get('cliente_tamano', '')})".strip()
        prob = _resumir(pc.get("problema_u_oportunidad", ""))
        pasos.append(f"1. **Punto de partida** (Reunión #1) — {cli}. {prob}")
    if im:
        sint = (im.get("sintesis_mercado") or "").strip()
        n = len(im.get("hallazgos", []) or [])
        det = _resumir(sint) if sint else f"se registraron {n} hallazgos de mercado."
        pasos.append(f"2. **Qué encontró la investigación de mercado** — {det}")
    if sm:
        segs = ", ".join(s.get("nombre", "") for s in (sm.get("segmentos") or [])[:3])
        pend = sum(1 for s in (sm.get("supuestos") or []) if s.get("confirmado") is False)
        pasos.append(f"3. **Qué se validó con el cliente** (Reunión #2) — segmentos: {segs or '—'}. "
                     f"{pend} supuesto(s) por confirmar.")
    if mn:
        eb = _en_breve_modelo(mn, rv)
        if eb:
            pasos.append(f"4. **El modelo** — {eb[0].replace('**En breve.** ', '')}")
    if rv.get("comentarios_revision"):
        pasos.append(f"5. **Revisión** — {rv.get('compuerta', '?')}. "
                     f"{_resumir('; '.join(rv['comentarios_revision']), 300)}")
    if datos.get("narrativa"):
        t = (datos["narrativa"] or {}).get("titulo_proyecto", "")
        pasos.append(f"6. **Redacción en curso** — «{t}». Secciones del formulario del fondo (detalle abajo).")
    if pasos:
        out += ["**El caso, paso a paso**", ""] + pasos + [""]

    out += _glosario_md(datos)
    out += ["---", ""]
    return out


# --------------------------------------------------------------------------- #
# Render de cada bloque
# --------------------------------------------------------------------------- #
def _sec_perfil_comercial(pc: dict) -> list[str]:
    c = pc.get("contacto_clave", {}) or {}
    h = pc.get("historia_previa", {}) or {}
    out = [_h2("EVAL_P1", "Reunión #1 — Perfil comercial"), "",
           f"- **Cliente:** {pc.get('cliente_razon_social', '')} ({pc.get('cliente_tamano', '')})"
           + ("" if pc.get("cliente_tamano_confirmado") else "  ⚠️ tamaño sin confirmar"),
           f"- **Inicio actividades:** {pc.get('cliente_fecha_inicio_actividades', '—')}",
           f"- **Contacto:** {c.get('nombre', '')} — {c.get('cargo', '')} ({c.get('email', '')})",
           f"- **Producto / servicio:** {pc.get('producto_o_servicio', '')}",
           f"- **Estado de desarrollo:** {pc.get('estado_desarrollo', '')}",
           f"- **Clientes actuales:** {pc.get('clientes_actuales', '')}",
           f"- **Canal actual:** {pc.get('canal_actual', '')}",
           f"- **Problema / oportunidad:** {pc.get('problema_u_oportunidad', '')}",
           f"- **Resultado de negocio esperado:** {pc.get('resultado_negocio_esperado', '')}",
           f"- **Presupuesto estimado:** {_fmt_clp(pc.get('presupuesto_estimado_clp'))}"]
    if any(h.values()):
        out.append("- **Historia previa:** "
                   + " · ".join(v for v in (h.get("modelo_negocio_actual"),
                                            h.get("intentos_previos_y_resultado"),
                                            h.get("postulaciones_o_evaluaciones_previas")) if v))
    out.append("")
    return out


def _sec_investigacion_mercado(im: dict) -> list[str]:
    out = [_h2("EVAL_P2", "Investigación de mercado + QA"), "", "### En breve", ""]
    out += _en_breve_mercado(im)
    tm = im.get("tamano_mercado") or {}
    if tm:
        out += ["", "### Tamaño de mercado", "",
                f"- **TAM:** {_fmt_clp(tm.get('tam_clp'))} · **SAM:** {_fmt_clp(tm.get('sam_clp'))} "
                f"· **SOM:** {_fmt_clp(tm.get('som_clp'))}",
                f"- **CAGR:** {tm.get('cagr_pct', '—')}% · **Método:** {tm.get('metodo', '?')} "
                f"· **Geografía:** {tm.get('geografia', '?')} · **Año:** {tm.get('anio_referencia', '?')} "
                f"· **Evidencia:** {tm.get('estado_evidencia', '?')}"]
        if tm.get("fuentes"):
            out.append(f"- **Fuentes:** {'; '.join(tm['fuentes'])}")
    comp = im.get("competidores") or []
    if comp:
        out += ["", "### Competidores y sustitutos", ""]
        for c in comp:
            out.append(f"- **{c.get('nombre', '?')}** — {c.get('que_ofrece', '')} · precio "
                       f"{c.get('precio_aprox', '—')} · fortaleza: {c.get('fortaleza', '—')} · "
                       f"debilidad: {c.get('debilidad', '—')}")
    hall = im.get("hallazgos") or []
    if hall:
        out += ["", "### Hallazgos (detalle)", "",
                "> _✅ verificado · 🟡 parcial · ⚠️ no verificado · QA: confirmado/observado/descartado/pendiente_", ""]
        marca = {"verificado": "✅", "parcial": "🟡", "no_verificado": "⚠️"}
        for x in hall:
            ev = marca.get(x.get("estado_evidencia", ""), "❓")
            qa = x.get("verificacion_qa", "pendiente")
            ficha = f" [{x['ficha_kb']}]" if x.get("ficha_kb") else ""
            out.append(f"- {ev} ({x.get('tipo', '')} · {x.get('fuente', '?')} · QA:{qa}) "
                       f"{x.get('hallazgo', '')} — _{x.get('referencia', '')}_{ficha}")
    cob = im.get("cobertura_busqueda") or []
    if cob:
        out += ["", "### Cobertura de búsqueda", ""]
        for c in cob:
            nota = f" — {c['nota']}" if c.get("nota") else ""
            out.append(f"- {c.get('fuente', '?')}: **{c.get('estado', '?')}**{nota}")
    preg = im.get("preguntas_para_reunion_2") or []
    if preg:
        out += ["", "### Preguntas para la Reunión #2 (pool)", ""]
        for i, q in enumerate(preg, 1):
            if isinstance(q, dict):
                cat = f"[{q.get('categoria', '')}] " if q.get("categoria") else ""
                out.append(f"{i}. {cat}{q.get('pregunta', '')}")
            else:
                out.append(f"{i}. {q}")
    out.append("")
    return out


def _sec_supuestos_modelo(sm: dict) -> list[str]:
    out = [_h2("EVAL_P3", "Reunión #2 — Supuestos del modelo"), ""]
    segs = sm.get("segmentos") or []
    if segs:
        out += ["### Segmentos", ""]
        for s in segs:
            out.append(f"- **{s.get('nombre', '?')}** ({s.get('prioridad', '?')}) — "
                       f"{s.get('descripcion', '')}"
                       + (f" · tamaño estimado: {s['tamano_estimado']}" if s.get("tamano_estimado") else ""))
    pv = sm.get("propuesta_valor") or []
    if pv:
        out += ["", "### Propuesta de valor", ""]
        for p in pv:
            out.append(f"- **[{p.get('segmento', '?')}]** {p.get('propuesta', '')} — resuelve: "
                       f"{p.get('dolor_que_resuelve', '')}"
                       + (f"; alternativa actual: {p['alternativa_actual_del_cliente']}"
                          if p.get("alternativa_actual_del_cliente") else ""))
    if sm.get("canales") or sm.get("relacion_clientes"):
        out += ["", f"- **Canales:** {sm.get('canales', '')}",
                f"- **Relación con clientes:** {sm.get('relacion_clientes', '')}"]
    ing = sm.get("estructura_ingresos") or []
    if ing:
        out += ["", "### Estructura de ingresos", ""]
        for x in ing:
            rec = f", cada {x['recurrencia_meses']} meses" if x.get("recurrencia_meses") else " (pago único)"
            out.append(f"- **{x.get('nombre', '?')}** ({x.get('tipo', '?')}) — "
                       f"{_fmt_clp(x.get('precio'))} por {x.get('unidad', '?')}{rec}")
    cost = sm.get("estructura_costos") or []
    if cost:
        out += ["", "### Estructura de costos", ""]
        for x in cost:
            out.append(f"- **{x.get('concepto', '?')}** ({x.get('tipo', '?')}): "
                       f"{_fmt_clp(x.get('monto'))} {x.get('unidad', '')}")
    cac = sm.get("costo_adquisicion_cliente") or {}
    if cac:
        out += ["", f"### CAC", "",
                f"{_fmt_clp(cac.get('valor_clp'))} — base: {cac.get('base', '?')} "
                f"({cac.get('estado_evidencia', '?')})"]
    if sm.get("capacidad_ejecucion"):
        out += ["", "### Capacidad de ejecución", "", sm["capacidad_ejecucion"]]
    if sm.get("recursos_y_socios_clave"):
        out += ["", f"- **Recursos y socios clave:** {sm['recursos_y_socios_clave']}"]
    sup = sm.get("supuestos") or []
    if sup:
        out += ["", "### Supuestos", ""]
        for s in sup:
            mk = "✅ confirmado" if s.get("confirmado") else "⏳ por confirmar"
            val = f" = {s['valor']}" if s.get("valor") is not None else ""
            imp = f" — si falla: {s['impacto_si_falla']}" if s.get("impacto_si_falla") else ""
            out.append(f"- [{mk}] {s.get('supuesto', '')}{val}{imp}")
    out.append("")
    return out


def _sec_modelo_negocio(mn: dict, rv: dict) -> list[str]:
    out = [_h2("EVAL_P4", "Construir el modelo"), "", "### En breve", ""]
    out += _en_breve_modelo(mn, rv) or ["_(modelo aún sin indicadores)_"]
    canvas = mn.get("canvas") or {}
    if canvas:
        out += ["", "### Business Model Canvas", "", "| Bloque | Contenido |", "|---|---|"]
        etiquetas = [
            ("segmentos_cliente", "Segmentos de cliente"), ("propuesta_valor", "Propuesta de valor"),
            ("canales", "Canales"), ("relacion_clientes", "Relación con clientes"),
            ("fuentes_ingreso", "Fuentes de ingreso"), ("recursos_clave", "Recursos clave"),
            ("actividades_clave", "Actividades clave"), ("socios_clave", "Socios clave"),
            ("estructura_costos", "Estructura de costos"),
        ]
        for k, lbl in etiquetas:
            v = (canvas.get(k) or "").replace("\n", " ").replace("|", "\\|")
            out.append(f"| {lbl} | {v} |")
    ue = mn.get("unit_economics") or {}
    if ue:
        out += ["", "### Unit economics", "",
                f"_Unidad del modelo: {ue.get('unidad_modelo', '—')}_", "",
                "| | Valor |", "|---|---|",
                f"| Precio unitario (entrada) | {_fmt_clp(ue.get('precio_unitario'))} |",
                f"| Costo variable unitario (entrada) | {_fmt_clp(ue.get('costo_variable_unitario'))} |",
                f"| Costos fijos mensuales (entrada) | {_fmt_clp(ue.get('costos_fijos_mensuales'))} |",
                f"| CAC (entrada) | {_fmt_clp(ue.get('cac_clp'))} |",
                f"| Vida del cliente (entrada) | {ue.get('vida_cliente_meses', '—')} meses |",
                f"| **Margen de contribución unitario** | {_fmt_clp(ue.get('margen_contribucion_unitario'))} |",
                f"| **Margen de contribución %** | {_pct(ue.get('margen_contribucion_pct'))} |",
                f"| **LTV** | {_fmt_clp(ue.get('ltv_clp'))} |",
                f"| **LTV / CAC** | {ue.get('ltv_cac_ratio', '—')} |",
                f"| **Payback de CAC** | {ue.get('payback_cac_meses', '—')} meses |",
                f"| **Punto de equilibrio** | {ue.get('punto_equilibrio_unidades', '—')} unidades "
                f"/ {_fmt_clp(ue.get('punto_equilibrio_clp'))} |"]
    proy = (mn.get("proyeccion") or {}).get("escenarios") or []
    if proy:
        out += ["", f"### Proyección ({(mn.get('proyeccion') or {}).get('horizonte_anios', '?')} años)", ""]
        for e in proy:
            out += [f"**Escenario {e.get('nombre', '?')}** — {e.get('supuestos_crecimiento', '')}", "",
                    "| Año | Unidades | Ingresos | Costos | Resultado |", "|---|---|---|---|---|"]
            for a in e.get("anios", []) or []:
                out.append(f"| {a.get('anio', '')} | {a.get('unidades', '')} | "
                           f"{_fmt_clp(a.get('ingresos_clp'))} | {_fmt_clp(a.get('costos_clp'))} | "
                           f"{_fmt_clp(a.get('resultado_clp'))} |")
            out.append("")
    enc = mn.get("encaje_mercado") or {}
    if enc:
        out += ["### Encaje con el mercado", "",
                f"- SOM: {_fmt_clp(enc.get('som_clp'))} · ingresos último año (base): "
                f"{_fmt_clp(enc.get('ingresos_ano_final_base_clp'))} · **penetración de SOM: "
                f"{_pct(enc.get('penetracion_som_pct'))}**", ""]
    return out


def _sec_revision_viabilidad(rv: dict) -> list[str]:
    out = [_h2("EVAL_P5", "Revisión de viabilidad + compuerta"), "",
           f"- **Compuerta:** **{rv.get('compuerta', '?')}**",
           f"- **Info suficiente:** {_si_no_bool(rv.get('info_suficiente', True))}", ""]
    ind = rv.get("indicadores") or []
    if ind:
        out += ["### Indicadores", "", "| Indicador | Valor | Umbral | Estado |", "|---|---|---|---|"]
        mk = {"ok": "✅", "alerta": "⚠️", "critico": "⛔", "sin_dato": "❓"}
        for i in ind:
            out.append(f"| {i.get('indicador', '')} | {i.get('valor', '—')} | {i.get('umbral', '')} "
                       f"| {mk.get(i.get('estado'), '?')} {i.get('estado', '')} |")
        out.append("")
    if rv.get("comentarios_revision"):
        out += ["### Comentarios de la revisión", ""]
        out += [f"- {c}" for c in rv["comentarios_revision"]] + [""]
    pal = rv.get("palancas_ajuste") or []
    if pal:
        out += ["### Palancas de ajuste (sugerencias — no cambian el veredicto)", ""]
        for p in pal:
            out.append(f"- **[{p.get('palanca', '?')}]** {p.get('hipotesis', '')}"
                       + (f" → {p['impacto_esperado']}" if p.get("impacto_esperado") else ""))
        out.append("")
    return out


def _sec_narrativa(nv: dict) -> list[str]:
    return [_h2("FORM_W1", "Redacción — Arquitectura de la narrativa"), "",
            f"- **Título:** {nv.get('titulo_proyecto', '')}",
            f"- **Resumen:** {nv.get('resumen', '')}", "",
            "### Problema / oportunidad", "", nv.get("problema_oportunidad", ""), "",
            "### Mercado objetivo", "", nv.get("mercado_objetivo", ""), "",
            "### Propuesta de valor", "", nv.get("propuesta_valor", ""), "",
            "### Diferenciación", "", nv.get("diferenciacion", ""), ""]


def _sec_formulario_oficial(fo: dict) -> list[str]:
    out = ["---", "", f"# Formulario oficial — {fo.get('fondo', '')} (FORM_W2)", "",
           "> Secciones de modelo de negocio / mercado / escalamiento redactadas por el piloto. "
           "Las de metodología técnica, actividades de I+D y equipo las completa el equipo GT.", ""]
    for s in fo.get("secciones", []) or []:
        if s.get("en_alcance_piloto") is False:
            out += [f"## {s.get('titulo', s.get('id', ''))} — _(fuera de alcance del piloto: la completa el equipo GT)_", ""]
            continue
        avisos = []
        if not s.get("cumple_requisitos"):
            avisos.append("requisitos por confirmar")
        if s.get("dentro_limite") is False:
            avisos.append("⚠️ excede el tope")
        cola = f"  _({'; '.join(avisos)})_" if avisos else ""
        out += [f"## {s.get('titulo', s.get('id', ''))}{cola}", "", s.get("respuesta", ""), ""]
    return out


def _sec_plan_escalamiento(pe: dict) -> list[str]:
    out = [_h2("FORM_W3", "Redacción — Plan de escalamiento"), "",
           f"- **Estado actual:** {pe.get('estado_actual', '')}"]
    hitos = pe.get("hitos_comerciales") or []
    if hitos:
        out += ["", "### Hitos comerciales", "", "| N° | Hito | Meta | Fecha objetivo |", "|---|---|---|---|"]
        for h in hitos:
            out.append(f"| {h.get('n', '')} | {h.get('nombre', '')} | {h.get('meta', '')} "
                       f"| {h.get('fecha_objetivo', '')} |")
    out += ["", f"- **Metas de tracción:** {pe.get('metas_traccion', '')}",
            f"- **Estrategia de escalamiento:** {pe.get('estrategia_escalamiento', '')}",
            f"- **Proyección estructurada:** {pe.get('proyeccion_estructurada', '—')}", ""]
    return out


def _sec_impacto_continuidad(ic: dict) -> list[str]:
    ie = ic.get("impacto_esperado", {}) or {}
    out = [_h2("FORM_W4", "Redacción — Impacto y continuidad"), "", "### Impacto esperado", "",
           f"- **Económico:** {ie.get('economico', '')}",
           f"- **Social:** {ie.get('social', '')}",
           f"- **Ambiental:** {ie.get('ambiental', '')}", "",
           "### Estrategia de continuidad", "", ic.get("estrategia_continuidad", ""), ""]
    rb = ic.get("riesgos_barreras") or []
    if rb:
        out += ["### Riesgos y barreras", ""]
        out += [f"- {r.get('riesgo', '')} → _mitigación:_ {r.get('mitigacion', '')}" for r in rb] + [""]
    sac = ic.get("supuestos_a_confirmar") or []
    if sac:
        out += ["### Supuestos a confirmar (antes de presentar)", ""]
        for s in sac:
            out.append(f"- {s.get('supuesto', '')} — afecta: {s.get('seccion_afectada', '—')} "
                       f"· responsable: {s.get('responsable_confirmar', '—')}")
        out.append("")
    return out


def _sec_qa_entrega(qe: dict) -> list[str]:
    out = [_h2("FORM_W5", "QA de coherencia + entrega"), ""]
    mk = {"ok": "✅", "alerta": "⚠️", "pendiente": "❓"}
    for r in qe.get("qa_coherencia", []) or []:
        out.append(f"- {mk.get(r.get('estado'), '❓')} {r.get('regla', '')}: {r.get('detalle', '')}")
    out += ["", f"**Entregado:** {_si_no_bool(qe.get('entregado'))}"
            + (f" · {qe['fecha_entrega']}" if qe.get("fecha_entrega") else "")
            + (f" · paquete: {qe['paquete_path']}" if qe.get("paquete_path") else "")]
    if qe.get("observaciones_abiertas"):
        out += ["", "**Observaciones abiertas (cerrar antes de presentar):**"]
        out += [f"- {o}" for o in qe["observaciones_abiertas"]]
    out.append("")
    return out


def _sec_perfil_corfo(pc: dict) -> list[str]:
    if not pc.get("secciones"):
        return []
    estado = ("feedback recibido ✅" if pc.get("feedback_recibido")
              else ("presentado, esperando feedback ⏳" if pc.get("enviado") else "en preparación"))
    out = ["---", "", f"# Perfil de Proyecto (Fase 1 CORFO) — {pc.get('fondo', '')}", "",
           f"> Estado: **{estado}**. Fase 1 obligatoria; la Fase 2 no inicia hasta el feedback.", ""]
    for s in pc["secciones"]:
        out += [f"## {s.get('titulo', s.get('id', ''))}", "", s.get("respuesta", ""), ""]
    if pc.get("retroalimentacion"):
        out += ["**Retroalimentación del Subcomité:**", "", pc["retroalimentacion"], ""]
    return out


def render_md(datos: dict) -> str:
    meta = datos.get("meta", {})
    out = [f"# Expediente — {meta.get('tenant', '?')}", "",
           f"> Paso actual: **{meta.get('paso_actual', '?')}** · "
           f"actualizado: {meta.get('actualizado', '?')}", ""]
    out += _panel_consultor(datos)

    if datos.get("perfil_comercial"):
        out += _sec_perfil_comercial(datos["perfil_comercial"])
    if datos.get("investigacion_mercado"):
        out += _sec_investigacion_mercado(datos["investigacion_mercado"])
    if datos.get("supuestos_modelo"):
        out += _sec_supuestos_modelo(datos["supuestos_modelo"])
    if datos.get("modelo_negocio"):
        out += _sec_modelo_negocio(datos["modelo_negocio"], datos.get("revision_viabilidad") or {})
    if datos.get("revision_viabilidad"):
        out += _sec_revision_viabilidad(datos["revision_viabilidad"])
    if datos.get("perfil_corfo"):
        out += _sec_perfil_corfo(datos["perfil_corfo"])
    if datos.get("narrativa"):
        out += _sec_narrativa(datos["narrativa"])
    if datos.get("formulario_oficial", {}).get("secciones"):
        out += _sec_formulario_oficial(datos["formulario_oficial"])
    if datos.get("plan_escalamiento"):
        out += _sec_plan_escalamiento(datos["plan_escalamiento"])
    if datos.get("impacto_continuidad"):
        out += _sec_impacto_continuidad(datos["impacto_continuidad"])
    if datos.get("qa_entrega"):
        out += _sec_qa_entrega(datos["qa_entrega"])

    md = "\n".join(out) + "\n"
    # GFM interpreta un par de ~ sueltos como tachado; se reemplaza por ≈ fuera de URLs.
    partes = re.split(r"(https?://\S+)", md)
    return "".join(p if p.startswith(("http://", "https://")) else p.replace("~", "≈")
                   for p in partes)


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def main() -> None:
    ap = argparse.ArgumentParser(description="Render/validación del expediente.")
    ap.add_argument("tenant", help="Nombre del caso en proyectos/")
    ap.add_argument("--validar", action="store_true", help="Solo validar contra el schema")
    ap.add_argument("--limites", action="store_true", help="Largo de campos vs. topes del formulario")
    ap.add_argument("--formulario", action="store_true",
                    help="Completitud de las secciones en alcance del formulario del fondo")
    args = ap.parse_args()

    ruta, datos = cargar_expediente(args.tenant)

    if args.formulario:
        filas = formulario_completitud(datos)
        pendientes = [f for f in filas if f["estado"] not in ("ok", "fuera_alcance")]
        for f in filas:
            marca = {"ok": "✅", "fuera_alcance": "➖"}.get(f["estado"], "❌")
            print(f"  {marca} [{f['estado']}] {f['seccion']}: {f['titulo']}")
        if pendientes:
            print(f"\nINCOMPLETO ({len(pendientes)}) — faltan secciones de modelo de negocio del fondo.")
            sys.exit(1)
        print("OK: secciones en alcance del piloto completas para el fondo.")
        return

    if args.limites:
        filas = limites_caracteres(datos)
        exceden = [f for f in filas if f["excede"]]
        for f in filas:
            print(f"  {'❌' if f['excede'] else '✅'} {f['campo']}: {f['largo']}/{f['limite']}")
        if exceden:
            print(f"\nEXCEDEN el tope ({len(exceden)}):")
            for f in exceden:
                print(f"  - {f['campo']}: {f['largo']} > {f['limite']}")
            sys.exit(1)
        print("OK: todos los campos dentro del tope.")
        return

    errores = validar(datos)

    if args.validar:
        if errores:
            print("INVÁLIDO:")
            for e in errores:
                print(f"  - {e}")
            sys.exit(1)
        print("OK: expediente válido.")
        alertas = alertas_cifras(datos)
        if alertas:
            print("\nAVISO · cifras del cliente inconsistentes entre bloques:")
            for a in alertas:
                print(f"  ⚠ {a}")
        return

    if errores:
        print("AVISO: el expediente tiene errores de validación (se renderiza igual):", file=sys.stderr)
        for e in errores:
            print(f"  - {e}", file=sys.stderr)

    destino = ruta.parent / "expediente.md"
    destino.write_text(render_md(datos), encoding="utf-8")
    print(f"Renderizado: {destino}")


if __name__ == "__main__":
    main()
