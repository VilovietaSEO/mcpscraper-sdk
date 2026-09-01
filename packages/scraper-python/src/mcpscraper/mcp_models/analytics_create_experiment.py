from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsCreateExperimentInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Authorized Analytics Site id.")
    plan: dict[str, Any] = Field(..., alias="plan", description="Preregistered hypothesis, metric, audience, sample requirements, expiry, allocations, and allowlisted visual operations. One control variant must have no operations.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsCreateExperimentOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    experiment: dict[str, Any] = Field(..., alias="experiment", description="")
