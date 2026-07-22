from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class FacebookPageIntelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    page_id: str | None = Field(None, alias="pageId", description="Facebook advertiser/page ID. Use only a value returned by facebook_ad_search or copied from Ad Library.")
    library_id: str | None = Field(None, alias="libraryId", description="Facebook Ad Library archive ID. Use a value returned by facebook_ad_search, or a libraryId/adArchiveId visible in Ad Library.")
    query: str | None = Field(None, alias="query", description="Broad Ad Library keyword discovery when pageId/libraryId is not known. Results can mix unrelated advertisers; inspect matchConfidence, matchedAdvertisers, and warnings before analysis. One of pageId, libraryId, or query is required.")
    max_ads: int | None = Field(None, alias="maxAds", description="Maximum ads to inspect. Default 50, maximum 200.")
    country: str | None = Field(None, alias="country", description="Two-letter Ad Library country code. Default US.")


class FacebookPageIntelOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    advertiser_name: Any = Field(..., alias="advertiserName", description="")
    input_mode: Literal["pageId", "libraryId", "query"] = Field(..., alias="inputMode", description="")
    match_confidence: Literal["high", "medium", "low"] = Field(..., alias="matchConfidence", description="")
    match_reason: str = Field(..., alias="matchReason", description="")
    warnings: list[str] = Field(..., alias="warnings", description="")
    matched_advertisers: list[dict[str, Any]] = Field(..., alias="matchedAdvertisers", description="")
    total_ads: int = Field(..., alias="totalAds", description="")
    active_count: int = Field(..., alias="activeCount", description="")
    video_count: int = Field(..., alias="videoCount", description="")
    image_count: int = Field(..., alias="imageCount", description="")
    ads: list[dict[str, Any]] = Field(..., alias="ads", description="")
