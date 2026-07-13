from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GoogleAdsPageIntelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    advertiser_id: str | None = Field(None, alias="advertiserId", description="Google Ads Transparency advertiser ID (starts with AR...). Use one returned by google_ads_search; do not construct one yourself.")
    domain: str | None = Field(None, alias="domain", description="A domain (e.g. getviktor.com) whose primary advertiser to inspect when advertiserId is unknown. One of advertiserId or domain is required.")
    region: str | None = Field(None, alias="region", description="Two-letter region code for where the ads are shown. Default US.")
    max_ads: int | None = Field(None, alias="maxAds", description="Maximum creatives to inspect and hydrate. Default 50, maximum 200. Prefer 25-50 for focused scans.")


class GoogleAdsPageIntelOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
