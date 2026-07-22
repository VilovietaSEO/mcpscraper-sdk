from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MapsSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="Business category, niche, or search term, e.g. \"roofers\". Do not include location here — use location instead.")
    location: str | None = Field(None, alias="location", description="City, region, country, or service area, e.g. \"Denver, CO\".")
    gl: str | None = Field(None, alias="gl", description="Google country code inferred from location.")
    hl: str | None = Field(None, alias="hl", description="Language inferred from user request.")
    max_results: int | None = Field(None, alias="maxResults", description="Number of candidates to return. Default 10, maximum 50.")
    include_services: bool | None = Field(None, alias="includeServices", description="Open each returned Google Business Profile and include configured services and areas served when available. Does not collect review cards.")
    proxy_mode: Literal["location", "configured", "none"] | None = Field(None, alias="proxyMode", description="Leave unset for the default direct browser route. Google localization comes from the city in the query plus UULE, gl, and hl. location is an explicit residential-proxy override.")
    proxy_zip: str | None = Field(None, alias="proxyZip", description="Optional US ZIP override when proxyMode is location.")
    debug: bool | None = Field(None, alias="debug", description="Include sanitized browser/proxy diagnostics.")


class MapsSearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="")
    location: Any = Field(..., alias="location", description="")
    search_query: str = Field(..., alias="searchQuery", description="")
    search_url: str = Field(..., alias="searchUrl", description="")
    extracted_at: str = Field(..., alias="extractedAt", description="")
    requested_max_results: int = Field(..., alias="requestedMaxResults", description="")
    result_count: int = Field(..., alias="resultCount", description="")
    results: list[dict[str, Any]] = Field(..., alias="results", description="")
    attempts: list[dict[str, Any]] = Field(..., alias="attempts", description="")
    duration_ms: int = Field(..., alias="durationMs", description="")
