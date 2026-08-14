from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class SearchSerpInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="The search topic, exactly as it should be searched. Include the place here when you want it in the search terms — the server sends your query to Google unchanged and never adds or removes a location.")
    location: str | None = Field(None, alias="location", description="Where Google should think the searcher is. Sets the Google UULE parameter only — it never changes your query text and never selects a proxy. To put the place in the search terms too, write it into query.")
    gl: str | None = Field(None, alias="gl", description="Google country code inferred from location or user language.")
    hl: str | None = Field(None, alias="hl", description="Google interface/content language inferred from user request.")
    device: Literal['desktop', 'mobile'] | None = Field(None, alias="device", description="SERP device context. Use mobile only for mobile rankings.")
    serp_identity: str | None = Field(None, alias="serpIdentity", description="Optional persistent SERP identity created with serp_identity_create. Reuses the same saved browser state and fixed network address across calls.")
    include_all_serp_features: bool | None = Field(None, alias="includeAllSerpFeatures", description="Capture every optional same-page SERP surface: local pack, forums, videos, AI Overview/AI Mode, and What People Are Saying.")
    include_local_pack: bool | None = Field(None, alias="includeLocalPack", description="Include Google local/map-pack businesses and merge their entity IDs.")
    include_forums: bool | None = Field(None, alias="includeForums", description="Include Discussions and Forums results.")
    include_videos: bool | None = Field(None, alias="includeVideos", description="Include video result names and URLs present on the original SERP.")
    include_ai_overview: bool | None = Field(None, alias="includeAiOverview", description="Include AI Overview and AI Mode text and citations when present.")
    include_what_people_saying: bool | None = Field(None, alias="includeWhatPeopleSaying", description="Include the What People Are Saying social surface when present.")
    pages: int | None = Field(None, alias="pages", description="Number of result pages to fetch (1–2).")
    recency: Literal['day', 'week', 'month', 'year'] | None = Field(None, alias="recency", description="Restrict results to a recent time window (Google \"past day/week/month/year\" filter). Omit for all-time. Useful for \"what is being said this week\" style queries; pairs well with a site: operator in the query.")


class SearchSerpOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="")
    location: Any = Field(..., alias="location", description="")
    result_quality: Any = Field(..., alias="resultQuality", description="")
    degraded_result: Any = Field(..., alias="degradedResult", description="")
    degradation_reasons: list[str] = Field(..., alias="degradationReasons", description="")
    retry_recommended: Any = Field(..., alias="retryRecommended", description="")
    organic_results: list[dict[str, Any]] = Field(..., alias="organicResults", description="")
    local_pack: list[dict[str, Any]] = Field(..., alias="localPack", description="")
    ai_overview: Any = Field(..., alias="aiOverview", description="")
    entity_ids: Any = Field(..., alias="entityIds", description="")
