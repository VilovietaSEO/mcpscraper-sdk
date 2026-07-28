from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class HarvestPaaInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="The search topic, e.g. \"best hvac company\". When location is supplied, the server sets Google UULE and adds the location to the executed query only if its city is not already present; do not add it manually.")
    location: str | None = Field(None, alias="location", description="City, region, or country for localized Google results, e.g. \"Denver, CO\". It sets UULE and supplies the city text when missing from query; it does not select a proxy.")
    max_questions: int | None = Field(None, alias="maxQuestions", description="PAA questions to extract. Default 30, maximum 200. Use 10 for quick probes, 100-200 for deep research. Billed per extracted question; unused hold refunded.")
    gl: str | None = Field(None, alias="gl", description="Google country code inferred from location or user language.")
    hl: str | None = Field(None, alias="hl", description="Google interface/content language inferred from the user request.")
    device: Literal["desktop", "mobile"] | None = Field(None, alias="device", description="SERP device context. Use mobile only for mobile rankings.")
    proxy_mode: Literal["configured", "none"] | None = Field(None, alias="proxyMode", description="Leave unset for direct egress. Set configured only when the installed server has a configured proxy and the user explicitly needs it; location is handled separately with UULE and query text.")
    proxy_zip: str | None = Field(None, alias="proxyZip", description="Optional US ZIP override for configured proxy routing.")
    debug: bool | None = Field(None, alias="debug", description="Include sanitized diagnostics for debugging.")


class HarvestPaaOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="")
    location: Any = Field(..., alias="location", description="")
    question_count: int = Field(..., alias="questionCount", description="")
    completion_status: Any = Field(..., alias="completionStatus", description="")
    result_quality: Any = Field(..., alias="resultQuality", description="")
    degraded_result: Any = Field(..., alias="degradedResult", description="")
    degradation_reasons: list[str] = Field(..., alias="degradationReasons", description="")
    retry_recommended: Any = Field(..., alias="retryRecommended", description="")
    questions: list[dict[str, Any]] = Field(..., alias="questions", description="")
    organic_results: list[dict[str, Any]] = Field(..., alias="organicResults", description="")
    ai_overview: Any = Field(..., alias="aiOverview", description="")
    entity_ids: Any = Field(..., alias="entityIds", description="")
    duration_ms: Any = Field(..., alias="durationMs", description="")
