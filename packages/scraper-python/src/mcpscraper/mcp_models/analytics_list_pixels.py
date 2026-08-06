from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsListPixelsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    limit: int | None = Field(None, alias="limit", description="")
    cursor: str | None = Field(None, alias="cursor", description="")


class AnalyticsListPixelsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
