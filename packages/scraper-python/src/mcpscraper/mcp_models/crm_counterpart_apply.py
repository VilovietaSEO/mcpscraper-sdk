from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmCounterpartApplyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    plan_id: str = Field(..., alias="planId", description="Durable CRM provisioning-plan identifier returned by the planning operation.")
    plan_handle: str = Field(..., alias="planHandle", description="Owner-scoped opaque preview handle returned with the plan.")
    digest: str = Field(..., alias="digest", description="Exact SHA-256 digest returned by the preview; any changed input invalidates it.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.")


class CrmCounterpartApplyOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    link: dict[str, Any] | None = Field(None, alias="link", description="")
    receipt: dict[str, Any] | None = Field(None, alias="receipt", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
