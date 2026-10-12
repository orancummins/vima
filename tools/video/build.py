#!/usr/bin/env python3
"""Turn the recorded frames and the narration into the finished video.

record.js saves Chrome's screencast frames, each stamped with the wall-clock
time it was drawn, and the moment the take started (t0, which is time zero
of narration.wav). This lays every frame on that clock for exactly as long
as it was on screen, resamples to a constant 30 fps, and lays narration.wav
underneath with a fade in and out, so picture and voice line up to the frame.

Writes out/Mastercard-Solution-Studio.mp4 (1920×1080, 30 fps, H.264 + AAC)
and, with --stills, a JPEG a moment after every sentence starts in
out/stills/ for a quick check against the script.

    python tools/video/build.py [--stills]
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=os.path.join(HERE, "out"))
    ap.add_argument("--stills", action="store_true", help="also write a still just after every sentence starts")
    args = ap.parse_args()
    out = args.out

    tl = json.load(open(os.path.join(out, "timeline.json"), encoding="utf-8"))
    rec = json.load(open(os.path.join(out, "frames.json"), encoding="utf-8"))
    total = tl["total"]
    t0 = rec["t0"]
    frames = sorted(rec["frames"], key=lambda f: f["ts"])
    if not frames:
        sys.exit("no frames recorded")

    # The frame on screen at t0 opens the video; later frames follow on the narration clock.
    first = max((i for i, f in enumerate(frames) if f["ts"] <= t0), default=0)
    timeline = [(0.0, frames[first]["file"])]
    timeline += [(f["ts"] - t0, f["file"]) for f in frames[first + 1:] if 0 < f["ts"] - t0 < total]
    listing = os.path.join(out, "frames.txt")
    with open(listing, "w") as fh:
        for (t, file), nxt in zip(timeline, timeline[1:] + [(total, None)], strict=True):
            fh.write(f"file 'frames/{file}'\nduration {max(0.001, nxt[0] - t):.4f}\n")
        fh.write(f"file 'frames/{timeline[-1][1]}'\n")  # the concat demuxer needs the last file repeated
    gaps = [b[0] - a[0] for a, b in zip(timeline, timeline[1:], strict=False)]
    print(f"{len(timeline)} frames over {total:.1f} s; longest still {max(gaps or [0]):.2f} s")

    final = os.path.join(out, "Mastercard-Solution-Studio.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", listing,
         "-i", os.path.join(out, "narration.wav"),
         "-filter_complex",
         f"[0:v]fps=30,scale=1920:1080:flags=lanczos,format=yuv420p,"
         f"fade=t=in:st=0:d=0.8,fade=t=out:st={total - 1.4:.2f}:d=1.4[v];"
         f"[1:a]loudnorm=I=-16:TP=-1.5:LRA=11,afade=t=out:st={total - 1.2:.2f}:d=1.2,aresample=48000[a]",
         "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "slow", "-crf", "19",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-t", f"{total:.3f}", final])
    print("wrote", final)

    if args.stills:
        stills = os.path.join(out, "stills")
        shutil.rmtree(stills, ignore_errors=True)
        os.makedirs(stills)
        for sec in tl["sections"]:
            for lid, line in sec["lines"].items():
                t = min(total - 0.1, line["start"] + 0.9)
                run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", final, "-frames:v", "1",
                     "-vf", "scale=960:-1", os.path.join(stills, f"{t:06.1f}_{lid}.jpg")])
        print("stills in", stills)
    return 0


if __name__ == "__main__":
    sys.exit(main())
