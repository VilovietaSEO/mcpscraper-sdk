from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsSaveFilterInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(..., alias="name", description="User-facing name for this MCP personalization filter. Reusing a name updates the saved filter.")
    description: str | None = Field(None, alias="description", description="Optional note explaining when this filter should be used.")
    filter: dict[str, Any] = Field(..., alias="filter", description="Search/filter scope to save for this account, such as a category, trail, source domain, tags, or media constraints.")


class CommonsSaveFilterOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
