from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class LeadListEnrichStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="The jobId returned by lead_list_enrich. Poll until status is complete, partial, empty, failed, or cancelled.")


class LeadListEnrichStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="")
    status: Literal['queued', 'running', 'complete', 'partial', 'empty', 'failed', 'cancelled'] = Field(..., alias="status", description="")
    progress: dict[str, Any] = Field(..., alias="progress", description="")
    billing: dict[str, Any] = Field(..., alias="billing", description="")
    sample_rows: list[dict[str, Any]] = Field(..., alias="sampleRows", description="")
    ambiguous_rows: list[dict[str, Any]] | None = Field(None, alias="ambiguousRows", description="")
    artifacts: list[dict[str, Any]] = Field(..., alias="artifacts", description="")
    warnings: list[str] = Field(..., alias="warnings", description="")
    created_at: str | None = Field(None, alias="createdAt", description="")
    updated_at: str | None = Field(None, alias="updatedAt", description="")
    completed_at: Any | None = Field(None, alias="completedAt", description="")
    error_code: Any | None = Field(None, alias="errorCode", description="")
    error: Any | None = Field(None, alias="error", description="")
    retryable: Any | None = Field(None, alias="retryable", description="")
