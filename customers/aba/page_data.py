"""ABA Bank, as a platform: the data behind ``ABA_Bank_Platform.html``.

``python customers/build_page.py aba`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``ABA_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from aba_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from aba_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'ABA'
PAGE = 'ABA_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "ABA Platform"
KICKER = f"ABA Bank (Advanced Bank of Asia) · as at {AS_OF}"
H1 = '<h1>ABA <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: ABA's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in ABA's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in ABA's colours"

PIN = (11.56, 104.92, 'Phnom Penh')
PIN_FACING = 'Cambodia and Southeast Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail banking', 'sme': 'SME banking', 'corp': 'Corporate & investment banking', 'pay': 'Payments & cards'}
DIV = {'aba': 'ABA Bank', 'mobile': 'ABA Mobile', 'abapay': 'ABA PAY & KHQR', 'payway': 'ABA PayWay', 'business': 'ABA Business', 'parent': 'National Bank of Canada Group'}
DEFAULT_DIV = 'aba'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F6", "panel-2": "#E4EEEE", "ink": "#0A171A", "ink-2": "#1C2B2E",
    "muted": "#465257", "faint": "#687378", "line": "#C9D3D7", "line-2": "#ABB7BD", "focus": "#005D86",
    "accent": "#005D86", "link": "#004065", "gold": "#005D86", "gold-deep": "#003757", "gold-ink": "#004065",
    "l1": "#00273D", "l2": "#003757", "l3": "#0B476D", "l4": "#2C6F89", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0B3E5B", "l2f": "#005D86", "l3f": "#1F77A2", "l4f": "#6CB2C4",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A171A", "shadow": "rgba(6,32,40,.22)", "wash-a": "rgba(0,93,134,.14)",
    "wash-b": "rgba(108,178,196,.10)", "gb2": "#0B3E5B", "gb3": "#005D86", "gb4": "#8FCDD9", "brand-grad": "linear-gradient(90deg,#003757,#005D86 55%,#8FCDD9)",
    "gold-grad": "linear-gradient(135deg,#8FCDD9 0%,#005D86 45%,#003757 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090C0D", "panel": "#111819", "panel-2": "#182123", "ink": "#F2F7F7", "ink-2": "#D4DFE0",
    "muted": "#A4AFB4", "faint": "#828C91", "line": "#2A3337", "line-2": "#3F494D", "focus": "#5FBAD3",
    "accent": "#4CAAC7", "link": "#8FCDD9", "gold": "#4CAAC7", "gold-deep": "#5FBAD3", "gold-ink": "#8FCDD9",
    "l1": "#8FCDD9", "l2": "#6FBCD0", "l3": "#7FBCDC", "l4": "#A9D9E3", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0B3E5B", "l2f": "#005D86", "l3f": "#1F77A2", "l4f": "#6CB2C4",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,93,134,.12)", "wash-b": "rgba(108,178,196,.06)",
    "gb2": "#0B3E5B", "gb3": "#005D86", "gb4": "#8FCDD9", "gold-grad": "linear-gradient(135deg,#BFE9F0 0%,#4CAAC7 45%,#005D86 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
