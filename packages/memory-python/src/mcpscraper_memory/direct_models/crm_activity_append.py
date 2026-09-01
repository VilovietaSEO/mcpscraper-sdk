from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmActivityAppendInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="")
    entity_id: str | None = Field(None, alias="entityId", description="")
    person_entity_id: str | None = Field(None, alias="personEntityId", description="")
    entity_ids: list[str] | None = Field(None, alias="entityIds", description="")
    activity_type: Literal['call', 'meeting', 'email', 'message', 'form', 'form_submission', 'conversion', 'note', 'calendar_event'] | None = Field(None, alias="activityType", description="")
    kind: str | None = Field(None, alias="kind", description="")
    occurred_at: str = Field(..., alias="occurredAt", description="")
    title: str | None = Field(None, alias="title", description="")
    content: str | None = Field(None, alias="content", description="")
    submitted_fields: dict[str, Any] | None = Field(None, alias="submittedFields", description="")
    source: dict[str, Any] | None = Field(None, alias="source", description="")
    props: dict[str, Any] | None = Field(None, alias="props", description="")


class CrmActivityAppendOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    record: dict[str, Any] | None = Field(None, alias="record", description="")
    receipt: dict[str, Any] | None = Field(None, alias="receipt", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
