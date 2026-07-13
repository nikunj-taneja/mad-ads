import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SkillDepthTests(unittest.TestCase):
    def assert_contains(self, relative, terms):
        text = (ROOT / relative).read_text(encoding="utf-8").lower()
        for term in terms:
            self.assertIn(term.lower(), text, f"{relative} lost required framework: {term}")

    def test_sugarman_framework_contract(self):
        self.assert_contains("skills/sugarman/SKILL.md", [
            "Schwartz strategic pre-flight", "Life-Force 8", "fifteen", "slippery slide",
            "38", "Intensification", "Gradualization", "Mechanization", "Camouflage",
            "Mental movie", "Four-walls", "31", "spoken register", "final diagnostic",
        ])

    def test_strategy_framework_contract(self):
        self.assert_contains("skills/creative-strategist/SKILL.md", [
            "winner", "coverage", "awareness", "sophistication", "Life-Force 8",
            "means-end", "Iterate", "Test New", "Refresh", "angle",
        ])

    def test_media_framework_contract(self):
        self.assert_contains("skills/media-buyer/SKILL.md", [
            "lifetime", "PAUSE", "WAIT", "KEEP", "SCALE", "ITERATE", "RESTRUCTURE",
            "Hook Rate", "Hold Rate", "blended ROAS", "learning", "utilisation",
        ])


if __name__ == "__main__":
    unittest.main()
