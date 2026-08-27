from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsListCrmOutboundPoliciesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")


class AnalyticsListCrmOutboundPoliciesOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    policies: list[dict[str, Any]] = Field(..., alias="policies", description="")
