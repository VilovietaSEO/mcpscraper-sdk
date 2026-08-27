from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsWithdrawConsentInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    subject_ref: str = Field(..., alias="subjectRef", description="Opaque consent subject reference returned by consent coverage or a safe journey. MCP cannot grant visitor consent.")
    occurred_at: str | None = Field(None, alias="occurredAt", description="Optional visitor-reported withdrawal time; defaults to server time.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.")


class AnalyticsWithdrawConsentOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    receipt: dict[str, Any] = Field(..., alias="receipt", description="")
    downstream: dict[str, Any] = Field(..., alias="downstream", description="")
