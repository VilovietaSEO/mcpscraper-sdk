from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsGetPredictionEligibilityInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    namespace_id: str = Field(..., alias="namespaceId", description="Identity Namespace belonging to this Site.")
    target_id: str = Field(..., alias="targetId", description="Prediction target id returned by analytics_list_prediction_targets.")


class AnalyticsGetPredictionEligibilityOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    target: dict[str, Any] = Field(..., alias="target", description="")
    eligibility: dict[str, Any] = Field(..., alias="eligibility", description="")
