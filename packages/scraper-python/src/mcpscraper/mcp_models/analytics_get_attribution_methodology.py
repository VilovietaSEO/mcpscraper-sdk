from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsGetAttributionMethodologyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Authorized Analytics Site id.")


class AnalyticsGetAttributionMethodologyOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    methodology: dict[str, Any] = Field(..., alias="methodology", description="")
