from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsApproveCrmProvisioningInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    plan: dict[str, Any] = Field(..., alias="plan", description="Exact normalized plan returned by analytics_plan_crm_provisioning.")
    approved_field_internal_names: list[str] = Field(..., alias="approvedFieldInternalNames", description="Exact proposed namespaced provider fields approved for creation.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.")


class AnalyticsApproveCrmProvisioningOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    receipt: dict[str, Any] = Field(..., alias="receipt", description="")
