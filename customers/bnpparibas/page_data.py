"""BNP Paribas, as a platform: the data behind ``BNP_Paribas_Platform.html``.

``python customers/build_page.py bnpparibas`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``BNP_Paribas_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bnpparibas_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bnpparibas_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BNP Paribas'
PAGE = 'BNP_Paribas_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BNP Paribas Platform"
KICKER = f"BNP Paribas · as at {AS_OF}"
H1 = '<h1>BNP Paribas <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BNP Paribas's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BNP Paribas's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BNP Paribas's colours"

PIN = (48.87, 2.33, 'Paris')
PIN_FACING = 'Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'cib': 'Corporate & Institutional Banking', 'cpbs': 'Commercial, Personal Banking & Services', 'ips': 'Investment & Protection Services', 'corp': 'Corporate Centre'}
DIV = {'group': 'BNP Paribas', 'france': 'BNP Paribas France', 'fortis': 'BNP Paribas Fortis', 'bnl': 'BNL', 'polska': 'BNP Paribas Bank Polska', 'pf': 'Personal Finance', 'nickel': 'Nickel', 'floa': 'Floa'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F3", "panel-2": "#E4EEE8", "ink": "#0A1A12", "ink-2": "#1B2D24",
    "muted": "#43544E", "faint": "#667570", "line": "#C8D6D1", "line-2": "#A9BCB5", "focus": "#008053",
    "accent": "#008053", "link": "#006245", "gold": "#008053", "gold-deep": "#00543B", "gold-ink": "#006245",
    "l1": "#003B2A", "l2": "#00543B", "l3": "#0A694F", "l4": "#2B8563", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0B5842", "l2f": "#008053", "l3f": "#1E9E74", "l4f": "#69C39B",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A1A12", "shadow": "rgba(6,39,25,.22)", "wash-a": "rgba(0,128,83,.14)",
    "wash-b": "rgba(105,195,155,.10)", "gb2": "#0B5842", "gb3": "#008053", "gb4": "#8DD8B3", "brand-grad": "linear-gradient(90deg,#00543B,#008053 55%,#8DD8B3)",
    "gold-grad": "linear-gradient(135deg,#8DD8B3 0%,#008053 45%,#00543B 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090D0B", "panel": "#111914", "panel-2": "#17221D", "ink": "#F2F7F4", "ink-2": "#D4E0D8",
    "muted": "#A2B3AD", "faint": "#808F8A", "line": "#283530", "line-2": "#3C4A45", "focus": "#5CD29E",
    "accent": "#49C691", "link": "#8DD8B3", "gold": "#49C691", "gold-deep": "#5CD29E", "gold-ink": "#8DD8B3",
    "l1": "#8DD8B3", "l2": "#6CCFA3", "l3": "#7DDBBD", "l4": "#A8E3C6", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0B5842", "l2f": "#008053", "l3f": "#1E9E74", "l4f": "#69C39B",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050806", "wash-a": "rgba(0,128,83,.12)", "wash-b": "rgba(105,195,155,.06)",
    "gb2": "#0B5842", "gb3": "#008053", "gb4": "#8DD8B3", "gold-grad": "linear-gradient(135deg,#BEF0D7 0%,#49C691 45%,#008053 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
