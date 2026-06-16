#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"
VIMA_PORT=9021
APP_ARGS=("$@")

# ── Helpers ──────────────────────────────────────────────────────────
kill_port() {
  local port=$1
  local pids
  pids=$(lsof -ti tcp:"$port" 2>/dev/null || true)
  if [[ -n "$pids" ]]; then
    echo "Stopping process on port $port..."
    # Try graceful shutdown first
    echo "$pids" | xargs kill -TERM 2>/dev/null || true
    # Wait for processes to exit gracefully
    for i in 1 2 3 4 5; do
      sleep 0.5
      remaining=$(lsof -ti tcp:"$port" 2>/dev/null || true)
      if [[ -z "$remaining" ]]; then
        break
      fi
    done
    # Force kill if still running
    remaining=$(lsof -ti tcp:"$port" 2>/dev/null || true)
    if [[ -n "$remaining" ]]; then
      echo "Forcing kill on port $port..."
      echo "$remaining" | xargs kill -9 2>/dev/null || true
    fi
  fi
}

# ── Create venv if missing ────────────────────────────────────────────
if [[ ! -f "$VENV_DIR/bin/activate" ]]; then
  echo "Creating Python virtual environment..."
  python3 -m venv "$VENV_DIR"
fi

# ── Activate venv ─────────────────────────────────────────────────────
source "$VENV_DIR/bin/activate"

# ── Bootstrap config/.env on first run ───────────────────────────────
if [[ ! -f "$SCRIPT_DIR/config/.env" && -f "$SCRIPT_DIR/config/.env.example" ]]; then
  cp "$SCRIPT_DIR/config/.env.example" "$SCRIPT_DIR/config/.env"
  echo "Created config/.env from .env.example — open the app and fill in your credentials."
fi

# ── Install / sync dependencies ───────────────────────────────────────
if [[ -f "$SCRIPT_DIR/requirements.txt" ]]; then
  echo "Installing dependencies..."
  python3 -m pip install -q --use-feature=truststore -r "$SCRIPT_DIR/requirements.txt"
fi

# ── Set up key-automation tool (once, on first run) ───────────────────
# Use a sentinel file as the install marker — checking for an interpreter
# alone is not enough because it exists immediately after `python -m venv`
# even if the subsequent pip install failed. We install dependencies
# directly (not `pip install -e .`) so pip never generates console_script
# shims (e.g. mcd-key-automation, playwright), which corporate AV /
# lockdown policies on Windows often block as unsigned executables.
TOOL_DIR="$SCRIPT_DIR/tools/mcd-key-automation"
TOOL_VENV="$TOOL_DIR/.venv"
TOOL_PY="$TOOL_VENV/bin/python"
TOOL_MARKER="$TOOL_VENV/.tool-installed"
if [[ ! -f "$TOOL_MARKER" ]]; then
  echo ""
  echo "Setting up API key automation tool (first run only)..."
  if [[ -f "$TOOL_PY" ]]; then
    echo "  Detected incomplete tool venv from a previous run - reinstalling..."
  fi
  echo "  [1/4] Creating Python virtual environment..."
  python3 -m venv "$TOOL_VENV"
  echo "  [2/4] Upgrading pip..."
  "$TOOL_PY" -m pip install --upgrade pip -q
  echo "  [3/4] Installing dependencies via python -m pip (no console_script shims)..."
  "$TOOL_PY" -m pip install --use-feature=truststore -r "$TOOL_DIR/requirements.txt"
  echo "  [4/4] Installing browser via python -m playwright (downloading, please wait)..."
  "$TOOL_PY" -m playwright install chromium
  # Belt-and-braces: remove any console_script shims left behind by older installs.
  rm -f "$TOOL_VENV/bin/mcd-key-automation" 2>/dev/null || true
  touch "$TOOL_MARKER"
  echo ""
  echo "API key automation tool ready."
  echo ""
fi

# ── Stop mode ─────────────────────────────────────────────────────────
if [[ "${1:-}" == "stop" ]]; then
  kill_port $VIMA_PORT
  echo "Server stopped."
  exit 0
fi

# ── Free port and start ───────────────────────────────────────────────
kill_port $VIMA_PORT

cd "$SCRIPT_DIR"

# ViMA Chat is embedded in-process as a Flask Blueprint — no separate
# chat server is needed.
echo "Starting vima on http://127.0.0.1:$VIMA_PORT"
exec python3 app.py "${APP_ARGS[@]}"
