#!/usr/bin/env python3
"""Listen back to the narration with Whisper and flag sentences it hears differently.

Optional quality check after tts.py: a word the voice mispronounces usually
comes back from speech recognition as a different word. Needs a sherpa-onnx
Whisper model (e.g. sherpa-onnx-whisper-base.en from the sherpa-onnx
"asr-models" release) at $WHISPER.

    python tools/video/check_voice.py
"""
from __future__ import annotations

import json
import os
import re
import sys

import numpy as np
import sherpa_onnx
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")


def words(s: str) -> list[str]:
    """Lower-case words, with British spellings and compounds folded to how Whisper writes them."""
    s = s.lower().replace("-", " ").replace("cybersecurity", "cyber security").replace("'s ", " ")
    s = re.sub(r"is(e|ed|es|ing|ation|ations)\b", r"iz\1", s)
    return re.findall(r"[a-z0-9']+", s)


def main() -> int:
    w = os.environ.get("WHISPER", os.path.join(HERE, "sherpa-onnx-whisper-base.en"))
    rec = sherpa_onnx.OfflineRecognizer.from_whisper(
        encoder=f"{w}/base.en-encoder.int8.onnx", decoder=f"{w}/base.en-decoder.int8.onnx",
        tokens=f"{w}/base.en-tokens.txt", num_threads=2)
    audio, sr = sf.read(os.path.join(OUT, "narration.wav"), dtype="float32")
    tl = json.load(open(os.path.join(OUT, "timeline.json"), encoding="utf-8"))
    flagged = 0
    for sec in tl["sections"]:
        for lid, line in sec["lines"].items():
            seg = audio[int(line["start"] * sr): int(line["end"] * sr) + int(0.1 * sr)]
            s = rec.create_stream()
            s.accept_waveform(sr, np.ascontiguousarray(seg))
            rec.decode_stream(s)
            heard = s.result.text.strip()
            want, got = words(line["say"]), words(heard)
            missing = [x for x in want if x not in got]
            mark = "  " if len(missing) <= 1 else "✗ "
            flagged += mark != "  "
            print(f"{mark}{lid:>4}  {heard}" + (f"   [not heard: {' '.join(missing)}]" if missing else ""))
    print(f"{flagged} sentence(s) to listen to" if flagged else "all sentences heard as written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
