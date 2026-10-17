"""Banca Intesa Beograd, as a platform: the data behind ``Banca_Intesa_Beograd_Platform.html``.

``python customers/build_page.py intesabeograd`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Banca_Intesa_Beograd_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from intesabeograd_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from intesabeograd_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Banca Intesa'
PAGE = 'Banca_Intesa_Beograd_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Banca Intesa Platform"
KICKER = f"Banca Intesa Beograd · as at {AS_OF}"
H1 = '<h1>Banca Intesa <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Banca Intesa's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Banca Intesa's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Banca Intesa's colours"

PIN = (44.81, 20.42, 'Belgrade')
PIN_FACING = 'Serbia and south-eastern Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail & Wealth Management', 'smallbiz': 'Small business & farmers', 'corp': 'Corporate & SME', 'central': 'Treasury & central functions'}
DIV = {'bib': 'Banca Intesa Beograd', 'isp': 'Intesa Sanpaolo', 'mobi': 'Intesa Mobi', 'magnifica': 'Intesa Magnifica', 'invest': 'Intesa Invest', 'leasing': 'Intesa Leasing'}
DEFAULT_DIV = 'bib'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F2", "panel-2": "#E3EEE6", "ink": "#09180F", "ink-2": "#18281E",
    "muted": "#3A4841", "faint": "#5D6C65", "line": "#C6D5CD", "line-2": "#A4B8AE", "focus": "#006935",
    "accent": "#006935", "link": "#00542F", "gold": "#006935", "gold-deep": "#004A29", "gold-ink": "#00542F",
    "l1": "#00371E", "l2": "#004A29", "l3": "#095736", "l4": "#26764C", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#094B2F", "l2f": "#006935", "l3f": "#1B8E58", "l4f": "#60BF87",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#09180F", "shadow": "rgba(6,37,19,.22)", "wash-a": "rgba(0,105,53,.14)",
    "wash-b": "rgba(96,191,135,.10)", "gb2": "#094B2F", "gb3": "#006935", "gb4": "#86D6A3", "brand-grad": "linear-gradient(90deg,#004A29,#006935 55%,#86D6A3)",
    "gold-grad": "linear-gradient(135deg,#86D6A3 0%,#006935 45%,#004A29 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090D0A", "panel": "#101712", "panel-2": "#161F19", "ink": "#F2F7F3", "ink-2": "#D2DFD5",
    "muted": "#9DAEA5", "faint": "#788880", "line": "#232E28", "line-2": "#323E38", "focus": "#52CF86",
    "accent": "#3EC377", "link": "#86D6A3", "gold": "#3EC377", "gold-deep": "#52CF86", "gold-ink": "#86D6A3",
    "l1": "#86D6A3", "l2": "#63CC8E", "l3": "#75D9AB", "l4": "#A3E1BA", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#094B2F", "l2f": "#006935", "l3f": "#1B8E58", "l4f": "#60BF87",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050805", "wash-a": "rgba(0,105,53,.12)", "wash-b": "rgba(96,191,135,.06)",
    "gb2": "#094B2F", "gb3": "#006935", "gb4": "#86D6A3", "gold-grad": "linear-gradient(135deg,#BCEFCE 0%,#3EC377 45%,#006935 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
