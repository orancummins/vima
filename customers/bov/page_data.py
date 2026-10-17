"""Bank of Valletta, as a platform: the data behind ``Bank_of_Valletta_Platform.html``.

``python customers/build_page.py bov`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Bank_of_Valletta_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bov_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bov_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BOV'
PAGE = 'Bank_of_Valletta_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BOV Platform"
KICKER = f"Bank of Valletta · as at {AS_OF}"
H1 = '<h1>BOV <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BOV's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BOV's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BOV's colours"

PIN = (35.9, 14.51, 'Valletta')
PIN_FACING = 'Malta and the EU'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail Banking', 'wealth': 'Wealth Management', 'business': 'Business Banking', 'treasury': 'Treasury', 'others': 'Others'}
DIV = {'bov': 'Bank of Valletta', 'cards': 'BOV Cards', 'smartpay': 'BOV SmartPay', 'digital': 'BOV Mobile & Internet Banking', 'funds': 'Valletta Fund Management & Fund Services', 'mapfre': 'Mapfre MSV Life & Mapfre Malta'}
DEFAULT_DIV = 'bov'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F1F5", "panel-2": "#EEE4EC", "ink": "#1A0A15", "ink-2": "#301D2A",
    "muted": "#5C4A54", "faint": "#7B6B74", "line": "#D8CAD2", "line-2": "#BEADB7", "focus": "#8E0250",
    "accent": "#8E0250", "link": "#6A0136", "gold": "#8E0250", "gold-deep": "#5A012D", "gold-ink": "#6A0136",
    "l1": "#3E0120", "l2": "#5A012D", "l3": "#730D3E", "l4": "#8F2F67", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#600D36", "l2f": "#8E0250", "l3f": "#A72269", "l4f": "#C471A7",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1A0A15", "shadow": "rgba(40,7,28,.22)", "wash-a": "rgba(142,2,80,.14)",
    "wash-b": "rgba(196,113,167,.10)", "gb2": "#600D36", "gb3": "#8E0250", "gb4": "#D993C4", "brand-grad": "linear-gradient(90deg,#5A012D,#8E0250 55%,#D993C4)",
    "gold-grad": "linear-gradient(135deg,#D993C4 0%,#8E0250 45%,#5A012D 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0D090C", "panel": "#191117", "panel-2": "#241920", "ink": "#F7F2F6", "ink-2": "#E0D5DE",
    "muted": "#B6A6AF", "faint": "#93858D", "line": "#3A2C34", "line-2": "#53434C", "focus": "#D264AC",
    "accent": "#C7529C", "link": "#D993C4", "gold": "#C7529C", "gold-deep": "#D264AC", "gold-ink": "#D993C4",
    "l1": "#D993C4", "l2": "#D074B0", "l3": "#DC83B2", "l4": "#E3ACD2", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#600D36", "l2f": "#8E0250", "l3f": "#A72269", "l4f": "#C471A7",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080508", "wash-a": "rgba(142,2,80,.12)", "wash-b": "rgba(196,113,167,.06)",
    "gb2": "#600D36", "gb3": "#8E0250", "gb4": "#D993C4", "gold-grad": "linear-gradient(135deg,#F0C1E2 0%,#C7529C 45%,#8E0250 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
