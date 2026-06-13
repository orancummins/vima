"""Transaction Notifications Live — real-time webhook demo.

The Flask app acts as the webhook receiver at POST /txnotify/webhook.
This module stores received payloads in a ring buffer and exposes them
to the use-case UI via do_action("poll", ...).

Integration flow:
  1. User launches ngrok (terminal button) → exposes port 9021.
  2. User registers https://<ngrok-id>.ngrok-free.app/txnotify/webhook
     as the webhook URL in their Mastercard Developer project.
  3. User enrolls a card via the Transaction Notifications API tab.
  4. User triggers a test transaction — Mastercard POSTs the signed
     payload to the ngrok URL → this module's receive_webhook().
  5. The UI polls do_action("poll") every 2 s and renders new events.
"""
from __future__ import annotations

import datetime
import uuid
from collections import deque
from typing import Any, Dict

MANIFEST: Dict[str, Any] = {
    "id": "txnotify",
    "name": "Transaction Notifications Live",
    "description": (
        "See Mastercard transaction notifications land in real time. "
        "Expose a local webhook receiver via ngrok, enroll a card, "
        "trigger a test transaction and watch the signed payload arrive "
        "in seconds — with a full JSON inspector built in."
    ),
    "apis": ["transaction_notifications"],
    "render": "txnotify",
}

# Use cases that don't need an Open Finance customer must declare this.
REQUIRES_CUSTOMER = False

# Ring buffer: newest events at index 0.
_inbox: deque = deque(maxlen=100)


def receive_webhook(payload: Any) -> None:
    """Called by app.py when POST /txnotify/webhook is hit."""
    _inbox.appendleft({
        "id": str(uuid.uuid4()),
        "received_at": datetime.datetime.utcnow().strftime("%H:%M:%S"),
        "received_at_iso": datetime.datetime.utcnow().isoformat() + "Z",
        "payload": payload,
    })


def do_action(action: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if action == "poll":
        # since_id: return only events newer than this ID.
        # _inbox is newest-first so events[:idx] are the newer ones.
        since_id = (params or {}).get("since_id")
        events = list(_inbox)
        if since_id:
            idx = next((i for i, e in enumerate(events) if e["id"] == since_id), None)
            if idx is not None:
                events = events[:idx]
        return {"ok": True, "events": events, "total": len(list(_inbox))}

    if action == "clear":
        _inbox.clear()
        return {"ok": True}

    if action == "get_state":
        try:
            from apis.transaction_notifications.api import STATE
            return {"ok": True, "state": dict(STATE)}
        except Exception as e:
            return {"ok": False, "error": str(e), "state": {}}

    return {"error": f"Unknown action: {action}"}
