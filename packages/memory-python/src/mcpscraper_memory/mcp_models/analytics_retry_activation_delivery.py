from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsRetryActivationDeliveryInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    job_id: str = Field(..., alias="jobId", description="Failed activation job id returned by analytics_list_activation_receipts.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsRetryActivationDeliveryOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    job: dict[str, Any] = Field(..., alias="job", description="")
