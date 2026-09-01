from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmDealUpsertInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    deal_id: str | None = Field(None, alias="dealId", description="")
    base_revision: int = Field(..., alias="baseRevision", description="")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="")
    entity_ids: list[str] = Field(..., alias="entityIds", description="")
    title: str = Field(..., alias="title", description="")
    content: str | None = Field(None, alias="content", description="")
    pipeline_id: str = Field(..., alias="pipelineId", description="")
    stage_id: str = Field(..., alias="stageId", description="")
    probability: float = Field(..., alias="probability", description="")
    party: str = Field(..., alias="party", description="")
    entered_at: str = Field(..., alias="enteredAt", description="")
    value: Any | None = Field(None, alias="value", description="")
    currency: Any | None = Field(None, alias="currency", description="")
    props: dict[str, Any] | None = Field(None, alias="props", description="")


class CrmDealUpsertOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    record: dict[str, Any] | None = Field(None, alias="record", description="")
    receipt: dict[str, Any] | None = Field(None, alias="receipt", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
