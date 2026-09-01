from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmCounterpartPreviewInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    research_entity_id: str = Field(..., alias="researchEntityId", description="")
    crm_entity_id: str = Field(..., alias="crmEntityId", description="")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="")
    ttl_minutes: int | None = Field(None, alias="ttlMinutes", description="")
    mode: str | None = Field(None, alias="mode", description="")


class CrmCounterpartPreviewOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    plan: dict[str, Any] | None = Field(None, alias="plan", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
