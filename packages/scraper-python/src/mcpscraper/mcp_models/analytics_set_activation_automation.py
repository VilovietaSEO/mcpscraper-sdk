from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsSetActivationAutomationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    destination_id: str = Field(..., alias="destinationId", description="Activation destination identifier returned by analytics_list_activation_destinations.")
    enabled: bool = Field(..., alias="enabled", description="Explicitly enable or disable automatic delivery. Enabling requires a verified destination.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsSetActivationAutomationOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    destination: dict[str, Any] = Field(..., alias="destination", description="")
