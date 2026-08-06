from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsCreateActivationDestinationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="")
    platform: Literal['meta', 'google', 'tiktok', 'reddit'] = Field(..., alias="platform", description="")
    name: str = Field(..., alias="name", description="")
    connection_ref: str | None = Field(None, alias="connectionRef", description="")
    external_dataset_id: str | None = Field(None, alias="externalDatasetId", description="")


class AnalyticsCreateActivationDestinationOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
