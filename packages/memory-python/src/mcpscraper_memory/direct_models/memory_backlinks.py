from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MemoryBacklinksInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    note: str = Field(..., alias="note", description="")
    vault: str | None = Field(None, alias="vault", description="")


class MemoryBacklinksOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    nodes: list[dict[str, Any]] | None = Field(None, alias="nodes", description="")
    edges: list[dict[str, Any]] | None = Field(None, alias="edges", description="")
    error: str | None = Field(None, alias="error", description="")
