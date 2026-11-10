from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class HarvestPaaInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    pages: int | None = Field(None, alias="pages", description="Organic result pages to capture. Default 1, maximum 2. Page 2 is captured when available before harvesting PAA on the original first page; it does not add a second PAA graph. Pagination output reports the pages actually captured.")
    query: str = Field(..., alias="query", description="The search topic, exactly as it should be searched, e.g. \"best hvac company in Denver\". Include the place here when you want it in the search terms — the server sends your query to Google unchanged and never adds or removes a location.")
    location: str | None = Field(None, alias="location", description="Where Google should think the searcher is, e.g. \"Denver, CO\". Sets the Google UULE parameter only — it never changes your query text and never selects a proxy. To put the place in the search terms too, write it into query.")
    max_questions: int | None = Field(None, alias="maxQuestions", description="PAA questions to extract. Default 30, maximum 100. Use 10 for quick probes and 100 for deep research. Billed per extracted question; unused hold refunded.")
    gl: str | None = Field(None, alias="gl", description="Google country code inferred from location or user language.")
    hl: str | None = Field(None, alias="hl", description="Google interface/content language inferred from the user request.")
    device: Literal['desktop', 'mobile'] | None = Field(None, alias="device", description="SERP device context. Use mobile only for mobile rankings.")
    idempotency_key: str | None = Field(None, alias="idempotencyKey", description="Optional duplicate-start key. Reuse it only after an uncertain or lost response to the same logical call; use a new key for an intentional retry after a terminal failure. This is not the run identifier.")
    serp_identity: str | None = Field(None, alias="serpIdentity", description="Optional persistent SERP identity created with serp_identity_create. Reuses the same saved browser state and fixed network address across calls.")
    include_all_serp_features: bool | None = Field(None, alias="includeAllSerpFeatures", description="Capture every optional same-page SERP surface: local pack, forums, videos, AI Overview/AI Mode, and What People Are Saying.")
    include_local_pack: bool | None = Field(None, alias="includeLocalPack", description="Include Google local/map-pack businesses and merge their entity IDs.")
    include_forums: bool | None = Field(None, alias="includeForums", description="Include Discussions and Forums results.")
    include_videos: bool | None = Field(None, alias="includeVideos", description="Include video result names and URLs present on the original SERP.")
    include_ai_overview: bool | None = Field(None, alias="includeAiOverview", description="Include AI Overview and AI Mode text and citations when present.")
    include_what_people_saying: bool | None = Field(None, alias="includeWhatPeopleSaying", description="Include the What People Are Saying social surface when present.")


class HarvestPaaOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str | None = Field(None, alias="query", description="")
    location: Any | None = Field(None, alias="location", description="")
    question_count: int | None = Field(None, alias="questionCount", description="")
    paa_incomplete_answers: int | None = Field(None, alias="paaIncompleteAnswers", description="")
    completion_status: Any | None = Field(None, alias="completionStatus", description="")
    result_quality: Any | None = Field(None, alias="resultQuality", description="")
    degraded_result: Any | None = Field(None, alias="degradedResult", description="")
    degradation_reasons: list[str] | None = Field(None, alias="degradationReasons", description="")
    retry_recommended: Any | None = Field(None, alias="retryRecommended", description="")
    paa_lifecycle: Any | None = Field(None, alias="paaLifecycle", description="")
    phase_timings: Any | None = Field(None, alias="phaseTimings", description="")
    pagination: Any | None = Field(None, alias="pagination", description="")
    questions: list[dict[str, Any]] | None = Field(None, alias="questions", description="")
    organic_results: list[dict[str, Any]] | None = Field(None, alias="organicResults", description="")
    ai_overview: Any | None = Field(None, alias="aiOverview", description="")
    entity_ids: Any | None = Field(None, alias="entityIds", description="")
    duration_ms: Any | None = Field(None, alias="durationMs", description="")
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
