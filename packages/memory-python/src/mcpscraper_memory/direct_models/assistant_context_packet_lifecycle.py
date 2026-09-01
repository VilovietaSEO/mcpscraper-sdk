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
    model_config = ConfigDict(populate_by_name=True, extra="allow")
