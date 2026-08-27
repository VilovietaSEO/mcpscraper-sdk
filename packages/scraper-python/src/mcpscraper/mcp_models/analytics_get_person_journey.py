from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsGetPersonJourneyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    person_id: str = Field(..., alias="personId", description="Opaque X-Ray person identifier returned by an attributed-people or journey result.")


class AnalyticsGetPersonJourneyOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: dict[str, Any] = Field(..., alias="data", description="")
    filters: dict[str, Any] = Field(..., alias="filters", description="")
