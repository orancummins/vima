#!/usr/bin/env bash
# Vima / Solution Studio — Test Suite (macOS / Linux)
#
# One-call usage:
#   ./test.sh --email you@mastercard.com --sso --clean --smoke
#   ./test.sh --email you@mastercard.com --sso --clean --full
#   ./test.sh --email you@mastercard.com --portal-password secret --existing
#   ./test.sh --email you@mastercard.com --sso --clean --storepass foobar!!
#
# NOTE: Default keystore password for provisioned .p12 certs is: foobar!!
#       Override with --key-password only if your org uses a different value.
#
# Test scope (default is smoke):
#   --smoke   Smoke tests only (connectivity + basic API checks)
#   --full    Full suite (smoke + API + use case + bundles + SDKs)
set -euo pipefail

echo ""
echo "============================================================"
echo " Vima / Solution Studio — Test Suite"
echo "============================================================"
echo ""

# ── Parse CLI arguments ───────────────────────────────────────
EMAIL=""
SSO=""
PORTAL_PASSWORD=""
INSTALL_TYPE=""
KEY_PASSWORD=""
TEST_SCOPE=""
SKIP_PROVISION=""
NO_SERVER=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --email)           EMAIL="$2";            shift 2 ;;
        --sso)             SSO="Y";               shift   ;;
        --portal-password) PORTAL_PASSWORD="$2";  shift 2 ;;
        --clean)           INSTALL_TYPE="C";      shift   ;;
        --existing)        INSTALL_TYPE="E";      shift   ;;
        --key-password)    KEY_PASSWORD="$2";     shift 2 ;;
        --storepass)       KEY_PASSWORD="$2";     shift 2 ;;
        --smoke)           TEST_SCOPE="S";        shift   ;;
        --full)            TEST_SCOPE="F";        shift   ;;
        --skip-provision)  SKIP_PROVISION="1";    shift   ;;
        --no-server)       NO_SERVER="1";         shift   ;;
        *) shift ;;
    esac
done

# ── Collect: email ────────────────────────────────────────────
while [[ -z "$EMAIL" ]]; do
    read -rp "Mastercard Developers email: " EMAIL
    [[ -z "$EMAIL" ]] && echo "  Email is required."
done

# ── Collect: SSO ──────────────────────────────────────────────
#   SSO (Y)     = corporate/federated login; email is auto-filled in the
#                 browser and the SSO redirect completes the login.
#   Non-SSO (N) = standard login; email + password are pre-filled and
#                 submitted automatically (MFA still requires human action).
if [[ -z "$SSO" ]]; then
    echo ""
    while [[ "$SSO" != "Y" && "$SSO" != "N" ]]; do
        read -rp "Mastercard Developers SSO [Y/N]: " SSO
        SSO="${SSO^^}"
        [[ "$SSO" != "Y" && "$SSO" != "N" ]] && echo "  Please enter Y or N."
    done
fi

# ── Collect: portal password (non-SSO only) ───────────────────
if [[ "$SSO" != "Y" && -z "$PORTAL_PASSWORD" ]]; then
    echo ""
    read -rsp "Mastercard Developers password: " PORTAL_PASSWORD
    echo ""
fi

# ── Collect: install type ─────────────────────────────────────
if [[ "$INSTALL_TYPE" != "C" && "$INSTALL_TYPE" != "E" ]]; then
    echo ""
    echo "Install type:"
    echo "  C - Clean  (clone repo to a temp directory first)"
    echo "  E - Existing  (use this directory as-is)"
    echo ""
    while [[ "$INSTALL_TYPE" != "C" && "$INSTALL_TYPE" != "E" ]]; do
        read -rp "Choice [C/E]: " INSTALL_TYPE
        INSTALL_TYPE="${INSTALL_TYPE^^}"
        [[ "$INSTALL_TYPE" != "C" && "$INSTALL_TYPE" != "E" ]] && echo "  Please enter C or E."
    done
fi

# ── Collect: test scope ───────────────────────────────────────
#   S / --smoke = smoke tests only (default)
#   F / --full  = full suite (smoke + API + use case + bundles + SDKs)
if [[ -z "$TEST_SCOPE" ]]; then
    echo ""
    echo "Test scope:"
    echo "  S - Smoke  (connectivity + basic checks, fast)"
    echo "  F - Full   (smoke + API + use case + bundles + SDKs)"
    echo ""
    while [[ "$TEST_SCOPE" != "S" && "$TEST_SCOPE" != "F" ]]; do
        read -rp "Choice [S/F, default S]: " TS_INPUT
        TEST_SCOPE="${TS_INPUT:-S}"
        TEST_SCOPE="${TEST_SCOPE^^}"
        [[ "$TEST_SCOPE" != "S" && "$TEST_SCOPE" != "F" ]] && echo "  Please enter S or F."
    done
fi

# ── Collect: key password (provision only) ────────────────────
# NOTE: Default keystore password for provisioned .p12 certs is: foobar!!
if [[ -z "$KEY_PASSWORD" ]]; then
    if [[ "$INSTALL_TYPE" == "C" ]]; then
        echo ""
        echo "  NOTE: Default keystore password for provisioned .p12 certs is: foobar!!"
        read -rp "Key password [default: foobar!!]: " KP_INPUT
        KEY_PASSWORD="${KP_INPUT:-foobar!!}"
    else
        KEY_PASSWORD="foobar!!"
    fi
fi

echo ""

# ── Resolve Python ────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON=""
if [[ -x "$SCRIPT_DIR/.venv/bin/python3" ]]; then
    PYTHON="$SCRIPT_DIR/.venv/bin/python3"
elif command -v python3 &>/dev/null; then
    PYTHON="python3"
elif command -v python &>/dev/null; then
    PYTHON="python"
else
    echo "ERROR: Python not found. Install Python 3.9+ and re-run."
    exit 1
fi

# ── Build optional flags ──────────────────────────────────────
EXTRA_ARGS=()
[[ "$SSO" == "Y" ]]             && EXTRA_ARGS+=(--sso)
[[ -n "$PORTAL_PASSWORD" ]]     && EXTRA_ARGS+=(--portal-password "$PORTAL_PASSWORD")
[[ "$TEST_SCOPE" == "F" ]]      && EXTRA_ARGS+=(--full)
[[ "$TEST_SCOPE" == "S" ]]      && EXTRA_ARGS+=(--smoke)
[[ "$SKIP_PROVISION" == "1" ]]  && EXTRA_ARGS+=(--skip-provision)
[[ "$NO_SERVER" == "1" ]]       && EXTRA_ARGS+=(--no-server)

# ── Launch test runner ────────────────────────────────────────
"$PYTHON" "$SCRIPT_DIR/tests/run.py" \
    --email "$EMAIL" \
    --install-type "$INSTALL_TYPE" \
    --key-password "$KEY_PASSWORD" \
    --work-dir "$SCRIPT_DIR" \
    "${EXTRA_ARGS[@]}"
