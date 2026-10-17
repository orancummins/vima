"""Bank of America, as a platform: the data behind ``Bank_of_America_Platform.html``.

``python customers/build_page.py bofa`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Bank_of_America_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bofa_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bofa_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BofA'
PAGE = 'Bank_of_America_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BofA Platform"
KICKER = f"Bank of America · as at {AS_OF}"
H1 = '<h1>BofA <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BofA's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BofA's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BofA's colours"

PIN = (35.23, -80.84, 'Charlotte')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'consumer': 'Consumer Banking', 'gwim': 'Global Wealth & Investment Management', 'gb': 'Global Banking', 'gm': 'Global Markets', 'other': 'All Other'}
DIV = {'bac': 'Bank of America Corporation', 'bofa': 'Bank of America', 'merrill': 'Merrill', 'pb': 'Bank of America Private Bank', 'bofas': 'BofA Securities', 'gps': 'Global Payments Solutions', 'bams': 'BofA Merchant Services'}
DEFAULT_DIV = 'bac'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F4F6", "panel-2": "#E3E9ED", "ink": "#0A1018", "ink-2": "#192028",
    "muted": "#3A3F49", "faint": "#5E626C", "line": "#C6CBD5", "line-2": "#A5ABB8", "focus": "#012169",
    "accent": "#012169", "link": "#011554", "gold": "#012169", "gold-deep": "#01134A", "gold-ink": "#011554",
    "l1": "#010E36", "l2": "#01134A", "l3": "#0A1B57", "l4": "#274176", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0A1A4B", "l2f": "#012169", "l3f": "#1C3C8D", "l4f": "#6287BF",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A1018", "shadow": "rgba(6,18,37,.22)", "wash-a": "rgba(1,33,105,.14)",
    "wash-b": "rgba(98,135,191,.10)", "gb2": "#0A1A4B", "gb3": "#012169", "gb4": "#87AAD5", "brand-grad": "linear-gradient(90deg,#01134A,#012169 55%,#87AAD5)",
    "gold-grad": "linear-gradient(135deg,#87AAD5 0%,#012169 45%,#01134A 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090A0C", "panel": "#101317", "panel-2": "#161A1F", "ink": "#F2F5F7", "ink-2": "#D2D9DE",
    "muted": "#9DA2AE", "faint": "#787D88", "line": "#23272E", "line-2": "#32363E", "focus": "#5484CE",
    "accent": "#4B7AC5", "link": "#87AAD5", "gold": "#4B7AC5", "gold-deep": "#5484CE", "gold-ink": "#87AAD5",
    "l1": "#87AAD5", "l2": "#658FCB", "l3": "#7691D8", "l4": "#A4BEE0", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0A1A4B", "l2f": "#012169", "l3f": "#1C3C8D", "l4f": "#6287BF",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050708", "wash-a": "rgba(1,33,105,.12)", "wash-b": "rgba(98,135,191,.06)",
    "gb2": "#0A1A4B", "gb3": "#012169", "gb4": "#87AAD5", "gold-grad": "linear-gradient(135deg,#BCD4EF 0%,#3F71C1 45%,#012169 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
