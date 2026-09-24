from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class SearchSerpStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="The jobId returned by search_serp.")


class SearchSerpStatusOutput(BaseModel):
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
