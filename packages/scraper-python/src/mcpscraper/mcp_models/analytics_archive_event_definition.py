from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsArchiveEventDefinitionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    definition_id: str = Field(..., alias="definitionId", description="Event definition id returned by analytics_list_event_definitions.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsArchiveEventDefinitionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    definition: dict[str, Any] = Field(..., alias="definition", description="")
