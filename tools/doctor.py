#!/usr/bin/env python3
"""Report whether the repository has enough inputs for its core workflows."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["templates/brand.md", "templates/products.md", "templates/offers.md", "templates/brand-voice.md", "templates/visual-identity.md", "variables/kpis.md"]

def filled(path: Path) -> bool:
    return path.exists() and "[NEEDS INPUT]" not in path.read_text(encoding="utf-8")

def main() -> int:
    print("Mad Ads readiness\n")
    missing = []
    for relative in REQUIRED:
        ok = filled(ROOT / relative)
        print(f"{'READY' if ok else 'INPUT'}  {relative}")
        if not ok:
            missing.append(relative)
    csvs = list((ROOT / "data").glob("*.csv"))
    print(f"{'READY' if csvs else 'OPTIONAL'}  Meta CSV in data/ ({len(csvs)} found)")
    print(f"{'FOUND' if (ROOT / '.env').exists() else 'OPTIONAL'}  .env for API integrations")
    print("\nCore onboarding is incomplete." if missing else "\nCore brand inputs are ready.")
    return 1 if missing else 0

if __name__ == "__main__":
    raise SystemExit(main())
