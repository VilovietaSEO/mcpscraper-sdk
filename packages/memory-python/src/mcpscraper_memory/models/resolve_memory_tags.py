from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ResolveMemoryTagsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    candidates: list[dict[str, Any]] = Field(..., alias="candidates", description="")


class ResolveMemoryTagsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    resolutions: list[dict[str, Any]] | None = Field(None, alias="resolutions", description="")
    error: str | None = Field(None, alias="error", description="")
