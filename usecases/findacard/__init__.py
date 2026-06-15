"""Find A Card — local agent use case.

Embeds the Fins A Card web service running on localhost:5432 into the
explorer. The service must be running locally for this use case to work;
if it is not reachable the UI shows an offline state.
"""
from __future__ import annotations

from typing import Any

MANIFEST: dict[str, Any] = {
    "id": "findacard",
    "name": "Find A Card",
    "description": (
        "In the future, your agent will find the perfect card for you, "
        "this is how Mastercard's Find A Card agent will help make that happen. "
        "This UI is built to illustrate how the agent would work, it will have the ability "
        "to fully autonomously source and provision a card to your wallet."
    ),
    "apis": ["open_finance", "offers_for_publishers"],
    "render": "findacard",
    "local_port": 5432,
}
