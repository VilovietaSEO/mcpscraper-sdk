from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class SearchSerpStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="The jobId returned by search_serp.")


class SearchSerpStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    mode: Literal['light', 'full'] | None = Field(None, alias="mode", description="")
    job_id: Any | None = Field(None, alias="jobId", description="")
    status: Literal['pending', 'running', 'done'] | None = Field(None, alias="status", description="")
    status_tool: Any | None = Field(None, alias="statusTool", description="")
    replayed: bool | None = Field(None, alias="replayed", description="")
    query: str | None = Field(None, alias="query", description="")
    location: Any | None = Field(None, alias="location", description="")
    result_quality: Any | None = Field(None, alias="resultQuality", description="")
    degraded_result: Any | None = Field(None, alias="degradedResult", description="")
    degradation_reasons: list[str] | None = Field(None, alias="degradationReasons", description="")
    retry_recommended: Any | None = Field(None, alias="retryRecommended", description="")
    pagination: Any | None = Field(None, alias="pagination", description="")
    serp_completeness: Any | None = Field(None, alias="serpCompleteness", description="")
    organic_results: list[dict[str, Any]] | None = Field(None, alias="organicResults", description="")
    local_pack: list[dict[str, Any]] | None = Field(None, alias="localPack", description="")
    ai_overview: Any | None = Field(None, alias="aiOverview", description="")
    ai_mode: Any | None = Field(None, alias="aiMode", description="")
    forums: list[dict[str, Any]] | None = Field(None, alias="forums", description="")
    videos: list[dict[str, Any]] | None = Field(None, alias="videos", description="")
    what_people_saying: list[dict[str, Any]] | None = Field(None, alias="whatPeopleSaying", description="")
    paa_preview: list[dict[str, Any]] | None = Field(None, alias="paaPreview", description="")
    additional_serp_features: list[dict[str, Any]] | None = Field(None, alias="additionalSerpFeatures", description="")
    feature_status: dict[str, Any] | None = Field(None, alias="featureStatus", description="")
    feature_pages: list[dict[str, Any]] | None = Field(None, alias="featurePages", description="")
    entity_ids: Any | None = Field(None, alias="entityIds", description="")
    phase_timings: Any | None = Field(None, alias="phaseTimings", description="")
    duration_ms: Any | None = Field(None, alias="durationMs", description="")
    attempt_count: int | None = Field(None, alias="attemptCount", description="")
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
