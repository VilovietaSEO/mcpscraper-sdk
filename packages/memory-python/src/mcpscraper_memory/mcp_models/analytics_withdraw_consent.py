from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsWithdrawConsentInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    subject_ref: str = Field(..., alias="subjectRef", description="Opaque consent subject reference returned by consent coverage or a safe journey. MCP cannot grant visitor consent.")
    occurred_at: str | None = Field(None, alias="occurredAt", description="Optional visitor-reported withdrawal time; defaults to server time.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.")


class AnalyticsWithdrawConsentOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    receipt: dict[str, Any] | None = Field(None, alias="receipt", description="")
    downstream: dict[str, Any] | None = Field(None, alias="downstream", description="")
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
