from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsDiscoverCrmSyncObjectsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    provider: Literal['hubspot', 'salesforce', 'highlevel', 'zoho', 'pipedrive', 'keap'] = Field(..., alias="provider", description="Supported CRM provider.")
    connection_id: str | None = Field(None, alias="connectionId", description="Optional service connection for tenant discovery.")


class AnalyticsDiscoverCrmSyncObjectsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    discovered: dict[str, Any] = Field(..., alias="discovered", description="")
