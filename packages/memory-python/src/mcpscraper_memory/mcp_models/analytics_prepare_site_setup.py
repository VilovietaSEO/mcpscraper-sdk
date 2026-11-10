from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


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

    ok: bool | None = Field(None, alias="ok", description="")
    operation: str | None = Field(None, alias="operation", description="")
    setup: dict[str, Any] | None = Field(None, alias="setup", description="")
    next_action: str | None = Field(None, alias="nextAction", description="Exactly one safe next user or system action based on the current durable state.")
    billing_receipt: dict[str, Any] | None = Field(None, alias="billingReceipt", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
