from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsGetEntitlementInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class AnalyticsGetEntitlementOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    entitlement: dict[str, Any] = Field(..., alias="entitlement", description="")
