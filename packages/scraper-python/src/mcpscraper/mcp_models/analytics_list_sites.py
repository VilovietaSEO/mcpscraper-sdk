from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsListSitesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class AnalyticsListSitesOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    sites: list[dict[str, Any]] = Field(..., alias="sites", description="")
