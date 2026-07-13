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
