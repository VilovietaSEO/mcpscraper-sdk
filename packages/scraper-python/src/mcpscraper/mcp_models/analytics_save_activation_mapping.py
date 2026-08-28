from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsSaveActivationMappingInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    destination_id: str = Field(..., alias="destinationId", description="Activation destination identifier returned by analytics_list_activation_destinations.")
    journey_tier: str | None = Field(None, alias="journeyTier", description="Confirmed, best-guess, or separately returned combined journey projection.")
    event_mapping: dict[str, Any] = Field(..., alias="eventMapping", description="Typed confirmed-event mapping; enabled rows require exactly one primary event.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsSaveActivationMappingOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    destination: dict[str, Any] = Field(..., alias="destination", description="")
