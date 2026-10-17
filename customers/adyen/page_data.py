"""Adyen, as a platform: the data behind ``Adyen_Platform.html``.

``python customers/build_page.py adyen`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Adyen_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from adyen_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from adyen_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Adyen'
PAGE = 'Adyen_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Adyen Platform"
KICKER = f"Adyen N.V. · as at {AS_OF}"
H1 = '<h1>Adyen <span class="os">Platform</span></h1>'
SERVES = 'who Adyen serves'

PALETTE_NOTE = ("Palette: Adyen's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Adyen's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Adyen's colours"

PIN = (52.37, 4.89, 'Amsterdam')
PIN_FACING = 'Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'digital': 'Digital', 'uc': 'Unified Commerce', 'platforms': 'Platforms', 'grp': 'Group'}
DIV = {'adyen': 'Adyen', 'emea': 'Adyen EMEA', 'na': 'Adyen North America', 'apac': 'Adyen APAC', 'latam': 'Adyen LATAM', 'talon': 'Talon.One', 'orb': 'Orb'}
DEFAULT_DIV = 'adyen'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F6F2", "panel-2": "#E6EFE7", "ink": "#0C1D11", "ink-2": "#253A2A",
    "muted": "#63796C", "faint": "#829188", "line": "#D1DCD5", "line-2": "#BBC8C0", "focus": "#09A748",
    "accent": "#09A748", "link": "#06783B", "gold": "#09A748", "gold-deep": "#066E36", "gold-ink": "#06783B",
    "l1": "#044823", "l2": "#066E36", "l3": "#179A56", "l4": "#40B06A", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#157B44", "l2f": "#0ABF53", "l3f": "#30C971", "l4f": "#89CB9D",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0C1D11", "shadow": "rgba(9,45,21,.22)", "wash-a": "rgba(10,191,83,.14)",
    "wash-b": "rgba(137,203,157,.10)", "gb2": "#157B44", "gb3": "#0ABF53", "gb4": "#A6DDB4", "brand-grad": "linear-gradient(90deg,#066E36,#0ABF53 55%,#A6DDB4)",
    "gold-grad": "linear-gradient(135deg,#A6DDB4 0%,#0ABF53 45%,#066E36 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0E0B", "panel": "#141D16", "panel-2": "#1E2A22", "ink": "#F3F7F3", "ink-2": "#D9E3DA",
    "muted": "#B5C1B9", "faint": "#99A49D", "line": "#3B4B41", "line-2": "#5D7165", "focus": "#0ABF53",
    "accent": "#0ABF53", "link": "#A6DDB4", "gold": "#0ABF53", "gold-deep": "#80D69B", "gold-ink": "#A6DDB4",
    "l1": "#A6DDB4", "l2": "#8CD4A2", "l3": "#99DEB7", "l4": "#B9E5C5", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#157B44", "l2f": "#0ABF53", "l3f": "#30C971", "l4f": "#89CB9D",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050806", "wash-a": "rgba(10,191,83,.12)", "wash-b": "rgba(137,203,157,.06)",
    "gb2": "#157B44", "gb3": "#0ABF53", "gb4": "#A6DDB4", "gold-grad": "linear-gradient(135deg,#C8EFD2 0%,#71CC8F 45%,#0ABF53 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
