from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsVerifyLiveEventDefinitionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    definition_id: str = Field(..., alias="definitionId", description="Browser event-definition identifier returned by analytics_list_event_definitions.")
    timeout_ms: int | None = Field(None, alias="timeoutMs", description="Bounded wait for a newly persisted matching event.")
    max_age_seconds: int | None = Field(None, alias="maxAgeSeconds", description="Maximum accepted age of the persisted matching event.")


class AnalyticsVerifyLiveEventDefinitionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    verification: dict[str, Any] = Field(..., alias="verification", description="")
