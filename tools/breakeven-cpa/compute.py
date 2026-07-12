#!/usr/bin/env python3
"""Calculate contribution margin and breakeven CPA from explicit inputs."""

import argparse
import csv
import json
from pathlib import Path


def calculate(*, gross_revenue, tax, cogs, payment_fees, returns_allowance,
              shipping, packaging, orders):
    if orders <= 0:
        raise ValueError("orders must be greater than zero")
    net_revenue = gross_revenue - tax
    cm1 = net_revenue - cogs - payment_fees - returns_allowance
    cm2 = cm1 - shipping - packaging
    return {
        "orders": orders,
        "gross_revenue_per_order": gross_revenue / orders,
        "net_revenue_per_order": net_revenue / orders,
        "cm1_per_order": cm1 / orders,
        "breakeven_cpa": cm2 / orders,
    }


def from_summary(path):
    data = json.loads(Path(path).read_text())
    required = {"gross_revenue", "tax", "cogs", "payment_fees", "returns_allowance",
                "shipping", "packaging", "orders"}
    missing = sorted(required - data.keys())
    if missing:
        raise ValueError(f"missing fields: {', '.join(missing)}")
    return calculate(**{key: float(data[key]) for key in required})


def from_orders(path, defaults):
    totals = {key: 0.0 for key in (
        "gross_revenue", "tax", "cogs", "payment_fees", "returns_allowance",
        "shipping", "packaging")}
    count = 0
    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or "gross_revenue" not in reader.fieldnames:
            raise ValueError("orders CSV requires a gross_revenue column")
        for row_number, row in enumerate(reader, 2):
            if not any((value or "").strip() for value in row.values()):
                continue
            count += 1
            gross = float(row["gross_revenue"])
            totals["gross_revenue"] += gross
            totals["tax"] += value_or_default(row, "tax", gross * defaults["tax_rate"], row_number)
            totals["cogs"] += value_or_default(row, "cogs", gross * defaults["cogs_rate"], row_number)
            totals["payment_fees"] += value_or_default(row, "payment_fees", gross * defaults["payment_fee_rate"], row_number)
            totals["returns_allowance"] += value_or_default(row, "returns_allowance", gross * defaults["returns_rate"], row_number)
            totals["shipping"] += value_or_default(row, "shipping", defaults["shipping_per_order"], row_number)
            totals["packaging"] += value_or_default(row, "packaging", defaults["packaging_per_order"], row_number)
    return calculate(orders=count, **totals)


def value_or_default(row, key, default, row_number):
    raw = (row.get(key) or "").replace(",", "").strip()
    try:
        return float(raw) if raw else default
    except ValueError as exc:
        raise ValueError(f"row {row_number}: {key} is not numeric") from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--summary", help="JSON containing aggregate cost totals")
    source.add_argument("--orders", help="CSV containing one row per order")
    parser.add_argument("--defaults", help="JSON defaults for omitted order-level costs")
    parser.add_argument("--current-cpa", type=float)
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()
    try:
        if args.summary:
            result = from_summary(args.summary)
        else:
            defaults = {"tax_rate": 0, "cogs_rate": 0, "payment_fee_rate": 0,
                        "returns_rate": 0, "shipping_per_order": 0, "packaging_per_order": 0}
            if args.defaults:
                defaults.update(json.loads(Path(args.defaults).read_text()))
            result = from_orders(args.orders, defaults)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    if args.current_cpa is not None:
        result["headroom_per_order"] = result["breakeven_cpa"] - args.current_cpa
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"Orders: {int(result['orders'])}")
        print(f"Gross revenue/order: {result['gross_revenue_per_order']:.2f}")
        print(f"Net revenue/order: {result['net_revenue_per_order']:.2f}")
        print(f"CM1/order: {result['cm1_per_order']:.2f}")
        print(f"Breakeven CPA (CM2/order): {result['breakeven_cpa']:.2f}")
        if "headroom_per_order" in result:
            print(f"Headroom vs current CPA: {result['headroom_per_order']:.2f}")


if __name__ == "__main__":
    main()
