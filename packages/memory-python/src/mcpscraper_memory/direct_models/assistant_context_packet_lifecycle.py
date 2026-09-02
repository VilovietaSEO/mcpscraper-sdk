from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantContextPacketLifecycleInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP request is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional caller session identifier.")
    packet_id: str = Field(..., alias="packetId", description="")
    expected_revision: int = Field(..., alias="expectedRevision", description="")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="")
    action: Any = Field(..., alias="action", description="")


class AssistantContextPacketLifecycleOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    packet: dict[str, Any] | None = Field(None, alias="packet", description="")
    share: dict[str, Any] | None = Field(None, alias="share", description="")
    code: Literal['auth_error', 'scope_error', 'invalid_request', 'not_found', 'revision_conflict', 'expired', 'data_integrity_error'] | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
