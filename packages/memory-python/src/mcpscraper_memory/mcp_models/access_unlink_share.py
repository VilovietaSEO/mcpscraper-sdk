from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AccessUnlinkShareInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    share_id: str = Field(..., alias="shareId", description="The shareId to unlink from your \"Shared with me\" notes.")


class AccessUnlinkShareOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True on success; false on auth/scope/lookup error.")
    share_id: str | None = Field(None, alias="shareId", description="The unlinked share.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
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
