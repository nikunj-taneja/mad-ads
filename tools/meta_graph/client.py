"""Safe shared HTTP plumbing for Meta tools. Tokens are never logged."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

DEFAULT_GRAPH_VERSION = "v23.0"
_SAFE_ERROR_KEYS = ("message", "type", "code", "error_subcode", "error_user_title", "error_user_msg", "fbtrace_id")


class MetaApiError(RuntimeError):
    pass


def load_env(path: Path) -> dict[str, str]:
    values = dict(os.environ)
    if path.exists():
        for raw in path.read_text().splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values.setdefault(key.strip(), value.strip().strip('"').strip("'"))
    return values


class MetaGraphClient:
    def __init__(self, token: str, account_id: str, graph_version: str = DEFAULT_GRAPH_VERSION) -> None:
        if not token or not account_id:
            raise MetaApiError("Both META_ACCESS_TOKEN and META_AD_ACCOUNT_ID are required.")
        self.token = token
        self.account_id = account_id.removeprefix("act_")
        self.graph_version = graph_version

    @classmethod
    def from_env(cls, env_path: Path, graph_version: str = DEFAULT_GRAPH_VERSION) -> "MetaGraphClient":
        env = load_env(env_path)
        return cls(env.get("META_ACCESS_TOKEN", ""), env.get("META_AD_ACCOUNT_ID", ""), graph_version)

    @property
    def base(self) -> str:
        return f"https://graph.facebook.com/{self.graph_version}"

    @property
    def account_path(self) -> str:
        return f"act_{self.account_id}"

    @staticmethod
    def _call(request: urllib.request.Request, timeout: int = 45) -> dict:
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode())
        except urllib.error.HTTPError as error:
            body = error.read().decode(errors="replace")
            try:
                detail = json.loads(body).get("error", {})
                safe = {key: detail[key] for key in _SAFE_ERROR_KEYS if key in detail}
                raise MetaApiError(json.dumps(safe)) from error
            except json.JSONDecodeError:
                raise MetaApiError(f"Meta API returned HTTP {error.code}.") from error
        except urllib.error.URLError as error:
            raise MetaApiError(f"Could not reach Meta Graph API: {error.reason}") from error

    def get(self, path: str, params: dict[str, object] | None = None) -> dict:
        query = {**(params or {}), "access_token": self.token}
        url = f"{self.base}/{path}?{urllib.parse.urlencode(query)}"
        return self._call(urllib.request.Request(url))

    def get_all(self, path: str, params: dict[str, object] | None = None) -> list[dict]:
        page = self.get(path, params)
        results: list[dict] = []
        while True:
            results.extend(page.get("data", []))
            next_url = (page.get("paging") or {}).get("next")
            if not next_url:
                return results
            page = self._call(urllib.request.Request(next_url))

    def form_post(self, path: str, fields: dict[str, object]) -> dict:
        body = urllib.parse.urlencode({"access_token": self.token, **fields}).encode()
        return self._call(urllib.request.Request(f"{self.base}/{path}", data=body, method="POST"), timeout=90)
