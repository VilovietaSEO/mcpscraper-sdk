from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmImportApplyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    import_id: str = Field(..., alias="importId", description="Owner-scoped governed CRM import plan identifier returned by preview.")
    plan_handle: str = Field(..., alias="planHandle", description="Owner-scoped opaque preview handle returned with the plan.")
    digest: str = Field(..., alias="digest", description="Exact SHA-256 digest returned by the preview; any changed input invalidates it.")
    confirmation_token: str = Field(..., alias="confirmationToken", description="Explicit confirmation token bound to the exact governed preview plan.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.")


class CrmImportApplyOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    result: dict[str, Any] | None = Field(None, alias="result", description="")
    receipt: dict[str, Any] | None = Field(None, alias="receipt", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
