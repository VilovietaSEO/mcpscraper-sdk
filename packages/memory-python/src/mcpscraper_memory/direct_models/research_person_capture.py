from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ResearchPersonCaptureInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    entity_id: str | None = Field(None, alias="entityId", description="")
    base_revision: int = Field(..., alias="baseRevision", description="")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="")
    display_name: str = Field(..., alias="displayName", description="")
    content: str | None = Field(None, alias="content", description="")
    source_evidence: list[dict[str, Any]] = Field(..., alias="sourceEvidence", description="")
    topics: list[str] | None = Field(None, alias="topics", description="")
    research_roles: list[str] | None = Field(None, alias="researchRoles", description="")
    props: dict[str, Any] | None = Field(None, alias="props", description="")
    lineage: dict[str, Any] = Field(..., alias="lineage", description="")


class ResearchPersonCaptureOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    record: dict[str, Any] | None = Field(None, alias="record", description="")
    receipt: dict[str, Any] | None = Field(None, alias="receipt", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
