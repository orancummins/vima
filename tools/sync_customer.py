#!/usr/bin/env python3
"""Refresh a customer's standalone page (customers/<id>/).

A customer's page is built outside Solution Studio (for Saudi National Bank,
in the ``snb`` project next to this one) on the same layer-picture engine as
the Platform tab, and copied into ``customers/<id>/`` with the customer's
logos added over its heading. This script copies a newer version in and checks that Studio can still use it:

* the functions and state ``mcos/web/mcos-bridge.js`` drives (the same
  checks as ``tools/sync_mcos.py``),
* the customer's text swaps, and
* every product and journey named in the customer's ``CUSTOMER["studio"]``
  and ``CUSTOMER["journey_bundles"]``.

Usage::

    python tools/sync_customer.py snb ../snb/SNB_Operating_System.html
    python tools/sync_customer.py snb ../snb/SNB_Operating_System.html --notes ../snb/*.md
    python tools/sync_customer.py --check            # check every customer's current copy

Exits non-zero, without touching the copy, if a check fails.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sync_mcos import REQUIRED_NAMES, REQUIRED_SNIPPETS  # noqa: E402

import customers  # noqa: E402
import mcos  # noqa: E402


def check(c: dict, src: str) -> list[str]:
    problems = []
    for name in REQUIRED_NAMES:
        if not re.search(rf"(?:\bfunction\s+{name}\s*\(|\b(?:const|let|var)\s+[^;]*?\b{name}\s*=)", src):
            problems.append(f"the page no longer defines {name!r}, which mcos-bridge.js uses")
    for snippet in REQUIRED_SNIPPETS:
        if snippet not in src:
            problems.append(f"the page no longer builds {snippet!r}, which mcos-bridge.js re-colours")
    for old, _new in c["text_swaps"]:
        if old not in src:
            problems.append(f"the page no longer says {old!r}, which Solution Studio renames")
    if '<div class="wrap">' not in src:
        problems.append('no <div class="wrap"> to put Studio\'s theme in front of')
    try:
        entries = mcos.parse_catalog(src)
    except ValueError as exc:
        return problems + [f"the page's inventory cannot be read: {exc}"]
    products = {e["id"] for e in entries if e["kind"] == "product"}
    journeys = {e["id"] for e in entries if e["kind"] == "outcome"}
    for pid in c["studio"]:
        if pid not in products:
            problems.append(f"product {pid!r} (mapped to Studio in customers/{c['id']}) is gone")
    for oid in c["journey_bundles"]:
        if oid not in journeys:
            problems.append(f"journey {oid!r} (mapped to Studio bundles in customers/{c['id']}) is gone")
    return problems


def _report(label: str, problems: list[str]) -> None:
    for p in problems:
        print(f"✗ {label}: {p}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("customer", nargs="?", help="customer id (its folder under customers/)")
    ap.add_argument("page", nargs="?", help="the new standalone page")
    ap.add_argument("--notes", nargs="*", default=[], help="notes files to copy in alongside it")
    ap.add_argument("--check", action="store_true", help="only check the current copies")
    args = ap.parse_args()

    if args.check or not args.customer:
        failed = 0
        for c in customers.all_customers():
            problems = check(c, customers.page_source(c))
            _report(c["id"], problems)
            failed += bool(problems)
            print(f"✓ {c['id']}: page is compatible" if not problems else f"{c['id']}: {len(problems)} problem(s)")
        return 1 if failed else 0

    c = customers.get(args.customer)
    if c is None:
        print(f"✗ no customer {args.customer!r} under customers/")
        return 1
    if not args.page:
        ap.error("give the page to copy in, or --check")
    with open(args.page, encoding="utf-8") as f:
        src = f.read()
    problems = check(c, src)
    if problems:
        _report(c["id"], problems)
        print(f"customers/{c['id']}/{c['page']} left unchanged. Update customers/{c['id']}/__init__.py first.")
        return 1
    with open(customers.page_path(c), "w", encoding="utf-8") as f:
        f.write(customers.with_brand(src, c))   # the customer's logos over the page's kicker
    print(f"✓ customers/{c['id']}/{c['page']} updated from {args.page}")
    for note in args.notes:
        shutil.copyfile(note, os.path.join(c["dir"], os.path.basename(note)))
        print(f"✓ customers/{c['id']}/{os.path.basename(note)} updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
