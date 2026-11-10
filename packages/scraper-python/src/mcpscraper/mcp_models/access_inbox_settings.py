from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AccessInboxSettingsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    allow_unapproved_senders: bool = Field(..., alias="allowUnapprovedSenders", description="Set true to accept invites/shares from anyone; false to require approval.")


class AccessInboxSettingsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True on success; false on auth error.")
    allow_unapproved_senders: bool | None = Field(None, alias="allowUnapprovedSenders", description="The setting now in effect.")
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
