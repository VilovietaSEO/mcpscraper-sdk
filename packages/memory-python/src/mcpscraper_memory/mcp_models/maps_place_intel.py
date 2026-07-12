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

    name: str = Field(..., alias="name", description="")
    rating: Any = Field(..., alias="rating", description="")
    review_count: Any = Field(..., alias="reviewCount", description="")
    category: Any = Field(..., alias="category", description="")
    address: Any = Field(..., alias="address", description="")
    phone: Any = Field(..., alias="phone", description="")
    website: Any = Field(..., alias="website", description="")
    hours_summary: Any = Field(..., alias="hoursSummary", description="")
    booking_url: Any = Field(..., alias="bookingUrl", description="")
    kgmid: Any = Field(..., alias="kgmid", description="")
    cid_decimal: Any = Field(..., alias="cidDecimal", description="")
    cid_url: Any = Field(..., alias="cidUrl", description="")
    lat: Any = Field(..., alias="lat", description="")
    lng: Any = Field(..., alias="lng", description="")
    reviews_status: str = Field(..., alias="reviewsStatus", description="")
    reviews_collected: int = Field(..., alias="reviewsCollected", description="")
    review_topics: list[dict[str, Any]] = Field(..., alias="reviewTopics", description="")
    services: list[str] = Field(..., alias="services", description="")
    areas_served: list[str] = Field(..., alias="areasServed", description="")
    services_status: str = Field(..., alias="servicesStatus", description="")
