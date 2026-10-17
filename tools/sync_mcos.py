#!/usr/bin/env python3
"""Refresh the vendored layer picture (the Mastercard Operating System in maos).

The platform tab shows ``src/layers.artifact.html`` from the maos
project (https://github.com/orancummins/maos), copied verbatim into
``mcos/vendor/``. This script copies a newer version in, records where it came
from in ``mcos/vendor/VERSION``, and checks that everything Solution Studio
relies on is still there:

* the functions and state ``mcos/web/mcos-bridge.js`` drives, and
* every product and outcome named in ``mcos/__init__.py``.

Usage::

    python tools/sync_mcos.py                     # clone maos (main) into a temp dir
    python tools/sync_mcos.py --maos ../maos      # use an existing checkout
    python tools/sync_mcos.py --ref <commit|tag>  # pin a version
    python tools/sync_mcos.py --check             # only check the current copy

Exits non-zero, without touching the vendored copy, if a check fails.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

import mcos  # noqa: E402

REPO = "https://github.com/orancummins/maos"
SOURCE = os.path.join("src", "layers.artifact.html")

# Top-level names in the picture's script that mcos-bridge.js uses.
REQUIRED_NAMES = (
    "MAP", "st", "OUTCOMES", "LAYERS", "TILE", "PADS", "sraf", "st0", "reduce", "f", "esc",
    "spin", "layout", "renderSide", "renderPick", "detailHtml", "tagHtml", "openTile",
    "openProduct", "closeDrawer", "drawerOpen", "setFocus", "pickOut", "clearPick",
    "openStack", "closeStack", "endIntro", "drawGlobe", "DOTS", "phi", "OX", "GR", "GY", "DEG",
)
# Gradients mcos-bridge.js re-colours (restyleDefs), as the picture builds them.
REQUIRED_SNIPPETS = (
    'lg("st"+k', 'lg("gs"+k', 'lg("bt"+k', 'lg("gc"+k',
    'id="ug"', 'id="gg"', 'id="gt"', 'id="ghl"', 'id="grl"', 'id="gha"',
)


def check(src: str) -> list[str]:
    problems = []
    for name in REQUIRED_NAMES:
        if not re.search(rf"(?:\bfunction\s+{name}\s*\(|\b(?:const|let|var)\s+[^;]*?\b{name}\s*=)", src):
            problems.append(f"the picture no longer defines {name!r}, which mcos-bridge.js uses")
    for snippet in REQUIRED_SNIPPETS:
        if snippet not in src:
            problems.append(f"the picture no longer builds {snippet!r}, which mcos-bridge.js re-colours")
    for old, _new in mcos.TEXT_SWAPS:
        if old not in src:
            problems.append(f"the picture no longer says {old!r}, which Solution Studio renames")
    if "</style>" not in src:
        problems.append("no </style> to split the head from the body at")
    products = set(re.findall(r'\bP\("([a-z0-9]+)",', src))
    outcomes = set(re.findall(r'\{id:"([a-z0-9]+)", who:"', src))
    for api_id, pid in mcos.API_PRODUCTS.items():
        if pid not in products:
            problems.append(f"product {pid!r} (home of API {api_id!r}) is gone")
    for uc_id, pids in mcos.USE_CASE_PRODUCTS.items():
        for pid in pids:
            if pid not in products:
                problems.append(f"product {pid!r} (for use case {uc_id!r}) is gone")
    for oid in mcos.OUTCOME_BUNDLES:
        if oid not in outcomes:
            problems.append(f"outcome {oid!r} is gone")
    problems += mcos.catalog_problems(src)
    return problems


def _git(*args: str, cwd: str | None = None) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--maos", help="path to an existing maos checkout (default: clone it)")
    ap.add_argument("--ref", help="commit, tag or branch to take (default: the checkout's HEAD / main)")
    ap.add_argument("--check", action="store_true", help="only check the vendored copy")
    args = ap.parse_args()

    if args.check:
        problems = check(mcos.vendor_source())
        for p in problems:
            print(f"✗ {p}")
        print("✓ vendored picture is compatible" if not problems else f"{len(problems)} problem(s)")
        return 1 if problems else 0

    tmp = None
    try:
        checkout = args.maos
        if not checkout:
            tmp = tempfile.mkdtemp(prefix="maos-")
            checkout = os.path.join(tmp, "maos")
            print(f"Cloning {REPO} …")
            _git("clone", "--quiet", REPO, checkout)
        if args.ref:
            _git("checkout", "--quiet", args.ref, cwd=checkout)
        commit = _git("rev-parse", "HEAD", cwd=checkout)
        committed = _git("log", "-1", "--format=%cI", cwd=checkout)

        with open(os.path.join(checkout, SOURCE), encoding="utf-8") as f:
            src = f.read()
        problems = check(src)
        if problems:
            for p in problems:
                print(f"✗ {p}")
            print("Vendored copy left unchanged. Update mcos/__init__.py or mcos/web/mcos-bridge.js first.")
            return 1

        shutil.copyfile(os.path.join(checkout, SOURCE), mcos.VENDOR_FILE)
        with open(os.path.join(os.path.dirname(mcos.VENDOR_FILE), "VERSION"), "w", encoding="utf-8") as f:
            f.write(f"source: {REPO}\nfile: {SOURCE.replace(os.sep, '/')}\ncommit: {commit}\ncommitted: {committed}\n")
        print(f"✓ mcos/vendor/layers.artifact.html updated to {commit[:12]} ({committed})")
        return 0
    finally:
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
