from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsListFiltersInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    include_examples: bool | None = Field(None, alias="includeExamples", description="When true, include short instructions for using a saved filter id in commons_search_entities.")


class CommonsListFiltersOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
