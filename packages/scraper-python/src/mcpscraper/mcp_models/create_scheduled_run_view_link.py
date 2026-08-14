from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CreateScheduledRunViewLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    run_id: str = Field(..., alias="runId", description="Opaque scheduled-run identifier returned by a scheduled-results tool.")
    artifact_id: str = Field(..., alias="artifactId", description="Opaque artifact identifier returned by the creating or listing tool.")
    expires_in_days: int | None = Field(None, alias="expiresInDays", description="Requested view-link lifetime in days; the server enforces its maximum.")


class CreateScheduledRunViewLinkOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    share_id: str | None = Field(None, alias="shareId", description="")
    run_id: str | None = Field(None, alias="runId", description="Opaque scheduled-run identifier returned by a scheduled-results tool.")
    artifact_id: str | None = Field(None, alias="artifactId", description="")
    url: str | None = Field(None, alias="url", description="")
    expires_at: str | None = Field(None, alias="expiresAt", description="")
    created_at: str | None = Field(None, alias="createdAt", description="")
    error: str | None = Field(None, alias="error", description="")
    error_code: Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'view_link_unavailable', 'internal_error'] | None = Field(None, alias="errorCode", description="")
    request_id: str | None = Field(None, alias="requestId", description="")
