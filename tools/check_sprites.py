#!/usr/bin/env python3
# Analiza script.rpy: construye el grafo de flujo (labels/jumps/calls/menus/if)
# y verifica que todo personaje que habla este visible en TODOS los caminos.
import re, sys
from collections import defaultdict

PATH = sys.argv[1] if len(sys.argv) > 1 else "/home/seguel/Escritorio/Jose_Lipian_La_Novela/Radal/game/script.rpy"
lines = open(PATH, encoding="utf-8").read().splitlines()

CHARS = {"jose","shakira","pablo","benjamin","marcelo","diego","fabian",
         "bastian","ruben","maxi","ivan","martin","hector","inacapini"}
TOP = frozenset(CHARS)

def indent(s):
    return len(s) - len(s.lstrip())

SAY = re.compile(r'^\s*([a-z_]+) "(.*)"\s*$')
HDR = re.compile(r'^(if|elif|else|menu|label|jump|call|return|scene|show|hide)\b')

# ---- 1. Parsear linea a linea, saltando bloques python/pantallas/estilos ----
stmts = []  # (line_no, indent, text)
i = 0
while i < len(lines):
    raw = lines[i]; s = raw.strip()
    if not s or s.startswith("#"):
        i += 1; continue
    ind = indent(raw)
    if re.match(r'^(init +)?python *:', s) or re.match(r'^(screen|transform|style) \b', s):
        i += 1
        while i < len(lines):
            l2 = lines[i]
            if l2.strip() and not l2.lstrip().startswith("#") and indent(l2) <= ind:
                break
            i += 1
        continue
    if s.startswith(("image ", "define ", "default ", "$", "#")):
        i += 1; continue
    stmts.append((i + 1, ind, s))
    i += 1

# ---- 2. Construir grafo ----
nodes = []  # dict: stmt=(kind,data)|None, succ=[]
def newnode(stmt=None):
    nodes.append({"stmt": stmt, "succ": []})
    return len(nodes) - 1
def edge(a, b):
    nodes[a]["succ"].append(b)

labels = {}
pending_calls = []   # (callee, after_node)
returns_by_label = defaultdict(list)
current_label = [None]

def parse_block(i, ind, cur):
    """Parsea sentencias con indent > 'ind'. Devuelve (i, cur)."""
    n = len(stmts)
    while i < n:
        ln, si, s = stmts[i]
        if si <= ind:
            return i, cur
        tok = s.split(None, 1)[0]
        mlabel = re.match(r'^label (\w+)\s*:', s)

        if mlabel:
            node = newnode()
            edge(cur, node)
            labels[mlabel.group(1)] = node
            current_label[0] = mlabel.group(1)
            cur = node; i += 1; continue

        if tok == "if":
            branch_exits = []
            has_else = False
            while i < n:
                ln2, si2, s2 = stmts[i]
                if si2 != si:
                    break
                if re.match(r'^if\b', s2):
                    i += 1
                    i, ec = parse_block(i, si, cur)
                    branch_exits.append(ec)
                elif re.match(r'^elif\b', s2):
                    i += 1
                    i, ec = parse_block(i, si, cur)
                    branch_exits.append(ec)
                elif re.match(r'^else\s*:', s2):
                    has_else = True
                    i += 1
                    i, ec = parse_block(i, si, cur)
                    branch_exits.append(ec)
                else:
                    break
            merge = newnode()
            for b in branch_exits:
                edge(b, merge)
            if not has_else:
                edge(cur, merge)   # condicion falsa sin else
            cur = merge; continue

        if tok == "menu":
            i += 1
            exits = []
            seq_cur = cur
            while i < n:
                ln2, si2, s2 = stmts[i]
                if si2 <= si:
                    break
                if si2 == si + 4 and re.match(r'^"(?:[^"\\]|\\.)*"(?: if .* )?:\s*$', s2):
                    # nueva opcion -> rama desde la condicion del menu
                    i += 1
                    i, ec = parse_block(i, si + 4, cur)
                    exits.append(ec)
                    seq_cur = newnode()   # punto muerto tras opcion
                else:
                    i, seq_cur = walk_one(i, seq_cur)
            merge = newnode()
            for e in exits:
                edge(e, merge)
            if not exits:
                edge(cur, merge)
            cur = merge; continue

        if tok == "jump":
            tgt = s.split()[1].rstrip(":")
            node = newnode(("jump", tgt)); edge(cur, node)
            cur = newnode()   # codigo muerto hasta el proximo label
            i += 1; continue

        if tok == "call":
            tgt = s.split()[1].rstrip(":")
            node = newnode(("call", tgt)); edge(cur, node)
            after = newnode()
            pending_calls.append((tgt, after))
            cur = after; i += 1; continue

        if tok == "return":
            node = newnode(("return", None)); edge(cur, node)
            if current_label[0]:
                returns_by_label[current_label[0]].append(node)
            cur = newnode(); i += 1; continue

        if tok in ("scene", "show", "hide"):
            node = newnode(("img", (tok, s.split(None, 1)[1] if " " in s else "")))
            edge(cur, node); cur = node; i += 1; continue

        m = SAY.match(s)
        if m and m.group(1) in CHARS | {"mc"}:
            node = newnode(("say", (m.group(1), ln)))
            edge(cur, node); cur = node; i += 1; continue

        # cualquier otra cosa: no-op
        i += 1; continue
    return i, cur

def walk_one(i, cur):
    """Procesa UNA sentencia simple (para lineas sueltas dentro de menu)."""
    n = len(stmts)
    if i >= n:
        return i, cur
    ln, si, s = stmts[i]
    tok = s.split(None, 1)[0]
    if tok in ("scene", "show", "hide"):
        node = newnode(("img", (tok, s.split(None, 1)[1] if " " in s else "")))
        edge(cur, node); cur = node
    else:
        m = SAY.match(s)
        if m and m.group(1) in CHARS | {"mc"}:
            node = newnode(("say", (m.group(1), ln)))
            edge(cur, node); cur = node
    return i + 1, cur

dummy = newnode()   # nodo raiz muerto
parse_block(0, -1, dummy)

# conectar returns con sus call-sites
for callee, after in pending_calls:
    for r in returns_by_label.get(callee, []):
        edge(r, after)

# labels sin predecesores = entradas del juego
has_pred = set()
for nd in nodes:
    for s in nd["succ"]:
        has_pred.add(s)
entries = [nd for name, nd in labels.items() if nd not in has_pred]

# ---- 3. Dataflow: interseccion (visibilidad en TODOS los caminos) ----
IN = [None] * len(nodes)
OUT = [None] * len(nodes)

def transfer(nd):
    st = IN[nd]
    stmt = nodes[nd]["stmt"]
    if stmt is None:
        return st
    kind, data = stmt
    if kind == "img":
        tok, arg = data
        first = arg.split()[0] if arg.split() else ""
        if tok == "scene":
            return frozenset()
        if tok == "show" and first in CHARS:
            return st | {first}
        if tok == "hide" and first in CHARS:
            return frozenset(c for c in st if c != first)
        return st
    return st   # say/jump/call/return no cambian estado

for e in entries:
    IN[e] = frozenset()

for _ in range(200):
    changed = False
    for nd in range(len(nodes)):
        preds = [p for p in range(len(nodes)) if nd in nodes[p]["succ"]]
        if nd in entries:
            new_in = frozenset()
        elif preds:
            new_in = TOP
            for p in preds:
                po = OUT[p] if OUT[p] is not None else TOP
                new_in = frozenset(c for c in new_in if c in po)
        else:
            new_in = IN[nd]   # nodo muerto: no se actualiza
        if new_in != IN[nd]:
            IN[nd] = new_in; changed = True
        new_out = transfer(nd)
        if new_out != OUT[nd]:
            OUT[nd] = new_out; changed = True
    if not changed:
        break

# ---- 4. Reportar ----
problems = []
for nd in range(len(nodes)):
    stmt = nodes[nd]["stmt"]
    if stmt and stmt[0] == "say":
        char, ln = stmt[1]
        if char != "mc" and IN[nd] is not None and char not in IN[nd]:
            problems.append((ln, char, sorted(IN[nd])))

problems.sort()
if problems:
    print(f"PROBLEMAS: {len(problems)}")
    for ln, char, shown in problems:
        print(f"  linea {ln}: '{char}' habla y NO esta en escena (visibles: {shown or 'ninguno'})")
else:
    print("OK: todo personaje que habla esta visible en todos los caminos.")
print(f"({len(nodes)} nodos, {len(labels)} labels, {sum(1 for n in nodes for s in n['stmt'] and [1] or [])} sentencias)")
