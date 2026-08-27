from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsCreateFunnelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    name: str = Field(..., alias="name", description="Human-readable funnel name.")
    stages: list[dict[str, Any]] = Field(..., alias="stages", description="Ordered stage definitions.")
    is_default: bool | None = Field(None, alias="isDefault", description="Make this version the Site default.")
    status: Literal['active', 'disabled'] | None = Field(None, alias="status", description="Initial funnel status.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.")


class AnalyticsCreateFunnelOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    definition: dict[str, Any] = Field(..., alias="definition", description="")
