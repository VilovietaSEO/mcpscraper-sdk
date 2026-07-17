from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ListMemoryTagsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    include_deprecated: bool | None = Field(None, alias="includeDeprecated", description="Include deprecated tags as well as active tags. Defaults true so the AI sees the complete vocabulary; pass false only for an active-only display.")


class ListMemoryTagsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    tags: list[dict[str, Any]] | None = Field(None, alias="tags", description="")
    error: str | None = Field(None, alias="error", description="")
