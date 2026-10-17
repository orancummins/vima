"""Itaú, as a platform: the data behind ``Itau_Platform.html``.

``python customers/build_page.py itau`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Itau_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from itau_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from itau_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = "Itaú"
PAGE = "Itau_Platform.html"
AS_OF = "17 October 2026"
TITLE = "Itaú Platform"
KICKER = f"Itaú Unibanco · as at {AS_OF}"
H1 = '<h1>Itaú <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Itaú's navy for the bank, from the deep foundation to the bright access layer, graphite for the people, Itaú\n"
                "   orange only in the brand strip, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = 'the five slices: foundation (deep navy), rails (Itaú blue), services (azure), lines (periwinkle), access (graphite); graphite for the people'
GLOBE_NOTE = "the globe: Itaú's navy, blue and azure"

PIN = (-23.55, -46.63, 'São Paulo')
PIN_FACING = 'South America'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
# Itaú reports Retail Business, Wholesale Business, and Activities with the Market + Corporation.
REV = {"retail": "Retail Business", "wholesale": "Wholesale Business", "corp": "Activities with the Market + Corporation"}
DIV = {"iuh": "Itaú Unibanco Holding", "retail": "Itaú (retail)", "cards": "Itaucard", "rede": "Rede",
       "sme": "Itaú Empresas", "bba": "Itaú BBA", "wms": "Itaú Private & Asset", "latam": "Itaú Latin America"}
DEFAULT_DIV = "iuh"

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F3F5FA", "panel-2": "#E6EAF4", "ink": "#0B1433", "ink-2": "#1D2A52",
    "muted": "#475373", "faint": "#6A7592", "line": "#CDD4E5", "line-2": "#B0BAD2", "focus": "#1F3FA8",
    "accent": "#1F3FA8", "link": "#152F86", "gold": "#EC7000", "gold-deep": "#002B7F", "gold-ink": "#152F86",
    "l1": "#001F5C", "l2": "#002B7F", "l3": "#1F3FA8", "l4": "#4766C7", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0E2A6E", "l2f": "#1F3FA8", "l3f": "#3D5FD0", "l4f": "#8299E3",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#EBF0FF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B1A4D", "l5t": "#FFFFFF", "slot": "#0B1433", "shadow": "rgba(8,20,60,.22)", "wash-a": "rgba(31,63,168,.14)",
    "wash-b": "rgba(236,112,0,.07)", "gb2": "#0E2A6E", "gb3": "#1F3FA8", "gb4": "#A9BCF5", "brand-grad": "linear-gradient(90deg,#002B7F,#1F3FA8 55%,#EC7000)",
    "gold-grad": "linear-gradient(135deg,#A9BCF5 0%,#1F3FA8 45%,#002B7F 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090C16", "panel": "#111628", "panel-2": "#181F3A", "ink": "#F2F4FB", "ink-2": "#D5DAEC",
    "muted": "#A3ACC7", "faint": "#8089A6", "line": "#29304C", "line-2": "#3D4669", "focus": "#8FA6F0",
    "accent": "#7B95EC", "link": "#A9BCF5", "gold": "#FF9A3D", "gold-deep": "#8FA6F0", "gold-ink": "#A9BCF5",
    "l1": "#A9BCF5", "l2": "#8FA6F0", "l3": "#9DB2F5", "l4": "#C0CDF7", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0E2A6E", "l2f": "#1F3FA8", "l3f": "#3D5FD0", "l4f": "#8299E3",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#05070D", "wash-a": "rgba(31,63,168,.12)", "wash-b": "rgba(236,112,0,.06)",
    "gb2": "#0E2A6E", "gb3": "#1F3FA8", "gb4": "#A9BCF5", "gold-grad": "linear-gradient(135deg,#D2DCFA 0%,#7B95EC 45%,#1F3FA8 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
