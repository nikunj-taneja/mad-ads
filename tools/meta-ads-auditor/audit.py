#!/usr/bin/env python3
"""Validate Meta credentials and optionally list campaigns. GET requests only."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from meta_graph import DEFAULT_GRAPH_VERSION, MetaApiError, MetaGraphClient

ROOT = Path(__file__).resolve().parents[2]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list-campaigns", action="store_true")
    parser.add_argument("--graph-version", default=DEFAULT_GRAPH_VERSION)
    args = parser.parse_args(argv)
    try:
        client = MetaGraphClient.from_env(ROOT / ".env", args.graph_version)
        account = client.get(client.account_path, {"fields": "id,name,account_status,currency,timezone_name"})
        output = {"credential_check": "ok", "account": account}
        if args.list_campaigns:
            output["campaigns"] = client.get_all(f"{client.account_path}/campaigns", {"fields": "id,name,status,effective_status", "limit": 100})
        print(json.dumps(output, indent=2))
        return 0
    except MetaApiError as error:
        print(f"Meta check failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
