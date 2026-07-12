#!/usr/bin/env python3
"""Inspect a Meta Ads CSV without third-party dependencies."""
import csv
import json
import sys
from pathlib import Path

ALIASES = {
    "ad": ["ad name", "ad_name"],
    "spend": ["amount spent (inr)", "amount spent (usd)", "amount spent", "spend"],
    "impressions": ["impressions"],
    "clicks": ["link clicks", "clicks (all)", "clicks"],
    "purchases": ["purchases", "website purchases"],
    "revenue": ["purchase conversion value", "website purchase conversion value"],
}

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: parse.py data/export.csv", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        count = sum(1 for _ in reader)
    lower = {header.strip().lower(): header for header in headers}
    mapping = {key: next((lower[a] for a in aliases if a in lower), None) for key, aliases in ALIASES.items()}
    print(json.dumps({"file": str(path), "rows": count, "columns": headers, "mapping": mapping}, indent=2))
    missing = [key for key in ("ad", "spend") if not mapping[key]]
    if missing:
        print(f"missing required mappings: {', '.join(missing)}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
