from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ReplyMessageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str = Field(..., alias="vault", description="The channel (vault) the parent message is in.")
    parent_message_id: str = Field(..., alias="parentMessageId", description="The top-level message to reply under (messageId from post-message or list-channel-messages).")
    content: str = Field(..., alias="content", description="The reply text.")
    attach_note: dict[str, Any] | None = Field(None, alias="attachNote", description="Attach one of your own notes to this reply, auto-shared with every current channel member. Optional.")


class ReplyMessageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the reply was posted; false on auth/scope/lookup error.")
    message_id: str | None = Field(None, alias="messageId", description="Path-style identifier for this reply (e.g. for react-message).")
    posted_at: str | None = Field(None, alias="postedAt", description="ISO-8601 timestamp the reply was posted.")
    attached_note: dict[str, Any] | None = Field(None, alias="attachedNote", description="Present when attachNote was given and the share succeeded.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
