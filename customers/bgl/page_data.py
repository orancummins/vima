"""BGL BNP Paribas, as a platform: the data behind ``BGL_BNP_Paribas_Platform.html``.

``python customers/build_page.py bgl`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``BGL_BNP_Paribas_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bgl_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bgl_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BGL'
PAGE = 'BGL_BNP_Paribas_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BGL Platform"
KICKER = f"BGL BNP Paribas · as at {AS_OF}"
H1 = '<h1>BGL <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BGL's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BGL's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BGL's colours"

PIN = (49.63, 6.16, 'Luxembourg')
PIN_FACING = 'Luxembourg and the Greater Region'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'rcb': 'Retail & Corporate Banking', 'wm': 'Wealth Management', 'lease': 'Leasing International', 'cc': 'Corporate centre'}
DIV = {'bgl': 'BGL BNP Paribas', 'retail': 'Retail banking', 'private': 'Private banking', 'ent': 'Corporate & professional banking', 'leasing': 'BNP Paribas Leasing Solutions', 'cardif': 'Cardif Lux Vie', 'group': 'BNP Paribas Group'}
DEFAULT_DIV = 'bgl'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F3", "panel-2": "#E4EEE8", "ink": "#0A1B13", "ink-2": "#1D3026",
    "muted": "#4A5D56", "faint": "#6C7C76", "line": "#CAD8D3", "line-2": "#ADBFB8", "focus": "#00915A",
    "accent": "#00915A", "link": "#006C49", "gold": "#00915A", "gold-deep": "#005B3E", "gold-ink": "#006C49",
    "l1": "#003F2B", "l2": "#005B3E", "l3": "#0C7656", "l4": "#2E9168", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0C6246", "l2f": "#00915A", "l3f": "#20AA79", "l4f": "#70C69D",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0A1B13", "shadow": "rgba(6,41,25,.22)", "wash-a": "rgba(0,145,90,.14)",
    "wash-b": "rgba(112,198,157,.10)", "gb2": "#0C6246", "gb3": "#00915A", "gb4": "#92DAB5", "brand-grad": "linear-gradient(90deg,#005B3E,#00915A 55%,#92DAB5)",
    "gold-grad": "linear-gradient(135deg,#92DAB5 0%,#00915A 45%,#005B3E 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090D0B", "panel": "#111A15", "panel-2": "#19241F", "ink": "#F2F7F4", "ink-2": "#D5E0D9",
    "muted": "#A6B6B0", "faint": "#85948E", "line": "#2C3A35", "line-2": "#43534D", "focus": "#00915A",
    "accent": "#00915A", "link": "#92DAB5", "gold": "#00915A", "gold-deep": "#63D49F", "gold-ink": "#92DAB5",
    "l1": "#92DAB5", "l2": "#73D1A4", "l3": "#82DDBE", "l4": "#ABE4C7", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0C6246", "l2f": "#00915A", "l3f": "#20AA79", "l4f": "#70C69D",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050806", "wash-a": "rgba(0,145,90,.12)", "wash-b": "rgba(112,198,157,.06)",
    "gb2": "#0C6246", "gb3": "#00915A", "gb4": "#92DAB5", "gold-grad": "linear-gradient(135deg,#C0F0D6 0%,#51C892 45%,#00915A 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
