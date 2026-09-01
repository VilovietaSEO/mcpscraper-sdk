from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsStartCrmSyncInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    provider: Literal['hubspot', 'highlevel', 'zoho', 'keap'] = Field(..., alias="provider", description="Supported CRM provider; tenant evidence may narrow this provider to webhook or manual mode.")
    connection_id: str = Field(..., alias="connectionId", description="Verified service connection reference.")
    mode: Literal['initial', 'incremental'] | None = Field(None, alias="mode", description="Incremental sync is the normal replay-safe mode.")
    mapping: dict[str, Any] = Field(..., alias="mapping", description="Typed mapping that passed analytics_test_crm_sync_mapping.")
    backfill_from: str | None = Field(None, alias="backfillFrom", description="Optional lower timestamp for an authorized initial backfill.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.")


class AnalyticsStartCrmSyncOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    sync: dict[str, Any] = Field(..., alias="sync", description="")
