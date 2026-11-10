from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmCounterpartApplyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    plan_id: str = Field(..., alias="planId", description="Exact owner-scoped counterpart plan identifier returned by crm-counterpart-preview; use its matching unexpired planHandle and digest.")
    plan_handle: str = Field(..., alias="planHandle", description="Owner-scoped opaque preview handle returned with the plan.")
    digest: str = Field(..., alias="digest", description="Exact SHA-256 digest returned by the preview; any changed input invalidates it.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.")


class CrmCounterpartApplyOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
