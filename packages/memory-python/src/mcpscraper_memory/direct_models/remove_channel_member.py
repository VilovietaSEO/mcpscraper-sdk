from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class RemoveChannelMemberInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    vault: str = Field(..., alias="vault", description="The vault (channel) to remove the member from. You must own it.")
    identity: str = Field(..., alias="identity", description="The member to remove.")


class RemoveChannelMemberOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth/scope/ownership error.")
    removed: bool | None = Field(None, alias="removed", description="True if a membership was found and removed; false if they were not a member.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
