from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MemoryGraphPathInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    from_: str = Field(..., alias="from", description="")
    to: str = Field(..., alias="to", description="")
    from_vault: str | None = Field(None, alias="fromVault", description="")
    to_vault: str | None = Field(None, alias="toVault", description="")
    max_depth: int | None = Field(None, alias="maxDepth", description="")


class MemoryGraphPathOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    nodes: list[dict[str, Any]] | None = Field(None, alias="nodes", description="")
    edges: list[dict[str, Any]] | None = Field(None, alias="edges", description="")
    error: str | None = Field(None, alias="error", description="")
