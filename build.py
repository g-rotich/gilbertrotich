#!/usr/bin/env python3
"""
build.py — Portfolio builder
=============================
Reads template.html, finds every <!-- INCLUDE: sections/xxx.html -->
comment, replaces it with the contents of that file, and writes
the result to index.html.

Run locally:  python3 build.py
Run on push:  handled automatically by .github/workflows/build.yml
"""

import re
from pathlib import Path

TEMPLATE = Path("template.html")
OUTPUT   = Path("index.html")
SECTIONS = Path("sections")

# ── Read template ──────────────────────────────────────────────────────────────
if not TEMPLATE.exists():
    raise FileNotFoundError(
        "template.html not found. "
        "Make sure template.html is in the repo root."
    )

source = TEMPLATE.read_text(encoding="utf-8")

# ── Replace each include comment with the matching section file ────────────────
# Matches:  <!-- INCLUDE: sections/papers.html -->
pattern = re.compile(r'<!--\s*INCLUDE:\s*(sections/[\w\-]+\.html)\s*-->')

def replace_include(match):
    filepath = Path(match.group(1))
    if not filepath.exists():
        print(f"  WARNING: {filepath} not found — leaving placeholder.")
        return f"<!-- MISSING: {filepath} -->"
    content = filepath.read_text(encoding="utf-8").strip()
    print(f"  ✓  Included {filepath}  ({len(content):,} chars)")
    return content

result = pattern.sub(replace_include, source)

# ── Write output ───────────────────────────────────────────────────────────────
OUTPUT.write_text(result, encoding="utf-8")
print(f"\nBuild complete → {OUTPUT}  ({OUTPUT.stat().st_size:,} bytes)")
