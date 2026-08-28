from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsExportGoogleAdsCsvInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    acknowledged_purpose: str = Field(..., alias="acknowledgedPurpose", description="Explicit governed purpose acknowledgement required for advertising identifiers or activation exports.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsExportGoogleAdsCsvOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    artifact: dict[str, Any] = Field(..., alias="artifact", description="")
