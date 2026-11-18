from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmFormStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    form_id: str | None = Field(None, alias="formId", description="Connection ID from crm-form-create; omit to list connections.")
    limit: int | None = Field(None, alias="limit", description="")
    cursor: str | None = Field(None, alias="cursor", description="")


class CrmFormStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
    result: dict[str, Any] | None = Field(None, alias="result", description="")
