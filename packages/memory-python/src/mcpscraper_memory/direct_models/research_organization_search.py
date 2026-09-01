from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ResearchOrganizationSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    query: str | None = Field(None, alias="query", description="")
    topic: str | None = Field(None, alias="topic", description="")
    role: str | None = Field(None, alias="role", description="")
    cursor: str | None = Field(None, alias="cursor", description="")
    limit: int | None = Field(None, alias="limit", description="")


class ResearchOrganizationSearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    items: list[dict[str, Any]] | None = Field(None, alias="items", description="")
    page_info: dict[str, Any] | None = Field(None, alias="pageInfo", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
