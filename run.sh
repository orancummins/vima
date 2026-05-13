#!/usr/bin/env bash
set -e

PORT=9021
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"

# Kill any process already listening on the port
if lsof -ti tcp:$PORT &>/dev/null; then
  echo "Stopping existing server on port $PORT..."
  lsof -ti tcp:$PORT | xargs kill -9 2>/dev/null || true
  sleep 0.5
fi

# Activate venv if present
if [[ -f "$VENV_DIR/bin/activate" ]]; then
  source "$VENV_DIR/bin/activate"
fi

echo "Starting vima on http://127.0.0.1:$PORT"
cd "$SCRIPT_DIR"
exec python3 app.py
