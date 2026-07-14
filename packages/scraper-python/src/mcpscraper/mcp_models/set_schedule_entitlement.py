from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class SetScheduleEntitlementInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    grantee_identity: str = Field(..., alias="granteeIdentity", description="Identity whose scheduling entitlement is being set (e.g. an email).")
    enabled: bool | None = Field(None, alias="enabled", description="Historical entitlement value for migration/recovery only. Omit to preserve the stored value.")
    quota_per_period: float | None = Field(None, alias="quotaPerPeriod", description="Historical monthly execution quota retained only for migration compatibility. Omit to preserve the stored value.")
    mcp_scraper_api_key: str | None = Field(None, alias="mcpScraperApiKey", description="The identity's mcp-scraper API key, stored encrypted, used to reach mcp-scraper tools during scheduled-action execution.")


class SetScheduleEntitlementOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the entitlement was set; false on auth/scope error.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
