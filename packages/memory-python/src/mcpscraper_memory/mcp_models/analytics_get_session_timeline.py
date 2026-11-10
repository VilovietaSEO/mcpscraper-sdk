from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsGetSessionTimelineInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    reference: str = Field(..., alias="reference", description="Opaque Site-scoped reference returned by an X-Ray read. Raw visitor, session, device, email, phone, IP, and identity hashes are never accepted.")
    from_: str | None = Field(None, alias="from", description="Inclusive ISO time. Defaults to 90 days before to; max window 366 days.")
    to: str | None = Field(None, alias="to", description="Exclusive ISO time. Defaults to now; max window 366 days.")


class AnalyticsGetSessionTimelineOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    data: dict[str, Any] | None = Field(None, alias="data", description="")
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
