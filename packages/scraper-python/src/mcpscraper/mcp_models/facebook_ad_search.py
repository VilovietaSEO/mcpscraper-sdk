from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class FacebookAdSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="Advertiser, brand, competitor, niche, or keyword to search in Facebook Ad Library.")
    country: str | None = Field(None, alias="country", description="Two-letter Ad Library country code. Default US. Examples: US, CA, GB, AU.")
    max_results: int | None = Field(None, alias="maxResults", description="Maximum advertisers to return. Default 10, maximum 20. Prefer tighter search terms over maxing this out.")


class FacebookAdSearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="")
    advertiser_count: int = Field(..., alias="advertiserCount", description="")
    advertisers: list[dict[str, Any]] = Field(..., alias="advertisers", description="")
