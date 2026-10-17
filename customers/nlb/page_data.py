"""NLB Group, as a platform: the data behind ``NLB_Platform.html``.

``python customers/build_page.py nlb`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``NLB_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from nlb_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from nlb_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'NLB'
PAGE = 'NLB_Platform.html'
AS_OF = "17 October 2026"
TITLE = "NLB Platform"
KICKER = f"NLB Group (Nova Ljubljanska banka) · as at {AS_OF}"
H1 = '<h1>NLB <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: NLB's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in NLB's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in NLB's colours"

PIN = (46.05, 14.51, 'Ljubljana')
PIN_FACING = 'Slovenia and the Western Balkans'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail banking in Slovenia', 'cib': 'Corporate & investment banking in Slovenia', 'fm': 'Financial markets in Slovenia', 'sfm': 'Strategic foreign markets', 'other': 'Other activities & non-core'}
DIV = {'group': 'NLB Group', 'nlb': 'NLB (Slovenia)', 'kb': 'NLB Komercijalna banka (Serbia)', 'skopje': 'NLB Banka Skopje', 'bih': 'NLB Banka Banja Luka & Sarajevo', 'prishtina': 'NLB Banka Prishtina', 'podgorica': 'NLB Banka Podgorica', 'ancillary': 'NLB Lease&Go & NLB Skladi'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F1F6", "panel-2": "#E4E4EE", "ink": "#0D0A19", "ink-2": "#1C1A2B",
    "muted": "#454050", "faint": "#676372", "line": "#CCC7D6", "line-2": "#ADA8BA", "focus": "#230078",
    "accent": "#230078", "link": "#21005D", "gold": "#230078", "gold-deep": "#1C0050", "gold-ink": "#21005D",
    "l1": "#14003A", "l2": "#1C0050", "l3": "#2B0A62", "l4": "#402980", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#240A54", "l2f": "#230078", "l3f": "#441D98", "l4f": "#7866C2",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0D0A19", "shadow": "rgba(13,6,38,.22)", "wash-a": "rgba(35,0,120,.14)",
    "wash-b": "rgba(120,102,194,.10)", "gb2": "#240A54", "gb3": "#230078", "gb4": "#968BD7", "brand-grad": "linear-gradient(90deg,#1C0050,#230078 55%,#968BD7)",
    "gold-grad": "linear-gradient(135deg,#968BD7 0%,#230078 45%,#1C0050 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#09090D", "panel": "#111018", "panel-2": "#191721", "ink": "#F2F2F7", "ink-2": "#D4D3DF",
    "muted": "#A5A0B1", "faint": "#827D8D", "line": "#2A2632", "line-2": "#3C3846", "focus": "#7F69D5",
    "accent": "#7F68D0", "link": "#968BD7", "gold": "#7F68D0", "gold-deep": "#7F69D5", "gold-ink": "#968BD7",
    "l1": "#968BD7", "l2": "#7D69CE", "l3": "#997ADB", "l4": "#B0A6E2", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#240A54", "l2f": "#230078", "l3f": "#441D98", "l4f": "#7866C2",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050508", "wash-a": "rgba(35,0,120,.12)", "wash-b": "rgba(120,102,194,.06)",
    "gb2": "#240A54", "gb3": "#230078", "gb4": "#968BD7", "gold-grad": "linear-gradient(135deg,#C4BDF0 0%,#6145C5 45%,#230078 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
