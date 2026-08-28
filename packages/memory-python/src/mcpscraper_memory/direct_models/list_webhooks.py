from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ListWebhooksInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")


class ListWebhooksOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    webhooks: list[dict[str, Any]] | None = Field(None, alias="webhooks", description="")
    error: str | None = Field(None, alias="error", description="")
