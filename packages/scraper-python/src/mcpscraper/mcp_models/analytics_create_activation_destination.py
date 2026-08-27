from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsCreateActivationDestinationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    platform: Literal['meta', 'google', 'tiktok', 'reddit'] = Field(..., alias="platform", description="Normalized external platform selected for this operation.")
    name: str = Field(..., alias="name", description="Human-readable name for the record being created or updated.")
    connection_ref: str = Field(..., alias="connectionRef", description="Existing provider connection reference authorized for this analytics account.")
    external_dataset_id: str = Field(..., alias="externalDatasetId", description="Provider destination identifier already owned by the connected account.")


class AnalyticsCreateActivationDestinationOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
