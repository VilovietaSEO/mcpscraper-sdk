from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsApplySiteSetupInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Authorized Analytics Site id owning the setup.")
    setup_id: str = Field(..., alias="setupId", description="Durable owner-bound setup id returned by an X-Ray setup operation; it is not a browser session id.")
    revision: int = Field(..., alias="revision", description="Exact current setup revision. Reload stale revisions before any mutation or canary.")
    confirmed: bool = Field(..., alias="confirmed", description="Confirms publishing this exact measurement manifest to the installed X-Ray tag runtime. This does not activate an experiment.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsApplySiteSetupOutput(BaseModel):
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
