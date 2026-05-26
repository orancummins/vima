"""Mapping from API id (as used in apis/<id>/) to its .env variable prefix.

Most prefixes match the API id (upper-cased), but a few are historical
(e.g. clarity uses CONSUMERCLARITY_).
"""
from __future__ import annotations

# api_id -> env prefix (without trailing underscore)
ENV_PREFIX: dict[str, str] = {
    "binlookup": "BINLOOKUP",
    "clarity": "CONSUMERCLARITY",
    "priceless": "PRICELESS",
    "places": "PLACES",
    "easysavings": "EASYSAVINGS",
    "txnotify": "TXNOTIFY",
    "consent": "CONSENT",
    "ofpub": "OFPUB",
    "ofmc": "OFMC",
    "eligibility": "ELIGIBILITY",
    "bces": "BCES",
    # ofin is OAuth 2.0 — handled separately via PARTNER_ID / APP_KEY / PARTNER_SECRET
    "ofin": "OFIN",
}

# APIs requiring an additional encryption .pem file from the portal.
# Currently captured manually; the tool only flags these for the operator.
ENC_KEY_VAR: dict[str, str] = {
    "consent": "CONSENT_ENCRYPTION_KEY_PATH",
    "bces": "BCES_ENCRYPTION_CERT_PATH",
}
