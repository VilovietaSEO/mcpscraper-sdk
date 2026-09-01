from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsVerifyRevenueSourceInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Authorized Analytics Site id.")
    setup_id: str = Field(..., alias="setupId", description="Owner-bound revenue setup id returned by prepare or the facade.")
    revision: int = Field(..., alias="revision", description="Exact current revenue setup revision; reload before retrying a stale mutation.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsVerifyRevenueSourceOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    operation: str = Field(..., alias="operation", description="")
    setup: dict[str, Any] = Field(..., alias="setup", description="")
