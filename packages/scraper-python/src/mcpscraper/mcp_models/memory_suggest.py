from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MemorySuggestInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="Partial text typed so far, e.g. \"what is the best r\".")
    limit: int | None = Field(None, alias="limit", description="Max suggestions to return. Optional; default 8.")


class MemorySuggestOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the lookup ran; false on auth error.")
    suggestions: list[dict[str, Any]] | None = Field(None, alias="suggestions", description="Title matches ordered prefix-first then most-recent. Present when ok is true; may be empty.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
