from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ListMemoryTagsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    include_deprecated: bool | None = Field(None, alias="includeDeprecated", description="")


class ListMemoryTagsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    tags: list[dict[str, Any]] | None = Field(None, alias="tags", description="")
    error: str | None = Field(None, alias="error", description="")
