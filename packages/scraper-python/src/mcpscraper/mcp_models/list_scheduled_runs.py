from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ListScheduledRunsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    view: Literal['inbox', 'all', 'archived'] | None = Field(None, alias="view", description="Scheduled-results view to return, such as inbox, all unarchived, or archived.")
    status: Literal['running', 'succeeded', 'no_output', 'partial', 'billing_stopped', 'failed'] | None = Field(None, alias="status", description="Optional scheduled-run execution status filter.")
    schedule_id: str | None = Field(None, alias="scheduleId", description="Optional scheduled-action identifier used to restrict results to one schedule.")
    template_id: str | None = Field(None, alias="templateId", description="Opaque saved-template identifier returned by an artifact-template tool.")
    from_: str | None = Field(None, alias="from", description="Inclusive ISO 8601 lower bound for scheduled-run creation time.")
    to: str | None = Field(None, alias="to", description="Exclusive ISO 8601 upper bound for scheduled-run creation time.")
    query: str | None = Field(None, alias="query", description="Text matched against scheduled-run titles and searchable metadata.")
    cursor: str | None = Field(None, alias="cursor", description="Opaque continuation cursor returned by the previous page; omit for the first page.")
    limit: int | None = Field(None, alias="limit", description="Maximum rows or records to return on this page; use the returned cursor for more.")


class ListScheduledRunsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    items: list[dict[str, Any]] | None = Field(None, alias="items", description="")
    next_cursor: Any | None = Field(None, alias="nextCursor", description="")
    error: str | None = Field(None, alias="error", description="")
    error_code: Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'view_link_unavailable', 'internal_error'] | None = Field(None, alias="errorCode", description="")
    request_id: str | None = Field(None, alias="requestId", description="")
