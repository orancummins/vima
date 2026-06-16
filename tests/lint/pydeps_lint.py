# -*- coding: utf-8 -*-
"""tests/lint/pydeps_lint.py - Dependency graph visualization via pydeps.

Uses pydeps --show-deps (pure Python, no Graphviz required) to extract the
import graph for each target package, generates a self-contained SVG
visualization, and reports:

  - Circular imports (import cycles) → FAIL
  - Modules with unusually high fan-in (most imported) → informational
  - SVG written to tests/output/pydeps/<package>.svg → PASS/FAIL

The SVGs are standalone HTML-embeddable files with colour-coded clusters.

Independently runnable::

    python tests/lint/pydeps_lint.py
"""
from __future__ import annotations

import json
import math
import os
import random
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from tests.lib.utils import TestRunner

_ROOT   = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
_OUTDIR = os.path.join(_ROOT, "tests", "output", "pydeps")

_TARGETS = ["apis", "usecases"]

# ── Palette ───────────────────────────────────────────────────────────────────
_PALETTE = [
    "#f97316", "#3b82f6", "#22c55e", "#a855f7", "#eab308",
    "#06b6d4", "#ec4899", "#10b981", "#6366f1", "#f43f5e",
    "#14b8a6", "#8b5cf6", "#84cc16", "#fb923c", "#38bdf8",
]


# ── Dependency extraction ─────────────────────────────────────────────────────

def _get_deps(pkg: str) -> dict:
    """Run pydeps --show-deps and return the parsed JSON dict."""
    result = subprocess.run(
        [
            sys.executable, "-m", "pydeps", pkg,
            "--noshow", "--no-output", "--show-deps",
            "--max-bacon", "3",
        ],
        capture_output=True, text=True, encoding="utf-8",
        cwd=_ROOT,
    )
    combined = result.stdout + result.stderr
    # pydeps may mix status lines with JSON — find the outermost { ... }
    depth = 0
    start = None
    for i, ch in enumerate(combined):
        if ch == "{":
            if start is None:
                start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start is not None:
                return json.loads(combined[start : i + 1])
    raise ValueError(f"No JSON found in pydeps output for '{pkg}'")


def _project_nodes(deps: dict, root: str) -> dict[str, dict]:
    """Filter to nodes that live inside the project root directory.

    Excludes:
    - Paths inside any virtualenv (.venv, venv, env) within the root — these
      are third-party packages that happen to be under _ROOT on macOS/Linux
      (where the venv is typically created inside the project).  On Windows,
      normcase lowercasing tends to hide these paths, but we exclude them
      explicitly for cross-platform consistency.
    - __main__ sentinel nodes emitted by pydeps.
    """
    norm_root = os.path.normcase(_ROOT)
    # Virtualenv sub-directories to exclude (case-insensitive via normcase)
    _venv_dirs = {
        os.path.normcase(os.path.join(_ROOT, d)) + os.sep
        for d in (".venv", "venv", "env", ".env")
    }

    out: dict[str, dict] = {}
    for name, info in deps.items():
        if name == "__main__":
            continue
        path = info.get("path") or ""
        if not path:
            continue
        norm_path = os.path.normcase(path)
        if not norm_path.startswith(norm_root):
            continue
        # Skip anything inside a virtualenv directory
        if any(norm_path.startswith(vd) for vd in _venv_dirs):
            continue
        out[name] = info
    return out


def _build_edges(nodes: dict[str, dict]) -> list[tuple[str, str]]:
    """Return (src, dst) edges where both endpoints are project nodes."""
    node_set = set(nodes)
    edges: list[tuple[str, str]] = []
    for name, info in nodes.items():
        for imp in (info.get("imports") or []):
            if imp in node_set and imp != name:
                edges.append((name, imp))
    return edges


def _find_cycles(nodes: dict[str, dict], edges: list[tuple[str, str]]) -> list[list[str]]:
    """Return lists of nodes forming import cycles (simple DFS)."""
    adj: dict[str, list[str]] = {n: [] for n in nodes}
    for src, dst in edges:
        adj[src].append(dst)

    visited: set[str] = set()
    rec_stack: set[str] = set()
    cycles: list[list[str]] = []

    def dfs(node: str, path: list[str]) -> None:
        visited.add(node)
        rec_stack.add(node)
        path.append(node)
        for nb in adj.get(node, []):
            if nb not in visited:
                dfs(nb, path)
            elif nb in rec_stack:
                # Extract the cycle
                idx = path.index(nb)
                cycles.append(path[idx:] + [nb])
        path.pop()
        rec_stack.discard(node)

    for n in list(nodes):
        if n not in visited:
            dfs(n, [])
    return cycles


# ── SVG generation ────────────────────────────────────────────────────────────

def _group_key(name: str, pkg: str) -> str:
    """Return the subpackage group for a module name."""
    parts = name.split(".")
    if len(parts) <= 1:
        return parts[0]
    if parts[0] == pkg and len(parts) >= 3:
        return parts[1]
    return parts[0] if parts[0] != pkg else "(root)"


def _force_layout(
    node_names: list[str],
    edges: list[tuple[str, str]],
    W: float,
    H: float,
    iterations: int = 400,
    seed: int = 42,
) -> dict[str, tuple[float, float]]:
    """Fruchterman-Reingold force-directed layout.

    Returns {name: (x, y)} positions inside the canvas W×H with margins.
    """
    rng = random.Random(seed)
    MARGIN = 120
    iW = W - 2 * MARGIN
    iH = H - 2 * MARGIN

    # Initial positions: place on a rough circle to avoid edge-length bias
    pos: dict[str, list[float]] = {}
    n = len(node_names)
    for i, name in enumerate(node_names):
        angle = 2 * math.pi * i / max(n, 1)
        pos[name] = [
            iW / 2 + iW * 0.4 * math.cos(angle) + rng.uniform(-10, 10),
            iH / 2 + iH * 0.4 * math.sin(angle) + rng.uniform(-10, 10),
        ]

    k = math.sqrt(iW * iH / max(n, 1)) * 0.85  # ideal spring length

    def _cool(t: float) -> float:
        return t * 0.92  # cooling schedule

    t = iW * 0.3  # initial temperature
    for _ in range(iterations):
        disp: dict[str, list[float]] = {name: [0.0, 0.0] for name in node_names}

        # Repulsion between every pair
        for i, u in enumerate(node_names):
            for v in node_names[i + 1 :]:
                dx = pos[u][0] - pos[v][0]
                dy = pos[u][1] - pos[v][1]
                dist = math.hypot(dx, dy) or 0.01
                force = k * k / dist
                fx, fy = (dx / dist) * force, (dy / dist) * force
                disp[u][0] += fx; disp[u][1] += fy
                disp[v][0] -= fx; disp[v][1] -= fy

        # Attraction along edges
        for src, dst in edges:
            if src not in pos or dst not in pos:
                continue
            dx = pos[src][0] - pos[dst][0]
            dy = pos[src][1] - pos[dst][1]
            dist = math.hypot(dx, dy) or 0.01
            force = dist * dist / k
            fx, fy = (dx / dist) * force, (dy / dist) * force
            disp[src][0] -= fx; disp[src][1] -= fy
            disp[dst][0] += fx; disp[dst][1] += fy

        # Apply displacement, capped at temperature
        for name in node_names:
            d = math.hypot(*disp[name]) or 0.01
            cap = min(d, t)
            pos[name][0] += (disp[name][0] / d) * cap
            pos[name][1] += (disp[name][1] / d) * cap
            # Clamp inside inner canvas
            pos[name][0] = max(0.0, min(iW, pos[name][0]))
            pos[name][1] = max(0.0, min(iH, pos[name][1]))

        t = _cool(t)

    return {name: (MARGIN + pos[name][0], MARGIN + pos[name][1]) for name in node_names}


def _convex_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Graham scan convex hull (returns CCW polygon vertices)."""
    pts = sorted(set(points))
    if len(pts) <= 2:
        return pts
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower: list[tuple[float, float]] = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper: list[tuple[float, float]] = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def _expand_hull(hull: list[tuple[float, float]], pad: float) -> list[tuple[float, float]]:
    """Expand each hull vertex outward from the centroid by `pad` pixels."""
    if not hull:
        return hull
    cx = sum(p[0] for p in hull) / len(hull)
    cy = sum(p[1] for p in hull) / len(hull)
    result = []
    for x, y in hull:
        dx, dy = x - cx, y - cy
        dist = math.hypot(dx, dy) or 1
        result.append((x + dx / dist * pad, y + dy / dist * pad))
    return result


def _smooth_polygon(pts: list[tuple[float, float]]) -> str:
    """SVG path using cubic bezier smoothing between polygon vertices."""
    n = len(pts)
    if n < 2:
        return ""
    if n == 1:
        x, y = pts[0]
        return f"M{x:.1f},{y:.1f}"

    def ctrl(a, b, ratio=0.25):
        return ((a[0] + b[0]) / 2 * (1 - ratio) + b[0] * ratio,
                (a[1] + b[1]) / 2 * (1 - ratio) + b[1] * ratio)

    d = [f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"]
    for i in range(n):
        p0 = pts[i]
        p1 = pts[(i + 1) % n]
        p2 = pts[(i + 2) % n]
        c1 = ctrl(p0, p1)
        c2 = ctrl(p2, p1)
        d.append(f"C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p1[0]:.1f},{p1[1]:.1f}")
    d.append("Z")
    return " ".join(d)


def _generate_svg(pkg: str, nodes: dict[str, dict], edges: list[tuple[str, str]]) -> str:
    """Build a force-directed SVG from dependency graph data."""
    if not nodes:
        return (
            '<svg xmlns="http://www.w3.org/2000/svg" width="400" height="100">'
            '<text x="10" y="30" font-family="sans-serif" font-size="14" fill="#888">'
            "No internal dependencies found.</text></svg>"
        )

    # ── Group nodes ──────────────────────────────────────────────────────────
    groups: dict[str, list[str]] = {}
    for name in sorted(nodes):
        g = _group_key(name, pkg)
        groups.setdefault(g, []).append(name)

    group_names = sorted(groups)
    colour_map = {g: _PALETTE[i % len(_PALETTE)] for i, g in enumerate(group_names)}

    # ── Force-directed layout ────────────────────────────────────────────────
    LEGEND_W = 200
    W, H = 1400, 950
    node_names = list(nodes.keys())
    node_pos = _force_layout(node_names, edges, W - LEGEND_W, H)

    # ── Helpers ──────────────────────────────────────────────────────────────
    def _fan_in(name: str) -> int:
        return len(nodes[name].get("imported_by") or [])

    def _node_r(name: str) -> float:
        return 9 + min(_fan_in(name), 6) * 1.5

    # ── Build SVG ────────────────────────────────────────────────────────────
    parts: list[str] = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'style="background:#0f172a;font-family:ui-sans-serif,system-ui,sans-serif">'
    )

    # ── Defs ─────────────────────────────────────────────────────────────────
    # One arrowhead marker per group colour, plus a dark drop-shadow filter
    marker_defs = []
    for gname in group_names:
        col = colour_map[gname]
        mid = gname.replace(" ", "_").replace("(", "").replace(")", "")
        marker_defs.append(
            f'<marker id="arr-{mid}" markerWidth="7" markerHeight="7" '
            f'refX="6" refY="3.5" orient="auto">'
            f'<path d="M0,0 L0,7 L7,3.5 Z" fill="{col}" fill-opacity="0.6"/></marker>'
        )
    parts.append(
        "  <defs>\n"
        + "\n".join(f"    {m}" for m in marker_defs)
        + "\n    <filter id='shadow' x='-20%' y='-20%' width='140%' height='140%'>"
        "\n      <feDropShadow dx='0' dy='2' stdDeviation='3' flood-color='#000' flood-opacity='0.5'/>"
        "\n    </filter>"
        "\n  </defs>"
    )

    # ── Background panel separator ────────────────────────────────────────────
    parts.append(
        f'  <rect x="{W - LEGEND_W}" y="0" width="{LEGEND_W}" height="{H}" '
        f'fill="#0a0f1e" rx="0"/>'
    )
    parts.append(
        f'  <line x1="{W - LEGEND_W}" y1="0" x2="{W - LEGEND_W}" y2="{H}" '
        f'stroke="rgba(255,255,255,0.08)" stroke-width="1"/>'
    )

    # ── Title ─────────────────────────────────────────────────────────────────
    graph_cx = (W - LEGEND_W) // 2
    parts.append(
        f'  <text x="{graph_cx}" y="34" text-anchor="middle" '
        f'fill="rgba(255,255,255,0.85)" font-size="20" font-weight="700" letter-spacing="0.5">'
        f'{pkg} - dependency graph</text>'
    )
    parts.append(
        f'  <text x="{graph_cx}" y="54" text-anchor="middle" '
        f'fill="rgba(255,255,255,0.35)" font-size="12">'
        f'{len(nodes)} modules &#183; {len(edges)} edges &#183; {len(group_names)} sub-packages</text>'
    )

    # ── Group hulls ───────────────────────────────────────────────────────────
    for gname in group_names:
        col = colour_map[gname]
        members = groups[gname]
        pts = [node_pos[m] for m in members if m in node_pos]
        if not pts:
            continue

        if len(pts) == 1:
            cx, cy = pts[0]
            r = _node_r(members[0]) + 22
            parts.append(
                f'  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" '
                f'fill="{col}" fill-opacity="0.06" stroke="{col}" '
                f'stroke-opacity="0.3" stroke-width="1.5" stroke-dasharray="4 3"/>'
            )
            parts.append(
                f'  <text x="{cx:.1f}" y="{cy - r - 7:.1f}" text-anchor="middle" '
                f'fill="{col}" font-size="11" font-weight="600" fill-opacity="0.9">{gname}</text>'
            )
        else:
            hull = _convex_hull(pts)
            expanded = _expand_hull(hull, 28)
            path_d = _smooth_polygon(expanded)
            # centroid for label
            lcx = sum(p[0] for p in hull) / len(hull)
            lcy = min(p[1] for p in hull) - 14
            parts.append(
                f'  <path d="{path_d}" fill="{col}" fill-opacity="0.07" '
                f'stroke="{col}" stroke-opacity="0.35" stroke-width="1.5" stroke-dasharray="5 3"/>'
            )
            parts.append(
                f'  <text x="{lcx:.1f}" y="{lcy:.1f}" text-anchor="middle" '
                f'fill="{col}" font-size="11" font-weight="600" fill-opacity="0.9">{gname}</text>'
            )

    # ── Edges ─────────────────────────────────────────────────────────────────
    for src, dst in edges:
        if src not in node_pos or dst not in node_pos:
            continue
        x1, y1 = node_pos[src]
        x2, y2 = node_pos[dst]
        col = colour_map.get(_group_key(src, pkg), "#888")
        mid = _group_key(src, pkg).replace(" ", "_").replace("(", "").replace(")", "")
        # Shorten line to node radius so arrowhead lands on circle edge
        r_dst = _node_r(dst)
        dx, dy = x2 - x1, y2 - y1
        dist = math.hypot(dx, dy) or 1
        ex = x2 - (dx / dist) * (r_dst + 3)
        ey = y2 - (dy / dist) * (r_dst + 3)
        # Slight quadratic curve
        qx = (x1 + x2) / 2 + (y2 - y1) * 0.08
        qy = (y1 + y2) / 2 - (x2 - x1) * 0.08
        parts.append(
            f'  <path d="M{x1:.1f},{y1:.1f} Q{qx:.1f},{qy:.1f} {ex:.1f},{ey:.1f}" '
            f'fill="none" stroke="{col}" stroke-opacity="0.35" stroke-width="1.2" '
            f'marker-end="url(#arr-{mid})"/>'
        )

    # ── Nodes ─────────────────────────────────────────────────────────────────
    for name in node_names:
        if name not in node_pos:
            continue
        nx, ny = node_pos[name]
        gname = _group_key(name, pkg)
        col = colour_map.get(gname, "#888")
        label = name.split(".")[-1]
        fi = _fan_in(name)
        r = _node_r(name)

        # Glow ring for highly-imported nodes
        if fi >= 3:
            parts.append(
                f'  <circle cx="{nx:.1f}" cy="{ny:.1f}" r="{r + 5:.1f}" '
                f'fill="{col}" fill-opacity="0.15" stroke="none"/>'
            )

        parts.append(
            f'  <circle cx="{nx:.1f}" cy="{ny:.1f}" r="{r:.1f}" '
            f'fill="{col}" fill-opacity="0.85" '
            f'stroke="rgba(255,255,255,0.45)" stroke-width="1.2">'
            f'<title>{name} - imported by {fi}</title></circle>'
        )

        # Label: pick least-cluttered side using edge directions
        neighbours = [dst for s, dst in edges if s == name and dst in node_pos] + \
                     [src for src, d in edges if d == name and src in node_pos]
        avg_dx = sum(node_pos[nb][0] - nx for nb in neighbours) / max(len(neighbours), 1)
        anchor = "start" if avg_dx <= 0 else "end"
        lx = nx + (r + 5) * (1 if anchor == "start" else -1)
        parts.append(
            f'  <text x="{lx:.1f}" y="{ny:.1f}" text-anchor="{anchor}" '
            f'dominant-baseline="central" fill="rgba(255,255,255,0.82)" font-size="11" '
            f'paint-order="stroke" stroke="#0f172a" stroke-width="3">{label}</text>'
        )

    # ── Legend panel ──────────────────────────────────────────────────────────
    lx0 = W - LEGEND_W + 18
    ly = 50
    parts.append(
        f'  <text x="{lx0}" y="{ly}" fill="rgba(255,255,255,0.55)" '
        f'font-size="11" font-weight="700" letter-spacing="1">SUB-PACKAGES</text>'
    )
    ly += 18
    for gname in group_names:
        col = colour_map[gname]
        n_m = len(groups[gname])
        parts.append(
            f'  <rect x="{lx0}" y="{ly}" width="10" height="10" rx="2" '
            f'fill="{col}" fill-opacity="0.85"/>'
        )
        display = gname if gname != "(root)" else f"{pkg} (root)"
        parts.append(
            f'  <text x="{lx0 + 15}" y="{ly + 9}" fill="rgba(255,255,255,0.72)" '
            f'font-size="11">{display} <tspan fill="rgba(255,255,255,0.35)">({n_m})</tspan></text>'
        )
        ly += 18
        if ly > H - 80:
            break  # avoid overflow

    # Node size key
    ly += 10
    parts.append(
        f'  <text x="{lx0}" y="{ly}" fill="rgba(255,255,255,0.55)" '
        f'font-size="11" font-weight="700" letter-spacing="1">NODE SIZE</text>'
    )
    ly += 16
    parts.append(
        f'  <text x="{lx0}" y="{ly}" fill="rgba(255,255,255,0.45)" font-size="10">'
        f'= fan-in (imports by others)</text>'
    )

    parts.append("</svg>")
    return "\n".join(parts)


# ── pyvis interactive HTML ────────────────────────────────────────────────────

def _generate_pyvis_html(pkg: str, nodes: dict[str, dict], edges: list[tuple[str, str]]) -> str:
    """Build a self-contained interactive HTML using pyvis + vis.js."""
    try:
        from pyvis.network import Network  # type: ignore[import]
    except ImportError:
        # Auto-install pyvis (it is listed in requirements.txt but may be
        # absent on an --existing install that hasn't been updated recently).
        print("  [pydeps] pyvis not found — installing automatically …")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "pyvis>=0.3.2", "-q"],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            raise AssertionError(
                f"pyvis not installed and auto-install failed:\n{result.stderr[:300]}\n"
                "Run manually: pip install pyvis"
            )
        from pyvis.network import Network  # type: ignore[import]

    groups: dict[str, list[str]] = {}
    for name in sorted(nodes):
        g = _group_key(name, pkg)
        groups.setdefault(g, []).append(name)

    group_names = sorted(groups)
    colour_map = {g: _PALETTE[i % len(_PALETTE)] for i, g in enumerate(group_names)}

    net = Network(
        height="600px",
        width="100%",
        bgcolor="#0f172a",
        font_color="#e2e8f0",
        directed=True,
    )
    net.set_options("""{
      "nodes": {
        "borderWidth": 1.5,
        "borderWidthSelected": 3,
        "font": { "size": 13, "face": "ui-sans-serif, system-ui, sans-serif" }
      },
      "edges": {
        "arrows": { "to": { "enabled": true, "scaleFactor": 0.6 } },
        "smooth": { "type": "dynamic" },
        "width": 1.2,
        "selectionWidth": 2.5
      },
      "physics": {
        "forceAtlas2Based": {
          "gravitationalConstant": -60,
          "centralGravity": 0.005,
          "springLength": 120,
          "springConstant": 0.08,
          "damping": 0.5
        },
        "maxVelocity": 50,
        "minVelocity": 0.75,
        "solver": "forceAtlas2Based",
        "stabilization": { "iterations": 200, "updateInterval": 25 }
      },
      "interaction": {
        "hover": true,
        "tooltipDelay": 100,
        "navigationButtons": true,
        "keyboard": true
      }
    }""")

    for name, info in nodes.items():
        g = _group_key(name, pkg)
        col = colour_map.get(g, "#888")
        label = name.split(".")[-1]
        fan_in = len(info.get("imported_by") or [])
        size = 12 + min(fan_in, 8) * 2.5
        tooltip = f"<b>{name}</b><br/>group: {g}<br/>imported by: {fan_in}"
        net.add_node(
            name,
            label=label,
            title=tooltip,
            color={"background": col, "border": "#ffffff40",
                   "highlight": {"background": col, "border": "#ffffff"},
                   "hover": {"background": col, "border": "#ffffffcc"}},
            size=size,
        )

    for src, dst in edges:
        g = _group_key(src, pkg)
        col = colour_map.get(g, "#888")
        net.add_edge(src, dst, color={"color": col + "66", "highlight": col, "hover": col})

    raw_html = net.generate_html(notebook=False)

    # Inject a legend + dark-theme polish into the body
    legend_items = "".join(
        f'<div style="display:flex;align-items:center;gap:7px;margin-bottom:6px">'
        f'<div style="width:11px;height:11px;border-radius:3px;background:{colour_map[g]};flex-shrink:0"></div>'
        f'<span style="font-size:11px;color:#94a3b8">{g} <span style="color:#475569">({len(groups[g])})</span></span>'
        f'</div>'
        for g in group_names
    )
    legend_html = (
        f'<div style="position:absolute;top:12px;right:12px;background:#0a0f1e;'
        f'border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:12px 14px;'
        f'z-index:999;min-width:170px">'
        f'<div style="font-size:11px;font-weight:700;color:#64748b;letter-spacing:1px;'
        f'margin-bottom:10px">SUB-PACKAGES</div>'
        f'{legend_items}'
        f'<div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.08);'
        f'font-size:10px;color:#475569">Node size = fan-in</div>'
        f'</div>'
    )

    # Insert legend before </body>
    raw_html = raw_html.replace(
        "</body>",
        f'<div style="position:relative">{legend_html}</div></body>',
    )
    # Fix vis.js canvas background
    raw_html = raw_html.replace(
        "#mynetwork {",
        "#mynetwork { background: #0f172a !important; border: none !important;",
    )
    return raw_html


# ── Main run() ────────────────────────────────────────────────────────────────

def run(base_url: str = "") -> TestRunner:
    runner = TestRunner("Dependency Graph (pydeps)")

    # ── Check pydeps is available ────────────────────────────────────────────
    def _check_pydeps():
        r = subprocess.run(
            [sys.executable, "-m", "pydeps", "--version"],
            capture_output=True, text=True, cwd=_ROOT,
        )
        assert r.returncode == 0, "pydeps not installed. Run: pip install pydeps"

    if not runner.run("pydeps is installed", _check_pydeps):
        return runner

    os.makedirs(_OUTDIR, exist_ok=True)
    targets = [t for t in _TARGETS if os.path.isdir(os.path.join(_ROOT, t))]

    for pkg in targets:

        # ── Extract deps ─────────────────────────────────────────────────────
        try:
            raw = _get_deps(pkg)
        except Exception as exc:
            def _deps_err(exc=exc, pkg=pkg):
                raise AssertionError(f"pydeps failed for '{pkg}': {exc}")
            runner.run(f"Extract deps: {pkg}", _deps_err)
            continue

        nodes  = _project_nodes(raw, pkg)
        edges  = _build_edges(nodes)
        cycles = _find_cycles(nodes, edges)

        # ── Scope summary ────────────────────────────────────────────────────
        fan_in = sorted(
            [(n, len(v.get("imported_by") or [])) for n, v in nodes.items()],
            key=lambda x: -x[1],
        )[:5]
        fan_in_str = ", ".join(f"{n.split('.')[-1]}({c})" for n, c in fan_in if c > 0)

        def _scope(pkg=pkg, nodes=nodes, edges=edges, fan_in_str=fan_in_str):
            pass
        runner.run(
            f"{pkg}: {len(nodes)} modules, {len(edges)} dependency edges\n"
            f"  Most imported: {fan_in_str or 'none'}",
            _scope,
        )

        # ── Cycle check ──────────────────────────────────────────────────────
        if cycles:
            for cycle in cycles:
                cycle_str = " → ".join(cycle)
                def _cycle_fail(cs=cycle_str):
                    raise AssertionError(f"Circular import detected: {cs}")
                runner.run(f"{pkg}: no circular imports", _cycle_fail)
        else:
            def _no_cycles():
                pass
            runner.run(f"{pkg}: no circular imports", _no_cycles)

        # ── Generate SVG ─────────────────────────────────────────────────────
        svg_path = os.path.join(_OUTDIR, f"{pkg}.svg")
        try:
            svg = _generate_svg(pkg, nodes, edges)
            with open(svg_path, "w", encoding="utf-8") as fh:
                fh.write(svg)
            rel = os.path.relpath(svg_path, _ROOT).replace("\\", "/")
            def _svg_ok(rel=rel):
                pass
            runner.run(f"{pkg}: SVG written -> {rel}", _svg_ok)
        except Exception as exc:
            def _svg_err(exc=exc):
                raise AssertionError(f"SVG generation failed: {exc}")
            runner.run(f"{pkg}: SVG generation", _svg_err)

        # ── Generate interactive HTML (pyvis) ────────────────────────────────
        html_path = os.path.join(_OUTDIR, f"{pkg}.html")
        try:
            html = _generate_pyvis_html(pkg, nodes, edges)
            with open(html_path, "w", encoding="utf-8") as fh:
                fh.write(html)
            rel_h = os.path.relpath(html_path, _ROOT).replace("\\", "/")
            def _html_ok(rel_h=rel_h):
                pass
            runner.run(f"{pkg}: interactive graph -> {rel_h}", _html_ok)
        except Exception as exc:
            def _html_err(exc=exc):
                raise AssertionError(f"pyvis generation failed: {exc}")
            runner.run(f"{pkg}: interactive graph", _html_err)

    return runner


if __name__ == "__main__":
    r = run()
    r.print_summary()
    sys.exit(0 if r.failed() == 0 else 1)
