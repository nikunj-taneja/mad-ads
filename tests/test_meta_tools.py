import argparse
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools" / "meta-ads-uploader"))

from meta_graph import MetaGraphClient, load_env
from upload import build_plan


class MetaToolTests(unittest.TestCase):
    def test_account_id_is_normalized(self):
        self.assertEqual(MetaGraphClient("secret", "act_123").account_path, "act_123")

    def test_process_environment_wins_over_dotenv(self):
        with tempfile.TemporaryDirectory() as directory:
            env_file = Path(directory) / ".env"
            env_file.write_text("META_ACCESS_TOKEN=file-token\n")
            with patch.dict(os.environ, {"META_ACCESS_TOKEN": "process-token"}, clear=False):
                self.assertEqual(load_env(env_file)["META_ACCESS_TOKEN"], "process-token")

    def test_upload_plan_is_always_paused(self):
        args = argparse.Namespace(name="Example", adset_id="1", page_id="2", image_hash="hash", url="https://example.com", primary_text="Text", headline="Headline", cta="SHOP_NOW")
        self.assertEqual(build_plan(args)["ad"]["status"], "PAUSED")


if __name__ == "__main__":
    unittest.main()
