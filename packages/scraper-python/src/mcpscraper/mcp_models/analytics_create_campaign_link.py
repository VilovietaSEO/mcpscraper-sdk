from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsCreateCampaignLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    pixel_id: str | None = Field(None, alias="pixelId", description="Analytics Pixel id belonging to the selected Site.")
    name: str = Field(..., alias="name", description="Human-readable name for the record being created or updated.")
    destination_url: str = Field(..., alias="destinationUrl", description="Final public destination URL for the tracked campaign link.")
    source: str = Field(..., alias="source", description="Required utm_source value identifying the acquisition source, such as google or a newsletter name.")
    medium: str = Field(..., alias="medium", description="Exact normalized campaign medium used to filter or label analytics data.")
    campaign: str = Field(..., alias="campaign", description="Exact normalized campaign value used to filter or label analytics data.")
    term: str | None = Field(None, alias="term", description="Optional paid-search term preserved on the tracked campaign link.")
    content: str | None = Field(None, alias="content", description="Optional utm_content label identifying the ad creative or link variant; this is not document content.")
    ad_group: str | None = Field(None, alias="adGroup", description="Optional advertising ad-group identifier preserved on the tracked campaign link.")
    ad_name: str | None = Field(None, alias="adName", description="Optional advertising ad name preserved on the tracked campaign link.")
    creative_id: str | None = Field(None, alias="creativeId", description="Optional advertising creative identifier preserved on the tracked campaign link.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsCreateCampaignLinkOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    link: dict[str, Any] | None = Field(None, alias="link", description="")
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
