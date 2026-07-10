from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class TrustpilotReviewsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    domain: str = Field(..., alias="domain", description="The business's domain as it appears in its Trustpilot URL, e.g. \"www.bhphotovideo.com\" (include the www. if the site uses it — pass the domain as-is, do not guess).")
    max_pages: int | None = Field(None, alias="maxPages", description="Review pages to fetch (~20 reviews per page). Default 5 (~100 reviews). Maximum 50 — large companies can have 1,000+ pages; this tool is for sampling, not full-corpus export.")


class TrustpilotReviewsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
