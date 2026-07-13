from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MapsSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="Business category, niche, or search term, e.g. \"roofers\". Do not include location here — use location instead.")
    location: str | None = Field(None, alias="location", description="City, region, country, or service area, e.g. \"Denver, CO\".")
    gl: str | None = Field(None, alias="gl", description="Google country code inferred from location.")
    hl: str | None = Field(None, alias="hl", description="Language inferred from user request.")
    max_results: int | None = Field(None, alias="maxResults", description="Number of candidates to return. Default 10, maximum 50.")
    proxy_mode: Literal["location", "configured", "none"] | None = Field(None, alias="proxyMode", description="Defaults to location (city/state residential proxy targeting). configured forces the service proxy without city/ZIP targeting; none is local debugging only.")
    proxy_zip: str | None = Field(None, alias="proxyZip", description="Optional US ZIP override for residential proxy targeting.")
    debug: bool | None = Field(None, alias="debug", description="Include sanitized browser/proxy diagnostics.")


class MapsSearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
