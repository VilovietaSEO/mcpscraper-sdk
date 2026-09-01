from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmTaskUpsertInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    task_id: str | None = Field(None, alias="taskId", description="")
    entity_id: str | None = Field(None, alias="entityId", description="")
    base_revision: int | None = Field(None, alias="baseRevision", description="")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="")
    person_entity_id: str | None = Field(None, alias="personEntityId", description="")
    communication_entity_id: str | None = Field(None, alias="communicationEntityId", description="")
    entity_ids: list[str] | None = Field(None, alias="entityIds", description="")
    title: str = Field(..., alias="title", description="")
    content: str | None = Field(None, alias="content", description="")
    status: Literal['todo', 'in_progress', 'blocked', 'done', 'cancelled'] | None = Field(None, alias="status", description="")
    due_at: Any | None = Field(None, alias="dueAt", description="")
    source: dict[str, Any] | None = Field(None, alias="source", description="")
    props: dict[str, Any] | None = Field(None, alias="props", description="")


class CrmTaskUpsertOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    record: dict[str, Any] | None = Field(None, alias="record", description="")
    receipt: dict[str, Any] | None = Field(None, alias="receipt", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
