from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class LeadListEnrichCancelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="The jobId returned by lead_list_enrich. Poll until status is complete, partial, empty, failed, or cancelled.")


class LeadListEnrichCancelOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str | None = Field(None, alias="jobId", description="")
    status: Literal['queued', 'running', 'complete', 'partial', 'empty', 'failed', 'cancelled'] | None = Field(None, alias="status", description="")
    progress: dict[str, Any] | None = Field(None, alias="progress", description="")
    billing: dict[str, Any] | None = Field(None, alias="billing", description="")
    sample_rows: list[dict[str, Any]] | None = Field(None, alias="sampleRows", description="")
    ambiguous_rows: list[dict[str, Any]] | None = Field(None, alias="ambiguousRows", description="")
    artifacts: list[dict[str, Any]] | None = Field(None, alias="artifacts", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
    created_at: str | None = Field(None, alias="createdAt", description="")
    updated_at: str | None = Field(None, alias="updatedAt", description="")
    completed_at: Any | None = Field(None, alias="completedAt", description="")
    error_code: Any | None = Field(None, alias="errorCode", description="")
    error: Any | None = Field(None, alias="error", description="")
    retryable: Any | None = Field(None, alias="retryable", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
