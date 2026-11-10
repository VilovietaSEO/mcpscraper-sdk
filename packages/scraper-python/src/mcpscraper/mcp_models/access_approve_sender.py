from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AccessApproveSenderInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    sender_identity: str = Field(..., alias="senderIdentity", description="Identity (email or user id) to approve as a sender.")


class AccessApproveSenderOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True on success; false on auth error.")
    sender: str | None = Field(None, alias="sender", description="The identity that was approved.")
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
