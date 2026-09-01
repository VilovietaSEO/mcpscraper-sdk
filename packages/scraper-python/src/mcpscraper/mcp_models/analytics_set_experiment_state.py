from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsSetExperimentStateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Authorized Analytics Site id.")
    experiment_id: str = Field(..., alias="experimentId", description="Owner-bound experiment id returned by analytics_create_experiment.")
    revision: int = Field(..., alias="revision", description="Exact experiment revision being changed.")
    operation: Literal['approve', 'activate_canary', 'activate', 'pause', 'kill', 'archive'] = Field(..., alias="operation", description="Approval and activation are distinct operations. Pause and kill publish rollback immediately.")
    confirmed: bool | None = Field(None, alias="confirmed", description="Required for approve, activate_canary, and activate. This confirms only the exact state transition.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsSetExperimentStateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    experiment: dict[str, Any] = Field(..., alias="experiment", description="")
