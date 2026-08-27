from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsTestCrmProvisioningInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    receipt: dict[str, Any] = Field(..., alias="receipt", description="Exact approval receipt returned by analytics_approve_crm_provisioning.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.")


class AnalyticsTestCrmProvisioningOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    receipt: dict[str, Any] = Field(..., alias="receipt", description="")
