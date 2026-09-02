from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmWorkSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    entity_id: str | None = Field(None, alias="entityId", description="Optional stable CRM person or organization entity ID associated with the work record.")
    entity_ids: list[str] | None = Field(None, alias="entityIds", description="Optional stable CRM entity IDs that must all be associated with the work record.")
    work_id: str | None = Field(None, alias="workId", description="Optional exact canonical CRM activity, task, or deal work ID.")
    query: str | None = Field(None, alias="query", description="Optional case-insensitive title search.")
    cursor: str | None = Field(None, alias="cursor", description="Opaque cursor returned by the previous crm-work-search page.")
    limit: int | None = Field(None, alias="limit", description="Maximum work records to return before cursor pagination.")
    object_kind: Literal['activity', 'task', 'deal'] = Field(..., alias="objectKind", description="Search exactly one canonical CRM work kind.")
    task_statuses: list[Literal['todo', 'in_progress', 'blocked', 'done', 'cancelled']] | None = Field(None, alias="taskStatuses", description="Task-only statuses to include.")
    due_before: str | None = Field(None, alias="dueBefore", description="Task-only inclusive upper due-time bound.")
    due_after: str | None = Field(None, alias="dueAfter", description="Task-only inclusive lower due-time bound.")
    due_unscheduled: bool | None = Field(None, alias="dueUnscheduled", description="Task-only filter for records without a due date.")
    task_owner_id: str | None = Field(None, alias="taskOwnerId", description="Task-only exact owner identifier.")
    deal_id: str | None = Field(None, alias="dealId", description="Task-only native CRM deal UUID.")
    pipeline_id: str | None = Field(None, alias="pipelineId", description="Deal-only native CRM pipeline UUID.")
    stage_ids: list[str] | None = Field(None, alias="stageIds", description="Deal-only native CRM stage UUIDs.")
    min_value: float | None = Field(None, alias="minValue", description="Deal-only inclusive minimum value.")
    max_value: float | None = Field(None, alias="maxValue", description="Deal-only inclusive maximum value.")


class CrmWorkSearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    items: list[dict[str, Any]] | None = Field(None, alias="items", description="")
    page_info: dict[str, Any] | None = Field(None, alias="pageInfo", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
