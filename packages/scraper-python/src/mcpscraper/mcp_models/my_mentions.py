from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MyMentionsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    limit: int | None = Field(None, alias="limit", description="Max mentions to return. Optional; default 25.")


class MyMentionsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth error.")
    mentions: list[dict[str, Any]] | None = Field(None, alias="mentions", description="Present when ok is true.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
