"""Stripe, as a platform: the data behind ``Stripe_Platform.html``.

``python customers/build_page.py stripe`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Stripe_research_notes.md``.
Stripe is private, so many figures are its own claims (annual letters,
Sessions) or press estimates; the products say which.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from stripe_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from stripe_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = "Stripe"
PAGE = "Stripe_Platform.html"
AS_OF = "17 October 2026"
TITLE = "Stripe Platform"
KICKER = f"Stripe · as at {AS_OF}"
H1 = '<h1>Stripe <span class="os">Platform</span></h1>'
SERVES = "who Stripe serves"

PALETTE_NOTE = ("Palette: Stripe's purples for the company, from the deep navy foundation to the bright access layer, graphite for\n"
                "   the people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = ("the five slices: foundation (deep navy), rails (Stripe blurple), services (violet), lines (lavender), "
               "access (graphite); graphite for the people")
GLOBE_NOTE = "the globe: Stripe's navy, blurple and cyan"

PIN = (37.77, -122.42, "San Francisco")
PIN_FACING = "the Americas"

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
# Stripe reports no segments; products are grouped by Stripe's own suites.
REV = {"pay": "Payments suite", "rev": "Revenue & finance automation", "plat": "Connect & platforms",
       "money": "Money management", "crypto": "Stablecoins & crypto", "ai": "AI & agentic commerce",
       "grp": "Company-wide"}
DIV = {"stripe": "Stripe", "bridge": "Bridge", "privy": "Privy", "tempo": "Tempo (a separate company)",
       "openrouter": "OpenRouter"}
DEFAULT_DIV = "stripe"

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F3F7", "panel-2": "#E9EBF1", "ink": "#0E1025", "ink-2": "#353958",
    "muted": "#AAA9BB", "faint": "#BCBCC5", "line": "#E0DFE8", "line-2": "#DBDAE2", "focus": "#635BFF",
    "accent": "#635BFF", "link": "#1900E6", "gold": "#635BFF", "gold-deep": "#1300B4", "gold-ink": "#1900E6",
    "l1": "#0B006B", "l2": "#1300B4", "l3": "#5741EC", "l4": "#9492DC", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#2D19D0", "l2f": "#635BFF", "l3f": "#928BE9", "l4f": "#BFC1E5",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0E1025", "shadow": "rgba(9,11,63,.22)", "wash-a": "rgba(99,91,255,.14)",
    "wash-b": "rgba(191,193,229,.10)", "gb2": "#2D19D0", "gb3": "#635BFF", "gb4": "#CED1EE", "brand-grad": "linear-gradient(90deg,#1300B4,#635BFF 55%,#CED1EE)",
    "gold-grad": "linear-gradient(135deg,#CED1EE 0%,#635BFF 45%,#1300B4 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0B0C11", "panel": "#1A1B26", "panel-2": "#292B3C", "ink": "#F3F4F8", "ink-2": "#E2E4EA",
    "muted": "#D8D7DE", "faint": "#C9C8CF", "line": "#5D5C78", "line-2": "#A7A6B7", "focus": "#B9BBEC",
    "accent": "#B1B2E7", "link": "#CED1EE", "gold": "#B1B2E7", "gold-deep": "#B9BBEC", "gold-ink": "#CED1EE",
    "l1": "#CED1EE", "l2": "#C0C2EA", "l3": "#CAC7F0", "l4": "#D4D7F1", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#2D19D0", "l2f": "#635BFF", "l3f": "#928BE9", "l4f": "#BFC1E5",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060709", "wash-a": "rgba(99,91,255,.12)", "wash-b": "rgba(191,193,229,.06)",
    "gb2": "#2D19D0", "gb3": "#635BFF", "gb4": "#CED1EE", "gold-grad": "linear-gradient(135deg,#D5D9F5 0%,#B1B2E7 45%,#635BFF 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
