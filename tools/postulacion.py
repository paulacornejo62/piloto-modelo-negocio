#!/usr/bin/env python3
"""Paquete de postulación: árbol de carpetas + CHECKLIST de gestión por fondo.

Al entrar a formulación, cada fondo exige reunir un set de documentos (formulario
técnico, estado del arte, CVs, instrumento de representación, arancel, subcontratos…).
Este script genera —según el fondo— la estructura de carpetas y un CHECKLIST que
distingue quién provee cada documento (cliente / brinca / sistema) y su estado, para
gestionar el armado y **bloquear el envío** hasta que esté completo.

El estado vivo se guarda en el bloque `postulacion` del expediente.json (fuente de
verdad); `CHECKLIST.md` es una proyección legible. Idempotente: re-generar preserva
lo marcado a mano y re-deriva los documentos que produce el sistema.

Uso:
    python3 tools/postulacion.py vincular <tenant> <url-o-id-carpeta-drive>  # vincula la carpeta Drive del cliente (al inicio)
    python3 tools/postulacion.py scaffold <tenant>           # crea/actualiza árbol + checklist
    python3 tools/postulacion.py estado <tenant>             # % y faltantes (exit 1 si faltan obligatorios)
    python3 tools/postulacion.py marcar <tenant> "<doc>" <estado> [nota]   # estado: listo|pendiente|na
    python3 tools/postulacion.py sync-drive <tenant> [--parent <folderId>]  # espejo a Drive: crea árbol + SUBE archivos (vía gws)
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

SISTEMA = Path(__file__).resolve().parent.parent
MANIFIESTO = SISTEMA / "motor-reglas" / "documentos_postulacion.json"

# Nombre humano del fondo (meta.instrumento_objetivo / instrumento del comité) → clave del manifiesto.
ALIAS_FONDO = {
    "ley i+d": "ley_id", "ley id": "ley_id", "ley_id": "ley_id",
    "crea y valida": "crea_valida", "crea_valida": "crea_valida",
    "innova alta tecnologia": "innova_alta_tecnologia", "innova alta tecnología": "innova_alta_tecnologia",
    "innova_alta_tecnologia": "innova_alta_tecnologia",
    "consolida y expande": "consolida_expande", "consolida y expande innovacion": "consolida_expande",
    "consolida_expande": "consolida_expande",
    "capital humano": "capital_humano", "capital humano para la innovacion": "capital_humano",
    "capital_humano": "capital_humano",
}

ICONO = {"generado": "✅", "listo": "✅", "pendiente": "⬜", "na": "➖"}


def _ruta_exp(tenant: str) -> Path:
    ruta = SISTEMA / "proyectos" / tenant / "expediente.json"
    if not ruta.exists():
        sys.exit(f"ERROR: no existe {ruta}")
    return ruta


def _cargar(tenant: str) -> tuple[Path, dict]:
    ruta = _ruta_exp(tenant)
    return ruta, json.loads(ruta.read_text(encoding="utf-8"))


def _guardar(ruta: Path, datos: dict) -> None:
    ruta.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _resolver_fondo(datos: dict) -> str:
    """Deduce la clave del fondo desde el expediente (instrumento del comité o meta)."""
    candidatos = [
        (datos.get("eval_p5") or {}).get("instrumento_corfo_seleccionado"),
        (datos.get("meta") or {}).get("instrumento_objetivo"),
    ]
    for c in candidatos:
        if c and (clave := ALIAS_FONDO.get(str(c).strip().lower())):
            return clave
    # Ley I+D si el comité marcó aplica_ley_id y no hay instrumento CORFO.
    if (datos.get("eval_p5") or {}).get("aplica_ley_id"):
        return "ley_id"
    sys.exit("ERROR: no se pudo determinar el fondo (define meta.instrumento_objetivo "
             "o eval_p5.instrumento_corfo_seleccionado).")


def _manifiesto_fondo(clave: str) -> list[dict]:
    man = json.loads(MANIFIESTO.read_text(encoding="utf-8"))
    fondo = man["fondos"].get(clave)
    if not fondo:
        sys.exit(f"ERROR: fondo '{clave}' no está en el manifiesto.")
    carpetas = list(man.get("_comunes", {}).get(fondo["hereda"], [])) if fondo.get("hereda") else []
    carpetas += fondo.get("carpetas", [])
    return carpetas


def _fuente_presente(datos: dict, fuente: str | None) -> bool:
    """¿El bloque del expediente que genera un documento del sistema ya existe?"""
    if not fuente:
        return False
    if fuente == "eval_p2/eval_p4":
        return bool(datos.get("eval_p2") or datos.get("eval_p4"))
    if "." in fuente:
        bloque, campo = fuente.split(".", 1)
        return bool((datos.get(bloque) or {}).get(campo))
    return bool(datos.get(fuente))


def _construir_items(datos: dict, carpetas: list[dict]) -> list[dict]:
    """Aplana el manifiesto a items {carpeta, doc, responsable, fuente, opcional, confirmar, estado}."""
    items = []
    for c in carpetas:
        for d in c.get("docs", []):
            resp = d.get("responsable", c.get("responsable", "cliente"))
            item = {
                "carpeta": c["carpeta"], "doc": d["doc"], "responsable": resp,
                "fuente": d.get("fuente"), "opcional": bool(d.get("opcional")),
                "confirmar": bool(d.get("confirmar")),
            }
            if resp == "sistema":
                item["estado"] = "generado" if _fuente_presente(datos, item["fuente"]) else "pendiente"
            else:
                item["estado"] = "na" if item["opcional"] else "pendiente"
            items.append(item)
    return items


def _merge(previos: list[dict], nuevos: list[dict]) -> list[dict]:
    """Preserva lo marcado a mano (cliente/brinca) y re-deriva los del sistema."""
    idx = {(p["carpeta"], p["doc"]): p for p in previos}
    for n in nuevos:
        antes = idx.get((n["carpeta"], n["doc"]))
        if antes and n["responsable"] != "sistema":
            n["estado"] = antes.get("estado", n["estado"])
            if antes.get("nota"):
                n["nota"] = antes["nota"]
    return nuevos


def _obligatorios_faltantes(items: list[dict]) -> list[dict]:
    return [i for i in items if not i["opcional"] and i["estado"] not in ("generado", "listo")]


def _render_checklist(tenant: str, clave: str, nombre: str, items: list[dict]) -> str:
    faltan = _obligatorios_faltantes(items)
    listos = sum(1 for i in items if i["estado"] in ("generado", "listo"))
    total_obl = sum(1 for i in items if not i["opcional"])
    listos_obl = total_obl - len(faltan)
    out = [f"# Checklist de postulación — {tenant} · {nombre}", "",
           f"> Paquete de documentos para postular. **{listos_obl}/{total_obl} obligatorios listos**"
           f"{' · **LISTO PARA ENVIAR**' if not faltan else f' · faltan {len(faltan)} para enviar'}.",
           "> Estado: ✅ listo/generado · ⬜ pendiente · ➖ opcional/no aplica. "
           "Responsable: cliente = lo aporta la empresa · brinca = lo arma el consultor · sistema = lo genera el flujo.",
           "", "| Carpeta | Documento | Responsable | Estado | Nota |",
           "|---|---|---|---|---|"]
    for i in items:
        ic = ICONO.get(i["estado"], "❓")
        doc = i["doc"] + (" _(confirmar con GT)_" if i.get("confirmar") else "")
        nota = i.get("nota", "") or ("opcional" if i["opcional"] else "")
        out.append(f"| {i['carpeta']} | {doc} | {i['responsable']} | {ic} {i['estado']} | {nota} |")
    if faltan:
        out += ["", "## Faltan para enviar", ""]
        for i in faltan:
            out.append(f"- **{i['carpeta']} / {i['doc']}** — lo provee: {i['responsable']}")
    out.append("")
    return "\n".join(out)


def scaffold(tenant: str) -> None:
    ruta, datos = _cargar(tenant)
    clave = _resolver_fondo(datos)
    man = json.loads(MANIFIESTO.read_text(encoding="utf-8"))
    nombre = man["fondos"][clave].get("nombre", clave)
    carpetas = _manifiesto_fondo(clave)
    items = _construir_items(datos, carpetas)
    previos = (datos.get("postulacion") or {}).get("items", [])
    items = _merge(previos, items)

    base = SISTEMA / "proyectos" / tenant / "postulacion"
    base.mkdir(parents=True, exist_ok=True)
    for c in carpetas:
        (base / c["carpeta"]).mkdir(exist_ok=True)

    datos["postulacion"] = {"fondo": clave, "fondo_nombre": nombre, "items": items}
    _guardar(ruta, datos)
    checklist = _render_checklist(tenant, clave, nombre, items)
    (base / "CHECKLIST.md").write_text(checklist, encoding="utf-8")

    faltan = _obligatorios_faltantes(items)
    print(f"Paquete de postulación generado para '{tenant}' · fondo {nombre}.")
    print(f"  Carpetas: {len(carpetas)} · documentos: {len(items)} · "
          f"listos {len(items) - len([i for i in items if i['estado']=='pendiente'])}/{len(items)}.")
    print(f"  Árbol: {base}")
    print(f"  Checklist: {base / 'CHECKLIST.md'}")
    if faltan:
        print(f"  Faltan {len(faltan)} obligatorios (ver checklist).")


def estado(tenant: str) -> None:
    _, datos = _cargar(tenant)
    post = datos.get("postulacion")
    if not post:
        sys.exit("No hay paquete de postulación. Corre: postulacion.py scaffold " + tenant)
    items = post.get("items", [])
    faltan = _obligatorios_faltantes(items)
    total_obl = sum(1 for i in items if not i["opcional"])
    print(f"Postulación '{tenant}' · {post.get('fondo_nombre', post.get('fondo'))}: "
          f"{total_obl - len(faltan)}/{total_obl} obligatorios listos.")
    for i in items:
        print(f"  {ICONO.get(i['estado'], '?')} [{i['responsable']}] {i['carpeta']} / {i['doc']}")
    if faltan:
        print(f"\nFaltan {len(faltan)} para enviar:")
        for i in faltan:
            print(f"  - {i['carpeta']} / {i['doc']} ({i['responsable']})")
        sys.exit(1)
    print("\nPaquete COMPLETO: listo para el gate de envío.")


def marcar(tenant: str, patron: str, nuevo_estado: str, nota: str = "") -> None:
    if nuevo_estado not in ("listo", "pendiente", "na"):
        sys.exit("estado inválido: usa listo | pendiente | na")
    ruta, datos = _cargar(tenant)
    post = datos.get("postulacion")
    if not post:
        sys.exit("No hay paquete. Corre scaffold primero.")
    patron_l = patron.lower()
    tocados = [i for i in post["items"] if patron_l in i["doc"].lower() or patron_l in i["carpeta"].lower()]
    if not tocados:
        sys.exit(f"Ningún documento coincide con '{patron}'.")
    if len(tocados) > 1:
        print(f"'{patron}' coincide con {len(tocados)} documentos; se marcan todos:")
    for i in tocados:
        if i["responsable"] == "sistema":
            print(f"  (omito '{i['doc']}': lo genera el sistema, su estado se deriva del expediente)")
            continue
        i["estado"] = nuevo_estado
        if nota:
            i["nota"] = nota
        print(f"  {ICONO.get(nuevo_estado)} {i['carpeta']} / {i['doc']} → {nuevo_estado}")
    _guardar(ruta, datos)
    # Re-render del checklist.
    base = SISTEMA / "proyectos" / tenant / "postulacion"
    if base.exists():
        (base / "CHECKLIST.md").write_text(
            _render_checklist(tenant, post["fondo"], post.get("fondo_nombre", ""), post["items"]),
            encoding="utf-8")


def _folder_id(url_o_id: str) -> str:
    """Extrae el id de carpeta de una URL de Drive o lo devuelve tal cual si ya es id."""
    if "drive.google.com" in url_o_id or "/" in url_o_id:
        m = re.search(r"/folders/([A-Za-z0-9_-]+)", url_o_id) or re.search(r"[?&]id=([A-Za-z0-9_-]+)", url_o_id)
        if m:
            return m.group(1)
    return url_o_id.strip()


def vincular(tenant: str, url_o_id: str) -> None:
    """Vincula la carpeta Drive del cliente (al inicio). El sync-drive la usa como raíz."""
    ruta, datos = _cargar(tenant)
    fid = _folder_id(url_o_id)
    datos.setdefault("meta", {})["drive_carpeta"] = fid
    _guardar(ruta, datos)
    print(f"Carpeta Drive vinculada a '{tenant}': {fid}")
    print("Al entrar a formulación, `sync-drive` creará ahí el árbol y subirá los documentos.")


def _gws(args: list[str]) -> dict:
    r = subprocess.run(["gws", *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip() or r.stdout.strip())
    return json.loads(r.stdout) if r.stdout.strip().startswith("{") else {}


def sync_drive(tenant: str, parent: str | None = None) -> None:
    """Espeja el paquete en Drive (on-demand): crea el árbol de carpetas y SUBE los
    archivos locales de cada subcarpeta de `postulacion/`. Requiere gws.

    La raíz es la carpeta vinculada (`meta.drive_carpeta`, vía `vincular`) o `--parent`.
    Local es la fuente de verdad: lo que esté en `proyectos/<tenant>/postulacion/<carpeta>/`
    se sube a la subcarpeta Drive homónima; los archivos ya subidos (por nombre) se omiten
    para no duplicar. Guarda los ids en el expediente.
    """
    ruta, datos = _cargar(tenant)
    post = datos.get("postulacion")
    if not post:
        sys.exit("No hay paquete. Corre scaffold primero.")
    parent = parent or (datos.get("meta") or {}).get("drive_carpeta")
    if not parent:
        sys.exit("No hay carpeta Drive vinculada. Corre: postulacion.py vincular "
                 f"{tenant} <url-o-id> (o pasa --parent <id>).")
    base = SISTEMA / "proyectos" / tenant / "postulacion"
    if not base.exists():
        sys.exit("No existe el árbol local. Corre scaffold primero.")
    drive = post.setdefault("drive", {})
    drive["parent"] = parent
    drive.setdefault("carpetas", {})
    drive.setdefault("archivos", {})

    def crear_carpeta(nombre: str, padre: str) -> str:
        params = json.dumps({
            "resource": {"name": nombre, "mimeType": "application/vnd.google-apps.folder", "parents": [padre]}
        }, ensure_ascii=False)
        return _gws(["drive", "files", "create", "--params", params]).get("id", "")

    def subir(archivo: Path, padre: str, clave: str) -> None:
        if clave in drive["archivos"]:
            return  # ya subido (evita duplicar)
        res = _gws(["drive", "+upload", str(archivo), "--parent", padre, "--name", archivo.name])
        drive["archivos"][clave] = res.get("id", "")
        print(f"    ↑ {clave}")

    subidos = 0
    try:
        if not drive.get("raiz"):
            drive["raiz"] = crear_carpeta(f"{tenant} — postulación ({post.get('fondo_nombre','')})", parent)
            print(f"Raíz en Drive: {drive['raiz']}")
        # Archivos sueltos en la raíz de postulacion/ (p.ej. CHECKLIST.md).
        for f in sorted(base.glob("*")):
            if f.is_file():
                antes = len(drive["archivos"]); subir(f, drive["raiz"], f.name)
                subidos += len(drive["archivos"]) - antes
        # Subcarpetas del paquete + sus archivos.
        for c in sorted({i["carpeta"] for i in post["items"]}):
            if c not in drive["carpetas"]:
                drive["carpetas"][c] = crear_carpeta(c, drive["raiz"])
                print(f"  + carpeta {c}")
            carpeta_local = base / c
            for f in sorted(carpeta_local.glob("*")) if carpeta_local.exists() else []:
                if f.is_file():
                    antes = len(drive["archivos"]); subir(f, drive["carpetas"][c], f"{c}/{f.name}")
                    subidos += len(drive["archivos"]) - antes
    finally:
        _guardar(ruta, datos)
    print(f"Espejo en Drive: {len(drive['carpetas'])} carpetas · {len(drive['archivos'])} archivos "
          f"({subidos} nuevos) bajo {drive['raiz']}.")


def main() -> None:
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    cmd, resto = a[0], a[1:]
    if cmd == "vincular" and len(resto) >= 2:
        vincular(resto[0], resto[1])
    elif cmd == "scaffold" and resto:
        scaffold(resto[0])
    elif cmd == "estado" and resto:
        estado(resto[0])
    elif cmd == "marcar" and len(resto) >= 3:
        marcar(resto[0], resto[1], resto[2], resto[3] if len(resto) > 3 else "")
    elif cmd == "sync-drive" and resto:
        parent = resto[resto.index("--parent") + 1] if "--parent" in resto else None
        sync_drive(resto[0], parent)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
