"""Bank Central Asia (BCA), as a platform: the data behind ``Bank_Central_Asia_BCA_Platform.html``.

``python customers/build_page.py bca`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Bank_Central_Asia_BCA_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bca_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bca_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BCA'
PAGE = 'Bank_Central_Asia_BCA_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BCA Platform"
KICKER = f"PT Bank Central Asia Tbk · as at {AS_OF}"
H1 = '<h1>BCA <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BCA's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BCA's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BCA's colours"

PIN = (-6.2, 106.82, 'Jakarta')
PIN_FACING = 'Indonesia and South-East Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'corp': 'Corporate', 'comm': 'Commercial & SME', 'cons': 'Consumer', 'txn': 'Transaction banking', 'grp': 'Group & subsidiaries'}
DIV = {'bca': 'BCA', 'blu': 'BCA Digital (blu)', 'syariah': 'BCA Syariah', 'finance': 'BCA Finance', 'sekuritas': 'BCA Sekuritas', 'insure': 'BCA Insurance & BCA Life', 'ccv': 'Central Capital Ventura'}
DEFAULT_DIV = 'bca'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F5F6", "panel-2": "#E5EDEF", "ink": "#0B161C", "ink-2": "#202F35",
    "muted": "#55616B", "faint": "#757E87", "line": "#CDD4DA", "line-2": "#B3BCC3", "focus": "#005CAB",
    "accent": "#005CAB", "link": "#003B7C", "gold": "#005CAB", "gold-deep": "#003167", "gold-ink": "#003B7C",
    "l1": "#002145", "l2": "#003167", "l3": "#0E478A", "l4": "#3472A2", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0D3C70", "l2f": "#005CAB", "l3f": "#2473BC", "l4f": "#7AADCA",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0B161C", "shadow": "rgba(7,30,44,.22)", "wash-a": "rgba(0,92,171,.14)",
    "wash-b": "rgba(122,173,202,.10)", "gb2": "#0D3C70", "gb3": "#005CAB", "gb4": "#9AC7DD", "brand-grad": "linear-gradient(90deg,#003167,#005CAB 55%,#9AC7DD)",
    "gold-grad": "linear-gradient(135deg,#9AC7DD 0%,#005CAB 45%,#003167 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090C0E", "panel": "#12191B", "panel-2": "#1B2327", "ink": "#F2F6F7", "ink-2": "#D6DFE2",
    "muted": "#ADB5BB", "faint": "#8E959C", "line": "#333B42", "line-2": "#4F5962", "focus": "#6EB0D7",
    "accent": "#5DA1CC", "link": "#9AC7DD", "gold": "#5DA1CC", "gold-deep": "#6EB0D7", "gold-ink": "#9AC7DD",
    "l1": "#9AC7DD", "l2": "#7DB5D5", "l3": "#8BB6DF", "l4": "#B0D4E5", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0D3C70", "l2f": "#005CAB", "l3f": "#2473BC", "l4f": "#7AADCA",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,92,171,.12)", "wash-b": "rgba(122,173,202,.06)",
    "gb2": "#0D3C70", "gb3": "#005CAB", "gb4": "#9AC7DD", "gold-grad": "linear-gradient(135deg,#C3E3F1 0%,#5DA1CC 45%,#005CAB 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
