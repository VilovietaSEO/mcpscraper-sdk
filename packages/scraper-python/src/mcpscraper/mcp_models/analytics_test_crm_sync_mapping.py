from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsTestCrmSyncMappingInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    provider: str = Field(..., alias="provider", description="CRM or call provider.")
    mapping: dict[str, Any] = Field(..., alias="mapping", description="Proposed typed CRM event mapping.")
    available_objects: list[dict[str, Any]] | None = Field(None, alias="availableObjects", description="Bounded discovery objects returned by analytics_discover_crm_sync_objects.")


class AnalyticsTestCrmSyncMappingOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    test: dict[str, Any] = Field(..., alias="test", description="")
