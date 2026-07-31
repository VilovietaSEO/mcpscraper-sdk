from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ResolveMemoryTagsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    candidates: list[dict[str, Any]] = Field(..., alias="candidates", description="")
    accept: dict[str, Any] | None = Field(None, alias="accept", description="Confirm a candidate returned by an earlier review, as {proposedTag: canonicalTag}. The proposed spelling is recorded as an alias of the canonical tag so the same judgement is never re-litigated.")


class ResolveMemoryTagsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    resolutions: list[dict[str, Any]] | None = Field(None, alias="resolutions", description="")
    error: str | None = Field(None, alias="error", description="")
