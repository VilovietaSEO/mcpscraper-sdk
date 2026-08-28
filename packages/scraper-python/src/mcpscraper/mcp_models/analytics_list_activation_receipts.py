from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsListActivationReceiptsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    destination_id: str = Field(..., alias="destinationId", description="Activation destination id returned by analytics_list_activation_destinations.")
    limit: int | None = Field(None, alias="limit", description="Maximum receipt rows to return.")
    cursor: str | None = Field(None, alias="cursor", description="Opaque pagination cursor from the prior receipt page.")


class AnalyticsListActivationReceiptsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    receipts: list[dict[str, Any]] = Field(..., alias="receipts", description="")
