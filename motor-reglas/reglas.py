#!/usr/bin/env python3
"""Motor de reglas determinista del sistema GTF.

Parte NO generativa: cálculos exactos y repetibles que no deben quedar a criterio
del LLM. Cubre la clasificación Frascati, la elegibilidad Ley I+D, la selección de
instrumentos CORFO y la compuerta GO/PIVOT/NO-GO.

Datos en `instrumentos.json` (mismo directorio). Sin dependencias externas.

Uso como CLI:
    python3 motor-reglas/reglas.py --test     # autotest (asserts)
    python3 motor-reglas/reglas.py --demo      # demo con un caso
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

DATA = json.loads((Path(__file__).resolve().parent / "instrumentos.json").read_text(encoding="utf-8"))


# ---------- Frascati (EVAL_P4-II) ----------
# Exclusiones de la Ley I+D (Frascati): categorías que NO son I+D. Por defecto (C1),
# antes de afirmar es_id el caso se contrasta contra ellas; cada componente I/D
# afirmado debe nombrar qué exclusión sortea, con sustento del estado del arte.
EXCLUSIONES_LEY_ID = [
    "adaptacion_rutinaria",          # ajustar/parametrizar algo existente sin incógnita
    "ingenieria_estandar",           # resoluble por un profesional calificado sin experimentar
    "adquisicion_puesta_en_marcha",  # comprar e instalar tecnología existente
    "validacion_medicion_comercial", # ensayos/mediciones de rutina, control de calidad
    "novedad_solo_local",            # nuevo para la empresa/país, no para el estado del arte
]


def evaluar_exclusiones(exclusiones: list[dict] | None) -> dict:
    """Contrasta el caso contra las exclusiones de la Ley I+D (prueba previa a es_id).

    Solo 'sorteada' CON sustento deja atrás una exclusión. Todo lo demás la deja
    abierta — pero no todo lo abierto significa lo mismo, y el motor lo distingue
    porque de eso depende qué puede hacer el consultor después:

      · 'aplica'    → FLANCO REAL: el caso cae ahí. Se resuelve REENCUADRANDO el
                      proyecto (ver `reencuadre_elegibilidad`), no indagando más.
      · 'pendiente' → NO SE INDAGÓ todavía. No es un no: es un dato que falta.
                      Se resuelve investigando o preguntando al cliente.
      · faltante    → ni siquiera se listó la exclusión.
      · sin sustento→ se declaró sorteada sin respaldo del estado del arte.

    Un veredicto negativo NUNCA es terminal: `bloqueos` dice qué está abierto y
    `como_destrabar` qué haría falta para cerrarlo. El equipo consultor decide si
    invierte en cerrarlo, si reencuadra o si lo deja.

    Args:
        exclusiones: lista de {exclusion, veredicto, sustento}. veredicto ∈
            {'sorteada','aplica','pendiente'}.

    Returns:
        dict con todas_sorteadas (bool), el detalle por categoría y la guía de
        destrabe.
    """
    items = exclusiones or []
    dadas = {(x.get("exclusion") or "").strip() for x in items}
    faltantes = [e for e in EXCLUSIONES_LEY_ID if e not in dadas]
    aplican = [x.get("exclusion") for x in items if x.get("veredicto") == "aplica"]
    pendientes = [x.get("exclusion") for x in items if x.get("veredicto") == "pendiente"]
    sin_sustento = [x.get("exclusion") for x in items
                    if x.get("veredicto") == "sorteada" and not (x.get("sustento") or "").strip()]
    # Una exclusión queda atrás SOLO si fue sorteada con sustento. 'pendiente' no cierra nada.
    todas = not faltantes and not aplican and not pendientes and not sin_sustento

    como_destrabar = []
    if aplican:
        como_destrabar.append(
            f"REENCUADRE (no más análisis): el caso cae en {', '.join(aplican)}. Indagar más no lo cambia — "
            "hay que cambiar el alcance. Ver `reencuadre_elegibilidad`: desarrollar en vez de comprar, socio "
            "académico, agregar un estudio financiable, o mover lo incierto a una fase posterior.")
    if pendientes:
        como_destrabar.append(
            f"INDAGAR: {', '.join(pendientes)} sin resolver. NO es un rechazo — es información que falta. "
            "Se cierra con estado del arte o con un dato del cliente.")
    if faltantes:
        como_destrabar.append(
            f"EVALUAR: {', '.join(faltantes)} ni siquiera se contrastó. La prueba de exclusiones es completa o no vale.")
    if sin_sustento:
        como_destrabar.append(
            f"SUSTENTAR: {', '.join(sin_sustento)} se declaró sorteada sin respaldo. Citar el estado del arte.")

    return {"todas_sorteadas": todas,
            "exclusiones_faltantes": faltantes,
            "exclusiones_que_aplican": aplican,
            "exclusiones_pendientes": pendientes,
            "sorteadas_sin_sustento": sin_sustento,
            "bloqueos": {"por_flanco_real": aplican, "por_falta_de_indagacion": pendientes,
                         "por_no_evaluadas": faltantes, "por_falta_de_sustento": sin_sustento},
            "como_destrabar": como_destrabar}


def frascati(componente_i: bool, componente_d: bool,
             exclusiones: list[dict] | None = None) -> dict:
    """Clasifica la naturaleza I+D según la matriz 2x2 de Frascati.

    Args:
        componente_i: cumple "I" (genera nuevo conocimiento / uso no trivial).
        componente_d: cumple "D" (resultado técnico incierto / experimentación).
        exclusiones: prueba de exclusiones (C1). Si se pasa, es_id solo es
            DEFENDIBLE cuando todas las exclusiones fueron sorteadas con sustento;
            un es_id afirmado que cae en una exclusión es un falso positivo.

    Returns:
        dict con cuadrante, es_id (bool), elegibilidad y —si hubo exclusiones—
        el veredicto de la prueba, es_id_defendible y `defendibilidad`.

    `es_id_defendible=False` NO es un veredicto final sobre el proyecto: es el
    estado del EXPEDIENTE hoy. `defendibilidad.estado` dice de qué tipo es el
    bloqueo y `defendibilidad.siguiente_paso` qué haría falta, porque el equipo
    consultor puede querer seguir analizando o buscar un reencuadre antes de
    descartar el caso:
      · 'defendible'            → las cinco sorteadas con sustento.
      · 'incompleto'            → falta indagar/sustentar. Se cierra con trabajo.
      · 'requiere_reencuadre'   → hay un flanco real; más análisis no lo mueve.
      · 'sin_id'                → no se afirmó ni I ni D.
    """
    es_id = bool(componente_i or componente_d)
    if componente_i and componente_d:
        cuadrante, elegibilidad = "I+D", "Alto"
    elif componente_i:
        cuadrante, elegibilidad = "Solo I", "Medio-Alto"
    elif componente_d:
        cuadrante, elegibilidad = "Solo D", "Medio-Alto"
    else:
        cuadrante, elegibilidad = "Sin I-D", "Cero"
    resultado = {"cuadrante": cuadrante, "es_id": es_id, "elegibilidad_ley_id": elegibilidad}
    if exclusiones is not None:
        veredicto = evaluar_exclusiones(exclusiones)
        resultado["exclusiones"] = veredicto
        defendible = bool(es_id and veredicto["todas_sorteadas"])
        resultado["es_id_defendible"] = defendible
        # Un `False` no cierra el caso: dice qué tipo de bloqueo hay y por dónde seguir.
        if not es_id:
            estado, paso = "sin_id", ("No se afirmó componente I ni D. Revisar si el alcance actual esconde "
                                      "incertidumbre técnica, o si conviene reencuadrar el proyecto.")
        elif defendible:
            estado, paso = "defendible", "Las cinco exclusiones sorteadas con sustento. El caso se sostiene."
        elif veredicto["exclusiones_que_aplican"]:
            estado, paso = "requiere_reencuadre", ("Hay un flanco real: más análisis no lo mueve. Trabajar "
                                                   "`reencuadre_elegibilidad` con el consultor antes de descartar.")
        else:
            estado, paso = "incompleto", ("El expediente está incompleto, no rechazado. Se cierra indagando, "
                                          "sustentando o pidiendo el dato al cliente.")
        resultado["defendibilidad"] = {"estado": estado, "siguiente_paso": paso,
                                       "como_destrabar": veredicto["como_destrabar"]}
    return resultado


# ---------- Elegibilidad Ley I+D ----------
def ley_id_elegible(contabilidad: str, trl: int | None, presupuesto_clp: float | None = None) -> dict:
    """Evalúa requisitos duros de la empresa/proyecto para la Ley I+D."""
    cfg = DATA["ley_id"]
    motivos = []
    if (contabilidad or "").strip().lower() != cfg["contabilidad_requerida"]:
        motivos.append(f"Requiere contabilidad {cfg['contabilidad_requerida']} (declarada: {contabilidad or '—'}).")
    if trl is not None and trl > cfg["trl_maximo"]:
        motivos.append(f"TRL {trl} > máximo {cfg['trl_maximo']}: Ley I+D no cubre validación comercial (TRL 8-9).")
    if presupuesto_clp is not None and presupuesto_clp < cfg["presupuesto_minimo_clp"]:
        motivos.append(f"Presupuesto ${presupuesto_clp:,.0f} < mínimo GT ${cfg['presupuesto_minimo_clp']:,.0f} (práctica de elegibilidad GT).")
    return {"elegible": not motivos, "motivos": motivos,
            "credito_pct": cfg["credito_tributario_pct"], "tope_anual_utm": cfg["tope_anual_utm"],
            "regla_facturacion": cfg["regla_facturacion"]}


# ---------- Instrumentos CORFO ----------
def cofinanciamiento(instrumento: dict, tamano: str, lidera_mujer: bool = False) -> float:
    """% de cofinanciamiento CORFO para un instrumento según tamaño de empresa."""
    base = instrumento["cofinanciamiento"].get(tamano)
    if base is None:
        raise ValueError(f"Tamaño de empresa inválido: {tamano}")
    return round(min(base + (instrumento["bono_mujer_pct"] if lidera_mujer else 0.0), 1.0), 3)


def instrumentos_elegibles(trl: int | None, tamano: str, antiguedad_meses: int,
                           lidera_mujer: bool = False) -> list[dict]:
    """Cruza el proyecto con cada instrumento y devuelve su elegibilidad + parámetros."""
    salida = []
    for ins in DATA["instrumentos"]:
        motivos = []
        if ins["trl_min"] is not None and (trl is None or trl < ins["trl_min"]):
            motivos.append(f"TRL {trl} < {ins['trl_min']} requerido")
        if antiguedad_meses < ins["antiguedad_meses_min"]:
            motivos.append(f"Antigüedad {antiguedad_meses}m < {ins['antiguedad_meses_min']}m requeridos")
        tope_key = "tope_subsidio_mujer_clp" if lidera_mujer else "tope_subsidio_clp"
        salida.append({
            "id": ins["id"], "nombre": ins["nombre"], "elegible": not motivos,
            "motivos": motivos,
            "cofinanciamiento_pct": cofinanciamiento(ins, tamano, lidera_mujer),
            "tope_subsidio_clp": ins.get(tope_key, ins["tope_subsidio_clp"]),
            "plazo_meses_max": ins["plazo_meses_max"],
        })
    return salida


# ---------- Arancel de postulación (FORM_W4/W5) ----------
def arancel(utm_proyecto: float) -> dict:
    """Arancel de postulación Ley I+D según la escala por tramos (tope 30 UTM).

    Args:
        utm_proyecto: tamaño del proyecto en UTM (= costo_total_clp / valor_utm_clp).

    Returns:
        dict con arancel_utm, arancel_clp, el tramo aplicado y el valor UTM usado.
    """
    cfg = DATA["ley_id"]["arancel"]
    tramo = cfg["tramos"][-1]
    for t in cfg["tramos"]:
        if t["hasta_utm"] is None or utm_proyecto <= t["hasta_utm"]:
            tramo = t
            break
    bruto = tramo["base_utm"] + max(0.0, utm_proyecto - tramo["excedente_sobre_utm"]) * tramo["tasa"]
    arancel_utm = round(min(bruto, cfg["tope_utm"]), 2)
    return {
        "arancel_utm": arancel_utm,
        "arancel_clp": round(arancel_utm * cfg["valor_utm_clp"]),
        "utm_proyecto": round(utm_proyecto, 2),
        "valor_utm_clp": cfg["valor_utm_clp"],
        "tramo_utm": f"{tramo['desde_utm']}–{tramo['hasta_utm'] or '∞'}",
    }


# ---------- Compuerta (EVAL_P5) ----------
def compuerta(es_id: bool, voto_comite: str, info_suficiente: bool = True) -> str:
    """Decisión de flujo tras el Comité. Determinista; no la decide el LLM.

    Args:
        es_id: naturaleza I+D del caso.
        voto_comite: voto del comité.
        info_suficiente: si es False, el comité no pudo resolver por entendimiento
            incompleto (típicamente del modelo de negocio, no del estado del arte).

    Returns: 'GO' | 'PIVOT' | 'NO-GO' | 'DEVOLVER'.

    DEVOLVER (C6) tiene prioridad: sin entender el caso no se puede resolver; el
    orquestador rutea a una **reunión con el cliente**, NO a un nuevo Deep Research
    (eso es PIVOT).
    """
    if info_suficiente is False:
        return "DEVOLVER"
    voto = (voto_comite or "").strip().lower()
    if not es_id:
        return "NO-GO"
    if voto in ("aprobado i+d", "aprobado", "go"):
        return "GO"
    if voto in ("condicionado a ajustes", "condicionado", "pivot"):
        return "PIVOT"
    return "NO-GO"


# ---------- QA de coherencia de cifras del cliente (C5) ----------
def coherencia_cifras_cliente(cifras: list[dict]) -> list[dict]:
    """Detecta inconsistencias entre las cifras DECLARADAS por el cliente en
    distintos bloques/documentos (tamaño de flota, ahorro, unidades convertibles…).

    A diferencia del QA de veracidad (que verifica fuentes EXTERNAS: papers/patentes),
    esto chequea la **consistencia interna** de los datos del propio cliente. El motor
    NO corrige ni silencia: expone la discrepancia como alerta para que el consultor
    la resuelva con el cliente.

    Args:
        cifras: lista de {concepto, valor, unidad?, fuente}. `fuente` = de dónde
            salió el dato (p.ej. 'reunion-1', 'propuesta.pdf', 'eval_p3').

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
            detalle = "; ".join(f"{v} (según {', '.join(fs)})" for v, fs in valores.items())
            out.append({"concepto": concepto or "—", "unidad": unidad, "estado": "alerta",
                        "detalle": f"Valores inconsistentes para el mismo concepto: {detalle}"})
        else:
            out.append({"concepto": concepto or "—", "unidad": unidad, "estado": "ok",
                        "detalle": f"Consistente ({len(items)} referencia(s))."})
    return out


# ---------- QA de coherencia de Formulación (FORM_W5) ----------
def _regla_semantica(nombre: str, confirmado: bool | None, detalle: str) -> dict:
    """Regla que el motor NO puede juzgar por sí solo; depende de confirmación del agente."""
    if confirmado is True:
        return {"regla": nombre, "estado": "ok", "detalle": detalle + " (confirmado)"}
    if confirmado is False:
        return {"regla": nombre, "estado": "alerta", "detalle": detalle + " (NO se cumple)"}
    return {"regla": nombre, "estado": "pendiente", "detalle": detalle + " (requiere confirmación)"}


def qa_coherencia_formulacion(*, fase_proyecto_actual: str | None = None,
                              profesional_contrato_vigente: bool | None = None,
                              profesional_id_36m: bool | None = None,
                              nuevo_conocimiento_trazable: bool | None = None,
                              incertidumbre_justificada: bool | None = None) -> list[dict]:
    """Las 4 reglas de coherencia de Formulación (Protocolo de Formulación §3).

    Reglas 1-2: deterministas con los datos dados. Reglas 3-4: semánticas (el motor
    las deja en 'pendiente' salvo confirmación explícita del agente; nunca 'ok' sin ella).
    """
    out = []
    # Regla 1: TRL vs fase del proyecto
    incoherentes = {"Producto Funcional", "Escalando en ventas"}
    if fase_proyecto_actual in incoherentes:
        out.append({"regla": "1. TRL vs fase", "estado": "alerta",
                    "detalle": f"Fase '{fase_proyecto_actual}' incoherente con Ley I+D en desarrollo (TRL 4-5); reajustar a Prototipo/Prototipo Funcional."})
    elif fase_proyecto_actual:
        out.append({"regla": "1. TRL vs fase", "estado": "ok", "detalle": f"Fase '{fase_proyecto_actual}' coherente con desarrollo."})
    else:
        out.append({"regla": "1. TRL vs fase", "estado": "pendiente", "detalle": "Falta la fase del proyecto."})
    # Regla 2: profesional acreditador (contrato vigente + I+D 36m)
    if profesional_contrato_vigente is None or profesional_id_36m is None:
        out.append({"regla": "2. Profesional acreditador", "estado": "pendiente", "detalle": "Faltan datos de contrato/experiencia I+D."})
    elif profesional_contrato_vigente and profesional_id_36m:
        out.append({"regla": "2. Profesional acreditador", "estado": "ok", "detalle": "Contrato vigente + experiencia I+D últimos 36m."})
    else:
        falta = [s for s, ok in (("contrato vigente", profesional_contrato_vigente),
                                 ("experiencia I+D 36m", profesional_id_36m)) if not ok]
        out.append({"regla": "2. Profesional acreditador", "estado": "alerta", "detalle": "Falta: " + ", ".join(falta)})
    # Reglas 3-4: semánticas
    out.append(_regla_semantica("3. Trazabilidad nuevo conocimiento", nuevo_conocimiento_trazable,
               "El nuevo conocimiento (P8) debe nacer de brechas del estado del arte (P7)."))
    out.append(_regla_semantica("4. Incertidumbre vs ingeniería estándar", incertidumbre_justificada,
               "Justificar por qué un ingeniero calificado no podría resolverlo sin experimentar (P11)."))
    return out


def _test() -> None:
    assert frascati(True, True)["cuadrante"] == "I+D"
    assert frascati(False, True)["es_id"] is True
    assert frascati(False, False) == {"cuadrante": "Sin I-D", "es_id": False, "elegibilidad_ley_id": "Cero"}
    assert ley_id_elegible("completa", 5)["elegible"] is True
    assert ley_id_elegible("simplificada", 5)["elegible"] is False
    assert ley_id_elegible("completa", 3)["elegible"] is True    # sin TRL mínimo (JP): TRL 3 elegible
    assert ley_id_elegible("completa", 8)["elegible"] is False   # TRL 8 > máx 7: validación comercial
    assert ley_id_elegible("completa", 5, presupuesto_clp=100_000_000)["elegible"] is False  # < $200M mín GT
    assert ley_id_elegible("completa", 5, presupuesto_clp=957_000_000)["elegible"] is True   # caso SRS
    ch = next(i for i in DATA["instrumentos"] if i["id"] == "capital_humano")
    assert cofinanciamiento(ch, "Pequeña") == 0.80
    assert cofinanciamiento(ch, "Grande", lidera_mujer=True) == 0.50
    el = {x["id"]: x for x in instrumentos_elegibles(trl=4, tamano="Pequeña", antiguedad_meses=20)}
    assert el["crea_valida"]["elegible"] is False          # antigüedad 20 < 24
    assert el["capital_humano"]["elegible"] is True         # 20 >= 18, sin TRL piso
    assert el["innova_alta_tecnologia"]["elegible"] is False  # antigüedad 20 < 36
    assert compuerta(True, "Aprobado I+D") == "GO"
    assert compuerta(True, "Condicionado a Ajustes") == "PIVOT"
    assert compuerta(False, "Aprobado I+D") == "NO-GO"
    # C6 · DEVOLVER (info insuficiente) tiene prioridad sobre es_id/voto
    assert compuerta(True, "Aprobado I+D", info_suficiente=False) == "DEVOLVER"
    assert compuerta(False, "Rechazado I+D", info_suficiente=False) == "DEVOLVER"
    # C1 · Frascati — prueba de exclusiones
    ex_ok = [{"exclusion": e, "veredicto": "sorteada", "sustento": "sustento del estado del arte"}
             for e in EXCLUSIONES_LEY_ID]
    assert frascati(True, True, ex_ok)["es_id_defendible"] is True
    assert frascati(True, True, ex_ok)["defendibilidad"]["estado"] == "defendible"
    ex_aplica = [{"exclusion": "adquisicion_puesta_en_marcha", "veredicto": "aplica", "sustento": "compra e instalación"}]
    r_ex = frascati(True, False, ex_aplica)               # afirma I pero cae en una exclusión
    assert r_ex["es_id"] is True and r_ex["es_id_defendible"] is False
    assert "adquisicion_puesta_en_marcha" in r_ex["exclusiones"]["exclusiones_que_aplican"]
    # C1-bis · REGRESIÓN: 'pendiente' NO cierra una exclusión (defecto detectado 14-ago-2026).
    # Antes, cinco 'pendiente' devolvían es_id_defendible=True: falso positivo de manual.
    ex_pend = [{"exclusion": e, "veredicto": "pendiente", "sustento": "no indagado"} for e in EXCLUSIONES_LEY_ID]
    r_p = frascati(True, True, ex_pend)
    assert r_p["es_id_defendible"] is False, "un 'pendiente' no puede pasar por 'sorteada'"
    assert r_p["exclusiones"]["exclusiones_pendientes"] == EXCLUSIONES_LEY_ID
    # …y el bloqueo se declara como INCOMPLETO (se cierra indagando), no como rechazo.
    assert r_p["defendibilidad"]["estado"] == "incompleto"
    assert r_p["defendibilidad"]["como_destrabar"], "debe decir cómo destrabar, no solo que no se puede"
    # Un flanco real se distingue de la falta de indagación: pide REENCUADRE, no más análisis.
    assert frascati(True, True, ex_aplica + [{"exclusion": e, "veredicto": "sorteada", "sustento": "ok"}
                    for e in EXCLUSIONES_LEY_ID if e != "adquisicion_puesta_en_marcha"]
                    )["defendibilidad"]["estado"] == "requiere_reencuadre"
    # Mezcla: un pendiente basta para bloquear aunque las otras cuatro estén sorteadas.
    ex_mix = [{"exclusion": e, "veredicto": ("pendiente" if e == "novedad_solo_local" else "sorteada"),
               "sustento": "s"} for e in EXCLUSIONES_LEY_ID]
    assert frascati(True, True, ex_mix)["es_id_defendible"] is False
    assert frascati(True, True)["es_id"] is True and "es_id_defendible" not in frascati(True, True)  # sin exclusiones: compat
    # C5 · coherencia de cifras del cliente
    cc = {c["concepto"]: c for c in coherencia_cifras_cliente([
        {"concepto": "flota", "valor": 120, "unidad": "camiones", "fuente": "reunion-1"},
        {"concepto": "flota", "valor": 90, "unidad": "camiones", "fuente": "propuesta"},
        {"concepto": "ahorro", "valor": 30, "unidad": "%", "fuente": "reunion-1"}])}
    assert cc["flota"]["estado"] == "alerta" and cc["ahorro"]["estado"] == "ok"
    qa = {r["regla"][0]: r for r in qa_coherencia_formulacion(
        fase_proyecto_actual="Escalando en ventas",
        profesional_contrato_vigente=True, profesional_id_36m=False,
        nuevo_conocimiento_trazable=True)}
    assert qa["1"]["estado"] == "alerta"   # fase incoherente
    assert qa["2"]["estado"] == "alerta"   # falta I+D 36m
    assert qa["3"]["estado"] == "ok"        # confirmado
    assert qa["4"]["estado"] == "pendiente" # sin confirmar
    # Arancel — anclado en el caso real SRS (19.041 UTM → 30 UTM → $1.508.160)
    ar = arancel(19041)
    assert ar["arancel_utm"] == 30 and ar["arancel_clp"] == 1508160, ar
    assert arancel(300)["arancel_utm"] == 10        # tramo 1 (plano)
    assert arancel(1000)["arancel_utm"] == 12.5      # tramo 2
    assert arancel(5000)["arancel_utm"] == 23.75     # tramo 3
    assert arancel(50000)["arancel_utm"] == 30       # tope
    print("OK: motor de reglas — todos los asserts pasan.")


def _demo() -> None:
    print("Frascati(I=sí, D=sí):", frascati(True, True))
    print("Ley I+D (completa, TRL 5):", ley_id_elegible("completa", 5))
    print("Instrumentos (TRL 4, Pequeña, 30m, lidera mujer):")
    for r in instrumentos_elegibles(4, "Pequeña", 30, lidera_mujer=True):
        marca = "✓" if r["elegible"] else "✗"
        print(f"  {marca} {r['nombre']}: cofin {int(r['cofinanciamiento_pct']*100)}% · "
              f"tope ${r['tope_subsidio_clp']:,} · {r['motivos'] or 'elegible'}")
    print("Compuerta(es_id=True, voto='Aprobado I+D'):", compuerta(True, "Aprobado I+D"))


if __name__ == "__main__":
    if "--demo" in sys.argv:
        _demo()
    elif "--arancel" in sys.argv:
        i = sys.argv.index("--arancel")
        print(json.dumps(arancel(float(sys.argv[i + 1])), ensure_ascii=False, indent=2))
    else:
        _test()
