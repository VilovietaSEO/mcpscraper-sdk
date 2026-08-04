from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ListLocalSourcebookTagsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    include_deprecated: bool | None = Field(None, alias="includeDeprecated", description="Include deprecated and pending tags so the caller sees the complete directory vocabulary.")


class ListLocalSourcebookTagsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
