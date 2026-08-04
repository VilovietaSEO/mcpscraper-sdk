from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class SearchSerpInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="The search topic. When location is supplied, the server sets Google UULE and adds the location to the executed query only if its city is not already present; do not add it manually.")
    location: str | None = Field(None, alias="location", description="City, region, or country for localized Google results. It sets UULE and supplies the city text when missing from query; it does not select a proxy.")
    gl: str | None = Field(None, alias="gl", description="Google country code inferred from location or user language.")
    hl: str | None = Field(None, alias="hl", description="Google interface/content language inferred from user request.")
    device: Literal["desktop", "mobile"] | None = Field(None, alias="device", description="SERP device context. Use mobile only for mobile rankings.")
    pages: int | None = Field(None, alias="pages", description="Number of result pages to fetch (1–2).")
    recency: Literal["day", "week", "month", "year"] | None = Field(None, alias="recency", description="Restrict results to a recent time window (Google \"past day/week/month/year\" filter). Omit for all-time. Useful for \"what is being said this week\" style queries; pairs well with a site: operator in the query.")


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
