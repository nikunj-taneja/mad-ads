#!/usr/bin/env python3
"""Estimate spoken duration from Markdown using a configurable words-per-minute rate."""
import argparse
import re
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("path", type=Path)
parser.add_argument("--wpm", type=int, default=145)
args = parser.parse_args()
text = args.path.read_text(encoding="utf-8")
spoken = "\n".join(line for line in text.splitlines() if not line.lstrip().startswith(("#", "- Visual:", "- Shot:")))
words = re.findall(r"\b[\w'’-]+\b", spoken)
seconds = round(len(words) / args.wpm * 60)
print(f"{len(words)} words, approximately {seconds}s at {args.wpm} wpm")
