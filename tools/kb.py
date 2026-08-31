#!/usr/bin/env python3
"""Consulta de la base de conocimiento transversal (papers/patentes).

La KB (`kb/indice.json` + `kb/fichas/`) es la única capa COMPARTIDA entre proyectos:
se consulta en cada Deep Research y se enriquece en cada uno. Esta herramienta la
hace consultable y evita duplicados. Sin dependencias externas.

Uso:
    python3 tools/kb.py listar
    python3 tools/kb.py buscar --tema oxígeno --tipo paper --texto hipoxia
    python3 tools/kb.py dedup "Forecasting hypoxia in salmon farms"   # ¿ya existe algo similar?
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

KB = Path(__file__).resolve().parent.parent / "kb"
INDICE = KB / "indice.json"


def _cargar() -> dict:
    return json.loads(INDICE.read_text(encoding="utf-8")) if INDICE.exists() else {"nodos": [], "aristas": []}


def _ficha_path(fid: str):
    """Ruta de la ficha (las fichas viven en subcarpetas por área)."""
    return next((KB / "fichas").glob(f"**/{fid}.md"), None)


def _norm(s: str) -> set[str]:
    return {w for w in re.findall(r"\w+", (s or "").lower()) if len(w) > 3}


def listar() -> None:
    d = _cargar()
    print(f"{len(d['nodos'])} fichas · {len(d.get('aristas', []))} relaciones\n")
    for n in d["nodos"]:
        print(f"- [{n.get('tipo','?')}] {n['id']} — {n.get('titulo','')[:80]}")
        print(f"    tema: {n.get('tema','')} · disciplina: {n.get('disciplina','')} · proyectos: {n.get('proyectos',[])}")


def buscar(args) -> None:
    d = _cargar()
    res = []
    for n in d["nodos"]:
        if args.tipo and n.get("tipo") != args.tipo:
            continue
        if args.area and args.area.lower() not in n.get("area_oecd", "").lower():
            continue
        if args.topico and not any(args.topico.lower() in t.lower() for t in n.get("topicos", [])):
            continue
        if args.tema and args.tema.lower() not in (n.get("tema", "") + n.get("titulo", "")).lower():
            continue
        if args.texto:
            blob = json.dumps(n, ensure_ascii=False).lower()
            ficha = _ficha_path(n["id"])
            if ficha:
                blob += ficha.read_text(encoding="utf-8").lower()
            if args.texto.lower() not in blob:
                continue
        res.append(n)
    print(f"{len(res)} resultado(s):")
    for n in res:
        tops = ", ".join(n.get("topicos", []))
        print(f"- {n['id']} — {n.get('titulo','')[:70]}")
        print(f"    tópicos: {tops}")


def dedup(titulo: str) -> None:
    """Antes de crear una ficha, ver si ya hay una similar (overlap de tokens)."""
    d = _cargar()
    base = _norm(titulo)
    cand = []
    for n in d["nodos"]:
        otros = _norm(n.get("titulo", "")) | _norm(n.get("tema", ""))
        if base and otros:
            sim = len(base & otros) / len(base | otros)
            if sim >= 0.18:
                cand.append((round(sim, 2), n["id"], n.get("titulo", "")))
    cand.sort(reverse=True)
    if cand:
        print("Posibles duplicados (similitud, id, título):")
        for s, i, t in cand[:5]:
            print(f"  {s}  {i} — {t[:80]}")
        print("→ Enlaza/actualiza la existente en vez de crear una nueva.")
    else:
        print("Sin duplicados aparentes; se puede crear la ficha nueva.")


def ver(fid: str) -> None:
    """Muestra una ficha + su vecindario en el grafo (relaciones)."""
    d = _cargar()
    nodo = next((n for n in d["nodos"] if n["id"] == fid), None)
    if not nodo:
        print(f"No existe la ficha '{fid}'.")
        return
    print(f"# {nodo['id']}\n{json.dumps(nodo, ensure_ascii=False, indent=1)}")
    rel = [a for a in d.get("aristas", []) if a.get("origen") == fid or a.get("destino") == fid]
    print(f"\nRelaciones ({len(rel)}):")
    for a in rel:
        otro = a["destino"] if a.get("origen") == fid else a.get("origen")
        flecha = "→" if a.get("origen") == fid else "←"
        print(f"  {flecha} [{a.get('tipo','?')}] {otro}  {('· ' + a['nota']) if a.get('nota') else ''}")
    ficha = _ficha_path(fid)
    if ficha:
        print(f"\n--- {ficha.name} ---\n{ficha.read_text(encoding='utf-8')[:1200]}")


def autocablear() -> None:
    """Deriva aristas del grafo desde las referencias [[ficha-id]] en el CUERPO de las fichas.

    Cero LLM (regex, microsegundos). Agrega a indice.json las aristas nuevas (con `auto: true`,
    tipo 'referencia') sin duplicar ni tocar las manuales. La adyacencia por tópico compartido
    NO se materializa como aristas (saturaría el grafo); ya vive en topicos.json y la usa `salud`.
    """
    d = _cargar()
    ids = {n["id"] for n in d["nodos"]}
    existentes = {(a.get("origen"), a.get("destino")) for a in d.get("aristas", [])}
    nuevas = []
    for n in d["nodos"]:
        f = _ficha_path(n["id"])
        if not f:
            continue
        for m in re.finditer(r"\[\[([a-z0-9][a-z0-9\-]*)(?:\|[^\]]*)?\]\]", f.read_text(encoding="utf-8")):
            destino, par = m.group(1), (n["id"], m.group(1))
            if destino in ids and destino != n["id"] and par not in existentes:
                nuevas.append({"origen": n["id"], "destino": destino, "tipo": "referencia",
                               "auto": True, "nota": "derivada de [[link]] en el cuerpo"})
                existentes.add(par)
    if nuevas:
        d.setdefault("aristas", []).extend(nuevas)
        INDICE.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Auto-cableado: {len(nuevas)} arista(s) nueva(s) desde [[ficha]] (tipo 'referencia').")
    for a in nuevas:
        print(f"  {a['origen']} → {a['destino']}")
    if not nuevas:
        print("  (sin referencias [[ficha]] nuevas; el grafo ya está al día)")


def _frontmatter_valor(path, clave: str):
    """Lee un valor escalar simple del frontmatter YAML de una ficha (o None)."""
    if not path:
        return None
    try:
        txt = path.read_text(encoding="utf-8")
    except Exception:
        return None
    if not txt.startswith("---"):
        return None
    fin = txt.find("\n---", 3)
    for line in txt[3:fin if fin > 0 else len(txt)].splitlines():
        k, sep, v = line.partition(":")
        if sep and k.strip() == clave:
            return v.split("#")[0].strip() or None
    return None


def salud() -> None:
    """Diagnóstico del grafo: huérfanos, cobertura por tipo/disciplina, fichas faltantes."""
    d = _cargar()
    nodos = d["nodos"]
    aristas = d.get("aristas", [])
    conectados = {a.get("origen") for a in aristas} | {a.get("destino") for a in aristas}
    huerfanos = [n["id"] for n in nodos if n["id"] not in conectados]
    sin_ficha = [n["id"] for n in nodos if not _ficha_path(n["id"])]
    sin_proyecto = [n["id"] for n in nodos if not n.get("proyectos")]
    sin_topico = [n["id"] for n in nodos if not n.get("topicos")]
    from collections import Counter
    print(f"Fichas: {len(nodos)} · Relaciones: {len(aristas)}")
    print("Por tipo:", dict(Counter(n.get("tipo", "?") for n in nodos)))
    print("Por área OCDE:", dict(Counter(n.get("area_oecd", "?") for n in nodos)))
    tops = Counter(t for n in nodos for t in n.get("topicos", []))
    print(f"Tópicos ({len(tops)}):", dict(tops.most_common(8)))
    prof = Counter(_frontmatter_valor(_ficha_path(n["id"]), "profundidad_lectura") or "?" for n in nodos)
    print("Profundidad de lectura:", dict(prof))
    print(f"Huérfanos (sin relaciones): {huerfanos or '—'}")
    print(f"Nodos sin ficha: {sin_ficha or '—'}")
    print(f"Nodos sin tópico: {sin_topico or '—'}")
    print(f"Nodos sin proyecto: {sin_proyecto or '—'}")

    # --- Gap analysis: qué NO cubre bien la KB (inspirado en GBrain, GTF-19) ---
    from collections import defaultdict
    tipos_por_area = defaultdict(set)
    for n in nodos:
        tipos_por_area[n.get("area_oecd", "?")].add(n.get("tipo"))
    delgados = sorted(t for t, c in tops.items() if c == 1)
    sin_patente = sorted(a for a, ts in tipos_por_area.items() if "paper" in ts and "patente" not in ts)
    parciales = [n["id"] for n in nodos
                 if _frontmatter_valor(_ficha_path(n["id"]), "profundidad_lectura") in ("abstract", "metadata")]
    print("\nBrechas (gap analysis — qué falta cubrir):")
    print(f"  · Tópicos delgados (1 sola ficha): {delgados or '—'}")
    print(f"  · Áreas con papers pero SIN patente (revisar prior art): {sin_patente or '—'}")
    print(f"  · Fichas solo abstract/metadata (subir a full-text): {len(parciales)}"
          + (f" → {parciales[:6]}{'…' if len(parciales) > 6 else ''}" if parciales else ""))
    print(f"  · Huérfanos en el grafo (correr `kb.py autocablear`): {len(huerfanos)}")


def export_mermaid() -> None:
    """Exporta el grafo a Mermaid (para visualizar/pegar en docs)."""
    d = _cargar()
    print("```mermaid\ngraph LR")
    for n in d["nodos"]:
        t = (n.get("titulo", n["id"])[:36]).replace('"', "'")
        print(f'  {n["id"].replace("-", "_")}["{t}"]')
    for a in d.get("aristas", []):
        o, de = a.get("origen", "").replace("-", "_"), a.get("destino", "").replace("-", "_")
        print(f'  {o} -->|{a.get("tipo", "")}| {de}')
    print("```")


def main() -> None:
    ap = argparse.ArgumentParser(description="Consulta de la base de conocimiento GTF.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("listar")
    b = sub.add_parser("buscar")
    b.add_argument("--tema"); b.add_argument("--tipo"); b.add_argument("--area")
    b.add_argument("--topico"); b.add_argument("--texto")
    dd = sub.add_parser("dedup"); dd.add_argument("titulo")
    v = sub.add_parser("ver"); v.add_argument("id")
    sub.add_parser("salud")
    sub.add_parser("autocablear")
    sub.add_parser("export")
    args = ap.parse_args()
    if args.cmd == "listar":
        listar()
    elif args.cmd == "buscar":
        buscar(args)
    elif args.cmd == "dedup":
        dedup(args.titulo)
    elif args.cmd == "ver":
        ver(args.id)
    elif args.cmd == "salud":
        salud()
    elif args.cmd == "autocablear":
        autocablear()
    elif args.cmd == "export":
        export_mermaid()


if __name__ == "__main__":
    main()
