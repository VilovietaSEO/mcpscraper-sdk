from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ResearchPersonGetInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    entity_id: str = Field(..., alias="entityId", description="")


class ResearchPersonGetOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    record: dict[str, Any] | None = Field(None, alias="record", description="")
    aliases: list[str] | None = Field(None, alias="aliases", description="")
    associations: list[dict[str, Any]] | None = Field(None, alias="associations", description="")
    counterpart_entity_id: Any | None = Field(None, alias="counterpartEntityId", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
