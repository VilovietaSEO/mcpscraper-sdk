from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmTaskUpsertInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    task_id: str | None = Field(None, alias="taskId", description="Task workId returned by crm-work-search; omit to create a new task.")
    entity_id: str | None = Field(None, alias="entityId", description="Compatibility alias for taskId, not a CRM relationship ID; taskId takes precedence.")
    base_revision: int | None = Field(None, alias="baseRevision", description="Use 0 to create a Task; for an edit, supply taskId or entityId and the current positive revision read from crm-work-get.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.")
    person_entity_id: str | None = Field(None, alias="personEntityId", description="Stable CRM Person entity identifier; Research identifiers are rejected.")
    communication_entity_id: str | None = Field(None, alias="communicationEntityId", description="Stable CRM Communication entity identifier returned by the activity append operation.")
    entity_ids: list[str] | None = Field(None, alias="entityIds", description="Stable CRM entity identifiers associated with this CRM activity, task, or deal.")
    title: str = Field(..., alias="title", description="Human-readable title for the proposed record or authored content.")
    content: str | None = Field(None, alias="content", description="Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.")
    status: Literal['todo', 'in_progress', 'blocked', 'done', 'cancelled'] | None = Field(None, alias="status", description="Lifecycle status used to filter or update the selected records.")
    due_at: Any | None = Field(None, alias="dueAt", description="Optional ISO 8601 due time for the CRM Task.")
    source: dict[str, Any] | None = Field(None, alias="source", description="Optional source provenance stored with the Task; this is not a record filter.")
    props: dict[str, Any] | None = Field(None, alias="props", description="Complete governed note properties required by the target vault contract.")


class CrmTaskUpsertOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
