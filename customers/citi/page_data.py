"""Citi, as a platform: the data behind ``Citi_Platform.html``.

``python customers/build_page.py citi`` turns this into the page. Public sources, as at the date
in ``AS_OF``; every product carries its own sources, and the research notes
behind them are in ``Citi_research_notes.md``.

A product is a dict with the template's own keys:

    id, n (name), d (description), short (optional, the name on the picture's tile list),
    s (kinds of user), lc (life-cycle stage, a key of LC), st (status, a key of ST),
    ay (when), o (origin, a key of OR), at (partner), div / rev (a key of DIV / REV),
    neo ([Mastercard depth 0–3 or None, note] — the lens; the key keeps the template's name),
    mc (where Mastercard fits), rel (related product ids), src ([[label, url], ...]).
"""
# ruff: noqa: E501

from citi_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from citi_story import LENS, OUTCOMES, WHO  # noqa: F401

SHORT = "Citi"
PAGE = "Citi_Platform.html"
AS_OF = "17 October 2026"
TITLE = "Citi Platform"
KICKER = f"Citigroup · as at {AS_OF}"
H1 = '<h1>Citi <span class="os">Platform</span></h1>'
SUB = ("A global bank in nearly 160 countries as five discs that stack into one platform, from the balance sheet and "
       "the transformation at the bottom to the app, the branches and CitiDirect at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined "
       "in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

PALETTE_NOTE = ("Palette: Citi's blues for the bank, from the deep navy foundation to the bright access layer, graphite for the people,\n"
                "   Citi red for the arc, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = ("the five slices: foundation (deep navy), rails (Citi blue), services (mid blue), lines (sky blue), "
               "access (graphite); graphite for the people")
GLOBE_NOTE = "the globe: Citi's navy, blue and sky"

PIN = (40.72, -74.01, "New York")
PIN_FACING = "the Americas"

# Words the leftover check in build_page.py lets through (none yet).
ALLOWED_MENTIONS: tuple[str, ...] = ()

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "US consumers & cardmembers", "user-round"),
    ("aff", "Affluent & Citigold clients", "gem"),
    ("pvt", "Private Bank & family offices", "landmark"),
    ("sme", "Mid-sized & commercial businesses", "store"),
    ("corp", "Multinationals & corporates", "factory"),
    ("inst", "Financial institutions & investors", "chart-candlestick"),
    ("gov", "Governments & public sector", "flag"),
    ("fin", "Retail partners, fintechs & developers", "code-xml"),
]
USERS_DESC = ("Eight kinds of client. Citi's money is made at both ends: the institutional franchise "
              "(Services, Markets, Banking) serves corporates, institutions and governments in about 95 markets, "
              "while the consumer bank is now almost entirely American cards, branches and wealth.")

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
# The five segments Citi has reported since 1Q26 (U.S. Consumer Cards replaced U.S. Personal Banking;
# U.S. retail banking moved into Wealth), plus All Other, where Banamex and the legacy franchises sit.
REV = {"svc": "Services segment", "mkt": "Markets segment", "bnk": "Banking segment", "wlt": "Wealth segment",
       "uscc": "U.S. Consumer Cards segment", "oth": "All Other / Legacy Franchises", "grp": "Group, not a segment"}
DIV = {"citi": "Citigroup", "svc": "Citi Services", "mkt": "Citi Markets", "bnk": "Citi Banking",
       "wlt": "Citi Wealth", "uscc": "U.S. Consumer Cards", "banamex": "Banamex", "ven": "Citi Ventures",
       "grp": "Citigroup"}
DEFAULT_DIV = "citi"

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F4F5", "panel-2": "#E6EBED", "ink": "#0D1318", "ink-2": "#222A2F",
    "muted": "#535960", "faint": "#73787E", "line": "#CED2D6", "line-2": "#B3B8BE", "focus": "#1C4882",
    "accent": "#1C4882", "link": "#15305F", "gold": "#1C4882", "gold-deep": "#112950", "gold-ink": "#15305F",
    "l1": "#0C1C36", "l2": "#112950", "l3": "#213B6B", "l4": "#436287", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#1D3358", "l2f": "#1C4882", "l3f": "#3C629A", "l4f": "#84A0B9",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0D1318", "shadow": "rgba(13,25,36,.22)", "wash-a": "rgba(28,72,130,.14)",
    "wash-b": "rgba(132,160,185,.10)", "gb2": "#1D3358", "gb3": "#1C4882", "gb4": "#A2BCCF", "brand-grad": "linear-gradient(90deg,#112950,#1C4882 55%,#A2BCCF)",
    "gold-grad": "linear-gradient(135deg,#A2BCCF 0%,#1C4882 45%,#112950 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0C0D", "panel": "#131719", "panel-2": "#1C2024", "ink": "#F3F5F6", "ink-2": "#D8DDDF",
    "muted": "#ACB0B6", "faint": "#8C9095", "line": "#32363C", "line-2": "#4C5157", "focus": "#7CA1C2",
    "accent": "#6B91B6", "link": "#A2BCCF", "gold": "#6B91B6", "gold-deep": "#7CA1C2", "gold-ink": "#A2BCCF",
    "l1": "#A2BCCF", "l2": "#88A7C3", "l3": "#96ADCF", "l4": "#B7CBDB", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#1D3358", "l2f": "#1C4882", "l3f": "#3C629A", "l4f": "#84A0B9",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060708", "wash-a": "rgba(28,72,130,.12)", "wash-b": "rgba(132,160,185,.06)",
    "gb2": "#1D3358", "gb3": "#1C4882", "gb4": "#A2BCCF", "gold-grad": "linear-gradient(135deg,#CADCE8 0%,#6B91B6 45%,#1C4882 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
