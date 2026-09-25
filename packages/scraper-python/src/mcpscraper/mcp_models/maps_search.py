from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MapsSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="Business category, niche, or search term, e.g. \"roofers\".")
    location: str | None = Field(None, alias="location", description="Enter a US state name or code, e.g. Utah or UT, for a state-targeted search. Omit for direct search.")
    gl: str | None = Field(None, alias="gl", description="Google country code inferred from location.")
    hl: str | None = Field(None, alias="hl", description="Language inferred from user request.")
    max_results: int | None = Field(None, alias="maxResults", description="Number of candidates to return. Default 10, maximum 50.")
    include_services: bool | None = Field(None, alias="includeServices", description="Open organic Businesses profiles for configured services and areas served. For more than three requested results, first click More businesses. Does not collect review cards; plain searches use the Google Maps feed.")


class MapsSearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    provider: str | None = Field(None, alias="provider", description="")
    fallback_from: str | None = Field(None, alias="fallbackFrom", description="")
    acquisition_provider: str | None = Field(None, alias="acquisitionProvider", description="")
    query: str = Field(..., alias="query", description="")
    location: Any = Field(..., alias="location", description="")
    search_query: str = Field(..., alias="searchQuery", description="")
    search_url: str = Field(..., alias="searchUrl", description="")
    extracted_at: str = Field(..., alias="extractedAt", description="")
    requested_max_results: int = Field(..., alias="requestedMaxResults", description="")
    result_count: int = Field(..., alias="resultCount", description="")
    results: list[dict[str, Any]] = Field(..., alias="results", description="")
    duration_ms: int = Field(..., alias="durationMs", description="")
