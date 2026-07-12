#!/usr/bin/env python3
"""Scan text files for common secret shapes and local privacy patterns."""
import re
import sys
from pathlib import Path

SKIP = {".git", ".venv", "data", "generated-media", "incoming-creatives"}
PATTERNS = [
    ("private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("likely secret assignment", re.compile(r"(?i)(token|secret|password|api[_-]?key)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}")),
    ("Meta token", re.compile(r"EAA[A-Za-z0-9]{20,}")),
]

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
custom = root / ".privacy-patterns"
if custom.exists():
    for line in custom.read_text(encoding="utf-8").splitlines():
        if line.strip() and not line.lstrip().startswith("#"):
            PATTERNS.append(("custom identifier", re.compile(line, re.I)))

hits = []
for path in root.rglob("*"):
    if not path.is_file() or any(part in SKIP for part in path.parts):
        continue
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (UnicodeDecodeError, OSError):
        continue
    for number, line in enumerate(lines, 1):
        for label, pattern in PATTERNS:
            if pattern.search(line):
                hits.append(f"{path}:{number}: {label}")
for hit in hits:
    print(hit)
raise SystemExit(1 if hits else 0)
