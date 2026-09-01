from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsPlanCrmProvisioningInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    provider: Literal['hubspot', 'highlevel', 'zoho', 'keap'] = Field(..., alias="provider", description="Supported CRM provider.")
    connection_id: str = Field(..., alias="connectionId", description="Existing service connection reference for tenant-specific discovery.")
    fields: list[dict[str, Any]] = Field(..., alias="fields", description="Discovered tenant fields used to build a no-write preview.")
    allowed_operations: list[str] | None = Field(None, alias="allowedOperations", description="Tenant-discovered operations; these may narrow but never widen the public provider profile.")


class AnalyticsPlanCrmProvisioningOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    plan: dict[str, Any] = Field(..., alias="plan", description="")
    reused: bool = Field(..., alias="reused", description="")
