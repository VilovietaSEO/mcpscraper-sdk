from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsCreateCampaignLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    pixel_id: str | None = Field(None, alias="pixelId", description="Analytics Pixel id belonging to the selected Site.")
    name: str = Field(..., alias="name", description="Human-readable name for the record being created or updated.")
    destination_url: str = Field(..., alias="destinationUrl", description="Final public destination URL for the tracked campaign link.")
    source: str = Field(..., alias="source", description="Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.")
    medium: str = Field(..., alias="medium", description="Exact normalized campaign medium used to filter or label analytics data.")
    campaign: str = Field(..., alias="campaign", description="Exact normalized campaign value used to filter or label analytics data.")
    term: str | None = Field(None, alias="term", description="Optional paid-search term preserved on the tracked campaign link.")
    content: str | None = Field(None, alias="content", description="Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.")
    ad_group: str | None = Field(None, alias="adGroup", description="Optional advertising ad-group identifier preserved on the tracked campaign link.")
    ad_name: str | None = Field(None, alias="adName", description="Optional advertising ad name preserved on the tracked campaign link.")
    creative_id: str | None = Field(None, alias="creativeId", description="Optional advertising creative identifier preserved on the tracked campaign link.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsCreateCampaignLinkOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    link: dict[str, Any] = Field(..., alias="link", description="")
