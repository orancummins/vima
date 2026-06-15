#!/usr/bin/env bash
# Vima / Solution Studio — Test Suite (macOS / Linux)
#
# One-call usage:
#
#   Clean install (clones repo, provisions API keys, runs tests, cleans up):
#     ./test.sh --clean --sso --email you@mastercard.com --smoke
#     ./test.sh --clean --sso --email you@mastercard.com --full
#     ./test.sh --clean --sso --email you@mastercard.com --storepass foobar!!
#     ./test.sh --clean --portal-password secret --email you@mastercard.com
#
#   Existing install (uses this directory as-is, no portal login needed):
#     ./test.sh --existing --smoke
#     ./test.sh --existing --full
#     ./test.sh --existing            (prompts for scope)
#
#   Clean-install flags (--email, --sso, --portal-password, --storepass,
#   --key-password, --skip-provision, --nocleanup) are an error with --existing.
set -euo pipefail

echo ""
echo "============================================================"
echo " Vima / Solution Studio — Test Suite"
echo "============================================================"
echo ""

# ── Parse CLI arguments ───────────────────────────────────────
EMAIL=""
# Default to non-SSO when `--sso` is not passed
SSO="N"
PORTAL_PASSWORD=""
INSTALL_TYPE=""
KEY_PASSWORD=""
TEST_SCOPE=""
SKIP_PROVISION=""
NO_SERVER=""
NOCLEANUP=""
BASE_URL=""
_CLEAN_FLAGS=""

# Portable uppercase helper for macOS / POSIX shells (bash 3.2 doesn't support ${VAR^^})
upper() {
    echo "$1" | tr '[:lower:]' '[:upper:]'
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --email)           EMAIL="$2";            _CLEAN_FLAGS="1"; shift 2 ;;
        --sso)             SSO="Y";               _CLEAN_FLAGS="1"; shift   ;;
        --portal-password) PORTAL_PASSWORD="$2";  _CLEAN_FLAGS="1"; shift 2 ;;
        --clean)           INSTALL_TYPE="C";                         shift   ;;
        --existing)        INSTALL_TYPE="E";                         shift   ;;
        --key-password)    KEY_PASSWORD="$2";     _CLEAN_FLAGS="1"; shift 2 ;;
        --storepass)       KEY_PASSWORD="$2";     _CLEAN_FLAGS="1"; shift 2 ;;
        --smoke)           TEST_SCOPE="S";                           shift   ;;
        --full)            TEST_SCOPE="F";                           shift   ;;
        --skip-provision)  SKIP_PROVISION="1";    _CLEAN_FLAGS="1"; shift   ;;
        --no-server)       NO_SERVER="1";                            shift   ;;
        --nocleanup)       NOCLEANUP="1";         _CLEAN_FLAGS="1"; shift   ;;
        --base-url)        BASE_URL="$2";                            shift 2 ;;
        *)
            echo "ERROR: Unknown flag: $1"
            exit 1
            ;;
    esac
done

# ── Collect: install type (first, so we know which prompts to show) ───────
if [[ "$INSTALL_TYPE" != "C" && "$INSTALL_TYPE" != "E" ]]; then
    echo ""
    echo "Install type:"
    echo "  C - Clean     (clone repo into a temp dir, provision API keys, run tests)"
    echo "  E - Existing  (use this directory as-is, no portal login needed)"
    echo ""
    while [[ "$INSTALL_TYPE" != "C" && "$INSTALL_TYPE" != "E" ]]; do
        read -rp "Choice [C/E]: " INSTALL_TYPE
        INSTALL_TYPE="$(upper "$INSTALL_TYPE")"
        [[ "$INSTALL_TYPE" != "C" && "$INSTALL_TYPE" != "E" ]] && echo "  Please enter C or E."
    done
fi

# ── Existing install: reject clean-only flags, then go straight to scope ──
if [[ "$INSTALL_TYPE" == "E" ]]; then
    if [[ "$_CLEAN_FLAGS" == "1" ]]; then
        echo ""
        echo "ERROR: The following flags are only valid with --clean:"
        echo "         --email, --sso, --portal-password, --storepass,"
        echo "         --key-password, --skip-provision, --nocleanup"
        echo "       For an existing install only --smoke and --full are accepted."
        exit 1
    fi
else
    # ── Clean install: collect email, SSO, portal password, key password ──
    # When --skip-provision is set these credentials are never used,
    # so skip collection entirely.
    if [[ "$SKIP_PROVISION" == "1" ]]; then
        : # nothing to collect
    else

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
            SSO="$(upper "$SSO")"
            [[ "$SSO" != "Y" && "$SSO" != "N" ]] && echo "  Please enter Y or N."
        done
    fi

    # ── Collect: portal password (non-SSO only) ───────────────────
    if [[ "$SSO" != "Y" && -z "$PORTAL_PASSWORD" ]]; then
        echo ""
        read -rsp "Mastercard Developers password: " PORTAL_PASSWORD
        echo ""
    fi

    # ── Collect: key password ─────────────────────────────────────
    if [[ -z "$KEY_PASSWORD" ]]; then
        echo ""
        echo "  NOTE: Default keystore password for provisioned .p12 certs is: foobar!!"
        read -rp "Key password [default: foobar!!]: " KP_INPUT
        KEY_PASSWORD="${KP_INPUT:-foobar!!}"
    fi
    fi  # end: not skip-provision credential collection
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
        TEST_SCOPE="$(upper "$TEST_SCOPE")"
        [[ "$TEST_SCOPE" != "S" && "$TEST_SCOPE" != "F" ]] && echo "  Please enter S or F."
    done
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

# ── Launch: existing install ──────────────────────────────────
if [[ "$INSTALL_TYPE" == "E" ]]; then
    EXTRA_ARGS=()
    [[ "$TEST_SCOPE" == "F" ]] && EXTRA_ARGS+=(--full)
    [[ "$TEST_SCOPE" == "S" ]] && EXTRA_ARGS+=(--smoke)
    [[ "$NO_SERVER"  == "1" ]] && EXTRA_ARGS+=(--no-server)
    [[ -n "$BASE_URL"       ]] && EXTRA_ARGS+=(--base-url "$BASE_URL")
    "$PYTHON" "$SCRIPT_DIR/tests/run.py" \
        --install-type E \
        --work-dir "$SCRIPT_DIR" \
        "${EXTRA_ARGS[@]}"
    exit $?
fi

# ── Launch: clean install ─────────────────────────────────────
EXTRA_ARGS=()
[[ "$SSO"            == "Y" ]] && EXTRA_ARGS+=(--sso)
[[ -n "$PORTAL_PASSWORD"    ]] && EXTRA_ARGS+=(--portal-password "$PORTAL_PASSWORD")
[[ "$TEST_SCOPE"     == "F" ]] && EXTRA_ARGS+=(--full)
[[ "$TEST_SCOPE"     == "S" ]] && EXTRA_ARGS+=(--smoke)
[[ "$SKIP_PROVISION" == "1" ]] && EXTRA_ARGS+=(--skip-provision)
[[ "$NO_SERVER"      == "1" ]] && EXTRA_ARGS+=(--no-server)
[[ "$NOCLEANUP"      == "1" ]] && EXTRA_ARGS+=(--nocleanup)
[[ -n "$BASE_URL"           ]] && EXTRA_ARGS+=(--base-url "$BASE_URL")
"$PYTHON" "$SCRIPT_DIR/tests/run.py" \
    --email "$EMAIL" \
    --install-type C \
    --key-password "$KEY_PASSWORD" \
    --work-dir "$SCRIPT_DIR" \
    "${EXTRA_ARGS[@]}"
