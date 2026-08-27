from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsCreateConnectionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    provider: Literal['callrail', 'calltrackingmetrics', 'twilio', 'hubspot', 'highlevel', 'generic_crm'] = Field(..., alias="provider", description="Supported phone, CRM, or advertising provider for this governed connection.")
    name: str = Field(..., alias="name", description="Human-readable name for the record being created or updated.")
    source_account_ref: str = Field(..., alias="sourceAccountRef", description="Stable non-secret account identifier at the phone, CRM, or event source.")
    service_connection_ref: str | None = Field(None, alias="serviceConnectionRef", description="Optional MCP Scraper connected-service identifier used for governed provider actions.")
    webhook_secret: str | None = Field(None, alias="webhookSecret", description="Provider webhook validation secret; it is encrypted at rest and never returned.")
    config: dict[str, Any] | None = Field(None, alias="config", description="Validated renderer configuration for the new immutable template version; arbitrary code is rejected.")


class AnalyticsCreateConnectionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
