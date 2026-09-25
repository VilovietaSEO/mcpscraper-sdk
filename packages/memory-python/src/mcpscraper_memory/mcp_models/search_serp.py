from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class SearchSerpInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    mode: Literal['light', 'full'] | None = Field(None, alias="mode", description="Light returns organic results. Full adds available SERP features for one page. With an explicit two-page request, only organic results are available and feature status is unsupported. Both default to one page.")
    query: str = Field(..., alias="query", description="The search topic, exactly as it should be searched. Include the place here when you want it in the search terms — the server sends your query to Google unchanged and never adds or removes a location.")
    location: str | None = Field(None, alias="location", description="Compatibility field. Ordinary search ignores this. Include a place in query when needed.")
    gl: str | None = Field(None, alias="gl", description="Compatibility field. Ordinary search uses its fixed default market.")
    hl: str | None = Field(None, alias="hl", description="Compatibility field. Ordinary search uses its fixed default language.")
    device: Literal['desktop', 'mobile'] | None = Field(None, alias="device", description="Compatibility field. Ordinary search uses desktop results.")
    idempotency_key: str | None = Field(None, alias="idempotencyKey", description="Retry key: reuse after a timeout to avoid re-billing. New key per search.")
    serp_identity: str | None = Field(None, alias="serpIdentity", description="Optional persistent SERP identity created with serp_identity_create. Reuses the same saved browser state and fixed network address across calls.")
    pages: int | None = Field(None, alias="pages", description="One page by default. Set 2 only when the user explicitly requests two pages; two-page results include organic listings only; if page 2 is unavailable, page 1 is returned and billed when available.")
    recency: Literal['day', 'week', 'month', 'year'] | None = Field(None, alias="recency", description="Compatibility field. Ordinary search does not apply a date filter.")


class SearchSerpOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    mode: Literal['light', 'full'] = Field(..., alias="mode", description="")
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
    ai_mode: Any = Field(..., alias="aiMode", description="")
    forums: list[dict[str, Any]] = Field(..., alias="forums", description="")
    videos: list[dict[str, Any]] = Field(..., alias="videos", description="")
    what_people_saying: list[dict[str, Any]] = Field(..., alias="whatPeopleSaying", description="")
    paa_preview: list[dict[str, Any]] = Field(..., alias="paaPreview", description="")
    additional_serp_features: list[dict[str, Any]] = Field(..., alias="additionalSerpFeatures", description="")
    feature_status: dict[str, Any] = Field(..., alias="featureStatus", description="")
    feature_pages: list[dict[str, Any]] = Field(..., alias="featurePages", description="")
    entity_ids: Any = Field(..., alias="entityIds", description="")
    phase_timings: Any = Field(..., alias="phaseTimings", description="")
    duration_ms: Any = Field(..., alias="durationMs", description="")
    attempt_count: int = Field(..., alias="attemptCount", description="")
