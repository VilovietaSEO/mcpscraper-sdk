from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsPrepareRevenueSourceInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Authorized Analytics Site id.")
    service_connection_ref: str = Field(..., alias="serviceConnectionRef", description="Already-authorized connected-account reference. Credentials never belong in this input.")
    role: Literal['primary', 'observation'] | None = Field(None, alias="role", description="Choose one primary authority per subscription-revenue outcome family; observation sources cannot create revenue.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsPrepareRevenueSourceOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    operation: str = Field(..., alias="operation", description="")
    setup: dict[str, Any] = Field(..., alias="setup", description="")
