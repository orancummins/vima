#!/usr/bin/env bash
# ============================================================================
#  ofin - Open Finance CLI launcher / builder  (macOS / Linux)
# ----------------------------------------------------------------------------
#  Usage:
#    ./cli.sh                 Run the CLI from this repo (dev mode). With no
#                             extra args it prints the ofin welcome screen.
#    ./cli.sh <args...>       Run an ofin command, e.g.  ./cli.sh us auth token
#    ./cli.sh build           Build a self-contained bundle in cli/dist/ that
#                             you can copy and run on any machine with Python.
#    ./cli.sh help            Show this help.
#
#  Requirements: Python 3.9+ with 'requests' and 'cryptography' installed
#                (pip install requests cryptography)
# ============================================================================
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLI_DIR="$REPO_DIR/cli"

# Pick an available Python 3 interpreter.
PY="${PYTHON:-}"
if [ -z "$PY" ]; then
    if command -v python3 >/dev/null 2>&1; then PY=python3
    elif command -v python >/dev/null 2>&1; then PY=python
    else
        echo "error: python3 not found on PATH" >&2
        exit 127
    fi
fi

usage() {
    cat <<'EOF'
ofin - Open Finance CLI launcher (macOS / Linux)

  ./cli.sh                Run the CLI (dev mode); no args shows the welcome screen
  ./cli.sh <args...>      Run a command, e.g.  ./cli.sh us auth token
  ./cli.sh build          Build a portable bundle in cli/dist/ (run anywhere)
  ./cli.sh help           Show this help

Requirements: Python 3.9+ with 'requests' and 'cryptography'.
Config is auto-discovered from config/.env; see cli/README.md for details.
EOF
}

case "${1:-}" in
    help|--help|-h)
        usage
        ;;
    build)
        echo "Building self-contained bundle into cli/dist/ ..."
        "$PY" "$CLI_DIR/build.py"
        echo
        echo "Done. The bundle in cli/dist/ is portable - copy it anywhere:"
        echo "    ./cli/dist/ofin config show"
        echo "    python3 cli/dist/ofin.pyz --env-file cli/dist/ofin.env us auth token"
        echo
        echo "Build outputs (cli/dist/) are gitignored."
        ;;
    *)
        # Default: run the CLI from the repo (dev mode). Pass all args through.
        export PYTHONPATH="$CLI_DIR:${PYTHONPATH:-}"
        exec "$PY" -m ofin "$@"
        ;;
esac
