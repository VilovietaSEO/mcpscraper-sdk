import itertools
import json
from typing import Any

import requests

from .errors import MemoryApiError
from ._generated_client import (
    AccessNamespace,
    CaptureNamespace,
    ChannelsNamespace,
    FactsNamespace,
    GraphNamespace,
    LibraryNamespace,
    MemoryNamespace,
    RecallNamespace,
    ScheduleNamespace,
    StorageNamespace,
    TablesNamespace,
    TagsNamespace,
    VaultsNamespace,
    VideoNamespace,
    WebhooksNamespace,
)

DEFAULT_BASE_URL = "https://memory.mcpscraper.dev"


class MemoryClient:
    def __init__(
        self,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        session: requests.Session | None = None,
    ) -> None:
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")
        self._session = session or requests.Session()
        self._rpc_id = itertools.count(1)

        self.access = AccessNamespace(self._call_tool)
        self.capture = CaptureNamespace(self._call_tool)
        self.channels = ChannelsNamespace(self._call_tool)
        self.facts = FactsNamespace(self._call_tool)
        self.graph = GraphNamespace(self._call_tool)
        self.library = LibraryNamespace(self._call_tool)
        self.memory = MemoryNamespace(self._call_tool)
        self.recall = RecallNamespace(self._call_tool)
        self.schedule = ScheduleNamespace(self._call_tool)
        self.storage = StorageNamespace(self._call_tool)
        self.tables = TablesNamespace(self._call_tool)
        self.tags = TagsNamespace(self._call_tool)
        self.vaults = VaultsNamespace(self._call_tool)
        self.video = VideoNamespace(self._call_tool)
        self.webhooks = WebhooksNamespace(self._call_tool)

    def _call_tool(self, name: str, arguments: dict[str, Any]) -> Any:
        response = self._session.post(
            f"{self._base_url}/mcp",
            headers={
                "content-type": "application/json",
                "accept": "application/json, text/event-stream",
                "authorization": f"Bearer {self._api_key}",
            },
            json={
                "jsonrpc": "2.0",
                "id": next(self._rpc_id),
                "method": "tools/call",
                "params": {"name": name, "arguments": arguments},
            },
        )

        if not response.ok:
            raise MemoryApiError(
                f'HTTP {response.status_code} calling tool "{name}"',
                http_status=response.status_code,
                data=response.text,
            )

        payload = response.json()

        if payload.get("error"):
            error = payload["error"]
            raise MemoryApiError(
                error.get("message", f'tool "{name}" failed'),
                rpc_code=error.get("code"),
                data=error.get("data"),
            )

        result = payload.get("result") or {}
        text_block = next(
            (block.get("text") for block in result.get("content", []) if block.get("type") == "text"),
            None,
        )

        parsed: Any = text_block
        if isinstance(text_block, str):
            try:
                parsed = json.loads(text_block)
            except ValueError:
                parsed = text_block
        if "structuredContent" in result:
            parsed = result["structuredContent"]

        if result.get("isError"):
            message = (
                parsed.get("message")
                if isinstance(parsed, dict) and "message" in parsed
                else parsed
                if isinstance(parsed, str)
                else f'Tool "{name}" failed'
            )
            raise MemoryApiError(str(message), tool_error=parsed)

        return parsed
