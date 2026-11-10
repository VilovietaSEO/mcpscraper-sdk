from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


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

    query: str | None = Field(None, alias="query", description="")
    location: Any | None = Field(None, alias="location", description="")
    search_query: str | None = Field(None, alias="searchQuery", description="")
    search_url: str | None = Field(None, alias="searchUrl", description="")
    extracted_at: str | None = Field(None, alias="extractedAt", description="")
    requested_max_results: int | None = Field(None, alias="requestedMaxResults", description="")
    result_count: int | None = Field(None, alias="resultCount", description="")
    results: list[dict[str, Any]] | None = Field(None, alias="results", description="")
    duration_ms: int | None = Field(None, alias="durationMs", description="")
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
