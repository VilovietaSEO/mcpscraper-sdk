from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GmailImportToMemoryInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    idempotency_key: str = Field(..., alias="idempotencyKey", description="Stable retry key bound to the immutable import plan; reuse resumes and conflicting input fails before a write.")
    import_plan_id: str = Field(..., alias="importPlanId", description="Reviewed, unexpired importPlanId returned by gmail_prepare_memory_import.")


class GmailImportToMemoryOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    ingest: dict[str, Any] | None = Field(None, alias="ingest", description="")
    error: Any = Field(..., alias="error", description="")
