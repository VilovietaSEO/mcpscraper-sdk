from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmActivityAppendInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.")
    entity_id: str | None = Field(None, alias="entityId", description="Optional stable ID for this new activity work record, not a CRM person or organization ID.")
    person_entity_id: str | None = Field(None, alias="personEntityId", description="CRM Person entity ID to associate with this activity.")
    entity_ids: list[str] | None = Field(None, alias="entityIds", description="CRM person or organization entity IDs associated with this activity; at least one association is required.")
    activity_type: Literal['call', 'meeting', 'email', 'message', 'form', 'form_submission', 'conversion', 'note', 'calendar_event'] | None = Field(None, alias="activityType", description="Canonical CRM activity family recorded on the associated CRM relationship.")
    kind: str | None = Field(None, alias="kind", description="Governed type discriminator for this rule, score, event, or record.")
    occurred_at: str = Field(..., alias="occurredAt", description="ISO 8601 timestamp when the source event actually occurred.")
    title: str | None = Field(None, alias="title", description="Human-readable title for the proposed record or authored content.")
    content: str | None = Field(None, alias="content", description="Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.")
    submitted_fields: dict[str, Any] | None = Field(None, alias="submittedFields", description="Bounded submitted form fields retained only on the canonical CRM Communication.")
    source: dict[str, Any] | None = Field(None, alias="source", description="Optional source provenance stored with the CRM activity; this is not a record filter.")
    props: dict[str, Any] | None = Field(None, alias="props", description="Complete governed note properties required by the target vault contract.")


class CrmActivityAppendOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
