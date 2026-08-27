from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsGetCrmSyncStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    sync_id: str = Field(..., alias="syncId", description="Durable sync id returned by analytics_start_crm_sync.")


class AnalyticsGetCrmSyncStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    sync: dict[str, Any] = Field(..., alias="sync", description="")
