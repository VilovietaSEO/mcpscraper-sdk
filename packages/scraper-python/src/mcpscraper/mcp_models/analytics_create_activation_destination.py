from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsCreateActivationDestinationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    platform: Literal['meta', 'google', 'tiktok', 'reddit'] = Field(..., alias="platform", description="Normalized external platform selected for this operation.")
    name: str = Field(..., alias="name", description="Human-readable name for the record being created or updated.")
    connection_ref: str = Field(..., alias="connectionRef", description="Existing provider connection reference authorized for this analytics account.")
    external_dataset_id: str = Field(..., alias="externalDatasetId", description="Provider destination identifier already owned by the connected account.")
    operating_account_id: str | None = Field(None, alias="operatingAccountId", description="Google Ads operating account identifier required for Google Data Manager destinations.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsCreateActivationDestinationOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    destination: dict[str, Any] | None = Field(None, alias="destination", description="")
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
