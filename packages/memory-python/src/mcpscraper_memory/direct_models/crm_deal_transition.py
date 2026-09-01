from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmDealTransitionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    deal_id: str = Field(..., alias="dealId", description="")
    pipeline_id: str = Field(..., alias="pipelineId", description="")
    target_stage_id: str = Field(..., alias="targetStageId", description="")
    base_revision: int = Field(..., alias="baseRevision", description="")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="")
    fields: dict[str, Any] | None = Field(None, alias="fields", description="")


class CrmDealTransitionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    record: dict[str, Any] | None = Field(None, alias="record", description="")
    receipt: dict[str, Any] | None = Field(None, alias="receipt", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
