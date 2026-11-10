from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsExportPrivacySubjectInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    subject_ref: str = Field(..., alias="subjectRef", description="Opaque Site-scoped reference returned by an X-Ray read. Raw visitor, session, device, email, phone, IP, and identity hashes are never accepted.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.")


class AnalyticsExportPrivacySubjectOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    export: dict[str, Any] | None = Field(None, alias="export", description="")
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
