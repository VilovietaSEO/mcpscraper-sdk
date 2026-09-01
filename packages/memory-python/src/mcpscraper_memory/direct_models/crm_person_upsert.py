from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmPersonUpsertInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    entity_id: str | None = Field(None, alias="entityId", description="")
    base_revision: int | None = Field(None, alias="baseRevision", description="")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="")
    display_name: str = Field(..., alias="displayName", description="")
    content: str | None = Field(None, alias="content", description="")
    relationship_types: list[Literal['prospect', 'customer', 'former_customer', 'friend', 'coworker', 'collaborator', 'vendor', 'partner', 'advisor', 'media', 'community', 'other']] = Field(..., alias="relationshipTypes", description="")
    relationship_status: Literal['active', 'inactive', 'archived', 'merged'] | None = Field(None, alias="relationshipStatus", description="")
    commercial_lifecycle: Any | None = Field(None, alias="commercialLifecycle", description="")
    relationship_owner_id: Any | None = Field(None, alias="relationshipOwnerId", description="")
    contact: dict[str, Any] | None = Field(None, alias="contact", description="")
    email: str | None = Field(None, alias="email", description="Bridge-compatible top-level email; normalized into contact provenance.")
    phone: str | None = Field(None, alias="phone", description="Bridge-compatible top-level phone; normalized into contact provenance.")
    organization_name: str | None = Field(None, alias="organizationName", description="Bridge-compatible organization label; it never creates or resolves an organization by inference.")
    source: dict[str, Any] | None = Field(None, alias="source", description="")
    props: dict[str, Any] | None = Field(None, alias="props", description="")
    lineage: dict[str, Any] | None = Field(None, alias="lineage", description="")


class CrmPersonUpsertOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    record: dict[str, Any] | None = Field(None, alias="record", description="")
    receipt: dict[str, Any] | None = Field(None, alias="receipt", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
