from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsReconcileConnectionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    connection_id: str = Field(..., alias="connectionId", description="Phone or CRM connection id returned by analytics_list_connections.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsReconcileConnectionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    reconciliation: dict[str, Any] = Field(..., alias="reconciliation", description="")
