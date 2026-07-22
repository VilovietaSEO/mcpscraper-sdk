from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class HarvestPaaInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="The search query. KEEP the place in the query text for localized results (e.g. \"best hvac company Denver CO\") and also set location — city-in-query is what localizes reliably.")
    location: str | None = Field(None, alias="location", description="City, region, or country for geo signals, e.g. \"Denver, CO\". Set alongside city-in-query wording; alone it does NOT reliably localize.")
    max_questions: int | None = Field(None, alias="maxQuestions", description="PAA questions to extract. Default 30, maximum 200. Use 10 for quick probes, 100-200 for deep research. Billed per extracted question; unused hold refunded.")
    gl: str | None = Field(None, alias="gl", description="Google country code inferred from location or user language.")
    hl: str | None = Field(None, alias="hl", description="Google interface/content language inferred from the user request.")
    device: Literal["desktop", "mobile"] | None = Field(None, alias="device", description="SERP device context. Use mobile only for mobile rankings.")
    proxy_mode: Literal["configured", "none"] | None = Field(None, alias="proxyMode", description="Leave unset for the default route. Country/region localization comes from gl/hl plus the city or region in the query.")
    proxy_zip: str | None = Field(None, alias="proxyZip", description="Optional US ZIP override.")
    debug: bool | None = Field(None, alias="debug", description="Include sanitized diagnostics for debugging.")


class HarvestPaaOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="")
    location: Any = Field(..., alias="location", description="")
    question_count: int = Field(..., alias="questionCount", description="")
    completion_status: Any = Field(..., alias="completionStatus", description="")
    questions: list[dict[str, Any]] = Field(..., alias="questions", description="")
    organic_results: list[dict[str, Any]] = Field(..., alias="organicResults", description="")
    ai_overview: Any = Field(..., alias="aiOverview", description="")
    entity_ids: Any = Field(..., alias="entityIds", description="")
    duration_ms: Any = Field(..., alias="durationMs", description="")
