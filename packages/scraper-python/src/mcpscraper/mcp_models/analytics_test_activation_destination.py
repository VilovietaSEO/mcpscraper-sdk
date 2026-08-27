from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsTestActivationDestinationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    destination_id: str = Field(..., alias="destinationId", description="Activation destination id returned by analytics_list_activation_destinations.")


class AnalyticsTestActivationDestinationOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
