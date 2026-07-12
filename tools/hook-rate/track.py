#!/usr/bin/env python3
"""Rank video ads using weighted hook and hold rates from Meta CSV exports."""

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


def find_column(fields, *aliases):
    lowered = {field.lower().strip(): field for field in fields or []}
    for alias in aliases:
        if alias.lower() in lowered:
            return lowered[alias.lower()]
    return None


def number(value):
    text = str(value or "").replace(",", "").replace("%", "").strip()
    try:
        return float(text) if text else 0.0
    except ValueError:
        return 0.0


def normalized_rate(value):
    value = number(value)
    return value / 100 if value > 1 else value


def aggregate(paths):
    ads = defaultdict(lambda: {"impressions": 0.0, "plays_3s": 0.0,
                               "hook_weighted": 0.0, "hold_weighted": 0.0,
                               "spend": 0.0, "purchases": 0.0})
    for path in paths:
        with Path(path).open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            fields = reader.fieldnames or []
            columns = {
                "ad": find_column(fields, "Ad name"),
                "impressions": find_column(fields, "Impressions"),
                "plays": find_column(fields, "3-second video plays", "Video plays at 3 seconds"),
                "hook": find_column(fields, "Hook Rate"),
                "hold": find_column(fields, "Hold Rate (50%)"),
                "spend": find_column(fields, "Amount spent", "Amount spent (USD)"),
                "purchases": find_column(fields, "Purchases", "Website purchases"),
            }
            missing = [key for key in ("ad", "impressions", "plays", "hook") if not columns[key]]
            if missing:
                raise ValueError(f"{path}: missing columns: {', '.join(missing)}")
            for row in reader:
                name = (row.get(columns["ad"]) or "").strip()
                if not name:
                    continue
                impressions = number(row.get(columns["impressions"]))
                plays = number(row.get(columns["plays"]))
                item = ads[name]
                item["impressions"] += impressions
                item["plays_3s"] += plays
                item["hook_weighted"] += normalized_rate(row.get(columns["hook"])) * impressions
                if columns["hold"]:
                    item["hold_weighted"] += normalized_rate(row.get(columns["hold"])) * plays
                item["spend"] += number(row.get(columns["spend"])) if columns["spend"] else 0
                item["purchases"] += number(row.get(columns["purchases"])) if columns["purchases"] else 0
    return ads


def rank(ads, min_impressions=500):
    output = []
    for name, item in ads.items():
        if item["impressions"] < min_impressions or item["plays_3s"] <= 0:
            continue
        output.append({
            "ad": name,
            "impressions": int(item["impressions"]),
            "plays_3s": int(item["plays_3s"]),
            "hook_rate": item["hook_weighted"] / item["impressions"],
            "hold_rate_50": item["hold_weighted"] / item["plays_3s"],
            "spend": item["spend"],
            "purchases": int(item["purchases"]),
        })
    return sorted(output, key=lambda row: row["hook_rate"], reverse=True)


def markdown(rows):
    lines = ["| Ad | Impressions | 3s plays | Hook rate | Hold rate (50%) | Spend | Purchases |",
             "|---|---:|---:|---:|---:|---:|---:|"]
    for row in rows:
        lines.append(f"| {row['ad']} | {row['impressions']:,} | {row['plays_3s']:,} | "
                     f"{row['hook_rate']:.1%} | {row['hold_rate_50']:.1%} | "
                     f"{row['spend']:.2f} | {row['purchases']} |")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", nargs="+", help="one or more Meta Ads CSV exports")
    parser.add_argument("--min-impressions", type=int, default=500)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        rows = rank(aggregate(args.csv), args.min_impressions)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(json.dumps(rows, indent=2) if args.json else markdown(rows))


if __name__ == "__main__":
    main()
