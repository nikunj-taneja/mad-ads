import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


breakeven = load("breakeven", "breakeven-cpa/compute.py")
hooks = load("hooks", "hook-rate/track.py")
verdicts = load("verdicts", "verdicts/validate.py")


class AnalysisToolTests(unittest.TestCase):
    def test_breakeven_calculation(self):
        result = breakeven.calculate(gross_revenue=1000, tax=100, cogs=250,
                                     payment_fees=30, returns_allowance=20,
                                     shipping=50, packaging=10, orders=2)
        self.assertEqual(result["breakeven_cpa"], 270)

    def test_hook_rate_weights_rows(self):
        content = ("Ad name,Impressions,3-second video plays,Hook Rate,Hold Rate (50%)\n"
                   "Video A,100,50,20%,40%\nVideo A,300,100,40%,20%\n")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "meta.csv"
            path.write_text(content)
            rows = hooks.rank(hooks.aggregate([path]), min_impressions=0)
        self.assertAlmostEqual(rows[0]["hook_rate"], 0.35)
        self.assertAlmostEqual(rows[0]["hold_rate_50"], 0.2666667, places=6)

    def test_verdict_contract(self):
        report = {"generated": "2026-01-02", "period": {"since": "2026-01-01", "until": "2026-01-02"},
                  "take": "Performance is stable.", "verdicts": [
                      {"ad": "example-video-v1", "verdict": "KEEP", "reason": "Enough signal."}]}
        self.assertEqual(verdicts.validate(report), [])
        report["verdicts"][0]["verdict"] = "GUESS"
        self.assertTrue(verdicts.validate(report))


if __name__ == "__main__":
    unittest.main()
