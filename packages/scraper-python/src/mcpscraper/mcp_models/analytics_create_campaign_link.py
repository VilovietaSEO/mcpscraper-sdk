from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsCreateCampaignLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="")
    pixel_id: str | None = Field(None, alias="pixelId", description="")
    name: str = Field(..., alias="name", description="")
    destination_url: str = Field(..., alias="destinationUrl", description="")
    source: str = Field(..., alias="source", description="")
    medium: str = Field(..., alias="medium", description="")
    campaign: str = Field(..., alias="campaign", description="")
    term: str | None = Field(None, alias="term", description="")
    content: str | None = Field(None, alias="content", description="")
    ad_group: str | None = Field(None, alias="adGroup", description="")
    ad_name: str | None = Field(None, alias="adName", description="")
    creative_id: str | None = Field(None, alias="creativeId", description="")


class AnalyticsCreateCampaignLinkOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
