from __future__ import annotations

import re
from typing import Callable, Literal, TypedDict


class ClientAttribution(TypedDict, total=False):
    """Explicit public caller labels; omitted labels remain unknown to reporting."""

    surface: Literal["sdk", "rest", "mcp-http", "mcp-stdio"]
    install_channel: Literal["npx", "npm", "mcpb", "source"]
    ai_client: Literal["claude", "claude-desktop", "claude-code", "chatgpt", "codex", "cursor", "gemini", "other"]
    ai_model: str


class ResponseMetadata(TypedDict):
    request_id: str | None
    status: int


ResponseCallback = Callable[[ResponseMetadata], None]


def client_attribution_headers(attribution: ClientAttribution | None = None) -> dict[str, str]:
    labels = attribution or {}
    headers = {"x-mcp-client-surface": "sdk"}
    choices = {
        "surface": ("x-mcp-client-surface", {"sdk", "rest", "mcp-http", "mcp-stdio"}),
        "install_channel": ("x-mcp-install-channel", {"npx", "npm", "mcpb", "source"}),
        "ai_client": ("x-mcp-ai-client", {"claude", "claude-desktop", "claude-code", "chatgpt", "codex", "cursor", "gemini", "other"}),
    }
    for key, (header, accepted) in choices.items():
        value = labels.get(key)
        if isinstance(value, str) and value.lower() in accepted:
            headers[header] = value.lower()
    model = labels.get("ai_model")
    if isinstance(model, str) and re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9._:/-]{0,79}", model):
        headers["x-mcp-ai-model"] = model
    return headers


def notify_response(callback: ResponseCallback | None, metadata: ResponseMetadata) -> None:
    """Reporting observers cannot change an operation's received result."""
    if callback is None:
        return
    try:
        callback(metadata)
    except Exception:
        pass
