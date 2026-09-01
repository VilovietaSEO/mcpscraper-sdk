from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmImportPreviewInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="")
    ttl_minutes: int | None = Field(None, alias="ttlMinutes", description="")
    mapping: dict[str, Any] = Field(..., alias="mapping", description="")
    rows: list[dict[str, Any]] = Field(..., alias="rows", description="")


class CrmImportPreviewOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    plan: dict[str, Any] | None = Field(None, alias="plan", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
