from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsSyncCrmPersonInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    provider: Literal['hubspot', 'highlevel', 'zoho', 'keap'] = Field(..., alias="provider", description="Supported CRM provider.")
    connection_id: str = Field(..., alias="connectionId", description="Verified service connection reference.")
    person: dict[str, Any] = Field(..., alias="person", description="Confirmed-person projection only. Candidate identity and evidence are schema-invalid.")
    mapping: dict[str, Any] | None = Field(None, alias="mapping", description="Approved provider field mapping.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.")


class AnalyticsSyncCrmPersonOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    receipt: dict[str, Any] = Field(..., alias="receipt", description="")
