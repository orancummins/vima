#!/usr/bin/env bash
# Make the Solution Studio walkthrough video end to end:
#   voice (tts.py) → film the running app (record.js) → cut and mux (build.py).
#
# Needs Solution Studio running (./run.sh in the repo root) and Find A Card on
# port 5432. Usage: tools/video/run.sh [--base http://localhost:9021] [--voice-only] [--no-voice]
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
BASE="http://localhost:9021"
VOICE=1; FILM=1
while [ $# -gt 0 ]; do
  case "$1" in
    --base) BASE="$2"; shift 2 ;;
    --voice-only) FILM=0; shift ;;
    --no-voice) VOICE=0; shift ;;
    *) echo "unknown option $1"; exit 2 ;;
  esac
done

for tool in ffmpeg node; do
  command -v "$tool" >/dev/null || { echo "✗ $tool is required"; exit 1; }
done

# Python environment for the voice and the build.
VENV="$HERE/.venv"
if [ ! -x "$VENV/bin/python" ]; then
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install -q -r "$HERE/requirements.txt"
fi
PY="$VENV/bin/python"

# The Kokoro voice model (~330 MB), once.
MODEL="${KOKORO:-$HERE/kokoro-multi-lang-v1_0}"
if [ ! -f "$MODEL/model.onnx" ]; then
  echo "Downloading the Kokoro voice model…"
  curl -L --retry 4 -C - -o "$HERE/kokoro.tar.bz2" \
    https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/kokoro-multi-lang-v1_0.tar.bz2
  tar xjf "$HERE/kokoro.tar.bz2" -C "$HERE" && rm "$HERE/kokoro.tar.bz2"
fi

if [ "$VOICE" = 1 ]; then
  KOKORO="$MODEL" "$PY" "$HERE/tts.py"
fi
[ "$FILM" = 1 ] || exit 0

curl -s -o /dev/null --max-time 5 "$BASE/app" || { echo "✗ Solution Studio is not answering at $BASE"; exit 1; }
curl -s -o /dev/null --max-time 5 "http://localhost:5432/" || { echo "✗ Find A Card is not running on port 5432"; exit 1; }

NODE_PATH="${NODE_PATH:-$(npm root -g)}" node "$HERE/record.js" --base "$BASE"
"$PY" "$HERE/build.py" --stills
echo "✓ $HERE/out/Mastercard-Solution-Studio.mp4"
