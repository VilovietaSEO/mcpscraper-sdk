from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class FileAssetSaveInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP request is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional caller session identifier.")
    vault: str | None = Field(None, alias="vault", description="Writable Memory vault. Raw source files should normally use Library.")
    artifact_id: str = Field(..., alias="artifactId", description="Owner-authorized MCP Scraper artifact ID for completed bytes. Local paths and remote URLs are not accepted.")
    title: str = Field(..., alias="title", description="")
    tags: list[str] | None = Field(None, alias="tags", description="")
    source_ref: dict[str, Any] | None = Field(None, alias="sourceRef", description="")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Stable key for this logical save. Same key and content resumes; conflicting content fails before another write.")


class FileAssetSaveOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    asset: dict[str, Any] | None = Field(None, alias="asset", description="")
    reused_object: bool | None = Field(None, alias="reusedObject", description="")
    next_action: str | None = Field(None, alias="nextAction", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
