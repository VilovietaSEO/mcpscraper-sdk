from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MemoryGraphPathInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    from_: str = Field(..., alias="from", description="Exact starting memory note path or resolvable note reference.")
    to: str = Field(..., alias="to", description="Exact destination memory note path or resolvable note reference.")
    from_vault: str | None = Field(None, alias="fromVault", description="Vault containing the starting memory note; omit only when the note reference already resolves unambiguously.")
    to_vault: str | None = Field(None, alias="toVault", description="Vault containing the destination memory note; omit only when the note reference already resolves unambiguously.")
    max_depth: int | None = Field(None, alias="maxDepth", description="Maximum number of graph edges to traverse before reporting no path.")


class MemoryGraphPathOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    nodes: list[dict[str, Any]] | None = Field(None, alias="nodes", description="")
    edges: list[dict[str, Any]] | None = Field(None, alias="edges", description="")
    error: str | None = Field(None, alias="error", description="")
