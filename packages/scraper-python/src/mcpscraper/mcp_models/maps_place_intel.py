from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MapsPlaceIntelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    business_name: str = Field(..., alias="businessName", description="Business name only, e.g. \"Elite Roofing\" (not \"Elite Roofing Denver CO\" — put the city in location).")
    location: str = Field(..., alias="location", description="City/region/country where the business should be searched, e.g. \"Denver, CO\".")
    gl: str | None = Field(None, alias="gl", description="Google country code inferred from location.")
    hl: str | None = Field(None, alias="hl", description="Language inferred from user request.")
    include_reviews: bool | None = Field(None, alias="includeReviews", description="Fetch individual review cards — for reviews, customer pain, complaints, or praise themes.")
    max_reviews: int | None = Field(None, alias="maxReviews", description="Max review cards when includeReviews is true. Default 50, maximum 500.")
    include_services: bool | None = Field(None, alias="includeServices", description="Fetch the business's configured services list and areas-served list, when the profile has them. Adds one extra page visit; not present for every business.")


class MapsPlaceIntelOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
