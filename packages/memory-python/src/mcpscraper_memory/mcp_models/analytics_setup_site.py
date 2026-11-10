from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsSetupSiteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str | None = Field(None, alias="siteId", description="Authorized Analytics Site id. Supply siteId or startUrl on the first call.")
    start_url: str | None = Field(None, alias="startUrl", description="Public same-origin URL to set up. Supply only when siteId is not yet known.")
    goal: str | None = Field(None, alias="goal", description="Plain-language customer outcome to measure; do not paste credentials, source code, form contents, or visitor data.")
    setup_id: str | None = Field(None, alias="setupId", description="Reuse to continue an existing durable setup after approval, deployment, or reconnecting.")
    revision: int | None = Field(None, alias="revision", description="Exact current setup revision. Reload stale revisions before any mutation or canary.")
    business_model: Literal['saas', 'lead_generation', 'ecommerce'] | None = Field(None, alias="businessModel", description="Optional explicit business model; omit to infer it from bounded site evidence.")
    goal_action: Literal['continue', 'prepare', 'apply', 'verify', 'first_answers'] | None = Field(None, alias="goalAction", description="Desired lifecycle step. Continue lets the façade select the single safe next operation from durable state.")
    authority: dict[str, Any] | None = Field(None, alias="authority", description="Source authority or ownership context supporting this content.")
    idempotency_key: str | None = Field(None, alias="idempotencyKey", description="Required only for apply or canary-capable verify; reuse for the exact same intent after an unknown result.")


class AnalyticsSetupSiteOutput(BaseModel):
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
