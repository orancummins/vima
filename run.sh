#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"
VIMA_PORT=9021
CHAT_PORT=3333
CHAT_DIR="$SCRIPT_DIR/chat"
CHAT_PID_FILE="$CHAT_DIR/.server.pid"

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
  kill_port $CHAT_PORT
  [[ -f "$CHAT_PID_FILE" ]] && rm -f "$CHAT_PID_FILE"
  echo "All servers stopped."
  exit 0
fi

# ── Start: free ports ─────────────────────────────────────────────────
kill_port $VIMA_PORT
kill_port $CHAT_PORT

cd "$SCRIPT_DIR"

# ── Start chat server in background ───────────────────────────────────
if [[ -d "$CHAT_DIR" ]]; then
  echo "Starting vima-chat on http://127.0.0.1:$CHAT_PORT"
  FLASK_DEBUG=0 nohup python3 "$CHAT_DIR/app.py" > "$CHAT_DIR/server.log" 2>&1 &
  CHAT_PID=$!
  echo "$CHAT_PID" > "$CHAT_PID_FILE"

  # Wait briefly and confirm
  sleep 1.5
  if kill -0 "$CHAT_PID" 2>/dev/null; then
    echo "vima-chat running (PID $CHAT_PID) — logs: chat/server.log"
  else
    echo "⚠  vima-chat failed to start. Check chat/server.log"
  fi
else
  echo "⚠  chat/ directory not found — skipping vima-chat"
fi

# ── Start vima in foreground ──────────────────────────────────────────
echo "Starting vima on http://127.0.0.1:$VIMA_PORT"
exec python3 app.py
