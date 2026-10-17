"""PKO Bank Polski, as a platform: the data behind ``PKO_Bank_Polski_Platform.html``.

``python customers/build_page.py pko`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``PKO_Bank_Polski_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from pko_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from pko_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'PKO'
PAGE = 'PKO_Bank_Polski_Platform.html'
AS_OF = "17 October 2026"
TITLE = "PKO Platform"
KICKER = f"PKO Bank Polski · as at {AS_OF}"
H1 = '<h1>PKO <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: PKO's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in PKO's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in PKO's colours"

PIN = (52.23, 21.01, 'Warsaw')
PIN_FACING = 'Poland and Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail', 'corp': 'Corporate & Investment', 'tc': 'Transfer centre & other'}
DIV = {'pko': 'PKO Bank Polski', 'hipo': 'PKO Bank Hipoteczny', 'leasing': 'PKO Leasing', 'tfi': 'PKO TFI', 'ins': 'PKO Życie & PKO TU', 'kredo': 'KREDOBANK', 'blik': 'BLIK (PSP)'}
DEFAULT_DIV = 'pko'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F2F6", "panel-2": "#E3E6ED", "ink": "#090B18", "ink-2": "#181B27",
    "muted": "#383847", "faint": "#5C5C6B", "line": "#C5C5D4", "line-2": "#A4A4B7", "focus": "#000066",
    "accent": "#000066", "link": "#050052", "gold": "#000066", "gold-deep": "#040048", "gold-ink": "#050052",
    "l1": "#030036", "l2": "#040048", "l3": "#0F0854", "l4": "#252774", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0D094A", "l2f": "#000066", "l3f": "#1D1B8C", "l4f": "#5F68BF",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#090B18", "shadow": "rgba(5,8,36,.22)", "wash-a": "rgba(0,0,102,.14)",
    "wash-b": "rgba(95,104,191,.10)", "gb2": "#0D094A", "gb3": "#000066", "gb4": "#8590D6", "brand-grad": "linear-gradient(90deg,#040048,#000066 55%,#8590D6)",
    "gold-grad": "linear-gradient(135deg,#8590D6 0%,#000066 45%,#040048 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#09090C", "panel": "#101117", "panel-2": "#15161F", "ink": "#F2F3F7", "ink-2": "#D2D5DE",
    "muted": "#9C9CAD", "faint": "#777787", "line": "#22222D", "line-2": "#353542", "focus": "#656FD5",
    "accent": "#686FCF", "link": "#8590D6", "gold": "#686FCF", "gold-deep": "#656FD5", "gold-ink": "#8590D6",
    "l1": "#8590D6", "l2": "#6671CD", "l3": "#7774D9", "l4": "#A2ABE1", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0D094A", "l2f": "#000066", "l3f": "#1D1B8C", "l4f": "#5F68BF",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050608", "wash-a": "rgba(0,0,102,.12)", "wash-b": "rgba(95,104,191,.06)",
    "gb2": "#0D094A", "gb3": "#000066", "gb4": "#8590D6", "gold-grad": "linear-gradient(135deg,#BCC4EF 0%,#3D46C2 45%,#000066 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
