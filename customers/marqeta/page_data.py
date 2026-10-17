"""Marqeta, Inc., as a platform: the data behind ``Marqeta_Platform.html``.

``python customers/build_page.py marqeta`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Marqeta_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from marqeta_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from marqeta_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Marqeta'
PAGE = 'Marqeta_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Marqeta Platform"
KICKER = f"Marqeta, Inc. · as at {AS_OF}"
H1 = '<h1>Marqeta <span class="os">Platform</span></h1>'
SERVES = 'who Marqeta serves'

PALETTE_NOTE = ("Palette: Marqeta's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Marqeta's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Marqeta's colours"

PIN = (37.81, -122.27, 'Oakland')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'fin': 'Financial services & fintech', 'lend': 'Lending & BNPL', 'exp': 'Expense management & commercial', 'od': 'On-demand & enterprise', 'grp': 'Group'}
DIV = {'mq': 'Marqeta (US platform)', 'tpay': 'TransactPay (UK & EEA)', 'eu': 'Marqeta Europe', 'can': 'Marqeta Payments (Canada)', 'apac': 'Marqeta Asia Pacific', 'grp': 'Marqeta, Inc.'}
DEFAULT_DIV = 'mq'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F3F1F6", "panel-2": "#E7E2ED", "ink": "#100916", "ink-2": "#1B1421",
    "muted": "#322B36", "faint": "#59515D", "line": "#CDC2D2", "line-2": "#AB9CB2", "focus": "#2F0046",
    "accent": "#2F0046", "link": "#2E003F", "gold": "#2F0046", "gold-deep": "#2B003A", "gold-ink": "#2E003F",
    "l1": "#22002F", "l2": "#2B003A", "l3": "#2E063C", "l4": "#481E5F", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#2B0738", "l2f": "#2F0046", "l3f": "#581675", "l4f": "#8E53BA",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#100916", "shadow": "rgba(22,5,33,.22)", "wash-a": "rgba(47,0,70,.14)",
    "wash-b": "rgba(142,83,186,.10)", "gb2": "#2B0738", "gb3": "#2F0046", "gb4": "#AA7CD2", "brand-grad": "linear-gradient(90deg,#2B003A,#2F0046 55%,#AA7CD2)",
    "gold-grad": "linear-gradient(135deg,#AA7CD2 0%,#2F0046 45%,#2B003A 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A080C", "panel": "#120E15", "panel-2": "#17131B", "ink": "#F4F2F7", "ink-2": "#D5D0DD",
    "muted": "#A194A7", "faint": "#786E7D", "line": "#28222C", "line-2": "#3B323F", "focus": "#A15BD2",
    "accent": "#9F5CCC", "link": "#AA7CD2", "gold": "#9F5CCC", "gold-deep": "#A15BD2", "gold-ink": "#AA7CD2",
    "l1": "#AA7CD2", "l2": "#9C5ECB", "l3": "#B669D6", "l4": "#C09CDF", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#2B0738", "l2f": "#2F0046", "l3f": "#581675", "l4f": "#8E53BA",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060508", "wash-a": "rgba(47,0,70,.12)", "wash-b": "rgba(142,83,186,.06)",
    "gb2": "#2B0738", "gb3": "#2F0046", "gb4": "#AA7CD2", "gold-grad": "linear-gradient(135deg,#D4B8EE 0%,#8138B2 45%,#2F0046 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
