from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class SearchSerpInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="The search topic, exactly as it should be searched. Include the place here when you want it in the search terms — the server sends your query to Google unchanged and never adds or removes a location.")
    location: str | None = Field(None, alias="location", description="Compatibility field. Ordinary search ignores this. Include a place in query when needed.")
    gl: str | None = Field(None, alias="gl", description="Compatibility field. Ordinary search uses its fixed default market.")
    hl: str | None = Field(None, alias="hl", description="Compatibility field. Ordinary search uses its fixed default language.")
    device: Literal['desktop', 'mobile'] | None = Field(None, alias="device", description="Compatibility field. Ordinary search uses desktop results.")
    idempotency_key: str | None = Field(None, alias="idempotencyKey", description="Retry key: reuse after a timeout to avoid re-billing. New key per search.")
    serp_identity: str | None = Field(None, alias="serpIdentity", description="Optional persistent SERP identity created with serp_identity_create. Reuses the same saved browser state and fixed network address across calls.")
    include_all_serp_features: bool | None = Field(None, alias="includeAllSerpFeatures", description="Compatibility field. Ordinary search returns organic results only.")
    include_local_pack: bool | None = Field(None, alias="includeLocalPack", description="Compatibility field. Ordinary search does not include the local pack.")
    include_forums: bool | None = Field(None, alias="includeForums", description="Compatibility field. Ordinary search does not include forum modules.")
    include_videos: bool | None = Field(None, alias="includeVideos", description="Compatibility field. Ordinary search does not include video modules.")
    include_ai_overview: bool | None = Field(None, alias="includeAiOverview", description="Compatibility field. Ordinary search does not include AI modules.")
    include_what_people_saying: bool | None = Field(None, alias="includeWhatPeopleSaying", description="Compatibility field. Ordinary search does not include social modules.")
    pages: int | None = Field(None, alias="pages", description="Request one page by default or two pages of organic results.")
    recency: Literal['day', 'week', 'month', 'year'] | None = Field(None, alias="recency", description="Compatibility field. Ordinary search does not apply a date filter.")


class SearchSerpOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: Any = Field(..., alias="jobId", description="")
    status: Literal['pending', 'running', 'done'] = Field(..., alias="status", description="")
    status_tool: Any = Field(..., alias="statusTool", description="")
    replayed: bool = Field(..., alias="replayed", description="")
    query: str = Field(..., alias="query", description="")
    location: Any = Field(..., alias="location", description="")
    result_quality: Any = Field(..., alias="resultQuality", description="")
    degraded_result: Any = Field(..., alias="degradedResult", description="")
    degradation_reasons: list[str] = Field(..., alias="degradationReasons", description="")
    retry_recommended: Any = Field(..., alias="retryRecommended", description="")
    pagination: Any = Field(..., alias="pagination", description="")
    serp_completeness: Any = Field(..., alias="serpCompleteness", description="")
    organic_results: list[dict[str, Any]] = Field(..., alias="organicResults", description="")
    local_pack: list[dict[str, Any]] = Field(..., alias="localPack", description="")
    ai_overview: Any = Field(..., alias="aiOverview", description="")
    entity_ids: Any = Field(..., alias="entityIds", description="")
    phase_timings: Any = Field(..., alias="phaseTimings", description="")
    duration_ms: Any = Field(..., alias="durationMs", description="")
    attempt_count: int = Field(..., alias="attemptCount", description="")
