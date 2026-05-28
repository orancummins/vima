#!/usr/bin/env bash
# addapi.sh — Provision a Mastercard API + emit the agent onboarding handoff.
#
# Usage:
#   ./addapi.sh <MASTERCARD_DOCS_URL>
#   ./addapi.sh --headful    <MASTERCARD_DOCS_URL>   # force browser window
#   ./addapi.sh --record     <MASTERCARD_DOCS_URL>   # record portal flow once
#   ./addapi.sh --code-only  <MASTERCARD_DOCS_URL>   # skip provisioning,
#                                                      print agent handoff only
#   ./addapi.sh --skip-agent <MASTERCARD_DOCS_URL>   # suppress the agent prompt
#   ./addapi.sh --init-session                       # cache portal session
#
# Example:
#   ./addapi.sh https://developer.mastercard.com/bin-lookup/documentation/
#
# What it does:
#   1. Provisions the portal (record-replay playbook for unknown APIs,
#      headless replay for known ones) and writes config/.env.generated.
#   2. Emits a structured AGENT NEXT STEPS block so the next agent
#      (Copilot Chat in VS Code) can pick up and finish the codebase
#      additions per docs/agent-onboarding/one-file-api-onboarding-instruction.md.
#
# Record once, replay forever:
#   APIs whose portal flow uses the playbook driver require a one-time
#   recording. Run `./addapi.sh --record <docs-url>` to walk through the
#   create-project flow in a real browser; the steps are saved to
#   tools/mcd-key-automation/playbooks/mastercard/<slug>.json. Subsequent
#   `./addapi.sh <docs-url>` calls replay that playbook autonomously.
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
RECORD=""
CODE_ONLY=""
SKIP_AGENT=""
URL=""

for arg in "$@"; do
  case "$arg" in
    --headful)   HEADFUL="--headful" ;;
    --init-session) INIT_SESSION="yes" ;;
    --record)    RECORD="yes" ;;
    --code-only) CODE_ONLY="yes" ;;
    --skip-agent) SKIP_AGENT="yes" ;;
    --help|-h)
      sed -n '2,32p' "$0" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    http*)       URL="$arg" ;;
    *)
      echo "Unknown argument: $arg" >&2
      echo "Usage: ./addapi.sh [--headful|--record|--code-only|--skip-agent|--init-session] <MASTERCARD_DOCS_URL>" >&2
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

# ── Record mode ───────────────────────────────────────────────────────────────
if [[ -n "$RECORD" ]]; then
  # Extract slug from URL: https://developer.mastercard.com/<slug>/documentation/
  SLUG="$(echo "$URL" | sed -E 's#https?://developer\.mastercard\.com/([^/]+)/.*#\1#')"
  if [[ -z "$SLUG" || "$SLUG" == "$URL" ]]; then
    echo "Error: Could not extract API slug from URL: $URL" >&2
    exit 1
  fi
  echo "Recording portal create-project flow for slug=$SLUG"
  echo "  A browser window will open. Drive the flow end-to-end (create project,"
  echo "  download key file). When done, return here and press Enter."
  echo ""
  "$MCD_CMD" record-api --api-slug "$SLUG" \
    --start-url "https://developer.mastercard.com/create-project?services=$SLUG"
  EXIT_CODE=$?
  if [[ $EXIT_CODE -eq 0 ]]; then
    echo ""
    echo "Playbook saved. Subsequent './addapi.sh $URL' will replay it autonomously."
  fi
  exit $EXIT_CODE
fi

# ── Run provision-api ─────────────────────────────────────────────────────────
echo "Adding API from: $URL"
echo ""

# Derive slug early so both auto-record fallback and the agent-handoff block
# can reference it.
SLUG="$(echo "$URL" | sed -E 's#https?://developer\.mastercard\.com/([^/]+)/.*#\1#')"
PLAYBOOK_FILE="$TOOL_DIR/playbooks/mastercard/$SLUG.json"
# Snake-case for use as canonical api_name (matches existing convention in
# config/.env: CONSUMER_CLARITY_*, BIN_LOOKUP_*, etc.).
API_NAME="$(echo "$SLUG" | tr '-' '_')"
ENV_PREFIX="$(echo "$API_NAME" | tr '[:lower:]' '[:upper:]')"

# Skip provisioning if --code-only was passed (e.g. re-running just the
# codebase additions after the portal keys are already in place).
if [[ -z "$CODE_ONLY" ]]; then

# Auto-record fallback: if the slug has no recorded playbook and is not in the
# catalog of known driver mappings, we can't safely run the headless flow
# (proceed button will hang on unknown wizard fields). Open the recorder first,
# then continue with provisioning automatically.
if [[ -z "$HEADFUL" && -n "$SLUG" && ! -f "$PLAYBOOK_FILE" ]]; then
  IS_CATALOGUED="$(
    "$TOOL_VENV/bin/python" -c "
import sys
sys.path.insert(0, '$TOOL_DIR')
from app._vima_catalog import iter_ordered
print('yes' if any(e.portal_slug == '$SLUG' for e in iter_ordered()) else 'no')
" 2>/dev/null || echo "unknown"
  )"
  if [[ "$IS_CATALOGUED" == "no" ]]; then
    echo "First-time API: no catalog entry and no recorded playbook for slug=$SLUG."
    echo "Launching the recorder so we can capture the wizard flow once."
    echo "  → A browser will open. Drive the create-project flow end-to-end,"
    echo "    download the key file, then return here and press Enter."
    echo ""
    "$MCD_CMD" record-api --api-slug "$SLUG" \
      --start-url "https://developer.mastercard.com/create-project?services=$SLUG"
    REC_EXIT=$?
    if [[ $REC_EXIT -ne 0 ]]; then
      echo "Recording failed (exit $REC_EXIT). Aborting." >&2
      exit $REC_EXIT
    fi
    if [[ ! -f "$PLAYBOOK_FILE" ]]; then
      echo "Recorder did not produce $PLAYBOOK_FILE. Aborting." >&2
      exit 1
    fi
    echo ""
    echo "Playbook saved. The manual walk-through already created a portal project,"
    echo "so credentials are in place. Re-run './addapi.sh $URL' later to provision"
    echo "additional projects autonomously."
    echo ""
    # Fall through to the agent-handoff block — codebase still needs to be added.
    PROVISION_SKIPPED="yes"
  fi
fi

if [[ -z "${PROVISION_SKIPPED:-}" ]]; then
  # Some APIs have portal steps that require a manual user click because the
  # portal's bot-detection blocks automated mouse/keyboard events on specific
  # wizard pages.  For these slugs we force a visible browser so the user can
  # intervene when prompted, and we print clear instructions.
  MANUAL_PROCEED_SLUGS="match"
  if [[ -z "$HEADFUL" && " $MANUAL_PROCEED_SLUGS " =~ " $SLUG " ]]; then
    HEADFUL="--headful"
    echo "ℹ️  $SLUG requires two manual clicks during provisioning (Mastercard portal"
    echo "   bot-detection blocks automated clicks on key-generation pages)."
    echo ""
    echo "   A browser window will open and fill in the form automatically."
    echo "   You will see two amber banners — click the indicated button each time:"
    echo ""
    echo "     1. 'Key form ready' banner  → click the blue Proceed button"
    echo "     2. 'Key downloaded' banner  → click the blue Create Project button"
    echo ""
    echo "   Everything else (form fill, download, credential capture) is automatic."
    echo ""
  fi

  "$MCD_CMD" provision-api $HEADFUL "$URL"
  EXIT_CODE=$?
  if [[ $EXIT_CODE -ne 0 ]]; then
    exit $EXIT_CODE
  fi
  echo ""
  echo "Provisioning complete. To activate the credentials:"
  echo "  cat config/.env.generated >> config/.env"
fi

fi  # end of !CODE_ONLY block

# ── Agent handoff — kick off the codebase additions ───────────────────────────
# The portal side is done (keys + .env.generated). The remaining work is
# wiring the API into the vima codebase: catalog entry, apis/<id>/api.py,
# simulator handler+fixture, validation, smoke tests, etc. This work is
# described step-by-step in docs/agent-onboarding/one-file-api-onboarding-instruction.md
# and the agent (Copilot / Claude in VS Code chat) is responsible for it.

cat <<EOF

================================================================
 AGENT NEXT STEPS — wire API into vima codebase
================================================================
 docs URL:     $URL
 portal slug:  $SLUG
 api_name:     $API_NAME
 env prefix:   $ENV_PREFIX
 key file:     config/keys/$API_NAME.p12
 playbook:     ${PLAYBOOK_FILE/#$SCRIPT_DIR\//}

 Required follow-up steps (per
 docs/agent-onboarding/one-file-api-onboarding-instruction.md):
   1. Update apis/catalog.py with a new ApiCatalogEntry for $API_NAME.
   2. Implement apis/$API_NAME/api.py with MANIFEST + execute().
   3. Add simulator handler at simulator/handlers/$API_NAME.py
      + fixture at simulator/fixtures/$API_NAME.json.
   4. Wire provisioning into
      tools/mcd-key-automation/providers/mastercard/api_config.py.
   5. Run validation: ./.venv/bin/python tools/validate_api_contract.py
   6. Run live smoke: ./addapi.sh --code-only $URL && \\
      cd tools/mcd-key-automation && \\
      ./.venv/bin/mcd-key-automation test-api "$URL"
   7. Create checklist artifact from
      docs/agent-onboarding/onboarding-checklist-template.md at
      docs/agent-onboarding/checklists/$API_NAME-onboarding-checklist.md.
================================================================
EOF

if [[ -z "$SKIP_AGENT" ]]; then
  cat <<EOF

To kick off the agent (Copilot Chat in VS Code), paste this prompt:

  Read docs/agent-onboarding/one-file-api-onboarding-instruction.md
  and onboard the API at $URL. Portal provisioning is already
  complete (api_name=$API_NAME, env_prefix=$ENV_PREFIX). Skip
  step 12 (provisioning) and proceed with steps 1-11 and 13-15.

(Re-run with --skip-agent to suppress this prompt.)
EOF
fi

exit 0
