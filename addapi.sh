#!/usr/bin/env bash
# addapi.sh — Provision a Mastercard API from its documentation URL.
#
# Usage:
#   ./addapi.sh <MASTERCARD_DOCS_URL>
#   ./addapi.sh --headful <MASTERCARD_DOCS_URL>   # force browser window
#
# Example:
#   ./addapi.sh https://developer.mastercard.com/bin-lookup/documentation/
#
# What it does:
#   1. Sets up the mcd-key-automation venv (first run only).
#   2. Runs `provision-api <url>` — creates a portal project, downloads keys,
#      writes credentials to config/.env.generated, and smoke-tests the API.
#   3. Prints instructions for merging credentials into config/.env.
#
# Prerequisites:
#   - Add MCD_PORTAL_EMAIL and MCD_PORTAL_PASSWORD to config/.env before running.
#   - Run `./addapi.sh --init-session` once to cache your portal session so
#     subsequent calls run headless (no browser window).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TOOL_DIR="$SCRIPT_DIR/tools/mcd-key-automation"
TOOL_VENV="$TOOL_DIR/.venv"
MCD_CMD="$TOOL_VENV/bin/mcd-key-automation"

# ── Parse arguments ───────────────────────────────────────────────────────────
HEADFUL=""
INIT_SESSION=""
URL=""

for arg in "$@"; do
  case "$arg" in
    --headful)   HEADFUL="--headful" ;;
    --init-session) INIT_SESSION="yes" ;;
    --help|-h)
      sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    http*)       URL="$arg" ;;
    *)
      echo "Unknown argument: $arg" >&2
      echo "Usage: ./addapi.sh [--headful] [--init-session] <MASTERCARD_DOCS_URL>" >&2
      exit 1
      ;;
  esac
done

# ── Ensure tool venv exists ───────────────────────────────────────────────────
if [[ ! -f "$TOOL_VENV/bin/python" ]]; then
  echo ""
  echo "Setting up API key automation tool (first run only)..."
  echo "  [1/3] Creating virtual environment..."
  python3 -m venv "$TOOL_VENV"
  echo "  [2/3] Installing dependencies..."
  "$TOOL_VENV/bin/pip" install -q -e "$TOOL_DIR"
  echo "  [3/3] Installing Chromium browser..."
  "$TOOL_VENV/bin/playwright" install chromium
  echo ""
  echo "API key automation tool ready."
  echo ""
fi

# ── Init-session mode ─────────────────────────────────────────────────────────
if [[ -n "$INIT_SESSION" ]]; then
  echo "Establishing portal session (browser will open for login + MFA)..."
  "$MCD_CMD" init-session
  echo ""
  echo "Session cached. Subsequent addapi.sh calls will run headless."
  exit 0
fi

# ── Require URL ───────────────────────────────────────────────────────────────
if [[ -z "$URL" ]]; then
  echo "Error: No Mastercard Developers URL provided." >&2
  echo "" >&2
  echo "Usage: ./addapi.sh <MASTERCARD_DOCS_URL>" >&2
  echo "" >&2
  echo "Examples:" >&2
  echo "  ./addapi.sh https://developer.mastercard.com/bin-lookup/documentation/" >&2
  echo "  ./addapi.sh https://developer.mastercard.com/merchant-identifier/documentation/" >&2
  echo "" >&2
  echo "First time? Cache your portal session so subsequent calls are headless:" >&2
  echo "  ./addapi.sh --init-session" >&2
  exit 1
fi

# ── Run provision-api ─────────────────────────────────────────────────────────
echo "Adding API from: $URL"
echo ""
"$MCD_CMD" provision-api $HEADFUL "$URL"
EXIT_CODE=$?

if [[ $EXIT_CODE -eq 0 ]]; then
  echo ""
  echo "Done. To activate the credentials:"
  echo "  cat config/.env.generated >> config/.env"
  echo "  ./run.sh  (restart the server)"
fi

exit $EXIT_CODE
