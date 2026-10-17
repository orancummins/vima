"""CRDB Bank, as a platform: the data behind ``CRDB_Bank_Platform.html``.

``python customers/build_page.py crdb`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``CRDB_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from crdb_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from crdb_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'CRDB'
PAGE = 'CRDB_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "CRDB Platform"
KICKER = f"CRDB Bank Plc · as at {AS_OF}"
H1 = '<h1>CRDB <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: CRDB's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in CRDB's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in CRDB's colours"

PIN = (-6.82, 39.28, 'Dar es Salaam')
PIN_FACING = 'Tanzania and East Africa'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'corp': 'Corporate Banking', 'retail': 'Retail Banking', 'treasury': 'Treasury', 'ins': 'Insurance'}
DIV = {'crdb': 'CRDB Bank Tanzania', 'barakah': 'Al Barakah Banking', 'burundi': 'CRDB Bank Burundi', 'drc': 'CRDB Bank Congo', 'cic': 'CRDB Insurance', 'found': 'CRDB Bank Foundation', 'dubai': 'CRDB Dubai (DIFC)'}
DEFAULT_DIV = 'crdb'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F4F5F2", "panel-2": "#EAEEE8", "ink": "#131B0F", "ink-2": "#303A2B",
    "muted": "#626E60", "faint": "#80897E", "line": "#D5DBD4", "line-2": "#C2C9C0", "focus": "#40A828",
    "accent": "#40A828", "link": "#297B1D", "gold": "#40A828", "gold-deep": "#226418", "gold-ink": "#297B1D",
    "l1": "#16400F", "l2": "#226418", "l3": "#3A9030", "l4": "#68A857", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#317228", "l2f": "#43B02A", "l3f": "#61B751", "l4f": "#A6C49A",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#131B0F", "shadow": "rgba(22,41,15,.22)", "wash-a": "rgba(67,176,42,.14)",
    "wash-b": "rgba(166,196,154,.10)", "gb2": "#317228", "gb3": "#43B02A", "gb4": "#BED6B3", "brand-grad": "linear-gradient(90deg,#226418,#43B02A 55%,#BED6B3)",
    "gold-grad": "linear-gradient(135deg,#BED6B3 0%,#43B02A 45%,#226418 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0C0E0B", "panel": "#181C16", "panel-2": "#242A22", "ink": "#F5F6F3", "ink-2": "#DEE2DC",
    "muted": "#BCC2BB", "faint": "#A1A7A0", "line": "#444D41", "line-2": "#6B7768", "focus": "#43B02A",
    "accent": "#43B02A", "link": "#BED6B3", "gold": "#43B02A", "gold-deep": "#A3CB94", "gold-ink": "#BED6B3",
    "l1": "#BED6B3", "l2": "#ABCC9D", "l3": "#B0D6A9", "l4": "#CCE0C3", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#317228", "l2f": "#43B02A", "l3f": "#61B751", "l4f": "#A6C49A",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#070806", "wash-a": "rgba(67,176,42,.12)", "wash-b": "rgba(166,196,154,.06)",
    "gb2": "#317228", "gb3": "#43B02A", "gb4": "#BED6B3", "gold-grad": "linear-gradient(135deg,#D9EAD0 0%,#95C186 45%,#43B02A 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
