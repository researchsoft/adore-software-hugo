#!/usr/bin/env python3
"""Verify our /declaration/ page text matches the canonical live site.

This compares the human-readable declaration text on
https://adore.software/declaration/ against our locally rendered page.

What it compares
----------------
The "declaration text" we care about for parity is:
  * the four Recommendations category titles,
  * the twelve recommendation sentences,
  * the "Cite as", "Contributors" and "Who can sign?" prose.

The dynamic signatory grid is data-driven (data/signatories.yaml), not
declaration prose, so it is intentionally excluded from the comparison.

How extraction works
---------------------
Live site: WordPress renders the recommendations as plain numbered <ol>
items (no "Recommendation N:" prefix). Our Hugo page renders them with an
explicit "Recommendation N:" label and curly quotes. To make the two
comparable, both sides are reduced to the same normalized segments:
numbering/labels are stripped, quotes/dashes/whitespace are normalized, so
only the actual wording is diffed.

The local side is taken from the rendered HTML (public/declaration/index.html)
so we compare apples to apples (rendered text vs rendered text). Run `hugo`
first; the script will offer to do so if the file is missing.

Usage
-----
    ./scripts/check-declaration.py
    ./scripts/check-declaration.py --build      # run `hugo` first
    ./scripts/check-declaration.py --local-only # skip network, just show local
    ./scripts/check-declaration.py --url <url>  # override live URL

Exit status is 0 when the texts match, 1 when they differ (CI-friendly).
Depends only on the Python 3 standard library.
"""

from __future__ import annotations

import argparse
import difflib
import html
import re
import subprocess
import sys
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

LIVE_URL = "https://adore.software/declaration/"
REPO_ROOT = Path(__file__).resolve().parent.parent
LOCAL_HTML = REPO_ROOT / "public" / "declaration" / "index.html"

# The four recommendation category titles, in order. Used to anchor extraction
# on both sides and as comparison segments themselves.
CATEGORY_TITLES = [
    "Research Software Practice",
    "Research Software Ecosystem",
    "Research Software Personnel",
    "Research Software Ethics",
]

# Prose headings/markers we look for after the recommendations block.
PROSE_MARKERS = ["Cite as", "Contributors", "Who can sign"]


class TextExtractor(HTMLParser):
    """Collect visible text, skipping non-content tags."""

    SKIP = {"script", "style", "noscript", "head", "nav", "footer", "header"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._skip_depth += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._skip_depth:
            self._skip_depth -= 1

    def handle_data(self, data):
        if self._skip_depth == 0:
            self.parts.append(data)

    def text(self) -> str:
        return " ".join(self.parts)


def normalize(text: str) -> str:
    """Normalize whitespace and punctuation so cosmetic differences vanish."""
    text = html.unescape(text)
    # Unify quote and dash variants.
    for ch in ("‘", "’", "′", "`"):
        text = text.replace(ch, "'")
    for ch in ("“", "”", "″", '"'):
        text = text.replace(ch, "'")
    text = text.replace("–", "-").replace("—", "-")
    text = text.replace(" ", " ")  # non-breaking space
    text = text.replace("…", "...")
    # Drop an explicit "Recommendation N:" label our page adds.
    text = re.sub(r"Recommendation\s+\d+\s*:?\s*", "", text)
    # Collapse whitespace.
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fetch_live(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "adore-declaration-check/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()
    return raw.decode("utf-8", errors="replace")


def extract_recommendation_sentences(text: str) -> list[str]:
    """Pull the twelve 'Funders should ...' sentences from normalized text.

    Each recommendation starts with "Funders should". We split on those
    boundaries and, for each chunk, keep everything up to the last sentence
    terminator (so trailing category headings such as "Research Software
    Ecosystem" that sit between recommendations are dropped).
    """
    starts = [m.start() for m in re.finditer(r"Funders should", text)]
    sentences: list[str] = []
    for idx, start in enumerate(starts):
        end = starts[idx + 1] if idx + 1 < len(starts) else len(text)
        chunk = text[start:end]
        # Trim to the last full stop so an intervening heading is excluded.
        last = chunk.rfind(".")
        if last != -1:
            chunk = chunk[: last + 1]
        sentences.append(normalize(chunk))
    return sentences


def extract_segments(full_text: str) -> dict[str, list[str] | str]:
    """Reduce a page's visible text to comparable declaration segments."""
    norm = normalize(full_text)

    segments: dict[str, list[str] | str] = {}

    # Category titles (presence/order check).
    segments["categories"] = [t for t in CATEGORY_TITLES if t in norm]

    # Recommendation sentences. Bound the search to the recommendations block
    # (between the "Recommendations" heading and the first following prose
    # marker) so trailing prose / the signatory grid is never swallowed.
    rec_start = norm.find("Recommendations")
    rec_region = norm[rec_start:] if rec_start != -1 else norm
    rec_end = len(rec_region)
    for marker in [
        "The Declaration text is available",  # local intro line after recs
        "Declaration text",                   # live visually-hidden heading
        "View full text on Zenodo",           # PDF preview block (both sides)
        "Cite as",
        "Contributors",
    ]:
        j = rec_region.find(marker)
        if j != -1:
            rec_end = min(rec_end, j)
    segments["recommendations"] = extract_recommendation_sentences(rec_region[:rec_end])

    # Prose blocks: capture the sentence(s) following each marker, up to the
    # next marker / signatories grid.
    def grab(after: str, until: list[str]) -> str:
        idx = norm.find(after)
        if idx == -1:
            return ""
        start = idx + len(after)
        end = len(norm)
        for u in until:
            j = norm.find(u, start)
            if j != -1:
                end = min(end, j)
        return normalize(norm[start:end])

    segments["cite_as"] = grab(
        "Cite as", ["Contributors"]
    ).lstrip(": ").strip()
    segments["contributors"] = grab(
        "Contributors", ["Who can sign"]
    ).strip()
    # "Who can sign?" prose ends before the signatory grid; we stop at the first
    # signatory/organisation card heading or the get-involved button text.
    who = grab("Who can sign", ["Signatories", "Get Involved", "Get involved"])
    segments["who_can_sign"] = who.strip("? ").strip()

    return segments


def flatten(label: str, segments: dict) -> list[str]:
    """Turn segments into a flat, labelled, line-oriented list for diffing."""
    lines: list[str] = []
    cats = segments["categories"]
    lines.append(f"[categories] {' | '.join(cats)}")
    for i, rec in enumerate(segments["recommendations"], start=1):
        lines.append(f"[rec {i:02d}] {rec}")
    lines.append(f"[cite_as] {segments['cite_as']}")
    lines.append(f"[contributors] {segments['contributors']}")
    lines.append(f"[who_can_sign] {segments['who_can_sign']}")
    return lines


def maybe_build() -> None:
    print("Running `hugo` to render the local site ...", file=sys.stderr)
    subprocess.run(["hugo", "--quiet"], cwd=REPO_ROOT, check=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--url", default=LIVE_URL, help="live declaration URL")
    ap.add_argument("--build", action="store_true", help="run `hugo` before checking")
    ap.add_argument("--local-only", action="store_true",
                    help="print local segments only; skip the live fetch")
    args = ap.parse_args()

    if args.build:
        maybe_build()

    if not LOCAL_HTML.exists():
        print(f"Local render not found: {LOCAL_HTML}", file=sys.stderr)
        print("Run `hugo` first, or pass --build.", file=sys.stderr)
        return 2

    local_extractor = TextExtractor()
    local_extractor.feed(LOCAL_HTML.read_text(encoding="utf-8"))
    local_segments = extract_segments(local_extractor.text())
    local_lines = flatten("local", local_segments)

    if args.local_only:
        print("\n".join(local_lines))
        return 0

    try:
        live_html = fetch_live(args.url)
    except Exception as exc:  # noqa: BLE001 - report and fail clearly
        print(f"Failed to fetch live site {args.url}: {exc}", file=sys.stderr)
        return 2

    live_extractor = TextExtractor()
    live_extractor.feed(live_html)
    live_segments = extract_segments(live_extractor.text())
    live_lines = flatten("live", live_segments)

    if local_lines == live_lines:
        print("MATCH: local /declaration/ text matches the live site.")
        print(f"  ({len(local_segments['recommendations'])} recommendations, "
              f"{len(local_segments['categories'])} categories compared)")
        return 0

    print("DIFFERENCE: local /declaration/ text does NOT match the live site.\n")
    diff = difflib.unified_diff(
        live_lines, local_lines,
        fromfile="live (adore.software)", tofile="local (public/declaration)",
        lineterm="",
    )
    print("\n".join(diff))
    return 1


if __name__ == "__main__":
    sys.exit(main())
