#!/usr/bin/env python3
"""Render y validación del expediente de una postulación.

Parte determinista del sistema (no generativa): valida el expediente.json de un
tenant contra el schema y genera su versión legible expediente.md.

Uso:
    python3 render/render.py <tenant>              # genera proyectos/<tenant>/expediente.md
    python3 render/render.py <tenant> --validar    # solo valida contra el schema

La validación usa jsonschema si está instalado; si no, hace chequeos mínimos
(campos requeridos por bloque) y avisa.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SISTEMA = Path(__file__).resolve().parent.parent
SCHEMA_PATH = SISTEMA / "expediente.schema.json"
FORMULARIOS_PATH = SISTEMA / "motor-reglas" / "formularios.json"

# Nombres legibles de cada paso (código → etiqueta), reusados de tools/estado.py
# para no duplicarlos. Los títulos de sección usan "<nombre legible> (CÓDIGO)".
try:
    sys.path.insert(0, str(SISTEMA / "tools"))
    from estado import PASOS as _PASOS  # type: ignore
    NOMBRE_PASO = {code: label for code, label, _ in _PASOS}
    ORDEN_PASOS = [code for code, _, _ in _PASOS]
except Exception:
    NOMBRE_PASO = {}
    ORDEN_PASOS = []


def _h2(code: str, fallback: str) -> str:
    """Encabezado de sección: nombre legible de la etapa + código entre paréntesis."""
    return f"## {NOMBRE_PASO.get(code, fallback)} ({code})"


def _en_breve_estado_arte(p2: dict) -> list[str]:
    """Capa 1 del estado del arte: síntesis para lectura rápida (antes del detalle).

    Combina la síntesis narrativa que escribe el agente (`sintesis_estado_del_arte`,
    opcional) con un **resumen automático** determinista de conteos y evidencia, para
    que el lector entienda el panorama sin leer toda la lista de hallazgos.
    """
    lineas = ["**En breve.**"]
    sintesis = (p2.get("sintesis_estado_del_arte") or "").strip()
    if sintesis:
        lineas += [sintesis, ""]
    hallazgos = p2.get("estado_del_arte_v1", []) or []
    if hallazgos:
        por_tipo: dict = {}
        ev = {"verificado": 0, "parcial": 0, "no_verificado": 0}
        for h in hallazgos:
            por_tipo[h.get("tipo", "otro")] = por_tipo.get(h.get("tipo", "otro"), 0) + 1
            if h.get("estado_evidencia") in ev:
                ev[h["estado_evidencia"]] += 1
        plural = {"paper": "papers", "patente": "patentes", "competidor": "competidores",
                  "producto": "productos"}
        tipos = ", ".join(f"{n} {plural.get(t, t + 's')}" for t, n in sorted(por_tipo.items()))
        conteo = (f"Se revisaron **{len(hallazgos)} fuentes** ({tipos}). "
                  f"Evidencia: {ev['verificado']} ✅ verificadas, {ev['parcial']} 🟡 parciales, "
                  f"{ev['no_verificado']} ⚠️ sin verificar.")
        cob = p2.get("cobertura_busqueda") or []
        no_ok = [c.get("motor", "?") for c in cob if c.get("estado") == "no_accesible"]
        parcial = sum(1 for c in cob if c.get("estado") == "acceso_parcial")
        if no_ok:
            conteo += f" Sin acceso a: {', '.join(no_ok)}"
            conteo += f" (y {parcial} con acceso parcial)." if parcial else "."
        elif parcial:
            conteo += f" {parcial} motor(es) con acceso parcial (ver cobertura abajo)."
        lineas.append(conteo)
    if not sintesis:
        lineas += ["", "> _Falta la síntesis narrativa (`sintesis_estado_del_arte`): arriba solo el "
                   "resumen automático. El agente del Deep Research debería redactarla._"]
    return lineas


def _si_no_bool(v) -> str:
    return "sí" if v is True else ("no" if v is False else "?")


def _en_breve_caso(p4: dict) -> list[str]:
    """Capa 1 de EVAL_P4: el veredicto en lenguaje llano, antes del detalle.

    Lo que el lector quiere primero: ¿es I+D? ¿es defendible? ¿qué instrumento calza?
    """
    fr = p4.get("frascati", {}) or {}
    es_id = fr.get("es_id")
    defendible = fr.get("es_id_defendible")
    partes = [f"**En breve.** ¿Es I+D? **{_si_no_bool(es_id).upper()}**"]
    if defendible is not None:
        partes[0] += f" · defendible tras la prueba de exclusiones: **{_si_no_bool(defendible)}**"
    partes[0] += f" · cuadrante **{fr.get('cuadrante', '?')}**."
    # Mejor instrumento elegible (por alineación Alto>Mediano>Bajo, luego cofinanciamiento).
    orden = {"Alto": 3, "Mediano": 2, "Bajo": 1}
    elegibles = [s for s in (p4.get("perfil_subsidios") or []) if s.get("elegible")]
    if elegibles:
        mejor = max(elegibles, key=lambda s: (orden.get(s.get("alineacion"), 0),
                                              s.get("cofinanciamiento_pct") or 0))
        partes.append(f"Instrumento con mejor calce: **{mejor.get('instrumento', '?')}** "
                      f"(alineación {mejor.get('alineacion', '?')}).")
    else:
        partes.append("Sin instrumento elegible por ahora (ver perfil de subsidios).")
    if defendible is False:
        partes.append("⚠️ **Candidato a falso positivo**: alguna exclusión de la Ley I+D aplica o quedó sin "
                      "sustento — no llevar como I+D sólido; ver la prueba de exclusiones y el reencuadre.")
    return [" ".join(partes)]


def _frascati_detalle(fr: dict) -> list[str]:
    """Bloque '¿Es I+D?' — la clasificación Frascati con la prueba de exclusiones (C1)."""
    if not fr:
        return []
    out = ["### ¿Es I+D? — Clasificación Frascati", "",
           f"- **Veredicto:** es_id = **{_si_no_bool(fr.get('es_id'))}** · "
           f"defendible = **{_si_no_bool(fr.get('es_id_defendible'))}** · cuadrante **{fr.get('cuadrante', '?')}**",
           f"- Componente I (conocimiento nuevo): **{_si_no_bool(fr.get('componente_i'))}** · "
           f"Componente D (resultado incierto): **{_si_no_bool(fr.get('componente_d'))}**",
           f"- **Justificación:** {fr.get('justificacion', '')}"]
    exclusiones = fr.get("exclusiones_evaluadas") or []
    if exclusiones:
        icono = {"sorteada": "✅", "aplica": "⛔", "pendiente": "⏳"}
        out += ["", "**Prueba de exclusiones** (cada componente debe sortear las no-elegibles de la Ley I+D):",
                "> _✅ sorteada (el caso no cae aquí) · ⛔ aplica (el caso cae → no es I+D por ese flanco) · ⏳ pendiente._"]
        for e in exclusiones:
            ic = icono.get(e.get("veredicto"), "❓")
            out.append(f"- {ic} `{e.get('exclusion', '?')}` — {e.get('sustento', '')}")
    else:
        out += ["", "> _Sin prueba de exclusiones registrada (Frascati adversarial, C1): el veredicto "
                "no fue estresado contra las no-elegibles. Debería correrse._"]
    return out


def cargar_expediente(tenant: str) -> tuple[Path, dict]:
    """Carga el expediente.json del tenant. Devuelve (ruta, datos)."""
    ruta = SISTEMA / "proyectos" / tenant / "expediente.json"
    if not ruta.exists():
        sys.exit(f"ERROR: no existe {ruta}")
    return ruta, json.loads(ruta.read_text(encoding="utf-8"))


def alertas_cifras(datos: dict) -> list[str]:
    """C5 · Corre el motor de coherencia sobre meta.cifras_declaradas y devuelve
    las inconsistencias (alertas). No es un error de schema: se surfacea, no se
    silencia, pero no bloquea la validación."""
    cifras = (datos.get("meta") or {}).get("cifras_declaradas") or []
    if not cifras:
        return []
    try:
        sys.path.insert(0, str(SISTEMA / "motor-reglas"))
        import reglas  # type: ignore
        return [f"{r['concepto']}: {r['detalle']}"
                for r in reglas.coherencia_cifras_cliente(cifras) if r["estado"] == "alerta"]
    except Exception:
        return []


def validar(datos: dict) -> list[str]:
    """Valida el expediente contra el schema. Devuelve lista de errores (vacía si OK)."""
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    try:
        import jsonschema  # type: ignore

        validador = jsonschema.Draft7Validator(schema)
        return [f"{'/'.join(map(str, e.path))}: {e.message}" for e in validador.iter_errors(datos)]
    except ImportError:
        # Fallback mínimo sin jsonschema: requeridos de cada bloque presente.
        errores: list[str] = []
        if "meta" not in datos:
            errores.append("meta: bloque requerido ausente")
        reqs = {
            "eval_p1": ["empresa_razon_social", "empresa_tamano",
                        "proyecto_presupuesto_estimado", "problema_oportunidad_declarado"],
            "eval_p2": ["hipotesis_preliminar_o_objetivo_general",
                        "estado_del_arte_v1", "cobertura_busqueda", "cuestionario_indagacion"],
        }
        for bloque, campos in reqs.items():
            if bloque in datos:
                for c in campos:
                    if c not in datos[bloque]:
                        errores.append(f"{bloque}/{c}: campo requerido ausente")
        if "eval_p2" in datos:
            ep2 = datos["eval_p2"]
            if isinstance(ep2.get("cuestionario_indagacion"), list) and len(ep2["cuestionario_indagacion"]) < 8:
                errores.append("eval_p2/cuestionario_indagacion: se requiere un pool ≥8 preguntas (2 categorías)")
            # Cada hallazgo debe declarar su evidencia (control de veracidad).
            for i, h in enumerate(ep2.get("estado_del_arte_v1", []) or []):
                for c in ("motor", "estado_evidencia"):
                    if c not in h:
                        errores.append(f"eval_p2/estado_del_arte_v1[{i}]/{c}: requerido (veracidad)")
                if h.get("estado_evidencia") not in (None, "verificado", "parcial", "no_verificado"):
                    errores.append(f"eval_p2/estado_del_arte_v1[{i}]/estado_evidencia: valor inválido")
        return errores


def limites_caracteres(datos: dict) -> list[dict]:
    """Chequea la longitud de cada campo de texto contra su maxLength del schema.

    Los campos del formulario Ley I+D/CORFO tienen topes de caracteres; un campo
    sobre el tope NO es enviable (la plataforma lo trunca/rechaza). Devuelve
    [{campo, largo, limite, excede}] para cada campo con maxLength presente.
    """
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
    """Chequea que el formulario_oficial cubra las secciones EXIGIDAS por el fondo.

    Lee motor-reglas/formularios.json, toma el fondo elegido (formulario_oficial.fondo
    o meta.instrumento_objetivo) y verifica que cada sección requerida esté presente,
    con respuesta no vacía y dentro de su límite. Devuelve [{seccion, titulo, estado}].
    estado: ok | falta | vacia | excede | fondo_desconocido.
    """
    fo = datos.get("formulario_oficial") or {}
    fondo = fo.get("fondo") or (datos.get("meta") or {}).get("instrumento_objetivo")
    spec = json.loads(FORMULARIOS_PATH.read_text(encoding="utf-8")).get("fondos", {})
    if not fondo or fondo not in spec:
        return [{"seccion": "-", "titulo": f"fondo '{fondo}'", "estado": "fondo_desconocido"}]
    tipo = (datos.get("meta") or {}).get("tipo_proyecto", "")
    respuestas = {s.get("id"): s for s in fo.get("secciones", []) or []}
    out = []
    for sec in spec[fondo]["secciones"]:
        if sec.get("solo_si_tipo") and sec["solo_si_tipo"] not in (tipo or ""):
            continue  # p.ej. incertidumbre solo si tipo_proyecto informático
        r = respuestas.get(sec["id"])
        if r is None:
            estado = "falta"
        elif not (r.get("respuesta") or "").strip():
            estado = "vacia"
        elif sec.get("limite") and len(r["respuesta"]) > sec["limite"]:
            estado = "excede"
        else:
            estado = "ok"
        out.append({"seccion": sec["id"], "titulo": sec["titulo"], "estado": estado})
    return out


def _resumir(texto: str, n: int = 320) -> str:
    """Recorta a las primeras frases hasta ~n caracteres, para el panel (lectura rápida)."""
    t = " ".join((texto or "").split())
    if len(t) <= n:
        return t
    corte = t[:n]
    fin = max(corte.rfind(". "), corte.rfind("; "))
    return (corte[:fin + 1] if fin > n // 2 else corte).rstrip() + " […]"


def _fondo_legible(datos: dict) -> str:
    return ((datos.get("postulacion") or {}).get("fondo_nombre")
            or (datos.get("eval_p5") or {}).get("instrumento_corfo_seleccionado")
            or (datos.get("meta") or {}).get("instrumento_objetivo")
            or "por definir")


def _datos_por_confirmar(datos: dict) -> list[str]:
    """Señales de supuestos sin confirmar que el consultor debe cerrar (no exhaustivo)."""
    p1 = datos.get("eval_p1") or {}
    faltan = []
    if p1 and p1.get("empresa_tamano_confirmado") is not True:
        faltan.append("tamaño de empresa (afecta el cofinanciamiento)")
    if p1 and not p1.get("empresa_fecha_inicio_actividades"):
        faltan.append("antigüedad de la empresa (elegibilidad)")
    # Marcadores [POR CONFIRMAR] regados en campos narrativos.
    blob = json.dumps(datos, ensure_ascii=False)
    n = blob.count("[POR CONFIRMAR]")
    if n:
        faltan.append(f"{n} dato(s) marcados «[POR CONFIRMAR]» en el detalle")
    return faltan


def _proxima_accion(datos: dict) -> str:
    """Nombre legible del paso siguiente al actual (según el orden del flujo)."""
    actual = (datos.get("meta") or {}).get("paso_actual", "")
    if actual == "ENVIADO":
        return "postulación enviada — fin del flujo"
    if actual == "FORM_W5":
        return "revisión final (QA + paquete completo) y envío en la plataforma"
    if actual in ORDEN_PASOS:
        i = ORDEN_PASOS.index(actual)
        if i + 1 < len(ORDEN_PASOS):
            sig = ORDEN_PASOS[i + 1]
            return f"{NOMBRE_PASO.get(sig, sig)} ({sig})"
    if actual in ("INICIO", ""):
        return f"{NOMBRE_PASO.get('EVAL_P1', 'Reunión #1')} (EVAL_P1)"
    return "—"


def _panel_consultor(datos: dict) -> list[str]:
    """Resumen para el consultor: todo el caso en lenguaje llano, antes del detalle técnico.

    Reúne los campos narrativos que ya existen (síntesis, objetivo, veredicto…) y los
    presenta como un digest legible; el detalle denso (tablas, íconos, formulario) queda
    abajo. No inventa: si un dato no está, lo omite.
    """
    meta = datos.get("meta") or {}
    p1 = datos.get("eval_p1") or {}
    p2 = datos.get("eval_p2") or {}
    p3 = datos.get("eval_p3") or {}
    p4 = datos.get("eval_p4") or {}
    p5 = datos.get("eval_p5") or {}
    fr = p4.get("frascati") or {}
    post = datos.get("postulacion") or {}

    out = ["## 🧭 Resumen para el consultor", "",
           "> Vista en lenguaje llano de todo el caso. El **detalle técnico completo** está más abajo. "
           "Los códigos entre paréntesis (EVAL_P4, FORM_W2…) son las etapas internas del flujo.", ""]

    # --- Estado de un vistazo ---
    paso = meta.get("paso_actual", "?")
    fase = "Formulación" if paso.startswith(("FORM", "PERFIL")) else ("Evaluación" if paso.startswith("EVAL") else "Inicio")
    donde = f"{fase} · {NOMBRE_PASO.get(paso, paso)} ({paso})" if paso not in ("?",) else "recién creado"
    out += ["**Estado de un vistazo**", "", "| | |", "|---|---|", f"| Dónde va | {donde} |"]
    if fr:
        esid = "Sí" if fr.get("es_id") else "No"
        defe = fr.get("es_id_defendible")
        cola = f" · defendible: {'sí' if defe else ('no ⚠️' if defe is False else '?')}"
        out.append(f"| ¿Es I+D? | **{esid}**{cola} · cuadrante {fr.get('cuadrante', '?')} |")
    out.append(f"| Fondo objetivo | {_fondo_legible(datos)} |")
    if p5:
        voto = p5.get("voto_comite", "?")
        out.append(f"| Decisión del comité | **{p5.get('compuerta', '?')}** ({voto}) |")
    if post.get("items"):
        its = post["items"]
        obl = [i for i in its if not i.get("opcional")]
        listos = sum(1 for i in obl if i.get("estado") in ("generado", "listo"))
        faltan_cli = sum(1 for i in obl if i.get("estado") not in ("generado", "listo") and i.get("responsable") == "cliente")
        cola = f" · faltan {len(obl) - listos}" + (f" ({faltan_cli} del cliente)" if faltan_cli else "")
        out.append(f"| Paquete de postulación | {listos}/{len(obl)} listos{cola} |")
    dpc = _datos_por_confirmar(datos)
    if dpc:
        out.append(f"| Datos por confirmar | {'; '.join(dpc)} |")
    out.append(f"| Próxima acción | {_proxima_accion(datos)} |")
    out.append("")

    # --- El caso, paso a paso (en lenguaje llano) ---
    pasos = []
    if p1:
        emp = f"{p1.get('empresa_razon_social', '')} ({p1.get('empresa_tamano', '')})".strip()
        prob = _resumir(p1.get("problema_oportunidad_declarado", ""))
        pasos.append(f"1. **Punto de partida** (Reunión #1) — {emp}. {prob}")
    if p2:
        sint = (p2.get("sintesis_estado_del_arte") or "").strip()
        n_fuentes = len(p2.get("estado_del_arte_v1", []) or [])
        n_preg = len(p2.get("cuestionario_indagacion", []) or [])
        det = _resumir(sint) if sint else f"se revisaron {n_fuentes} fuentes del estado del arte."
        extra = f" Se prepararon {n_preg} preguntas para la Reunión #2." if n_preg else ""
        pasos.append(f"2. **Qué encontró la investigación** (Deep Research #1) — {det}{extra}")
    if p3:
        ref = _resumir(p3.get("hipotesis_objetivo_refinado", ""))
        trl = p3.get("trl_declarado", "?")
        pasos.append(f"3. **Qué se refinó con el cliente** (Reunión #2) — {ref} (madurez tecnológica declarada: TRL {trl}).")
    if p4:
        obj = _resumir(p4.get("objetivo_general_smart", ""), 360)
        if fr:
            veredicto = "es I+D" if fr.get("es_id") else "no califica como I+D"
            just = _resumir(fr.get("justificacion", ""), 360)
            pasos.append(f"4. **¿Es I+D?** (Preparar el caso) — {veredicto}. {just}")
        if obj:
            pasos.append(f"5. **Objetivo del proyecto** — {obj}")
    if p5:
        enf = _resumir(p5.get("enfoque_postulacion", ""), 240)
        cola = f" Enfoque: {enf}" if enf else ""
        pasos.append(f"6. **Decisión del comité** — {p5.get('compuerta', '?')} ({p5.get('voto_comite', '?')}).{cola}")
    if datos.get("form_w1") or datos.get("form_w2"):
        w1 = datos.get("form_w1") or {}
        titulo = w1.get("titulo_proyecto", "")
        pasos.append(f"7. **Formulación en curso** — «{titulo}». Redacción del formulario del fondo (ver detalle abajo).")
    if pasos:
        out += ["**El caso, paso a paso**", ""] + pasos + [""]

    # --- Glosario ---
    out += _glosario_md(datos)
    out += ["---", ""]
    return out


def _glosario_md(datos: dict) -> list[str]:
    """Glosario de términos del área, en lenguaje llano (para un consultor no experto)."""
    glos = datos.get("glosario") or []
    if not glos:
        return []
    out = ["**Glosario** (términos del área, en simple)", ""]
    for g in glos:
        sigla = f" ({g['sigla']})" if g.get("sigla") else ""
        out.append(f"- **{g.get('termino', '?')}{sigla}:** {g.get('definicion', '')}")
    out.append("")
    return out


def render_md(datos: dict) -> str:
    """Genera el Markdown legible del expediente."""
    meta = datos.get("meta", {})
    out = [f"# Expediente — {meta.get('tenant', '?')}", ""]
    out += [f"> Paso actual: **{meta.get('paso_actual', '?')}** · "
            f"actualizado: {meta.get('actualizado', '?')}", ""]
    out += _panel_consultor(datos)

    p1 = datos.get("eval_p1")
    if p1:
        c = p1.get("contacto_clave", {}) or {}
        out += [_h2("EVAL_P1", "Reunión #1 — Perfil preliminar"), "",
                f"- **Empresa:** {p1.get('empresa_razon_social', '')} "
                f"({p1.get('empresa_tamano', '')})",
                f"- **Inicio actividades:** {p1.get('empresa_fecha_inicio_actividades', '')}",
                f"- **Contacto:** {c.get('nombre', '')} — {c.get('cargo', '')} "
                f"({c.get('email', '')})",
                f"- **Presupuesto estimado:** {p1.get('proyecto_presupuesto_estimado', '')} CLP",
                f"- **Problema/oportunidad:** {p1.get('problema_oportunidad_declarado', '')}",
                f"- **Resultado esperado:** {p1.get('resultado_esperado_negocio', '')}", ""]

    p2 = datos.get("eval_p2")
    if p2:
        out += [_h2("EVAL_P2", "Deep Research #1 + QA de veracidad"), "",
                f"**Hipótesis / objetivo general:** {p2.get('hipotesis_preliminar_o_objetivo_general', '')}",
                "", "### Estado del arte", ""]
        # Capa 1 — En breve (síntesis para lectura rápida): narrativa del agente + resumen automático.
        out += _en_breve_estado_arte(p2)
        # Capa 2 — Cómo leer lo que sigue (guía + leyenda).
        out += ["",
                "**Cómo leer lo que sigue.** Abajo, en orden: (1) el **detalle de cada fuente** hallada, "
                "con su nivel de evidencia y el resultado del QA independiente; (2) la **cobertura de búsqueda** "
                "(qué motores se consultaron y con qué suerte); (3) los **desafíos técnicos** con su fact-check; "
                "y (4) el **pool de preguntas** para la Reunión #2.",
                "",
                "> _Leyenda — evidencia:_ ✅ verificado (fuente abierta y coincide) · "
                "🟡 parcial (solo abstract/metadata; full-text en paywall) · "
                "⚠️ no verificado (referenciado pero no confirmado). "
                "_QA (control de veracidad independiente):_ confirmado · observado (matiz/corrección) · "
                "descartado · pendiente.",
                ""]
        # Capa 3 — Detalle (lo que se mostraba antes).
        out += ["**1. Fuentes halladas (detalle):**", ""]
        marca = {"verificado": "✅", "parcial": "🟡", "no_verificado": "⚠️"}
        for h in p2.get("estado_del_arte_v1", []) or []:
            ficha = f" [{h['ficha_kb']}]" if h.get("ficha_kb") else ""
            ev = marca.get(h.get("estado_evidencia", ""), "❓")
            qa = h.get("verificacion_qa", "pendiente")
            out.append(f"- {ev} ({h.get('tipo', '')} · {h.get('motor', '?')} · QA:{qa}) "
                       f"{h.get('hallazgo', '')} — _{h.get('referencia', '')}_{ficha}")
        cob = p2.get("cobertura_busqueda")
        if cob:
            out += ["", "**2. Cobertura de búsqueda (honestidad):**"]
            for c in cob:
                nota = f" — {c['nota']}" if c.get("nota") else ""
                out.append(f"- {c.get('motor', '?')}: **{c.get('estado', '?')}**{nota}")
        out += ["", f"**3. Desafíos técnicos (con fact-check):** {p2.get('desafios_tecnicos_identificados_v1', '')}",
                "", "**4. Cuestionario para Reunión #2** (pool — seleccionar las mejores):"]
        etiqueta_cat = {"objetivo_es_id": "Objetivo / ¿es I+D?", "estado_arte_desafios": "Estado del arte / desafíos técnicos"}
        preguntas = p2.get("cuestionario_indagacion", []) or []
        por_cat = {}
        for q in preguntas:
            if isinstance(q, dict):
                por_cat.setdefault(q.get("categoria", "otras"), []).append(q.get("pregunta", ""))
            else:
                por_cat.setdefault("otras", []).append(q)
        if list(por_cat) == ["otras"]:  # formato plano (compat)
            for i, q in enumerate(por_cat["otras"], 1):
                out.append(f"{i}. {q}")
        else:
            for cat, qs in por_cat.items():
                out += ["", f"_{etiqueta_cat.get(cat, cat)}:_"]
                out += [f"{i}. {q}" for i, q in enumerate(qs, 1)]
        out.append("")

    p3 = datos.get("eval_p3")
    if p3:
        out += [_h2("EVAL_P3", "Reunión #2 — Perfil técnico v2"), "",
                f"- **Objetivo/hipótesis refinado:** {p3.get('hipotesis_objetivo_refinado', '')}",
                f"- **TRL declarado:** {p3.get('trl_declarado', '?')}",
                f"- **Perfil técnico v2:** {p3.get('perfil_tecnico_proyecto_v2', '')}", ""]

    p4 = datos.get("eval_p4")
    if p4:
        out += [_h2("EVAL_P4", "Preparar el caso — Frascati + subsidios"), ""]
        out += _en_breve_caso(p4)
        out += ["", f"**Objetivo (SMART):** {p4.get('objetivo_general_smart', '')}", ""]
        # Estado del arte específico + desafíos (narrativa; antes ni se renderizaban).
        if p4.get("estado_del_arte_especifico"):
            out += ["### Estado del arte específico", "", p4["estado_del_arte_especifico"], ""]
        if p4.get("desafios_tecnicos_consolidados"):
            out += [f"**Desafíos técnicos (consolidados, con vigencia):** {p4['desafios_tecnicos_consolidados']}", ""]
        # ¿Es I+D? — Frascati adversarial (con la prueba de exclusiones, C1).
        out += _frascati_detalle(p4.get("frascati", {}) or {})
        # Reencuadre a elegibilidad (C3) — solo si hay sugerencias.
        reenc = p4.get("reencuadre_elegibilidad") or []
        if reenc:
            out += ["", "### Reencuadre a elegibilidad",
                    "> _Sugerencias para volver el caso elegible. NO cambian el veredicto; el consultor y el cliente deciden._", ""]
            for r in reenc:
                tipo = f" _({r['tipo']})_" if r.get("tipo") else ""
                out.append(f"- **{r.get('opcion', '?')}**{tipo}: {r.get('descripcion', '')}")
            out.append("")
        # Perfil de subsidios.
        out += ["", "### Perfil de subsidios (elegibilidad del motor de reglas)", ""]
        for s in p4.get("perfil_subsidios", []) or []:
            mk = "✓" if s.get("elegible") else "✗"
            pct = s.get("cofinanciamiento_pct")
            pct_s = f" · cofin {int(pct*100)}%" if isinstance(pct, (int, float)) else ""
            out.append(f"- {mk} {s.get('instrumento', '?')} (alineación {s.get('alineacion', '?')}{pct_s})"
                       f" — {s.get('justificacion', '')}")
        out.append("")

    p5 = datos.get("eval_p5")
    if p5:
        out += [_h2("EVAL_P5", "Comité + compuerta"), "",
                f"- **Voto:** {p5.get('voto_comite', '?')}",
                f"- **Instrumento seleccionado:** {p5.get('instrumento_corfo_seleccionado', '—')}",
                f"- **Compuerta:** **{p5.get('compuerta', '?')}**", ""]

    # --- Fase 2: Formulación ---
    w1 = datos.get("form_w1")
    if w1:
        out += [_h2("FORM_W1", "Formulación: arquitectura técnica"), "",
                f"- **Título:** {w1.get('titulo_proyecto', '')}",
                f"- **Resumen del proyecto:** {w1.get('resumen_proyecto', '')}",
                f"- **Contexto técnico del proyecto:** {w1.get('contexto_tecnico_proyecto', '')}",
                f"- **Objetivo general:** {w1.get('objetivo_general_proyecto', '')}",
                f"- **Clasificación:** {w1.get('clasificacion_actividades', '')}", ""]
    w2 = datos.get("form_w2")
    if w2:
        ruta_lbl = {"A": "A — Investigación", "B": "B — Desarrollo Experimental",
                    "AB": "AB — Investigación + Desarrollo Experimental"}
        r = w2.get("ruta", "?")
        out += [f'{_h2("FORM_W2", "Formulación: redacción I+D")} — Ruta {ruta_lbl.get(r, r)}', ""]
        etiquetas = [
            ("estado_del_arte_investigacion", "Estado del arte (Investigación, P7)"),
            ("nuevos_conocimientos_generados", "Nuevos conocimientos generados (Investigación, P8)"),
            ("descripcion_desarrollo_tangible", "Desarrollo tangible (Desarrollo Experimental, P9)"),
            ("atributos_tecnicos_superioridad", "Atributos técnicos de superioridad (Desarrollo Experimental, P10)"),
            ("incertidumbre_cientifico_tecnologica", "Incertidumbre científico-tecnológica (Desarrollo Experimental, P11)"),
        ]
        for k, label in etiquetas:
            if w2.get(k):
                out += [f"### {label}", "", w2[k], ""]
    w3 = datos.get("form_w3")
    if w3:
        def _si_no(v):
            return "Sí" if v is True else ("No" if v is False else "?")
        pa = w3.get("profesional_acreditador", {}) or {}
        out += [_h2("FORM_W3", "Formulación: capacidades + Gantt"), "",
                f"- **Profesional acreditador:** {pa.get('nombre', '')} "
                f"(contrato vigente: {_si_no(pa.get('tiene_contrato_vigente'))}, "
                f"I+D últimos 36m: {_si_no(pa.get('experiencia_id_36m'))})",
                f"- **Plan de trabajo:** {w3.get('plan_de_trabajo', '')}"]
        personal = w3.get("personal_asociado", []) or []
        if personal:
            out.append("- **Personal asociado:**")
            for pe in personal:
                hh = f", {pe['horas']} hh" if pe.get("horas") else ""
                cta = f" · {pe['cuenta']}" if pe.get("cuenta") else ""
                out.append(f"  - {pe.get('nombre', '')} — {pe.get('funcion', '')}{cta}{hh}")
        else:
            out.append("- **Personal asociado:** [POR CONFIRMAR]")
        subs = w3.get("subcontratos_habilitados", []) or []
        if subs:
            out.append("- **Subcontratos habilitados:**")
            for s in subs:
                out.append(f"  - {s}")
        acts = w3.get("actividades", []) or []
        if acts:
            out += ["", "**Carta Gantt (actividades):**",
                    "", "| N° | Actividad | Objetivo | Desafío | Inicio | Fin |",
                    "|---|---|---|---|---|---|"]
            for a in acts:
                out.append(f"| {a.get('n', '')} | {a.get('nombre', '')} | {a.get('objetivo', '')} "
                           f"| {a.get('desafio_n', '')} | {a.get('fecha_inicio', '')} | {a.get('fecha_fin', '')} |")
        out.append("")
    w4 = datos.get("form_w4")
    if w4:
        enc = w4.get("registro_encuesta_ley_id", {}) or {}
        out += [_h2("FORM_W4", "Formulación: admin + encuesta"), "",
                f"- **Sistema contable:** {w4.get('nombre_sistema_contable', '')}",
                f"- **Fase del proyecto:** {enc.get('fase_proyecto_actual', '')}",
                f"- **Arancel:** {w4.get('arancel_clp', '—')} CLP", ""]
    w5 = datos.get("form_w5")
    if w5:
        out += [_h2("FORM_W5", "Formulación: QA + envío"), ""]
        mk = {"ok": "✅", "alerta": "⚠️", "pendiente": "❓"}
        for r in w5.get("qa_coherencia", []) or []:
            out.append(f"- {mk.get(r.get('estado'), '❓')} {r.get('regla', '')}: {r.get('detalle', '')}")
        out += ["", f"**Enviado:** {w5.get('enviado', False)}"
                f"{' · comprobante: ' + w5['comprobante_envio_ley_id'] if w5.get('comprobante_envio_ley_id') else ''}", ""]

    pc = datos.get("perfil_corfo")
    if pc and pc.get("secciones"):
        estado = "feedback recibido ✅" if pc.get("feedback_recibido") else ("presentado, esperando feedback ⏳" if pc.get("enviado") else "en preparación")
        out += ["---", "", f"# Perfil de Proyecto (Fase 1 CORFO) — {pc.get('fondo', '')}", "",
                f"> Estado: **{estado}**. Fase 1 obligatoria; la Fase 2 no inicia hasta el feedback.", ""]
        for s in pc["secciones"]:
            out += [f"## {s.get('titulo', s.get('id', ''))}", "", s.get("respuesta", ""), ""]
        if pc.get("retroalimentacion"):
            out += ["**Retroalimentación del Subcomité:**", "", pc["retroalimentacion"], ""]

    fo = datos.get("formulario_oficial")
    if fo and fo.get("secciones"):
        out += ["---", "", f"# Formulario oficial — {fo.get('fondo', '')}", "",
                "> Respuestas al formulario del fondo elegido (se agregan al insumo del proceso).", ""]
        for s in fo["secciones"]:
            check = "" if s.get("cumple_requisitos") else "  ⚠️ requisitos por confirmar"
            out += [f"## {s.get('titulo', s.get('id', ''))}{check}", "", s.get("respuesta", ""), ""]

    md = "\n".join(out) + "\n"
    # GFM interpreta un par de ~ sueltos como tachado ("~13 ... ~100" raya todo
    # el texto intermedio), y no todos los previsualizadores soportan el escape
    # \~. Se reemplaza ~ por ≈ (mismo sentido: aproximadamente) fuera de URLs,
    # donde una ~ puede ser parte de la ruta.
    partes = re.split(r"(https?://\S+)", md)
    return "".join(p if p.startswith(("http://", "https://")) else p.replace("~", "≈")
                   for p in partes)


def main() -> None:
    ap = argparse.ArgumentParser(description="Render/validación del expediente.")
    ap.add_argument("tenant", help="Nombre del proyecto en proyectos/")
    ap.add_argument("--validar", action="store_true", help="Solo validar contra el schema")
    ap.add_argument("--limites", action="store_true", help="Chequear largo de campos vs topes del formulario")
    ap.add_argument("--formulario", action="store_true", help="Chequear completitud del formulario oficial del fondo")
    args = ap.parse_args()

    ruta, datos = cargar_expediente(args.tenant)

    if args.formulario:
        filas = formulario_completitud(datos)
        faltan = [f for f in filas if f["estado"] != "ok"]
        for f in filas:
            marca = "✅" if f["estado"] == "ok" else "❌"
            print(f"  {marca} [{f['estado']}] {f['seccion']}: {f['titulo']}")
        if faltan:
            print(f"\nINCOMPLETO ({len(faltan)}) — NO enviable hasta cubrir las secciones del fondo.")
            sys.exit(1)
        print("OK: formulario oficial completo para el fondo.")
        return

    if args.limites:
        filas = limites_caracteres(datos)
        exceden = [f for f in filas if f["excede"]]
        for f in filas:
            marca = "❌" if f["excede"] else "✅"
            print(f"  {marca} {f['campo']}: {f['largo']}/{f['limite']}")
        if exceden:
            print(f"\nEXCEDEN el tope ({len(exceden)}) — NO enviable hasta acortar:")
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
            print("\nAVISO (C5) · cifras del cliente inconsistentes entre bloques:")
            for a in alertas:
                print(f"  ⚠ {a}")
        return

    if errores:
        print("AVISO: el expediente tiene errores de validación (se renderiza igual):",
              file=sys.stderr)
        for e in errores:
            print(f"  - {e}", file=sys.stderr)

    destino = ruta.parent / "expediente.md"
    destino.write_text(render_md(datos), encoding="utf-8")
    print(f"Renderizado: {destino}")


if __name__ == "__main__":
    main()
