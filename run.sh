#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"
VIMA_PORT=9021

# ── Helpers ──────────────────────────────────────────────────────────
kill_port() {
  local port=$1
  local pids
  pids=$(lsof -ti tcp:"$port" 2>/dev/null || true)
  if [[ -n "$pids" ]]; then
    echo "Stopping process on port $port..."
    echo "$pids" | xargs kill -9 2>/dev/null || true
    sleep 0.5
  fi
}

# ── Activate venv ─────────────────────────────────────────────────────
if [[ -f "$VENV_DIR/bin/activate" ]]; then
  source "$VENV_DIR/bin/activate"
fi

# ── Install / sync dependencies ───────────────────────────────────────
if [[ -f "$SCRIPT_DIR/requirements.txt" ]]; then
  echo "Installing dependencies..."
  pip install -q -r "$SCRIPT_DIR/requirements.txt"
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
exec python3 app.py
