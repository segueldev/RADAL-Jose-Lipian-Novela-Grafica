#!/usr/bin/env python3
# Detecta menús donde TODAS las opciones son condicionales (Ren'Py crashea
# si en un momento del juego ninguna se cumple).
import re, sys

PATH = sys.argv[1] if len(sys.argv) > 1 else "/home/seguel/Escritorio/Jose_Lipian_La_Novela/Radal/game/script.rpy"
lines = open(PATH, encoding="utf-8").read().splitlines()

def indent(s):
    return len(s) - len(s.lstrip())

CHOICE = re.compile(r'^"((?:[^"\\]|\\.)*)"(\s+if\s+(.+?))?\s*:\s*$')

i = 0
problems = []
menus = 0
while i < len(lines):
    raw = lines[i]
    s = raw.strip()
    ind = indent(raw)
    if not s or s.startswith("#"):
        i += 1
        continue
    if re.match(r"^(init\s+)?python\s*:", s):
        i += 1
        while i < len(lines):
            l2 = lines[i]
            s2 = l2.strip()
            if s2 and not s2.startswith("#") and indent(l2) <= ind and not s2.startswith(")"):
                break
            i += 1
        continue
    if re.match(r"^(screen|transform|style)\b", s):
        i += 1
        while i < len(lines):
            l2 = lines[i]
            s2 = l2.strip()
            if s2 and not s2.startswith("#") and indent(l2) <= ind:
                break
            i += 1
        continue
    if re.match(r"^menu\b.*:\s*$", s):
        menus += 1
        menuind = ind
        i += 1
        choices = []
        while i < len(lines):
            l2 = lines[i]
            s2 = l2.strip()
            ind2 = indent(l2)
            if s2 and not s2.startswith("#") and ind2 <= menuind:
                break
            if s2.startswith('"') and ind2 == menuind + 4:
                m = CHOICE.match(s2)
                if m:
                    choices.append((i + 1, bool(m.group(3)), m.group(3) or ""))
            i += 1
        if choices and all(c[1] for c in choices):
            problems.append((choices[0][0], choices))
        elif not choices:
            problems.append((i, []))
        continue
    i += 1

if problems:
    print(f"MENÚES A REVISAR: {len(problems)}")
    for ln, choices in problems:
        if not choices:
            print(f"  menu cerca de linea {ln}: sin opciones detectadas")
        else:
            print(f"  menu en linea {ln}: LAS {len(choices)} OPCIONES SON CONDICIONALES")
            for cln, _, cond in choices:
                print(f"    linea {cln}: if {cond}")
else:
    print(f"OK: los {menus} menús todos tienen opción incondicional.")
