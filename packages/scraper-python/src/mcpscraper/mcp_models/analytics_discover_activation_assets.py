from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsDiscoverActivationAssetsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    platform: Literal['meta', 'google', 'tiktok', 'reddit'] = Field(..., alias="platform", description="Authorized provider connection to inspect.")
    connection_ref: str = Field(..., alias="connectionRef", description="Existing provider connection reference; credentials are never accepted.")


class AnalyticsDiscoverActivationAssetsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    platform: Literal['meta', 'google', 'tiktok', 'reddit'] = Field(..., alias="platform", description="")
    required_destination_field: Literal['datasetId', 'conversionActionId', 'pixelCode', 'pixelId'] = Field(..., alias="requiredDestinationField", description="")
    assets: list[dict[str, Any]] = Field(..., alias="assets", description="")
    manual_entry_allowed: bool = Field(..., alias="manualEntryAllowed", description="")
    discovery: Literal['discovered', 'permission_limited', 'not_advertised', 'provider_error', 'manual_entry'] = Field(..., alias="discovery", description="")
    diagnostic: dict[str, Any] = Field(..., alias="diagnostic", description="")
    next_action: Literal['select_asset', 'reconnect_permissions', 'retry_discovery', 'enter_manual_id'] = Field(..., alias="nextAction", description="")
