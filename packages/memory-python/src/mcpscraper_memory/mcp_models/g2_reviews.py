from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class G2ReviewsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    product: str = Field(..., alias="product", description="The product's G2 URL slug, e.g. \"notion\" from g2.com/products/notion/reviews (also accepts a full g2.com product URL).")
    max_pages: int | None = Field(None, alias="maxPages", description="Review pages to fetch (~10 reviews per page). Default 5 (~50 reviews). Maximum 50 — this tool is for sampling, not full-corpus export.")


class G2ReviewsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    product: str = Field(..., alias="product", description="")
    review_url: str = Field(..., alias="reviewUrl", description="")
    extracted_at: str = Field(..., alias="extractedAt", description="")
    requested_max_pages: int = Field(..., alias="requestedMaxPages", description="")
    pages_fetched: int = Field(..., alias="pagesFetched", description="")
    review_count: int = Field(..., alias="reviewCount", description="")
    reviews: list[dict[str, Any]] = Field(..., alias="reviews", description="")
    duration_ms: float = Field(..., alias="durationMs", description="")
