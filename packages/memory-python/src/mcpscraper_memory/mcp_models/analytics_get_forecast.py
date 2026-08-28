from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsGetForecastInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    limit: int | None = Field(None, alias="limit", description="Maximum rows or records to return on this page; use the returned cursor for more.")
    cursor: str | None = Field(None, alias="cursor", description="Opaque continuation cursor returned by the previous page; omit for the first page.")


class AnalyticsGetForecastOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: dict[str, Any] = Field(..., alias="data", description="")
