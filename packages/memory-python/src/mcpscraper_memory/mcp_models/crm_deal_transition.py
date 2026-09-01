from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmDealTransitionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    deal_id: str = Field(..., alias="dealId", description="Stable CRM deal or opportunity identifier.")
    pipeline_id: str = Field(..., alias="pipelineId", description="Exact CRM pipeline identifier selected from authorized tenant discovery.")
    target_stage_id: str = Field(..., alias="targetStageId", description="Governed destination stage identifier for this deal transition.")
    base_revision: int = Field(..., alias="baseRevision", description="Last revision read by the caller; supply it to reject an update if the record changed meanwhile.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.")
    fields: dict[str, Any] | None = Field(None, alias="fields", description="Ordered form-field definitions to render and validate for submissions.")


class CrmDealTransitionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    record: dict[str, Any] | None = Field(None, alias="record", description="")
    receipt: dict[str, Any] | None = Field(None, alias="receipt", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
