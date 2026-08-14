from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MemoryBacklinksInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    note: str = Field(..., alias="note", description="Exact memory note path or resolvable note reference used as the graph target.")
    vault: str | None = Field(None, alias="vault", description="Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.")


class MemoryBacklinksOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    nodes: list[dict[str, Any]] | None = Field(None, alias="nodes", description="")
    edges: list[dict[str, Any]] | None = Field(None, alias="edges", description="")
    error: str | None = Field(None, alias="error", description="")
