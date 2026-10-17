"""Citi, as a platform: the data behind ``Citi_Platform.html``.

``build_page.py`` turns this into the page. Public sources, as at the date
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

AS_OF = "17 October 2026"
TITLE = "Citi Platform"
KICKER = f"Citigroup · as at {AS_OF}"
H1 = '<h1>Citi <span class="os">Platform</span></h1>'
SUB = ("A global bank in nearly 160 countries as five discs that stack into one platform, from the balance sheet and "
       "the transformation at the bottom to the app, the branches and CitiDirect at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined "
       "in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

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
    "ground": "#FFFFFF", "panel": "#F2F5F9", "panel-2": "#E6ECF3", "ink": "#0A1424", "ink-2": "#1E2A3B",
    "muted": "#4A5668", "faint": "#6B7686", "line": "#CBD3DE", "line-2": "#AEB9C7",
    "focus": "#056DAE", "accent": "#056DAE", "link": "#0B4F8A",
    "gold": "#EE1C25", "gold-deep": "#003B70", "gold-ink": "#0B4F8A",
    "l1": "#002D62", "l2": "#003B70", "l3": "#0B5A9C", "l4": "#1F78BE", "l5": "#1F2937", "lu": "#6B7280",
    "l1f": "#0A3D7A", "l2f": "#056DAE", "l3f": "#1B8BD0", "l4f": "#5AAAE0", "l5f": "#374151", "luf": "#9CA3AF",
    "l1t": "#EAF3FF", "l2t": "#FFFFFF", "l3t": "#FFFFFF", "l4t": "#06213D", "l5t": "#FFFFFF",
    "slot": "#0A1424", "shadow": "rgba(6,24,48,.22)",
    "wash-a": "rgba(5,109,174,.14)", "wash-b": "rgba(238,28,37,.07)",
    "gb2": "#0A3D7A", "gb3": "#056DAE", "gb4": "#8CC8F0",
    "brand-grad": "linear-gradient(90deg,#003B70,#056DAE 55%,#EE1C25)",
    "gold-grad": "linear-gradient(135deg,#8CC8F0 0%,#056DAE 45%,#003B70 100%)",
    "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00",
    "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0D12", "panel": "#121821", "panel-2": "#1A2230", "ink": "#F3F6FA", "ink-2": "#D6DEE8",
    "muted": "#A9B4C2", "faint": "#87929F", "line": "#2C3644", "line-2": "#424E5E",
    "focus": "#7FB8F0", "accent": "#5AB0F0", "link": "#8CC8F0",
    "gold": "#FF5A60", "gold-deep": "#5AB0F0", "gold-ink": "#8CC8F0",
    "l1": "#8CC8F0", "l2": "#6CB8F0", "l3": "#7FD0F5", "l4": "#A9D6F5", "l5": "#D1D5DB", "lu": "#8B93A1",
    "l1f": "#0A3D7A", "l2f": "#056DAE", "l3f": "#1B8BD0", "l4f": "#5AAAE0", "l5f": "#6B7280", "luf": "#6B7280",
    "slot": "#05070A",
    "wash-a": "rgba(5,109,174,.12)", "wash-b": "rgba(238,28,37,.06)",
    "gb2": "#0A3D7A", "gb3": "#056DAE", "gb4": "#8CC8F0",
    "gold-grad": "linear-gradient(135deg,#BFE2FA 0%,#5AB0F0 45%,#056DAE 100%)",
    "neo": "#FFB070", "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
