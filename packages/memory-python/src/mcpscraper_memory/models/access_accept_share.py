from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AccessAcceptShareInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    share_id: str = Field(..., alias="shareId", description="The shareId from note-inbox to accept.")


class AccessAcceptShareOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth/scope/lookup error.")
    share_id: str | None = Field(None, alias="shareId", description="The accepted share.")
    owner: str | None = Field(None, alias="owner", description="Identity who shared the note.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
