from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantContextPacketShareAcceptInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP request is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional caller session identifier.")
    share_ref: str = Field(..., alias="shareRef", description="")


class AssistantContextPacketShareAcceptOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
