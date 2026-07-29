from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GoogleAdsPageIntelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    domain: str | None = Field(None, alias="domain", description="A website from google_ads_search.websites (e.g. getviktor.com). Preferred input: people know the website, not the advertiser's registered name. Resolves to whichever advertiser account runs ads for that domain.")
    advertiser_name: str | None = Field(None, alias="advertiserName", description="An advertiser name exactly as returned in google_ads_search.advertisers[].name (e.g. \"PPS Plumbing Services\"). Use when the user picked an advertiser rather than a website.")
    advertiser_id: str | None = Field(None, alias="advertiserId", description="Google Ads Transparency advertiser ID (starts with AR...). Only available if you already have one from a prior page-intel result — google_ads_search does NOT return advertiser IDs. Do not construct one yourself.")
    region: str | None = Field(None, alias="region", description="Two-letter region code for where the ads are shown. Default US.")
    max_ads: int | None = Field(None, alias="maxAds", description="Maximum creatives to inspect and hydrate. Default 50, maximum 200. Prefer 25-50 for focused scans.")


class GoogleAdsPageIntelOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    advertiser_id: Any = Field(..., alias="advertiserId", description="")
    advertiser_name: Any = Field(..., alias="advertiserName", description="")
    domain: Any = Field(..., alias="domain", description="")
    region: str = Field(..., alias="region", description="")
    total_creatives: int = Field(..., alias="totalCreatives", description="")
    video_count: int = Field(..., alias="videoCount", description="")
    image_count: int = Field(..., alias="imageCount", description="")
    text_count: int = Field(..., alias="textCount", description="")
    ads: list[dict[str, Any]] = Field(..., alias="ads", description="")
