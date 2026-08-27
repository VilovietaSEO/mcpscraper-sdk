from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsTestActivationDestinationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    destination_id: str = Field(..., alias="destinationId", description="Activation destination id returned by analytics_list_activation_destinations.")
    test_event_code: str | None = Field(None, alias="testEventCode", description="Provider test event code required by Meta and TikTok. Obtain it from the authorized provider test-events screen; it is sent only to that configured destination.")
    test_id: str | None = Field(None, alias="testId", description="Provider test ID required by Reddit Conversions API. It is sent only to that configured destination.")


class AnalyticsTestActivationDestinationOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
