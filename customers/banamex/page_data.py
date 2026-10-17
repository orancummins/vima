"""Banamex, as a platform: the data behind ``Banamex_Platform.html``.

``python customers/build_page.py banamex`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Banamex_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from banamex_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from banamex_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Banamex'
PAGE = 'Banamex_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Banamex Platform"
KICKER = f"Grupo Financiero Banamex · as at {AS_OF}"
H1 = '<h1>Banamex <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Banamex's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Banamex's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Banamex's colours"

PIN = (19.36, -99.26, 'Mexico City')
PIN_FACING = 'Mexico'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'consumer': 'Consumer Banking', 'commercial': 'Commercial, Government & Institutional Banking', 'insurance': 'Insurance & Pensions', 'afore': 'Afore', 'group': 'Group & ownership'}
DIV = {'gfb': 'Grupo Financiero Banamex', 'bank': 'Banco Nacional de México', 'cards': 'Banamex cards', 'wealth': 'Wealth & Private Banking', 'seguros': 'Seguros Banamex', 'pensiones': 'Pensiones Banamex', 'afore': 'Afore Banamex'}
DEFAULT_DIV = 'gfb'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F7F2F4", "panel-2": "#F0E8EC", "ink": "#220D13", "ink-2": "#4B2E38",
    "muted": "#A0888C", "faint": "#AEA2A4", "line": "#E3D9DA", "line-2": "#D7CCCE", "focus": "#FF1B44",
    "accent": "#FF1B44", "link": "#BF0017", "gold": "#FF1B44", "gold-deep": "#980013", "gold-ink": "#BF0017",
    "l1": "#5D000C", "l2": "#980013", "l3": "#E0162A", "l4": "#CF687D", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#AD1527", "l2f": "#FF1B44", "l3f": "#E05E72", "l4f": "#DBA6B5",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#220D13", "shadow": "rgba(56,8,21,.22)", "wash-a": "rgba(255,27,68,.14)",
    "wash-b": "rgba(219,166,181,.10)", "gb2": "#AD1527", "gb3": "#FF1B44", "gb4": "#E8BBC9", "brand-grad": "linear-gradient(90deg,#980013,#FF1B44 55%,#E8BBC9)",
    "gold-grad": "linear-gradient(135deg,#E8BBC9 0%,#FF1B44 45%,#980013 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0B0C", "panel": "#22171B", "panel-2": "#352429", "ink": "#F8F3F5", "ink-2": "#E7DEE2",
    "muted": "#D1C8C9", "faint": "#BCB3B5", "line": "#654D51", "line-2": "#9B8387", "focus": "#FF1B44",
    "accent": "#FF1B44", "link": "#E8BBC9", "gold": "#FF1B44", "gold-deep": "#E49EB1", "gold-ink": "#E8BBC9",
    "l1": "#E8BBC9", "l2": "#E2A7B8", "l3": "#EAB1BA", "l4": "#EDC7D3", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#AD1527", "l2f": "#FF1B44", "l3f": "#E05E72", "l4f": "#DBA6B5",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090607", "wash-a": "rgba(255,27,68,.12)", "wash-b": "rgba(219,166,181,.06)",
    "gb2": "#AD1527", "gb3": "#FF1B44", "gb4": "#E8BBC9", "gold-grad": "linear-gradient(135deg,#F4CFDB 0%,#DD92A5 45%,#FF1B44 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
