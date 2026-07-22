from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GoogleAdsSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="A domain (e.g. getviktor.com) or advertiser/brand name to look up in Google Ads Transparency Center.")
    region: str | None = Field(None, alias="region", description="Two-letter region code for where the ads are shown. Default US. Examples: US, CA, GB, AU.")
    max_results: int | None = Field(None, alias="maxResults", description="Maximum advertisers to return. Default 10, maximum 20.")


class GoogleAdsSearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="")
    region: str = Field(..., alias="region", description="")
    advertiser_count: int = Field(..., alias="advertiserCount", description="")
    advertisers: list[dict[str, Any]] = Field(..., alias="advertisers", description="")
