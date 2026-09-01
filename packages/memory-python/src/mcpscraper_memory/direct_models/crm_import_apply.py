from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmImportApplyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    import_id: str = Field(..., alias="importId", description="")
    plan_handle: str = Field(..., alias="planHandle", description="")
    digest: str = Field(..., alias="digest", description="")
    confirmation_token: str = Field(..., alias="confirmationToken", description="")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="")


class CrmImportApplyOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    result: dict[str, Any] | None = Field(None, alias="result", description="")
    receipt: dict[str, Any] | None = Field(None, alias="receipt", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
