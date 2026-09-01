from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmMergePreviewInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    master_entity_id: str = Field(..., alias="masterEntityId", description="Stable CRM record selected as the surviving master in a merge preview.")
    duplicate_entity_id: str = Field(..., alias="duplicateEntityId", description="Stable CRM record selected as the duplicate candidate in a merge preview.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.")
    ttl_minutes: int | None = Field(None, alias="ttlMinutes", description="Bounded preview lifetime in minutes before the plan expires.")


class CrmMergePreviewOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    plan: dict[str, Any] | None = Field(None, alias="plan", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
