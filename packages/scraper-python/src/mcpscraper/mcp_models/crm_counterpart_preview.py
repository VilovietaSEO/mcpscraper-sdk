from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmCounterpartPreviewInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    research_entity_id: str = Field(..., alias="researchEntityId", description="Stable Research entity identifier used only for explicit counterpart planning.")
    crm_entity_id: str = Field(..., alias="crmEntityId", description="Stable CRM entity identifier; it is distinct from any Research record identifier.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.")
    ttl_minutes: int | None = Field(None, alias="ttlMinutes", description="Bounded preview lifetime in minutes before the plan expires.")
    mode: str | None = Field(None, alias="mode", description="Governed execution mode for this operation.")


class CrmCounterpartPreviewOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    plan: dict[str, Any] | None = Field(None, alias="plan", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
