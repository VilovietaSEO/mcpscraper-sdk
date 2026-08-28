from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ListChannelMembersInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    vault: str = Field(..., alias="vault", description="The vault (channel) to list members of. You must own it.")


class ListChannelMembersOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth/scope/ownership error.")
    owner: str | None = Field(None, alias="owner", description="The channel owner.")
    can_manage: bool | None = Field(None, alias="canManage", description="True if the caller is the owner (and so can call remove-channel-member).")
    members: list[dict[str, Any]] | None = Field(None, alias="members", description="Present when ok is true. Always includes at least the owner.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
