from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsDiscoverCrmCapabilitiesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    provider: Literal['hubspot', 'salesforce', 'highlevel', 'zoho', 'pipedrive', 'keap'] = Field(..., alias="provider", description="Supported CRM provider.")
    connection_id: str = Field(..., alias="connectionId", description="Existing service connection reference for tenant-specific discovery.")


class AnalyticsDiscoverCrmCapabilitiesOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    profile: dict[str, Any] = Field(..., alias="profile", description="")
    capability: dict[str, Any] = Field(..., alias="capability", description="")
