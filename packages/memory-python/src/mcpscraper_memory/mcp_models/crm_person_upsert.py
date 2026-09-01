from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmPersonUpsertInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    entity_id: str | None = Field(None, alias="entityId", description="Existing governed entity identifier for this relation or edit.")
    base_revision: int | None = Field(None, alias="baseRevision", description="Last revision read by the caller; supply it to reject an update if the record changed meanwhile.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.")
    display_name: str = Field(..., alias="displayName", description="Human-readable person or organization name; paths, filenames, Vault references, and email-only labels are rejected.")
    content: str | None = Field(None, alias="content", description="Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.")
    relationship_types: list[Literal['prospect', 'customer', 'former_customer', 'friend', 'coworker', 'collaborator', 'vendor', 'partner', 'advisor', 'media', 'community', 'other']] = Field(..., alias="relationshipTypes", description="One or more owner-declared relationship types; at least one is required for CRM creation.")
    relationship_status: Literal['active', 'inactive', 'archived', 'merged'] | None = Field(None, alias="relationshipStatus", description="Operational relationship status independent of optional commercial lifecycle.")
    commercial_lifecycle: Any | None = Field(None, alias="commercialLifecycle", description="Optional commercial lifecycle; friends, coworkers, and other non-commercial relationships may leave it null.")
    relationship_owner_id: Any | None = Field(None, alias="relationshipOwnerId", description="Optional owner identifier responsible for the CRM relationship.")
    contact: dict[str, Any] | None = Field(None, alias="contact", description="Purpose-authorized confirmed contact projection; candidate evidence is forbidden.")
    email: str | None = Field(None, alias="email", description="Bridge-compatible top-level email; normalized into contact provenance.")
    phone: str | None = Field(None, alias="phone", description="Bridge-compatible top-level phone; normalized into contact provenance.")
    organization_name: str | None = Field(None, alias="organizationName", description="Bridge-compatible organization label; it never creates or resolves an organization by inference.")
    source: dict[str, Any] | None = Field(None, alias="source", description="Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.")
    props: dict[str, Any] | None = Field(None, alias="props", description="Complete governed note properties required by the target vault contract.")
    lineage: dict[str, Any] | None = Field(None, alias="lineage", description="Field authority, sensitivity, source, observation time, and confidence recorded with this governed write.")


class CrmPersonUpsertOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    record: dict[str, Any] | None = Field(None, alias="record", description="")
    receipt: dict[str, Any] | None = Field(None, alias="receipt", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
