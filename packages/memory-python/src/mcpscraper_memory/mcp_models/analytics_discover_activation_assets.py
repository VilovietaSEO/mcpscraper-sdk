from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsDiscoverActivationAssetsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    platform: Literal['meta', 'google', 'tiktok', 'reddit'] = Field(..., alias="platform", description="Authorized provider connection to inspect.")
    connection_ref: str = Field(..., alias="connectionRef", description="Existing provider connection reference; credentials are never accepted.")


class AnalyticsDiscoverActivationAssetsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    platform: Literal['meta', 'google', 'tiktok', 'reddit'] | None = Field(None, alias="platform", description="")
    required_destination_field: Literal['datasetId', 'conversionActionId', 'pixelCode', 'pixelId'] | None = Field(None, alias="requiredDestinationField", description="")
    assets: list[dict[str, Any]] | None = Field(None, alias="assets", description="")
    manual_entry_allowed: bool | None = Field(None, alias="manualEntryAllowed", description="")
    discovery: Literal['discovered', 'permission_limited', 'not_advertised', 'provider_error', 'manual_entry'] | None = Field(None, alias="discovery", description="")
    diagnostic: dict[str, Any] | None = Field(None, alias="diagnostic", description="")
    next_action: Literal['select_asset', 'reconnect_permissions', 'retry_discovery', 'enter_manual_id'] | None = Field(None, alias="nextAction", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
