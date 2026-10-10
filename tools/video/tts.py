#!/usr/bin/env python3
"""Voice the Solution Studio video from narration.json.

Each sentence is synthesised on its own with Kokoro-82M v1.0 (voice af_heart)
so it keeps a natural falling ending, trimmed of silence, faded in and out
over 12 ms, and joined to the next with the pause narration.json gives it.
This is the approach of the maos project's videos (maos/video/layers/tts.py).

Writes, under --out (default tools/video/out):
  narration.wav   the whole voice track, 24 kHz mono
  timeline.json   {"total": s, "sections": [{"id", "title", "start", "end",
                   "lines": {line_id: {"start", "end", "say"}}}]}, times in
                   seconds from the start of the track. record.js schedules
                   every action from it.

Needs: pip install -r tools/video/requirements.txt, and the model folder
kokoro-multi-lang-v1_0 from the sherpa-onnx "tts-models" release, at
tools/video/kokoro-multi-lang-v1_0 or wherever $KOKORO points.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np
import sherpa_onnx
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))


def load_tts(model_dir: str) -> sherpa_onnx.OfflineTts:
    m = model_dir
    for name in ("model.onnx", "voices.bin", "tokens.txt"):
        if not os.path.exists(os.path.join(m, name)):
            sys.exit(f"Kokoro model not found in {m} (missing {name}). Download kokoro-multi-lang-v1_0 "
                     "from https://github.com/k2-fsa/sherpa-onnx/releases/tag/tts-models and set $KOKORO.")
    cfg = sherpa_onnx.OfflineTtsConfig(
        model=sherpa_onnx.OfflineTtsModelConfig(
            kokoro=sherpa_onnx.OfflineTtsKokoroModelConfig(
                model=f"{m}/model.onnx", voices=f"{m}/voices.bin", tokens=f"{m}/tokens.txt",
                data_dir=f"{m}/espeak-ng-data", dict_dir=f"{m}/dict",
                lexicon=f"{m}/lexicon-us-en.txt,{m}/lexicon-zh.txt",
            ),
            num_threads=int(os.environ.get("THREADS", "2")), provider="cpu",
        ),
        max_num_sentences=1,
    )
    return sherpa_onnx.OfflineTts(cfg)


def trim(x: np.ndarray, sr: int, th: float = 0.004) -> np.ndarray:
    idx = np.where(np.abs(x) > th)[0]
    if len(idx) == 0:
        return x
    return x[max(0, idx[0] - int(0.03 * sr)): min(len(x), idx[-1] + int(0.09 * sr))]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--narration", default=os.path.join(HERE, "narration.json"))
    ap.add_argument("--out", default=os.path.join(HERE, "out"))
    ap.add_argument("--model", default=os.environ.get("KOKORO", os.path.join(HERE, "kokoro-multi-lang-v1_0")))
    args = ap.parse_args()

    spec = json.load(open(args.narration, encoding="utf-8"))
    voice = spec.get("voice", {})
    sid = int(os.environ.get("SID", voice.get("sid", 3)))
    base_speed = float(os.environ.get("SPEED", voice.get("speed", 1.0)))
    tts = load_tts(args.model)
    os.makedirs(args.out, exist_ok=True)

    sr = 24000
    out = [np.zeros(int(spec.get("lead", 0.8) * sr), dtype=np.float32)]
    t = spec.get("lead", 0.8)
    sections = []
    for sec in spec["sections"]:
        start = t
        lines = {}
        for line in sec["lines"]:
            a = tts.generate(line["say"], sid=sid, speed=base_speed * line.get("speed", 1.0))
            sr = a.sample_rate
            x = trim(np.array(a.samples, dtype=np.float32), sr)
            f = int(0.012 * sr)
            x[:f] *= np.linspace(0, 1, f)
            x[-f:] *= np.linspace(1, 0, f)
            lines[line["id"]] = {"start": round(t, 3), "end": round(t + len(x) / sr, 3), "say": line["say"]}
            out.append(x)
            t += len(x) / sr
            pause = line.get("pause", 0.45)
            out.append(np.zeros(int(pause * sr), dtype=np.float32))
            t += pause
            print(f"{line['id']:>4}  {lines[line['id']]['start']:7.2f}–{lines[line['id']]['end']:7.2f}  {line['say']}", flush=True)
        sections.append({"id": sec["id"], "title": sec.get("title", ""), "start": round(start, 3),
                         "end": round(t, 3), "lines": lines})
    tail = spec.get("tail", 2.5)
    out.append(np.zeros(int(tail * sr), dtype=np.float32))
    t += tail
    sections[-1]["end"] = round(t, 3)

    y = np.concatenate(out)
    y = y / max(1e-6, float(np.max(np.abs(y)))) * 0.89
    sf.write(os.path.join(args.out, "narration.wav"), y, sr, subtype="PCM_16")
    json.dump({"total": round(t, 3), "sections": sections},
              open(os.path.join(args.out, "timeline.json"), "w", encoding="utf-8"), indent=1)
    print(f"total {t:.1f} s ({int(t // 60)}:{int(t % 60):02d})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
