from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


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

    ok: bool | None = Field(None, alias="ok", description="")
    target: dict[str, Any] | None = Field(None, alias="target", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
