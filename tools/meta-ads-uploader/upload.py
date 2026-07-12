#!/usr/bin/env python3
"""Create a simple link ad from an existing Meta image hash. Dry-run by default."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from meta_graph import DEFAULT_GRAPH_VERSION, MetaApiError, MetaGraphClient

ROOT = Path(__file__).resolve().parents[2]


def build_plan(args: argparse.Namespace) -> dict:
    story = {"page_id": args.page_id, "link_data": {"image_hash": args.image_hash, "link": args.url, "message": args.primary_text, "name": args.headline, "call_to_action": {"type": args.cta, "value": {"link": args.url}}}}
    return {"creative": {"name": f"{args.name} creative", "object_story_spec": json.dumps(story)}, "ad": {"name": args.name, "adset_id": args.adset_id, "status": "PAUSED"}}


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    for flag in ("name", "adset-id", "page-id", "image-hash", "url", "primary-text", "headline"):
        p.add_argument(f"--{flag}", required=True)
    p.add_argument("--cta", default="SHOP_NOW")
    p.add_argument("--graph-version", default=DEFAULT_GRAPH_VERSION)
    p.add_argument("--execute", action="store_true", help="Actually call Meta. Resulting ad remains PAUSED.")
    p.add_argument("--confirm-paused-upload", action="store_true", help="Required together with --execute.")
    return p


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    plan = build_plan(args)
    if not args.execute:
        print(json.dumps({"mode": "dry-run", **plan}, indent=2))
        return 0
    if not args.confirm_paused_upload:
        print("Refusing write: --execute also requires --confirm-paused-upload.", file=sys.stderr)
        return 2
    try:
        client = MetaGraphClient.from_env(ROOT / ".env", args.graph_version)
        creative = client.form_post(f"{client.account_path}/adcreatives", plan["creative"])
        ad = client.form_post(f"{client.account_path}/ads", {**plan["ad"], "creative": json.dumps({"creative_id": creative["id"]})})
        print(json.dumps({"status": "created_paused", "creative_id": creative["id"], "ad_id": ad["id"]}, indent=2))
        return 0
    except (MetaApiError, KeyError) as error:
        print(f"Upload failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
