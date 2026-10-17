"""SBI Card, as a platform: the data behind ``SBI_Card_Platform.html``.

``python customers/build_page.py sbicard`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``SBI_Card_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from sbicard_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from sbicard_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'SBI Card'
PAGE = 'SBI_Card_Platform.html'
AS_OF = "17 October 2026"
TITLE = "SBI Card Platform"
KICKER = f"SBI Cards and Payment Services · as at {AS_OF}"
H1 = '<h1>SBI Card <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: SBI Card's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in SBI Card's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in SBI Card's colours"

PIN = (28.46, 77.03, 'Gurugram')
PIN_FACING = 'India and Asia-Pacific'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail cards', 'corporate': 'Corporate cards', 'central': 'Company & treasury'}
DIV = {'sbicard': 'SBI Card', 'sbi': 'State Bank of India', 'platform': 'Digital-platform co-brands', 'travel': 'Travel & fuel co-brands', 'banks': 'Partner-bank cards', 'corp': 'Corporate cards'}
DEFAULT_DIV = 'sbicard'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F3F5", "panel-2": "#E6E9EC", "ink": "#0D1018", "ink-2": "#21252D",
    "muted": "#4F515C", "faint": "#70717B", "line": "#CDCED6", "line-2": "#B1B3BC", "focus": "#1A287B",
    "accent": "#1A287B", "link": "#13195B", "gold": "#1A287B", "gold-deep": "#10164D", "gold-ink": "#13195B",
    "l1": "#0B0F35", "l2": "#10164D", "l3": "#1F2466", "l4": "#404C82", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#1B2054", "l2f": "#1A287B", "l3f": "#394494", "l4f": "#808EB7",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0D1018", "shadow": "rgba(12,17,35,.22)", "wash-a": "rgba(26,40,123,.14)",
    "wash-b": "rgba(128,142,183,.10)", "gb2": "#1B2054", "gb3": "#1A287B", "gb4": "#A0ADCE", "brand-grad": "linear-gradient(90deg,#10164D,#1A287B 55%,#A0ADCE)",
    "gold-grad": "linear-gradient(135deg,#A0ADCE 0%,#1A287B 45%,#10164D 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0B0D", "panel": "#131518", "panel-2": "#1B1D23", "ink": "#F3F4F6", "ink-2": "#D7DADF",
    "muted": "#AAACB4", "faint": "#898B93", "line": "#303139", "line-2": "#484A53", "focus": "#7889C1",
    "accent": "#6778B4", "link": "#A0ADCE", "gold": "#6778B4", "gold-deep": "#7889C1", "gold-ink": "#A0ADCE",
    "l1": "#A0ADCE", "l2": "#8594C1", "l3": "#939ACE", "l4": "#B6C0DA", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#1B2054", "l2f": "#1A287B", "l3f": "#394494", "l4f": "#808EB7",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060708", "wash-a": "rgba(26,40,123,.12)", "wash-b": "rgba(128,142,183,.06)",
    "gb2": "#1B2054", "gb3": "#1A287B", "gb4": "#A0ADCE", "gold-grad": "linear-gradient(135deg,#C9D2E8 0%,#6778B4 45%,#1A287B 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
