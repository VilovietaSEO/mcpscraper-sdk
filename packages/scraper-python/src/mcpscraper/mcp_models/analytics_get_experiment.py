from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsGetExperimentInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Authorized Analytics Site id.")
    experiment_id: str = Field(..., alias="experimentId", description="Owner-bound experiment id returned by analytics_create_experiment.")


class AnalyticsGetExperimentOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    experiment: dict[str, Any] = Field(..., alias="experiment", description="")
