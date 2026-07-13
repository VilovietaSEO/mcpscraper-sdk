from __future__ import annotations

import itertools
import json
import time
from typing import Any

import requests

from ._mcp_generated_client import GeneratedMcpToolsClient


class McpToolError(RuntimeError):
    def __init__(
        self,
        message: str,
        *,
        http_status: int | None = None,
        rpc_code: int | None = None,
        data: Any = None,
        tool_error: Any = None,
    ) -> None:
        super().__init__(message)
        self.http_status = http_status
        self.rpc_code = rpc_code
        self.data = data
        self.tool_error = tool_error


class McpToolsClient(GeneratedMcpToolsClient):
    """Typed access to every tool exposed by https://mcpscraper.dev/mcp."""

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://mcpscraper.dev",
        session: requests.Session | None = None,
        list_retries: int = 2,
        retry_delay_s: float = 0.25,
    ) -> None:
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")
        self._session = session or requests.Session()
        self._rpc_id = itertools.count(1)
        self._list_retries = list_retries
        self._retry_delay_s = retry_delay_s
        super().__init__(self._call_tool)

    def _request(self, method: str, params: dict[str, Any] | None = None) -> Any:
        payload: dict[str, Any] = {
            "jsonrpc": "2.0",
            "id": next(self._rpc_id),
            "method": method,
        }
        if params is not None:
            payload["params"] = params
        attempts = self._list_retries + 1 if method == "tools/list" else 1
        response = None
        for attempt in range(attempts):
            response = self._session.post(
                f"{self._base_url}/mcp",
                headers={
                    "x-api-key": self._api_key,
                    "content-type": "application/json",
                    "accept": "application/json, text/event-stream",
                },
                json=payload,
            )
            transient_discovery_failure = method == "tools/list" and response.status_code in (502, 503, 504)
            if not transient_discovery_failure or attempt == attempts - 1:
                break
            time.sleep(self._retry_delay_s * (attempt + 1))
        assert response is not None
        if not response.ok:
            raise McpToolError(
                f'HTTP {response.status_code} calling MCP method "{method}"',
                http_status=response.status_code,
                data=response.text,
            )
        body = response.json()
        if body.get("error"):
            error = body["error"]
            raise McpToolError(
                error.get("message", f'MCP method "{method}" failed'),
                rpc_code=error.get("code"),
                data=error.get("data"),
            )
        if "result" not in body:
            raise McpToolError(f'MCP method "{method}" returned no result')
        return body["result"]

    def list_tools(self) -> list[dict[str, Any]]:
        result = self._request("tools/list")
        return result.get("tools", [])

    def describe_tool(self, name: str) -> dict[str, Any] | None:
        return next((tool for tool in self.list_tools() if tool.get("name") == name), None)

    def call_tool(self, name: str, args: dict[str, Any] | None = None) -> Any:
        return self._call_tool(name, args or {})

    @staticmethod
    def _parsed_tool_value(result: dict[str, Any]) -> Any:
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
        return parsed

    def call_tool_result(self, name: str, args: dict[str, Any] | None = None) -> dict[str, Any]:
        """Return the complete MCP tool result, preserving image/audio/resource content blocks."""
        result = self._request("tools/call", {"name": name, "arguments": args or {}})
        parsed = self._parsed_tool_value(result)
        if result.get("isError"):
            message = (
                parsed.get("message")
                if isinstance(parsed, dict) and "message" in parsed
                else parsed
                if isinstance(parsed, str)
                else f'Tool "{name}" failed'
            )
            raise McpToolError(str(message), tool_error=parsed)
        return result

    def _call_tool(self, name: str, arguments: dict[str, Any]) -> Any:
        result = self.call_tool_result(name, arguments)
        parsed = self._parsed_tool_value(result)
        return parsed
