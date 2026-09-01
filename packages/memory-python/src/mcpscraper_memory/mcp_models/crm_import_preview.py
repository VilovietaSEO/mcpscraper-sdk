from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmImportPreviewInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.")
    ttl_minutes: int | None = Field(None, alias="ttlMinutes", description="Bounded preview lifetime in minutes before the plan expires.")
    mapping: dict[str, Any] = Field(..., alias="mapping", description="CSV-column mapping used to identify and protect supported CRM fields.")
    rows: list[dict[str, Any]] = Field(..., alias="rows", description="Bounded normalized import rows; every row must target crm_person or crm_organization.")


class CrmImportPreviewOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    plan: dict[str, Any] | None = Field(None, alias="plan", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
