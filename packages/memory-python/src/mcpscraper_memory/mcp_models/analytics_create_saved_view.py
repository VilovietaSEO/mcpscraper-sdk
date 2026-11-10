from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsCreateSavedViewInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    name: str = Field(..., alias="name", description="Saved report name.")
    settings: dict[str, Any] = Field(..., alias="settings", description="Complete versioned report settings validated by the same canonical parser as REST and exports.")
    is_default: bool | None = Field(None, alias="isDefault", description="Make this the operator default for the report family.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.")


class AnalyticsCreateSavedViewOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    view: dict[str, Any] | None = Field(None, alias="view", description="")
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
