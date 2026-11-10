from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class G2ReviewsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    product: str = Field(..., alias="product", description="The product's G2 URL slug, e.g. \"notion\" from g2.com/products/notion/reviews (also accepts a full g2.com product URL).")
    max_pages: int | None = Field(None, alias="maxPages", description="Review pages to fetch (~10 reviews per page). Default 5 (~50 reviews). Maximum 50 — this tool is for sampling, not full-corpus export.")


class G2ReviewsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    product: str | None = Field(None, alias="product", description="")
    review_url: str | None = Field(None, alias="reviewUrl", description="")
    extracted_at: str | None = Field(None, alias="extractedAt", description="")
    requested_max_pages: int | None = Field(None, alias="requestedMaxPages", description="")
    pages_fetched: int | None = Field(None, alias="pagesFetched", description="")
    review_count: int | None = Field(None, alias="reviewCount", description="")
    reviews: list[dict[str, Any]] | None = Field(None, alias="reviews", description="")
    duration_ms: float | None = Field(None, alias="durationMs", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
