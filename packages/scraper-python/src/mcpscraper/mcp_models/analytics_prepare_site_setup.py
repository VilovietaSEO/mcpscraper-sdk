from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsPrepareSiteSetupInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Authorized Analytics Site id returned by analytics_list_sites.")
    start_url: str = Field(..., alias="startUrl", description="Public same-origin URL from which X-Ray discovers bounded routes and rendering surfaces.")
    goal: str | None = Field(None, alias="goal", description="Plain-language customer outcome to measure; do not paste credentials, source code, form contents, or visitor data.")
    business_model: Literal['saas', 'lead_generation', 'ecommerce'] | None = Field(None, alias="businessModel", description="Optional user-confirmed model; omit to receive an evidence-backed recommendation.")
    scope: Literal['same_origin', 'sitemap'] | None = Field(None, alias="scope", description="Bounded route discovery scope; neither mode authorizes third-party crawling.")
    max_pages: int | None = Field(None, alias="maxPages", description="Maximum pages inspected under the X-Ray entitlement; this consumes zero MCP Scraper Credits.")
    pixel_id: str | None = Field(None, alias="pixelId", description="Optional existing Pixel belonging to the Site; omit to let the service resolve the canonical Pixel.")
    consent_mode: Literal['required', 'granted_test', 'unknown'] | None = Field(None, alias="consentMode", description="Consent expectation for non-delivering discovery. It never grants a visitor consent choice.")


class AnalyticsPrepareSiteSetupOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    operation: str = Field(..., alias="operation", description="")
    setup: dict[str, Any] = Field(..., alias="setup", description="")
    next_action: str = Field(..., alias="nextAction", description="Exactly one safe next user or system action based on the current durable state.")
    billing_receipt: dict[str, Any] = Field(..., alias="billingReceipt", description="")
