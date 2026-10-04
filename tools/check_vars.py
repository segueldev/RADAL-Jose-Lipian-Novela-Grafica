#!/usr/bin/env python3
# Busca variables usadas en condiciones (if/elif/menu) que no tienensin default
# ni asignacion, es decir, posibles NameError en rutas especificas.
import re, sys
from collections import defaultdict

PATH = sys.argv[1] if len(sys.argv) > 1 else "/home/seguel/Escritorio/Jose_Lipian_La_Novela/Radal/game/script.rpy"
lines = open(PATH, encoding="utf-8").read().splitlines()

KEYWORDS = set("""if elif else and or not in is True False None for while
lambda del return yield pass raise with as global nonlocal assert break
continue def class import from print len str int float bool abs min max
round sorted sum range enumerate isinstance list dict set tuple super
self cls open iter next zip map filter any all""".split())

defaults = set()
assigned_anywhere = set()
pyfuncs = set()

# --- pasada 1: defaults, asignaciones $ , defs de python ---
in_python = 0
python_depth = None
for i, raw in enumerate(lines, 1):
    s = raw.strip()
    ind = len(raw) - len(raw.lstrip())
    if in_python:
        if s and not s.startswith("#") and ind <= python_depth and not s.startswith(")"):
            in_python = 0
        else:
            m = re.match(r"def\s+([A-Za-z_]\w*)\s*\(", s)
            if m:
                pyfuncs.add(m.group(1))
            continue
    if re.match(r"^(init\s+)?python\s*:", s):
        in_python = 1
        python_depth = ind
        continue
    if re.match(r"^(screen|transform|style)\b", s):
        # bloque de pantalla/estilo: saltar hasta dedent
        depth = ind
        for j in range(i, len(lines)):
            l2 = lines[j]
            s2 = l2.strip()
            ind2 = len(l2) - len(l2.lstrip())
            if s2 and not s2.startswith("#") and ind2 <= depth and j > i - 1:
                break
        continue
    m = re.match(r"default\s+([A-Za-z_]\w*)\s*=", s)
    if m:
        defaults.add(m.group(1))
        continue
    if s.startswith("$"):
        expr = s[1:].strip()
        m = re.match(r"([A-Za-z_]\w*)\s*(?:\+|-|\*|/|//|%|)?=", expr)
        if m:
            assigned_anywhere.add(m.group(1))
    m = re.match(r"def\s+([A-Za-z_]\w*)\s*\(", s)
    if m:
        pyfuncs.add(m.group(1))

# --- pasada 2: condiciones ---
def vars_in(expr, lineno, store):
    # quitar literales de texto
    expr = re.sub(r'"(?:[^"\\]|\\.)*"', ' ', expr)
    expr = re.sub(r"'(?:[^'\\]|\\.)*'", ' ', expr)
    toks = re.findall(r"[A-Za-z_]\w*", expr)
    # posiciones para detectar 'objeto.' y '.atributo'
    keep = []
    for m in re.finditer(r"[A-Za-z_]\w*", expr):
        name = m.group(0)
        after = expr[m.end():m.end() + 1]
        before = expr[max(0, m.start() - 1):m.start()]
        if after == "." or before == ".":
            continue  # contexto de objeto/atributo
        keep.append((name, m.end()))
    for name, end in keep:
        if name in KEYWORDS:
            continue
        nxt = expr[end:end + 1]
        if nxt == "(":
            if name not in pyfuncs:
                store["funcs"].add((lineno, name))
            continue
        store["vars"].add((name, lineno))

store = {"vars": set(), "funcs": set()}
cond_re = re.compile(r"^\s*(?:if|elif)\s+(.+):\s*$")
menu_re = re.compile(r'^\s*"(?:[^"\\]|\\.)*"\s*(?:if\s+(.+?))?\s*:\s*$')

in_python = 0
python_depth = None
in_screen = 0
screen_depth = 0
for i, raw in enumerate(lines, 1):
    s = raw.strip()
    ind = len(raw) - len(raw.lstrip())
    if in_python:
        if s and not s.startswith("#") and ind <= python_depth and not s.startswith(")"):
            in_python = 0
        continue
    if in_screen:
        if s and not s.startswith("#") and ind <= screen_depth:
            in_screen = 0
        elif cond_re.match(raw):
            continue
        else:
            continue
    if re.match(r"^(init\s+)?python\s*:", s):
        in_python = 1
        python_depth = ind
        continue
    if re.match(r"^(screen|transform|style)\b", s):
        in_screen = 1
        screen_depth = ind
        continue
    m = cond_re.match(raw)
    if m:
        vars_in(m.group(1), i, store)
        continue
    if re.match(r'^\s*"', raw):
        m = menu_re.match(raw)
        if m and m.group(1):
            vars_in(m.group(1), i, store)

known = defaults | assigned_anywhere | pyfuncs
problemas = []
for name, ln in sorted(store["vars"], key=lambda x: x[1]):
    if name not in known:
        problemas.append((ln, name, "sin default ni asignacion"))
    elif name not in defaults:
        problemas.append((ln, name, "asignado en $ pero SIN default (riesgo si la ruta lo salta)"))

funcs_malas = [(ln, f) for ln, f in sorted(store["funcs"]) if f not in pyfuncs]

if problemas:
    print("VARIABLES A REVISAR:")
    for ln, name, why in problemas:
        print(f"  linea {ln}: {name}  ({why})")
else:
    print("OK: todas las variables de condiciones tienen default.")
if funcs_malas:
    print("FUNCIONES EN CONDICIONES SIN def:")
    for ln, f in funcs_malas:
        print(f"  linea {ln}: {f}()")
print(f"({len(defaults)} defaults, {len(assigned_anywhere)} asignaciones $, {len(pyfuncs)} defs)")
