from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MemoryGraphUniverseInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    note: str = Field(..., alias="note", description="Exact memory note path or resolvable note reference used as the graph target.")
    vault: str | None = Field(None, alias="vault", description="Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.")
    depth: int | None = Field(None, alias="depth", description="Maximum graph traversal depth from the root note.")
    max_nodes: int | None = Field(None, alias="maxNodes", description="Maximum graph nodes to return before marking the result truncated.")


class MemoryGraphUniverseOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    root: str | None = Field(None, alias="root", description="")
    depth: float | None = Field(None, alias="depth", description="")
    truncated: bool | None = Field(None, alias="truncated", description="")
    nodes: list[dict[str, Any]] | None = Field(None, alias="nodes", description="")
    edges: list[dict[str, Any]] | None = Field(None, alias="edges", description="")
    error: str | None = Field(None, alias="error", description="")
