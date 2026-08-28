from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AccessUnlinkShareInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    share_id: str = Field(..., alias="shareId", description="The shareId to unlink from your \"Shared with me\" notes.")


class AccessUnlinkShareOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth/scope/lookup error.")
    share_id: str | None = Field(None, alias="shareId", description="The unlinked share.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
