#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

# ── Colours ──────────────────────────────────────────────────────────
GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; RESET='\033[0m'
info()  { echo -e "${GREEN}▶ $*${RESET}"; }
warn()  { echo -e "${YELLOW}⚠ $*${RESET}"; }
error() { echo -e "${RED}✗ $*${RESET}"; }

PORT=3333
PID_FILE="$DIR/.server.pid"

# ── Check .env ───────────────────────────────────────────────────────
if [[ ! -f "$DIR/.env" ]]; then
  warn ".env not found — copying from .env.example"
  cp "$DIR/.env.example" "$DIR/.env"
  error "Please add your ANTHROPIC_API_KEY to .env then re-run."
  exit 1
fi

if grep -q "your_api_key_here" "$DIR/.env" 2>/dev/null; then
  error "ANTHROPIC_API_KEY is still the placeholder value in .env — please set it."
  exit 1
fi

# ── Stop existing server ─────────────────────────────────────────────
stop_server() {
  # Kill by saved PID first
  if [[ -f "$PID_FILE" ]]; then
    OLD_PID=$(cat "$PID_FILE")
    if kill -0 "$OLD_PID" 2>/dev/null; then
      info "Stopping existing server (PID $OLD_PID)…"
      kill "$OLD_PID"
      sleep 1
    fi
    rm -f "$PID_FILE"
  fi

  # Also kill anything else holding the port
  PIDS=$(lsof -ti tcp:"$PORT" 2>/dev/null || true)
  if [[ -n "$PIDS" ]]; then
    info "Freeing port $PORT (PID(s): $PIDS)…"
    echo "$PIDS" | xargs kill 2>/dev/null || true
    sleep 1
  fi
}

# ── Install dependencies ─────────────────────────────────────────────
install_deps() {
  info "Installing / verifying dependencies…"
  python3 -m pip install -q -r "$DIR/requirements.txt"
  info "Dependencies OK."
}

# ── Start server ─────────────────────────────────────────────────────
start_server() {
  info "Starting Vima Chat on http://localhost:$PORT …"
  nohup python3 "$DIR/app.py" > "$DIR/server.log" 2>&1 &
  SERVER_PID=$!
  echo "$SERVER_PID" > "$PID_FILE"

  # Wait briefly and confirm it came up
  sleep 1.5
  if kill -0 "$SERVER_PID" 2>/dev/null; then
    info "Server running  (PID $SERVER_PID) — logs: server.log"
    info "Open: http://localhost:$PORT"
  else
    error "Server failed to start. Check server.log:"
    tail -20 "$DIR/server.log"
    rm -f "$PID_FILE"
    exit 1
  fi
}

# ── Main ─────────────────────────────────────────────────────────────
case "${1:-start}" in
  start)
    stop_server
    install_deps
    start_server
    ;;
  stop)
    stop_server
    info "Server stopped."
    ;;
  restart)
    stop_server
    install_deps
    start_server
    ;;
  logs)
    tail -f "$DIR/server.log"
    ;;
  status)
    if [[ -f "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
      info "Server is running (PID $(cat "$PID_FILE")) on port $PORT."
    else
      warn "Server is not running."
    fi
    ;;
  *)
    echo "Usage: $0 {start|stop|restart|logs|status}"
    exit 1
    ;;
esac
