from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class PostMessageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str = Field(..., alias="vault", description="The channel (vault) to post to.")
    content: str = Field(..., alias="content", description="The message text.")
    attach_note: dict[str, Any] | None = Field(None, alias="attachNote", description="Attach one of your own notes to this message, auto-shared with every current channel member. Optional.")


class PostMessageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True when the message was posted; false on auth/scope error.")
    message_id: str | None = Field(None, alias="messageId", description="Path-style identifier for this message: use it as parentMessageId on reply-message, or messageId on react-message.")
    posted_at: str | None = Field(None, alias="postedAt", description="ISO-8601 timestamp the message was posted.")
    attached_note: dict[str, Any] | None = Field(None, alias="attachedNote", description="Present when attachNote was given and the share succeeded.")
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
