"""PayPal Holdings, as a platform: the data behind ``PayPal_Platform.html``.

``python customers/build_page.py paypal`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``PayPal_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from paypal_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from paypal_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'PayPal'
PAGE = 'PayPal_Platform.html'
AS_OF = "17 October 2026"
TITLE = "PayPal Platform"
KICKER = f"PayPal Holdings · as at {AS_OF}"
H1 = '<h1>PayPal <span class="os">Platform</span></h1>'
SERVES = 'who PayPal serves'

PALETTE_NOTE = ("Palette: PayPal's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in PayPal's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in PayPal's colours"

PIN = (37.38, -121.92, 'San Jose')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'checkout': 'Checkout Solutions & PayPal', 'consumer': 'Consumer Financial Services & Venmo', 'services': 'Payment Services & Crypto', 'grp': 'Corporate'}
DIV = {'paypal': 'PayPal', 'venmo': 'Venmo', 'braintree': 'Braintree', 'xoom': 'Xoom', 'paidy': 'Paidy', 'honey': 'Honey', 'europe': 'PayPal (Europe)', 'grp': 'PayPal Holdings'}
DEFAULT_DIV = 'paypal'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F4F6", "panel-2": "#E4EAEE", "ink": "#0A111A", "ink-2": "#1C252E",
    "muted": "#464C58", "faint": "#686E78", "line": "#C9CED7", "line-2": "#ABB1BD", "focus": "#003087",
    "accent": "#003087", "link": "#001E66", "gold": "#003087", "gold-deep": "#001A57", "gold-ink": "#001E66",
    "l1": "#00123D", "l2": "#001A57", "l3": "#0B266E", "l4": "#2C508A", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0B235C", "l2f": "#003087", "l3f": "#1F4BA3", "l4f": "#6C94C4",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A111A", "shadow": "rgba(6,21,40,.22)", "wash-a": "rgba(0,48,135,.14)",
    "wash-b": "rgba(108,148,196,.10)", "gb2": "#0B235C", "gb3": "#003087", "gb4": "#8FB4D9", "brand-grad": "linear-gradient(90deg,#001A57,#003087 55%,#8FB4D9)",
    "gold-grad": "linear-gradient(135deg,#8FB4D9 0%,#003087 45%,#001A57 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090B0D", "panel": "#111519", "panel-2": "#181D23", "ink": "#F2F5F7", "ink-2": "#D4DBE0",
    "muted": "#A4AAB4", "faint": "#828791", "line": "#2A2F37", "line-2": "#3F444E", "focus": "#5F93D3",
    "accent": "#4C81C7", "link": "#8FB4D9", "gold": "#4C81C7", "gold-deep": "#5F93D3", "gold-ink": "#8FB4D9",
    "l1": "#8FB4D9", "l2": "#6F9BD0", "l3": "#7F9DDC", "l4": "#A9C5E3", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0B235C", "l2f": "#003087", "l3f": "#1F4BA3", "l4f": "#6C94C4",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050708", "wash-a": "rgba(0,48,135,.12)", "wash-b": "rgba(108,148,196,.06)",
    "gb2": "#0B235C", "gb3": "#003087", "gb4": "#8FB4D9", "gold-grad": "linear-gradient(135deg,#BFD8F0 0%,#4C81C7 45%,#003087 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
