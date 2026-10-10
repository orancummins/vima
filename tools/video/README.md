# Walkthrough video

Makes the narrated Solution Studio walkthrough (about three minutes, 1920×1080)
straight from the running app, so it can be re-made whenever the UI or the
script changes. The script, with timings and what happens on screen, is in
[docs/video/solution-studio-video-script.md](../../docs/video/solution-studio-video-script.md).

| Step | File | What it does |
|---|---|---|
| Script | `narration.json` | Every sentence, with its pause and pace, grouped into eight sections |
| Voice | `tts.py` | Voices each sentence with Kokoro-82M (`af_heart`), trims and joins them → `out/narration.wav` + `out/timeline.json` |
| Check | `check_voice.py` | Optional: plays the voice back through Whisper and flags any sentence heard differently |
| Film | `record.js` | Drives Solution Studio and Find A Card with Playwright, every action timed from the voice track; saves Chrome's timestamped screencast frames → `out/frames/` |
| Build | `build.py` | Lays the frames on the narration's clock, adds the voice and fades → `out/Mastercard-Solution-Studio.mp4` (and `out/stills/` with `--stills`) |

## Make it

1. Start Solution Studio (`./run.sh` or `.\run.bat`) and Find A Card on port
   5432. Check that the Find A Card use case shows the app, not "Service not
   running".
2. Have **ffmpeg**, **Node** with Playwright (`npm install -g playwright`,
   then `npx playwright install chromium`) and **Python 3**.
3. Run:

   ```bash
   tools/video/run.sh                 # voice, film, build
   tools/video/run.sh --no-voice      # re-film with the existing voice track
   tools/video/run.sh --voice-only    # just re-voice after editing narration.json
   ```

   The first run creates `tools/video/.venv` and downloads the Kokoro model
   (~330 MB) into `tools/video/kokoro-multi-lang-v1_0`. On Windows, run the
   same steps by hand:

   ```bat
   python -m venv tools\video\.venv
   tools\video\.venv\Scripts\pip install -r tools\video\requirements.txt
   tools\video\.venv\Scripts\python tools\video\tts.py
   node tools\video\record.js --base http://localhost:9021
   tools\video\.venv\Scripts\python tools\video\build.py --stills
   ```

   (set `NODE_PATH` to the output of `npm root -g` so `record.js` finds the
   global Playwright, and `KOKORO` to the model folder if it is elsewhere).

The take runs in real time in a headless browser; nothing on your screen
moves. It uses whatever the app has — real sandbox keys give real API
responses, otherwise the simulator answers. It **never provisions keys**: the
welcome dialog is opened directly and "Provision Selected APIs" is only
hovered.

## Change it

- **Words:** edit `narration.json` (`say`, `pause` in seconds, optional
  `speed`), then re-run everything — actions are scheduled from the new
  timings automatically. Write sentences as they are spoken; numbers in
  words. Run `check_voice.py` (needs a sherpa-onnx Whisper model, e.g.
  `sherpa-onnx-whisper-base.en` from the sherpa-onnx `asr-models` release,
  at `$WHISPER`) to catch mispronunciations.
- **Voice:** `SID` picks another Kokoro speaker (3 = `af_heart`; British
  voices are 20–27), `SPEED` scales the pace.
- **Choreography:** each section of `record.js` places clicks and hovers
  relative to a sentence's start, e.g. `at(S('p2') + 1.3)`. The run log says
  if a step fails or the take falls behind the narration; `out/stills/`
  shows a frame just after each sentence starts.
