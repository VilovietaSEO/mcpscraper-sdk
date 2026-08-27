from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsGetVisitorJourneyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    reference: str = Field(..., alias="reference", description="Opaque Site-scoped reference returned by an X-Ray read. Raw visitor, session, device, email, phone, IP, and identity hashes are never accepted.")


class AnalyticsGetVisitorJourneyOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: dict[str, Any] = Field(..., alias="data", description="")
