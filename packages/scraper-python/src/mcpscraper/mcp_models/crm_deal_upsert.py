from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmDealUpsertInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    deal_id: str | None = Field(None, alias="dealId", description="Stable CRM deal or opportunity identifier.")
    base_revision: int = Field(..., alias="baseRevision", description="Last revision read by the caller; supply it to reject an update if the record changed meanwhile.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.")
    entity_ids: list[str] = Field(..., alias="entityIds", description="Stable CRM entity identifiers associated with this CRM activity, task, or deal.")
    title: str = Field(..., alias="title", description="Human-readable title for the proposed record or authored content.")
    content: str | None = Field(None, alias="content", description="Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.")
    pipeline_id: str = Field(..., alias="pipelineId", description="Exact CRM pipeline identifier selected from authorized tenant discovery.")
    stage_id: str = Field(..., alias="stageId", description="Exact CRM stage identifier required for the conversion rule to match.")
    probability: float = Field(..., alias="probability", description="Deal probability from zero through one hundred for the selected governed stage.")
    party: str = Field(..., alias="party", description="Stable CRM person or organization party associated with the deal.")
    entered_at: str = Field(..., alias="enteredAt", description="ISO 8601 time when the deal entered the selected pipeline stage.")
    value: Any | None = Field(None, alias="value", description="Typed bounded comparison or field value for this declarative rule.")
    currency: Any | None = Field(None, alias="currency", description="Three-letter ISO currency code for the event value.")
    props: dict[str, Any] | None = Field(None, alias="props", description="Complete governed note properties required by the target vault contract.")


class CrmDealUpsertOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    record: dict[str, Any] | None = Field(None, alias="record", description="")
    receipt: dict[str, Any] | None = Field(None, alias="receipt", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
