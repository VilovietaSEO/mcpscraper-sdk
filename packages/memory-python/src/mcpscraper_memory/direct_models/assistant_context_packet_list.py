from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantContextPacketListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP request is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional caller session identifier.")
    task_ref: str | None = Field(None, alias="taskRef", description="")
    conversation_ref: str | None = Field(None, alias="conversationRef", description="")
    limit: int | None = Field(None, alias="limit", description="")
    before_created_at: str | None = Field(None, alias="beforeCreatedAt", description="")


class AssistantContextPacketListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
