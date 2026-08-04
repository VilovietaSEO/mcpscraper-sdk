from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ResolveLocalSourcebookTagsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    candidates: list[dict[str, Any]] = Field(..., alias="candidates", description="Proposed reusable directory concepts to resolve against the live vocabulary.")


class ResolveLocalSourcebookTagsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
