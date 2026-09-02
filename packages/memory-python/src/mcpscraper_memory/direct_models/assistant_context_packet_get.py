from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantContextPacketGetInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP request is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional caller session identifier.")
    packet_id: str | None = Field(None, alias="packetId", description="")
    share_ref: str | None = Field(None, alias="shareRef", description="")
    revision: int | None = Field(None, alias="revision", description="")


class AssistantContextPacketGetOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    packet: dict[str, Any] | None = Field(None, alias="packet", description="")
    code: Literal['auth_error', 'scope_error', 'invalid_request', 'not_found', 'revision_conflict', 'expired', 'data_integrity_error'] | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
