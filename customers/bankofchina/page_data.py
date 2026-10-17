"""Bank of China, as a platform: the data behind ``Bank_of_China_Platform.html``.

``python customers/build_page.py bankofchina`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Bank_of_China_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bankofchina_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bankofchina_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BOC'
PAGE = 'Bank_of_China_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BOC Platform"
KICKER = f"Bank of China · as at {AS_OF}"
H1 = '<h1>BOC <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BOC's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BOC's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BOC's colours"

PIN = (39.91, 116.36, 'Beijing')
PIN_FACING = 'China and the world'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'corporate': 'Corporate banking', 'personal': 'Personal banking', 'treasury': 'Treasury operations', 'ibins': 'Investment banking & insurance', 'other': 'Others'}
DIV = {'boc': 'Bank of China', 'cards': 'BOC Bank Card Centre (Great Wall)', 'bochk': 'BOC Hong Kong', 'hkcards': 'BOC Credit Card (International)', 'boci': 'BOCI & insurance', 'subs': 'Other subsidiaries', 'overseas': 'Overseas branches'}
DEFAULT_DIV = 'boc'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F4", "panel-2": "#EEE6EA", "ink": "#1C0C11", "ink-2": "#37232B",
    "muted": "#725D62", "faint": "#8C7C80", "line": "#DACFD2", "line-2": "#C5B7BB", "focus": "#B10A32",
    "accent": "#B10A32", "link": "#7E071D", "gold": "#B10A32", "gold-deep": "#680618", "gold-ink": "#7E071D",
    "l1": "#440410", "l2": "#680618", "l3": "#8F1629", "l4": "#A63D59", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#731425", "l2f": "#B10A32", "l3f": "#BF2F4E", "l4f": "#C8849B",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1C0C11", "shadow": "rgba(43,9,20,.22)", "wash-a": "rgba(177,10,50,.14)",
    "wash-b": "rgba(200,132,155,.10)", "gb2": "#731425", "gb3": "#B10A32", "gb4": "#DBA2B8", "brand-grad": "linear-gradient(90deg,#680618,#B10A32 55%,#DBA2B8)",
    "gold-grad": "linear-gradient(135deg,#DBA2B8 0%,#B10A32 45%,#680618 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0E0A0B", "panel": "#1C1417", "panel-2": "#291D21", "ink": "#F7F3F5", "ink-2": "#E2D8DD",
    "muted": "#BEB1B4", "faint": "#A09497", "line": "#46373B", "line-2": "#69575B", "focus": "#D47B98",
    "accent": "#C96A88", "link": "#DBA2B8", "gold": "#C96A88", "gold-deep": "#D47B98", "gold-ink": "#DBA2B8",
    "l1": "#DBA2B8", "l2": "#D287A1", "l3": "#DD95A4", "l4": "#E4B6C7", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#731425", "l2f": "#B10A32", "l3f": "#BF2F4E", "l4f": "#C8849B",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080507", "wash-a": "rgba(177,10,50,.12)", "wash-b": "rgba(200,132,155,.06)",
    "gb2": "#731425", "gb3": "#B10A32", "gb4": "#DBA2B8", "gold-grad": "linear-gradient(135deg,#EFC7D7 0%,#C96A88 45%,#B10A32 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
