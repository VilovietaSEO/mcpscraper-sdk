from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class ReactMessageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str = Field(..., alias="vault", description="The channel (vault) the message is in.")
    message_id: str = Field(..., alias="messageId", description="The message or reply to react to (from post-message, reply-message, or list-channel-messages).")
    emoji: str = Field(..., alias="emoji", description="The emoji to add or remove, e.g. \"👍\".")
    remove: bool | None = Field(None, alias="remove", description="Set true to remove a reaction you previously added. Default false (add).")


class ReactMessageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True on success; false on auth/scope error.")
    message_id: str | None = Field(None, alias="messageId", description="The message reacted to.")
    emoji: str | None = Field(None, alias="emoji", description="The emoji applied or removed.")
    removed: bool | None = Field(None, alias="removed", description="True if this call removed a reaction; false if it added one.")
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
