from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class RevokeVaultAppLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Optional when the MCP session is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier.")


class RevokeVaultAppLinkOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the request succeeded.")
    revoked: bool | None = Field(None, alias="revoked", description="True when an active Vault App link was revoked.")
    error: str | None = Field(None, alias="error", description="Human-readable error when the request cannot be completed.")
