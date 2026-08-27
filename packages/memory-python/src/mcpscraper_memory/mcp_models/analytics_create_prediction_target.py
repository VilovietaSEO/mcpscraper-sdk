from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsCreatePredictionTargetInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    namespace_id: str = Field(..., alias="namespaceId", description="Identity Namespace belonging to this Site.")
    name: str = Field(..., alias="name", description="Human-readable prediction target.")
    outcome_event: str = Field(..., alias="outcomeEvent", description="Confirmed outcome event to predict.")
    horizon_days: int = Field(..., alias="horizonDays", description="Prediction horizon in days.")
    outcome_value_minor: int | None = Field(None, alias="outcomeValueMinor", description="Optional outcome value in minor units; this is not predicted revenue.")
    currency: str | None = Field(None, alias="currency", description="ISO 4217 currency, required with outcomeValueMinor.")
    enabled: bool | None = Field(None, alias="enabled", description="Whether to collect eligibility evidence for this target.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.")


class AnalyticsCreatePredictionTargetOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    target: dict[str, Any] = Field(..., alias="target", description="")
