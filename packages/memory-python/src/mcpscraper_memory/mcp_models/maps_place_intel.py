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
    include_images: bool | None = Field(None, alias="includeImages", description="Collect Google Maps listing photos, download them, and return an AI-readable manifest plus an owner-scoped ZIP artifact. The gallery is scrolled until quiescent or maxImages is reached.")
    image_scope: Literal['owner', 'all'] | None = Field(None, alias="imageScope", description="owner collects only the Google Maps By owner gallery. all collects the full gallery and labels exact owner matches versus other/unknown media.")
    max_images: int | None = Field(None, alias="maxImages", description="Maximum photos to collect when includeImages is true. Default 100, maximum 250.")
    max_inline_images: int | None = Field(None, alias="maxInlineImages", description="Maximum downloaded photos attached as MCP image blocks for direct AI vision. The ZIP and structured manifest still contain the wider result.")


class MapsPlaceIntelOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(..., alias="name", description="")
    place_url: Any = Field(..., alias="placeUrl", description="")
    rating: Any = Field(..., alias="rating", description="")
    review_count: Any = Field(..., alias="reviewCount", description="")
    category: Any = Field(..., alias="category", description="")
    address: Any = Field(..., alias="address", description="")
    phone: Any = Field(..., alias="phone", description="")
    website: Any = Field(..., alias="website", description="")
    hours_summary: Any = Field(..., alias="hoursSummary", description="")
    hours_table: list[dict[str, Any]] = Field(..., alias="hoursTable", description="")
    plus_code: Any = Field(..., alias="plusCode", description="")
    booking_url: Any = Field(..., alias="bookingUrl", description="")
    kgmid: Any = Field(..., alias="kgmid", description="")
    cid_decimal: Any = Field(..., alias="cidDecimal", description="")
    cid_url: Any = Field(..., alias="cidUrl", description="")
    lat: Any = Field(..., alias="lat", description="")
    lng: Any = Field(..., alias="lng", description="")
    reviews_status: str = Field(..., alias="reviewsStatus", description="")
    reviews_collected: int = Field(..., alias="reviewsCollected", description="")
    reviews: list[dict[str, Any]] = Field(..., alias="reviews", description="")
    review_histogram: list[dict[str, Any]] = Field(..., alias="reviewHistogram", description="")
    review_topics: list[dict[str, Any]] = Field(..., alias="reviewTopics", description="")
    services: list[str] = Field(..., alias="services", description="")
    areas_served: list[str] = Field(..., alias="areasServed", description="")
    services_status: str = Field(..., alias="servicesStatus", description="")
    about_attributes: list[dict[str, Any]] = Field(..., alias="aboutAttributes", description="")
    media: dict[str, Any] = Field(..., alias="media", description="")
