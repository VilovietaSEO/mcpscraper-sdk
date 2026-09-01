from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsUpdateCrmSyncScheduleInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    sync_id: str = Field(..., alias="syncId", description="Durable sync id returned by analytics_start_crm_sync.")
    provider: Literal['hubspot', 'highlevel', 'zoho', 'keap'] = Field(..., alias="provider", description="Supported CRM provider; scheduling fails closed unless effective capability permits polling.")
    connection_id: str = Field(..., alias="connectionId", description="Verified service connection reference.")
    interval_seconds: Any = Field(..., alias="intervalSeconds", description="Bounded synchronization interval; null disables the schedule.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.")


class AnalyticsUpdateCrmSyncScheduleOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    schedule: dict[str, Any] = Field(..., alias="schedule", description="")
