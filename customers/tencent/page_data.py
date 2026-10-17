"""Tencent, as a platform: the data behind ``Tencent_Platform.html``.

``python customers/build_page.py tencent`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Tencent_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from tencent_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from tencent_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Tencent'
PAGE = 'Tencent_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Tencent Platform"
KICKER = f"Tencent Holdings, read through Weixin Pay and its payments · as at {AS_OF}"
H1 = '<h1>Tencent <span class="os">Platform</span></h1>'
SERVES = 'who WeChat Pay serves'

PALETTE_NOTE = ("Palette: Tencent's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Tencent's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Tencent's colours"

PIN = (22.54, 113.93, 'Shenzhen')
PIN_FACING = 'China and Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'fbs': 'FinTech & Business Services', 'mkt': 'Marketing Services', 'vas': 'Value-added Services', 'grp': 'Group-level'}
DIV = {'wxpay': 'Weixin Pay (Tenpay)', 'global': 'TenPay Global', 'hk': 'WeChat Pay HK', 'fit': 'FinTech services', 'weixin': 'Weixin Group', 'cloud': 'Tencent Cloud', 'grp': 'Tencent Holdings'}
DEFAULT_DIV = 'wxpay'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F5F6", "panel-2": "#E6ECEF", "ink": "#0C151E", "ink-2": "#26333E",
    "muted": "#616B7A", "faint": "#7F8590", "line": "#D2D6DD", "line-2": "#BDC2CB", "focus": "#0050D8",
    "accent": "#0050D8", "link": "#002F97", "gold": "#0050D8", "gold-deep": "#00267B", "gold-ink": "#002F97",
    "l1": "#00194F", "l2": "#00267B", "l3": "#113EAD", "l4": "#3D71C0", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#103589", "l2f": "#0050D8", "l3f": "#2F69D7", "l4f": "#8CACD1",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0C151E", "shadow": "rgba(7,26,49,.22)", "wash-a": "rgba(0,80,216,.14)",
    "wash-b": "rgba(140,172,209,.10)", "gb2": "#103589", "gb3": "#0050D8", "gb4": "#A7C5E1", "brand-grad": "linear-gradient(90deg,#00267B,#0050D8 55%,#A7C5E1)",
    "gold-grad": "linear-gradient(135deg,#A7C5E1 0%,#0050D8 45%,#00267B 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0C0E", "panel": "#141A1E", "panel-2": "#1F262D", "ink": "#F2F6F7", "ink-2": "#D9E0E4",
    "muted": "#B8BCC4", "faint": "#9DA1A9", "line": "#3D4450", "line-2": "#636B7A", "focus": "#82ABDD",
    "accent": "#739DD3", "link": "#A7C5E1", "gold": "#739DD3", "gold-deep": "#82ABDD", "gold-ink": "#A7C5E1",
    "l1": "#A7C5E1", "l2": "#8EB2DA", "l3": "#9BB3E4", "l4": "#BAD1E8", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#103589", "l2f": "#0050D8", "l3f": "#2F69D7", "l4f": "#8CACD1",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,80,216,.12)", "wash-b": "rgba(140,172,209,.06)",
    "gb2": "#103589", "gb3": "#0050D8", "gb4": "#A7C5E1", "gold-grad": "linear-gradient(135deg,#C8DEF2 0%,#739DD3 45%,#0050D8 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
