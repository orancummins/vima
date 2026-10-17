"""Golomt Bank, as a platform: the data behind ``Golomt_Bank_Platform.html``.

``python customers/build_page.py golomt`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Golomt_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from golomt_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from golomt_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Golomt'
PAGE = 'Golomt_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Golomt Platform"
KICKER = f"Golomt Bank · as at {AS_OF}"
H1 = '<h1>Golomt <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Golomt's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Golomt's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Golomt's colours"

PIN = (47.92, 106.92, 'Ulaanbaatar')
PIN_FACING = 'Mongolia and East Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'corp': 'Corporate banking', 'sme': 'SME banking', 'retail': 'Retail banking', 'treasury': 'Treasury & international'}
DIV = {'golomt': 'Golomt Bank', 'gfg': 'Golomt Financial Group', 'socialpay': 'SocialPay', 'universe': 'Universe cards', 'premiere': 'Premiere Banking', 'intl': 'International Banking'}
DEFAULT_DIV = 'golomt'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F5F6", "panel-2": "#E5EDEF", "ink": "#0B161C", "ink-2": "#213037",
    "muted": "#58656F", "faint": "#78828A", "line": "#CED5DA", "line-2": "#B5BDC5", "focus": "#0061B3",
    "accent": "#0061B3", "link": "#003E81", "gold": "#0061B3", "gold-deep": "#00346A", "gold-ink": "#003E81",
    "l1": "#002247", "l2": "#00346A", "l3": "#0E4A90", "l4": "#3576A7", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0E3F74", "l2f": "#0061B3", "l3f": "#2577C2", "l4f": "#7DAFCB",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0B161C", "shadow": "rgba(7,30,45,.22)", "wash-a": "rgba(0,97,179,.14)",
    "wash-b": "rgba(125,175,203,.10)", "gb2": "#0E3F74", "gb3": "#0061B3", "gb4": "#9CC9DD", "brand-grad": "linear-gradient(90deg,#00346A,#0061B3 55%,#9CC9DD)",
    "gold-grad": "linear-gradient(135deg,#9CC9DD 0%,#0061B3 45%,#00346A 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0C0E", "panel": "#13191C", "panel-2": "#1C2428", "ink": "#F2F6F7", "ink-2": "#D7E0E2",
    "muted": "#AFB6BD", "faint": "#91989E", "line": "#343D45", "line-2": "#525D66", "focus": "#72B2D8",
    "accent": "#61A4CE", "link": "#9CC9DD", "gold": "#61A4CE", "gold-deep": "#72B2D8", "gold-ink": "#9CC9DD",
    "l1": "#9CC9DD", "l2": "#80B7D6", "l3": "#8EB8E0", "l4": "#B2D5E6", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0E3F74", "l2f": "#0061B3", "l3f": "#2577C2", "l4f": "#7DAFCB",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,97,179,.12)", "wash-b": "rgba(125,175,203,.06)",
    "gb2": "#0E3F74", "gb3": "#0061B3", "gb4": "#9CC9DD", "gold-grad": "linear-gradient(135deg,#C4E3F1 0%,#61A4CE 45%,#0061B3 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
