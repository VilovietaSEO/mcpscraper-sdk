from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmCounterpartApplyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    plan_id: str = Field(..., alias="planId", description="")
    plan_handle: str = Field(..., alias="planHandle", description="")
    digest: str = Field(..., alias="digest", description="")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="")


class CrmCounterpartApplyOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    link: dict[str, Any] | None = Field(None, alias="link", description="")
    receipt: dict[str, Any] | None = Field(None, alias="receipt", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
