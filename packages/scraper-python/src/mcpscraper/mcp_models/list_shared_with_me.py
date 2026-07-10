from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ListSharedWithMeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class ListSharedWithMeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth error.")
    notes: list[dict[str, Any]] | None = Field(None, alias="notes", description="Notes shared with you and accepted. Present when ok is true.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
