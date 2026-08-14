# -*- coding: utf-8 -*-
"""tests/lint/arch_lint.py - Application architecture diagrams via Mermaid.

Generates two self-contained HTML files containing interactive Mermaid diagrams:

  1. ``app_arch.html``  - Flask app structure: blueprints, port, API groups
  2. ``uc_flows.html``  - Use case -> API dependency flows

Output: tests/output/arch/{app_arch,uc_flows}.html
Tests:  checks both files were written without error.

Independently runnable::

    python tests/lint/arch_lint.py
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from tests.lib.utils import TestRunner

_ROOT   = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
_OUTDIR = os.path.join(_ROOT, "tests", "output", "arch")

# ---------------------------------------------------------------------------
# Mermaid diagram builders
# ---------------------------------------------------------------------------

def _app_arch_mermaid() -> str:
    """Flowchart: Flask app entry point -> blueprints -> API groups."""
    from apis.catalog import _ENTRIES, GROUP_ORDER, DISABLED_API_IDS  # type: ignore[attr-defined]

    # Build group -> [display_name] map (skip disabled)
    groups: dict[str, list[str]] = {}
    for e in _ENTRIES:
        if e.id in DISABLED_API_IDS:
            continue
        groups.setdefault(e.group, []).append(e.display_name)

    # Safe Mermaid node id
    def _nid(s: str) -> str:
        return s.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "").replace("&", "and").replace("-", "_").replace(",", "").replace(".", "").replace("'", "")

    lines: list[str] = [
        "flowchart TB",
        "",
        "    %% ---- Entry point ----",
        '    BROWSER(["Browser"])',
        '    APP["Flask app.py\\nport :9021"]',
        "    BROWSER --> APP",
        "",
        "    %% ---- Blueprints ----",
        '    BP_CHAT["chat blueprint\\n/chat"]',
        '    BP_SIM["simulator blueprint\\n/api-sim"]',
        '    BP_TEST["test dashboard\\n/vima/test"]',
        '    BP_MAIN["main routes\\n/  /explorer  /usecases"]',
        "    APP --> BP_CHAT",
        "    APP --> BP_SIM",
        "    APP --> BP_TEST",
        "    APP --> BP_MAIN",
        "",
        "    %% ---- Middleware / cross-cutting ----",
        '    MW_LOG["API call logger\\n(monkey-patches requests)"]',
        '    MW_SIM["simulator switcher\\n(intercepts /api-sim/)"]',
        '    MW_PROXY["ProxyFix middleware"]',
        "    APP -.-> MW_LOG",
        "    APP -.-> MW_SIM",
        "    APP -.-> MW_PROXY",
        "",
        "    %% ---- Registries ----",
        '    REG_API["apis.registry"]',
        '    REG_UC["usecases.registry"]',
        "    BP_MAIN --> REG_API",
        "    BP_MAIN --> REG_UC",
        "",
    ]

    # API groups as subgraphs
    group_node_ids: dict[str, list[str]] = {}
    for group in GROUP_ORDER:
        apis = groups.get(group, [])
        if not apis:
            continue
        sg_id = _nid(group)
        lines.append(f"    subgraph {sg_id} [\"{group}\"]")
        lines.append("        direction LR")
        nids = []
        for name in apis:
            nid = _nid(name)
            lines.append(f'        {nid}["{name}"]')
            nids.append(nid)
        group_node_ids[group] = nids
        lines.append("    end")
        lines.append(f"    REG_API --> {sg_id}")
        lines.append("")

    # Use cases
    lines += [
        '    subgraph USE_CASES ["Use Cases"]',
        "        direction LR",
    ]
    from usecases.registry import USE_CASE_MODULES
    import importlib
    for mod_name in USE_CASE_MODULES:
        try:
            m = importlib.import_module(f"usecases.{mod_name}")
            label = m.MANIFEST.get("name", mod_name)
            nid = "UC_" + _nid(mod_name)
            lines.append(f'        {nid}["{label}"]')
        except Exception:
            pass
    lines += [
        "    end",
        "    REG_UC --> USE_CASES",
        "",
        "    %% ---- Styling ----",
        "    classDef blueprint fill:#1e40af,stroke:#3b82f6,color:#fff",
        "    classDef middleware fill:#374151,stroke:#6b7280,color:#d1d5db",
        "    classDef registry fill:#065f46,stroke:#10b981,color:#fff",
        "    classDef entry fill:#1c1917,stroke:#f97316,color:#fdba74",
        "    class BP_CHAT,BP_SIM,BP_TEST,BP_MAIN blueprint",
        "    class MW_LOG,MW_SIM,MW_PROXY middleware",
        "    class REG_API,REG_UC registry",
        "    class APP,BROWSER entry",
    ]

    return "\n".join(lines)


def _uc_flows_mermaid() -> str:
    """Flowchart: Use cases on left, APIs they depend on on right."""
    import importlib
    from usecases.registry import USE_CASE_MODULES

    def _nid(s: str) -> str:
        return s.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "").replace("&", "and").replace("-", "_").replace(",", "").replace(".", "").replace("'", "")

    lines: list[str] = [
        "flowchart LR",
        "",
        "    %% Use cases (left side)",
    ]

    uc_api_pairs: list[tuple[str, str, str, str]] = []  # (uc_nid, uc_label, api_nid, api_id)
    api_labels: dict[str, str] = {}

    from apis.catalog import _ENTRIES  # type: ignore[attr-defined]
    catalog_map = {e.id: e.display_name for e in _ENTRIES}

    for mod_name in USE_CASE_MODULES:
        try:
            m = importlib.import_module(f"usecases.{mod_name}")
            uc_label = m.MANIFEST.get("name", mod_name)
            uc_nid = "UC_" + _nid(mod_name)
            apis_used: list[str] = m.MANIFEST.get("apis", [])
            lines.append(f'    {uc_nid}(["{uc_label}"])')
            for api_id in apis_used:
                api_nid = "API_" + _nid(api_id)
                api_label = catalog_map.get(api_id, api_id.replace("_", " ").title())
                api_labels[api_nid] = api_label
                uc_api_pairs.append((uc_nid, uc_label, api_nid, api_id))
        except Exception:
            pass

    lines.append("")
    lines.append("    %% APIs (right side)")
    for nid, label in api_labels.items():
        lines.append(f'    {nid}["{label}"]')

    lines.append("")
    lines.append("    %% Edges")
    for uc_nid, _, api_nid, _ in uc_api_pairs:
        lines.append(f"    {uc_nid} --> {api_nid}")

    lines += [
        "",
        "    %% Styling",
        "    classDef uc fill:#1e3a5f,stroke:#3b82f6,color:#bfdbfe",
        "    classDef api fill:#14532d,stroke:#22c55e,color:#bbf7d0",
    ]
    # Apply classes
    uc_nids = list({p[0] for p in uc_api_pairs})
    api_nids = list(api_labels.keys())
    if uc_nids:
        lines.append("    class " + ",".join(uc_nids) + " uc")
    if api_nids:
        lines.append("    class " + ",".join(api_nids) + " api")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# HTML wrapper — mermaid bundled locally (no CDN at render time)
# ---------------------------------------------------------------------------

_MERMAID_CACHE = os.path.join(_OUTDIR, "_mermaid.min.js")
# UMD build — standard <script> tag, no ES-module import() needed
_MERMAID_CDN   = "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"
# URL where the Flask dashboard serves the cached copy
_MERMAID_ROUTE = "/vima/test/arch/mermaid.js"


def _ensure_mermaid() -> bool:
    """Download and cache mermaid UMD JS if not already present. Returns True on success."""
    if os.path.exists(_MERMAID_CACHE) and os.path.getsize(_MERMAID_CACHE) > 100_000:
        return True
    os.makedirs(_OUTDIR, exist_ok=True)
    try:
        # Inject corporate CA trust store (same as app.py does)
        try:
            import truststore as _ts
            _ts.inject_into_ssl()
        except Exception:
            pass
        import requests as _req
        resp = _req.get(_MERMAID_CDN, timeout=30)
        resp.raise_for_status()
        with open(_MERMAID_CACHE, "w", encoding="utf-8") as fh:
            fh.write(resp.text)
        return True
    except Exception:
        return False


def _render_html(title: str, subtitle: str, mermaid_src: str) -> str:
    has_mermaid = _ensure_mermaid()
    if has_mermaid:
        script_block = (
            f'<script src="{_MERMAID_ROUTE}"></script>\n'
            "<script>\n"
            "  mermaid.initialize({\n"
            "    startOnLoad: true,\n"
            "    theme: 'dark',\n"
            "    themeVariables: {\n"
            "      primaryColor: '#1e40af', primaryTextColor: '#e2e8f0',\n"
            "      primaryBorderColor: '#3b82f6', lineColor: '#475569',\n"
            "      secondaryColor: '#065f46', tertiaryColor: '#1e293b',\n"
            "      background: '#0f172a', mainBkg: '#1e293b',\n"
            "      nodeBorder: '#475569', clusterBkg: '#1e293b',\n"
            "      titleColor: '#f8fafc', edgeLabelBackground: '#0f172a',\n"
            "    },\n"
            "    flowchart: { curve: 'basis', padding: 20 },\n"
            "  });\n"
            "</script>"
        )
        diagram_style  = ""
        fallback_style = "display:none"
    else:
        script_block   = ""
        diagram_style  = "display:none"
        fallback_style = ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{title}</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html, body {{ height: 100%; background: #0f172a; color: #e2e8f0;
                  font-family: ui-sans-serif,system-ui,sans-serif;
                  scrollbar-width: thin; scrollbar-color: rgba(255,255,255,0.12) transparent; }}
    html::-webkit-scrollbar {{ width: 5px; }}
    html::-webkit-scrollbar-thumb {{ background: rgba(255,255,255,0.12); border-radius: 3px; }}
    html::-webkit-scrollbar-track {{ background: transparent; }}
    body {{ display: flex; flex-direction: column; }}
    .diagram   {{ flex: 1; overflow: auto; padding: 16px;
                  display: flex; justify-content: center; align-items: flex-start; }}
    .mermaid   {{ width: 100%; }}
    /* Force the Mermaid-rendered SVG to fill available width */
    .mermaid svg {{ width: 100% !important; height: auto !important;
                    max-width: none !important; background: transparent !important; }}
    .fallback  {{ padding: 20px; }}
    .fallback pre {{ font-size: 12px; color: #94a3b8; white-space: pre-wrap;
                     font-family: 'Cascadia Code','Fira Code',monospace;
                     background: #1e293b; border: 1px solid #334155;
                     border-radius: 8px; padding: 16px; }}
    .fallback-note {{ font-size: 12px; color: #f97316; margin-bottom: 12px; }}
  </style>
</head>
<body>
  <div class="diagram" style="{diagram_style}">
    <div class="mermaid">
{mermaid_src}
    </div>
  </div>
  <div class="fallback" style="{fallback_style}">
    <p class="fallback-note">Mermaid JS unavailable. Re-run the Architecture suite with network access to bundle it. Raw source:</p>
    <pre>{mermaid_src}</pre>
  </div>
  {script_block}
</body>
</html>"""


# ---------------------------------------------------------------------------
# Main run()
# ---------------------------------------------------------------------------

def run(base_url: str = "") -> TestRunner:
    runner = TestRunner("Architecture Diagrams (Mermaid)")
    os.makedirs(_OUTDIR, exist_ok=True)

    diagrams = [
        (
            "app_arch",
            "Application Architecture",
            "Flask app, blueprints, middleware, API registry and groups",
            _app_arch_mermaid,
        ),
        (
            "uc_flows",
            "Use Case -> API Flows",
            "Which use cases depend on which Mastercard APIs",
            _uc_flows_mermaid,
        ),
    ]

    for stem, title, subtitle, builder in diagrams:
        out_path = os.path.join(_OUTDIR, f"{stem}.html")
        try:
            mmd = builder()
            html = _render_html(title, subtitle, mmd)
            with open(out_path, "w", encoding="utf-8") as fh:
                fh.write(html)
            rel = os.path.relpath(out_path, _ROOT).replace("\\", "/")
            def _ok(rel=rel):
                pass
            runner.run(f"{stem}: written -> {rel}", _ok)
        except Exception as exc:
            def _fail(exc=exc, stem=stem):
                raise AssertionError(f"{stem} generation failed: {exc}")
            runner.run(f"{stem}: diagram generation", _fail)

    return runner


if __name__ == "__main__":
    r = run()
    r.print_summary()
    sys.exit(0 if r.failed() == 0 else 1)
