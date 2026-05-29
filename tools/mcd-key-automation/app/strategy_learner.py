"""Learning + reporting layer for provisioning.

When the API_CONFIG-declared ``provision_type`` for an API fails, we try a
small ordered list of plausible alternative strategies (the *fallback chain*)
before giving up. If a non-primary strategy succeeds, we record the discovery
so a human can promote it into ``providers/mastercard/api_config.py``. If
every strategy fails, we write a structured failure report so the human
isn't left squinting at a log tail.

Design notes
------------
* Default-on but conservative. The primary strategy is always tried first,
  unchanged. Fallbacks only run if the primary raises. APIs already known to
  work see zero behaviour change.
* Set ``MCD_PROVISION_LEARN=0`` to disable fallbacks entirely (primary only,
  legacy behaviour).
* The fallback chain is deliberately short and auth-aware. It does not
  attempt every permutation — only the ones that have empirically worked for
  similar APIs in vima.
"""
from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Iterable

from loguru import logger


_HERE = Path(__file__).resolve().parents[1]
LEARNED_DIR = _HERE / "learned"
FAILURE_DIR = _HERE / "output" / "failures"


# Fallback chains keyed by the primary provision_type. Order = try order.
# Only OAuth1 family chains exist — OAuth2 and the special flows (playbook,
# priceless, match_inline) are explicit choices, not heuristics.
_FALLBACK_CHAIN: dict[str, tuple[str, ...]] = {
    "oauth1_standard":   ("oauth1_skip_step3", "oauth1_enc_key"),
    "oauth1_skip_step3": ("oauth1_standard", "oauth1_enc_key"),
    "oauth1_enc_key":    ("oauth1_standard", "oauth1_skip_step3"),
}


def learning_enabled() -> bool:
    return os.environ.get("MCD_PROVISION_LEARN", "1") != "0"


def fallback_strategies(primary: str) -> tuple[str, ...]:
    """Return the ordered list of strategies to try after ``primary`` fails.

    Empty tuple = no learning for this strategy (e.g. playbook, oauth2_region).
    """
    if not learning_enabled():
        return ()
    return _FALLBACK_CHAIN.get(primary, ())


def write_learned(api_name: str, primary: str, winner: str, attempts: list[dict]) -> Path:
    """Persist a learned strategy override.

    The human can promote it by adding an entry to ``_SPECIAL_BY_ID`` in
    ``providers/mastercard/api_config.py`` then deleting this file.
    """
    LEARNED_DIR.mkdir(parents=True, exist_ok=True)
    path = LEARNED_DIR / f"{api_name}.json"
    payload = {
        "api_name": api_name,
        "primary_declared": primary,
        "winning_strategy": winner,
        "discovered_at": datetime.utcnow().isoformat() + "Z",
        "attempts": attempts,
        "promote_hint": (
            f"Add to _SPECIAL_BY_ID in providers/mastercard/api_config.py:\n"
            f'    "{api_name}": {{"provision_type": "{winner}"}},'
        ),
    }
    path.write_text(json.dumps(payload, indent=2))
    logger.info("Learned strategy for {!r}: {} → {} (saved to {})",
                api_name, primary, winner, path)
    # Stable marker for the supervisor (VIMA Flask app) to surface in the UI.
    print(f"__VIMA_LEARNED__ api={api_name} strategy={winner} report={path}",
          flush=True)
    return path


def write_failure_report(
    api_name: str,
    primary: str,
    attempts: list[dict],
    *,
    page_url: str | None = None,
    screenshot_path: str | None = None,
) -> Path:
    """Write a structured failure report so the human gets actionable signal.

    ``attempts`` is a list of dicts: ``{"strategy": str, "error": str,
    "url": str, "screenshot": str | None}`` — one per attempt in order.
    """
    FAILURE_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    path = FAILURE_DIR / f"{api_name}-{ts}.json"

    last_err = attempts[-1]["error"] if attempts else "no attempts recorded"
    hints = _remediation_hints(attempts, primary)

    payload = {
        "api_name": api_name,
        "primary_declared": primary,
        "page_url_at_failure": page_url,
        "screenshot": screenshot_path,
        "attempts": attempts,
        "summary": f"All {len(attempts)} provisioning strategy/strategies failed for {api_name!r}. "
                   f"Last error: {last_err}",
        "remediation_hints": hints,
        "next_steps": [
            "Open the screenshot above and inspect what the portal looked like at failure.",
            "If the wizard UI has changed, re-record the playbook with: "
            f"./addapi.sh --record <docs-url>  (writes playbooks/mastercard/<slug>.json)",
            "If you see an entitlement / 'Requires API Owner approval' banner, set "
            f"provision_note=\"Requires API Owner approval\" on the catalog entry for {api_name!r} "
            "and have the API owner approve the project in developer.mastercard.com before retrying.",
            "If the failure is auth-related (login loop, MFA), check MCD_PORTAL_USERNAME, "
            "MCD_PORTAL_PASSWORD, and MCD_PORTAL_TOTP_SECRET in config/.env.",
            f"Inspect attempts[].error above and patch providers/mastercard/workflows/project_workflow.py "
            f"if a selector has changed.",
        ],
        "generated_at": datetime.utcnow().isoformat() + "Z",
    }
    path.write_text(json.dumps(payload, indent=2))
    logger.error("Wrote failure report for {!r}: {}", api_name, path)
    # Stable marker for the supervisor to surface to the user.
    print(f"__VIMA_PROVISION_REPORT__ api={api_name} report={path}", flush=True)
    return path


def _remediation_hints(attempts: list[dict], primary: str) -> list[str]:
    """Pattern-match the collected errors and emit specific guidance."""
    hints: list[str] = []
    blob = " | ".join(a.get("error", "") for a in attempts).lower()

    if "timeout" in blob and "download" in blob:
        hints.append(
            "Looks like the wizard never produced a key download. The most "
            "common cause is an extra step in the create-project flow "
            "(e.g. Step 3 'Additional credentials'). Try recording a playbook."
        )
    if "selector" in blob or "locator" in blob or "not found" in blob:
        hints.append(
            "A selector miss usually means Mastercard changed the portal UI. "
            "Patch providers/mastercard/selectors.py or re-record the playbook."
        )
    if "captcha" in blob or "verify you are human" in blob:
        hints.append(
            "Portal hit a CAPTCHA. Re-run with --headful and solve it manually, "
            "or wait for the rate-limit window to expire."
        )
    if "requires approval" in blob or "api owner" in blob or "not authorized" in blob:
        hints.append(
            "This API needs explicit owner approval before a sandbox project "
            "can be created. Visit developer.mastercard.com and have the API "
            "owner approve the request."
        )
    if "401" in blob or "403" in blob:
        hints.append(
            "401/403 from the portal usually means the logged-in user lacks "
            "permission for this product. Confirm the account has access to "
            f"the {primary!r} flow on developer.mastercard.com."
        )
    if not hints:
        hints.append(
            "No matching pattern. Open the failure screenshot and the trace "
            "logged above; the portal state at the moment of failure is the "
            "best signal."
        )
    return hints
