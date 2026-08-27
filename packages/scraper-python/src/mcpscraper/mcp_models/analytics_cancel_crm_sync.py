from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsCancelCrmSyncInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    sync_id: str = Field(..., alias="syncId", description="Sync id returned by analytics_start_crm_sync.")


class AnalyticsCancelCrmSyncOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    sync_id: str = Field(..., alias="syncId", description="")
    cancelled: bool = Field(..., alias="cancelled", description="")
