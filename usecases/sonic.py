"""Mastercard Sonic Branding — UI-only showcase.

Demonstrates Mastercard's sonic identity assets and how they should be
integrated across different payment touchpoints:

  - Acceptance Sound   (primary checkout / tap-to-pay confirmation)
  - Jingle             (full branded melody for marketing contexts)
  - App UI Sounds      (micro-interactions inside digital products)
  - Regional Variants  (culturally adapted versions of the core melody)

This use case is front-end only. All sounds are synthesised in the browser
using the Web Audio API to approximate Mastercard's sonic DNA — the actual
licensed assets must be obtained from Mastercard Brand Centre.
"""
from __future__ import annotations
from typing import Any, Dict

MANIFEST: Dict[str, Any] = {
    "id": "sonic",
    "name": "Sonic Branding",
    "description": (
        "Mastercard Sonic Branding is a complete audio identity — from the "
        "acceptance chime at checkout, to tap-to-pay pings and in-app "
        "micro-sounds. Explore every asset, hear it in context and understand "
        "where each one should (and shouldn't) be used."
    ),
    "apis": ["Mastercard Brand Centre"],
    "render": "sonic",
}
