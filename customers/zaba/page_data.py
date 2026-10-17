"""Zagrebačka banka, as a platform: the data behind ``Zagrebacka_banka_Platform.html``.

``python customers/build_page.py zaba`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Zagrebacka_banka_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from zaba_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from zaba_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Zaba'
PAGE = 'Zagrebacka_banka_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Zaba Platform"
KICKER = f"Zagrebačka banka · UniCredit · as at {AS_OF}"
H1 = '<h1>Zaba <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Zaba's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Zaba's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Zaba's colours"

PIN = (45.81, 15.98, 'Zagreb')
PIN_FACING = 'Croatia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail & Prime', 'sme': 'Small business', 'corp': 'Corporate & investment banking', 'subs': 'Subsidiaries (funds, leasing, Bosnia)'}
DIV = {'zaba': 'Zagrebačka banka', 'cards': 'Zaba cards & payments', 'digital': 'm-zaba & e-zaba', 'ucinv': 'UniCredit Invest', 'leasing': 'UniCredit Leasing Croatia', 'mostar': 'UniCredit Bank Mostar', 'uc': 'UniCredit Group'}
DEFAULT_DIV = 'zaba'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F3", "panel-2": "#F0E8EA", "ink": "#200E0F", "ink-2": "#472F31",
    "muted": "#776462", "faint": "#918282", "line": "#E1D9D8", "line-2": "#D3C9C8", "focus": "#EE3124",
    "accent": "#EE3124", "link": "#AD210D", "gold": "#EE3124", "gold-deep": "#891A0B", "gold-ink": "#AD210D",
    "l1": "#541007", "l2": "#891A0B", "l3": "#CB3C24", "l4": "#C56D6A", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#9E2F1F", "l2f": "#EE3124", "l3f": "#D56C62", "l4f": "#D6A6A8",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#200E0F", "shadow": "rgba(52,12,12,.22)", "wash-a": "rgba(238,49,36,.14)",
    "wash-b": "rgba(214,166,168,.10)", "gb2": "#9E2F1F", "gb3": "#EE3124", "gb4": "#E4BCBF", "brand-grad": "linear-gradient(90deg,#891A0B,#EE3124 55%,#E4BCBF)",
    "gold-grad": "linear-gradient(135deg,#E4BCBF 0%,#EE3124 45%,#891A0B 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0B0B", "panel": "#211818", "panel-2": "#332525", "ink": "#F7F3F4", "ink-2": "#E6DEDF",
    "muted": "#CFC7C6", "faint": "#B9B2B1", "line": "#604E4D", "line-2": "#958280", "focus": "#EE3124",
    "accent": "#EE3124", "link": "#E4BCBF", "gold": "#EE3124", "gold-deep": "#DEA0A1", "gold-ink": "#E4BCBF",
    "l1": "#E4BCBF", "l2": "#DDA9AB", "l3": "#E5B8B3", "l4": "#E9C8CB", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#9E2F1F", "l2f": "#EE3124", "l3f": "#D56C62", "l4f": "#D6A6A8",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090607", "wash-a": "rgba(238,49,36,.12)", "wash-b": "rgba(214,166,168,.06)",
    "gb2": "#9E2F1F", "gb3": "#EE3124", "gb4": "#E4BCBF", "gold-grad": "linear-gradient(135deg,#F1D0D3 0%,#D69495 45%,#EE3124 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
