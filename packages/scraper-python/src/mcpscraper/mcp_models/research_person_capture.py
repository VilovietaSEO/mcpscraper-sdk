from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ResearchPersonCaptureInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    entity_id: str | None = Field(None, alias="entityId", description="Existing governed entity identifier for this relation or edit.")
    base_revision: int = Field(..., alias="baseRevision", description="Last revision read by the caller; supply it to reject an update if the record changed meanwhile.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.")
    display_name: str = Field(..., alias="displayName", description="Human-readable person or organization name; paths, filenames, Vault references, and email-only labels are rejected.")
    content: str | None = Field(None, alias="content", description="Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.")
    source_evidence: list[dict[str, Any]] = Field(..., alias="sourceEvidence", description="One or more cited source references supporting this Research capture.")
    topics: list[str] | None = Field(None, alias="topics", description="Research topics supported by the captured source evidence.")
    research_roles: list[str] | None = Field(None, alias="researchRoles", description="Sourced roles associated with this Research subject.")
    props: dict[str, Any] | None = Field(None, alias="props", description="Complete governed note properties required by the target vault contract.")
    lineage: dict[str, Any] = Field(..., alias="lineage", description="Field authority, sensitivity, source, observation time, and confidence recorded with this governed write.")


class ResearchPersonCaptureOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    record: dict[str, Any] | None = Field(None, alias="record", description="")
    receipt: dict[str, Any] | None = Field(None, alias="receipt", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
