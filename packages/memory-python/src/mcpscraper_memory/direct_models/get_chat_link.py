from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GetChatLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")


class GetChatLinkOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth error.")
    url: str | None = Field(None, alias="url", description="The chat link. Present only the first time a link is minted for this identity.")
    already_exists: bool | None = Field(None, alias="alreadyExists", description="True when a link already exists and was NOT re-shown. Use revoke-chat-link then call this again to get a fresh one.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
