from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CreateWebhookInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    vault: str | None = Field(None, alias="vault", description="Vault this webhook writes into. Optional; defaults to \"Issues\".")
    label: str | None = Field(None, alias="label", description="Optional human-readable label to help you remember what this webhook is for, e.g. \"Website contact form\".")


class CreateWebhookOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    id: str | None = Field(None, alias="id", description="Webhook id, for listing/revoking later.")
    url: str | None = Field(None, alias="url", description="The full webhook URL — POST here to write a note.")
    vault: str | None = Field(None, alias="vault", description="")
    error: str | None = Field(None, alias="error", description="")
