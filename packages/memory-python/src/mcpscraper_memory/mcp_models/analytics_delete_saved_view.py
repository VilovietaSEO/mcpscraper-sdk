from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsDeleteSavedViewInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    view_id: str = Field(..., alias="viewId", description="Saved-view id returned by analytics_list_saved_views.")


class AnalyticsDeleteSavedViewOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
