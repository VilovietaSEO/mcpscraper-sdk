from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class SetAgentIdentityInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    is_agent: bool = Field(..., alias="isAgent", description="true to mark this identity as an AI agent; false to unmark it.")


class SetAgentIdentityOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth error.")
    is_agent: bool | None = Field(None, alias="isAgent", description="The flag now in effect.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
