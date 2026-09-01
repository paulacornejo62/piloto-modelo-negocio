#!/usr/bin/env python3
"""Motor de reglas determinista del piloto de modelo de negocio.

Parte NO generativa: calculos exactos y repetibles que no deben quedar a criterio
del LLM (un modelo podria alucinar un umbral). Cubre:

  - dimensionamiento de mercado (coherencia TAM / SAM / SOM),
  - unit economics (margen de contribucion, LTV, LTV/CAC, payback, punto de equilibrio),
  - proyeccion financiera anual por escenario,
  - encaje de la proyeccion con el mercado obtenible,
  - la compuerta de viabilidad SOLIDO / AJUSTAR / INVIABLE / DEVOLVER,
  - QA de coherencia de la Fase 2 (FORM_W5) y de las cifras que declara el cliente.

Umbrales y parametros en `parametros.json` (mismo directorio). Sin dependencias
externas.

>>> PRIMERA VERSION. Los umbrales (margen minimo, LTV/CAC, payback, penetracion de
    SOM) estan POR VALIDAR con ingenieria comercial. Se editan en parametros.json.

Uso como CLI:
    python3 motor-reglas/reglas.py --test     # autotest (asserts)
    python3 motor-reglas/reglas.py --demo     # demo con un caso
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

PARAMS = json.loads((Path(__file__).resolve().parent / "parametros.json").read_text(encoding="utf-8"))
UMBRALES = PARAMS["umbrales"]


# ---------- helpers ----------
def _num(x):
    """float(x) si es un numero utilizable; None en cualquier otro caso (incl. bool)."""
    try:
        if x is None or isinstance(x, bool):
            return None
        return float(x)
    except (TypeError, ValueError):
        return None


def _pct(x):
    return None if x is None else round(x, 4)


# ---------- Mercado: coherencia TAM / SAM / SOM (EVAL_P2 / EVAL_P4) ----------
def mercado_coherencia(tam_clp=None, sam_clp=None, som_clp=None) -> dict:
    """Verifica el embudo de mercado: SOM <= SAM <= TAM.

    No opina sobre si el mercado es grande o chico: solo chequea que las tres
    cifras esten en la relacion correcta y marca lo que falta o no cuadra.
    """
    tam, sam, som = _num(tam_clp), _num(sam_clp), _num(som_clp)
    alertas = []
    faltan = [n for n, v in (("TAM", tam), ("SAM", sam), ("SOM", som)) if v is None]
    if sam is not None and tam is not None and sam > tam:
        alertas.append(f"SAM ({sam:,.0f}) > TAM ({tam:,.0f}): el mercado servible no puede exceder el total.")
    if som is not None and sam is not None and som > sam:
        alertas.append(f"SOM ({som:,.0f}) > SAM ({sam:,.0f}): el mercado obtenible no puede exceder el servible.")
    if som is not None and tam is not None and sam is None and som > tam:
        alertas.append(f"SOM ({som:,.0f}) > TAM ({tam:,.0f}).")
    return {
        "ok": not alertas and not faltan,
        "faltan": faltan,
        "alertas": alertas,
        "tam_clp": tam, "sam_clp": sam, "som_clp": som,
    }


# ---------- Unit economics (EVAL_P4) ----------
def unit_economics(precio_unitario=None, costo_variable_unitario=None,
                   costos_fijos_mensuales=None, cac_clp=None,
                   vida_cliente_meses=None) -> dict:
    """Indicadores unitarios del modelo, calculados desde sus ENTRADAS.

    Entradas en CLP salvo vida_cliente_meses (meses). 'Unidad' es lo que el modelo
    defina (un cliente/mes, una transaccion, un equipo vendido); el caller pasa
    valores consistentes con esa unidad.

    Devuelve las SALIDAS y `faltan_entradas` (que entrada falto para cada calculo
    que quedo en None).
    """
    p = _num(precio_unitario)
    cv = _num(costo_variable_unitario)
    cf = _num(costos_fijos_mensuales)
    cac = _num(cac_clp)
    vida = _num(vida_cliente_meses)

    faltan: list[str] = []
    r: dict = {
        "margen_contribucion_unitario": None,
        "margen_contribucion_pct": None,
        "ltv_clp": None,
        "ltv_cac_ratio": None,
        "payback_cac_meses": None,
        "punto_equilibrio_unidades": None,
        "punto_equilibrio_clp": None,
    }

    if p is None or cv is None:
        faltan.append("precio_unitario y/o costo_variable_unitario")
    else:
        mcu = p - cv
        r["margen_contribucion_unitario"] = round(mcu, 2)
        r["margen_contribucion_pct"] = _pct(mcu / p) if p else None

        # LTV (modelos recurrentes)
        if vida is not None:
            r["ltv_clp"] = round(mcu * vida, 2)
            if cac is not None and cac > 0:
                r["ltv_cac_ratio"] = round((mcu * vida) / cac, 2)
        elif cac is not None:
            faltan.append("vida_cliente_meses (para LTV / LTV-CAC)")

        # Payback de CAC (en periodos unitarios; si la unidad es cliente/mes -> meses)
        if cac is not None and mcu > 0:
            r["payback_cac_meses"] = round(cac / mcu, 1)

        # Punto de equilibrio
        if cf is not None and mcu > 0:
            pe_u = cf / mcu
            r["punto_equilibrio_unidades"] = round(pe_u, 1)
            r["punto_equilibrio_clp"] = round(pe_u * p, 0)
        elif cf is None:
            faltan.append("costos_fijos_mensuales (para punto de equilibrio)")

    if cac is None:
        faltan.append("cac_clp (para payback / LTV-CAC)")

    r["faltan_entradas"] = faltan
    return r


# ---------- Proyeccion financiera (EVAL_P4) ----------
def proyeccion(precio_unitario, costo_variable_unitario, costos_fijos_mensuales,
               unidades_ano_1, crecimiento_anual_pct, horizonte_anios) -> list[dict]:
    """Proyeccion anual simple: las unidades crecen a tasa constante; ingresos y
    costos se derivan de los unit economics.

    SUPUESTO v1 (POR VALIDAR): precio_unitario y costo_variable_unitario se toman
    como el ingreso / costo variable ANUAL por unidad activa. Si el modelo es
    mensual, el caller anualiza (x12) antes de llamar. costos_fijos_mensuales se
    anualiza aqui (x12).
    """
    p = _num(precio_unitario) or 0.0
    cv = _num(costo_variable_unitario) or 0.0
    cf = (_num(costos_fijos_mensuales) or 0.0) * 12
    u = _num(unidades_ano_1) or 0.0
    g = (_num(crecimiento_anual_pct) or 0.0) / 100.0
    n = int(_num(horizonte_anios) or 0)

    filas = []
    for anio in range(1, n + 1):
        unidades = u * ((1 + g) ** (anio - 1))
        ingresos = unidades * p
        costos = unidades * cv + cf
        filas.append({
            "anio": anio,
            "unidades": round(unidades, 1),
            "ingresos_clp": round(ingresos, 0),
            "costos_clp": round(costos, 0),
            "resultado_clp": round(ingresos - costos, 0),
        })
    return filas


def proyeccion_escenarios(unit_in: dict, escenarios: list[dict], horizonte_anios: int) -> list[dict]:
    """Corre proyeccion() para cada escenario y le adjunta su tabla anual (`anios`).

    unit_in: {precio_unitario, costo_variable_unitario, costos_fijos_mensuales}
    escenarios: lista de {nombre, unidades_ano_1, crecimiento_anual_pct, ...}
    """
    salida = []
    for e in escenarios or []:
        filas = proyeccion(
            unit_in.get("precio_unitario"), unit_in.get("costo_variable_unitario"),
            unit_in.get("costos_fijos_mensuales"),
            e.get("unidades_ano_1"), e.get("crecimiento_anual_pct"), horizonte_anios,
        )
        salida.append({**e, "anios": filas})
    return salida


# ---------- Encaje con el mercado (EVAL_P4) ----------
def encaje_mercado(ingresos_ano_final_clp=None, som_clp=None) -> dict:
    """Cruza los ingresos proyectados del ultimo anio (escenario base) con el SOM.

    penetracion_som_pct > 1.0 = la proyeccion no cabe en el mercado obtenible
    estimado; hay que revisar la proyeccion o el SOM.
    """
    ing = _num(ingresos_ano_final_clp)
    som = _num(som_clp)
    pen = round(ing / som, 4) if (ing is not None and som) else None
    if pen is None:
        estado = "sin_dato"
    elif pen > UMBRALES["penetracion_som_pct_critico"]:
        estado = "critico"
    elif pen > UMBRALES["penetracion_som_pct_alerta"]:
        estado = "alerta"
    else:
        estado = "ok"
    return {
        "ingresos_ano_final_base_clp": ing,
        "som_clp": som,
        "penetracion_som_pct": pen,
        "estado": estado,
    }


# ---------- Indicadores de viabilidad (EVAL_P5) ----------
def _fila(indicador, valor, umbral, estado):
    return {"indicador": indicador, "valor": valor, "umbral": umbral, "estado": estado}


def indicadores_viabilidad(ue: dict, enc: dict | None = None) -> list[dict]:
    """Evalua cada indicador clave contra su umbral (de parametros.json).

    ue: salida de unit_economics(). enc: salida de encaje_mercado() (opcional).
    Estados: ok | alerta | critico | sin_dato.
    """
    out = []
    mcu = ue.get("margen_contribucion_unitario")

    # Margen de contribucion %
    mc = ue.get("margen_contribucion_pct")
    u_mc = UMBRALES["margen_contribucion_pct_min"]
    if mc is None:
        out.append(_fila("margen_contribucion_pct", None, f">= {u_mc:.0%}", "sin_dato"))
    elif mc <= 0:
        out.append(_fila("margen_contribucion_pct", mc, f">= {u_mc:.0%}", "critico"))
    elif mc < u_mc:
        out.append(_fila("margen_contribucion_pct", mc, f">= {u_mc:.0%}", "alerta"))
    else:
        out.append(_fila("margen_contribucion_pct", mc, f">= {u_mc:.0%}", "ok"))

    # LTV / CAC
    ratio = ue.get("ltv_cac_ratio")
    u_r = UMBRALES["ltv_cac_ratio_min"]
    if ratio is None:
        out.append(_fila("ltv_cac_ratio", None, f">= {u_r}", "sin_dato"))
    elif ratio < 1:
        out.append(_fila("ltv_cac_ratio", ratio, f">= {u_r}", "critico"))
    elif ratio < u_r:
        out.append(_fila("ltv_cac_ratio", ratio, f">= {u_r}", "alerta"))
    else:
        out.append(_fila("ltv_cac_ratio", ratio, f">= {u_r}", "ok"))

    # Payback de CAC
    pb = ue.get("payback_cac_meses")
    u_pb = UMBRALES["payback_cac_meses_max"]
    if pb is None and mcu is not None and mcu <= 0:
        out.append(_fila("payback_cac_meses", None, f"<= {u_pb}", "critico"))
    elif pb is None:
        out.append(_fila("payback_cac_meses", None, f"<= {u_pb}", "sin_dato"))
    elif pb > 2 * u_pb:
        out.append(_fila("payback_cac_meses", pb, f"<= {u_pb}", "critico"))
    elif pb > u_pb:
        out.append(_fila("payback_cac_meses", pb, f"<= {u_pb}", "alerta"))
    else:
        out.append(_fila("payback_cac_meses", pb, f"<= {u_pb}", "ok"))

    # Penetracion de SOM (si hay encaje)
    if enc:
        out.append(_fila("penetracion_som_pct", enc.get("penetracion_som_pct"),
                         f"<= {UMBRALES['penetracion_som_pct_alerta']:.0%}",
                         enc.get("estado", "sin_dato")))
    return out


# ---------- Compuerta de viabilidad (EVAL_P5) ----------
def compuerta_viabilidad(indicadores: list[dict], info_suficiente: bool = True,
                         punto_equilibrio_clp=None, som_clp=None,
                         resultado_optimista_final_clp=None) -> dict:
    """Decision de flujo tras la revision del modelo. Determinista; no la decide el LLM.

    Reglas (v1, POR VALIDAR con ingenieria comercial):
      DEVOLVER  -> info_suficiente es False (faltan datos del cliente para evaluar).
      INVIABLE  -> el modelo no cierra ni en el mejor caso razonable:
                     - punto de equilibrio > SOM (no se alcanza dentro del mercado
                       obtenible), o
                     - el resultado del ultimo anio del escenario OPTIMISTA es < 0.
      AJUSTAR   -> hay indicadores 'critico'/'alerta' o falta dato, pero el modelo
                   podria cerrar moviendo palancas (pricing, segmento, canal, costos).
      SOLIDO    -> todos los indicadores con dato estan 'ok'.

    Returns: {compuerta, motivos, criticos, alertas, sin_dato}.
    """
    if info_suficiente is False:
        return {"compuerta": "DEVOLVER",
                "motivos": ["Informacion insuficiente del cliente para evaluar el modelo."],
                "criticos": [], "alertas": [], "sin_dato": []}

    criticos = [i["indicador"] for i in indicadores if i.get("estado") == "critico"]
    alertas = [i["indicador"] for i in indicadores if i.get("estado") == "alerta"]
    sin_dato = [i["indicador"] for i in indicadores if i.get("estado") == "sin_dato"]

    pe = _num(punto_equilibrio_clp)
    som = _num(som_clp)
    opt = _num(resultado_optimista_final_clp)
    motivos: list[str] = []
    inviable = False
    if pe is not None and som is not None and pe > som:
        inviable = True
        motivos.append(f"El punto de equilibrio (${pe:,.0f}) supera el mercado obtenible SOM "
                       f"(${som:,.0f}): el modelo no cubre sus costos fijos dentro del mercado alcanzable.")
    if opt is not None and opt < 0:
        inviable = True
        motivos.append("Incluso el escenario optimista termina con resultado negativo en el ultimo anio.")
    if inviable:
        return {"compuerta": "INVIABLE", "motivos": motivos,
                "criticos": criticos, "alertas": alertas, "sin_dato": sin_dato}

    if criticos or alertas or sin_dato:
        detalle = []
        if criticos:
            detalle.append("criticos: " + ", ".join(criticos))
        if alertas:
            detalle.append("alertas: " + ", ".join(alertas))
        if sin_dato:
            detalle.append("sin dato: " + ", ".join(sin_dato))
        motivos.append("; ".join(detalle) + ". Revisar palancas (pricing, segmento, canal, "
                       "estructura de costos) y/o completar datos, y re-evaluar (EVAL_P4).")
        return {"compuerta": "AJUSTAR", "motivos": motivos,
                "criticos": criticos, "alertas": alertas, "sin_dato": sin_dato}

    return {"compuerta": "SÓLIDO",
            "motivos": ["Todos los indicadores dentro de umbral."],
            "criticos": [], "alertas": [], "sin_dato": []}


# ---------- QA de coherencia de cifras del cliente ----------
def coherencia_cifras_cliente(cifras: list[dict]) -> list[dict]:
    """Detecta inconsistencias entre las cifras DECLARADAS por el cliente en
    distintos bloques/documentos (nro de clientes, precio, ticket, volumen...).

    A diferencia del QA de veracidad (que verifica fuentes EXTERNAS de mercado),
    esto chequea la consistencia INTERNA de los datos del propio cliente. El motor
    no corrige ni silencia: expone la discrepancia como alerta.

    Args:
        cifras: lista de {concepto, valor, unidad?, fuente}.

    Returns:
        lista de {concepto, unidad, estado ('ok'|'alerta'), detalle}, una por
        (concepto, unidad).
    """
    from collections import defaultdict
    grupos: dict = defaultdict(list)
    for c in cifras or []:
        clave = ((c.get("concepto") or "").strip().lower(), (str(c.get("unidad") or "")).strip().lower())
        grupos[clave].append(c)
    out = []
    for (concepto, unidad), items in grupos.items():
        valores: dict = defaultdict(list)
        for it in items:
            valores[it.get("valor")].append(str(it.get("fuente") or "—"))
        if len(valores) > 1:
            detalle = "; ".join(f"{v} (segun {', '.join(fs)})" for v, fs in valores.items())
            out.append({"concepto": concepto or "—", "unidad": unidad, "estado": "alerta",
                        "detalle": f"Valores inconsistentes para el mismo concepto: {detalle}"})
        else:
            out.append({"concepto": concepto or "—", "unidad": unidad, "estado": "ok",
                        "detalle": f"Consistente ({len(items)} referencia(s))."})
    return out


# ---------- QA de coherencia del modelo / Fase 2 (FORM_W5) ----------
def _regla_semantica(nombre: str, confirmado: bool | None, detalle: str) -> dict:
    """Regla que el motor NO puede juzgar por si solo; depende de confirmacion del agente."""
    if confirmado is True:
        return {"regla": nombre, "estado": "ok", "detalle": detalle + " (confirmado)"}
    if confirmado is False:
        return {"regla": nombre, "estado": "alerta", "detalle": detalle + " (NO se cumple)"}
    return {"regla": nombre, "estado": "pendiente", "detalle": detalle + " (requiere confirmacion)"}


def qa_coherencia_modelo(*, mercado: dict | None = None,
                         penetracion_som_pct: float | None = None,
                         supuestos: list[dict] | None = None,
                         supuestos_a_confirmar: list[dict] | None = None,
                         secciones_formulario: list[dict] | None = None,
                         cifras_formulario_cuadran: bool | None = None) -> list[dict]:
    """Reglas de coherencia de la Fase 2 (FORM_W5). Deterministas 1-4; semantica 5.

    Args:
        mercado: {tam_clp, sam_clp, som_clp} para el chequeo del embudo.
        penetracion_som_pct: ingresos ultimo anio (base) / SOM.
        supuestos: supuestos_modelo.supuestos (cada uno {supuesto, confirmado}).
        supuestos_a_confirmar: impacto_continuidad.supuestos_a_confirmar.
        secciones_formulario: formulario_oficial.secciones (usa el flag dentro_limite).
        cifras_formulario_cuadran: el agente confirma que los numeros citados en el
            formulario coinciden con modelo_negocio.
    """
    out = []

    # Regla 1: embudo de mercado coherente
    mc = mercado_coherencia(**(mercado or {})) if mercado else None
    if mc is None:
        out.append({"regla": "1. Embudo de mercado (TAM>=SAM>=SOM)", "estado": "pendiente",
                    "detalle": "Sin cifras de mercado."})
    elif mc["alertas"]:
        out.append({"regla": "1. Embudo de mercado (TAM>=SAM>=SOM)", "estado": "alerta",
                    "detalle": " ".join(mc["alertas"])})
    elif mc["faltan"]:
        out.append({"regla": "1. Embudo de mercado (TAM>=SAM>=SOM)", "estado": "pendiente",
                    "detalle": "Faltan: " + ", ".join(mc["faltan"])})
    else:
        out.append({"regla": "1. Embudo de mercado (TAM>=SAM>=SOM)", "estado": "ok",
                    "detalle": "SOM <= SAM <= TAM."})

    # Regla 2: la proyeccion cabe en el mercado obtenible
    p = _num(penetracion_som_pct)
    if p is None:
        out.append({"regla": "2. Proyeccion vs SOM", "estado": "pendiente",
                    "detalle": "Sin penetracion de SOM calculada."})
    elif p > UMBRALES["penetracion_som_pct_critico"]:
        out.append({"regla": "2. Proyeccion vs SOM", "estado": "alerta",
                    "detalle": f"La proyeccion captura {p:.0%} del SOM: no cabe en el mercado obtenible estimado."})
    else:
        out.append({"regla": "2. Proyeccion vs SOM", "estado": "ok",
                    "detalle": f"Proyeccion = {p:.0%} del SOM."})

    # Regla 3: los supuestos sin confirmar quedan registrados para confirmar
    no_conf = [s.get("supuesto") for s in (supuestos or []) if s.get("confirmado") is False]
    registrados = {s.get("supuesto") for s in (supuestos_a_confirmar or [])}
    sin_registrar = [s for s in no_conf if s and s not in registrados]
    if not no_conf:
        out.append({"regla": "3. Supuestos sin confirmar registrados", "estado": "ok",
                    "detalle": "No hay supuestos pendientes, o todos estan confirmados."})
    elif sin_registrar:
        out.append({"regla": "3. Supuestos sin confirmar registrados", "estado": "alerta",
                    "detalle": f"{len(sin_registrar)} supuesto(s) sin confirmar fuera de supuestos_a_confirmar: "
                               + "; ".join(str(s) for s in sin_registrar[:5])})
    else:
        out.append({"regla": "3. Supuestos sin confirmar registrados", "estado": "ok",
                    "detalle": f"{len(no_conf)} supuesto(s) pendiente(s), todos registrados."})

    # Regla 4: respuestas dentro del limite de caracteres
    secs = secciones_formulario or []
    fuera = [s.get("id") for s in secs if s.get("dentro_limite") is False]
    sin_chequear = [s.get("id") for s in secs if s.get("dentro_limite") is None]
    if not secs:
        out.append({"regla": "4. Limite de caracteres por seccion", "estado": "pendiente",
                    "detalle": "Sin secciones redactadas."})
    elif fuera:
        out.append({"regla": "4. Limite de caracteres por seccion", "estado": "alerta",
                    "detalle": "Secciones sobre el tope: " + ", ".join(str(x) for x in fuera)})
    elif sin_chequear:
        out.append({"regla": "4. Limite de caracteres por seccion", "estado": "pendiente",
                    "detalle": "Sin chequear (dentro_limite) en: " + ", ".join(str(x) for x in sin_chequear)})
    else:
        out.append({"regla": "4. Limite de caracteres por seccion", "estado": "ok",
                    "detalle": "Todas dentro del tope."})

    # Regla 5: las cifras del formulario cuadran con el modelo (semantica)
    out.append(_regla_semantica("5. Cifras del formulario vs modelo", cifras_formulario_cuadran,
               "Los numeros citados en el formulario (mercado, precio, proyeccion) deben coincidir con modelo_negocio."))
    return out


# ---------- autotest ----------
def _test() -> None:
    # --- Mercado ---
    assert mercado_coherencia(tam_clp=1_000_000_000, sam_clp=300_000_000, som_clp=30_000_000)["ok"] is True
    assert mercado_coherencia(tam_clp=100, sam_clp=200)["alertas"], "SAM>TAM debe alertar"
    assert mercado_coherencia(som_clp=10)["faltan"] == ["TAM", "SAM"]

    # --- Unit economics (precio 100k, cv 40k, fijos 5M/mes, CAC 120k, vida 24m) ---
    ue = unit_economics(precio_unitario=100_000, costo_variable_unitario=40_000,
                        costos_fijos_mensuales=5_000_000, cac_clp=120_000, vida_cliente_meses=24)
    assert ue["margen_contribucion_unitario"] == 60_000
    assert ue["margen_contribucion_pct"] == 0.6
    assert ue["ltv_clp"] == 60_000 * 24
    assert ue["ltv_cac_ratio"] == round((60_000 * 24) / 120_000, 2)   # 12.0
    assert ue["payback_cac_meses"] == 2.0
    assert ue["punto_equilibrio_unidades"] == round(5_000_000 / 60_000, 1)
    assert ue["punto_equilibrio_clp"] == round((5_000_000 / 60_000) * 100_000, 0)
    assert not ue["faltan_entradas"], ue["faltan_entradas"]

    # margen negativo: sin payback, sin punto de equilibrio
    ue_neg = unit_economics(precio_unitario=100, costo_variable_unitario=150,
                            costos_fijos_mensuales=1000, cac_clp=50)
    assert ue_neg["margen_contribucion_unitario"] == -50
    assert ue_neg["payback_cac_meses"] is None
    assert ue_neg["punto_equilibrio_unidades"] is None

    # faltan entradas
    assert "cac_clp (para payback / LTV-CAC)" in unit_economics(precio_unitario=100, costo_variable_unitario=40)["faltan_entradas"]

    # --- Proyeccion (100 u anio 1, +20%/anio, 3 anios) ---
    filas = proyeccion(precio_unitario=1_000_000, costo_variable_unitario=400_000,
                       costos_fijos_mensuales=2_000_000, unidades_ano_1=100,
                       crecimiento_anual_pct=20, horizonte_anios=3)
    assert len(filas) == 3
    assert filas[0]["unidades"] == 100.0
    assert filas[0]["ingresos_clp"] == 100_000_000
    assert filas[0]["costos_clp"] == 100 * 400_000 + 24_000_000   # 64M
    assert filas[0]["resultado_clp"] == 36_000_000
    assert filas[2]["unidades"] == round(100 * 1.2 ** 2, 1)       # 144.0

    esc = proyeccion_escenarios(
        {"precio_unitario": 1_000_000, "costo_variable_unitario": 400_000, "costos_fijos_mensuales": 2_000_000},
        [{"nombre": "base", "unidades_ano_1": 100, "crecimiento_anual_pct": 20}], 3)
    assert esc[0]["nombre"] == "base" and len(esc[0]["anios"]) == 3

    # --- Encaje con el mercado ---
    assert encaje_mercado(ingresos_ano_final_clp=200_000_000, som_clp=1_000_000_000) == \
        {"ingresos_ano_final_base_clp": 200_000_000.0, "som_clp": 1_000_000_000.0,
         "penetracion_som_pct": 0.2, "estado": "ok"}
    assert encaje_mercado(ingresos_ano_final_clp=1_200, som_clp=1_000)["estado"] == "critico"
    assert encaje_mercado(ingresos_ano_final_clp=300, som_clp=1_000)["estado"] == "alerta"

    # --- Indicadores + compuerta ---
    enc_ok = encaje_mercado(200_000_000, 1_000_000_000)
    ind_ok = indicadores_viabilidad(ue, enc_ok)
    estados = {i["indicador"]: i["estado"] for i in ind_ok}
    assert estados == {"margen_contribucion_pct": "ok", "ltv_cac_ratio": "ok",
                       "payback_cac_meses": "ok", "penetracion_som_pct": "ok"}, estados
    g_ok = compuerta_viabilidad(ind_ok, info_suficiente=True,
                                punto_equilibrio_clp=ue["punto_equilibrio_clp"],
                                som_clp=1_000_000_000, resultado_optimista_final_clp=50_000_000)
    assert g_ok["compuerta"] == "SÓLIDO", g_ok

    # DEVOLVER
    assert compuerta_viabilidad([], info_suficiente=False)["compuerta"] == "DEVOLVER"

    # AJUSTAR: margen bajo el umbral (20% < 30%), LTV/CAC bajo
    ue_bajo = unit_economics(precio_unitario=100_000, costo_variable_unitario=80_000,
                             costos_fijos_mensuales=5_000_000, cac_clp=500_000, vida_cliente_meses=6)
    ind_bajo = indicadores_viabilidad(ue_bajo)
    g_aj = compuerta_viabilidad(ind_bajo, info_suficiente=True,
                                punto_equilibrio_clp=ue_bajo["punto_equilibrio_clp"],
                                som_clp=10_000_000_000, resultado_optimista_final_clp=1)
    assert g_aj["compuerta"] == "AJUSTAR", g_aj

    # INVIABLE: punto de equilibrio > SOM
    assert compuerta_viabilidad(ind_ok, info_suficiente=True, punto_equilibrio_clp=5_000_000_000,
                                som_clp=100_000_000, resultado_optimista_final_clp=10)["compuerta"] == "INVIABLE"
    # INVIABLE: optimista negativo
    assert compuerta_viabilidad(ind_ok, info_suficiente=True,
                                resultado_optimista_final_clp=-1)["compuerta"] == "INVIABLE"

    # --- Coherencia de cifras del cliente ---
    cc = {c["concepto"]: c for c in coherencia_cifras_cliente([
        {"concepto": "clientes_actuales", "valor": 12, "unidad": "empresas", "fuente": "reunion-1"},
        {"concepto": "clientes_actuales", "valor": 8, "unidad": "empresas", "fuente": "pitch.pdf"},
        {"concepto": "precio", "valor": 100000, "unidad": "clp", "fuente": "reunion-2"}])}
    assert cc["clientes_actuales"]["estado"] == "alerta" and cc["precio"]["estado"] == "ok"

    # --- QA de coherencia del modelo (FORM_W5) ---
    qa = {r["regla"][0]: r for r in qa_coherencia_modelo(
        mercado={"tam_clp": 1_000_000_000, "sam_clp": 300_000_000, "som_clp": 30_000_000},
        penetracion_som_pct=1.5,
        supuestos=[{"supuesto": "precio 100k", "confirmado": False}],
        supuestos_a_confirmar=[],
        secciones_formulario=[{"id": "mercado_objetivo", "dentro_limite": False}],
        cifras_formulario_cuadran=True)}
    assert qa["1"]["estado"] == "ok"        # embudo coherente
    assert qa["2"]["estado"] == "alerta"    # proyeccion 150% del SOM
    assert qa["3"]["estado"] == "alerta"    # supuesto sin registrar
    assert qa["4"]["estado"] == "alerta"    # seccion sobre el tope
    assert qa["5"]["estado"] == "ok"        # confirmado

    print("OK: motor de reglas (modelo de negocio) — todos los asserts pasan.")


def _demo() -> None:
    # unit economics: valores MENSUALES por cliente (modelo de suscripcion)
    ue = unit_economics(precio_unitario=100_000, costo_variable_unitario=40_000,
                        costos_fijos_mensuales=5_000_000, cac_clp=120_000, vida_cliente_meses=24)
    print("Unit economics:", json.dumps(ue, ensure_ascii=False, indent=2))
    # proyeccion: se anualiza el ingreso/costo por cliente activo (x12), como pide proyeccion()
    filas = proyeccion(precio_unitario=100_000 * 12, costo_variable_unitario=40_000 * 12,
                       costos_fijos_mensuales=5_000_000, unidades_ano_1=200,
                       crecimiento_anual_pct=30, horizonte_anios=5)
    print("\nProyeccion (base):")
    for f in filas:
        print(f"  anio {f['anio']}: {f['unidades']:.0f} u  ->  ingresos {f['ingresos_clp']:,.0f}  /  "
              f"resultado {f['resultado_clp']:,.0f}")
    enc = encaje_mercado(filas[-1]["ingresos_clp"], som_clp=2_000_000_000)
    ind = indicadores_viabilidad(ue, enc)
    print("\nIndicadores:", json.dumps(ind, ensure_ascii=False, indent=2))
    g = compuerta_viabilidad(ind, punto_equilibrio_clp=ue["punto_equilibrio_clp"],
                             som_clp=2_000_000_000, resultado_optimista_final_clp=filas[-1]["resultado_clp"])
    print("\nCompuerta:", json.dumps(g, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if "--demo" in sys.argv:
        _demo()
    else:
        _test()
