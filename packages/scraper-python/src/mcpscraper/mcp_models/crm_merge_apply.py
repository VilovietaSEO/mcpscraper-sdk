from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmMergeApplyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    merge_id: str = Field(..., alias="mergeId", description="Owner-scoped merge plan identifier returned by merge preview.")
    plan_handle: str = Field(..., alias="planHandle", description="Owner-scoped opaque preview handle returned with the plan.")
    digest: str = Field(..., alias="digest", description="Exact SHA-256 digest returned by the preview; any changed input invalidates it.")
    owner_confirmation: str = Field(..., alias="ownerConfirmation", description="Explicit owner confirmation bound to the exact non-expired merge plan.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.")


class CrmMergeApplyOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    result: dict[str, Any] | None = Field(None, alias="result", description="")
    receipt: dict[str, Any] | None = Field(None, alias="receipt", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
