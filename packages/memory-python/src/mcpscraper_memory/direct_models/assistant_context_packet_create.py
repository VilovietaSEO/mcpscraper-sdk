from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantContextPacketCreateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP request is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional caller session identifier.")
    purpose: Any = Field(..., alias="purpose", description="")
    task_ref: Any | None = Field(None, alias="taskRef", description="")
    conversation_ref: Any | None = Field(None, alias="conversationRef", description="")
    source_handles: list[dict[str, Any]] = Field(..., alias="sourceHandles", description="")
    attachment_handles: list[Any] | None = Field(None, alias="attachmentHandles", description="")
    summary: str = Field(..., alias="summary", description="")
    body: str = Field(..., alias="body", description="")
    expires_at: str = Field(..., alias="expiresAt", description="")
    sensitivity: Literal['standard', 'sensitive', 'restricted'] = Field(..., alias="sensitivity", description="")


class AssistantContextPacketCreateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
