"""Online Identity Verification — UI-only simulation.

Demonstrates establishing identity online by combining:
  - Finicity Connect (bank account ownership / KYC)
  - Mastercard Consent API (card-based consent + 3DS)
  - Ekata (device + email + IP risk signals)

This use case is currently a front-end simulation only. No live API calls
are made; the goal is to illustrate the user-facing journey and a
"behind the scenes" reveal of the signals each provider contributes.
"""
from __future__ import annotations

from typing import Any

MANIFEST: dict[str, Any] = {
    "id": "identity",
    "name": "Online Identity Verification",
    "description": (
        "Sign up for a government services portal and prove who you are by "
        "combining bank ownership (Finicity Connect), card consent "
        "(Mastercard Consent API) and device + email risk signals (Ekata). "
        "Flip the reveal toggle to see what is happening behind the scenes."
    ),
    "apis": ["open_finance", "consent_management"],
    "render": "identity",
}
