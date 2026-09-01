from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class RevokeWebhookToolInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    id: str = Field(..., alias="id", description="Webhook id, from list-webhooks.")


class RevokeWebhookToolOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    revoked: bool | None = Field(None, alias="revoked", description="")
    error: str | None = Field(None, alias="error", description="")
