from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CreateChannelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    name: str = Field(..., alias="name", description="Channel name. Must match ^[A-Za-z0-9 _-]{1,48}$.")
    invite_members: list[dict[str, Any]] | None = Field(None, alias="inviteMembers", description="Members to invite at creation. Optional; you can also invite later with share-vault.")


class CreateChannelOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the channel was created; false on auth/scope/validation error.")
    channel: str | None = Field(None, alias="channel", description="The channel (vault) name. Present when ok is true.")
    created: bool | None = Field(None, alias="created", description="True if newly created; false if a vault with this name already existed for you (idempotent).")
    members: list[dict[str, Any]] | None = Field(None, alias="members", description="Per-member invite result. A member entry with ok:false did NOT block channel creation; invite them again later once approved.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
