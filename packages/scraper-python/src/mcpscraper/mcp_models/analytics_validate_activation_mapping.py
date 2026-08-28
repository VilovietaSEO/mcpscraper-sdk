from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsValidateActivationMappingInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    journey_tier: str | None = Field(None, alias="journeyTier", description="External activation is confirmed-only. Best-guess and candidate-assisted journey evidence is schema-invalid.")
    platform: Literal['meta', 'google', 'tiktok', 'reddit'] = Field(..., alias="platform", description="Destination provider.")
    external_dataset_id: str = Field(..., alias="externalDatasetId", description="Authorized dataset, Pixel, or conversion-action id.")
    event_mapping: dict[str, Any] = Field(..., alias="eventMapping", description="Confirmed X-Ray event to provider event mapping. Candidate-assisted events are ineligible.")


class AnalyticsValidateActivationMappingOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    validation: dict[str, Any] = Field(..., alias="validation", description="")
