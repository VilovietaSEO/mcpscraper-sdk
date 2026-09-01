from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmDuplicateSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    domain: Literal['crm_person', 'crm_organization'] = Field(..., alias="domain", description="")
    entity_id: str | None = Field(None, alias="entityId", description="")
    display_name: str | None = Field(None, alias="displayName", description="")
    email: str | None = Field(None, alias="email", description="")
    phone: str | None = Field(None, alias="phone", description="")
    limit: int | None = Field(None, alias="limit", description="")


class CrmDuplicateSearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    candidates: list[dict[str, Any]] | None = Field(None, alias="candidates", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
