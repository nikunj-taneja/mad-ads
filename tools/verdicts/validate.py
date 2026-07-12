#!/usr/bin/env python3
"""Validate a structured media-buying verdict report."""

import argparse
import json
import re
from pathlib import Path

VERDICTS = {"PAUSE", "WAIT", "KEEP", "SCALE", "ITERATE", "RESTRUCTURE"}
ACTION_TAGS = {"pause", "redirect", "scale", "watch"}
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def validate(report):
    errors = []
    if not isinstance(report, dict):
        return ["top level must be an object"]
    for key in ("generated", "period", "take", "verdicts"):
        if key not in report:
            errors.append(f"missing required key '{key}'")
    if "generated" in report and not isinstance(report["generated"], str) or (
            isinstance(report.get("generated"), str) and not DATE.fullmatch(report["generated"])):
        errors.append("generated must be YYYY-MM-DD")
    period = report.get("period")
    if period is not None:
        if not isinstance(period, dict):
            errors.append("period must be an object")
        else:
            for key in ("since", "until"):
                if not isinstance(period.get(key), str) or not DATE.fullmatch(period[key]):
                    errors.append(f"period.{key} must be YYYY-MM-DD")
    if "take" in report and (not isinstance(report["take"], str) or not report["take"].strip()):
        errors.append("take must be a non-empty string")
    verdicts = report.get("verdicts")
    if verdicts is not None:
        if not isinstance(verdicts, list) or not verdicts:
            errors.append("verdicts must be a non-empty list")
        else:
            for index, item in enumerate(verdicts):
                where = f"verdicts[{index}]"
                if not isinstance(item, dict):
                    errors.append(f"{where} must be an object")
                    continue
                if not isinstance(item.get("ad"), str) or not item["ad"].strip():
                    errors.append(f"{where}.ad must be a non-empty string")
                if item.get("verdict") not in VERDICTS:
                    errors.append(f"{where}.verdict must be one of {sorted(VERDICTS)}")
                if not isinstance(item.get("reason"), str) or not item["reason"].strip():
                    errors.append(f"{where}.reason must be a non-empty string")
    for key in ("actions", "budget_plan", "data_flags"):
        if key in report and not isinstance(report[key], list):
            errors.append(f"{key} must be a list")
    for index, action in enumerate(report.get("actions", []) if isinstance(report.get("actions", []), list) else []):
        if not isinstance(action, dict) or not isinstance(action.get("text"), str) or not action["text"].strip():
            errors.append(f"actions[{index}] requires non-empty text")
        elif action.get("tag") is not None and action["tag"] not in ACTION_TAGS:
            errors.append(f"actions[{index}].tag must be one of {sorted(ACTION_TAGS)}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default="analysis/verdicts.json")
    args = parser.parse_args()
    try:
        report = json.loads(Path(args.path).read_text())
    except (OSError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    errors = validate(report)
    if errors:
        for error in errors:
            print(f"[error] {error}")
        raise SystemExit(1)
    print(f"[ok] {args.path}: {len(report['verdicts'])} verdicts")


if __name__ == "__main__":
    main()
